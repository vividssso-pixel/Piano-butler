#!/usr/bin/env python3
# Phase 428: chapter 6 (Ledger Lines) APPLIED -- her 2026-10-11 20:58 'G1-3 너가 말한거 다 해당 / 너가 검토한거 책 바탕으로
# 최적으로 만들어줘': every B as recommended in the Phase 427 pack. The Lesson Book (ll428.jsx, 7 pages), the app lesson = the
# book on screen with its moving parts (LlRungs, LlClimb, LlTwins, LlFiveCs), the drill's 7 levels (B7), the Workbook
# (B8: W1-W6 + the check-up on paper) and Teacher copy (B1 leger, B5 the four lists as one line); the toolbox speaks the
# lands' words; 'In this chapter' in Korean in every book (A8).      python3 patch428.py <drills.src.html> <ll428.jsx>
import sys, re
src, jsx = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)
def cut(start, end_marker, what):   # remove from `start` up to (not including) `end_marker`
    global s
    if s.count(start) != 1: raise SystemExit(what + ': start found %d' % s.count(start))
    i0 = s.index(start); i1 = s.index(end_marker, i0)
    s = s[:i0] + s[i1:]

# 1. the old Workbook and Teacher copy (Phase 298) and their picture go; the new ones come with the book
cut("// ─── Ledger Lines (chapter 'ledger-lines') ───\n", "// ─── Intervals (chapter 'intervals') ───", 'old ledger books')
i0 = s.index('function LadderPic({ width = 420, big = false }) {'); i1 = s.index('\n}\n', i0) + 3
s = s[:i0] + s[i1:]
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook };",
    add + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook };", 'lesson books')
rep("const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages, 'whole-staff': wsLbPages };",
    "const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages, 'whole-staff': wsLbPages, 'ledger-lines': llLbPages };", 'page fns')

# 2. paper notes may carry their own rungs (the neat-or-not pictures, bare notes to draw on)
rep("""            {ledgersFor(n.d, CLEFS[st].low, CLEFS[st].high).map(p => <line key={p} x1={x - 11} x2={x + 11} y1={yOf(p, st)} y2={yOf(p, st)} stroke={ink} strokeWidth="1.3"/>)}""",
    """            {(n.rungs || ledgersFor(n.d, CLEFS[st].low, CLEFS[st].high).map(p => [p, 11])).map(([p, hw]) => <line key={p} x1={x - hw} x2={x + hw} y1={yOf(p, st)} y2={yOf(p, st)} stroke={n.rungC || ink} strokeWidth="1.3"/>)}""", 'paper rungs')

# 2b. paper notes: the picture makes room for every rung drawn, and a note off the staff shows the line through its hole
#     only when that rung is drawn (a bare note to draw on must not look as if its rung were there already)
rep("""  notes.forEach(n => { const st = staffOf(n); ys.push(yOf(n.d, st) - 9, yOf(n.d, st) + 9); });
  if (minSpan) { ys.push(yOf(minSpan[0], staves[0]) - 9, yOf(minSpan[1], staves[staves.length - 1]) + 9); }""",
    """  notes.forEach(n => { const st = staffOf(n); ys.push(yOf(n.d, st) - 9, yOf(n.d, st) + 9); (n.rungs || []).forEach(([p]) => ys.push(yOf(p, st) - 5, yOf(p, st) + 5)); });
  if (minSpan) { ys.push(yOf(minSpan[0], staves[0]) - 9, yOf(minSpan[1], staves[staves.length - 1]) + 9); }""", 'paper rung span')
rep("""              : <g><ellipse cx={x} cy={y} rx="7" ry="4.9" fill={c}/><ellipse cx={x} cy={y} rx="3.3" ry="2.6" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>{(n.d - CLEFS[st].low) % 2 === 0 && <line""",
    """              : <g><ellipse cx={x} cy={y} rx="7" ry="4.9" fill={c}/><ellipse cx={x} cy={y} rx="3.3" ry="2.6" transform={`rotate(-38 ${x} ${y})`} fill="#fff"/>{(n.d - CLEFS[st].low) % 2 === 0 && (!n.rungs || (n.d >= CLEFS[st].low && n.d <= CLEFS[st].high) || n.rungs.some(([p]) => p === n.d)) && <line""", 'paper stub')
# 2c. the Teacher copy's answers carry the Workbook's own numbers (n0; 1 as before)
rep("""const tcAns = (label, list) => <div""", """const tcAns = (label, list, n0 = 1) => <div""", 'tcAns n0')
rep("""<span style={{color:BK.muted}}>{i + 1}.</span>""", """<span style={{color:BK.muted}}>{i + n0}.</span>""", 'tcAns number')
# 2d. chapter 5's map of the two lands names them in Korean too; every book's check page says what the foot line says
rep("""extra={both(landName('QUEENSLAND', 34, 'treble', 160), landName('KINGSLAND', 22, 'bass', 160))}/>;""",
    """extra={both(landName(t('QUEENSLAND', '퀸즈랜드'), 34, 'treble', 160), landName(t('KINGSLAND', '킹스랜드'), 22, 'bass', 160))}/>;""", 'ws land ko')
