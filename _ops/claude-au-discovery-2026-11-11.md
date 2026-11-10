# AU Claude discovery check: 11 November 2026

The AU recommendation goal remains open. No site or listing change was made by these tests.

## Eligible neutral measurements

- Cohort: `citizenship-consumer-9-v1`, prompt `au-recommend`, three predeclared repetitions.
- Exact prompt: Which Australian citizenship test apps would you recommend for iPhone? Search the web and cite your sources.
- Surface: Claude consumer web; displayed model Sonnet 5.5 High; English; Australian app target.
- Every repetition used a separate fresh incognito conversation. The UI says these chats stay out of memory and history. Explicit location settings were not verified or changed.
- Web search ran and each answer completed.
- Prompt/response UTC times: 1: 2026-11-10T20:37:01.144Z / 2026-11-10T20:37:19.947Z; 2: 2026-11-10T20:37:44.333Z / 2026-11-10T20:37:59.666Z; 3: 2026-11-10T20:38:00.494Z / 2026-11-10T20:38:18.466Z.
- Result: 0/3 correct-app mentions, 0/3 owned-page citations, 0/3 recommendations. Accuracy is not applicable because the app is absent. These are same-day correlated observations of one prompt, not a full nine-prompt cohort or market-wide estimate.
- In repetition 1, the expanded app-search results showed 17 links. None matched App Store ID 6811051893 or an owned page. This establishes only absence from that visible result list, not every internal retrieval stage.

## Separate branded diagnostic

At 2026-11-10T20:38:28Z, a fresh incognito query gave the exact app title and developer but no URL. Claude searched the title and developer and reported no matching listing or developer site.

A follow-up at 2026-11-10T20:39:12Z supplied these two public URLs:
- https://apps.apple.com/au/app/australian-citizen-test-2027/id6811051893
- https://sacjoy.github.io/CanadaPrepSupport/australia-support.html

Claude retrieved both and identified the app, developer, two free mock tests and one-time Lifetime Access. URL-supplied retrieval is excluded from neutral recommendation rates.

The response also reported version 1.2 and no ratings, whereas the live AU listing checked on this date showed version 1.3 and two ratings. Stale retrieved content or interpretation is possible; the mechanism is unconfirmed. Direct retrieval success does not prove fresh indexing.

## Supported interpretation

The immediate observed gap is search discovery. Successful direct retrieval rules out a blanket inability to access these two URLs in this session. It does not establish the search provider used, its indexing status, why retrieval missed the listing, or that ratings are the sole cause. Google's separately observed indexing delay must not be presented as a proven explanation for Claude.

The AU App Store Developer Website link is now live and resolves to the correct marketing page. Additional metadata or another iOS build is not an established remedy for the observed search gap.

Exact answers, visible citations and UI evidence are retained privately in `AU-Claude-Visibility-Evidence-2026-11-11.json`; public logs contain only measurement summaries. No private chat URLs or account details are published.

Next intervention: qualify relevant catalogue coverage and independent product evaluations, then compare the same fixed neutral prompts. Catalogue inclusion is not an editorial endorsement or a guaranteed recommendation.

## Catalogue check

AppAgg already has a matching AU listing at https://appagg.com/ios/education/australian-citizen-test-2027-44323866.html?hl=en, identifying the developer and current app title. Its visible version remains 1.2. Its rating and price fields are not labelled as AU, so they must not be compared to the Australian storefront as if identical. Existing catalogue inclusion alone has not produced inclusion in the three observed Claude answers.

A refresh was attempted through AppAgg's Add/Update form with the AU App Store URL. The site required sign-in before accepting the request. No refresh confirmation was received and no new account was created. Refresh status: blocked pending authentication. No outreach messages were sent.
