#!/usr/bin/env python3
"""Search the directory without network access or dependencies."""
import argparse
import json
from pathlib import Path

def main():
    root=Path(__file__).resolve().parents[1]
    data=json.loads((root/'data/projects.json').read_text())
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query',nargs='?',default='')
    parser.add_argument('--category',choices=[c['id'] for c in data['categories']])
    parser.add_argument('--evidence',choices=sorted({e['evidence'] for e in data['entries']}))
    parser.add_argument('--lifecycle',choices=sorted({e['lifecycle'] for e in data['entries']}))
    parser.add_argument('--network',help='Case-insensitive exact network tag, e.g. Zcash, NEAR or Solana')
    parser.add_argument('--json',action='store_true')
    args=parser.parse_args()
    result=[]
    for e in data['entries']:
        if any(getattr(args,k) and e[k]!=getattr(args,k) for k in ('category','evidence','lifecycle')): continue
        if args.network and args.network.casefold() not in [n.casefold() for n in e['networks']]: continue
        searchable=' '.join([e['name'],e['kind'],e['category'],e['description'],e['zcash_mechanism'],e['review_focus'],e['review_note'],*e['networks']]).casefold()
        if not all(term in searchable for term in args.query.casefold().split()): continue
        result.append(e)
    if args.json:
        print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print(f'{len(result)} result(s)')
        for e in result:
            print(f"\n{e['name']} [evidence: {e['evidence']}; lifecycle: {e['lifecycle']}] — {', '.join(e['networks'])}\n{e['description']}\n{e['website']}")

if __name__=='__main__':
    main()
