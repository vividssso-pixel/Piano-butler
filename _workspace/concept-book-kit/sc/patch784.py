#!/usr/bin/env python3
"""Build DI (on t783 -> t784): the split, part 3 (her 14:39, 1a). Melody & Phrasing keeps its id and the Grade 2 floor with
steps 1 to 6 (the line, phrasing, question and answer, the motif, repetition and sequence, words and rhythm). Three rooms
leave it, each one step, on the floor whose exam asks for it: Writing a Melody (melody-3, Grade 3: a four-bar melody on a
rhythm), A Melody for a Couplet (melody-4, Grade 4) and A Melody for a Stanza (melody-5, Grade 5). The split layer's
page map now takes the list of base pages kept (steps, extras such as 'my piece', the check-up), and a sub-room with no
check-up parts drops the check-up page.
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

# ── the layer: a page map from the list of base pages kept; extras; no check-up when no parts; a kicker's '· Grade 4' tail goes ──
R("""const splitMap = (steps, last) => { const m = { 1: 1 }; steps.forEach((st, i) => { m[st + 1] = i + 2; }); m[last] = steps.length + 2; return m; };""",
  """const splitMap = (keep) => { const m = { 1: 1 }; keep.forEach((b, i) => { m[b] = i + 2; }); return m; };   // keep: the base Workbook pages kept, in order (page 1 is the opener)""")
R("""  return keep.map((pg, i) => React.cloneElement(pg, { key: String(i + 1), no: i + 1, kicker: i > 0 && i < keep.length - 1 && pg.props.kicker ? String(pg.props.kicker).replace(/\\d+/, String(i)) : pg.props.kicker }));""",
  """  return keep.map((pg, i) => React.cloneElement(pg, { key: String(i + 1), no: i + 1, kicker: i > 0 && i < keep.length - 1 && pg.props.kicker ? String(pg.props.kicker).replace(/\\s*·.*$/, '').replace(/\\d+/, String(i)) : pg.props.kicker }));""")
R("""function splitWb(pages, steps, secs, startNo = 1) {   // a Workbook: the pages facing the steps, then the check-up with its parts
  const last = pages.length, keep = steps.map(st => pages[st - 1]).concat([pages[last - 1]]);
  return keep.map((pg, i) => <SplitCtx.Provider key={i} value={{ steps, secs, pages: splitMap(steps, last + 1), step: i < steps.length ? i + 1 : null }}>{React.cloneElement(pg, { no: startNo + 1 + i, children: i === steps.length ? <PaperParts secs={secs}>{pg.props.children}</PaperParts> : pg.props.children })}</SplitCtx.Provider>);
}""", """function splitWb(pages, steps, secs, startNo = 1, extra = []) {   // a Workbook: the pages facing the steps, any extra pages (by base page number), then the check-up with its parts (none: no check-up page)
  const last = pages.length, keepNo = steps.map(st => st + 1).concat(extra).concat(secs.length ? [last + 1] : []);
  const map = splitMap(keepNo);
  return keepNo.map((b, i) => { const pg = pages[b - 2], chk = b === last + 1;
    return <SplitCtx.Provider key={i} value={{ steps, secs, pages: map, step: i < steps.length ? i + 1 : null }}>{React.cloneElement(pg, { no: startNo + 1 + i, children: chk ? <PaperParts secs={secs}>{pg.props.children}</PaperParts> : pg.props.children })}</SplitCtx.Provider>; });
}""")
R("""value={{ steps: STEPS, secs, pages: splitMap(STEPS, 7) }}><WbPage no={pages.length + 1} chId={ch} teacher>""",
  """value={{ steps: STEPS, secs, pages: splitMap(STEPS.map(st => st + 1).concat([7])) }}><WbPage no={pages.length + 1} chId={ch} teacher>""", 2)
R("""const SPLIT_OLD = { 'harmony-23': 'harmony-3', 'rhythm-23': 'rhythm-3' };""", """const SPLIT_OLD = { 'harmony-23': 'harmony-3', 'rhythm-23': 'rhythm-3' };   // (Melody & Phrasing keeps its id: the Grade 2 steps)""")

