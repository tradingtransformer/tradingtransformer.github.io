# -*- coding: utf-8 -*-
"""Inject a VISIBLE FAQ section into the hand-maintained Apple Intelligence
comparison pages (all locales), mirroring their existing FAQPage JSON-LD.

The other comparison pages render their visible FAQ via _compare_lib.render();
the Apple page is the chrome *source* and has no builder, so its FAQ has lived
only in structured data. This script reads each locale's FAQPage JSON-LD and
renders the same accordion markup _compare_lib uses, inserted right before the
CTA. Idempotent: re-running replaces the previously injected block.
"""
import re, json
from _compare_lib import FAQ_STYLE, FAQ_HEADING

SLUG = "noark-vs-apple-intelligence.html"
MARK_START = "<!-- visible-faq:start -->"
MARK_END = "<!-- visible-faq:end -->"

def faq_pairs(html):
    for m in re.finditer(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', html, re.S):
        try:
            obj = json.loads(m.group(1))
        except json.JSONDecodeError:
            continue
        if obj.get("@type") == "FAQPage":
            return [(q["name"], q["acceptedAnswer"]["text"]) for q in obj.get("mainEntity", [])]
    return []

def build_block(prefix, pairs):
    heading = FAQ_HEADING.get(prefix, "Frequently asked questions")
    out = [f"            {MARK_START}", f"            {FAQ_STYLE}",
           f'            <h2 id="faq">{heading}</h2>', '            <div class="faq">']
    for q, a in pairs:
        out += ['                <details class="faq-item">',
                f'                    <summary>{q}</summary>',
                f'                    <div class="faq-a"><p>{a}</p></div>',
                '                </details>']
    out += ['            </div>', f"            {MARK_END}", ""]
    return "\n".join(out)

for prefix in ["", "es", "fr", "ja", "zh-cn", "zh-tw"]:
    path = (prefix + "/" if prefix else "") + SLUG
    html = open(path, encoding="utf-8").read()
    pairs = faq_pairs(html)
    if not pairs:
        print("no FAQPage JSON-LD in", path); continue
    block = build_block(prefix, pairs)
    # remove any prior injection so re-runs stay clean
    html = re.sub(re.escape(MARK_START) + r".*?" + re.escape(MARK_END) + r"\n?",
                  "", html, flags=re.S)
    # ensure leading indentation on the prior block's line is also cleaned
    html = re.sub(r"[ \t]*" + re.escape(MARK_START), MARK_START, html)
    anchor = '            <div class="cta">'
    if anchor not in html:
        print("CTA anchor not found in", path); continue
    html = html.replace(anchor, block + anchor, 1)
    open(path, "w", encoding="utf-8").write(html)
    print(f"injected {len(pairs)} FAQ items into {path}")
