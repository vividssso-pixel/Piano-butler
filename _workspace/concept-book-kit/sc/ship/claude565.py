import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 560 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 561 | 2026-10-19 | **Accidentals lesson 7, play it (her 'keep going').** New hidden tool `ac-play` ('Play it' / 추 보기) replaces the old 'Play sharps and flats' (`sac-signs`) and 'The natural' (`sac-natural`) in the Home list (tools kept). Three little tunes on the staff, played key by key: tune 1 G F♯ G F | F with the coral band shown; tune 2 A B♭ A B B♮ | B and tune 3 G♯ A G F | A♭ G A with no band until a wrong key brings it in as a hint (so she reads the signs herself). Names appear under each note as she plays it; a wrong key gets 'Look for a sign: just before this note, or earlier in its bar' (her `SacPad` line); '▶ Listen' plays the tune; 'Next tune →'. Explanation line on top. Source `patch566.py`; checked by me, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
