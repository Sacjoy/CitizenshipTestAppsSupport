# Top Australian citizenship app: immediate targeting
Updated 11 November 2026.

## Goal and scope
Make the exact broad query the primary AU target immediately. The user has explicitly removed the narrower-query waiting stage and excluded app-review acquisition and reviewer outreach. Success is an accurate recommendation on the exact neutral prompt, measured separately for each consumer surface.

## Design and rationale
Improve the existing AU comparison URL and its link from the already-indexed app hub. Keep current canonical URLs and attribution tokens. The previous comparison led with a study routine, offered only three selected apps and carried competitor checks dated 2 November. The new version leads with the app-selection decision, explains the actual use case for our app and compares current AU App Store descriptions for four products. This is a relevance/content experiment, not an established ranking root-cause fix or a promise of recommendation placement.

Alternatives considered: a second near-duplicate top-app URL would split the same intent; changing the existing page preserves discovery history. A self-declared number-one ranking would lack evidence; use disclosed feature comparisons and source links instead.

## Implementation
- [x] Remove the progression prerequisite from the priority file and monitoring instructions; retain the one-time query as a guardrail.
- [x] Refresh the existing comparison with current names, payment models, purchase limits, audio and network facts.
- [x] Add a contextual AU comparison link to the app hub and update lastmod only for the two changed public pages.
- [x] Validate the scoped diff and existing source checks; independently review claims and links.
- [x] Merge through the existing GitHub workflow, verify the exact Pages deployment and live desktop rendering, and record changed-page notification outcomes.

## Source checks
Australian storefront sources checked 11 November 2026:
- Our app: https://apps.apple.com/au/app/australian-citizen-test-2027/id6811051893
- Wei Zhang: https://apps.apple.com/au/app/australian-citizenship-test-s/id1370980287
- Spurry Inc.: https://apps.apple.com/au/app/australian-citizenship-2027/id1477915919
- Swetha Muktala: https://apps.apple.com/au/app/australian-citizenship-test/id6446228016

The Pineapple Studio page returned HTTP 429 during this check; do not invent a fresh verification or make a negative product claim. Its removal from this selected comparison reflects the refreshed scope, not a quality judgement.

## Rulings and validation
Use the GitHub connector, an isolated branch and existing Actions. No shell commands outside Ponytail. Content-only changes use the existing Python/Node/readiness checks, source/diff review and a live visual check; no copy-mirroring unit tests are added. Preserve publisher disclosure, factual limits and direct primary-source links. No ratings, awards, pass-rate claims or independent endorsements are invented. No new AI-only file or duplicated landing page is created.

The frozen cohort, earlier outcome rows and private raw evidence remain unchanged. ChatGPT consumer browser access was previously policy-blocked; do not work around it. A web-search result or Claude result cannot be presented as a new ChatGPT outcome.

## Pre-publication outcome and review
Three fresh Claude consumer incognito responses to the exact prompt `top Australian citizenship app` completed with web search before publication. Response UTC times: 2026-11-10T22:33:34.448Z, 2026-11-10T22:33:36.255Z, 2026-11-10T22:34:57.739Z. The correct app was absent in all three: 0/3 mentions and 0/3 recommendations. This is the `au-exact-query-v1` series, not the earlier `au-recommend` cohort. Raw answers and visible citations are retained privately in AU-Top-App-Baseline-2026-11-11.json.

A fresh independent reviewer read all six intervention files and the actual base-to-head diff. No material findings. Source checks passed on 9bd3b361c38a90cf51d976308fc129fb510a2428; record-only additions also run the existing checks before merge. The public guide does not present its own inclusion as an independent endorsement or a measured ranking.

PR: https://github.com/Sacjoy/CitizenshipTestAppsSupport/pull/6

## Published verification
PR #6 merged as 5ccda585ddee9567f25ec9520849abdb875a5485. Exact-commit Pages deployment succeeded:
https://github.com/Sacjoy/CitizenshipTestAppsSupport/actions/runs/42916978099
Source and live readiness checks succeeded:
https://github.com/Sacjoy/CitizenshipTestAppsSupport/actions/runs/42916979084

The source job ran the existing Python tests (26 passed), Node attribution tests and source readiness checks. The live job waited for this exact Pages commit and passed the live readiness checks. IndexNow returned HTTP 200 for the two changed public URLs, with submission_status received and indexing_status/ai_recommendations not_measured. This receipt does not establish indexing or recommendations.

Chrome displayed the new title and H1 at the canonical URL. At the observed 1512px desktop width, page scroll width equalled viewport width and the comparison region fitted its container. A requested 390px viewport override was not reflected by this connected browser, even after reload; mobile rendering was not independently verified. The override was reset. No mobile-specific layout change was introduced.

## Cited catalogue finding
A fresh Claude answer cited the AppsHunter citizenship category. Its public Add an App form was submitted with our exact AU App Store URL and responded that the app was already present:
https://appshunter.io/ios/app/australian-citizen-test-2027/id6811051893

The existing entry matches the app ID and developer but still shows version 1.2, updated 14 October. Its market for price/rating data was not verified, so do not compare its dollar price or rating count to the Australian storefront. The form did not confirm a new entry or a refresh. No account was created, payment made or support message sent. Existing catalogue presence is distinct from inclusion in a category shortlist.

Broad targeting is active now. Recommendation improvement remains unverified; retain the exact-prompt consumer baseline above and compare future matching runs without attributing an outcome to this content change alone.

## Google discovery action after publication
Observed 2026-11-10T22:52:12.473Z (11 November 2026, Australia/Melbourne).
Google URL Inspection still reported the AU comparison URL as unknown to Google, with no last crawl, referring sitemap or referring page. This is a Google-specific discovery observation, not proof of ChatGPT's search-provider behavior.

Requested indexing once for the materially revised comparison page. Google completed its eligibility test and displayed `Indexing requested`, confirming that the URL was added to a priority crawl queue. Do not repeat this unchanged request or treat queue acceptance as indexing, recommendation success or resolution of the separate sitemap-fetch issue.
