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
- [ ] Validate the scoped diff and existing source checks; independently review claims and links.
- [ ] Merge through the existing GitHub workflow, verify the exact Pages deployment and live rendering, and record changed-page notification outcomes.

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
