#!/usr/bin/env python3
"""Build DG (on t781 -> t782). Sohyun 2026-10-30 13:18: the mixed Grades 2-3 rooms split by grade, as every other floor is.
Part 1: the split layer, and Intervals and Chords Further -> Intervals, Grade 2 (harmony-2: above the tonic in a minor key)
on the Grade 2 floor, and Chords and Cadences, Grade 3 (harmony-3: the degree names, root position and first inversion,
the four voices, perfect and plagal cadences) on the Grade 3 floor.
The layer: a sub-room keeps the base room's code. Its Lesson Book is the opener, the steps named and the check-up page,
renumbered (splitLb); its Workbook the pages facing those steps and the check-up with only its parts (splitWb, PaperParts);
its Teacher copy the base's, with the page numbers mapped and the other steps' blocks dropped (SplitCtx in TcBlock and
WbTop); its drill the base's levels named (splitDrill). The Home keeps the base id's lessons (LBH_FN) unchanged.
Old links `?drill=harmony-23` open harmony-3.
"""
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
def within(start, end, pairs):
    global s
    a = s.index(start); b = s.index(end, a); part = s[a:b]
    for old, new in pairs:
        assert part.count(old) == 1, (part.count(old), old[:100]); part = part.replace(old, new)
    s = s[:a] + part + s[b:]

# ── 1. the split layer ──
R("""const CkpKeyCtx = React.createContext(null);   // Build CX: a checkpoint key collects one Teacher copy's check-up answers
function TcBlock({ page, title, answers, watch, say, goBack }) {
  const K = React.useContext(CkpKeyCtx);""", """const CkpKeyCtx = React.createContext(null);   // Build CX: a checkpoint key collects one Teacher copy's check-up answers
// ─── Build DG: rooms split by grade (her 13:18). A sub-room shows some of a base room's steps; the base code is shared. ───
// { steps: the base step numbers kept, in order; secs: the check-up parts kept; pages: base page -> this room's page }
const SplitCtx = React.createContext(null);
const splitMap = (steps, last) => { const m = { 1: 1 }; steps.forEach((st, i) => { m[st + 1] = i + 2; }); m[last] = steps.length + 2; return m; };
function splitLb(pages, steps) {   // a Lesson Book: the opener, the steps named, the check-up page; renumbered
  const last = pages.length, keep = [pages[0]].concat(steps.map(st => pages[st])).concat([pages[last - 1]]);
  return keep.map((pg, i) => React.cloneElement(pg, { key: String(i + 1), no: i + 1, kicker: i > 0 && i < keep.length - 1 && pg.props.kicker ? String(pg.props.kicker).replace(/\\d+/, String(i)) : pg.props.kicker }));
}
function splitWb(pages, steps, secs, startNo = 1) {   // a Workbook: the pages facing the steps, then the check-up with its parts
  const last = pages.length, keep = steps.map(st => pages[st - 1]).concat([pages[last - 1]]);
  return keep.map((pg, i) => <SplitCtx.Provider key={i} value={{ steps, secs, pages: splitMap(steps, last + 1), step: i < steps.length ? i + 1 : null }}>{React.cloneElement(pg, { no: startNo + 1 + i, children: i === steps.length ? <PaperParts secs={secs}>{pg.props.children}</PaperParts> : pg.props.children })}</SplitCtx.Provider>);
}
function PaperParts({ secs, children }) {   // the check-up page with only the parts named (the others hidden, their numbers kept)
  const box = useRef(null);
  React.useLayoutEffect(() => {
    const el = box.current && box.current.querySelector('.lb-paper'); if (!el) return; let cur = null;
    [...el.children].forEach(c => { const sec = c.getAttribute('data-sec'); if (sec != null) cur = sec; const on = cur == null || cur.split(' · ').some(L => secs.includes(L)); if (!on) c.style.display = 'none'; });   // a shown part keeps its own display (flex, grid)
  });
  return <div ref={box} style={{display:'contents'}}>{children}</div>;
}
function TcBlock({ page, title, answers, watch, say, goBack }) {
  const K = React.useContext(CkpKeyCtx), SP = React.useContext(SplitCtx);
  if (SP && !K) {   // a sub-room's Teacher copy: only its steps' blocks, their pages renumbered, the check-up's parts filtered
    if (!SP.pages[page]) return null;
    const kids = React.Children.toArray(answers && answers.props && answers.props.children !== undefined ? answers.props.children : answers);
    const chk = /^(The check-up on paper|Check-up)/.test(title || '');
    const ans = chk ? kids.filter(c => !(c && c.props && c.props['data-sec'] != null) || String(c.props['data-sec']).split(' · ').some(L => SP.secs.includes(L))) : kids;
    return <SplitCtx.Provider value={null}><TcBlock page={SP.pages[page]} title={title} answers={<>{ans}</>} watch={watch} say={say} goBack={chk ? null : goBack}/></SplitCtx.Provider>;
  }""")