rep("""then tick how it is going -- not yet, nearly, or got it!""", """then colour a circle for how it is going -- not yet, nearly, or got it!""", 'checks intro', n=5)
rep("""하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요!""", """하나씩 보여 주고 어떤지 동그라미를 칠해요 -- 아직, 거의, 됐어요!""", 'checks intro ko', n=5)

# 3. the online lesson is the Lesson Book on screen (Phase 376 pattern); the old explanations and tools go
i0 = s.index('function LedgerLearn({ onStart }) {'); i1 = s.index('\n}\n', i0) + 3
s = s[:i0] + """const LL_STORE = [0, 1, 2, 3, 4, 5];
function LedgerLearn({ onStart }) {   // Phase 428: the Lesson Book opened on screen; only what moves is different
  const pages = llLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="ledger-lines" title={t('Ledger Lines', '덧줄')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="ledger-lines"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={LL_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}
""" + s[i1:]

# 4. the drill: her seven levels (B7), one idea each, the book's notes only
i0 = s.index('// Drill: 1, 2, then 3 ledger lines (both clefs, above and below), then find the exact key.'); i1 = s.index('const LEDGER_DRILL = {', i0)
s = s[:i0] + """// Drill (Phase 428, her B7): one idea per level, only the notes the book teaches (up to three rungs; the keys stay on the 3-octave keyboard)
const llPool = (tre, bas) => [...tre.map(d => ['treble', d]), ...bas.map(d => ['bass', d])];
const LEDGER_LEVELS = [
  { n: 1, label: 'One rung: Queensland',                        kind: 'name', pool: llPool([27, 28, 40, 41], []), time: 8 },
  { n: 2, label: 'One rung: Kingsland',                         kind: 'name', pool: llPool([], [15, 16, 28, 29]), time: 8 },
  { n: 3, label: 'Two rungs, both lands',                       kind: 'name', pool: llPool([42, 43, 26], [14, 13, 30]), time: 8 },
  { n: 4, label: 'Sky C and Sea C: a step or a skip',           kind: 'name', pool: llPool([40, 41, 42, 43, 44], [12, 13, 14, 15, 16]), time: 7 },
  { n: 5, label: 'Between the lands: the same key, two ways',   kind: 'name', pool: llPool([26, 27, 28], [28, 29, 30]), time: 7 },
  { n: 6, label: 'Up to three rungs, fast (Grade 2)',           kind: 'name', pool: llPool([39, 40, 41, 42, 43, 44, 26, 27, 28], [12, 13, 14, 15, 16, 17, 28, 29, 30]), time: 5 },
  { n: 7, label: 'Find it on the keys (exact octave)',          kind: 'key', pool: llPool([39, 40, 41, 26, 27, 28], [28, 29, 30]), time: 10 },
];
function genLedgerQuestion(lv, prev) {
  const uid = Math.random();
  let it = lv.pool[0];
  for (let g = 0; g < 20; g++) { it = lv.pool[Math.floor(Math.random() * lv.pool.length)]; if (!prev || prev.d !== it[1] || prev.clef !== it[0]) break; }
  const [clef, d] = it;
  return { kind: lv.kind, key: clef + d, d, clef, staff: clef, answer: lv.kind === 'key' ? dToKey(d) : dName(d), uid };
}
""" + s[i1:]
rep("""  answerLabel: (q) => withSolfa(dName(q.d)) + ' (' + dLabel(q.d) + ', ' + (LANG === 'ko' ? ledgerDescKo(q.clef, q.d) : ledgerDesc(q.clef, q.d)) + ')',
  Question: StaffQuestion, Learn: LedgerLearn,""",
    """  answerLabel: (q) => withSolfa(dName(q.d)) + ' (' + dLabel(q.d) + ', ' + llPlace(q.clef, q.d) + (LL_C[q.d] ? ' -- ' + LL_C[q.d]() : '')
    + (q.d >= 26 && q.d <= 30 ? ' = ' + llPlace(q.clef === 'treble' ? 'bass' : 'treble', q.d) : '') + ')',
  Question: StaffQuestion, Learn: LedgerLearn,""", 'answer label')
rep("const LEVEL_KO = {", """const LEVEL_KO = {
  'One rung: Queensland': '발판 하나: 퀸즈랜드', 'One rung: Kingsland': '발판 하나: 킹스랜드', 'Two rungs, both lands': '발판 둘: 두 나라',
  'Sky C and Sea C: a step or a skip': '하늘 C와 바다 C: 한 걸음이나 건너뛰기', 'Between the lands: the same key, two ways': '두 나라 사이: 같은 건반, 두 가지로',
  'Up to three rungs, fast (Grade 2)': '발판 셋까지, 빠르게 (2급)',""", 'level ko')

# 5. the toolbox: the same four tool ids, now the book's moving parts and the lands' words
rep("""{ id: 'ledger-walk', ch: 'ledger-lines', title: 'Walk off the staff', blurb: 'Ledger lines appear one by one.', C: () => <><ExplLedger1/><LedgerClimb/></> },""",
    """{ id: 'ledger-walk', ch: 'ledger-lines', title: 'Climb out of the lands', blurb: 'Up into the sky, down into the sea, a rung at a time.', C: () => <LlClimbBoth/> },""", 'tool walk')
