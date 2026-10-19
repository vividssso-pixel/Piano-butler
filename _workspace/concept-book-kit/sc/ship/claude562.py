import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 557 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 558 | 2026-10-19 | **Signs in a bar, reworked after her 16:12 note (colours were ambiguous; which sign covers what; 'same pitch follows automatically' was too thin).** Each sign now has its own colour and a coloured band along ITS line or space from the sign to the bar line (sharp coral, flat blue, natural grey); a note wears the colour of the sign that reaches it; the note in focus is ringed in navy (no longer coral), and the '?' note in her turn has a dashed ring. The walk is eight small steps: F♯ / the sharp covers this space to the bar line / G is on another line: not touched / F on the same space is F♯ with no sign, automatically / the F an octave higher is on another line: plain (her `ACC_EXAMPLES` octave note) / B♭ with its band / the natural ends the flat / new bar, every band stopped. Her turn asks six notes (covered F, high F, G, natural B, new-bar F, B♭) with the reason after each answer. Blue is the one hue added to navy + coral, for the flat's band only (to be confirmed by her). Source `patch563.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