# ── the rooms ──
R("""const MELODY_DRILL = { id: 'melody', label: 'Melody & Phrasing' };""", """const MELODY_DRILL = { id: 'melody', label: 'Melody & Phrasing' };   // Build DI: the Grade 2 steps; the base of the three rooms below
const MELODY_3_DRILL = { id: 'melody-3', label: 'Writing a Melody' };   // Build DI: Grade 3
const MELODY_4_DRILL = { id: 'melody-4', label: 'A Melody for a Couplet' };   // Build DI: Grade 4
const MELODY_5_DRILL = { id: 'melody-5', label: 'A Melody for a Stanza' };   // Build DI: Grade 5""")
R("""  { id: 'melody', label: 'Melody & Phrasing', concept: MELODY_DRILL, track: 'reading' },""",
  """  { id: 'melody', label: 'Melody & Phrasing', concept: MELODY_DRILL, track: 'reading' },
  { id: 'melody-3', label: 'Writing a Melody', concept: MELODY_3_DRILL, track: 'reading' },   // Build DI
  { id: 'melody-4', label: 'A Melody for a Couplet', concept: MELODY_4_DRILL, track: 'reading' },   // Build DI
  { id: 'melody-5', label: 'A Melody for a Stanza', concept: MELODY_5_DRILL, track: 'reading' },   // Build DI""")
R("""  'melody': '선율과 프레이징',""", """  'melody': '선율과 프레이징', 'melody-3': '선율 쓰기', 'melody-4': '두 줄 시에 선율 붙이기', 'melody-5': '네 줄 시에 선율 붙이기',""")
R("""  'melody': ['Melody', '선율'],""", """  'melody': ['Melody', '선율'], 'melody-3': ['Writing', '선율 쓰기'], 'melody-4': ['Couplet', '두 줄 시'], 'melody-5': ['Stanza', '네 줄 시'],""")
R("""'melody': 'Prelim–G3',""", """'melody': 'G2', 'melody-3': 'G3', 'melody-4': 'G4', 'melody-5': 'G5',""")
R("""'signs': 'c-map', 'melody': 'c-map', 'form': 'c-map',""", """'signs': 'c-map', 'melody': 'c-map', 'melody-3': 'c-map', 'melody-4': 'c-map', 'melody-5': 'c-map', 'form': 'c-map',""")
R("""'c-map': ['signs', 'melody', 'form']""", """'c-map': ['signs', 'melody', 'melody-3', 'melody-4', 'melody-5', 'form']""")
R("""  { ids: ['listen-23', 'melody', 'scales-23', 'harmony-2', 'rhythm-2'], en: ['Grade 2',""", """  { ids: ['listen-23', 'melody', 'scales-23', 'harmony-2', 'rhythm-2'], en: ['Grade 2',""")
R("""  { ids: ['listen-3', 'harmony-3', 'rhythm-3'], en: ['Grade 3',""", """  { ids: ['listen-3', 'melody-3', 'harmony-3', 'rhythm-3'], en: ['Grade 3',""")
R("""  { ids: ['listen-4', 'scales-4', 'keys-4', 'harmony-4', 'rhythm-4'], en: """, """  { ids: ['listen-4', 'scales-4', 'keys-4', 'harmony-4', 'rhythm-4', 'melody-4'], en: """)
R("""  { ids: ['listen-5', 'scales-5', 'keys-5', 'harmony-5'], en: ['Grade 5',""", """  { ids: ['listen-5', 'scales-5', 'keys-5', 'harmony-5', 'melody-5'], en: ['Grade 5',""")
R("""melody: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],""", """melody: [1, 2, 3, 4, 5, 6, 7, 8, 10], 'melody-3': [11, 12], 'melody-4': [11], 'melody-5': [12],""")
R("""  melody: 2, 'harmony-2': 2,""", """  melody: 2, 'melody-3': 3, 'melody-4': 4, 'melody-5': 5, 'harmony-2': 2,""")
R("""melody: ['reading-steps', 'form'],""", """melody: ['reading-steps', 'form'], 'melody-3': ['melody'], 'melody-4': ['melody-3'], 'melody-5': ['melody-4'],""")
R("""  'melody': 'melody tune line contour""", """  'melody-3': 'writing a melody grade 3 four bars question answer rhythm given tonic phrasing',
  'melody-4': 'melody for a couplet grade 4 words set the rhythm line 1 asks line 2 answers tonic minor key',
  'melody-5': 'melody for a four-line stanza grade 5 verse phrase marks rest away come home',
  'melody': 'melody tune line contour""")
R("""  { id: 'mlx-write', ch: 'melody',""", """  { id: 'mlx-write', ch: 'melody-3',""")
R("""  { id: 'mlx-couplet', ch: 'melody',""", """  { id: 'mlx-couplet', ch: 'melody-4',""")
R("""TOOLS.push({ id: 'mlx-stanza', ch: 'melody',""", """TOOLS.push({ id: 'mlx-stanza', ch: 'melody-5',""")
R("""  { id: 'mlx-modulate', ch: 'melody',""", """  { id: 'mlx-modulate', ch: 'melody-5',""")
R("""  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-couplet', 'mlx-stanza', 'mlx-modulate', 'mlx-build',""",
  """  'melody-3': ['mlx-write'], 'melody-4': ['mlx-couplet'], 'melody-5': ['mlx-stanza', 'mlx-modulate'],   // Build DI
  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-build',""")

