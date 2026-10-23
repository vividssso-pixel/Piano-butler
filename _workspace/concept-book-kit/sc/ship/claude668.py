import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 645 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 646 | 2026-10-24 | **Rhythm opens its chapter straight away (her call).** On the Home, an area with only one concept skips its one-row list: tapping Rhythm opens Beat and time (its five groups) at once, and that page's back button says ← Home and goes to the Home. A link to the area (area=rhythm) lands on the chapter too. Areas with several concepts (Pitch, Touch, Technique, Pieces) are unchanged. Files: drills.html, drills.src.html, _workspace/concept-book-kit/sc/patch668.py. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
