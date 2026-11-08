# Visibility repair implementation plan

Goal: repair sitemap coverage and make crawl-readiness failures observable before and after deployment.

Scope: the two existing GitHub Pages support sites. Keep existing page URLs, content, verification files and hosting. A successful HTTP check is not proof of indexing or AI recommendations.

1. Add a regression check for the missing CanadaPrepSupport homepage. Add UTF-8 text sitemaps generated from each XML sitemap, with identical URL sets, as a controlled Google fetch diagnostic.
2. Add a dependency-free validator and tests. Validate sitemap namespace, absolute in-scope URLs, duplicates, required pages and XML/text agreement. Check deployed status, redirects, HTML title, canonical, robots directives and robots.txt access. Treat unavailable checks as failures, not zero visibility.
3. Run source checks on pushes and pull requests. Run live checks after successful Pages deployments and on manual dispatch. Preserve a JSON report in Actions. No credentials or scheduled paid requests required.
4. Review the changes independently, deploy, verify public responses, then submit the new sitemaps to Google and refresh Bing once. Request indexing for previously unrequested support pages.
5. Record submission results separately from indexing and recommendation outcomes. Keep paid-launch evidence gate closed until measured outcomes support the service claim.

Review focus: malformed XML, redirects to error pages, scoped robots directives, stale deployed content, omitted URLs, false success on network errors.

Execution: work on isolated fresh clones and branches. User requested immediate repair; proceed through implementation and deployment within that scope.
