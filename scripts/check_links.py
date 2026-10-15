#!/usr/bin/env python3
"""Check source/website HTTP reachability; never infer operational safety."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]

def check(url):
    try:
        req = Request(url, headers={'User-Agent': 'Awesome-ZecFi-LinkCheck/1.0 (+https://github.com/Milbaxter/awesome-zecfi)'})
        with urlopen(req, timeout=18) as response:
            response.read(1024)
            return {'url': url, 'http_status': response.status, 'final_url': response.url, 'result': 'reachable'}
    except HTTPError as error:
        return {'url': url, 'http_status': error.code, 'result': 'http-error', 'note': 'May be access protection; manual review required.'}
    except (URLError, TimeoutError, OSError) as error:
        return {'url': url, 'http_status': None, 'result': 'unresolved', 'note': str(error)[:220]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='data/link-health.json')
    parser.add_argument('--workers', type=int, default=8)
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/projects.json').read_text())
    urls = sorted({url for entry in data['entries'] for url in [entry['website'], *[s['url'] for s in entry['sources']]]})
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 12))) as pool:
        results = list(pool.map(check, urls))
    report = {'checked_at': datetime.now(timezone.utc).isoformat(),
              'meaning': 'HTTP reachability only. A 200 response is not proof of an active service; failure is not proof of closure.',
              'results': results}
    (ROOT / args.output).write_text(json.dumps(report, indent=2) + '\n')
    ok = sum(r['result'] == 'reachable' for r in results)
    print(f'{ok}/{len(results)} URLs reachable; {len(results)-ok} need manual review.')
    for row in results:
        if row['result'] != 'reachable':
            print(row['http_status'], row['url'], row.get('note', ''))

if __name__ == '__main__':
    main()
