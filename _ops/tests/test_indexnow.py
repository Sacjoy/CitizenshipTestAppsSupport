"""Behavior checks for change-scoped IndexNow notifications."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://example.com/apps/'
KEY = 'test-ownership-key-123456'
URLS = [BASE, BASE+'uk/support.html', BASE+'au.html']

class Response:
    def __init__(self, body=b'', status=200, url=''):
        self.body, self.status, self.url = body, status, url
    def read(self): return self.body
    def geturl(self): return self.url
    def __enter__(self): return self
    def __exit__(self, *args): pass

class IndexNowTests(unittest.TestCase):
    def setUp(self):
        path = ROOT/'notify_indexnow.py'
        self.assertTrue(path.is_file(), 'IndexNow notifier has not been implemented')
        spec = importlib.util.spec_from_file_location('notify_indexnow', path)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    def test_only_changed_sitemap_pages_are_notified(self):
        self.assertEqual(self.module.changed_urls(
            ['index.html', 'uk/support.md', 'uk/support.html',
             '_ops/README.md', 'sitemap.xml', 'unlisted.html'],
            BASE, URLS), [BASE, BASE+'uk/support.html'])

    def test_privacy_index_markdown_maps_to_directory(self):
        self.assertEqual(self.module.changed_urls(
            ['uk/index.md'], BASE, [BASE+'uk/']), [BASE+'uk/'])

    def test_project_key_location_and_app_urls_are_kept(self):
        self.assertEqual(self.module.make_payload(BASE, KEY, [BASE+'au.html']), {
            'host':'example.com', 'key':KEY,
            'keyLocation':BASE+'indexnow-key.txt', 'urlList':[BASE+'au.html']})

    def test_foreign_host_and_sibling_project_are_rejected(self):
        for url in ['https://other.example/apps/au.html',
                    'https://example.com/other/au.html',
                    BASE+'../other.html', BASE+'au.html#section']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                self.module.make_payload(BASE, KEY, [url])

    def test_invalid_key_and_empty_batch_are_rejected(self):
        for key, urls in [('short', URLS), ('bad key value', URLS), (KEY, [])]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.module.make_payload(BASE, key, urls)

    def test_notification_posts_only_after_matching_live_key(self):
        payload = self.module.make_payload(BASE, KEY, [BASE+'au.html'])
        requests = []
        def transport(request, timeout):
            requests.append(request)
            if len(requests)==1:
                return Response(KEY.encode(), url=BASE+'indexnow-key.txt')
            self.assertEqual(request.full_url, 'https://api.indexnow.org/indexnow')
            self.assertEqual(request.get_method(), 'POST')
            self.assertEqual(json.loads(request.data), payload)
            return Response(status=202, url=request.full_url)
        result = self.module.notify(payload, transport)
        self.assertEqual(len(requests), 2)
        self.assertEqual(result['submission_status'], 'key_validation_pending')
        self.assertEqual(result['indexing_status'], 'not_measured')

    def test_wrong_or_redirected_key_prevents_notification(self):
        payload = self.module.make_payload(BASE, KEY, [BASE+'au.html'])
        for body, url in [(b'wrong', BASE+'indexnow-key.txt'),
                          (KEY.encode(), 'https://other.example/key.txt')]:
            requests = []
            def transport(request, timeout):
                requests.append(request)
                return Response(body, url=url)
            with self.subTest(url=url), self.assertRaises(ValueError):
                self.module.notify(payload, transport)
            self.assertEqual(len(requests), 1)

    def test_rejected_notification_is_not_reported_as_success(self):
        payload = self.module.make_payload(BASE, KEY, [BASE+'au.html'])
        requests = []
        def transport(request, timeout):
            requests.append(request)
            if len(requests)==1:
                return Response(KEY.encode(), url=BASE+'indexnow-key.txt')
            return Response(status=429, url=request.full_url)
        with self.assertRaises(RuntimeError):
            self.module.notify(payload, transport)

if __name__ == '__main__':
    unittest.main()
