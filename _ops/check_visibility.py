"""Crawl-readiness checks, not an indexing or recommendation score. Python stdlib only."""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree as ET

NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
BOTS = ('Googlebot', 'bingbot', 'OAI-SearchBot', 'Claude-SearchBot')


def sitemap_errors(xml, text, base, required):
    errors = []
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as exc:
        return ['Invalid XML: '+str(exc)]
    if root.tag != NS+'urlset':
        errors.append('Invalid sitemap namespace or root')
    for entry in root:
        locations = entry.findall(NS+'loc')
        if entry.tag != NS+'url' or len(locations) != 1 or not (locations[0].text or '').strip():
            errors.append('Each sitemap URL entry needs exactly one nonempty loc')
    urls = [(node.text or '').strip() for node in root.findall(NS+'url/'+NS+'loc')]
    lines = text.splitlines()
    if not urls:
        errors.append('Empty XML sitemap')
    if len(urls) != len(set(urls)):
        errors.append('Duplicate XML URLs')
    if len(lines) != len(set(lines)):
        errors.append('Duplicate text URLs')
    if set(urls) != set(lines):
        errors.append('XML and text sitemaps differ')
    for url in urls + lines:
        if not url.startswith(base) or urlsplit(url).fragment or any(c.isspace() for c in url):
            errors.append('Invalid or out-of-scope URL: '+url)
    for url in required:
        if url not in urls:
            errors.append('Required URL missing: '+url)
    return errors


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals, self.robots, self.title = [], [], []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'link' and 'canonical' in (attrs.get('rel') or '').lower().split():
            self.canonicals.append(attrs.get('href'))
        if tag == 'meta' and (attrs.get('name') or '').lower() in ('robots', 'googlebot', 'bingbot'):
            self.robots.append(attrs.get('content') or '')

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


def page_errors(html, expected, status, final_url, headers):
    errors = []
    headers = {k.lower(): v for k, v in headers.items()}
    if status != 200:
        errors.append(f'HTTP status {status}')
    if final_url != expected:
        errors.append('Redirected to '+final_url)
    if headers.get('content-type') and 'text/html' not in headers['content-type'].lower():
        errors.append('Not served as HTML')
    page = Page()
    page.feed(html)
    if not ''.join(page.title).strip():
        errors.append('Missing title')
    if page.canonicals != [expected]:
        errors.append('Canonical must equal '+expected)
    for directive in page.robots + [headers.get('x-robots-tag', '')]:
        if re.search(r'\b(noindex|none)\b', directive, flags=re.I):
            errors.append('Indexing blocked by directive: '+directive)
    return errors


def robots_errors(body, status, urls, final_url=None, expected_url=None):
    if expected_url and final_url != expected_url:
        return ['robots.txt redirected; manual review required: '+str(final_url)]
    if status in (404, 410):
        return []
    if status != 200:
        return [f'robots.txt unavailable: HTTP {status}']
    if re.search(r'<(?:!doctype|html|head|body)\b', body, re.I):
        return ['robots.txt returned HTML; manual review required']
    # stdlib does not implement crawler wildcard/end-anchor precedence. Fail
    # explicitly instead of reporting a potentially blocked URL as crawlable.
    for line in body.splitlines():
        directive = line.split('#', 1)[0].strip()
        if re.match(r'(?i)(allow|disallow)\s*:', directive) and re.search(r'[*$]', directive):
            return ['robots.txt wildcard/end-anchor rules require manual review']
    parser = RobotFileParser()
    parser.parse(body.splitlines())
    return [f'{bot} blocked: {url}' for bot in BOTS for url in urls if not parser.can_fetch(bot, url)]


def fetch(url):
    request = Request(url, headers={'User-Agent': 'MentionRise-ReadinessCheck/1.0'})
    try:
        response = urlopen(request, timeout=20)
    except HTTPError as exc:
        response = exc
    with response:
        return (response.read().decode('utf-8'), response.status,
                response.geturl(), dict(response.headers))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--report', default='visibility-report.json')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    config = json.loads((root/'_ops/visibility.json').read_text())
    base = config['base_url']
    required = [urljoin(base, path) for path in config['required_paths']]
    results = []

    def record(target, errors, **details):
        results.append(dict(target=target, passed=not errors, errors=errors, **details))
        print(('FAIL ' if errors else 'PASS ')+target+(': '+'; '.join(errors) if errors else ''))

    xml = (root/'sitemap.xml').read_text(encoding='utf-8')
    text = (root/'sitemap.txt').read_text(encoding='utf-8') if (root/'sitemap.txt').exists() else ''
    record('source sitemaps', sitemap_errors(xml, text, base, required))
    if args.live:
        fetched = {}
        for name in ('sitemap.xml', 'sitemap.txt'):
            url = urljoin(base, name)
            try:
                body, status, final, headers = fetch(url)
                errors = []
                if status != 200 or final != url:
                    errors.append(f'Expected direct HTTP 200; got {status} at {final}')
                expected = xml if name.endswith('.xml') else text
                if body != expected:
                    errors.append('Deployed sitemap differs from checked-out source')
                record(url, errors, status=status)
                if status == 200 and final == url:
                    fetched[name] = body
            except Exception as exc:
                record(url, [f'{type(exc).__name__}: {exc}'])
        if len(fetched) == 2:
            record('deployed sitemap agreement', sitemap_errors(fetched['sitemap.xml'], fetched['sitemap.txt'], base, required))
        # Check every listed URL, including existing USA support; no content changes.
        urls = sorted(set(required + text.splitlines()))
        for url in urls:
            try:
                body, status, final, headers = fetch(url)
                record(url, page_errors(body, url, status, final, headers), status=status)
            except Exception as exc:
                record(url, [f'{type(exc).__name__}: {exc}'])
        robots_url = urljoin(base, '/robots.txt')
        try:
            body, status, final, _ = fetch(robots_url)
            record(robots_url, robots_errors(body, status, urls, final, robots_url), status=status)
        except Exception as exc:
            record(robots_url, [f'{type(exc).__name__}: {exc}'])
    else:
        for url in required:
            relative = url[len(base):] or 'index.html'
            target = root/relative
            exists = target.is_file() or target.with_suffix('.md').is_file()
            record(url, [] if exists else ['Missing source page'])
    report = dict(checked_at=datetime.now(timezone.utc).isoformat(),
                  mode='live' if args.live else 'source',
                  indexing_status='not_measured', ai_recommendations='not_measured',
                  passed=all(row['passed'] for row in results), checks=results)
    Path(args.report).write_text(json.dumps(report, indent=2)+'\n')
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
