import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 491 |')]
assert len(idx) == 1, 'row491'
row = ("| 492 | 2026-10-19 | **Key finder in four short steps (her 2026-10-19 01:03 teaching order, 01:37 'learn the order and tap right below it', 01:28 'keep it simple, one look').** "
"`KeyFinder` is now a stepper: **1 Sharps** and **2 Flats** each put the order and the tap on one screen (pick 1-7; the staff and the Father Charles sentence light up in order; '▶ Say the order' plays it; then tap the last sharp, or the second-to-last flat, and the key lights on a one-octave piano; one flat = F), **3 Major and minor** side by side on a piano with the same signature (‹ › over the 15 keys), **4 Before you play the piece** (staff, major · minor, link to the Scale finder). "
"The 'why' is shown, not written: a fixed three-pill chain 'Read it → Name the key → Play its scale' highlights where the step sits, and the title is a question that turns into its answer ('What key has 3♯?' → '3♯ → A major'). The key found in step 1/2 carries to steps 3-4. The old all-at-once Key finder is kept as `KeyFinderFree`, reached by 'Free play'. Source `patch492.py`. "
"Full review (a rebuilt concept tool): one fresh reviewer, no must-fix; theory checked for all 15 keys through the UI; should-fix all fixed (44 px count chips in a 4+3 grid on narrow screens, key carried between steps, chain on one row, one header line less, Korean 샤프/플랫 spelled out, roving tabindex and arrow keys on the tabs). "
"**Open for her:** the wording 'second-to-last flat' and '3 half steps down' against how she says it in lessons; the same four-step shape for the Scale finder (finger numbers, white keys, black-key starts, 12 keys, hands); the 'Reading a piece' map is parked as a later review layer, not built. |")
lines.insert(idx[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
