#!/usr/bin/env python3
# Phase 448 (QA after her 18:56 '다른 오류들 있나 한번 더 검사'): the articulation marks under the notes sat exactly where a
# ledger line goes (a whole space under the staff), so a tenuto looked like middle C's ledger line. The heads sit on the
# second line; the first space clear of the head is under the staff: the dot and the tenuto now go half a space under the
# bottom line (between the ledger positions), the wedge points up at the note, the accent stays under the staff.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b):
    global s
    if s.count(a) != 1: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
rep("""// Four crotchets with an articulation drawn on them (stems up, marks below the heads... kept above for clarity).
function ArticBar({ mark, ink = '#26296b', width = 220 }) {
  const xs = [40, 90, 140, 190], y = 62;
  const marks = xs.map((x, i) => {
    const my = y + 16;
    if (mark === 'dot') return <circle key={i} cx={x} cy={my} r="2.6" fill={ink}/>;
    if (mark === 'wedge') return <path key={i} d={`M${x - 3},${my - 4} L${x + 3},${my - 4} L${x},${my + 5} Z`} fill={ink}/>;
    if (mark === 'tenuto') return <line key={i} x1={x - 7} x2={x + 7} y1={my} y2={my} stroke={ink} strokeWidth="2.4"/>;""",
"""// Four crotchets with an articulation drawn on them: stems up, so the marks go under the heads. The heads sit on the second
// line; the first space clear of a head is just under the staff (Phase 448: a whole space under it, a tenuto read as a
// ledger line). The wedge points at the note.
function ArticBar({ mark, ink = '#26296b', width = 220 }) {
  const xs = [40, 90, 140, 190], y = 62;
  const marks = xs.map((x, i) => {
    const my = y + 16, mi = y + 12;   // mi: half a space under the bottom line (70), clear of the head and of any ledger line
    if (mark === 'dot') return <circle key={i} cx={x} cy={mi} r="2.6" fill={ink}/>;
    if (mark === 'wedge') return <path key={i} d={`M${x - 3},${my + 4} L${x + 3},${my + 4} L${x},${my - 5} Z`} fill={ink}/>;
    if (mark === 'tenuto') return <line key={i} x1={x - 7} x2={x + 7} y1={mi} y2={mi} stroke={ink} strokeWidth="2.4"/>;""")
open(dst, 'w', encoding='utf-8').write(s); print('448 applied')
