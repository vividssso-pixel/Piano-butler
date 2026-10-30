#!/usr/bin/env python3
"""Build DH (on t782 -> t783): the split, part 2. Rhythm Further -> Rhythm, Grade 2 (rhythm-2: semiquavers; triplets and
duplets) on the Grade 2 floor, and Rhythm, Grade 3 (rhythm-3: the dotted quaver and semiquaver, the minim beat, 3/8 and 9/8,
and 'Listen: which line?') on the Grade 3 floor. Same layer as DG (splitLb, splitWb, SplitCtx, splitDrill).
"""
import sys
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

R("""const SPLIT_OLD = { 'harmony-23': 'harmony-3' };""", """const SPLIT_OLD = { 'harmony-23': 'harmony-3', 'rhythm-23': 'rhythm-3' };""")
R("""const RHYTHM_23_DRILL = { id: 'rhythm-23', label: 'Rhythm Further' };""",
  """const RHYTHM_23_DRILL = { id: 'rhythm-23', label: 'Rhythm Further' };   // Build DH: the base of rhythm-2 and rhythm-3
const RHYTHM_2_DRILL = { id: 'rhythm-2', label: 'Rhythm, Grade 2' };   // Build DH
const RHYTHM_3_DRILL = { id: 'rhythm-3', label: 'Rhythm, Grade 3' };""")
R("""  { id: 'rhythm-23', label: 'Rhythm Further', concept: RHYTHM_23_DRILL, track: 'start' },   // Build AM""",
  """  { id: 'rhythm-2', label: 'Rhythm, Grade 2', concept: RHYTHM_2_DRILL, track: 'start' },   // Build DH
  { id: 'rhythm-3', label: 'Rhythm, Grade 3', concept: RHYTHM_3_DRILL, track: 'start' },   // Build DH""")
R("""'rhythm-23': '리듬 한 걸음 더'""", """'rhythm-2': '리듬, Grade 2', 'rhythm-3': '리듬, Grade 3'""")
R("""'rhythm-23': ['Rhythm further', '리듬 더']""", """'rhythm-2': ['Rhythm 2', '리듬 2'], 'rhythm-3': ['Rhythm 3', '리듬 3']""")
R("""'rhythm-23': ['rhythm', 'six-eight']""", """'rhythm-2': ['rhythm', 'six-eight'], 'rhythm-3': ['rhythm-2']""")
R("""  'rhythm-23': 'rhythm grade 2 grade 3 semiquavers dotted quaver triplet duplet minim beat 2/2 3/2 cut common time 3/8 9/8 compound triple anacrusis rests time signatures',""",
  """  'rhythm-2': 'rhythm grade 2 semiquavers four to a beat 1 e + a triplet three for two duplet two for three',
  'rhythm-3': 'rhythm grade 3 dotted quaver semiquaver long short minim beat 2/2 3/2 cut common time 3/8 9/8 compound triple simple time signatures listen which line',""")
R("""'rhythm-23': 'r-beat'""", """'rhythm-2': 'r-beat', 'rhythm-3': 'r-beat'""")
R("""  { ids: ['listen-23', 'melody', 'scales-23', 'harmony-2'], en: ['Grade 2',""", """  { ids: ['listen-23', 'melody', 'scales-23', 'harmony-2', 'rhythm-2'], en: ['Grade 2',""")
R("""  { ids: ['listen-3', 'harmony-3', 'rhythm-23'], en: ['Grade 3',""", """  { ids: ['listen-3', 'harmony-3', 'rhythm-3'], en: ['Grade 3',""")
R("""  'harmony-2': [1, 2], 'harmony-3': [3, 4, 5, 6], 'rhythm-23': [1, 2, 3, 4, 5, 6],""", """  'harmony-2': [1, 2], 'harmony-3': [3, 4, 5, 6], 'rhythm-2': [1, 3], 'rhythm-3': [2, 4, 5, 6],""")
R("""  melody: 2, 'harmony-2': 2, 'harmony-3': 3, 'rhythm-23': 3,""", """  melody: 2, 'harmony-2': 2, 'harmony-3': 3, 'rhythm-2': 2, 'rhythm-3': 3,""")
R("""  { id: 'mk-split', ch: 'rhythm-23',""", """  { id: 'mk-split', ch: 'rhythm-3',""")
R("""lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98', 'mk-split'], check: 'rhythm-23' }""", """lessons: ['r2-semi', 'r2-dot', 'r2-trip', 'r2-minim', 'r2-98', 'mk-split'], check: 'rhythm-3' }""")
R("""  const ch = 'rhythm-4', r2c = bkChapterNo('rhythm-23');""", """  const ch = 'rhythm-4', r2c = bkChapterNo('rhythm-3');""")