R("""function WbTop({ step }) {
  const chId = React.useContext(BkChapterCtx);""", """function WbTop({ step }) {
  const chId = React.useContext(BkChapterCtx), SP = React.useContext(SplitCtx);
  if (SP && SP.step) step = SP.step;   // Build DG: a sub-room's own step number""")
R("""const alias = { 'letter-chain': 'note-names', 'finger-numbers': 'posture-hands', 'five-finger': 'reading-steps', 'scale-fingering': 'scales' };""",
  """const alias = { 'letter-chain': 'note-names', 'finger-numbers': 'posture-hands', 'five-finger': 'reading-steps', 'scale-fingering': 'scales', ...SPLIT_OLD };""", 2)
R("""function bkChapterName(id) { const d = DRILLS.find(x => x.id === id); return d ? d.label : id; }""",
  """function bkChapterName(id) { const d = DRILLS.find(x => x.id === id); return d ? d.label : SPLIT_OLD[id] ? bkChapterName(SPLIT_OLD[id]) : id; }""")
# the teacher's Workbook pages carry the split too (a sub-room's Teacher copy is drawn inside splitWb's providers below)

# ── 2. Intervals and Chords Further -> harmony-2 and harmony-3 ──
R("""const HARMONY_23_DRILL = { id: 'harmony-23', label: 'Intervals and Chords Further' };   // Build AL: Grades 2-3 theory""",
  """// Build DG: a sub-room's drill is the base's levels named (the rest of the split layer sits by TcBlock)
const splitDrill = (d, base, levels, Learn) => Object.defineProperties(d, { levels: { get: () => (base.allLevels || base.levels).filter(l => levels.includes(l.n)) }, generate: { value: (lv, prev) => base.generate(lv, prev) }, check: { value: (q, a) => base.check(q, a) }, answerLabel: { value: (q) => base.answerLabel(q) }, Question: { get: () => base.Question }, noPrint: { get: () => base.noPrint }, Learn: { value: Learn } });
const SPLIT_OLD = { 'harmony-23': 'harmony-3' };   // old links to the rooms that were split
const HARMONY_23_DRILL = { id: 'harmony-23', label: 'Intervals and Chords Further' };   // Build AL: Grades 2-3 theory; Build DG: the base of harmony-2 and harmony-3
const HARMONY_2_DRILL = { id: 'harmony-2', label: 'Intervals, Grade 2' };   // Build DG
const HARMONY_3_DRILL = { id: 'harmony-3', label: 'Chords and Cadences, Grade 3' };   // Build DG""")
R("""  { id: 'harmony-23', label: 'Intervals and Chords Further', concept: HARMONY_23_DRILL, track: 'start' },   // Build AL""",
  """  { id: 'harmony-2', label: 'Intervals, Grade 2', concept: HARMONY_2_DRILL, track: 'start' },   // Build DG
  { id: 'harmony-3', label: 'Chords and Cadences, Grade 3', concept: HARMONY_3_DRILL, track: 'start' },   // Build DG""")
