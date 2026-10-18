import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 492 |')]
assert len(idx) == 1, 'row492'
row = ("| 493 | 2026-10-19 | **Scale finder in three short steps (her 2026-10-19 01:01 teaching order: finger-number pattern 123 / 1234, white-key scales, black-key scales, all twelve a half step apart; hands right, left, both).** "
"`ScaleFinder` is now a stepper when opened from the Toolbox or Home: **1 White keys** (C D E F G A B), **2 Black keys** (D♭ E♭ F♯ A♭ B♭), **3 All twelve** in chromatic order (C D♭ D E♭ E F F♯ G A♭ A B♭ B). Each step: a question title ('How do you play C major?'), key chips, hand chips Right / Left / Both (both = two keyboards stacked; the hand choice carries across steps), the keyboard with finger numbers coloured by the 1-2-3 and 1-2-3-4 groups, '▶ Hear it', 'Next →'. A fixed chain 'White keys → Black keys → All twelve' shows where you are. "
"The old finder is kept as `ScaleFinderFree` ('Free play' at the bottom): every link with `?key=` (including the Key finder's last step, the book QR and the concept-book link, which now carry `&key=C`) and every lesson step that passes `ext`/`onKey` open it unchanged, so typing a scale and the minor forms still work. Source `patch493.py`. "
"Full review: one fresh reviewer, no must-fix, theory checked for all 12 keys, both hands; should-fix all fixed (chips no longer overlap at 320, stale Home/Toolbox lines, links that promised typing, 흰건반 not 하얀건반, one try-box in Free play). "
"**Open for her:** the existing A♭ right-hand fingering is 2 3 1 2 3 1 2 3, where 3 4 1 2 3 1 2 3 is more usual (data from before this change, not touched); minor scales are only in Free play for now; next the concept book is rebuilt to follow these steps. |")
lines.insert(idx[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
