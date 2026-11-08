import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 678 |')]
assert len(idx) == 1
rows = [
"| 679 | 2026-10-26 | **Rhythm Further, the fourth Grades 2-3 room (Build AM); the rhythm engine learns mixed groups.** Built on row 678. Board call 14, in her order: the four Grades 2-3 rooms are now all built. New chapter `rhythm-23` (chapter 33) on the Grades 2-3 floor after Intervals and Chords Further; Rhythm door group rb-23 after 6/8 time; Stories of music moves to 34-36. Theory of Music Grades 2 and 3, Time and Rhythm (Manual 2026 p66, read from the page image): (1) semiquavers, four on a beat (Grade 2), with a quaver (Grade 3), counted 1 e + a; (2) the dotted quaver and semiquaver (Grade 3); (3) the triplet (Grade 2) and the duplet (Grade 3); (4) the minim beat: 2/2, cut common time, 3/2 (Grade 3); (5) 3/8 and 9/8, simple and compound triple (Grade 3). Lines in R2 (each tapped and scored by RqStaff), questions in R2_Q, one pad R2Pad per step, drill levels semi, dot, trip, minim, e98, hear (which line?); Home r2-semi, r2-dot, r2-trip, r2-minim, r2-98 (tap a line, or a question); Lesson Book of 7 pages (r2LbPages); teacher's copy R2Teacher with every line and its counts. Engine (srhRaw and friends): SRH_PARTS, beamed groups whose notes differ in length: es (quaver, two semiquavers), se, ds (dotted quaver, semiquaver), du (the duplet, its 2 over the beam), dse (dotted quaver, semiquaver, quaver); srhGroupParts draws the main beam, the second beam or a stub, and the dots; du and dse sit where they sound; two rests (sr semiquaver, qdr dotted crotchet); the cut-time sign ['ts', '¢']. Existing items unchanged. Transposition at Grades 2 and 3 stays with the Home's Transposing lesson (noted in the teacher's copy). Tests am706.js, am706b.js, chsweep, booksweep, reg674. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
