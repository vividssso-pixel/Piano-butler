import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 493 |')]
assert len(idx) == 1, 'row493'
row = ("| 494 | 2026-10-19 | **Note names on the scale keyboard (her 2026-10-19 03:26: '스케일 건반에 노트이름을 적는게 낫지 않을까').** "
"`ScaleKeyboard` got an opt-in `names`: every lit key shows its note name above its finger number, in the scale's own spelling (D♭ major reads D♭ E♭ F G♭ A♭ B♭ C D♭, never C♯). The three Scale finder steps and Free play pass it; every other user of the keyboard is unchanged. Source `patch494.py`. "
"Checked by me against an independently computed spelling for all 12 major keys, right and left hand (0 mismatches), plus screenshots at 320 and 390 in English and Korean; no new fresh reviewer because the names are the same `spellFor` data the finder already printed in its note row. "
"**Open for her:** the concept book is rebuilt next to follow the Key finder and Scale finder steps (one page per step, the screen's Learn opens the steps). |")
lines.insert(idx[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
