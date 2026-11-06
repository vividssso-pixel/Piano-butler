#!/usr/bin/env python3
# Phase 419: chapter 5 (The Whole Staff) APPLIED -- her 'all yes' (2026-10-10 07:08) to B1-B8 and D1:
#   the Lesson Book (ws420.jsx: 7 pages), the app lesson = the book on screen with its moving parts, the drill's 7 levels
#   (B6: crown check, Queensland, Kingsland, five landmarks, landmark hop, both lands fast, keys), the Workbook (B7:
#   W1-W6 + the check-up on paper) and Teacher copy; the landmark/fold/hop tools speak the royal names and lose the
#   two-ledger-line High C / Low C (chapter 6).
#   python3 patch419.py <drills.src.html> <ws420.jsx>
import sys, re
src, jsx = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read(); add = open(jsx, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. the pages, the Workbook, the Teacher copy; registered with the other chapters
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook };",
    add + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook };", 'lesson books')
rep("const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages };",
    "const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages, 'whole-staff': wsLbPages };", 'page fns')
rep("const WORKBOOKS = { front: FrontMatter, staff: SfWorkbook,", "const WORKBOOKS = { front: FrontMatter, staff: SfWorkbook, 'whole-staff': WsWorkbook,", 'workbooks')
rep("const TEACHER_COPIES = { staff: SfTeacher,", "const TEACHER_COPIES = { staff: SfTeacher, 'whole-staff': WsTeacher,", 'teacher copies')

# 2. the online lesson is the Lesson Book on screen (Phase 376 pattern)
i0 = s.index('function WholeStaffLearn({ onStart }) {'); i1 = s.index('\n}\n', i0) + 3
s = s[:i0] + """const WS_STORE = [0, 1, 2, 3, 4, 5];
function WholeStaffLearn({ onStart }) {   // Phase 419: the Lesson Book opened on screen; only what moves is different
  const pages = wsLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="whole-staff" title={t('The Whole Staff', '오선 전체 읽기')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="whole-staff"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} storeAs={WS_STORE[i]} title={pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}
""" + s[i1:]

# 3. the drill: her seven levels (B6), one idea each
i0 = s.index('const WHOLE_STAFF_LEVELS = ['); i1 = s.index('];\n', i0) + 3
s = s[:i0] + """const WS_RANGE = (lo, hi) => Array.from({ length: hi - lo + 1 }, (_, i) => lo + i);
const WHOLE_STAFF_LEVELS = [   // Phase 419 (her B6): one idea per level; every line and space, and the note just outside each staff (B3)
  { n: 1, label: 'Crown check: whose land?',            kind: 'crown', pools: { treble: WS_RANGE(29, 39), bass: WS_RANGE(17, 27) }, clef: 'mixed', time: 5 },
  { n: 2, label: 'Queensland: every line and space',    kind: 'name', range: [29, 39], clef: 'treble', time: 7 },
  { n: 3, label: 'Kingsland: every line and space',     kind: 'name', range: [17, 27], clef: 'bass', time: 7 },
  { n: 4, label: 'The five landmarks',                  kind: 'name', pools: { treble: [28, 32, 35], bass: [21, 24, 28] }, clef: 'mixed', time: 6 },
  { n: 5, label: 'Landmark hop: a step or a skip away', kind: 'name', pools: { treble: [29, 30, 31, 33, 34, 36, 37], bass: [19, 20, 22, 23, 25, 26, 27] }, clef: 'mixed', time: 7 },
  { n: 6, label: 'Both lands, fast',                    kind: 'name', pools: { treble: WS_RANGE(28, 39), bass: WS_RANGE(17, 28) }, clef: 'mixed', time: 5 },
  { n: 7, label: 'Find it on the keys (exact octave)',  kind: 'key', range: [21, 39], clef: 'grand', time: 10 },
];
""" + s[i1:]
rep("""  let d, clef;
  for (let n = 0; n < 12; n++) {
    if (lv.clef === 'mixed') { clef = Math.random() < 0.5 ? 'treble' : 'bass'; d = lv.ranges ? rnd(...lv.ranges[clef]) : clef === 'treble' ? rnd(26, 42) : rnd(14, 30); }""",
    """  let d, clef;
  for (let n = 0; n < 12; n++) {
    if (lv.clef === 'mixed') { clef = Math.random() < 0.5 ? 'treble' : 'bass'; d = lv.pools ? lv.pools[clef][Math.floor(Math.random() * lv.pools[clef].length)] : lv.ranges ? rnd(...lv.ranges[clef]) : clef === 'treble' ? rnd(26, 42) : rnd(14, 30); }""", 'pools')
