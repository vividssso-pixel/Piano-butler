import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 719 |')]
assert len(idx) == 1
rows = [
"| 720 | 2026-10-28 | **Ear Training, and the older toys on the room cards (Build CB; her 09:38).** The aural rooms are called Ear Training (Korean 청음): Ear Training, Grade 4 to Grade 8 and Ear Training, Grades 2–3 (until that room splits into Grade 2 and Grade 3, call 27); the house labels are Aural 4 … Aural 8, 청음 4 … (Ear training N lost its number in the four-room rows), the Home groups Ear training, Grade N; search finds 'ear training'. The rooms whose thing to make came before the mk- toys now show it on the MAKE YOUR OWN card (MAKE_EXTRA): Patterns, Black-key jam; Rhythm, Make a rhythm card; Key signatures, Transpose a tune; Form, Build your own form; Melody, Draw a tune; those leave the 'More in the toolbox' chips. Time signatures' Build a bar is a step of that room already. Source patch747.py. chsweep 57 chapters 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
