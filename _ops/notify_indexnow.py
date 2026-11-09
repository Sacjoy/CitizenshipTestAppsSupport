"""Notify IndexNow of changed, currently published sitemap pages after a verified deploy."""
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen

ENDPOINT = 'https://api.indexnow.org/indexnow'


def changed_urls(paths, base, allowed):
    allowed = set(allowed)
    urls = set()
    for path in paths:
        parts = PurePosixPath(path).parts
        if not parts or any(p.startswith(('.', '_')) for p in parts):
            continue
        if not path.endswith(('.html', '.md')):
            continue
        if path.endswith('.md'):
            path = path[:-3]+'.html'
        if path == 'index.html':
            path = ''
        elif path.endswith('/index.html'):
            path = path[:-10]
        url = urljoin(base, path)
        if url in allowed:
            urls.add(url)
    return sorted(urls)


def make_payload(base, key, urls):
    origin = urlsplit(base)
    if (origin.scheme != 'https' or not origin.hostname or origin.username or
            origin.password or origin.port or not base.endswith('/') or
            origin.query or origin.fragment):
        raise ValueError('Expected an HTTPS project base URL ending in /')
    if not re.fullmatch(r'[A-Za-z0-9-]{8,128}', key):
        raise ValueError('Invalid IndexNow ownership key')
    urls = sorted(set(urls))
    if not 1 <= len(urls) <= 10000:
        raise ValueError('Expected 1 to 10000 changed URLs')
    for url in urls:
        parsed = urlsplit(url)
        decoded = unquote(parsed.path)
        if (not url.startswith(base) or parsed.scheme != origin.scheme or
                parsed.netloc != origin.netloc or parsed.fragment or parsed.query or
                any(c.isspace() for c in url) or
                any(part in ('.', '..') for part in decoded.split('/'))):
            raise ValueError('URL outside this project or not canonical: '+url)
    return dict(host=origin.hostname, key=key,
                keyLocation=urljoin(base, 'indexnow-key.txt'), urlList=urls)


def notify(payload, transport=urlopen):
    # A response from the key URL must contain this exact deployed key.
    # Do not send a notification if the new deployment is missing the file.
    request = Request(payload['keyLocation'], headers={'User-Agent':'MentionRise-IndexNow/1.0'})
    with transport(request, timeout=20) as response:
        if (response.status != 200 or response.geturl() != payload['keyLocation'] or
                response.read().decode('utf-8').strip() != payload['key']):
            raise ValueError('Deployed IndexNow key is missing, redirected or incorrect')
    request = Request(ENDPOINT, data=json.dumps(payload).encode('utf-8'), method='POST',
                      headers={'Content-Type':'application/json; charset=utf-8',
                               'User-Agent':'MentionRise-IndexNow/1.0'})
    with transport(request, timeout=20) as response:
        status = response.status
    if status not in (200, 202):
        raise RuntimeError('IndexNow rejected notification: HTTP '+str(status))
    return dict(http_status=status, url_count=len(payload['urlList']),
                submission_status='received' if status == 200 else 'key_validation_pending',
                indexing_status='not_measured', ai_recommendations='not_measured')


def main():
    root = Path(__file__).resolve().parents[1]
    report_path = root/'indexnow-report.json'
    if os.environ.get('GITHUB_EVENT_NAME') != 'push':
        print('IndexNow skipped: only changed-page push deployments send notifications')
        return 0
    try:
        event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
        before, after = event.get('before', ''), os.environ.get('GITHUB_SHA', '')
        if (not all(re.fullmatch(r'[0-9a-f]{40}', sha) for sha in (before, after))
                or before == '0'*40):
            raise ValueError('Cannot identify the deployed push change range')
        paths = subprocess.run(
            ['git', 'diff', '--name-only', '--no-renames', before, after, '--'],
            cwd=root, check=True, capture_output=True, text=True).stdout.splitlines()
        base = json.loads((root/'_ops/visibility.json').read_text())['base_url']
        urls = changed_urls(paths, base, (root/'sitemap.txt').read_text().splitlines())
        if not urls:
            report = dict(submission_status='skipped_no_changed_pages', urls=[],
                          indexing_status='not_measured', ai_recommendations='not_measured')
        else:
            key = (root/'indexnow-key.txt').read_text().strip()
            report = notify(make_payload(base, key, urls))
            report['urls'] = urls
        report_path.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(report))
        return 0
    except Exception as exc:
        report = dict(submission_status='failed', error=str(exc),
                      indexing_status='not_measured', ai_recommendations='not_measured')
        report_path.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(report))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