rep("""  const staff = lv.clef === 'grand' ? (d > 28 ? 'treble' : d < 28 ? 'bass' : (Math.random() < 0.5 ? 'treble' : 'bass')) : clef;
  return { kind: lv.kind, key: clef + d, d, clef, staff, answer: lv.kind === 'key' ? dToKey(d) : dName(d), uid };""",
    """  const staff = lv.clef === 'grand' ? (d > 28 ? 'treble' : d < 28 ? 'bass' : (Math.random() < 0.5 ? 'treble' : 'bass')) : clef;
  if (lv.kind === 'crown') return { kind: 'crown', key: 'cr' + clef + d + uid, d, clef, staff, answer: clef, uid };   // Phase 419: whose land?
  return { kind: lv.kind, key: clef + d, d, clef, staff, answer: lv.kind === 'key' ? dToKey(d) : dName(d), uid };""", 'crown kind')
rep("""const WHOLE_STAFF_DRILL = {
  id: 'whole-staff', label: 'The Whole Staff', levels: WHOLE_STAFF_LEVELS, generate: genStaffQuestion,
  check: STAFF_DRILL.check, answerLabel: STAFF_DRILL.answerLabel,
  Question: StaffQuestion, Learn: WholeStaffLearn,
};""", """const WHOLE_STAFF_DRILL = {
  id: 'whole-staff', label: 'The Whole Staff', levels: WHOLE_STAFF_LEVELS, generate: genStaffQuestion,
  check: STAFF_DRILL.check,
  answerLabel: (q) => q.kind === 'crown' ? (q.answer === 'treble' ? t('Queensland', '퀸즈랜드') : t('Kingsland', '킹스랜드')) + ' -- ' + withSolfa(dName(q.d)) : STAFF_DRILL.answerLabel(q),
  Question: (props) => props.q.kind === 'crown' ? <WsCrownQuestion {...props}/> : <StaffQuestion {...props}/>,
  Learn: WholeStaffLearn,
};""", 'drill object')

# 4. the tools speak the royal names; the two-ledger-line Cs go to chapter 6
i0 = s.index('const LANDMARKS = ['); i1 = s.index('];\n', i0) + 3
s = s[:i0] + """const LANDMARKS = [   // Phase 419: chapter 5's five landmarks, in the royal names (High C / Low C wait for chapter 6)
  { d: 28, get name() { return t('Clara\\'s C', '클라라의 C'); }, get tip() { return t('Princess Clara\\'s middle C, on her own little ladder rung between the two lands -- the middle of the piano.', '클라라 공주의 가운데 도, 두 나라 사이 자기만의 작은 사다리 발판 위 -- 피아노의 한가운데.'); } },
  { d: 32, get name() { return t('the Queen\\'s G', '여왕의 G'); }, get tip() { return t('The Queen\\'s curl wraps round this line: line 2 of Queensland.', '여왕의 소용돌이가 감싸는 줄: 퀸즈랜드의 2번 줄.'); } },
  { d: 24, get name() { return t('the King\\'s F', '왕의 F'); }, get tip() { return t('The King\\'s two dots guard this line: line 4 of Kingsland.', '왕의 두 점이 지키는 줄: 킹스랜드의 4번 줄.'); } },
  { d: 35, get name() { return t('Queensland C', '퀸즈랜드 C'); }, get tip() { return t('Space 3 of Queensland, one octave above Clara.', '퀸즈랜드의 3번 칸, 클라라보다 한 옥타브 위.'); } },
  { d: 21, get name() { return t('Kingsland C', '킹스랜드 C'); }, get tip() { return t('Space 2 of Kingsland, one octave below Clara.', '킹스랜드의 2번 칸, 클라라보다 한 옥타브 아래.'); } },
];
""" + s[i1:]
i0 = s.index('const HOP_MARKS = ['); i1 = s.index('];\n', i0) + 3
s = s[:i0] + """const HOP_MARKS = [   // Phase 419: the five landmarks of chapter 5
  { d: 21, get name() { return t('Kingsland C', '킹스랜드 C'); } }, { d: 24, get name() { return t('the King\\'s F', '왕의 F'); } }, { d: 28, get name() { return t('Clara\\'s C', '클라라의 C'); } },
  { d: 32, get name() { return t('the Queen\\'s G', '여왕의 G'); } }, { d: 35, get name() { return t('Queensland C', '퀸즈랜드 C'); } },
];
""" + s[i1:]
rep("""  const newD = (prev) => { let d; do { d = 15 + Math.floor(Math.random() * 27); } while (d === prev || HOP_MARKS.some(m => m.d === d)); return d; };""",
    """  const newD = (prev) => { let d; do { d = 17 + Math.floor(Math.random() * 23); } while (d === prev || HOP_MARKS.some(m => m.d === d)); return d; };   // the staves and the note just outside each""", 'hop range')
