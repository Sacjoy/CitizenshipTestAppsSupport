"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const { classifySource, attributeLink } = require("../../assets/attribution.js");
const au = "https://apps.apple.com/au/app/australian-citizen-test-2027/id6811051893?pt=129443273&ct=au_support_2026&mt=8";
test("uses only known AI referral hosts and explicit source tags", () => {
  assert.equal(classifySource("https://example.org/?utm_source=chatgpt.com", ""), "chatgpt");
  assert.equal(classifySource("https://example.org/", "https://www.perplexity.ai/search/test"), "perplexity");
  assert.equal(classifySource("https://example.org/", "https://claude.ai/chat/test"), "claude");
  assert.equal(classifySource("https://example.org/", "https://gemini.google.com/app/test"), "gemini");
});
test("does not mistake ordinary search, malformed URLs or lookalike domains for AI", () => {
  for (const ref of ["", "not-a-url", "https://google.com/search?q=app", "https://bing.com/search?q=app", "https://chatgpt.com.evil.example/", "https://evil.example/?next=chatgpt.com"]) {
    assert.equal(classifySource("https://example.org/", ref), null);
  }
  assert.equal(classifySource("bad", "bad"), null);
});
test("falls back to a verified referrer when a tag is unknown", () => {
  assert.equal(classifySource("https://example.org/?utm_source=newsletter", "https://chatgpt.com/"), "chatgpt");
});
test("keeps app identity, provider token, media type and unrelated parameters", () => {
  const output = new URL(attributeLink(au + "&custom=x#info", "support", "chatgpt"));
  assert.equal(output.pathname, new URL(au).pathname);
  assert.equal(output.searchParams.get("pt"), "129443273");
  assert.equal(output.searchParams.get("mt"), "8");
  assert.equal(output.searchParams.get("custom"), "x");
  assert.equal(output.searchParams.get("ct"), "au_support_chatgpt_26");
  assert.equal(output.hash, "#info");
});
test("does not label unknown origins, competitors or other developers", () => {
  assert.equal(attributeLink(au, "support", null), au);
  for (const href of ["https://example.org/", au.replace("6811051893", "99999999"), au.replace("129443273", "123"), au.replace("apps.apple.com", "apps.apple.com.evil.example"), "not-a-url"]) {
    assert.equal(attributeLink(href, "support", "chatgpt"), href);
  }
  assert.equal(attributeLink(au, "support", "invented"), au);
  assert.equal(attributeLink(au, "invented", "chatgpt"), au);
});
test("maps all three separate apps and respects Apple's 30-character token limit", () => {
  for (const [id,country] of [["6811051893","au"],["6811515364","ca"],["6811575732","uk"]]) {
    for (const page of ["support","guide","hub","reviewkit"]) {
      for (const source of ["chatgpt","claude","perplexity","gemini"]) {
        const token = new URL(attributeLink(au.replace("6811051893",id),page,source)).searchParams.get("ct");
        assert.equal(token, country+"_"+page+"_"+source+"_26");
        assert.ok(token.length <= 30);
      }
    }
  }
});
