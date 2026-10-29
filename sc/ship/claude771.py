import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 740 |')]
assert len(idx) == 1
assert not any(l.startswith('| 741 |') for l in lines)
rows = [
"| 741 | 2026-10-29 | **Floors by grade only; Clara only for the key names; a stopwatch online; wide pictures (Build CV; her 14:22 and 14:24).** (1) Floors are named by their grade alone, everywhere: the house plaques ('BEGINNER', not 'FLOOR 1 · BEGINNER'), floorName (map, placement, next on the path, checkpoints), the map's welcome texts ('Start on Beginner') and the teacher dashboard (dhFloorName). The words 'floor' and 'up a floor' stay; only the numbers go. (2) Clara is used only while learning the key names (Chapter 3, Note names: Clara, Dog, Exit...). Everywhere else it is middle C, and counting from middle C counts it as 1 (her pick): the Queen's G is the fifth note up, the King's F the fifth note down, treble and bass C the eighth (Home: 'Fold: G and F', 'Fold again'). Clara's ladder is now middle C's short line on Beginner and its ledger line on Prelim and the Home ('Middle C's short line is a ledger line'). Staff, whole staff, ledger lines, tones, hand positions, scale play, the ear rooms (Turtle, middle C or bird?), Staff maker, the Toolbox fold, the landmarks, the Home's Keys and staff, workbooks and teacher copies. The pink pawn left the staff pictures; one middle C key (B C D, C in coral, MIDC_KEY_SVG / sfMidKey) marks middle C where a sign was needed. Note names keeps Clara; its teacher note now says she is only the key-name helper. (3) 'Beat your time' online: LbStopwatch, tap to start and stop, the best time kept on the device (pb_beat_v1, by each challenge's tid beat1-12, so either language keeps it); print unchanged. (4) LbPic: a wide, short drawing (under 62% of its frame's height) gets a frame that hugs it, with the page's spare room above and below the frame (auto margins), so the blocks after it stay together and the page still ends level. Tests: cv771.js (stopwatch, map, floorName, no Clara in 6 rooms x 2 languages), house771.js, dash771.js; book sweeps as before. Files: sc/patch771.py, sc/dpatch771.py. |",
]
lines[idx[0] + 1:idx[0] + 1] = rows
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('row 741 added')