rep("""      <StaffFrame clef="grand" lo={14} hi={42} width={300}>
        {(yOf) => <>
          {step >= 0 && HOP_MARKS.map(m =>""", """      <StaffFrame clef="grand" lo={16} hi={40} width={300}>
        {(yOf) => <>
          {step >= 0 && HOP_MARKS.map(m =>""", 'hop frame')
i0 = s.index('const FOLD_PAIRS = ['); i1 = s.index('];\n', i0) + 3
s = s[:i0] + """const FOLD_PAIRS = [   // Phase 419: the two space Cs meet; High C / Low C (two ledger lines) wait for chapter 6
  { d: 35, color: '#e4572e', get label() { return t('Queensland C ↔ Kingsland C', '퀸즈랜드 C ↔ 킹스랜드 C'); } },
];
""" + s[i1:]
rep("  const topY = dY(44), botY = dY(12);", "  const topY = dY(41), botY = dY(15);", 'fold frame')
rep("""{t('Middle C sits right on the fold -- it is its own mirror.', '가운데 도는 접는 선 바로 위에 있어요 -- 자기 자신이 거울이에요.')}""",
    """{t('Clara\\'s C sits right on the fold -- it is its own mirror.', '클라라의 C는 접는 선 바로 위에 있어요 -- 자기 자신이 거울이에요.')}""", 'fold clara')
rep("""{t('Treble G line ↔ Bass F line -- the G clef curls round one, the F clef’s dots hug the other.', '높은음자리표 G 줄 ↔ 낮은음자리표 F 줄 -- G 음자리표는 한쪽을 감싸고, F 음자리표의 두 점은 다른 쪽을 감싸요.')}""",
    """{t('The Queen\\'s G line ↔ the King\\'s F line -- her curl wraps one, his two dots guard the other.', '여왕의 G 줄 ↔ 왕의 F 줄 -- 여왕의 소용돌이는 한쪽을 감싸고, 왕의 두 점은 다른 쪽을 지켜요.')}""", 'fold gf')
rep("""{t('Fold the staff at middle C', '가운데 도에서 오선 접기')}""", """{t('Fold the staff at Clara\\'s rung', '클라라의 발판에서 오선 접기')}""", 'fold title')

# 5. the sayings tool can stay in one land (pages 3 and 4 on screen)
rep("""function MnemonicStaff() {
  const [clef, setClef] = useState('treble');""", """function MnemonicStaff({ fixed }) {   // Phase 419: fixed = one land only (the book's Queensland and Kingsland pages)
  const [clef, setClef] = useState(fixed || 'treble');""", 'mnemonic fixed')
rep("""          {['treble', 'bass'].map(x => <button key={x} className={'chip' + (clef === x ? ' active' : '')} style={{padding:'3px 9px',fontSize:12}} onClick={() => setClef(x)}>{x === 'treble' ? t('𝄞 treble', '𝄞 높은음') : t('𝄢 bass', '𝄢 낮은음')}</button>)}""",
    """          {!fixed && ['treble', 'bass'].map(x => <button key={x} className={'chip' + (clef === x ? ' active' : '')} style={{padding:'3px 9px',fontSize:12}} onClick={() => setClef(x)}>{x === 'treble' ? t('𝄞 Queensland', '𝄞 퀸즈랜드') : t('𝄢 Kingsland', '𝄢 킹스랜드')}</button>)}""", 'mnemonic chips')

