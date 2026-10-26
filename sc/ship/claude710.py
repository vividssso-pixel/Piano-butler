import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 682 |')]
assert len(idx) == 1
rows = [
"| 683 | 2026-10-26 | **Stories of music is the one place for the piano, the instruments, composers and styles (Build AQ, her 22:35: '음악이야기에 스타일, 작곡가, 자잘 악기 관련 다 넣어줘. 여기저기 흩어지지 않게. 중복된 건 더 잘 만들어진 걸로 남기든 정리하든 새로 만들든 하자').** 1. The attic's room (high and low, big is low, the instrument families, the violin family, ranges, Hz and the octave ladder) moves into the Stories of music storey as 'Instruments' (악기), after the piano; the attic goes (it held only this room). This changes the 25 Oct call 'Pitch, Hz & range to the attic', at her word. The house now reads four floors and a Stories of music room: the piano's story 1-5, Instruments 6-13, Composers 14-24, Styles 25-32. 2. Scattered pieces come home, the better one kept: the Home's 'Pitch and range' topic (Long and short; How far a piano reaches) gives way to the Instruments steps that do the same with more instruments and a quiz; the 12-bar blues (Chords) and the pentatonic scale (Scales) give way to the Styles steps; Straight or swing? moves from Rhythm into Styles beside Blues and swing; Which style? leaves the Aural extras; the piano's pedals step leaves the Touch room (which keeps its own pedalling lesson). 3. The planned 'more-scales' room is dropped from the Grades 2-3 floor (pentatonic and blues are in Styles; the modes have their own Home topic). Source patch710.py (t710). Tests: aq710.js (house, Stories door, chapter numbers 34-37, kickers), chsweep 37 chapters 0 errors, booksweep 0 errors, Instruments Lesson Book 0 overflow, regression 274 lessons, 45 drills, 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
