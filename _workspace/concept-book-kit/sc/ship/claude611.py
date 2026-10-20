import sys
p = sys.argv[1]
txt = open(p, encoding='utf-8').read()
lines = txt.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 597 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 598 | 2026-10-21 | **Lessons 4–7: her turn now ends with coming down.** Lessons 4 and 5 (white keys): after she answers \"standard or different?\" the key can be played ▶ up and down with its fingers (same fingers in reverse on the way down, direction tag, colours cleared). Lessons 6 and 7 (black keys): after she finds the thumb keys going up, the way up stays on screen with \"Both thumbs found: that is the way up. Coming down, the thumbs are on the same keys.\", a \"Come down →\" button clears it and she taps the thumb keys again with the ↓ tag; then the whole fingering can be played up and down. Reminder section in this file reworded: the books are rebuilt after ALL the Home work is done, not after Scales alone. Built by `patch607.py` (`t611`). Checked in English and Korean, no console errors. Local commit only, not pushed. |")
txt = '\n'.join(lines)
a = "Sohyun's plan: first finish the Scales concept (`p-scale`, 11 lessons + drill) in drills.html and arrange it on Home one lesson at a time; **then rebuild the Lesson Book, Workbook, Teacher copy, chapters and Toolbox to match it.** Remind her of this when the Scales work is finished, and do not rebuild the books before she says the lessons are final."
assert txt.count(a) == 1
b = "Sohyun's plan (2026-10-21): first finish **all** the Home work, that is every concept arranged on Home one lesson at a time (the Scales concept, `p-scale`, 11 lessons + drill, is the first and sets the standard); **only then rebuild the Lesson Book, Workbook, Teacher copy, chapters and Toolbox to match Home, using the standard below.** Remind her of this when the Home work is all done, and do not rebuild the books before she says so."
txt = txt.replace(a, b)
open(p, 'w', encoding='utf-8').write(txt); print('ok')
