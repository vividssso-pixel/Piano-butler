#!/usr/bin/env python3
# Phase 439: CLAUDE.md -- the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 439 | 2026-10-12 | **Lines that read well: the double dash and Korean words never split.** Her 14:52 on A8 and the Korean line breaks: '내 생각엔 줄을 잘 정리해야할 것 같아. 읽기 쉽게.' patch439.py: a MutationObserver on #root fixes every text node as it arrives or changes -- ' -- ' (the house dash) becomes a no-break space, '-', a word joiner, '-', so the dash stays with the word before it and its two strokes never part (books, app, SVG text alike); html lang follows the app's language switch (it was set only for the books), and html[lang=ko] body gets word-break: keep-all with overflow-wrap: anywhere, so Korean breaks between words, never inside one. Checks: lbcheck for all seven Lesson Books the same as 438; wbcheck no overflow (front and seven chapters); house438test 63/63, tn437test 11/11, ll431 24/24, ll429 82/82 and ch3app397 35/35 (tests updated: they read ' -- ' through the glue; the black-key level is Tones level 5 since Phase 437), ws419 45/45, ch2app395 21/21, sf405 22/22, nosong399 24/24, ch1app376 21/21 (one timing flake on the first run). |
"""
m = re.search(r'^\| 438 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 438')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 439')
