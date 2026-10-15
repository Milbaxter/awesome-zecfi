#!/usr/bin/env python3
"""Validate required evidence, data integrity and generated Markdown links."""
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE={'direct-source','ecosystem-only','code-only'}
LIFECYCLES={'unverified','mainnet-announced','testnet','research','changed','deprecated','discontinued','not-applicable'}
FIELDS={'id','name','category','website','networks','kind','description','zcash_mechanism','review_focus','evidence','lifecycle','review_note','sources','last_reviewed'}

def require(condition,message):
    if not condition: raise ValueError(message)

def valid_url(value):
    parts=urlsplit(value)
    return parts.scheme=='https' and bool(parts.netloc) and not parts.username and not parts.password and not any(c.isspace() for c in value)

def markdown_anchors(content):
    """Resolve explicit anchors and the plain Markdown headings used by this repo."""
    anchors=set(re.findall(r'<a\s+id="([^"]+)"',content))
    counts={}
    for heading in re.findall(r'^#{1,6}\s+(.+)$',content,re.MULTILINE):
        slug=re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-')
        number=counts.get(slug,0)
        counts[slug]=number+1
        anchors.add(f'{slug}-{number}' if number else slug)
    return anchors

def main():
    data=json.loads((ROOT/'data/projects.json').read_text())
    require(data['schema_version']==2,'Unsupported schema version')
    snapshot=date.fromisoformat(data['as_of'])
    require(snapshot<=date.today(),'Future research date')
    categories=[c['id'] for c in data['categories']]
    require(len(categories)==len(set(categories)),'Duplicate category')
    ids,names=set(),set()
    for e in data['entries']:
        require(set(e)==FIELDS,f"Unexpected/missing fields: {e.get('name')}")
        require(all(isinstance(e[k],str) and e[k].strip() for k in FIELDS-{'networks','sources'}),f"Empty/non-text field: {e.get('name')}")
        require(re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['id']),f"Invalid ID: {e['id']}")
        require(e['id'] not in ids and e['name'].casefold() not in names,f"Duplicate: {e['name']}")
        ids.add(e['id']); names.add(e['name'].casefold())
        require(e['category'] in categories,f"Unknown category: {e['name']}")
        require(e['evidence'] in EVIDENCE,f"Unknown evidence: {e['name']}")
        require(e['lifecycle'] in LIFECYCLES,f"Unknown lifecycle: {e['name']}")
        require(valid_url(e['website']),f"Invalid URL: {e['name']}")
        require(isinstance(e['networks'],list) and e['networks'] and all(isinstance(n,str) and n.strip() for n in e['networks']),f"Invalid networks: {e['name']}")
        require(len(set(e['networks']))==len(e['networks']),f"Duplicate network: {e['name']}")
        require(date.fromisoformat(e['last_reviewed'])<=snapshot,f"Invalid review date: {e['name']}")
        require(isinstance(e['sources'],list) and e['sources'],f"No evidence: {e['name']}")
        require(any(s['type']=='primary' for s in e['sources']),f"No primary evidence: {e['name']}")
        require(len({s['url'] for s in e['sources']})==len(e['sources']),f"Duplicate source: {e['name']}")
        for s in e['sources']:
            require(valid_url(s['url']) and s['type'] in {'primary','secondary'},f"Invalid source: {e['name']}")
            require(date.fromisoformat(s['checked'])<=date.fromisoformat(e['last_reviewed']),f"Invalid source date: {e['name']}")
    for category in categories:
        require(any(e['category']==category for e in data['entries']),f'Empty category: {category}')
    subprocess.run([sys.executable,str(ROOT/'scripts/build.py'),'--check'],check=True)
    for path in ROOT.rglob('*.md'):
        content=path.read_text()
        for match in re.finditer(r'\]\(([^)]+)\)',content):
            target=match.group(1)
            if urlsplit(target).scheme: continue
            filepart,_,fragment=target.partition('#')
            dest=(path.parent/unquote(filepart)).resolve() if filepart else path.resolve()
            require(dest.is_relative_to(ROOT),f'Link escapes repo: {path.name}: {target}')
            require(dest.exists(),f'Broken local link: {path.name}: {target}')
            if fragment and dest.suffix=='.md':
                require(unquote(fragment) in markdown_anchors(dest.read_text()),f'Missing Markdown anchor: {path.name}: {target}')
    print(f"Validated {len(ids)} unique entries, dated sources, categories and local links.")

if __name__=='__main__':
    main()
