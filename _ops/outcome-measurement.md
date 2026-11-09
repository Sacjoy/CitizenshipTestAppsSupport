# Citizenship search outcome measurement
Updated 10 November 2026.

## Keep four measurements separate
1. Readiness: existing six-hour workflow checks live HTTP responses, canonicals, robots and sitemap membership. This is not an index or recommendation check.
2. Discovery: record Google URL Inspection, sitemap processing and Bing URL status for each of the three support pages and three guides. A submission or IndexNow 202 does not mean indexed.
3. Answers: use the frozen answer-prompts.json cohort. Record consumer UI and API results separately, with model, locale, date, exact prompt and repetition. Do not use this planning conversation as an unprompted discovery result.
4. Conversion: Apple Analytics Campaigns, using generated provider token 129443273. Report product-page views, first-time downloads and proceeds when available. These are Apple metrics, not raw website click counts.

## Answer protocol
Use a fresh conversation for each prompt. Do not name the app, paste our URLs, provide fact sheets or ask for a favourable result in a neutral run. Run three repetitions per prompt per surface, ideally repeated on another day. Do not switch models mid-cohort. If the surface is unavailable, login is required, a rate limit occurs or search cannot run, record blocked with a reason; exclude it from answer-rate denominators.
Preserve exact prompt and response evidence privately, with visible citation URLs. Public logs may contain scores and public-source URLs, never account details, private chat IDs, keys or user content.

Score independently:
- Mention: unambiguous correct app identity, matched by developer or App Store ID where names overlap.
- Citation: a clickable citation to one of our support, guide or reviewer pages.
- Recommendation: a positive choice/shortlist for the user's need, not a mere mention or warning.
- Accuracy: audit country, developer, iOS minimum, two-free-mock limit, one-time purchase, paid features, audio/network limits and government independence against the product pages. Unknown facts are not silently counted as correct.
- Accurate recommendation: recommendation with no material false claim and correct app identity.
- Rate: successes / completed neutral runs, separately for each country, surface, model and prompt set. Show counts as well as percentages. Accuracy is not applicable when the app is absent; zero eligible answers gives null, not 0% accuracy.

A useful release signal is at least two accurate recommendations out of three runs of the same neutral prompt, repeated on another day on at least one target surface. This is an internal checkpoint, not a prediction of market-wide visibility. Existing AU-30-v2 history is unchanged.

## Apple campaign map
Static fallback tokens: {au,ca,uk}_{support,guide,hub,reviewkit}_2026.
Recognised AI referral tokens: {au,ca,uk}_{support,guide,hub,reviewkit}_{chatgpt,claude,perplexity,gemini}_26.
The source comes only from a recognised referring hostname or an explicit known utm_source value. These observable signals can be omitted or forged and are not proof of causal influence. No source means default website token. Google/Bing search referrers are not assumed to be AI. The script stores nothing and sends no events. Attribution covers the current landing page only: following an internal link can lose the original AI source, so these campaign totals undercount journeys that continue through other pages.
Apple campaign links use the same developer provider token across all three apps, as documented by Apple. First-time downloads follow Apple's attribution window, not a direct website click counter. Direct App Store visits and unidentifiable referrals remain unclassified.
https://developer.apple.com/help/app-store-connect-analytics/acquisition/campaign-links/
Apple generally requires at least five qualifying users and 24 hours before a campaign becomes visible. Store "not enough data" or "not available", not zero, when withheld. Never report the pre-existing total app installs as AI-attributed installs.
Campaign metrics at setup: not enough data. Historical Claude exploratory answers observed 10 November: the target app was absent in each country; those single runs are not a completed new-cohort benchmark.

## Google
Consult the current Generative AI performance report guidance:
https://support.google.com/webmasters/answer/16984139
Report availability can depend on impressions. Its absence does not prove zero AI visibility. Keep ordinary Web performance and any available Generative AI report separate and label coverage. Do not infer consumer Gemini performance from Search Console.

## Next check
Run the fixed cohort after deployment and on the next day when access permits. Then compare the same cohort weekly. Check source accuracy after each app release and refresh screenshots when the listing changes. App Store Marketing URLs remain queued in app-store-links.json until an editable release exists.
