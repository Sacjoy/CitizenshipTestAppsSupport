import unittest
from _ops.check_visibility import sitemap_errors, page_errors, robots_errors

BASE = 'https://example.com/app/'
URL = BASE + 'support.html'
XML = f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}</loc></url><url><loc>{URL}</loc></url></urlset>'
HTML = f'<html><head><title>App support</title><link rel="canonical" href="{URL}"></head><body>Support</body></html>'


class VisibilityTests(unittest.TestCase):
    def test_valid_pair(self):
        self.assertEqual([], sitemap_errors(XML, BASE+'\n'+URL+'\n', BASE, [BASE, URL]))

    def test_missing_required_homepage(self):
        xml = XML.replace(f'<url><loc>{BASE}</loc></url>', '')
        self.assertIn('Required URL missing: '+BASE, sitemap_errors(xml, URL+'\n', BASE, [BASE, URL]))

    def test_malformed_or_wrong_namespace(self):
        for xml in ['<urlset>', XML.replace('http://www.sitemaps.org/schemas/sitemap/0.9', 'wrong')]:
            with self.subTest(xml=xml):
                self.assertTrue(sitemap_errors(xml, URL, BASE, [URL]))

    def test_text_mismatch_and_duplicates(self):
        self.assertIn('XML and text sitemaps differ', sitemap_errors(XML, URL+'\n', BASE, [URL]))
        self.assertIn('Duplicate text URLs', sitemap_errors(XML, BASE+'\n'+URL+'\n'+URL, BASE, [URL]))

    def test_out_of_scope_and_fragments(self):
        for url in ['http://example.com/app/x', 'https://example.com/application/x', URL+'#x']:
            xml = XML.replace(URL, url)
            with self.subTest(url=url):
                self.assertTrue(sitemap_errors(xml, BASE+'\n'+url, BASE, [BASE]))

    def test_valid_page(self):
        self.assertEqual([], page_errors(HTML, URL, 200, URL, {'Content-Type':'text/html'}))

    def test_redirect_and_bad_status(self):
        self.assertIn('HTTP status 404', page_errors(HTML, URL, 404, URL, {}))
        self.assertIn('Redirected to '+BASE, page_errors(HTML, URL, 200, BASE, {}))

    def test_bad_or_duplicate_canonical(self):
        self.assertIn('Canonical must equal '+URL, page_errors(HTML.replace(URL, BASE), URL, 200, URL, {}))
        self.assertTrue(page_errors(HTML.replace('</head>', f'<link rel="canonical" href="{URL}"></head>'), URL, 200, URL, {}))

    def test_missing_title_and_wrong_content_type(self):
        self.assertTrue(page_errors(HTML.replace('<title>App support</title>', ''), URL, 200, URL, {}))
        self.assertTrue(page_errors(HTML, URL, 200, URL, {'Content-Type':'application/json'}))

    def test_blocking_directives(self):
        for directive in ['noindex', 'none']:
            for name in ['robots', 'googlebot', 'bingbot']:
                with self.subTest(name=name, directive=directive):
                    html = HTML.replace('</head>', f'<meta name="{name}" content="{directive}"></head>')
                    self.assertTrue(page_errors(html, URL, 200, URL, {}))
        self.assertTrue(page_errors(HTML, URL, 200, URL, {'X-Robots-Tag':'googlebot: noindex'}))

    def test_robots_404_allows_but_server_error_fails(self):
        self.assertEqual([], robots_errors('', 404, [URL]))
        self.assertTrue(robots_errors('', 503, [URL]))

    def test_robots_disallow(self):
        self.assertTrue(robots_errors('User-agent: *\nDisallow: /app/', 200, [URL]))
        self.assertEqual([], robots_errors('User-agent: *\nDisallow: /private/', 200, [URL]))

    def test_robots_wildcards_require_manual_review(self):
        for directive in ['Disallow: /*support.html', 'Disallow: /app/support.html$']:
            self.assertTrue(robots_errors('User-agent: *\n'+directive, 200, [URL]))

    def test_robots_html_is_not_a_pass(self):
        self.assertTrue(robots_errors('<html><title>Oops</title></html>', 200, [URL]))

    def test_robots_redirect_requires_review(self):
        self.assertTrue(robots_errors('', 200, [URL], final_url=BASE, expected_url='https://example.com/robots.txt'))

    def test_sitemap_rejects_missing_and_multiple_locations(self):
        for entry in ['<url/>', '<url><loc/></url>', f'<url><loc>{URL}</loc><loc>{URL}</loc></url>']:
            xml = XML.replace('</urlset>', entry+'</urlset>')
            self.assertTrue(sitemap_errors(xml, BASE+'\n'+URL, BASE, [BASE, URL]))


if __name__ == '__main__':
    unittest.main()
