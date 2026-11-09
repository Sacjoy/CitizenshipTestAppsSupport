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
- [ ] Improve AU/CA headings and add concise product facts and page metadata.
- [ ] Replace UK support.md with support.html, preserving its help content.
- [ ] Add publisher identity and linked product collection metadata to the main hub.
- [ ] Add change-scoped IndexNow notifications after successful deployment, with ownership-file verification and honest 200/202 status reporting. Never submit on the six-hour schedule.
- [ ] Run existing source tests and add a six-hour live schedule to both repositories.
- [ ] Review isolated branches, merge, verify exact deployed commits and live pages.
- [ ] Inspect Google/Bing status and submit changed URLs where supported.
- [ ] Check App Store Marketing URL fields after account sign-in.

## Rulings
Use GitHub connector branches and existing Actions for execution; do not run shell commands outside Ponytail.
These reversible static content/config changes use existing source/live checks and direct output inspection rather than adding tests that merely duplicate the page copy.
Do not change sitemaps merely to reset submission dates; current ingestion failure remains separately tracked.

## Execution evidence
- Both original static branches passed all existing source checks.
- Eight notification behavior tests failed as expected before implementation; the existing 18 tests passed in each repository.
- Scope addition: Bing live fetch succeeded while its index reported discovered but not crawled; automate changed-page notifications instead of relying solely on manual retries.
- Reviewer found two minor presentation issues. Fixed capitalization and moved paid product facts outside the free-access region before publication.
