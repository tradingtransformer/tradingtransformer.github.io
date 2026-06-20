# -*- coding: utf-8 -*-
"""Wrap mentor names in Wikipedia links on every homepage (all locales):
  - the "Ask the wisest people in history" cards (6), and
  - the educational mentor-table (~38).

Links point to each locale's own-language Wikipedia (en/es/fr/ja + shared zh for
zh-cn/zh-tw), using titles resolved from /tmp/mentor_urls.json (built + verified by
the langlink step). Anchor text keeps each page's existing (localized) display name;
mapping is by position, since all locales share the same row/card order.

Idempotent: skips a file whose mentor-table already contains anchors.
"""
import re, json

URLS = json.load(open("/tmp/mentor_urls.json"))   # {EN name: {en,es,fr,ja,zh: url}}
WIKI = {"": "en", "es": "es", "fr": "fr", "ja": "ja", "zh-cn": "zh", "zh-tw": "zh"}

# EN ordered table names (canonical key + position) — read from the EN page once
_en = open("index.html", encoding="utf-8").read()
_tb = re.search(r'<table class="mentor-table">.*?</table>', _en, re.S).group(0)
TABLE_ORDER = re.findall(r'<tr><td>([^<]*)</td>', _tb)            # 38 EN names in order
CARD_ORDER = ["Marcus Aurelius", "Charlie Munger", "Steve Jobs",
              "Albert Einstein", "Leonardo da Vinci", "Socrates"]  # 6 cards in order

def anchor(url, text, style):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer" style="{style}">{text}</a>'

for prefix, lang in WIKI.items():
    path = (prefix + "/" if prefix else "") + "index.html"
    s = open(path, encoding="utf-8").read()

    tbl_m = re.search(r'(<table class="mentor-table">.*?</table>)', s, re.S)
    table = tbl_m.group(1)
    if "<td><a " in table:
        print("skip (already linked):", path); continue

    # --- table: positional wrap of each row's first <td> ---
    cnt = {"i": 0}
    def repl_row(m):
        i = cnt["i"]; cnt["i"] += 1
        url = URLS[TABLE_ORDER[i]][lang]
        return f'<tr><td>{anchor(url, m.group(1), "color: var(--accent); text-decoration: none;")}</td>'
    new_table = re.sub(r'<tr><td>([^<]*)</td>', repl_row, table)
    assert cnt["i"] == len(TABLE_ORDER), f"{path}: table rows {cnt['i']} != {len(TABLE_ORDER)}"
    s = s[:tbl_m.start()] + new_table + s[tbl_m.end():]

    # --- cards: positional wrap of the 6 name <p> ---
    ccnt = {"i": 0}
    def repl_card(m):
        i = ccnt["i"]; ccnt["i"] += 1
        url = URLS[CARD_ORDER[i]][lang]
        return f'{m.group(1)}{anchor(url, m.group(2), "color: inherit; text-decoration: none;")}</p>'
    s = re.sub(r'(<p style="color: var\(--accent\); font-weight: 700; margin: 0 0 12px; font-size: 1\.05em;">)([^<]*)</p>',
               repl_card, s)
    assert ccnt["i"] == len(CARD_ORDER), f"{path}: cards {ccnt['i']} != {len(CARD_ORDER)}"

    open(path, "w", encoding="utf-8").write(s)
    print(f"linked {len(TABLE_ORDER)} table + {len(CARD_ORDER)} card mentors in {path}")