within("function r2LbPages(scr = false) {", "function Rhythm23LessonBook()", [
 ("function r2LbPages(scr = false) {\n  const ch = 'rhythm-23', rh = bkChapterNo('rhythm'), e8 = bkChapterNo('six-eight');",
  "function r2LbPages(scr = false, g) {   // Build DH: g = 2 (steps 1 and 3) or 3 (steps 2, 4, 5); no g: every page (the Home)\n  const ch = g === 2 ? 'rhythm-2' : g === 3 ? 'rhythm-3' : 'rhythm-23', rh = bkChapterNo('rhythm'), e8 = bkChapterNo('six-eight');\n  const STEPS = g === 2 ? [1, 3] : g === 3 ? [2, 4, 5] : [1, 2, 3, 4, 5];"),
 ("  const toc = [[t('Semiquavers', '16분음표'), 2], [t('Dotted quaver and semiquaver', '점8분음표와 16분음표'), 3], [t('Triplets and duplets', '셋잇단음표와 2잇단음표'), 4], [t('The minim beat', '2분음표 박'), 5], [t('3/8 and 9/8', '3/8과 9/8'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]]",
  "  const tocAll = [t('Semiquavers', '16분음표'), t('Dotted quaver and semiquaver', '점8분음표와 16분음표'), t('Triplets and duplets', '셋잇단음표와 2잇단음표'), t('The minim beat', '2분음표 박'), t('3/8 and 9/8', '3/8과 9/8')];\n  const nw = ['', 'one', 'two', 'three', 'four', 'five'][STEPS.length], nk = ['', '한', '두', '세', '네', '다섯'][STEPS.length], checksT = t('My ' + nw + ' checks', '나의 ' + nk + ' 가지 확인');\n  const toc = STEPS.map((st, i) => [tocAll[st - 1], i + 2]).concat([[checksT, STEPS.length + 2]]);\n  const checks = checks5.filter((_, i) => STEPS.includes(i + 1));"),
 ("<div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Rhythm Further', '리듬 한 걸음 더')}</div>",
  "<div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{g === 2 ? t('Rhythm, Grade 2', '리듬, Grade 2') : g === 3 ? t('Rhythm, Grade 3', '리듬, Grade 3') : t('Rhythm Further', '리듬 한 걸음 더')}</div>"),
 ("      {still(['semiB', 'e98'])}\n", "      {still(g === 2 ? ['semiA', 'tripA'] : g === 3 ? ['dotA', 'e98'] : ['semiB', 'e98'])}\n"),
 ("<LbSay size={18}>{t('Rhythm for Grades 2 and 3: smaller notes inside the beat, long and short, three for two, the minim beat, and nine quavers in a bar.', '2·3급 리듬: 박 안의 더 작은 음표, 길게 짧게, 둘 자리에 셋, 2분음표 박, 그리고 한 마디에 8분음표 아홉.')}</LbSay>",
  "<LbSay size={18}>{g === 2 ? t('Rhythm for Grade 2: four notes inside one beat, and three where two go.', '2급 리듬: 한 박 안에 음 넷, 그리고 둘 자리에 셋.') : g === 3 ? t('Rhythm for Grade 3: long and short inside the beat, the minim beat, and nine quavers in a bar.', '3급 리듬: 박 안의 길게 짧게, 2분음표 박, 그리고 한 마디에 8분음표 아홉.') : t('Rhythm for Grades 2 and 3: smaller notes inside the beat, long and short, three for two, the minim beat, and nine quavers in a bar.', '2·3급 리듬: 박 안의 더 작은 음표, 길게 짧게, 둘 자리에 셋, 2분음표 박, 그리고 한 마디에 8분음표 아홉.')}</LbSay>"),
 ("<LbGuess q={t('Four semiquavers under two beams: how many beats?', '빔 두 개로 묶인 16분음표 넷: 몇 박일까요?')} a={t('One beat, shared four ways: 1 e + a.', '한 박을 넷이 나눠요: 1 e + a.')} page={2}/>",
  "{g === 3 ? <LbGuess q={t('A dotted quaver and a semiquaver: which one comes last, on a?', '점8분음표와 16분음표: 어느 쪽이 마지막 a에 올까요?')} a={t('The semiquaver: long, short.', '16분음표예요. 길게, 짧게.')} page={2}/> : <LbGuess q={t('Four semiquavers under two beams: how many beats?', '빔 두 개로 묶인 16분음표 넷: 몇 박일까요?')} a={t('One beat, shared four ways: 1 e + a.', '한 박을 넷이 나눠요: 1 e + a.')} page={2}/>}"),
 ("{[t('count and clap semiquavers and the dotted quaver', '16분음표와 점8분음표를 세고 칠 수 있어요'), t('fit three where two go, and two where three go', '둘 자리에 셋, 셋 자리에 둘을 넣을 수 있어요'), t('count in 2/2, 3/2, 3/8 and 9/8', '2/2, 3/2, 3/8, 9/8로 셀 수 있어요'), t('say whether a time signature is simple or compound', '박자표가 홑박자인지 겹박자인지 말할 수 있어요')].map(",
  "{(g === 2 ? [t('count and clap four semiquavers to a beat: 1 e + a', '한 박에 16분음표 넷을 세고 칠 수 있어요: 1 e + a'), t('fit three where two go, and two where three go', '둘 자리에 셋, 셋 자리에 둘을 넣을 수 있어요')] : g === 3 ? [t('clap the dotted quaver and semiquaver: long, short', '점8분음표와 16분음표를 칠 수 있어요: 길게, 짧게'), t('count in 2/2, 3/2, 3/8 and 9/8', '2/2, 3/2, 3/8, 9/8로 셀 수 있어요'), t('say whether a time signature is simple or compound', '박자표가 홑박자인지 겹박자인지 말할 수 있어요')] : [t('count and clap semiquavers and the dotted quaver', '16분음표와 점8분음표를 세고 칠 수 있어요'), t('fit three where two go, and two where three go', '둘 자리에 셋, 셋 자리에 둘을 넣을 수 있어요'), t('count in 2/2, 3/2, 3/8 and 9/8', '2/2, 3/2, 3/8, 9/8로 셀 수 있어요'), t('say whether a time signature is simple or compound', '박자표가 홑박자인지 겹박자인지 말할 수 있어요')]).map("),
 ("<LbPage key=\"7\" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}", "<LbPage key=\"7\" no={7} chId={ch} kicker={t('Check-up', '점검')} title={checksT}"),
 ("<LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey=\"pb_r2_five\"/>}/>",
  "<LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey={'pb_r2_five' + (g || '')}/>}/>"),
 ("  return [\n    <LbPage key=\"1\" no={1} chId={ch} teacher={<>{t('Theory of Music, Grades 2 and 3, Time and Rhythm:", "  const pages = [\n    <LbPage key=\"1\" no={1} chId={ch} teacher={<>{t('Theory of Music, Grades 2 and 3, Time and Rhythm:"),
 ("    </LbPage>,\n  ];\n}\n", "    </LbPage>,\n  ];\n  return g ? splitLb(pages, STEPS) : pages;\n}\n"),
])
R("""function Rhythm23LessonBook() { return <>{r2LbPages(false)}</>; }
function R2Learn({ onStart }) {
  const pages = r2LbPages(true), opener = pages[0];
  return (
    <Lesson id="rhythm-23" title={t('Rhythm Further', '리듬 한 걸음 더')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="rhythm-23">""",
  """function Rhythm2LessonBook() { return <>{r2LbPages(false, 2)}</>; }
function Rhythm3LessonBook() { return <>{r2LbPages(false, 3)}</>; }
function R2Learn({ onStart, g = 3 }) {
  const pages = r2LbPages(true, g), opener = pages[0], id = g === 2 ? 'rhythm-2' : 'rhythm-3';
  return (
    <Lesson id={id} title={g === 2 ? t('Rhythm, Grade 2', '리듬, Grade 2') : t('Rhythm, Grade 3', '리듬, Grade 3')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value={id}>""")