# 6. the toolbox names
rep("""{ id: 'rhymes', ch: 'whole-staff', title: 'Line and space rhymes', blurb: 'Every Good Boy... tap by tap.',""", """{ id: 'rhymes', ch: 'whole-staff', title: 'The sayings of the two lands', blurb: 'Queensland and Kingsland, line by line, tap by tap.',""", 'tool rhymes')
rep("""{ id: 'landmarks', ch: 'whole-staff', title: 'Landmark notes', blurb: 'Middle C, treble G, bass F, the Cs.',""", """{ id: 'landmarks', ch: 'whole-staff', title: 'The five landmarks', blurb: 'The Queen\\'s G, the King\\'s F, Clara\\'s C and the two space Cs.',""", 'tool landmarks')
rep("""{ id: 'landmark-hop', ch: 'whole-staff', title: 'Hop from a landmark', blurb: 'Guess the note, then count from a landmark.',""", """{ id: 'landmark-hop', ch: 'whole-staff', title: 'Hop from a landmark', blurb: 'Name the note, then hop from the nearest landmark.',""", 'tool hop')
rep("""{ id: 'fold', ch: 'whole-staff', title: 'Fold at middle C (grand staff)', blurb: 'The treble and bass staves are mirror images.',""", """{ id: 'fold', ch: 'whole-staff', title: 'Fold at Clara\\'s rung', blurb: 'The two lands are mirror images: G meets F, C meets C.',""", 'tool fold')
rep("""  'rhymes': ['줄과 칸 외우는 문장', 'Every Good Boy... 하나씩 눌러 봐요.'],""", """  'rhymes': ['두 나라의 외우는 문장', '퀸즈랜드와 킹스랜드, 줄 하나씩, 눌러 가며.'],""", 'ko rhymes')
rep("""  'landmarks': ['기준 음', '가운데 도, 높은음자리표 G, 낮은음자리표 F, 그리고 여러 C.'],""", """  'landmarks': ['다섯 랜드마크', '여왕의 G, 왕의 F, 클라라의 C, 그리고 칸에 있는 두 C.'],""", 'ko landmarks')
rep("""  'landmark-hop': ['기준 음에서 뛰어가기', '음을 맞혀 보고, 기준 음에서 세어 확인해요.'],""", """  'landmark-hop': ['랜드마크에서 뛰어가기', '음 이름을 말하고, 가장 가까운 랜드마크에서 뛰어 확인해요.'],""", 'ko hop')
rep("""  'fold': ['가운데 도에서 접기 (큰보표)', '높은음자리표와 낮은음자리표 오선은 거울처럼 마주 봐요.'],""", """  'fold': ['클라라의 발판에서 접기', '두 나라는 거울처럼 마주 봐요: G는 F와, C는 C와.'],""", 'ko fold')

# 7. Korean for the new level names
rep("const LEVEL_KO = {", """const LEVEL_KO = {
  'Crown check: whose land?': '왕관 확인: 어느 나라?', 'Queensland: every line and space': '퀸즈랜드: 모든 줄과 칸', 'Kingsland: every line and space': '킹스랜드: 모든 줄과 칸',
  'The five landmarks': '다섯 랜드마크', 'Landmark hop: a step or a skip away': '랜드마크에서 뛰기: 한 걸음이나 건너뛰기', 'Both lands, fast': '두 나라, 빠르게',""", 'level ko')

# 8. the five checks' foot line names what is there: circles to colour (all chapters)
rep("""    <div style={{fontSize:11.5,color:BK.muted}}>{t('Tick a box each time it gets better: not yet, then nearly, then got it!', '좋아질 때마다 한 칸씩 표시해요: 아직, 거의, 그리고 됐어요!')}</div>""",
    """    <div style={{fontSize:13,color:BK.muted}}>{t('Colour a circle each time it gets better: not yet, then nearly, then got it!', '좋아질 때마다 동그라미를 하나씩 칠해요: 아직, 거의, 그리고 됐어요!')}</div>""", 'checks foot')

open(src, 'w', encoding='utf-8').write(s); print('patch419 ok')
