import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 735 |')]
assert len(idx) == 1
assert not any(l.startswith('| 736 |') for l in lines)
rows = [
"| 736 | 2026-10-28 | **The Theory mark (Build CQ; board call 24, her 18:11: mark C, 'a small tag at the end').** Theory of Music content carries a small T1 to T6. On the Home, a navy tag at the end of a lesson's line (TheoryTag); in the house, an outlined tag in the room's lower left corner (the check's star stays lower right); the room's card says 'Theory Grade N'. THEORY_ROOM gives each theory room the grade most of it teaches, from the Syllabus check tabs (Theory of Music Grades 1 to 3), the Grade 4 check and the rooms built for Theory Grades 4 to 6: T1 for the Beginner theory rooms, Tempo, Rhythm, Ledger lines, Scales, Accidentals, Key signatures, Terms, Intervals, Chords; T2 for Minor scales, Signs, 6/8, Form, Melody; T3 Intervals and chords further, Rhythm further; T4 to T6 the Keys, Chords and Rhythm rooms of Grades 4 to 6. A lesson's tag is its own grade (its floor mark from Grade 2 up, otherwise its room's), with THEORY_LESSON for the exceptions (the term lists T2, the dotted crotchet T2, 6/8 in the time signatures room T2, the relative minor T2, syncopation and double sharps T4) and for what gets no tag: fingering, playing and listening lessons, the things to make, and what Theory of Music does not ask (modes, the alto clef, 8va, the pedal, swing, the fugue). Stories of music tags only its graded lessons (the strings T4, the dances T4, the woodwinds T5, the brass and the genres T6). The student's own theory grade and the checkpoint's theory filter wait for the dashboard (call 8). Source patch762.py; tests th762.js, hs762.js. |",
]
lines[idx[0] + 1:idx[0] + 1] = rows
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('row 736 added')