within("function mlxLbPages(scr = false) {", "function MelodyLessonBook()", [
 ("function mlxLbPages(scr = false) {\n  const ch = 'melody';", "function mlxLbPages(scr = false, g = 2) {   // Build DI: g = 2 (steps 1 to 6), 3 (step 7), 4 (step 8), 5 (step 9); null: every page (the Home)\n  const ch = g === 3 ? 'melody-3' : g === 4 ? 'melody-4' : g === 5 ? 'melody-5' : 'melody';\n  const STEPS = g === 2 ? [1, 2, 3, 4, 5, 6] : g === 3 ? [7] : g === 4 ? [8] : g === 5 ? [9] : [1, 2, 3, 4, 5, 6, 7, 8, 9];\n  const ROW_STEP = [1, 1, 2, 3, 5, 6, 7, 8, 9], TITLE = g === 3 ? t('Writing a Melody', '선율 쓰기') : g === 4 ? t('A Melody for a Couplet', '두 줄 시에 선율 붙이기') : g === 5 ? t('A Melody for a Stanza', '네 줄 시에 선율 붙이기') : t('Melody & Phrasing', '선율과 프레이징');"),
 ("  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(mlxNbKo(x))) : sscNbEn(x)]);\n",
  "  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(mlxNbKo(x))) : sscNbEn(x)]).filter((_, i) => STEPS.includes(ROW_STEP[i]));\n  const tocAll = [t('The line of a tune', '선율선'), t('Phrasing', '프레이징'), t('Question and answer', '질문과 대답'), t('The motif', '동기'), t('Repetition and sequence', '반복과 동형 진행'), t('Words and rhythm', '가사와 리듬'), t('Writing a melody', '선율 쓰기'), t('A melody for a couplet', '두 줄 시에 선율 붙이기'), t('A melody for a four-line stanza', '네 줄 시에 선율 붙이기')];\n  const nw = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][checksRows.length], nk = ['', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉'][checksRows.length], checksT = t('My ' + nw + ' check' + (checksRows.length > 1 ? 's' : ''), '나의 ' + nk + ' 가지 확인');\n  const toc = STEPS.map((st, i) => [tocAll[st - 1], i + 2]).concat([[checksT, STEPS.length + 2]]);\n"),
 ("<div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>", "<div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{TITLE}</div>"),
 ("{[[t('The line of a tune', '선율선'), 2], [t('Phrasing', '프레이징'), 3], [t('Question and answer', '질문과 대답'), 4], [t('The motif', '동기'), 5], [t('Repetition and sequence', '반복과 동형 진행'), 6], [t('Words and rhythm', '가사와 리듬'), 7], [t('Writing a melody', '선율 쓰기'), 8], [t('A couplet, a stanza (Grades 4, 5)', '두 줄 시, 네 줄 시(4·5급)'), '9, 10'], [t('My nine checks', '나의 아홉 가지 확인'), 11]].map(", "{toc.map("),
 ("{checksRows.slice(0, 7).map(([, x], i) =>", "{checksRows.map(([, x], i) =>"),
 ("<LbPage key=\"11\" no={11} chId={ch} kicker={t('Check-up', '점검')} title={t('My nine checks', '나의 아홉 가지 확인')}>\n      <LbSay>{t('Show each one at the piano, on its page (1 to 4, and 6 to 10). The check-up on paper is in the Workbook.', '1~4쪽과 6~10쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>",
  "<LbPage key=\"11\" no={11} chId={ch} kicker={t('Check-up', '점검')} title={checksT}>\n      <LbSay>{g === 2 ? t('Show each one at the piano, on its page. The check-up on paper is in the Workbook.', '하나씩 그 쪽을 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.') : t('Show it at the piano, then in the Workbook.', '피아노 앞에서 보여 주고, 워크북에 써요.')}</LbSay>"),
 ("live={<FiveChecks376 storeKey=\"pb_five_mlx_v1\" rows=", "live={<FiveChecks376 storeKey={'pb_five_mlx_v1' + (g === 2 ? '' : g)} rows="),
 ("  return [\n    <LbPage key=\"1\" no={1} chId={ch}>", "  const pages = [\n    <LbPage key=\"1\" no={1} chId={ch}>"),
 ("    </LbPage>,\n  ];\n}\n", "    </LbPage>,\n  ];\n  return g ? splitLb(pages, STEPS) : pages;\n}\n"),
])
# the opener's words and guess per room
within("function mlxLbPages(scr = false, g = 2) {", "function MelodyLessonBook()", [
 ("<LbSay size={17.5}>{LANG === 'ko' ? <>음이 리듬과 함께 하나씩 이어져 만드는 음악이 <b>선율</b>이에요. 이 선율은 한 동기로 만든 질문과 대답이에요.</> : <><b>Melody</b> is notes one after another, with their rhythm, that make a tune. This tune is a question and an answer, built from one motif.</>}</LbSay>",
  "<LbSay size={17.5}>{g === 3 ? t('Now you write the tune: four bars on a given rhythm, a question and an answer that comes home.', '이제 선율을 직접 써요: 주어진 리듬에 네 마디, 묻고 집으로 돌아오는 대답.') : g === 4 ? t('Words first: the couplet sets the rhythm, line 1 asks and line 2 answers.', '가사가 먼저: 두 줄 시가 리듬을 정하고, 첫 줄은 묻고 둘째 줄은 대답해요.') : g === 5 ? t('Four lines, one way home: each line rests, and the last one comes home.', '네 줄, 집으로 가는 한 길: 줄마다 쉬고, 마지막 줄이 집으로 와요.') : LANG === 'ko' ? <>음이 리듬과 함께 하나씩 이어져 만드는 음악이 <b>선율</b>이에요. 이 선율은 한 동기로 만든 질문과 대답이에요.</> : <><b>Melody</b> is notes one after another, with their rhythm, that make a tune. This tune is a question and an answer, built from one motif.</>}</LbSay>"),
 ("<LbGuess q={X('A tune in C major stops on G. Is that a question or an answer?', 'C장조 선율이 G에서 멈춰요. 질문일까요, 대답일까요?')} a={X('A question: it has not come home to C.', '질문이에요. 아직 집인 C로 돌아오지 않았어요.')} page={4}/>",
  "{g === 2 ? <LbGuess q={X('A tune in C major stops on G. Is that a question or an answer?', 'C장조 선율이 G에서 멈춰요. 질문일까요, 대답일까요?')} a={X('A question: it has not come home to C.', '질문이에요. 아직 집인 C로 돌아오지 않았어요.')} page={4}/> : g === 3 ? <LbGuess q={X('Your four-bar tune: which note must the last bar end on?', '네 마디 선율: 마지막 마디는 어느 음에서 끝나야 할까요?')} a={X('The tonic: home.', '으뜸음, 집이에요.')} page={2}/> : g === 4 ? <LbGuess q={X('A couplet has two lines. Which line ends on the tonic?', '두 줄 시는 두 줄이에요. 어느 줄이 으뜸음에서 끝날까요?')} a={X('Line 2: it answers.', '둘째 줄, 대답하는 줄이에요.')} page={2}/> : <LbGuess q={X('Four lines: how many of them rest away from home?', '네 줄: 그중 몇 줄이 집 밖에서 쉴까요?')} a={X('Three. Line 4 comes home.', '세 줄. 4줄이 집으로 와요.')} page={2}/>}"),
])
R("""function MelodyLessonBook() { return <>{mlxLbPages(false)}</>; }""", """function MelodyLessonBook() { return <>{mlxLbPages(false, 2)}</>; }
function Melody3LessonBook() { return <>{mlxLbPages(false, 3)}</>; }   // Build DI
function Melody4LessonBook() { return <>{mlxLbPages(false, 4)}</>; }
function Melody5LessonBook() { return <>{mlxLbPages(false, 5)}</>; }""")
R("""function MlxLearn({ onStart }) {
  const pages = mlxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="melody" title={bkChapterName('melody')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="melody">""",
  """function MlxLearn({ onStart, g = 2 }) {   // Build DI
  const pages = mlxLbPages(true, g), id = g === 2 ? 'melody' : 'melody-' + g;
  const opener = pages[0];
  return (
    <Lesson id={id} title={bkChapterName(id)} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value={id}>""")
