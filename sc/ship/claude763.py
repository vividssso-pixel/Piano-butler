import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 736 |')]
assert len(idx) == 1
assert not any(l.startswith('| 737 |') for l in lines)
rows = [
"| 737 | 2026-10-28 | **Where should you start? (Build CR; board call 29, her 19:58: 'some children's practical and theory don't match ... a diagnostic like this is the hook that starts people on the drills').** A placement round on the map's head (chip 'Where should I start?'; 'Already playing? Find your start' for a new user; 'Find my start again' after) and by the link ?view=path&start=1. Two ladders, apart: Piano, the practical rooms of each floor that have checks and no theory mark (ear training, Ear prep and the Beginner rooms, the scales and arpeggio rooms, the Grade 7 pieces room: Beginner, Prelim, Grades 1 to 8), and Theory, the rooms by their Theory mark T1 to T6, asked without sound or tapping (no noPrint levels). The child says which piano and theory exam they have passed (or Not yet); each ladder starts at that rung: six questions a rung from as many of its rooms as possible (CheckRun, floor style), five to climb; the first rung missed is the start; if the first rung tried is missed, one rung lower is tried once. Rooms missed on rungs passed are listed to look at. The result: the piano floor and the theory grade, a 'Start here' button for each, saved on the device (pb_place_v1 {piano: floor index, theory: 1 to 6, or 7 when all were easy}). The house's main button ('Your start' until a room is started) and 'you are here' then run from the placed floor up, with theory rooms above the placed theory grade left for later (call 24). Playing itself is not tested: the piano part is ears, keys and scales knowledge. Nothing on the main site links to it (her call). Source patch763.py; tests pl763.js (five paths, en and ko), pl763b.js (the house), pl763c.js (5,760 generated questions, none with sound in theory). |",
]
lines[idx[0] + 1:idx[0] + 1] = rows
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('row 737 added')