R("""'harmony-23': '음정과 화음 한 걸음 더'""", """'harmony-2': '음정, Grade 2', 'harmony-3': '화음과 종지, Grade 3'""")
R("""'harmony-23': ['Chords further', '화음 더']""", """'harmony-2': ['Intervals 2', '음정 2'], 'harmony-3': ['Chords 3', '화음 3']""")
R("""'harmony-23': ['intervals', 'chords']""", """'harmony-2': ['intervals', 'minor-scales'], 'harmony-3': ['harmony-2', 'chords']""")
R("""  'harmony-23': 'intervals chords grade 2 grade 3 theory above the tonic major minor perfect bass clef degree names tonic supertonic mediant subdominant dominant submediant leading note primary triads first inversion soprano alto tenor bass four part vocal cadence perfect plagal',""",
  """  'harmony-2': 'intervals grade 2 theory above the tonic minor key major minor perfect number quality treble clef',
  'harmony-3': 'chords grade 3 theory bass clef degree names tonic supertonic mediant subdominant dominant submediant leading note primary triads root position first inversion soprano alto tenor bass four part vocal cadence perfect plagal',""")
R("""'harmony-23': 'p-chords'""", """'harmony-2': 'p-intervals', 'harmony-3': 'p-chords'""")
R("""  { ids: ['listen-23', 'melody', 'scales-23'], en: ['Grade 2',""", """  { ids: ['listen-23', 'melody', 'scales-23', 'harmony-2'], en: ['Grade 2',""")
R("""  { ids: ['listen-3', 'harmony-23', 'rhythm-23'], en: ['Grade 3',""", """  { ids: ['listen-3', 'harmony-3', 'rhythm-23'], en: ['Grade 3',""")
R("""  'harmony-23': [1, 2, 3, 4, 5, 6], 'rhythm-23': [1, 2, 3, 4, 5, 6],""", """  'harmony-2': [1, 2], 'harmony-3': [3, 4, 5, 6], 'rhythm-23': [1, 2, 3, 4, 5, 6],""")
R("""  melody: 2, 'harmony-23': 3, 'rhythm-23': 3,""", """  melody: 2, 'harmony-2': 2, 'harmony-3': 3, 'rhythm-23': 3,""")
R("""  { id: 'mk-choir', ch: 'harmony-23',""", """  { id: 'mk-choir', ch: 'harmony-3',""")
R("""lessons: ['h3-iv', 'h3-deg', 'h3-inv', 'h3-satb', 'h3-cad', 'mk-choir'], check: 'harmony-23' }""", """lessons: ['h3-iv', 'h3-deg', 'h3-inv', 'h3-satb', 'h3-cad', 'mk-choir'], check: 'harmony-3' }""")