R("""Object.assign(MELODY_DRILL, { levels: MLX_LEVELS, generate: genMlxQuestion,""", """splitDrill(MELODY_3_DRILL, MELODY_DRILL, [11, 12], (p) => <MlxLearn g={3} {...p}/>);   // Build DI
splitDrill(MELODY_4_DRILL, MELODY_DRILL, [11], (p) => <MlxLearn g={4} {...p}/>);
splitDrill(MELODY_5_DRILL, MELODY_DRILL, [12], (p) => <MlxLearn g={5} {...p}/>);
Object.assign(MELODY_DRILL, { allLevels: MLX_LEVELS, levels: MLX_LEVELS.filter(l => l.n <= 10), generate: genMlxQuestion,""")
R("""function MlxWorkbook({ startNo = 1 }) {
  const W = MLX_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="melody">{content}</WbPage>);""",
  """function MlxWorkbook({ startNo = 1, g = 2 }) {   // Build DI
  const W = MLX_WB, pages = [], ch = g === 2 ? 'melody' : 'melody-' + g;
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId={ch}>{content}</WbPage>);""")
R("""  P(<MlxMyPiece/>);
  P(<MlxPaperCheck/>);
  return <>{pages}</>;
}""", """  P(<MlxMyPiece/>);
  P(<MlxPaperCheck/>);
  return <>{splitWb(pages, g === 2 ? [1, 2, 3, 4, 5, 6] : [g + 4], g === 2 ? ['A', 'B', 'C', 'D', 'E'] : [], startNo, g === 2 ? [11] : [])}</>;   // page 11: my piece
}""")
R("""function MlxTeacher() {
  const W = MLX_WB, C = MLX_CHK, pages = [], { nB, nC, nD, nE, total } = mlxChkNo();
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="melody" teacher>{content}</WbPage>);""",
  """function MlxTeacher({ g = 2 }) {   // Build DI
  const W = MLX_WB, C = MLX_CHK, pages = [], { nB, nC, nD, nE, total } = mlxChkNo(), ch = g === 2 ? 'melody' : 'melody-' + g;
  const STEPS = g === 2 ? [1, 2, 3, 4, 5, 6] : [g + 4], secs = g === 2 ? ['A', 'B', 'C', 'D', 'E'] : [], keep = STEPS.map(st => st + 1).concat(g === 2 ? [11, 12] : []);
  const one = [], P = (content) => g === 2 ? pages.push(<SplitCtx.Provider key={pages.length} value={{ steps: STEPS, secs, pages: splitMap(keep) }}><WbPage no={pages.length + 1} chId={ch} teacher>{content}</WbPage></SplitCtx.Provider>) : one.push(content);   // a one-step room: one page
  const finish = () => { if (one.length) pages.push(<SplitCtx.Provider key="one" value={{ steps: STEPS, secs, pages: splitMap(keep) }}><WbPage no={1} chId={ch} teacher>{one.map((c, i) => <React.Fragment key={i}>{c}</React.Fragment>)}</WbPage></SplitCtx.Provider>); };""")
