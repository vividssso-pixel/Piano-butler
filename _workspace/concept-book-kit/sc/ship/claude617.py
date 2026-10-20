import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 603 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 604 | 2026-10-21 | **Scale finder: one pair of keyboards in the lessons' look; the staff button renamed everywhere.** Her feedback (2026-10-21): no reason to keep both the new top keyboard and the old-design fingering keyboards; use the new design with the group colours, large, right hand above left hand. The finder now shows only two keyboards (`ScKeys`, now with optional `mw` width and `oct` octave count): finger numbers above the keys, coral = a group of 3, blue = a group of 4 (the same colours as lessons 4-9), note names on the keys, both names on black keys; 2 octaves scroll sideways at a readable size. Where the harmonic fingering would put a thumb on a black key, one scale keyboard is shown with the note as before. `ScStaffBtn` (every lesson) now reads \"Show on the staff\" / \"스태프로 보여주기\" and \"Hide the staff\" / \"스태프 숨기기\" instead of \"Write it on the staff\". Built by `patch613.py` (`t617`). Checked major, minor, 1 and 2 octaves, Korean: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
