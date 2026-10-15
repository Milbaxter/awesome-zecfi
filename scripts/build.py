#!/usr/bin/env python3
"""Deterministically generate the awesome list and detailed catalog from JSON."""
import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- DIRECTORY:START -->', '<!-- DIRECTORY:END -->'

def render(data):
    entries, categories = data['entries'], data['categories']
    counts = Counter(e['category'] for e in entries)
    lines = [f"**{len(entries)} entries · {len(categories)} categories · reviewed {data['as_of']}**", '', '## Contents', '']
    for cat in categories:
        lines.append(f"- [{cat['title']}](#{cat['id']}) ({counts[cat['id']]})")
    detail = ['# Detailed ZecFi directory', '', f"Snapshot: **{data['as_of']}**. [Method and status definitions](methodology.md) · [Awesome list](../README.md)", '',
              'Descriptions summarize publisher documentation. Review focuses are editorial questions, not completed security assessments. Network tags describe relevance, not a certified list of live deployments.', '']
    for cat in categories:
        lines += ['', f'<a id="{cat["id"]}"></a>', f"## {cat['title']}", '']
        detail += [f"## {cat['title']}", '']
        for e in sorted((e for e in entries if e['category']==cat['id']), key=lambda e:e['name'].casefold()):
            labels = [e['evidence']] if e['evidence'] != 'direct-source' else []
            if e['lifecycle'] not in {'unverified', 'not-applicable'}:
                labels.append(e['lifecycle'])
            badges = ''.join(f' `{label}`' for label in labels)
            lines.append(f"- [{e['name']}]({e['website']}) — {e['description']}{badges} · [Details & sources](docs/directory.md#{e['id']}).")
            detail += [f'<a id="{e["id"]}"></a>', f"### {e['name']}", '',
                f"**Type:** {e['kind']} · **Networks:** {', '.join(e['networks'])} · **Reviewed:** {e['last_reviewed']}", '',
                f"**Evidence:** `{e['evidence']}` · **Lifecycle:** `{e['lifecycle']}`", '',
                e['description'], '',
                f"- **Zcash mechanism:** {e['zcash_mechanism']}",
                f"- **Review focus:** {e['review_focus']}",
                f"- **Evidence and availability qualification:** {e['review_note']}",
                f"- **Project/resource:** [{e['name']}]({e['website']})"]
            for i,s in enumerate(e['sources'],1):
                detail.append(f"- **Source {i}:** [{s.get('title', 'Primary source' if s['type']=='primary' else 'Source')}]({s['url']}) — {s['type']}; reviewed {s['checked']}.")
            detail.append('')
    return '\n'.join(lines).rstrip()+'\n', '\n'.join(detail).rstrip()+'\n'

def render_browse(data):
    entries=data['entries']
    lines=['# Browse Awesome ZecFi', '', '[Awesome list](../README.md) · [Ways to use ZecFi](ways-to-use-zecfi.md) · [Evidence coverage](coverage.md)', '',
           'Browse directly on GitHub. Network tags show ecosystem relevance, not a verified deployment list. An entry can appear under several networks.', '',
           '- [By network](#by-network)', '- [By evidence](#by-evidence)', '- [By lifecycle](#by-lifecycle)', '- [By entry type](#by-entry-type)', '']
    for heading, field in [('By network','networks'),('By evidence','evidence'),('By lifecycle','lifecycle'),('By entry type','kind')]:
        lines += [f'## {heading}', '', 'Expand a group to browse its entries.', '']
        values=sorted({v for e in entries for v in (e[field] if field=='networks' else [e[field]])},key=str.casefold)
        for value in values:
            group=[e for e in entries if value in e[field]] if field=='networks' else [e for e in entries if e[field]==value]
            lines += ['<details>', f'<summary>{value} ({len(group)})</summary>', '']
            for e in sorted(group,key=lambda e:e['name'].casefold()):
                lines.append(f"- [{e['name']}](directory.md#{e['id']}) — {e['description']}")
            lines += ['', '</details>', '']
        lines.append('')
    return '\n'.join(lines).rstrip()+'\n'

def render_coverage(data):
    entries=data['entries']
    single=[e for e in entries if len(e['sources'])==1]
    website_only=[e for e in entries if {s['url'] for s in e['sources']}=={e['website']}]
    lines=['# Evidence coverage and review queue', '', f"Snapshot: **{data['as_of']}** · [Method](methodology.md) · [Browse](browse.md) · [Material changes](research-notes.md)", '',
           'Generated from the dataset. Counts describe research coverage, not project quality or safety. Several sources from one publisher are not independent corroboration.', '',
           '| Measure | Count |', '| --- | ---: |', f'| Total entries | {len(entries)} |', f'| Entries with one cited source | {len(single)} |',
           f'| Entries citing only their listed website/resource URL | {len(website_only)} |']
    for value,count in sorted(Counter(e['evidence'] for e in entries).items()):
        lines.append(f'| Evidence: {value} | {count} |')
    lines += ['', 'A website/resource URL can be a technical document or repository, so the URL-only count is a triage signal, not a claim that all those sources are marketing pages.', '',
              '## Entries needing stronger direct evidence', '', '| Entry | Evidence | Specific unresolved point |', '| --- | --- | --- |']
    for e in entries:
        if e['evidence']!='direct-source':
            lines.append(f"| [{e['name']}](directory.md#{e['id']}) | {e['evidence']} | {e['review_note']} |")
    lines += ['', '## Coverage still missing', '',
              'Deeper coverage is still needed for exchange-by-exchange shielded deposit and withdrawal support, Ironwood support in each wallet and payment tool, additional ZEC venues on Solana and NEAR, and regional regulated access. The list also lacks a systematic deployment-by-deployment audit and incident history. These gaps remain open; entry count is not a measure of completeness.', '',
              '## Next review priorities', '',
              '1. Resolve the ecosystem-only and code-only entries above with dated product documentation.',
              '2. Recheck redemptions, changed strategies, closures and permissioned bridge roles.',
              '3. Add deployment-specific audit scope and incident/recovery sources where independently verified.',
              '4. Review the HTTP failures in [link health](../data/link-health.json), without inferring closure from access errors.']
    return '\n'.join(lines).rstrip()+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'data/projects.json').read_text())
    listing, detail=render(data)
    readme=(ROOT/'README.md').read_text()
    if readme.count(START)!=1 or readme.count(END)!=1:
        raise SystemExit('README needs one start marker and one end marker.')
    before, rest=readme.split(START)
    _, after=rest.split(END)
    outputs={ROOT/'README.md':before+START+'\n\n'+listing+'\n'+END+after,ROOT/'docs/directory.md':detail,
             ROOT/'docs/browse.md':render_browse(data),ROOT/'docs/coverage.md':render_coverage(data)}
    for path, content in outputs.items():
        if args.check:
            if not path.exists() or path.read_text()!=content:
                raise SystemExit(f'Out of date: {path.relative_to(ROOT)}; run scripts/build.py')
        else:
            path.write_text(content)
    print('Generated files match.' if args.check else f"Generated {len(data['entries'])} entries.")

if __name__=='__main__':
    main()