# the book: g picks the room; the opener's lists and words follow
within("function h3LbPages(scr = false) {", "function Harmony23LessonBook()", [
 ("function h3LbPages(scr = false) {\n  const ch = 'harmony-23', iv = bkChapterNo('intervals'), cd = bkChapterNo('chords');",
  "function h3LbPages(scr = false, g) {   // Build DG: g = 2 (step 1) or 3 (steps 2 to 5); no g: every page (the Home)\n  const ch = g === 2 ? 'harmony-2' : g === 3 ? 'harmony-3' : 'harmony-23', iv = bkChapterNo('intervals'), cd = bkChapterNo('chords');\n  const STEPS = g === 2 ? [1] : g === 3 ? [2, 3, 4, 5] : [1, 2, 3, 4, 5];"),
 ("  const toc = [[t('Above the tonic, in a minor key', '단조에서 으뜸음 위의 음정'), 2], [t('The degree names', '음계 음의 이름'), 3], [t('Root position and first inversion', '기본 위치와 제1전위'), 4], [t('Soprano, alto, tenor, bass', '소프라노, 알토, 테너, 베이스'), 5], [t('Perfect and plagal cadences', '정격종지와 변격종지'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];",
  "  const tocAll = [t('Above the tonic, in a minor key', '단조에서 으뜸음 위의 음정'), t('The degree names', '음계 음의 이름'), t('Root position and first inversion', '기본 위치와 제1전위'), t('Soprano, alto, tenor, bass', '소프라노, 알토, 테너, 베이스'), t('Perfect and plagal cadences', '정격종지와 변격종지')];\n  const nw = ['', 'one', 'two', 'three', 'four', 'five'][STEPS.length], nk = ['', '한', '두', '세', '네', '다섯'][STEPS.length], checksT = t('My ' + nw + ' check' + (STEPS.length > 1 ? 's' : ''), '나의 ' + nk + ' 가지 확인');\n  const toc = STEPS.map((st, i) => [tocAll[st - 1], i + 2]).concat([[checksT, STEPS.length + 2]]);\n  const checks = checks5.filter((_, i) => STEPS.includes(i + 1));"),
 ("<div style={{fontFamily:LB_SERIF,fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Intervals and Chords Further', '음정과 화음 한 걸음 더')}</div>",
  "<div style={{fontFamily:LB_SERIF,fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{g === 2 ? t('Intervals, Grade 2', '음정, Grade 2') : g === 3 ? t('Chords and Cadences, Grade 3', '화음과 종지, Grade 3') : t('Intervals and Chords Further', '음정과 화음 한 걸음 더')}</div>"),
 ("<LbPic h={170}><div style={{width:'100%',maxWidth:scr ? 300 : 420,margin:'0 auto'}}><SatbStaff chords={h3CadChords('C', 'perfect')} labels={['V', 'I']} width={W}/></div></LbPic>",
  "{g === 2 ? <LbPic h={170}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:560,margin:'0 auto'}}>{ivStill('Am', 'treble')}</div></LbPic> : <LbPic h={170}><div style={{width:'100%',maxWidth:scr ? 300 : 420,margin:'0 auto'}}><SatbStaff chords={h3CadChords('C', 'perfect')} labels={['V', 'I']} width={W}/></div></LbPic>}"),
 ("<LbSay size={18}>{t('Theory for Grades 2 and 3: intervals in minor keys, the names of the degrees, chords turned over, four voices, and the two cadences that end a piece.', '2·3급 이론: 단조의 음정, 음계 음의 이름, 자리를 바꾼 화음, 네 성부, 그리고 곡을 끝내는 두 종지.')}</LbSay>",
  "<LbSay size={18}>{g === 2 ? t('Theory for Grade 2: the intervals above the tonic, now in a minor key too, by number and quality.', '2급 이론: 으뜸음 위의 음정, 이제 단조에서도, 숫자와 성질로.') : g === 3 ? t('Theory for Grade 3: the names of the degrees, chords turned over, four voices, and the two cadences that end a piece.', '3급 이론: 음계 음의 이름, 자리를 바꾼 화음, 네 성부, 그리고 곡을 끝내는 두 종지.') : t('Theory for Grades 2 and 3: intervals in minor keys, the names of the degrees, chords turned over, four voices, and the two cadences that end a piece.', '2·3급 이론: 단조의 음정, 음계 음의 이름, 자리를 바꾼 화음, 네 성부, 그리고 곡을 끝내는 두 종지.')}</LbSay>"),
 ("<LbGuess q={t('In a minor key, the 3rd above the tonic: major or minor?', '단조에서 으뜸음 위의 3도는 장3도일까요, 단3도일까요?')} a={t('Minor. The 6th too.', '단3도예요. 6도도 단음정.')} page={2}/>",
  "{g === 3 ? <LbGuess q={t('The dominant is a 5th above the tonic. Where is the subdominant?', '딸림음은 으뜸음의 5도 위예요. 버금딸림음은 어디일까요?')} a={t('A 5th below the tonic.', '으뜸음의 5도 아래.')} page={2}/> : <LbGuess q={t('In a minor key, the 3rd above the tonic: major or minor?', '단조에서 으뜸음 위의 3도는 장3도일까요, 단3도일까요?')} a={t('Minor. The 6th too.', '단3도예요. 6도도 단음정.')} page={2}/>}"),
 ("{[t('name any interval above the tonic, major or minor key', '장조든 단조든 으뜸음 위의 음정을 말할 수 있어요'), t('name every degree of the scale', '음계의 모든 음의 이름을 말할 수 있어요'), t('write I, IV and V in root position and first inversion', 'I, IV, V를 기본 위치와 제1전위로 쓸 수 있어요'), t('write a perfect and a plagal cadence in four parts', '정격종지와 변격종지를 네 성부로 쓸 수 있어요')].map(",
  "{[[1, t('name any interval above the tonic, major or minor key', '장조든 단조든 으뜸음 위의 음정을 말할 수 있어요')], [2, t('name every degree of the scale', '음계의 모든 음의 이름을 말할 수 있어요')], [3, t('write I, IV and V in root position and first inversion', 'I, IV, V를 기본 위치와 제1전위로 쓸 수 있어요')], [5, t('write a perfect and a plagal cadence in four parts', '정격종지와 변격종지를 네 성부로 쓸 수 있어요')]].filter(([st]) => STEPS.includes(st)).map(([, x]) => x).map("),
 ("<LbPage key=\"7\" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}",
  "<LbPage key=\"7\" no={7} chId={ch} kicker={t('Check-up', '점검')} title={checksT}"),
 ("<LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey=\"pb_h3_five\"/>}/>",
  "<LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey={'pb_h3_five' + (g || '')}/>}/>"),
 ("    </LbPage>,\n  ];\n}\n", "    </LbPage>,\n  ];\n  return g ? splitLb(pages, STEPS) : pages;\n}\n"),
 ("  return [\n    <LbPage key=\"1\" no={1} chId={ch} teacher={<>{t('Theory of Music, Grades 2 and 3:", "  const pages = [\n    <LbPage key=\"1\" no={1} chId={ch} teacher={<>{t('Theory of Music, Grades 2 and 3:"),
])
# the Learn, the registry, the drills
R("""function Harmony23LessonBook() { return <>{h3LbPages(false)}</>; }
function H3Learn({ onStart }) {
  const pages = h3LbPages(true), opener = pages[0];
  return (
    <Lesson id="harmony-23" title={t('Intervals and Chords Further', '음정과 화음 한 걸음 더')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="harmony-23">""",
  """function Harmony2LessonBook() { return <>{h3LbPages(false, 2)}</>; }
function Harmony3LessonBook() { return <>{h3LbPages(false, 3)}</>; }
function H3Learn({ onStart, g = 3 }) {
  const pages = h3LbPages(true, g), opener = pages[0], id = g === 2 ? 'harmony-2' : 'harmony-3';
  return (
    <Lesson id={id} title={g === 2 ? t('Intervals, Grade 2', '음정, Grade 2') : t('Chords and Cadences, Grade 3', '화음과 종지, Grade 3')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value={id}>""")
