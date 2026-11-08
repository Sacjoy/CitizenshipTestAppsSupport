# Visibility operations

Run `python3 -m unittest discover -s _ops/tests -v` and `python3 _ops/check_visibility.py` before publishing. After Pages deploys, run `python3 _ops/check_visibility.py --live` or the **Visibility readiness** Actions workflow manually. It also runs automatically after a successful **pages build and deployment** workflow.

Source mode validates XML/text agreement, required page coverage and source-file existence. Live mode checks both deployed sitemaps against source, every listed page's HTTP status, redirects, title, canonical, robots metadata/headers, and root robots.txt. Results are saved as `visibility-report.json`; Actions keeps the report for 30 days. Failed requests fail the run. A 404/410 robots.txt means no file, not blocked crawling. Robots redirects or wildcard/end-anchor rules deliberately fail for manual review because Python's built-in parser cannot reliably evaluate those rules. This is a conservative check for these small sites, not a full crawler emulator.

The text sitemap is a diagnostic alternative for Google's existing XML fetch failure, supported by Google's sitemap documentation. Keep it identical to the XML URL set. Do not change lastmod unless the page actually changed.

## Evidence before paid launch

1. **Published:** live readiness passes. This establishes technical availability only.
2. **Discovered/indexed:** record Google Search Console and Bing URL Inspection results per support page and guide, including timestamp, last crawl and selected canonical. A submission confirmation is not indexing.
3. **Recommended:** use unchanged unbranded prompts, the same provider/model/search setting, fresh conversations and a fixed country/language. Record the full response, citations, app ID and timestamp. Run three independent trials per prompt; errors/timeouts are invalid, never negative answers. Separate branded recognition from unbranded recommendations. Never mix API and consumer-chat results in one comparison.
4. **Commercial result:** measure actual referred visits and conversions using consent-appropriate analytics. Recommendations alone do not establish revenue.

Pilot release criterion: all three priority support pages and three guides technically available and confirmed indexed, plus unbranded recommendations containing the correct app identity in at least two of three trials, repeated on a second day, for each app on at least one target assistant. This is an internal evidence threshold, not a customer guarantee. Do not advertise results across all assistants unless each is measured.

If live checks pass but a search engine does not crawl: inspect that engine's fetch/discovery report. If indexed but absent from recommendations: inspect cited competitors and original source coverage; do not keep resubmitting unchanged URLs. Preserve failures and changes, not just successful answers. External editorial coverage and customer reviews must be genuine. Do not fabricate reviews, rankings, or independent endorsements.

## Repair record

- Initial confirmed defect: CanadaPrepSupport homepage omitted from XML sitemap. Corrected and covered by required_paths.
- Both original XML files were publicly reachable; Google's earlier report still said Couldn't fetch. The exact cause of Google's failure is unproven. Text submission tests an alternate format; it does not establish a ranking fix.
- Regression tests reproduced missing homepage and absent text sitemap before repair. Validator tests exercise errors rather than assuming a deployment proves indexing.
- Independent review found two robots false-success paths and incomplete sitemap-entry validation. All reproduced before correction. Unsupported robots syntax now requires review instead of a green result. Sitemap validation was treated as required because silently ignored malformed entries would invalidate the readiness report.
