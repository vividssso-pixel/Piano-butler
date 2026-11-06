#!/usr/bin/env python3
# Phase 467 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 10, Dynamics &
# Articulation, built in full: the Lesson Book (dictionary entries), its screen lesson (the book with what moves on pages
# 2 to 6), a 9-level drill, the Workbook and the Teacher copy.
#   sdybook467.jsx: sdyMarks / SdyStaff (dynamics, hairpins, staccato dots, slurs, ties and sound lines over sskRaw's
#                   notes), the Lesson Book
#   sdyapp467.jsx:  the pads of pages 2 to 6, SdyLearn, the drill (Object.assign on DYN_DRILL)
#   sdywb467.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Also: a slur is 이음줄 and a tie 붙임줄 in Korean everywhere (a few old strings said 슬러); 크레셴도; the toolbox gets
# the five pads; the room comes after Steps & Skips (its tunes are in C position).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['sdybook467.jsx', 'sdyapp467.jsx', 'sdywb467.jsx'])

# 1. the new code before the Lesson Book registry; dynamics joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("'reading-steps': ReadingStepsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", dynamics: DynamicsLessonBook };") + s[j:]
rep("'time-signatures': tsLbPages, 'reading-steps': sskLbPages };", "'time-signatures': tsLbPages, 'reading-steps': sskLbPages, dynamics: sdyLbPages };")

# 2. the toolbox: this room's moving parts first
rep("  { id: 'dyn-order', ch: 'dynamics',", """  { id: 'sdy-pf', ch: 'dynamics', title: 'Soft or loud?', blurb: 'Hear a tune p and f, then say which you heard.', C: () => <SdyPfPad/> },
  { id: 'sdy-ladder', ch: 'dynamics', title: 'From pp to f', blurb: 'Four steps of loudness: hear them, then put them in order.', C: () => <SdyLadder/> },
  { id: 'sdy-hair', ch: 'dynamics', title: 'Louder or softer?', blurb: 'Hairpins on the staff: hear them, then say which you heard.', C: () => <SdyHairPad/> },
  { id: 'sdy-touch', ch: 'dynamics', title: 'Legato or staccato?', blurb: 'Watch the sound lines, then say which you heard.', C: () => <SdyTouchPad/> },
  { id: 'sdy-tie', ch: 'dynamics', title: 'Tie or slur?', blurb: 'The same curve: on the same note or on different notes?', C: () => <SdyTiePad/> },
  { id: 'dyn-order', ch: 'dynamics',""")
rep("  'dyn-order': ['다이나믹 순서대로 놓기',", """  'sdy-pf': ['여리게? 세게?', '선율을 p와 f로 듣고, 어느 쪽을 들었는지 골라요.'],
  'sdy-ladder': ['pp에서 f까지', '네 단계의 셈여림: 듣고, 차례대로 놓아요.'],
  'sdy-hair': ['점점 세게? 점점 여리게?', '오선 아래의 헤어핀: 듣고, 어느 쪽을 들었는지 골라요.'],
  'sdy-touch': ['레가토? 스타카토?', '소리 줄을 보며 듣고, 어느 쪽을 들었는지 골라요.'],
  'sdy-tie': ['붙임줄? 이음줄?', '같은 곡선: 같은 음 위일까요, 다른 음 위일까요?'],
  'dyn-order': ['다이나믹 순서대로 놓기',""")
rep("  'dyn-order': ['expression', 0, 1, 'game'],", "  'sdy-pf': ['expression', 0, 1, 'game ear'], 'sdy-ladder': ['expression', 0, 1, 'game ear'], 'sdy-hair': ['expression', 0, 2, 'game ear'], 'sdy-touch': ['expression', 0, 1, 'show ear'], 'sdy-tie': ['expression', 0, 2, 'game'],\n  'dyn-order': ['expression', 0, 1, 'game'],")
rep("['ssk-read', 'mini-tune'],", "['ssk-read', 'mini-tune'], ['sdy-pf', 'dyn-order'], ['sdy-ladder', 'dyn-order'], ['sdy-hair', 'hairpin'], ['sdy-touch', 'touch-lengths'], ['sdy-tie', 'tie-slur'],")
rep("  'dynamics': ['dyn-order', 'hairpin', 'pedal', 'tie-slur', 'touch-ear', 'touch-lengths'],", "  'dynamics': ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'sdy-touch', 'sdy-tie', 'dyn-order', 'hairpin', 'touch-ear', 'touch-lengths', 'tie-slur', 'pedal'],")
rep("  ['e2', 'ear', 'Plays loud and soft', ['dyn-order', 'touch-ear']],", "  ['e2', 'ear', 'Plays loud and soft', ['sdy-pf', 'sdy-ladder', 'dyn-order', 'touch-ear']],")
rep("  ['e4', 'ear', 'Legato and staccato', ['touch-ear', 'touch-lengths']],", "  ['e4', 'ear', 'Legato and staccato', ['sdy-touch', 'touch-ear', 'touch-lengths']],")
rep("  ['e6', 'ear', 'Crescendo, diminuendo, rit.', ['hairpin', 'speed-change']],", "  ['e6', 'ear', 'Crescendo, diminuendo, rit.', ['sdy-hair', 'hairpin', 'speed-change']],")
rep("  ['r8', 'read', 'Repeats, D.C. and ties', ['road-map', 'tie-slur']],", "  ['r8', 'read', 'Repeats, D.C. and ties', ['road-map', 'sdy-tie', 'tie-slur']],")

# 3. Korean: a slur is 이음줄, a tie 붙임줄 (the book's words); 크레셴도
rep("  'tie-slur': ['이음줄일까요, 슬러일까요?', '같은 음일까, 다른 음일까?'],", "  'tie-slur': ['붙임줄일까요, 이음줄일까요?', '같은 음일까요, 다른 음일까요?'],")
rep("{tip(t('Slur', '슬러'),", "{tip(t('Slur', '이음줄'),")
rep("<b>슬러</b>는 레가토가", "<b>이음줄</b>은 레가토가")
rep("'짧은 슬러, 가볍고 맑은 터치'", "'짧은 이음줄, 가볍고 맑은 터치'")
rep("'크레센도와 디미누엔도.'", "'크레셴도와 디미누엔도.'")

# 4. 'easier after': Steps & Skips (C position; it comes after Time Signatures, where the tie is learned)
rep("dynamics: ['first-steps', 'staff'],", "dynamics: ['reading-steps'],")
# 5. hover only where there is a real pointer (a tapped answer button stayed outlined on phones and looked chosen);
#    a semibreve's ledger line a little wider than its head
rep("    .choice-btn:hover:not(:disabled) { border-color: var(--text); }", "    @media (hover: hover) { .choice-btn:hover:not(:disabled) { border-color: var(--text); } }")
rep("  const ledgers = (nx, d) => ledgersFor(d, low, high).map(p => '<line x1=\"' + pFix(nx - 12) + '\" x2=\"' + pFix(nx + 12) + '\"", "  const ledgers = (nx, d, lw = 12) => ledgersFor(d, low, high).map(p => '<line x1=\"' + pFix(nx - lw) + '\" x2=\"' + pFix(nx + lw) + '\"")
rep("    out.push(ledgers(nx, d), nvbHead(nx, y, kind, c, 1));", "    out.push(ledgers(nx, d, kind === 'w' ? 14.5 : 12), nvbHead(nx, y, kind, c, 1));")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