R("""Object.assign(RHYTHM_23_DRILL, { levels: R2_LEVELS, generate: genR2Question,""", """splitDrill(RHYTHM_2_DRILL, RHYTHM_23_DRILL, [1, 3], (p) => <R2Learn g={2} {...p}/>);   // Build DH
splitDrill(RHYTHM_3_DRILL, RHYTHM_23_DRILL, [2, 4, 5, 6], (p) => <R2Learn g={3} {...p}/>);
Object.assign(RHYTHM_23_DRILL, { levels: R2_LEVELS, generate: genR2Question,""")
R("""function R2Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="rhythm-23" teacher>{content}</WbPage>);""",
  """function R2Teacher({ g = 3 }) {   // Build DH: g = 2 (steps 1 and 3) or 3 (steps 2, 4, 5)
  const pages = [], ch = g === 2 ? 'rhythm-2' : 'rhythm-3', STEPS = g === 2 ? [1, 3] : [2, 4, 5], secs = g === 2 ? ['B'] : ['A', 'C', 'D'];
  const P = (content) => pages.push(<SplitCtx.Provider key={pages.length} value={{ steps: STEPS, secs, pages: splitMap(STEPS, 7) }}><WbPage no={pages.length + 1} chId={ch} teacher>{content}</WbPage></SplitCtx.Provider>);""")