R("""WORKBOOKS['melody'] = MlxWorkbook;
TEACHER_COPIES['melody'] = MlxTeacher;""", """WORKBOOKS['melody'] = MlxWorkbook;
TEACHER_COPIES['melody'] = MlxTeacher;
[3, 4, 5].forEach(g => { WORKBOOKS['melody-' + g] = () => <MlxWorkbook g={g}/>; TEACHER_COPIES['melody-' + g] = () => <MlxTeacher g={g}/>; });   // Build DI""")
R(""" melody: MelodyLessonBook,""", """ melody: MelodyLessonBook, 'melody-3': Melody3LessonBook, 'melody-4': Melody4LessonBook, 'melody-5': Melody5LessonBook,""")
R(""" melody: mlxLbPages,""", """ melody: (s) => mlxLbPages(s, 2), 'melody-3': (s) => mlxLbPages(s, 3), 'melody-4': (s) => mlxLbPages(s, 4), 'melody-5': (s) => mlxLbPages(s, 5),""")
R("""Teacher copy · {bkChapterName('melody')}</div>""", """Teacher copy · {bkChapterName(ch)}</div>""")
within("function MlxTeacher({ g = 2 }) {", "WORKBOOKS['melody'] = MlxWorkbook;", [("  return <>{pages}</>;\n}", "  finish();\n  return <>{pages}</>;\n}")])
# the base room's side notes (the drill list, the nine checks) only in the Grade 2 copy
import re as _re
a = s.index("function MlxTeacher({ g = 2 }) {"); b = s.index("WORKBOOKS['melody'] = MlxWorkbook;", a); part = s[a:b]
part2 = _re.sub(r"\n    (<div style=\{\{border:'0\.8px solid ' \+ BK\.hair,padding:'[67]px 12px'[^\n]*</div>)\n", lambda m: "\n    {g === 2 && " + m.group(1) + "}\n", part)
assert part2.count("{g === 2 && <div") == 2, part2.count("{g === 2 && <div")
s = s[:a] + part2 + s[b:]
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
