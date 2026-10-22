import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 633 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 634 | 2026-10-22 | **Intervals is on the Home** (first step, structure only). Ten lessons in one order from the existing Toolbox tools (ladder, count, in the hand, 6th/7th/octave, melodic or harmonic, above the tonic, semitones, hear them, invert, tritone) and the same single 'Questions →' button under them. The four older tools (step-skip, interval ruler, letter hop, major-scale shortcut) are left out of the list for now; they overlap the new order. The lessons themselves are the old Toolbox tools, not rebuilt in the Keys and staff style yet: that is the next decision for her. Patch: sc/patch655.py on the t654 build. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
