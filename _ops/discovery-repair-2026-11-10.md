# Citizenship product discovery repairs
**Goal:** Make the three verified live apps unambiguous and accessible at their established URLs; detect future availability failures without a code push.
**Architecture:** Keep static GitHub Pages and existing canonical URLs. Replace the UK Markdown/theme wrapper with standalone HTML. Keep all support and privacy links. Add factual product summaries and WebPage metadata linking the published app identity to its regional App Store URL.
**Spec:** User request to fix all citizenship app discovery. The three live App Store IDs verified are AU 6811051893, CA 6811515364, UK 6811575732. USA support exists but no live Apple listing was verified; do not invent one.

## Constraints and review focus
- No invented ratings, endorsements, ranking claims, features or recommendation guarantees.
- Existing privacy and purchase help must remain reachable.
- UK must retain exactly the same public support URL and one primary H1.
- Canonical URL, download link and app identifier must agree.
- App Store names, free limits, purchase model and minimum OS must match verified listings.
- Structured data describes the page and app identity; no copied ratings or promise of rich results.
- Scheduled checks measure HTTP/crawl readiness, not Google indexing or AI recommendations.

## Work
- [x] Improve AU/CA headings and add concise product facts and page metadata.
- [x] Replace UK support.md with support.html, preserving its help content.
- [x] Add publisher identity and linked product collection metadata to the main hub.
- [x] Add change-scoped IndexNow notifications after successful deployment, with ownership-file verification and honest 200/202 status reporting. Never submit on the six-hour schedule.
- [x] Run existing source tests and add a six-hour live schedule to both repositories.
- [x] Review isolated branches, merge, verify exact deployed commits and live pages.
- [x] Inspect Google/Bing status and submit changed URLs where supported.
- [x] Check App Store Marketing URL fields after account sign-in.

## Rulings
Use GitHub connector branches and existing Actions for execution; do not run shell commands outside Ponytail.
These reversible static content/config changes use existing source/live checks and direct output inspection rather than adding tests that merely duplicate the page copy.
Do not change sitemaps merely to reset submission dates; current ingestion failure remains separately tracked.

## Execution evidence
- Both original static branches passed all existing source checks.
- Eight notification behavior tests failed as expected before implementation; the existing 18 tests passed in each repository.
- Scope addition: Bing live fetch succeeded while its index reported discovered but not crawled; automate changed-page notifications instead of relying solely on manual retries.
- Reviewer found two minor presentation issues. Fixed capitalization and moved paid product facts outside the free-access region before publication.

## Release verification
- Main PR #2 merged as 7fc2dcebd86112134a3961562aec64ce4338589b; Canada PR #2 merged as bedaf61fd897de3f5ab0aedc3b3ad95c79389405.
- All 26 tests pass in each repository. Both exact-commit Pages deployments and live readiness checks passed.
- IndexNow returned HTTP 202 for the main hub and UK support, and separately for AU/CA support. This means key validation pending, not indexing.
- Australian App Store Support URL was the separate AustraliaPrepSupport homepage. That page still used the old 2026 brand and had no link to the current product page. Commit 89877dd8659b9758dda13faf33e98d907412d3d2 adds an instant meta refresh and canonical to the current AU page, retains fallback contact help, and updates the old brand. Deployment succeeded; browser navigation confirmed the final target.
- Current Google request outcomes: UK accepted; Canada explicitly rejected with daily quota exceeded. Further Google retries stopped. This does not establish the cause of older failures.
- Google sitemap ingestion remains separately unresolved. No claim of improved ranking or AI recommendations is made.

## Follow-up release metadata
The three released App Store versions have empty Marketing URL fields; those fields are disabled in the released-version UI. Use app-store-links.json for the next editable App Store release. AU's existing Support URL now works through the repaired legacy entry point; no new app version was created merely to work around locked metadata.

## Review and operating limits
Independent review found no critical/important defects. The two static-content findings were fixed. The remaining minor test gap is lack of isolated main() tests; this release exercised the actual push entrypoint through successful deployed key verification and real API responses. The six-hour monitor checks crawl readiness, not indexing or recommendation success. It notifies only on changed-page pushes and intentionally does not notify repeatedly on the schedule.

## Google sitemap investigation follow-up, 10 November 2026

Status: sitemap processing remains unresolved. Do not mark this closed from a submission receipt or from a successful URL Inspection live test.

- Google's own live tests at 11:08:07 Australia/Melbourne successfully fetched both existing sitemap.xml URLs. Each response was HTTP 200 OK with Content-Type application/xml, crawl allowed Yes and indexing allowed Yes. Google's tested source contained the current seven main-site URLs and three CanadaPrepSupport URLs. The inspection crawler was Google Inspection Tool smartphone.
- Both verified properties reported No issues detected under Manual actions and Security issues. Root robots.txt returning 404 is not a crawl block. The directory-level properties do not expose root Crawl stats or robots history, so historical host failures and crawl demand remain unconfirmed.
- Re-submitted the same tested XML URLs once after the live tests. Google accepted both submissions. The Sitemaps report still showed Unknown, Couldn't fetch and zero discovered pages, with no last-read value in the table. No more specific fetch error was exposed. Submission is not processing success.
- The main app hub is already indexed. Its recorded Googlebot smartphone crawl was 2 November 2026 at 15:12:06 Australia/Melbourne, with successful fetch, crawling/indexing allowed and the intended canonical selected. A refresh request for the updated hub was also accepted into the priority crawl queue. This does not prove the newly published country pages are indexed.
- AU australia-support.html, CA support.html and UK uk/support.html each still reported URL is unknown to Google before the requests. All three now received Indexing requested confirmations stating that they were added to a priority crawl queue. This supersedes the earlier Canada daily-quota rejection above. Queue acceptance is not indexing.

The reproducible failure is the sitemap-processing report; a current file-serving, XML, robots or manual-action defect was not reproduced. A stale/transient processing result or low crawl demand remains a hypothesis, not a proven cause. Do not rename valid sitemaps, change accurate lastmod dates, add ineffective directory-level robots.txt files, or repeat accepted URL requests to manufacture a green status.

For the next scheduled outcome check, inspect sitemap status and the three canonical country URLs separately. Close sitemap ingestion only when Google reports Success with the expected discovered URLs (7 main, 3 CanadaPrepSupport). Close each page's indexing item only when URL Inspection confirms it is indexed with the correct canonical. If the live fetch fails later, use the specific response error to identify the repair.

Official troubleshooting reference: https://support.google.com/webmasters/answer/7451001
