/* Identifies visible referral signals only. No cookies, storage, requests or user IDs. */
(function () {
  "use strict";
  const hosts = {"chatgpt.com":"chatgpt","chat.openai.com":"chatgpt","claude.ai":"claude","perplexity.ai":"perplexity","gemini.google.com":"gemini"};
  const tags = Object.assign({chatgpt:"chatgpt",claude:"claude",perplexity:"perplexity",gemini:"gemini"}, hosts);
  const apps = {"6811051893":"au","6811515364":"ca","6811575732":"uk"};
  function classifySource(pageURL, referrer) {
    try {
      const tag = new URL(pageURL).searchParams.get("utm_source");
      if (tag && Object.hasOwn(tags, tag.toLowerCase())) return tags[tag.toLowerCase()];
    } catch (_) {}
    try {
      const host = new URL(referrer).hostname.toLowerCase();
      for (const domain of Object.keys(hosts)) {
        if (host === domain || host.endsWith("." + domain)) return hosts[domain];
      }
    } catch (_) {}
    return null;
  }
  function attributeLink(href, page, source) {
    if (!["support","guide","hub","reviewkit"].includes(page) || !["chatgpt","claude","perplexity","gemini"].includes(source)) return href;
    try {
      const url = new URL(href);
      const match = url.pathname.match(/\/id(\d+)$/);
      if (url.protocol !== "https:" || url.hostname !== "apps.apple.com" || !match || !apps[match[1]] || url.searchParams.get("pt") !== "129443273") return href;
      url.searchParams.set("ct", apps[match[1]] + "_" + page + "_" + source + "_26");
      return url.toString();
    } catch (_) { return href; }
  }
  if (typeof module !== "undefined" && module.exports) module.exports = {classifySource, attributeLink};
  if (typeof document !== "undefined") {
    const source = classifySource(window.location.href, document.referrer);
    const page = document.body.dataset.campaignPage;
    document.querySelectorAll('a[href^="https://apps.apple.com/"]').forEach(function (link) {
      link.href = attributeLink(link.href, page, source);
    });
  }
}());