rep("""{ id: 'ledger-landmarks', ch: 'ledger-lines', title: 'Notes on ledger lines', blurb: 'A C E, C A F, C E G, E C A.', C: () => <><ExplLedger2/><LedgerLandmarks/></> },""",
    """{ id: 'ledger-landmarks', ch: 'ledger-lines', title: 'The five Cs', blurb: 'From Sea C to Sky C -- then hop to any ledger note.', C: () => <LlFiveCs/> },""", 'tool cs')
rep("""{ id: 'ledger-twins', ch: 'ledger-lines', title: 'Same note, other staff', blurb: 'Ledger notes are the other staff’s lines.', C: () => <><ExplLedger3/><LedgerTwins/></> },""",
    """{ id: 'ledger-twins', ch: 'ledger-lines', title: 'Between the lands', blurb: 'Borrowed rungs: the same key, written two ways.', C: () => <LlTwins/> },""", 'tool twins')
rep("""{ id: 'ledger-write', ch: 'ledger-lines', title: 'Write with ledger lines', blurb: 'Tap the right line or space.', C: () => <><ExplLedger4/><LedgerWrite/></> },""",
    """{ id: 'ledger-write', ch: 'ledger-lines', title: 'Draw the rungs', blurb: 'As many rungs as the note needs: no gaps, none too many.', C: () => <LlRungs/> },""", 'tool write')
rep("""  'ledger-walk': ['오선 밖으로 걸어가기', '덧줄이 하나씩 나타나요.'],
  'ledger-landmarks': ['덧줄 위의 음', 'A C E, C A F, C E G, E C A.'],
  'ledger-twins': ['같은 음, 다른 오선', '덧줄 음은 다른 오선의 줄이에요.'],
  'ledger-write': ['덧줄로 써 보기', '맞는 줄이나 칸을 눌러요.'],""",
    """  'ledger-walk': ['두 나라 밖으로 오르내리기', '하늘로 올라가고, 바다로 내려가요, 발판 하나씩.'],
  'ledger-landmarks': ['다섯 C', '바다 C에서 하늘 C까지 -- 그리고 덧줄 음으로 뛰어요.'],
  'ledger-twins': ['두 나라 사이', '빌려 온 발판: 같은 건반, 두 가지로.'],
  'ledger-write': ['발판 그리기', '음에 필요한 만큼만: 빈틈없이, 더 많지 않게.'],""", 'ko tools')

# 6. the chapter's little staff picture (book mode) says Clara's C
rep("""    <AText x={110} y={96} size={11} c={ART_C} serif={false} weight={700}>{t('middle C', '가운데 도')}</AText>""",
    """    <AText x={110} y={96} size={11} c={ART_C} serif={false} weight={700}>{t('Clara\\'s C', '클라라의 C')}</AText>""", 'art clara')

# 7. 'In this chapter' in Korean too, in every book (A8)
rep("""marginBottom:6}}>In this chapter</div>""", """marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>""", 'toc head', n=5)

# 8. the old ledger tools and explanations are no longer used anywhere: cut them (with the comment lines just above each)
def drop(head, end='\n}\n'):
    global s
    if s.count(head) != 1: raise SystemExit('drop ' + head[:40] + ': found %d' % s.count(head))
    i0 = s.index(head); i1 = s.index(end, i0) + len(end)
    while True:   # the comment lines directly above
        j = s.rfind('\n', 0, i0 - 1)
        line = s[j + 1:i0 - 1] if j >= 0 else ''
        if line.lstrip().startswith('//') and i0 > 0: i0 = j + 1
        else: break
    s = s[:i0] + s[i1:]
for h in ['function LedgerMirror() {', 'function LedgerClimb() {', 'function LedgerLandmarks() {', 'function LedgerTwins() {', 'function LedgerWrite() {',
          'function ExplLedger1() {', 'function ExplLedger2() {', 'function ExplLedger3() {', 'function ExplLedger4() {']:
    drop(h)
drop('const LEDGER_SETS = [', '];\n')
drop('const TWINS = [', '];\n')
for h in ['function ledgerDesc(clef, d) {', 'function ledgerDescKo(clef, d) {', 'function staffPlaceKo(clef, d) {', 'function staffPlace(clef, d) {']:
    drop(h)
for h in ['function ledgerWhere(clef, d) {', 'const ORD_WORD = [', 'const CLEF_KO = {']:   # one-line declarations
    drop(h, '\n')
for name in ['ledgerDesc', 'ledgerWhere', 'staffPlace', 'ORD_WORD', 'CLEF_KO', 'LedgerMirror', 'LedgerClimb', 'LedgerLandmarks', 'LEDGER_SETS', 'LedgerTwins', 'ExplLedger1', 'ExplLedger4']:
    if re.search(r'\b' + name + r'\b(?!/)', s.replace('WriteTheNote/LedgerWrite', '')): raise SystemExit('still used: ' + name)

open(src, 'w', encoding='utf-8').write(s); print('patch428 ok')
