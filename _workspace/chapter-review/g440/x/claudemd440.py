#!/usr/bin/env python3
# Phase 440: CLAUDE.md -- the log row.
import sys, re
p = sys.argv[1]; s = open(p, encoding='utf-8').read()
ROW = """| 440 | 2026-10-12 | **Tones & Semitones: the steps dotted on the keys; the chromatic scale named; 'nearest neighbour'.** Her 14:52 on G1/G2: '점선으로 건반에서 제일 가깝다라고 표기하는게 나을 것 같아 ... 위에 그려진 화살표로는 좀 바로 눈에 안띄어서'; the chromatic scale and W W H W W W H ('여기에 붙이느냐 마느냐 고민되네' -- my recommendation, taken: name them here, build them in the Scales room); G2 '제일 가까운 이웃이라고 해도 되고'; G3 nothing for parents. tnStepLine draws a step on the keys: a dotted line, a dot at each end, its name. Page 1: two coral half steps as a stair on the keys, the whole step a navy ruler under them, a dotted legend. Page 2: from the Dog's D a dotted line to each black key ('half' on the key), from a black key to each white key; captions 'The Dog's closest keys / A black key's closest keys'. Page 3: the halves dotted through the keys, the whole step on a navy plate along the top. Page 4: E F and B C joined by a coral dotted line on a plate between the black keys. Page 5: a V -- from C (♯ up) and from D (♭ down) two dotted lines meet on the same black key. Text: a half step is 'its nearest neighbour, the closest key there is' (가장 가까운 이웃); the half-step walk 'is the chromatic scale' (반음계(크로마틱 스케일)); page 4's whole/half order 'is the major scale's recipe -- in the Scales room you build scales with it'; the Teacher copy says so. Checks: tn437test 11/11, lbcheck tones 0/0 (en, ko). |
"""
m = re.search(r'^\| 439 \| [^\n]*\n', s, re.M)
if not m: raise SystemExit('row 439')
s = s[:m.end()] + ROW + s[m.end():]
open(p, 'w', encoding='utf-8').write(s); print('CLAUDE.md: log row 440')