R("""Object.assign(HARMONY_23_DRILL, { levels: H3_LEVELS, generate: genH3Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: h3AnswerLabel, Question: H3Question, Learn: H3Learn });""",
  """Object.assign(HARMONY_23_DRILL, { levels: H3_LEVELS, generate: genH3Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: h3AnswerLabel, Question: H3Question, Learn: H3Learn });
splitDrill(HARMONY_2_DRILL, HARMONY_23_DRILL, [1, 2], (p) => <H3Learn g={2} {...p}/>);   // Build DG
splitDrill(HARMONY_3_DRILL, HARMONY_23_DRILL, [3, 4, 5, 6], (p) => <H3Learn g={3} {...p}/>);""")
# the Workbook and the Teacher copy
R("""function H3Workbook({ startNo = 1 }) {
  const W = H3_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="harmony-23">{content}</WbPage>);""",
  """function H3Workbook({ startNo = 1, g = 3 }) {   // Build DG: g = 2 (step 1) or 3 (steps 2 to 5)
  const W = H3_WB, pages = [], ch = g === 2 ? 'harmony-2' : 'harmony-3';
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId={ch}>{content}</WbPage>);""")
R("""  P(<H3PaperCheck/>);
  return <>{pages}</>;
}
function H3PaperCheck() {""", """  P(<H3PaperCheck/>);
  return <>{splitWb(pages, g === 2 ? [1] : [2, 3, 4, 5], g === 2 ? ['A'] : ['B', 'C', 'D'], startNo)}</>;
}
function H3PaperCheck() {""")
R("""function H3Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="harmony-23" teacher>{content}</WbPage>);""",
  """function H3Teacher({ g = 3 }) {   // Build DG: g = 2 (step 1) or 3 (steps 2 to 5); the blocks map themselves (SplitCtx in TcBlock)
  const pages = [], ch = g === 2 ? 'harmony-2' : 'harmony-3', STEPS = g === 2 ? [1] : [2, 3, 4, 5], secs = g === 2 ? ['A'] : ['B', 'C', 'D'];
  const P = (content) => pages.push(<SplitCtx.Provider key={pages.length} value={{ steps: STEPS, secs, pages: splitMap(STEPS, 7) }}><WbPage no={pages.length + 1} chId={ch} teacher>{content}</WbPage></SplitCtx.Provider>);""")
