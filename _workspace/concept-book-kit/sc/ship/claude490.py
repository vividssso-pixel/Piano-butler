import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 489 |')]
assert len(idx) == 1, 'row489'
row = ("| 490 | 2026-10-19 | **The concept book's key pad shows one thing at a time (her 2026-10-19 00:52: '이렇게 다같이 보이니까 어딜 봐야할지 모르겠어. 서클오브5th랑 조표랑 같이 ... 반음계 클락은 건반이랑 ... 검은건반 두이름 ... 두개 다').** "
"`CbKeyPad` (page 2 of the Scales and keys concept book, `cb-p-scales`) is now two tabs: **Keyboard clock** (the clock, a one-octave piano under it with both names on every black key, and the spelled major scale under a caption) and **Circle of fifths** (the circle with the twin keys, the key signature on a staff right under it, and the key line on two lines). The chosen key survives a tab switch; Listen and Fingering stay below both. "
"Shared parts: `KeyRing` got an opt-in `both` (both enharmonic names on black keys even when the scale spells one), `TapKeyboard` an opt-in `bigLabels` (11 units instead of 8.5, so the labels are legible at 320 px); neither changes any other user of them (text and print page identical to Phase 489). Tablist semantics (aria-controls, tabpanel, roving tabindex, arrow keys, visible focus ring). Source `patch490.py` in `_workspace/concept-book-kit/`. "
"Full review (shared KeyRing): one fresh reviewer, no must-fix; 5 should-fix all fixed (label size, key line wrapping, title no longer says 'all at once', tab semantics, caption for the note row). **Open for her:** show the relative minor beside the major in the Scale finder (her 2026-10-19 01:03); how her teaching order (scale: finger numbers, white keys, black-key starts, 12 keys by semitones, hands; key: sharp and flat order, tonic in each group, then the minor) becomes steps in the two tools. |")
lines.insert(idx[0] + 1, row)
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('ok')