R("""    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('rhythm-23')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grades 2 and 3, Time and Rhythm.""",
  """    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName(ch)}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Theory of Music Grade {g}, Time and Rhythm.""")
R("""function R2Workbook({ startNo = 1 }) {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="rhythm-23">{content}</WbPage>);""",
  """function R2Workbook({ startNo = 1, g = 3 }) {   // Build DH
  const pages = [], ch = g === 2 ? 'rhythm-2' : 'rhythm-3';
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId={ch}>{content}</WbPage>);""")
R("""  P(<R2PaperCheck/>);
  return <>{pages}</>;
}""", """  P(<R2PaperCheck/>);
  return <>{splitWb(pages, g === 2 ? [1, 3] : [2, 4, 5], g === 2 ? ['B'] : ['A', 'C', 'D'], startNo)}</>;
}""")
R("""WORKBOOKS['rhythm-23'] = R2Workbook;""", """WORKBOOKS['rhythm-2'] = () => <R2Workbook g={2}/>;   // Build DH
WORKBOOKS['rhythm-3'] = () => <R2Workbook g={3}/>;""")
R("""TEACHER_COPIES['rhythm-23'] = R2Teacher;""", """TEACHER_COPIES['rhythm-2'] = () => <R2Teacher g={2}/>;   // Build DH
TEACHER_COPIES['rhythm-3'] = () => <R2Teacher g={3}/>;""")
R("""'rhythm-23': Rhythm23LessonBook,""", """'rhythm-2': Rhythm2LessonBook, 'rhythm-3': Rhythm3LessonBook,""")
R("""'rhythm-23': r2LbPages,""", """'rhythm-2': (s) => r2LbPages(s, 2), 'rhythm-3': (s) => r2LbPages(s, 3),""")
R("""  'rhythm-23': { secs: ['C', 'D'], back: { C: ['4 and 5', '5 and 6'], D: ['3 and 5', '4 and 6'] }, Paper: () => <R2PaperCheck/> },""",
  """  'rhythm-2': { secs: ['B'], back: { B: ['1 and 2', '2 and 3'] }, Paper: () => <R2PaperCheck/> },   // Build DH
  'rhythm-3': { secs: ['C', 'D'], back: { C: ['2 and 3', '3 and 4'], D: ['1 and 3', '2 and 4'] }, Paper: () => <R2PaperCheck/> },""")
R("""const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23', 'harmony-2']], '4': [['listen-3', 'harmony-3'], ['rhythm-23']],""",
  """const CKP_PAGES = { '3': [['listen-23', 'melody'], ['scales-23', 'harmony-2', 'rhythm-2']], '4': [['listen-3', 'harmony-3'], ['rhythm-3']],""")
R("""'keys-4': ['key-signatures', 'harmony-23']""", """'keys-4': ['key-signatures', 'harmony-3']""")
R("""'harmony-4': ['harmony-23', 'keys-4']""", """'harmony-4': ['harmony-3', 'keys-4']""")
R("""'rhythm-4': ['rhythm-23']""", """'rhythm-4': ['rhythm-3']""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