R("""    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('harmony-23')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music, Grades 2 and 3. Every answer""",
  """    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName(ch)}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music, Grade {g}. Every answer""")
# the Grade 2 room's check-up stays in the treble clef (the bass clef is Grade 3)
R("""function H3PaperCheck() {
  const C = H3_WB.chk;""", """function H3PaperCheck() {
  const SP = React.useContext(SplitCtx), C = SP && SP.steps.length === 1 ? { ...H3_WB.chk, iv: H3_WB.chk.iv.map(it => [it[0], it[1], 'treble']) } : H3_WB.chk;   // Build DG: Grade 2, treble only""")
R("""Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.6. Then play each one at the piano.""",
  """Not passed? Go back to that step's page: {g === 2 ? 'A p.2' : 'B p.2 · C p.3 · D p.5'}. Then play each one at the piano.""")
R("""WORKBOOKS['harmony-23'] = H3Workbook;""", """WORKBOOKS['harmony-2'] = () => <H3Workbook g={2}/>;   // Build DG
WORKBOOKS['harmony-3'] = () => <H3Workbook g={3}/>;""")
R("""TEACHER_COPIES['harmony-23'] = H3Teacher;""", """TEACHER_COPIES['harmony-2'] = () => <H3Teacher g={2}/>;   // Build DG
TEACHER_COPIES['harmony-3'] = () => <H3Teacher g={3}/>;""")
# the registries of books
R("""'harmony-23': Harmony23LessonBook,""", """'harmony-2': Harmony2LessonBook, 'harmony-3': Harmony3LessonBook,""")
R("""'harmony-23': h3LbPages,""", """'harmony-2': (s) => h3LbPages(s, 2), 'harmony-3': (s) => h3LbPages(s, 3),""")
# the checkpoints
R("""  'harmony-23': { secs: ['B', 'D'], back: { B: [2, 3], D: [5, 6] }, Paper: () => <H3PaperCheck/> },""",
  """  'harmony-2': { secs: ['A'], back: { A: [1, 2] }, Paper: () => <SplitCtx.Provider value={{ steps: [1], secs: ['A'], pages: {} }}><H3PaperCheck/></SplitCtx.Provider> },   // Build DG
  'harmony-3': { secs: ['B', 'D'], back: { B: [1, 2], D: [4, 5] }, Paper: () => <H3PaperCheck/> },""")
R("""const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23']], '4': [['listen-3', 'harmony-23'], ['rhythm-23']],""",
  """const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23', 'harmony-2']], '4': [['listen-3', 'harmony-3'], ['rhythm-23']],""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
