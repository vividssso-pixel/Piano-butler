import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
def within(start, end, pairs):
    """edit only inside s[start:end] (start inclusive, end exclusive); every old string must occur exactly once there"""
    global s
    a = s.index(start); b = s.index(end, a)
    part = s[a:b]
    for old, new in pairs:
        assert part.count(old) == 1, (part.count(old), old[:90])
        part = part.replace(old, new)
    s = s[:a] + part + s[b:]
def cut(start, end):
    """remove s[start:end) where start and end are unique markers (end kept)"""
    global s
    assert s.count(start) == 1, (s.count(start), start[:80])
    a = s.index(start); b = s.index(end, a)
    s = s[:a] + s[b:]

# Build CC (her 09:38 and 09:50): the house by grade. Prelim and Grade 1 are a floor each (floor 2 Prelim, floor 3 Grade 1),
# each grade has its own Ear Training room (the aural tests of that grade, Manual 2026 section 21, Table B), and the Beginner
# floor gets an Ear Prep room: five quick listening games before the graded tests. Her 09:56: everything must be fun, as the
# How to Blitz books are, so each Ear Prep step is a quick round of five with a streak and stars (QuickRound).
#   Ear Prep (new, Beginner): turtle, Clara or bird (low, middle, high); same rhythm or not; same tune or not; which way did it
#     go; find your note (moved from Listen and Sing, which the Prelim tests don't ask).
#   Ear Training, Prelim (was Listen and Sing): keep the beat, echo the rhythm, higher or lower, sing it back.
#   Ear Training, Grade 1 (was Listen, Clap, Write): the home note, clap it back, sing it with its rhythm. Two or three? moves to
#     Grade 3, where the test asks for it; Write the rhythm (dictation) leaves the ear rooms: no practical test asks for it.
#   Ear Training, Grade 2 (was Grades 2-3): two notes at once (a 3rd or a 5th), clap it back, sing a longer tune.
#   Ear Training, Grade 3 (new): any two notes, from the keynote, two or three?, clap it back and name it, sing a longer tune.
# Chapter numbers move (her 09:50: fine, before the Lesson Books and Workbooks are redone).

# ── 1. the drills ──
rep("""const LISTEN_DRILL = { id: 'listen-sing', label: 'Listen and Sing', noPrint: true };""",
    """const LISTEN_DRILL = { id: 'listen-sing', label: 'Ear Training, Prelim', noPrint: true };   // Build CC: was Listen and Sing
const EAR_PREP_DRILL = { id: 'ear-prep', label: 'Ear Prep', noPrint: true };   // Build CC: the Beginner floor's ears""")
rep("""const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Listen, Clap, Write', noPrint: true };""",
    """const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Ear Training, Grade 1', noPrint: true };   // Build CC: was Listen, Clap, Write""")
rep("""const LISTEN_23_DRILL = { id: 'listen-23', label: 'Ear Training, Grades 2–3', noPrint: true };""",
    """const LISTEN_23_DRILL = { id: 'listen-23', label: 'Ear Training, Grade 2', noPrint: true };   // Build CC: Grade 2 only
const LISTEN_3_DRILL = { id: 'listen-3', label: 'Ear Training, Grade 3', noPrint: true };   // Build CC""")
rep("""  { id: 'listen-sing', label: 'Listen and Sing', concept: LISTEN_DRILL, track: 'start' },   // Build X""",
    """  { id: 'ear-prep', label: 'Ear Prep', concept: EAR_PREP_DRILL, track: 'start' },   // Build CC
  { id: 'listen-sing', label: 'Ear Training, Prelim', concept: LISTEN_DRILL, track: 'start' },   // Build X""")
rep("""  { id: 'listen-write', label: 'Listen, Clap, Write', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE""",
    """  { id: 'listen-write', label: 'Ear Training, Grade 1', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE""")
rep("""  { id: 'listen-23', label: 'Ear Training, Grades 2–3', concept: LISTEN_23_DRILL, track: 'start' },   // Build AJ""",
    """  { id: 'listen-23', label: 'Ear Training, Grade 2', concept: LISTEN_23_DRILL, track: 'start' },   // Build AJ
  { id: 'listen-3', label: 'Ear Training, Grade 3', concept: LISTEN_3_DRILL, track: 'start' },   // Build CC""")
rep("""'listen-sing': '듣고 노래하기', 'listen-write': '듣고, 치고, 적기', 'listen-23': '청음, Grade 2–3',""",
    """'ear-prep': '청음 준비', 'listen-sing': '청음, Prelim', 'listen-write': '청음, Grade 1', 'listen-23': '청음, Grade 2', 'listen-3': '청음, Grade 3',""")
rep("""'listen-sing': ['pulse', 'hand-positions'], 'listen-write': ['listen-sing', 'time-signatures'], 'listen-23': ['listen-write'], 'listen-4': ['listen-23', 'intervals'],""",
    """'ear-prep': ['pulse', 'hand-positions'], 'listen-sing': ['ear-prep'], 'listen-write': ['listen-sing', 'time-signatures'], 'listen-23': ['listen-write'], 'listen-3': ['listen-23'], 'listen-4': ['listen-3', 'intervals'],""")
rep("""  'listen-sing': 'listen sing aural ear training echo rhythm clap beat up down high low find note sing back pitch',""",
    """  'ear-prep': 'ear prep warm up aural ear training listening games low middle high turtle bird clara same different rhythm tune which way shape find note quick round',
  'listen-sing': 'ear training aural ear prelim preliminary listen sing echo rhythm clap beat higher lower sing back phrase pitch',""")
rep("""  'listen-23': 'ear training aural ear grade 2 grade 3 two notes together higher lower sing major third perfect fifth keynote second third fourth fifth name interval clap back duple triple sing phrase',
  'listen-write': 'aural ear grade 1 tonic home note unfinished phrase duple triple two three beats clap back sing phrase rhythm dictation write rhythm contour shape',""",
    """  'listen-23': 'ear training aural ear grade 2 two notes together higher lower sing major third perfect fifth clap back dotted sing phrase',
  'listen-3': 'ear training aural ear grade 3 any two notes together higher lower keynote second third fourth fifth name interval duple triple two three oom-pah clap back sing phrase',
  'listen-write': 'ear training aural ear grade 1 tonic home note unfinished phrase clap back sing phrase rhythm contour shape',""")
rep("""'listen-sing': ['Listen & sing', '듣고 노래'], 'listen-write': ['Listen & write', '듣고 적기'], 'listen-23': ['Aural 2–3', '청음 2–3'],""",
    """'ear-prep': ['Ear prep', '청음 준비'], 'listen-sing': ['Aural Prelim', '청음 Prelim'], 'listen-write': ['Aural 1', '청음 1'], 'listen-23': ['Aural 2', '청음 2'], 'listen-3': ['Aural 3', '청음 3'],""")
rep("""const thArea = (id) => { if (id === 'listen-sing' || id === 'listen-write' || id === 'listen-23' ||""",
    """const thArea = (id) => { if (id === 'ear-prep' || id === 'listen-sing' || id === 'listen-write' || id === 'listen-23' || id === 'listen-3' ||""")
rep("""const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6, composers: 6, styles: 6 };""",
    """const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6, composers: 6, styles: 6, 'ear-prep': 6, 'listen-sing': 5, 'listen-write': 4, 'listen-23': 4, 'listen-3': 6 };   // Build CC: the ear rooms by grade""")

# ── 2. the house: floors by grade ──
rep("""  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'hand-positions', 'listen-sing', 'note-values', 'dynamics', 'staff', 'reading-steps', 'whole-staff', 'time-signatures', 'tones'], en: ['Beginner', 'Sitting and hands, the keys and their letters, beat and note values, listening and singing, loud and soft, the staff and the first tunes, half and whole steps.'], ko: ['Beginner', '자세와 손, 건반과 글자, 박과 음표 길이, 듣고 노래하기, 셈여림, 오선과 첫 선율, 반음과 온음.'] },""",
    """  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'hand-positions', 'ear-prep', 'note-values', 'dynamics', 'staff', 'reading-steps', 'whole-staff', 'time-signatures', 'tones'], en: ['Beginner', 'Sitting and hands, the keys and their letters, beat and note values, games for your ears, loud and soft, the staff and the first tunes, half and whole steps.'], ko: ['Beginner', '자세와 손, 건반과 글자, 박과 음표 길이, 귀 놀이, 셈여림, 오선과 첫 선율, 반음과 온음.'] },   // Build CC: Ear Prep""")
rep("""  { ids: ['tempo', 'rhythm', 'six-eight', 'ledger-lines', 'scales', 'scale-play', 'accidentals'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, 6/8, ledger lines, scales and how to play them, and accidentals.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 6/8박자, 덧줄, 스케일과 스케일 치기, 그리고 임시표.'] },""",
    """  { ids: ['listen-sing', 'tempo', 'rhythm', 'ledger-lines', 'scales', 'scale-play', 'minor-scales', 'signs'], en: ['Prelim', 'Your ears for Prelim, speed, quavers and dots, ledger lines, scales and how to play them, minor scales, and signs.'], ko: ['Prelim', 'Prelim 청음, 빠르기, 8분음표와 점, 덧줄, 스케일과 스케일 치기, 단음계, 그리고 기호.'] },   // Build CC: a floor for Prelim""")
rep("""  { ids: ['key-signatures', 'minor-scales', 'signs', 'intervals', 'chords', 'terms', 'form', 'listen-write'], en: ['Prelim – Grade 1', 'Key signatures and minor scales, signs, intervals and chords, the words for how to play, how a piece is built, and listening a step further.'], ko: ['Prelim – Grade 1', '조표와 단음계, 기호, 음정과 화음, 음악 용어, 곡의 짜임, 그리고 한 걸음 더 듣기.'] },""",
    """  { ids: ['listen-write', 'accidentals', 'key-signatures', 'terms', 'six-eight', 'intervals', 'chords', 'form'], en: ['Grade 1', 'Your ears for Grade 1, accidentals and key signatures, the words for how to play, 6/8, intervals and chords, and how a piece is built.'], ko: ['Grade 1', '1급 청음, 임시표와 조표, 음악 용어, 6/8박자, 음정과 화음, 그리고 곡의 짜임.'] },   // Build CC: a floor for Grade 1""")
rep("""  { ids: ['melody', 'listen-23', 'scales-23', 'harmony-23', 'rhythm-23'], en: ['Grades 2–3', 'How a tune is shaped; your ears, scales, intervals and chords, and rhythm a step further.'], ko: ['Grade 2–3', '선율의 모양, 그리고 귀, 스케일, 음정과 화음, 리듬을 한 걸음 더.'] },""",
    """  { ids: ['listen-23', 'listen-3', 'melody', 'scales-23', 'harmony-23', 'rhythm-23'], en: ['Grades 2–3', 'Your ears for Grade 2 and for Grade 3; how a tune is shaped; scales, intervals and chords, and rhythm a step further.'], ko: ['Grade 2–3', '2급 청음과 3급 청음, 선율의 모양, 그리고 스케일, 음정과 화음, 리듬을 한 걸음 더.'] },   // Build CC: an ear room per grade""")
rep("""  { wp: 'trellis', fl: 'tiles', lamp: 'pendant' }       // 9
];""", """  { wp: 'trellis', fl: 'tiles', lamp: 'pendant' },      // 9
  { wp: 'damask', fl: 'planks', lamp: 'globe' }         // 10 (Build CC: Prelim and Grade 1 are a floor each)
];""")
# house icons: Ear Prep (low, middle, high), Grade 1 (the tune falls home), Grade 3 (the keynote and a note above it)
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"ear-prep": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><circle cx=\\"25\\" cy=\\"36\\" r=\\"3.6\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"33\\" cy=\\"25\\" r=\\"3.6\\" fill=\\"#e4572e\\" stroke=\\"none\\"/><circle cx=\\"41\\" cy=\\"14\\" r=\\"3.6\\" fill=\\"#26296b\\" stroke=\\"none\\"/>", "listen-3": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><ellipse cx=\\"27\\" cy=\\"35\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 27 35)\\" fill=\\"#26296b\\"/><ellipse cx=\\"39\\" cy=\\"19\\" rx=\\"5.5\\" ry=\\"4\\" transform=\\"rotate(-20 39 19)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><path d=\\"M30 30 L36 24\\" stroke-dasharray=\\"2 3\\"/>",""")
rep('''"listen-write": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><path d=\\"M24 36 L40 14 L45 18 L29 40 Z\\" stroke=\\"#e4572e\\"/><path d=\\"M24 36 L22 43 L29 40\\" stroke=\\"#e4572e\\"/>"''',
    '''"listen-write": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><circle cx=\\"24\\" cy=\\"13\\" r=\\"3\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"30\\" cy=\\"20\\" r=\\"3\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"36\\" cy=\\"27\\" r=\\"3\\" fill=\\"#26296b\\" stroke=\\"none\\"/><circle cx=\\"42\\" cy=\\"35\\" r=\\"4.2\\" fill=\\"#e4572e\\" stroke=\\"none\\"/><path d=\\"M35 41 H48\\"/>"''')

# ── 3. Ear Training, Prelim (was Listen and Sing): Find your note moves to Ear Prep ──
within("function lsLbPages(scr = false) {", "function ListenSingLessonBook()", [
    ("""[lsPicFind(), t('I sing a note, then find it on the keys', '음 하나를 부르고, 건반에서 찾아요')], """, ""),
    ("""[t('Find your note', '내 음 찾기'), 5], [t('Sing it back', '따라 부르기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]]""",
     """[t('Sing it back', '따라 부르기'), 5], [t('My four checks', '나의 네 가지 확인'), 6]]"""),
    ("""{t('Ears first. Every step here is listening, then singing or tapping, then the keys: the app plays and scores the taps; whether a child sang in tune is your ear. Sing on "la" at a comfortable pitch: if a voice sits higher than C position, let it sing there. No staff yet: the staff comes in chapter ' + bkChapterNo('staff') + '.', '귀가 먼저예요. 모든 단계가 듣기, 그다음 부르거나 치기, 그다음 건반이에요. 앱은 소리를 들려주고 탭을 채점해요. 음정에 맞게 불렀는지는 선생님의 귀가 판단해요. 편한 높이에서 "라"로 불러요. 목소리가 C 자리보다 높은 곳에 있으면 거기서 불러도 돼요. 오선은 아직이에요: ' + bkChapterNo('staff') + '장에서 배워요.')}""",
     """{t('The Preliminary aural tests, one step each (Manual of Syllabuses, section 21): the beat of chords in two or three clapped at different speeds, carrying on when the music stops; a two-bar rhythm echoed; higher or lower of two notes a third or more apart; a phrase of five or six one-beat notes sung back, the examiner waiting on each note. Every step is listening, then singing or tapping, then the keys: the app plays and scores the taps; whether a child sang in tune is your ear. Sing on "la" at a comfortable pitch: if a voice sits higher than C position, let it sing there. The warm-up games are in chapter ' + bkChapterNo('ear-prep') + '.', 'Prelim 청음 시험을 한 단계씩(실라버스 21절): 두 박이나 세 박 화음의 박을 여러 빠르기로 손뼉 치고, 음악이 멈춰도 계속하기; 두 마디 리듬 메아리; 3도 이상 떨어진 두 음 중 높은 음과 낮은 음; 한 박짜리 다섯·여섯 음 선율 따라 부르기(시험관이 음마다 기다려 줘요). 모든 단계가 듣기, 그다음 부르거나 치기, 그다음 건반이에요. 앱은 소리를 들려주고 탭을 채점해요. 음정에 맞게 불렀는지는 선생님의 귀가 판단해요. 편한 높이에서 "라"로 불러요. 목소리가 C 자리보다 높은 곳에 있으면 거기서 불러도 돼요. 준비운동 놀이는 ' + bkChapterNo('ear-prep') + '장에 있어요.')}"""),
    ("""{t('Listen and Sing', '듣고 노래하기')}""", """{t('Ear Training, Prelim', '청음, Prelim')}"""),
    ("""t('sing a note and find it on the keys', '음 하나를 부르고 건반에서 찾을 수 있어요'), """, ""),
    ("""<LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Echo the rhythm', '리듬 메아리')}""", """<LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Echo the rhythm', '리듬 메아리')}"""),
    ("""'두 마디를 손뼉으로 치면, 아이가 박을 끊지 않고 바로 이어서 똑같이 쳐요(부르고, 메아리). ' + bkChapterNo('pulse') + '장의 낱말을 써요: 타는 한 박에 한 소리, 티-티는 두 소리. 타와 길게 누르는 박으로 시작하고, 쉬워지면 티-티를 더해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>""",
     """'두 마디를 손뼉으로 치면, 아이가 박을 끊지 않고 바로 이어서 똑같이 쳐요(부르고, 메아리). ' + bkChapterNo('pulse') + '장의 낱말을 써요: 타는 한 박에 한 소리, 티-티는 두 소리. 타와 길게 누르는 박으로 시작하고, 쉬워지면 티-티를 더해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>"""),
    ("""<LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Sing it back', '따라 부르기')}""", """<LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Sing it back', '따라 부르기')}"""),
    ("""'처음엔 C 자리에서 한 걸음씩 움직이는 세 음, 그다음 한 박씩 다섯·여섯 음. 선율을 한 번 쳐 주고, 다시 한 음씩 치면서 아이가 하나씩 부를 때까지 기다려 주세요. 치기 전에 언제나 먼저 따라 불러요: 귀가 앞서고 손이 따라가요. 치다가 틀리면 건반을 더듬지 말고 다시 불러 보게 해 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>""",
     """'처음엔 C 자리에서 한 걸음씩 움직이는 세 음, 그다음 한 박씩 다섯·여섯 음. 선율을 한 번 쳐 주고, 다시 한 음씩 치면서 아이가 하나씩 부를 때까지 기다려 주세요. 치기 전에 언제나 먼저 따라 불러요: 귀가 앞서고 손이 따라가요. 치다가 틀리면 건반을 더듬지 말고 다시 불러 보게 해 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>"""),
    ("""<LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}""", """<LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}"""),
    ("""storeKey="pb_ls_five\"""", """storeKey="pb_ls_four\""""),
])
# the Find your note page goes to Ear Prep (written there afresh)
cut("""    // 5. find your note
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Find your note', '내 음 찾기')}""", """    // 6. sing it back""")
within("function LsTeacher() {", "TEACHER_COPIES['listen-sing'] = LsTeacher;", [
    ("""Sing on "la" at a comfortable pitch; C position only, no staff yet.</div>""", """Sing on "la" at a comfortable pitch; C position. These are the Preliminary aural tests; the warm-up games are in chapter {bkChapterNo('ear-prep')}.</div>"""),
    ("""    <TcBlock page={5} title="Find your note" answers={<>{tcAns('PLAY', ['one note from C position (C to G); the child sings it, then finds it'])}</>}
      watch="Hunting along the keys. Ask “higher or lower?” before the next try."
      say="“Sing it, then find it: higher or lower?”"/>
""", ""),
    ("""<TcBlock page={6} title="Sing it back\"""", """<TcBlock page={5} title="Sing it back\""""),
    ("""<TcBlock page={7} title="My five checks\"""", """<TcBlock page={6} title="My four checks\""""),
])
rep("""    <Lesson id="listen-sing" title={t('Listen and sing', '듣고 노래하기')} onStart={onStart} noArt""",
    """    <Lesson id="listen-sing" title={bkChapterName('listen-sing')} onStart={onStart} noArt""")
rep("""Object.assign(LISTEN_DRILL, { levels: LS_LEVELS, generate: genLsQuestion,""",
    """// Build CC: the Prelim room asks the Prelim tests; low, middle or high, the shapes and finding a note are Ear Prep's
const lsLevelsOf = (kinds) => kinds.map((k, j) => ({ ...LS_LEVELS.find(lv => lv.kind === k), n: j + 1 }));
const LS_P_LEVELS = lsLevelsOf(['updown', 'rhythm', 'tune']), EP_LEVELS = lsLevelsOf(['hml', 'rhythm', 'tune', 'shape', 'find']);
Object.assign(LISTEN_DRILL, { levels: LS_P_LEVELS, generate: genLsQuestion,""")

# ── 4. Ear Prep (new, Beginner) ──
EP = r'''
// ─── Chapter: Ear Prep (Build CC, 2026-10-28; her 09:50: a Beginner room for the ears before the graded tests) ───
// Five listening games before Prelim's tests: turtle, Clara or bird (low, middle or high: her turtle = low, bird = high, Clara =
// middle C); the same rhythm or not; the same tune or not; which way three notes went; find your note (from the old Listen and
// Sing). Her 09:56, 'everything must be fun, like How to Blitz': each game is a quick round of five, with a streak, stars for the
// round and the best round kept on the device (QuickRound), and away from the screen a game with the body.
const QR_N = 5;
const QR_SAY = (n) => n >= QR_N ? ['A perfect round!', '완벽한 한 판!'] : n === QR_N - 1 ? ['So close. Again for five?', '거의 다 왔어요. 다섯 개 도전?'] : n === QR_N - 2 ? ['Good ears. Again for four?', '좋은 귀예요. 네 개 도전?'] : ['Warmed up! Again: listen to the end before you tap.', '몸풀기 끝! 다시: 끝까지 듣고 눌러요.'];
function QuickRound({ kind, id }) {
  const lv = { kind }, T = useRef(null), store = 'pb_qr_' + (id || kind);
  const [phase, setPhase] = useState('ready'), [q, setQ] = useState(() => genLsQuestion(lv, null)), [marks, setMarks] = useState([]), [given, setGiven] = useState(null), [run, setRun] = useState(0), [fresh, setFresh] = useState(false);
  const [best, setBest] = useState(() => { try { return +localStorage.getItem(store) || 0; } catch (e) { return 0; } });
  useEffect(() => () => clearTimeout(T.current), []);
  const score = marks.filter(Boolean).length;
  const start = () => { clearTimeout(T.current); setMarks([]); setGiven(null); setRun(0); setFresh(false); setQ(p => genLsQuestion(lv, p)); setPhase('play'); };
  const next = (m) => { clearTimeout(T.current);
    if (m.length >= QR_N) { const sc = m.filter(Boolean).length; setPhase('done'); if (sc > best) { setBest(sc); setFresh(true); try { localStorage.setItem(store, String(sc)); } catch (e) {} } return; }
    setGiven(null); setQ(p => genLsQuestion(lv, p)); };
  const answer = (a) => { if (given || phase !== 'play') return; const ok = a === q.answer, m = marks.concat([ok]); setGiven({ ans: a }); setMarks(m); setRun(r => (ok ? r + 1 : 0)); if (ok) T.current = setTimeout(() => next(m), 1300); };
  const dots = <div style={{display:'flex',gap:7,justifyContent:'center',margin:'0 0 8px'}}>{Array.from({ length: QR_N }, (_, j) => { const m = marks[j], cur = phase === 'play' && j === marks.length - (given ? 1 : 0);
    return <span key={j} style={{width:18,height:18,borderRadius:9,boxSizing:'border-box',border:'2px solid ' + (m === true ? BK.green : m === false || cur ? BK.coral : BK.line),background:m === true ? BK.green : m === false ? '#fbe3da' : '#fff'}}/>; })}</div>;
  const btn = { minHeight:44, fontSize:15, padding:'8px 18px' };
  return (
    <div className="try-box" style={actBox} data-qr={kind} data-phase={phase}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',gap:8,flexWrap:'wrap'}}>
        <div style={actTitle}>{t('Quick round', '빠른 한 판')}</div>
        <span style={{fontSize:12.5,fontWeight:800,color:BK.muted}}>{t('Best: ' + best + ' of ' + QR_N, '최고: ' + QR_N + '개 중 ' + best + '개')}</span>
      </div>
      {phase === 'ready' && <div style={{textAlign:'center',padding:'6px 0 2px'}}>
        <div style={{fontSize:15,color:BK.ink,margin:'0 0 10px',lineHeight:1.45}}>{t('Five quick questions, heard not seen. How many in a row can you get?', '눈이 아니라 귀로 푸는 다섯 문제. 몇 개 연속으로 맞힐까요?')}</div>
        <button className="primary-btn" style={btn} onClick={start}>{t('▶ Start the round', '▶ 한 판 시작')}</button></div>}
      {phase === 'play' && <>
        {dots}
        <div style={{textAlign:'center',minHeight:22,fontSize:13.5,fontWeight:900,color:BK.coral,margin:'0 0 4px'}}>{run >= 2 ? t(run + ' in a row!', run + '개 연속!') : ''}</div>
        <LsQuestion key={q.uid} q={q} given={given} locked={false} onAnswer={answer}/>
        {given && given.ans !== q.answer && <div style={{textAlign:'center',marginTop:10}}><button className="ghost-btn" style={btn} onClick={() => next(marks)}>{marks.length >= QR_N ? t('See my stars ▶', '내 별 보기 ▶') : t('Next ▶', '다음 ▶')}</button></div>}
      </>}
      {phase === 'done' && <div style={{textAlign:'center',padding:'4px 0'}}>
        <div aria-label={t(score + ' of ' + QR_N, QR_N + '개 중 ' + score + '개')} style={{fontSize:34,letterSpacing:4,lineHeight:1.1,margin:'2px 0 4px'}}>{Array.from({ length: QR_N }, (_, j) => <span key={j} style={{color:j < score ? BK.coral : 'rgba(38,41,107,0.22)'}}>★</span>)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:24,fontWeight:900,color:BK.ink}}>{t(score + ' of ' + QR_N, QR_N + '개 중 ' + score + '개')}</div>
        <div style={{fontSize:15,color:BK.ink,margin:'4px 0 2px'}}>{t(...QR_SAY(score))}</div>
        {fresh && <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.06em',margin:'2px 0'}}>{t('NEW BEST', '새 최고 기록')}</div>}
        <div style={{marginTop:10}}><button className="primary-btn" style={btn} onClick={start}>{t('▶ Play again', '▶ 한 판 더')}</button></div></div>}
    </div>
  );
}
// the pictures on paper
const epPicHml = () => ({ shapes: [...fsTurtle(13, 35, 0.5), { k: 'raw', svg: '<circle cx="40" cy="24" r="6" fill="#e4572e"/>' }, ...fsBird(67, 10, 0.72)], vb: [0, 0, 80, 44] });
const epPicRhythm = () => lsRawPic([0, 1, 2, 3].map(i => lsCircleSvg(10 + i * 18, 11, 6, i === 2 ? 'beat' : 'play')).join('') + [0, 1, 2, 3].map(i => lsCircleSvg(10 + i * 18, 33, 6, i === 1 ? 'beat' : 'play')).join('') + '<circle cx="28" cy="33" r="9" fill="none" stroke="#e4572e" stroke-width="2"/>', [0, 0, 80, 44]);
const epPicTune = () => lsRawPic('<polyline points="6,32 14,24 22,16 30,24" fill="none" stroke="#26296b" stroke-width="1.6"/>' + [[6, 32], [14, 24], [22, 16], [30, 24]].map(([x, y]) => '<circle cx="' + x + '" cy="' + y + '" r="3.4" fill="#26296b"/>').join('')
  + '<polyline points="46,32 54,24 62,30 70,24" fill="none" stroke="#26296b" stroke-width="1.6"/>' + [[46, 32], [54, 24], [62, 30], [70, 24]].map(([x, y], j) => '<circle cx="' + x + '" cy="' + y + '" r="3.4" fill="' + (j === 2 ? '#e4572e' : '#26296b') + '"/>').join(''), [0, 0, 80, 44]);
const epPicShape = () => lsRawPic('<polyline points="12,34 40,10 68,28" fill="none" stroke="#e4572e" stroke-width="2.4" stroke-linejoin="round"/><circle cx="12" cy="34" r="5" fill="#26296b"/><circle cx="40" cy="10" r="5" fill="#26296b"/><circle cx="68" cy="28" r="5" fill="#26296b"/>', [0, 0, 80, 44]);
// turtle, Clara, bird: low, middle, high (raised step by step)
const epHml = (big, scr) => { const k = scr ? 1 : 1.75;   // larger on paper
  return <div style={{display:'flex',justifyContent:'center',alignItems:'flex-end',gap:scr ? 26 : 60,width:'100%'}}>
  {[[turtleIcon((big ? 84 : 62) * k), t('low', '낮은')], [lsClara((big ? 58 : 44) * k), t('middle', '가운데')], [birdIcon((big ? 84 : 62) * k), t('high', '높은')]].map(([ic, w], j) =>
    <div key={j} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:5,marginBottom:j * (big ? 24 : 18) * k}}>{ic}<span style={{fontSize:scr ? 14 : 18,fontWeight:900,color:j === 1 ? BK.coral : BK.ink}}>{w}</span></div>)}</div>; };

function epLbPages(scr = false) {
  const ch = 'ear-prep';
  const checks5 = [[epPicHml(), t('I hear whether a note is low, in the middle or high', '음이 낮은지, 가운데인지, 높은지 들어요')], [epPicRhythm(), t('I hear whether two rhythms are the same', '두 리듬이 같은지 들어요')],
    [epPicTune(), t('I hear whether two tunes are the same', '두 선율이 같은지 들어요')], [epPicShape(), t('I hear which way three notes go', '세 음이 어느 쪽으로 가는지 들어요')], [lsPicFind(), t('I sing a note, then find it on the keys', '음 하나를 부르고, 건반에서 찾아요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Turtle, Clara or bird?', '거북이, 클라라, 새?'), 2], [t('Same rhythm, or not?', '같은 리듬일까?'), 3], [t('Same tune, or not?', '같은 선율일까?'), 4], [t('Which way did it go?', '어느 쪽으로 갔을까?'), 5], [t('Find your note', '내 음 찾기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const row = (lab, el, col) => <div style={{display:'flex',alignItems:'center',gap:8}}><span style={{width:78,fontSize:12.5,fontWeight:900,color:col || BK.muted}}>{lab}</span><div style={{flex:1,minWidth:0}}>{el}</div></div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Before the graded aural tests: five quick listening games. In the app each step is a round of five questions with a streak and stars; the best round is kept on this device. Away from the screen each one is a game with the body: crouch, stand tall and flap; thumbs up or down; draw the path in the air; swap roles and let the child try to catch you out. The Preliminary tests start in chapter ' + bkChapterNo('listen-sing') + '.', '등급 청음 시험 전에: 빠른 듣기 놀이 다섯 가지. 앱에서는 단계마다 다섯 문제 한 판, 연속 기록과 별이 있고, 가장 좋은 판은 이 기기에 남아요. 화면 밖에서는 몸으로 하는 놀이예요: 웅크리고, 서고, 퍼덕이기; 엄지 위로 아래로; 공중에 길 그리기; 역할을 바꿔서 아이가 선생님을 속여 보기. Prelim 시험은 ' + bkChapterNo('listen-sing') + '장에서 시작해요.')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Ear Prep', '청음 준비')}</div>
      </div></LbOnly>
      <LbPic h={190}>{epHml(true, scr)}</LbPic>
      <LbSay size={18}>{t('A warm-up for your ears: quick rounds of five. How many in a row?', '귀 준비운동: 다섯 문제씩 빠르게. 몇 개 연속으로 맞힐까요?')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('tell low, middle and high', '낮은 음, 가운데 음, 높은 음을 구별할 수 있어요'), t('hear whether two rhythms are the same', '두 리듬이 같은지 들을 수 있어요'), t('hear whether two tunes are the same', '두 선율이 같은지 들을 수 있어요'), t('hear which way a tune goes', '선율이 어느 쪽으로 가는지 들을 수 있어요'), t('sing a note and find it on the keys', '음 하나를 부르고 건반에서 찾을 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Turtle, Clara or bird?', '거북이, 클라라, 새?')}
      teacher={<>{t('Low, middle or high: the first listening there is. The app plays one note from three places far apart: low, two octaves below middle C; the middle, around middle C (Clara); high, two octaves above. Away from the screen, play a note and the child answers with the body: crouch like the turtle, stand tall like Clara, flap like the bird. Watch for high meaning loud: play a soft high note and a loud low one.', '낮은 음, 가운데 음, 높은 음: 가장 첫 듣기예요. 앱은 멀리 떨어진 세 곳 중 하나에서 음 하나를 쳐요: 낮은 음은 가운데 도보다 두 옥타브 아래, 가운데는 가운데 도(클라라) 근처, 높은 음은 두 옥타브 위. 화면 밖에서는 선생님이 음을 치고 아이가 몸으로 답해요: 거북이처럼 웅크리기, 클라라처럼 똑바로 서기, 새처럼 퍼덕이기. "높다"를 "크다"로 헷갈리는지 봐 주세요: 여린 높은 음과 센 낮은 음을 쳐 보세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}>{epHml(false, scr)}</LbPic>} live={<QuickRound kind="hml" id="ep-hml"/>}/>
      <LbSay>{LANG === 'ko' ? <>모든 음은 사는 곳이 있어요. <b>낮은</b> 음은 거북이와 바다에, <b>가운데</b> 음은 클라라(가운데 도)와, <b>높은</b> 음은 새와 하늘에. 다섯 개 빠르게: 몇 개 연속으로 맞힐까요?</> : <>Every note lives somewhere: <b>low</b> down with the turtle, <b>in the middle</b> with Clara (middle C), or <b>high</b> up with the bird. Five quick ones: how many in a row?</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 음 하나를 쳐요. 낮으면 거북이처럼 웅크리고, 가운데면 클라라처럼 똑바로 서고, 높으면 새처럼 날개를 퍼덕여요.</>,
        <>이번엔 빠르게: 세 음 연달아, 동작 세 개.</>,
        <>바꿔요: 내가 치고, 선생님이 움직여요. 선생님을 헷갈리게 할 수 있을까요?</>,
      ] : [
        <>Your teacher plays a note. Low: crouch like the turtle. Middle: stand tall like Clara. High: flap like the bird.</>,
        <>Faster now: three notes in a row, three moves.</>,
        <>Swap: you play, your teacher moves. Can you catch them out?</>,
      ]}/>
      <LbRemember>{t('Low, middle, high: turtle, Clara, bird.', '낮은, 가운데, 높은: 거북이, 클라라, 새.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Same rhythm, or not?', '같은 리듬일까?')}
      teacher={<>{t('Two one-bar rhythms on one note, one after the other: walks, run-nings and holds, chapter ' + bkChapterNo('pulse') + '\'s words. The child answers the same or different. If "different" is a guess, ask where it changed: the start, the middle or the end. Swapping roles is the best part: to trick you, the child has to hold a rhythm and change it on purpose.', '한 음으로 한 마디 리듬 두 개를 차례로: 타, 티-티, 길게, ' + bkChapterNo('pulse') + '장의 낱말이에요. 아이는 같은지 다른지 답해요. "달라요"가 짐작이면 어디서 바뀌었는지 물어보세요: 처음, 가운데, 끝. 역할 바꾸기가 제일 좋아요: 선생님을 속이려면 아이가 리듬을 붙잡고 일부러 바꿔야 하니까요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={160}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%'}}>
        {row(t('the same', '같아요'), <LsCells cells={LS_R1[1].concat(LS_R1[1])} size={scr ? 26 : 44}/>)}
        {row(t('different', '달라요'), <LsCells cells={LS_R1[1].concat(LS_R1[6])} size={scr ? 26 : 44}/>, BK.coral)}
      </div></LbPic>} live={<QuickRound kind="rhythm" id="ep-rhythm"/>}/>
      <LbSay>{LANG === 'ko' ? <>리듬 두 개가 차례로 나와요. <b>같을까요</b>, <b>다를까요</b>? 둘 다 끝까지 들어요: 바뀐 곳은 어디에나 숨어 있어요. 낱말로 말해 봐요: <b>타</b>, <b>티-티</b>.</> : <>Two rhythms, one after the other. <b>The same</b>, or <b>different</b>? Listen to the end of both: the change can hide anywhere. Say the words: <b>walk</b>, <b>run-ning</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 리듬 두 개를 손뼉으로 쳐요. 같으면 엄지 위로, 다르면 엄지 아래로.</>,
        <>달랐나요? 두 번째 리듬을 손뼉 치며 말해 봐요: "타 티-티 타 타".</>,
        <>바꿔요: 내가 두 개를 치고, 선생님이 맞혀요. 아주 작은 차이로 속여 봐요.</>,
      ] : [
        <>Your teacher claps two rhythms. Thumbs up: the same. Thumbs down: different.</>,
        <>Different? Clap the second one and say it: "walk run-ning walk walk".</>,
        <>Swap: you clap two, your teacher answers. Try a tiny change to trick them.</>,
      ]}/>
      <LbRemember>{t('Listen to the end of both.', '둘 다 끝까지 들어요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Same tune, or not?', '같은 선율일까?')}
      teacher={<>{t('Two four-note tunes in C position; when they differ, one note has moved a step or two. If it is hard, the child sings the first one back before the second plays. Then swap: the child plays a tune twice and changes one note the second time.', 'C 자리의 네 음 선율 두 개. 다를 때는 한 음이 한두 칸 움직였어요. 어려우면 두 번째가 나오기 전에 첫 번째를 따라 불러요. 그다음 바꿔요: 아이가 선율을 두 번 치면서 두 번째에 한 음을 바꿔요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:12,width:'100%',maxWidth:scr ? 420 : 560,margin:'0 auto'}}>
        {row(t('tune 1', '선율 1'), <LsSingRow fs={[1, 3, 5, 3]} show size={scr ? 32 : 58}/>)}
        {row(t('tune 2', '선율 2'), <LsSingRow fs={[1, 3, 4, 3]} show lit={2} size={scr ? 32 : 58}/>, BK.coral)}
      </div></LbPic>} live={<QuickRound kind="tune" id="ep-tune"/>}/>
      <LbSay>{LANG === 'ko' ? <>짧은 선율 두 개. <b>같을까요</b>, 아니면 <b>한 음이 바뀌었을까요</b>? 두 번째가 나오는 동안 첫 번째를 속으로 불러요.</> : <>Two short tunes. <b>The same</b>, or did <b>one note change</b>? Sing the first one inside while the second plays.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 C 자리에서 짧은 선율 두 개를 쳐요. 같으면 끄덕, 다르면 도리도리.</>,
        <>달랐나요? 둘 다 불러 보고, 바뀐 음을 찾아요.</>,
        <>내 차례: 선율을 두 번 치는데, 두 번째에 한 음을 바꿔요. 선생님이 찾을 수 있을까요?</>,
      ] : [
        <>Your teacher plays two short tunes in C position. The same: nod. Different: shake your head.</>,
        <>Different? Sing both, and find the note that changed.</>,
        <>Your turn: play a tune twice and change one note the second time. Can your teacher spot it?</>,
      ]}/>
      <LbRemember>{t('Sing the first one inside.', '첫 번째를 속으로 불러요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Which way did it go?', '어느 쪽으로 갔을까?')}
      teacher={<>{t('Three notes near middle C, by step or a small skip: up and up, down and down, up then down, or down then up. Drawing the path on paper, a dot for each note joined up, is the first step towards reading the staff: up the page is up in sound.', '가운데 도 근처의 세 음, 한 칸이나 작은 건너뛰기로: 위로 위로, 아래로 아래로, 위로 그다음 아래로, 아래로 그다음 위로. 종이에 음마다 점을 찍고 이어 그리는 것이 오선 읽기의 첫걸음이에요: 종이 위쪽이 소리도 위쪽.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:scr ? 6 : 18,width:'100%',maxWidth:scr ? 560 : 640,margin:'0 auto'}}>{LS_SHAPES.map(sh => <div key={sh} style={{textAlign:'center'}}>{lsShapePic(sh, scr ? 60 : 130)}<div style={{fontSize:scr ? 12 : 15,fontWeight:800,color:BK.muted,marginTop:4}}>{lsShapeName(sh)}</div></div>)}</div></LbPic>} live={<QuickRound kind="shape" id="ep-shape"/>}/>
      <LbSay>{LANG === 'ko' ? <>세 음이 길을 만들어요: 새 쪽으로 <b>위로</b>, 거북이 쪽으로 <b>아래로</b>, 그리고 한 번 더. 들으면서 손가락으로 공중에 그려요.</> : <>Three notes make a path: <b>up</b> towards the bird or <b>down</b> towards the turtle, then once more. Draw it in the air as you listen.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 세 음을 쳐요. 손가락 하나로 공중에 길을 그려요.</>,
        <>이제 종이에: 음마다 점 하나, 점을 이어요.</>,
        <>바꿔요: 내가 길을 그리면, 선생님이 쳐요. 그림처럼 들렸나요?</>,
      ] : [
        <>Your teacher plays three notes. Draw the path in the air with one finger.</>,
        <>Now on paper: a dot for each note, joined up.</>,
        <>Swap: you draw a path, your teacher plays it. Did it sound like your drawing?</>,
      ]}/>
      <LbRemember>{t('Up to the bird, down to the turtle.', '위로는 새, 아래로는 거북이.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Find your note', '내 음 찾기')}
      teacher={<>{t('Sing first, then find it: the voice holds the note while the hand looks for it. Only C position (C to G) for now. If the child plays a wrong key, ask "higher or lower?" before they try again.', '먼저 부르고, 그다음 찾아요: 손이 찾는 동안 목소리가 그 음을 붙잡고 있어요. 지금은 C 자리(C부터 G)만 써요. 틀린 건반을 치면 다시 치기 전에 "더 높아? 더 낮아?"를 물어봐 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:420,margin:'0 auto',textAlign:'center'}}>
        <div style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:800,fontStyle:'italic',color:BK.coral,marginBottom:4}}>“la”</div>
        <HpKeys pos="C" hands="R" fingers={false} names={false} lit={{ 30: 'cor' }} k={2}/></div></LbPic>} live={<LsFindPad/>}/>
      <LbSay>{LANG === 'ko' ? <>음 하나를 들어요. <b>"라"로 따라 불러요</b>. 그다음 C 자리에서 찾아요: 쳐 보고, 들어 보고, <b>더 높을까요, 더 낮을까요?</b></> : <>Hear one note. <b>Sing it on "la"</b>. Then find it in C position: play, listen, <b>higher or lower?</b></>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>선생님이 C부터 G 사이의 음 하나를 쳐요. "라"로 불러요.</>,
        <>계속 부르면서 C 자리에서 찾아요. 틀리면: 더 높을까, 더 낮을까?</>,
        <>찾으면 그 건반을 치면서 함께 불러요. 음이름도 말해요.</>,
      ] : [
        <>Your teacher plays one note from C to G. Sing it on "la".</>,
        <>Keep singing while you look for it in C position. A wrong key: higher or lower?</>,
        <>Found it? Play it and sing with it. Say its letter name too.</>,
      ]}/>
      <LbRemember>{t('Sing it, then find it: higher or lower?', '부르고, 찾아요: 더 높아? 더 낮아?')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one with you, at the piano or away from it: you play or clap, the child answers by moving, singing or playing. You only correct.', '하나씩 선생님과 함께, 피아노 앞에서든 아니든: 선생님이 치거나 손뼉 치고, 아이는 움직이고, 부르고, 쳐서 답해요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_ep_five"/>}/>
    </LbPage>,
  ];
}
function EarPrepLessonBook() { return <>{epLbPages(false)}</>; }
function EpLearn({ onStart }) {
  const pages = epLbPages(true), opener = pages[0];
  return (
    <Lesson id="ear-prep" title={bkChapterName('ear-prep')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="ear-prep"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
Object.assign(EAR_PREP_DRILL, { levels: EP_LEVELS, generate: genLsQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lsAnswerLabel, Question: LsQuestion, Learn: EpLearn });
// the teacher's copy (no Workbook: every step is by ear)
function EpTeacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="ear-prep" teacher>{content}</WbPage>);
  const rw = (cells) => cells.map(lstWord).join(' ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('ear-prep')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear. In the app each step is a quick round of five questions with a streak and stars; away from the screen each one is a game with the body. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. The graded tests start in chapter {bkChapterNo('listen-sing')}.</div>
    <TcBlock page={2} title="Turtle, Clara or bird?" answers={<>{tcAns('PLAY ONE NOTE', ['LOW: C to G, two octaves below middle C', 'MIDDLE: the B below middle C, middle C, or D', 'HIGH: B to E, around two octaves above middle C'])}</>}
      watch="High heard as loud. Play a soft high note and a loud low one, so only the pitch gives the answer."
      say="“Low, middle, high: turtle, Clara, bird.”"/>
    <TcBlock page={3} title="Same rhythm, or not?" answers={<>{tcAns('CLAP TWO, ONE BAR EACH', [[0, 0], [1, 6], [2, 2], [3, 8], [5, 6]].map(([a, b]) => rw(LS_R1[a]) + '  /  ' + rw(LS_R1[b]) + (a === b ? '  (the same)' : '  (different)')))}</>}
      watch="Answering before the second rhythm ends. Listen to the end of both; then ask where it changed."
      say="“Listen to the end of both.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Same tune, or not?" answers={<>{tcAns('PLAY TWO, C POSITION', ['C D E C  /  C D E C  (the same)', 'C E G E  /  C E F E  (different: the 3rd note)', 'G F E D  /  G F E D  (the same)', 'E D C D  /  E D E D  (different: the 3rd note)'])}</>}
      watch="Guessing “different” every time. Sing the first tune back before the second plays."
      say="“Sing the first one inside.”"/>
    <TcBlock page={5} title="Which way did it go?" answers={<>{tcAns('PLAY THREE NOTES', ['C D E: up, then up', 'G F E: down, then down', 'C E D: up, then down', 'E C D: down, then up'])}</>}
      watch="Drawing with the whole arm too late. Draw while the notes sound, one finger, one dot a note."
      say="“Up to the bird, down to the turtle.”"/>
    <TcBlock page={6} title="Find your note" answers={<>{tcAns('PLAY', ['one note from C position (C to G); the child sings it, then finds it'])}</>}
      watch="Hunting along the keys. Ask “higher or lower?” before the next try."
      say="“Sing it, then find it: higher or lower?”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you, at the piano or away from it: you play or clap, the child moves, sings or plays. You only correct. Use material the child has not heard this week.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['ear-prep'] = EpTeacher;
'''
rep("""Object.assign(LISTEN_DRILL, { levels: LS_P_LEVELS, generate: genLsQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lsAnswerLabel, Question: LsQuestion, Learn: LsLearn });""",
    """Object.assign(LISTEN_DRILL, { levels: LS_P_LEVELS, generate: genLsQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: lsAnswerLabel, Question: LsQuestion, Learn: LsLearn });""" + EP)

# ── 5. Ear Training, Grade 1 (was Listen, Clap, Write) ──
within("function lwLbPages(scr = false) {", "function ListenWriteLessonBook()", [
    ("""[[lwPicHome(), t('I hum the home note at the end of an unfinished tune', '끝나지 않은 선율 끝에 집 음을 흥얼거려요')], [lwPicMetre(), t('I hear two or three beats in a bar', '한 마디에 두 박인지 세 박인지 들어요')],
    [lwPicClap(), t('I clap back a passage I have heard twice', '두 번 들은 리듬을 따라 쳐요')], [lwPicPhrase(), t('I sing back a tune with its rhythm, then play it', '리듬까지 선율을 따라 부르고 쳐요')], [lwPicWrite(), t('I write down two bars of crotchets and minims', '4분음표와 2분음표 두 마디를 받아 적어요')]];""",
     """[[lwPicHome(), t('I hum the home note at the end of an unfinished tune', '끝나지 않은 선율 끝에 집 음을 흥얼거려요')],
    [lwPicClap(), t('I clap back a passage I have heard twice', '두 번 들은 리듬을 따라 쳐요')], [lwPicPhrase(), t('I sing back a tune with its rhythm, then play it', '리듬까지 선율을 따라 부르고 쳐요')]];"""),
    ("""const toc = [[t('The home note', '집 음'), 2], [t('Two or three?', '두 박? 세 박?'), 3], [t('Clap it back', '따라 치기'), 4], [t('Sing it with its rhythm', '리듬까지 따라 부르기'), 5], [t('Write the rhythm', '리듬 받아 적기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];""",
     """const toc = [[t('The home note', '집 음'), 2], [t('Clap it back', '따라 치기'), 3], [t('Sing it with its rhythm', '리듬까지 따라 부르기'), 4], [t('My three checks', '나의 세 가지 확인'), 5]];"""),
    ("""{t('Chapter ' + bkChapterNo('listen-sing') + ' a step further, as the Grade 1 aural tests and the listening part of the Grade 1 theory ask: the tonic at the end of an unfinished phrase; a passage in duple or triple time played twice, then tapped or clapped; a short phrase played twice, sung back with its rhythm; and, on paper, two bars of crotchets and minims in 2/4 or 3/4 written from dictation (played up to five times).', bkChapterNo('listen-sing') + '장에서 한 걸음 더: 2단계 청음과 이론 시험의 듣기처럼, 끝나지 않은 선율 끝의 으뜸음, 두 번 들려준 두 박·세 박 리듬 따라 치기, 두 번 들려준 짧은 선율을 리듬까지 따라 부르기, 그리고 종이에 2/4나 3/4의 4분음표·2분음표 두 마디 받아 적기(다섯 번까지 들려줘요).')}""",
     """{t('The Grade 1 aural tests, one step each (Manual of Syllabuses, section 21): the tonic hummed or sung at the end of a short unfinished phrase; a passage in duple or triple time played twice, then tapped or clapped back; a short phrase played twice, hummed or sung back with its melody and its time. Chapter ' + bkChapterNo('listen-sing') + ' a step further: from this grade on, every test is played twice.', '1급 청음 시험을 한 단계씩(실라버스 21절): 끝나지 않은 짧은 선율 끝의 으뜸음을 흥얼거리거나 부르기; 두 박이나 세 박 리듬을 두 번 듣고 따라 치기; 짧은 선율을 두 번 듣고 음과 리듬까지 따라 부르기. ' + bkChapterNo('listen-sing') + '장에서 한 걸음 더: 이 급부터 모든 시험을 두 번 들려줘요.')}"""),
    ("""{t('Listen, Clap, Write', '듣고, 치고, 적기')}""", """{t('Ear Training, Grade 1', '청음, Grade 1')}"""),
    ("""{rqStaffEl(lwDictItems(LW_DICTS[2]), { hearts: false })}""", """{rqStaffEl(LW_CLAP[1], { hearts: false })}"""),
    ("""{t('Your ears a step further: find home, feel two or three, clap it back, sing it with its rhythm, write it down.', '귀를 한 걸음 더: 집 음 찾기, 두 박·세 박 느끼기, 따라 치기, 리듬까지 부르기, 받아 적기.')}""",
     """{t('Your ears for Grade 1: find home, clap it back, sing it with its rhythm.', '1급의 귀: 집 음 찾기, 따라 치기, 리듬까지 부르기.')}"""),
    ("""t('hear two or three beats in a bar', '한 마디의 두 박·세 박을 들을 수 있어요'), """, ""),
    (""", t('write down a two-bar rhythm', '두 마디 리듬을 받아 적을 수 있어요')]""", """]"""),
    ("""<LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Clap it back', '따라 치기')}""", """<LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Clap it back', '따라 치기')}"""),
    ("""'장의 메아리보다 길고, 두 번 들어요: 전체 모양을 들어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>""", """'장의 메아리보다 길고, 두 번 들어요: 전체 모양을 들어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>"""),
    ("""<LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Sing it with its rhythm', '리듬까지 따라 부르기')}""", """<LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Sing it with its rhythm', '리듬까지 따라 부르기')}"""),
    ("""'타, 티-티, 긴 음이 섞인 짧은 선율을 두 번 쳐 주세요. 아이는 음과 리듬을 둘 다 살려 "라"로 따라 불러요. 그다음 C 자리에서 쳐요. 리듬이 흔들리면 먼저 손뼉으로 치고, 그다음 불러요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>""",
     """'타, 티-티, 긴 음이 섞인 짧은 선율을 두 번 쳐 주세요. 아이는 음과 리듬을 둘 다 살려 "라"로 따라 불러요. 그다음 C 자리에서 쳐요. 리듬이 흔들리면 먼저 손뼉으로 치고, 그다음 불러요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>"""),
    ("""<LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}""", """<LbPage key="5" no={5} chId={ch} kicker={t('Check-up', '점검')} title={t('My three checks', '나의 세 가지 확인')}"""),
    ("""{t('Each one with you at the piano, away from the screen: you play, the child hums, says, claps, sings or writes. You only correct.', '하나씩 화면 없이 피아노 앞에서: 선생님이 치고, 아이는 흥얼거리고, 말하고, 손뼉 치고, 부르고, 적어요. 선생님은 고쳐 주기만 해요.')}""",
     """{t('Each one with you at the piano, away from the screen, played twice: you play, the child hums, claps or sings. You only correct.', '하나씩 화면 없이 피아노 앞에서, 두 번씩: 선생님이 치고, 아이는 흥얼거리고, 손뼉 치고, 불러요. 선생님은 고쳐 주기만 해요.')}"""),
    ("""storeKey="pb_lw_five\"""", """storeKey="pb_lw_three\""""),
])
cut("""    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Two or three?', '두 박? 세 박?')}""", """    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Clap it back', '따라 치기')}""")
cut("""    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Write the rhythm', '리듬 받아 적기')}""", """    <LbPage key="5" no={5} chId={ch} kicker={t('Check-up', '점검')} title={t('My three checks', '나의 세 가지 확인')}""")
within("function LwTeacher() {", "TEACHER_COPIES['listen-write'] = LwTeacher;", [
    ("""No Workbook for this chapter: every step is by ear, as the Grade 1 aural tests and the listening part of the Grade 1 theory ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. The dictation on page 6 is written on paper: any staff paper will do.</div>""",
     """No Workbook for this chapter: every step is by ear, as the Grade 1 aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice, as the examiner does.</div>"""),
    ("""    <TcBlock page={3} title="Two or three?" answers={<>{tcAns('PLAY', ['oom-pah: the low note on 1, the chord on 2 (two)', 'oom-pah-pah: the low note on 1, the chord on 2 and 3 (three)', 'then a tune with no accompaniment: count from each strong note'])}</>}
      watch="Counting every note instead of feeling where the strong one comes back. Sway or step on 1."
      say="“Oom-pah: two. Oom-pah-pah: three.”"/>
""", ""),
    ("""<TcBlock page={4} title="Clap it back\"""", """<TcBlock page={3} title="Clap it back\""""),
    ("""<TcBlock page={5} title="Sing it with its rhythm\"""", """<TcBlock page={4} title="Sing it with its rhythm\""""),
    ("""<TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen: you play, the child hums, says, claps, sings or writes.""",
     """<TcBlock page={5} title="My three checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen, played twice: you play, the child hums, claps or sings."""),
])
cut("""    <TcBlock page={6} title="Write the rhythm\"""", """    <TcBlock page={5} title="My three checks\"""")
rep("""    <Lesson id="listen-write" title={t('Listen, clap, write', '듣고, 치고, 적기')} onStart={onStart} noArt""",
    """    <Lesson id="listen-write" title={bkChapterName('listen-write')} onStart={onStart} noArt""")
rep("""const LW_LEVELS = [
  { n: 1, label: 'Find the home note', kind: 'home', time: 16 },
  { n: 2, label: 'Two or three beats?', kind: 'metre', time: 14 },
  { n: 3, label: 'Which rhythm did you hear?', kind: 'which', time: 16 },
  { n: 4, label: 'Which shape did the tune make?', kind: 'shape', time: 16 },
  { n: 5, label: 'Clap it back', kind: 'clap', time: 40 },
  { n: 6, label: 'Write the rhythm', kind: 'write', time: 60 },
];""", """const LW_LEVELS = [   // Build CC: the Grade 1 tests (two or three moved to Grade 3; the dictation left the ear rooms)
  { n: 1, label: 'Find the home note', kind: 'home', time: 16 },
  { n: 2, label: 'Which rhythm did you hear?', kind: 'which', time: 16 },
  { n: 3, label: 'Which shape did the tune make?', kind: 'shape', time: 16 },
  { n: 4, label: 'Clap it back', kind: 'clap', time: 40 },
];""")

# ── 6. Ear Training, Grade 2 and Grade 3: a room each ──
# the clap-back pad: Grade 2 claps it back only; Grade 3 also says two or three
rep("""function L2ClapPad({ onResult, fixed }) {""", """function L2ClapPad({ onResult, fixed, askMetre = true }) {   // Build CC: askMetre false for Grade 2 (clap it back only)""")
within("function L2ClapPad({ onResult, fixed, askMetre = true }) {", "// ── step 5: a longer tune", [
    ("""      setRes({ hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok: E.full ? mt.hits >= notes.length - 1 && mt.extra <= 1 : mt.hits === notes.length && mt.extra === 0 }); setPhase('done'); }); };""",
     """      const ok = E.full ? mt.hits >= notes.length - 1 && mt.extra <= 1 : mt.hits === notes.length && mt.extra === 0;
      setRes({ hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok }); setPhase('done'); if (!askMetre && E.full && onResult) onResult({ ok, clap: ok }); }); };"""),
    ("""<div style={actTitle}>{t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?')}</div>""",
     """<div style={actTitle}>{askMetre ? t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?') : t('Clap it back', '따라 치기')}</div>"""),
    ("""<div style={actNote}>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 그다음 클릭에 맞춰 똑같이 치고, <b>두 박인지 세 박인지</b> 말해요. 이번에는 <b>점4분음표와 8분음표</b>(길게, 짧게)도 나와요.</>
        : <>Hear the passage <b>twice</b>. Then tap it back with the clicks and say: <b>two or three</b> beats in a bar? Now with <b>the dotted crotchet and quaver</b> too (long, short).</>}</div>""",
     """<div style={actNote}>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 그다음 클릭에 맞춰 똑같이 쳐요{askMetre ? <>, 그리고 <b>두 박인지 세 박인지</b> 말해요</> : null}. 이번에는 <b>점4분음표와 8분음표</b>(길게, 짧게)도 나와요.</>
        : <>Hear the passage <b>twice</b>. Then tap it back with the clicks{askMetre ? <> and say: <b>two or three</b> beats in a bar?</> : '.'} Now with <b>the dotted crotchet and quaver</b> too (long, short).</>}</div>"""),
    ("""{met || (res && !E.full) ? rqStaffEl(""", """{met || (res && (!E.full || !askMetre)) ? rqStaffEl("""),
    ("""(E.full ? '. Two or three?' : res.ok ? ' ✓' : ''), '제때: ' + res.total + '개 중 ' + res.hits + '개' + (E.full ? '. 두 박? 세 박?' : res.ok ? ' ✓' : ''))""",
     """(E.full && askMetre ? '. Two or three?' : res.ok ? ' ✓' : ''), '제때: ' + res.total + '개 중 ' + res.hits + '개' + (E.full && askMetre ? '. 두 박? 세 박?' : res.ok ? ' ✓' : ''))"""),
    ("""{res && !met && E.full && <div""", """{res && !met && E.full && askMetre && <div"""),
    ("""{(E.full ? met : res) && ecNext(""", """{(E.full && askMetre ? met : res) && ecNext("""),
])

L2PAGES = r'''function l2LbPages(scr = false, g = 2) {   // Build CC: Grade 2 and Grade 3 are a room each; the steps are the grade's own tests
  const ch = g === 3 ? 'listen-3' : 'listen-23';
  const order = g === 3 ? ['any', 'deg', 'metre', 'clap', 'sing'] : ['dyad', 'clap', 'sing'];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const NAME = { dyad: t('Two notes at once', '두 음을 함께'), any: t('Any two notes', '어떤 두 음이든'), deg: t('From the keynote', '으뜸음에서'), metre: t('Two or three?', '두 박? 세 박?'),
    clap: g === 3 ? t('Clap it back: two or three?', '따라 치고, 두 박? 세 박?') : t('Clap it back', '따라 치기'), sing: t('Sing a longer tune', '더 긴 선율 따라 부르기') };
  const CK = { dyad: [l2PicDyad(), t('I hum the higher or the lower of two notes played together (a 3rd or a 5th)', '함께 울린 두 음(3도나 5도) 중 높은 음이나 낮은 음을 흥얼거려요')],
    any: [l2PicAny(), t('I hum the higher or the lower of any two notes', '어떤 두 음이든 높은 음이나 낮은 음을 흥얼거려요')],
    deg: [l2PicDeg(), t('I sing and name the 2nd, 3rd, 4th or 5th from the keynote', '으뜸음에서 2도, 3도, 4도, 5도를 부르고 이름을 말해요')],
    metre: [lwPicMetre(), t('I hear two or three beats in a bar', '한 마디에 두 박인지 세 박인지 들어요')],
    clap: [l2PicClap(), g === 3 ? t('I clap back a passage and say two or three', '리듬을 따라 치고 두 박인지 세 박인지 말해요') : t('I clap back a passage I have heard twice', '두 번 들은 리듬을 따라 쳐요')],
    sing: [l2PicSing(), t('I sing back a longer tune with its rhythm', '더 긴 선율을 리듬까지 따라 불러요')] };
  const END = { dyad: t('hum the higher or the lower of two notes together', '함께 울린 두 음 중 높은 음이나 낮은 음을 흥얼거릴 수 있어요'), any: t('hum the higher or the lower of any two notes together', '함께 울린 어떤 두 음이든 높은 음이나 낮은 음을 흥얼거릴 수 있어요'),
    deg: t('sing and name the 2nd, 3rd, 4th or 5th from the keynote', '으뜸음에서 2도, 3도, 4도, 5도를 부르고 이름을 말할 수 있어요'), metre: t('feel two or three beats in a bar', '한 마디의 두 박·세 박을 느낄 수 있어요'),
    clap: g === 3 ? t('clap back a passage and say two or three', '리듬을 따라 치고 두 박인지 세 박인지 말할 수 있어요') : t('clap back a passage heard twice', '두 번 들은 리듬을 따라 칠 수 있어요'), sing: t('sing back a longer tune with its rhythm', '더 긴 선율을 리듬까지 따라 부를 수 있어요') };
  const nw = ['', 'one', 'two', 'three', 'four', 'five'][order.length], nk = ['', '한', '두', '세', '네', '다섯'][order.length];
  const checksT = t('My ' + nw + ' checks', '나의 ' + nk + ' 가지 확인'), checks = order.map(x => CK[x]);
  const toc = order.map((x, j) => [NAME[x], j + 2]).concat([[checksT, order.length + 2]]);
  const dyadStill = (pairs) => <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:620,margin:'0 auto'}}>{pairs.map(([a, b]) => <div key={a + '-' + b}>
    <div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{l2Let(a)} + {l2Let(b)}: {l2IvName(a, b)}</div>
    <SpKb lo={0} hi={12} W={scr ? 26 : 36} H={scr ? 66 : 96} lit={{ [a]: 'pale', [b]: 'cor' }} names={{ [a]: l2Let(a), [b]: l2Let(b) }}/></div>)}</div></LbPic>;
  const opTeach = g === 3
    ? t('The Grade 3 aural tests, one step each (Manual of Syllabuses, section 21): any two notes played together within an octave from middle C, the higher or the lower sung; the keynote, then the 2nd, 3rd, 4th or 5th of the major scale straight after it, sung and named; a passage in duple or triple time played twice, tapped or clapped back, and named duple or triple; a short phrase played twice, sung back with its rhythm. Every test is played twice. The app plays and scores the taps and answers; whether a child sang in tune is your ear.', '3급 청음 시험을 한 단계씩(실라버스 21절): 가운데 도부터 한 옥타브 안에서 함께 울린 어떤 두 음이든 높은 음이나 낮은 음 부르기; 으뜸음 바로 다음의 장음계 2도, 3도, 4도, 5도를 부르고 이름 말하기; 두 박이나 세 박 리듬을 두 번 듣고 따라 치고 박자 말하기; 짧은 선율을 두 번 듣고 리듬까지 따라 부르기. 모든 시험을 두 번 들려줘요. 앱은 탭과 답을 채점하고, 음정이 맞았는지는 선생님의 귀예요.')
    : t('The Grade 2 aural tests, one step each (Manual of Syllabuses, section 21): two notes a major 3rd or a perfect 5th apart, played together within an octave from middle C, the higher or the lower sung; a passage in duple or triple time played twice, then tapped or clapped back; a short phrase played twice, sung back with its melody and time. Every test is played twice. The app plays and scores the taps; whether a child sang in tune is your ear.', '2급 청음 시험을 한 단계씩(실라버스 21절): 가운데 도부터 한 옥타브 안에서 장3도나 완전5도 떨어져 함께 울린 두 음 중 높은 음이나 낮은 음 부르기; 두 박이나 세 박 리듬을 두 번 듣고 따라 치기; 짧은 선율을 두 번 듣고 음과 리듬까지 따라 부르기. 모든 시험을 두 번 들려줘요. 앱은 탭을 채점하고, 음정이 맞았는지는 선생님의 귀예요.');
  const step = (x, k) => { const no = k + 1, kick = t('Step ' + k, k + '단계'), qr = bkLink('drill=' + ch + '&tab=drill&level=' + k);
    if (x === 'dyad') return <LbPage key={no} no={no} chId={ch} kicker={kick} title={NAME.dyad}
      teacher={<>{t('Grade 2: two notes played together, a major 3rd or a perfect 5th apart, within an octave from middle C; the child hums or sings the higher or the lower one, as asked. Played twice. If it is hard, play the two one after the other, then together again; the top note is usually easier to hear first.', '2급: 장3도나 완전5도 떨어진 두 음을 함께 쳐요(가운데 도부터 한 옥타브 안). 아이는 묻는 대로 높은 음이나 낮은 음을 흥얼거리거나 불러요. 두 번 들려줘요. 어려우면 두 음을 하나씩 친 다음 다시 함께 쳐 주세요. 보통 위의 음이 먼저 잘 들려요.')}</>} qr={qr}>
      <LbLive still={dyadStill([[0, 4], [5, 12]])} live={<L2DyadPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 음이 <b>함께</b> 울려요. 선생님이 묻는 음을 흥얼거려요: <b>높은 음</b>(새 쪽)이나 <b>낮은 음</b>(거북이 쪽). 그다음 건반에서 찾아요.</> : <>Two notes sound <b>together</b>. Hum the one your teacher asks for: <b>the higher</b> (the bird's) or <b>the lower</b> (the turtle's). Then find it on the keys.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 두 음을 함께 두 번 쳐요. 높은 음부터 흥얼거려 봐요.</>, <>이번엔 낮은 음. 어려우면 선생님이 두 음을 하나씩 쳐 줘요.</>, <>흥얼거린 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays two notes together, twice. Hum the higher one first.</>, <>Now the lower one. If it is hard, your teacher plays them one at a time.</>, <>Find the note you hummed on the keys.</>]}/>
      <LbRemember>{t('Two at once: pick one out and hum it.', '함께 울리는 두 음: 하나를 골라 흥얼거려요.')}</LbRemember>
    </LbPage>;
    if (x === 'any') return <LbPage key={no} no={no} chId={ch} kicker={kick} title={NAME.any}
      teacher={<>{t('Grade 3: any two notes played together, within an octave from middle C. The closer the notes, the harder: a 2nd is the hardest. If the child is stuck, play the asked note alone, then the pair again.', '3급: 가운데 도부터 한 옥타브 안의 어떤 두 음이든 함께 쳐요. 두 음이 가까울수록 어려워요: 2도가 가장 어려워요. 막히면 묻는 음만 따로 친 다음 다시 두 음을 함께 쳐 주세요.')}</>} qr={qr}>
      <LbLive still={dyadStill([[4, 5], [2, 11]])} live={<L2DyadPad any/>}/>
      <LbSay>{LANG === 'ko' ? <>이제 <b>어떤 두 음이든</b>. 가까운 두 음은 더 어려워요. 먼저 두 음을 듣고, 묻는 음 하나만 마음속으로 따라가요.</> : <>Now <b>any two notes</b>. Close ones are harder. Hear both, then follow just the one you are asked for.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 두 음을 함께 두 번 쳐요. 높은 음, 그다음 낮은 음을 흥얼거려요.</>, <>가까운 두 음(2도)도 해 봐요.</>, <>흥얼거린 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays two notes together, twice. Hum the higher, then the lower.</>, <>Try two close ones (a 2nd) too.</>, <>Find the note you hummed on the keys.</>]}/>
      <LbRemember>{t('Close or far: follow just one.', '가깝든 멀든: 하나만 따라가요.')}</LbRemember>
    </LbPage>;
    if (x === 'deg') return <LbPage key={no} no={no} chId={ch} kicker={kick} title={NAME.deg}
      teacher={<>{t('Grade 3: you sound the keynote, then the 2nd, 3rd, 4th or 5th of the major scale straight after it; the child sings it, then names it ("the 3rd"). Played twice. To find the number, sing up the scale from the keynote (1 2 3 4 5) until the voice meets the note.', '3급: 으뜸음을 울린 다음 바로 장음계의 2도, 3도, 4도, 5도를 쳐요. 아이는 그 음을 부르고 이름을 말해요("3도"). 두 번 들려줘요. 숫자를 찾으려면 으뜸음에서 음계를 1 2 3 4 5로 올라가며 불러서 그 음을 만날 때까지 가요.')}</>} qr={qr}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:540,margin:'0 auto'}}><SpKb maxW={540} lo={0} hi={14} W={32} H={80} lit={{ 0: 'cor', 2: 'pale', 4: 'pale', 5: 'pale', 7: 'pale' }} names={{ 0: '1', 2: '2', 4: '3', 5: '4', 7: '5' }}/></div></LbPic>} live={<L2DegPad/>}/>
      <LbSay>{LANG === 'ko' ? <>먼저 <b>으뜸음(1)</b>, 그다음 다른 음. 1에서 <b>1 2 3 4 5</b>로 올라가며 불러요. 그 음을 만나는 숫자가 이름이에요: <b>2도, 3도, 4도, 5도</b>.</> : <>First <b>the keynote (1)</b>, then another note. Sing up from 1, <b>1 2 3 4 5</b>. The number where you meet it is its name: <b>the 2nd, 3rd, 4th or 5th</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 으뜸음과 다른 음을 두 번 쳐요. 그 음을 불러요.</>, <>으뜸음에서 1 2 3 4 5로 올라가며 불러서 숫자를 찾아요.</>, <>이름을 말해요: "3도", "5도".</>]
        : [<>Your teacher plays the keynote and another note, twice. Sing the note.</>, <>Sing up from the keynote, 1 2 3 4 5, to find its number.</>, <>Say its name: "the 3rd", "the 5th".</>]}/>
      <LbRemember>{t('Sing up from home until you meet it.', '집에서부터 올라가며, 만날 때까지 불러요.')}</LbRemember>
    </LbPage>;
    if (x === 'metre') return <LbPage key={no} no={no} chId={ch} kicker={kick} title={NAME.metre}
      teacher={<>{t('Grade 3 says whether the passage it claps back is in duple or triple time. First the feel of it: play a simple accompaniment, the low note on beat 1 and the chord on the others (oom-pah, oom-pah-pah); the child counts from each low note, or sways on 1. Then a rhythm with no accompaniment, and ask again.', '3급은 따라 친 리듬이 두 박인지 세 박인지 말해요. 먼저 느낌부터: 간단한 반주를 쳐 주세요, 1박에 낮은 음, 나머지 박에 화음(쿵-짝, 쿵-짝-짝). 아이는 낮은 음마다 1부터 세거나, 1에서 몸을 흔들어요. 그다음 반주 없는 리듬으로 다시 물어봐요.')}</>} qr={qr}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',display:'grid',gap:10}}>{[2, 3].map(m => <div key={m} style={{display:'grid',gridTemplateColumns:'90px 1fr',alignItems:'center',gap:6}}><span style={{fontSize:12.5,fontWeight:900,color:BK.muted}}>{m === 2 ? t('oom-pah', '쿵-짝') : t('oom-pah-pah', '쿵-짝-짝')}</span><PlCircles n={m * 4} r={scr ? 10 : 13} gap={scr ? 24 : 32} group={m} kind={(i) => (i % m === 0 ? 'play' : 'beat')} label={(i) => String(i % m + 1)}/></div>)}</div></LbPic>} live={<LwMetrePad/>}/>
      <LbSay>{LANG === 'ko' ? <>센 박(1)이 몇 박마다 오는지 들어요. <b>쿵-짝</b>이면 한 마디에 <b>두 박</b>, <b>쿵-짝-짝</b>이면 <b>세 박</b>.</> : <>Listen for how often the strong beat (1) comes. <b>Oom-pah</b>: <b>two</b> beats in a bar. <b>Oom-pah-pah</b>: <b>three</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 반주를 쳐요. 낮은 음마다 1부터 세어요.</>, <>두 박이면 1에서 손뼉, 2에서 무릎. 세 박이면 손뼉, 무릎, 무릎.</>, <>반주 없는 리듬으로도 해 봐요.</>]
        : [<>Your teacher plays an accompaniment. Count from 1 at each low note.</>, <>In two: clap on 1, pat your knees on 2. In three: clap, pat, pat.</>, <>Now try it with a rhythm on its own.</>]}/>
      <LbRemember>{t('Oom-pah: two. Oom-pah-pah: three.', '쿵-짝: 두 박. 쿵-짝-짝: 세 박.')}</LbRemember>
    </LbPage>;
    if (x === 'clap') return <LbPage key={no} no={no} chId={ch} kicker={kick} title={NAME.clap}
      teacher={<>{g === 3 ? t('Grade 3: a passage in duple or triple time played twice; the child claps or taps it back, then says whether it was duple or triple. The Manual makes the examples harder with each grade, so these passages have the dotted crotchet and quaver (long, short). Listen both times without clapping; count inside.', '3급: 두 박이나 세 박의 리듬을 두 번 쳐요. 아이는 손뼉이나 탭으로 따라 친 다음, 두 박인지 세 박인지 말해요. 실라버스는 급마다 예제를 더 어렵게 하니까, 이 리듬에는 점4분음표와 8분음표(길게, 짧게)가 나와요. 두 번 다 손뼉 치지 않고 들으며 속으로 세요.')
        : t('Grade 2: a passage in duple or triple time played twice; the child claps or taps it back. The Manual makes the examples harder with each grade, so these passages add the dotted crotchet and quaver (long, short) to the Grade 1 room\'s. Listen both times without clapping; count inside.', '2급: 두 박이나 세 박의 리듬을 두 번 쳐요. 아이는 손뼉이나 탭으로 따라 쳐요. 실라버스는 급마다 예제를 더 어렵게 하니까, 1급 방의 리듬에 점4분음표와 8분음표(길게, 짧게)가 더해져요. 두 번 다 손뼉 치지 않고 들으며 속으로 세요.')}</>} qr={qr}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{rqStaffEl(L2_CLAP[1], { hearts: false })}</div></LbPic>} live={g === 3 ? <L2ClapPad/> : <L2ClapPad askMetre={false}/>}/>
      <LbSay>{LANG === 'ko' ? <>리듬을 <b>두 번</b> 들어요. 같은 빠르기로 똑같이 쳐요{g === 3 ? <>, 그리고 <b>두 박인지 세 박인지</b> 말해요</> : null}. <b>점4분음표와 8분음표</b>는 길게, 짧게.</> : <>Hear it <b>twice</b>. Clap it back at the same speed{g === 3 ? <>, then say <b>two or three</b></> : null}. <b>The dotted crotchet and quaver</b>: long, short.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 네 마디를 두 번 쳐요. 듣기만 하며 속으로 세요.</>, <>같은 빠르기로 손뼉 쳐요.</>, g === 3 ? <>두 박이었나요, 세 박이었나요? 센 박이 몇 박마다 오는지 떠올려요.</> : <>틀린 곳은 선생님이 그 마디만 다시 쳐 줘요.</>]
        : [<>Your teacher plays four bars, twice. Just listen and count inside.</>, <>Clap it back at the same speed.</>, g === 3 ? <>Two or three? Think how often the strong beat came.</> : <>Where it went wrong, your teacher plays just that bar again.</>]}/>
      <LbRemember>{g === 3 ? t('Clap it back, then say two or three.', '따라 치고, 두 박인지 세 박인지 말해요.') : t('Listen twice, then clap: long, short.', '두 번 듣고 손뼉: 길게, 짧게.')}</LbRemember>
    </LbPage>;
    return <LbPage key={no} no={no} chId={ch} kicker={kick} title={NAME.sing}
      teacher={<>{t('Grade ' + g + ': a short phrase played twice, combining melody and time. The Manual makes the examples harder with each grade, so the tunes here are longer and wider than the Grade 1 room\'s: up to eight notes, skips as well as steps, within an octave from middle C. Sing back on "la"; then play it. If the rhythm slips, clap it first.', g + '급: 음과 리듬이 함께 있는 짧은 선율을 두 번 쳐요. 실라버스는 급마다 예제를 더 어렵게 하니까, 여기 선율은 1급 방보다 길고 넓어요: 여덟 음까지, 한 걸음과 건너뛰기, 가운데 도부터 한 옥타브 안. "라"로 따라 부르고, 그다음 쳐요. 리듬이 흔들리면 먼저 손뼉으로 쳐요.')}</>} qr={qr}>
      <LbLive still={<LbPic h={150}><div style={{display:'flex',flexDirection:'column',gap:10,width:'100%',maxWidth:scr ? 480 : 640,margin:'0 auto'}}><L2Pills ph={L2_PH[1]} show u={scr ? 34 : 50}/><SpKb lo={0} hi={12} W={scr ? 30 : 44} H={scr ? 70 : 104} lit={Object.fromEntries(L2_PH[1].map(([k]) => [k, 'pale']))} names={Object.fromEntries(L2_PH[1].map(([k]) => [k, l2Let(k)]))}/></div></LbPic>} live={<L2SingPad/>}/>
      <LbSay>{LANG === 'ko' ? <>이번 선율은 <b>더 길고</b>, <b>건너뛰는 음</b>도 있어요. 두 번 듣고, <b>음도 리듬도</b> 따라 불러요: 타, 티-티, 길게.</> : <>This tune is <b>longer</b>, with <b>skips</b> as well as steps. Hear it twice and sing back <b>the notes and the rhythm</b>: walk, run-ning, hold.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 선율을 두 번 쳐요. 들으며 속으로 따라 불러요.</>, <>"라"로 불러요: 음도, 리듬도.</>, <>건반에서 쳐요. 긴 음은 끝까지 누르고 있어요.</>]
        : [<>Your teacher plays the tune twice. Sing along inside as you listen.</>, <>Sing it on "la": the notes and the rhythm.</>, <>Play it on the keys. Hold the long note to its end.</>]}/>
      <LbRemember>{t('Longer, with skips: the notes and the rhythm, both.', '더 길고 건너뛰어도: 음도, 리듬도.')}</LbRemember>
    </LbPage>; };
  const last = order.length + 2;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{opTeach}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{g === 3 ? t('Ear Training, Grade 3', '청음, Grade 3') : t('Ear Training, Grade 2', '청음, Grade 2')}</div>
      </div></LbOnly>
      {dyadStill(g === 3 ? [[2, 5], [0, 9]] : [[0, 4], [0, 7]])}
      <LbSay size={18}>{g === 3 ? t('Your ears for Grade 3: any two notes at once, the notes of the scale from home, two or three, and longer tunes.', '3급의 귀: 함께 울리는 어떤 두 음이든, 집에서 세는 음계의 음, 두 박·세 박, 더 긴 선율.') : t('Your ears for Grade 2: two notes at once, a passage clapped back, and a longer tune sung back.', '2급의 귀: 함께 울리는 두 음, 따라 치는 리듬, 따라 부르는 더 긴 선율.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {order.map(x => END[x]).map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    ...order.map((x, j) => step(x, j + 1)),
    <LbPage key={last} no={last} chId={ch} kicker={t('Check-up', '점검')} title={checksT}
      teacher={<>{g === 3 ? t('Each one with you at the piano, away from the screen, played twice as in the exam: you play, the child hums, sings, names or claps. You only correct.', '하나씩 화면 없이 피아노 앞에서, 시험처럼 두 번씩: 선생님이 치고, 아이는 흥얼거리고, 부르고, 이름을 말하고, 손뼉 쳐요. 선생님은 고쳐 주기만 해요.') : t('Each one with you at the piano, away from the screen, played twice as in the exam: you play, the child hums, claps or sings. You only correct.', '하나씩 화면 없이 피아노 앞에서, 시험처럼 두 번씩: 선생님이 치고, 아이는 흥얼거리고, 손뼉 치고, 불러요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey={g === 3 ? 'pb_l3_five' : 'pb_l2_three'}/>}/>
    </LbPage>,
  ];
}
function Listen23LessonBook() { return <>{l2LbPages(false, 2)}</>; }
function Listen3LessonBook() { return <>{l2LbPages(false, 3)}</>; }
function L2Learn({ onStart, g = 2 }) {
  const ch = g === 3 ? 'listen-3' : 'listen-23', pages = l2LbPages(true, g), opener = pages[0];
  return (
    <Lesson id={ch} title={bkChapterName(ch)} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value={ch}><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const L3Learn = ({ onStart }) => <L2Learn onStart={onStart} g={3}/>;
'''
a = s.index("function l2LbPages(scr = false) {"); b = s.index("// ── the drill: every question is heard (twice, as the tests are) ──", a)
s = s[:a] + L2PAGES + s[b:]
rep("""const L2_LEVELS = [
  { n: 1, label: 'Two notes: hum the higher or the lower (3rd or 5th)', kind: 'dyad', time: 30 },
  { n: 2, label: 'Any two notes: hum the higher or the lower', kind: 'any', time: 30 },
  { n: 3, label: 'From the keynote: 2nd, 3rd, 4th or 5th?', kind: 'deg', time: 20 },
  { n: 4, label: 'Duple or triple?', kind: 'metre', time: 20 },
  { n: 5, label: 'Clap it back, then two or three', kind: 'clap', time: 45 },
  { n: 6, label: 'Sing a longer tune, then play it', kind: 'sing', time: 60 },
];""", """const L2_LEVELS = [   // Build CC: Grade 2
  { n: 1, label: 'Two notes: hum the higher or the lower (3rd or 5th)', kind: 'dyad', time: 30 },
  { n: 2, label: 'Clap it back', kind: 'clap2', time: 45 },
  { n: 3, label: 'Sing a longer tune, then play it', kind: 'sing', time: 60 },
];
const L3_LEVELS = [   // Build CC: Grade 3
  { n: 1, label: 'Any two notes: hum the higher or the lower', kind: 'any', time: 30 },
  { n: 2, label: 'From the keynote: 2nd, 3rd, 4th or 5th?', kind: 'deg', time: 20 },
  { n: 3, label: 'Duple or triple?', kind: 'metre', time: 20 },
  { n: 4, label: 'Clap it back, then two or three', kind: 'clap', time: 45 },
  { n: 5, label: 'Sing a longer tune, then play it', kind: 'sing', time: 60 },
];""")
rep("""  if (kind === 'clap') { let i, g = 0; do { i = Math.floor(Math.random() * L2_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind, i, answer: 'ok', choices: [], key: 'c' + i, uid }; }
  let i, g = 0; do { i = Math.floor(Math.random() * L2_PH.length); }""",
    """  if (kind === 'clap' || kind === 'clap2') { let i, g = 0; do { i = Math.floor(Math.random() * L2_CLAP.length); } while (prev && prev.i === i && g++ < 10); return { kind, i, answer: 'ok', choices: [], key: 'c' + i, uid }; }
  let i, g = 0; do { i = Math.floor(Math.random() * L2_PH.length); }""")
rep("""  else if (q.kind === 'clap') { title = t('Listen twice, clap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'); body = <L2ClapPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }""",
    """  else if (q.kind === 'clap') { title = t('Listen twice, clap it back, then say two or three.', '두 번 듣고, 따라 치고, 두 박인지 세 박인지 말해요.'); body = <L2ClapPad key={q.uid} fixed={q.i} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }
  else if (q.kind === 'clap2') { title = t('Listen twice, then clap it back.', '두 번 듣고, 따라 쳐요.'); body = <L2ClapPad key={q.uid} fixed={q.i} askMetre={false} onResult={(r) => pickIt(r.ok ? 'ok' : 'no')}/>; }""")
rep("""Object.assign(LISTEN_23_DRILL, { levels: L2_LEVELS, generate: genL2Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: l2AnswerLabel, Question: L2Question, Learn: L2Learn });""",
    """Object.assign(LISTEN_23_DRILL, { levels: L2_LEVELS, generate: genL2Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: l2AnswerLabel, Question: L2Question, Learn: L2Learn });
Object.assign(LISTEN_3_DRILL, { levels: L3_LEVELS, generate: genL2Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: l2AnswerLabel, Question: L2Question, Learn: L3Learn });   // Build CC""")

L2T = r'''function L2Teacher({ g = 2 }) {   // Build CC: a teacher copy per grade
  const ch = g === 3 ? 'listen-3' : 'listen-23', order = g === 3 ? ['any', 'deg', 'metre', 'clap', 'sing'] : ['dyad', 'clap', 'sing'];
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId={ch} teacher>{content}</WbPage>);
  const lt = (i) => lwLet(i) + (i >= 12 ? "'" : '');   // C' = the C above middle C
  const pair = ([a, b]) => lt(a) + ' + ' + lt(b) + ' (' + l2IvName(a, b) + ')';
  const deg = (k, n) => lt(k) + ' then ' + lt(k + L2_DEG.find(y => y[0] === n)[1]) + ': the ' + l2DegName(n);
  const phText = (ph) => { const out = []; for (let j = 0; j < ph.length; j++) { const [k, b] = ph[j];
    if (b === 0.5 && ph[j + 1] && ph[j + 1][1] === 0.5) { out.push(lt(k) + '-' + lt(ph[j + 1][0]) + ' run-ning'); j++; } else out.push(lt(k) + ' ' + (b === 2 ? 'hold' : 'walk')); } return out.join(' · '); };
  const B = {
    dyad: (no) => <TcBlock key="dyad" page={no} title="Two notes at once" answers={<>{tcAns('PLAY TOGETHER', L2_G2.map(pair))}</>}
      watch="Humming a note between the two, or the top note every time. Ask for the lower one as often as the higher."
      say="“Two at once: pick one out and hum it.”"/>,
    any: (no) => <TcBlock key="any" page={no} title="Any two notes" answers={<>{tcAns('PLAY TOGETHER', [[4, 5], [0, 2], [2, 11], [5, 11], [9, 12], [0, 9]].map(pair))}</>}
      watch="The close ones (2nds) heard as one note. Play the asked note alone, then the pair again."
      say="“Close or far: follow just one.”"/>,
    deg: (no) => <TcBlock key="deg" page={no} title="From the keynote" answers={<>{tcAns('PLAY', [[0, 3], [7, 5], [5, 2], [2, 4], [0, 5], [7, 3]].map(([k, n]) => deg(k, n)))}</>}
      watch="Naming by guess. Sing up from the keynote, 1 2 3 4 5, every time until it is quick."
      say="“Sing up from home until you meet it.”"/>,
    metre: (no) => <TcBlock key="metre" page={no} title="Two or three?" answers={<>{tcAns('PLAY', ['oom-pah: the low note on 1, the chord on 2 (two)', 'oom-pah-pah: the low note on 1, the chord on 2 and 3 (three)', 'then a rhythm with no accompaniment: count from each strong note'])}</>}
      watch="Counting every note instead of feeling where the strong one comes back. Sway or step on 1."
      say="“Oom-pah: two. Oom-pah-pah: three.”"/>,
    clap: (no) => <TcBlock key="clap" page={no} title={g === 3 ? 'Clap it back: two or three?' : 'Clap it back'} answers={<><div style={{fontSize:10.5,fontWeight:900,color:BK.muted,letterSpacing:'0.06em',marginBottom:4}}>{spTx((g === 3 ? 'PLAY TWICE, THEN THE CHILD CLAPS AND SAYS TWO OR THREE' : 'PLAY TWICE, THEN THE CHILD CLAPS') + ' (♩ = ' + L2_CLAP_BPM + ')')}</div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:'4px 14px'}}>{L2_CLAP.map((row, i) => <div key={i} style={{display:'flex',alignItems:'center',gap:6}}>{nvNum(i + 1)}<div style={{flex:1,minWidth:0}}>{rqStaffEl(row, { counts: false, hearts: false })}</div></div>)}</div></>}
      watch="The dotted crotchet clapped as two even notes. Long, short: the quaver comes late, just before the next beat."
      say={g === 3 ? '“Clap it back, then say two or three.”' : '“Listen twice, then clap: long, short.”'}/>,
    sing: (no) => <TcBlock key="sing" page={no} title="Sing a longer tune" answers={<>{tcAns('PLAY TWICE, THEN THE CHILD SINGS', L2_PH.map(phText))}</>}
      watch="The skips sung as steps, or the held note cut short. Sing the skip slowly once, then the whole tune."
      say="“Longer, with skips: the notes and the rhythm, both.”"/>,
  };
  const nw = ['', 'one', 'two', 'three', 'four', 'five'][order.length];
  const blocks = order.map((x, j) => B[x](j + 2)).concat([<TcBlock key="checks" page={order.length + 2} title={'My ' + nw + ' checks'} answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen, played twice: you play, the child {g === 3 ? 'hums, sings, names or claps' : 'hums, claps or sings'}. You only correct. Use material the child has not heard this week.</div>}/>]);
  const cutAt = g === 3 ? 3 : 2;
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName(ch)}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade {g} aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice, as the examiner does. Middle C is C here; the C above is C'.</div>
    {blocks.slice(0, cutAt)}
  </>);
  P(<>{blocks.slice(cutAt)}</>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-23'] = L2Teacher;
TEACHER_COPIES['listen-3'] = () => <L2Teacher g={3}/>;
'''
a = s.index("function L2Teacher() {"); b = s.index("TEACHER_COPIES['listen-23'] = L2Teacher;\n", a) + len("TEACHER_COPIES['listen-23'] = L2Teacher;\n")
s = s[:a] + L2T + s[b:]

# ── 7. the books ──
rep("""'listen-23': Listen23LessonBook,""", """'listen-23': Listen23LessonBook, 'listen-3': Listen3LessonBook, 'ear-prep': EarPrepLessonBook,""")
rep("""'listen-23': l2LbPages,""", """'listen-23': (s) => l2LbPages(s, 2), 'listen-3': (s) => l2LbPages(s, 3), 'ear-prep': epLbPages,""")

# ── 8. the Home: a group per ear room ──
rep("""    { id: 'au-ls', en: 'Listen and sing', ko: '듣고 노래하기', lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-find', 'ls-sing'], check: 'listen-sing' },
    { id: 'au-lw', en: 'Listen, clap, write', ko: '듣고, 치고, 적기', lessons: ['lw-home', 'lw-metre', 'lw-clap', 'lw-phrase', 'lw-write'], check: 'listen-write' },
    { id: 'au-23', en: 'Ear training, Grades 2–3', ko: '청음, Grade 2–3', lessons: ['l2-dyad', 'l2-any', 'l2-deg', 'l2-clap', 'l2-sing'], check: 'listen-23' },""",
    """    { id: 'au-ep', en: 'Ear prep', ko: '청음 준비', lessons: ['ep-hml', 'ep-rhythm', 'ep-tune', 'ep-shape', 'ls-find'], check: 'ear-prep' },   // Build CC
    { id: 'au-ls', en: 'Ear training, Prelim', ko: '청음, Prelim', lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-sing'], check: 'listen-sing' },
    { id: 'au-lw', en: 'Ear training, Grade 1', ko: '청음, Grade 1', lessons: ['lw-home', 'lw-clap', 'lw-phrase'], check: 'listen-write' },
    { id: 'au-23', en: 'Ear training, Grade 2', ko: '청음, Grade 2', lessons: ['l2-dyad', 'l2-clap2', 'l2-sing'], check: 'listen-23' },
    { id: 'au-3', en: 'Ear training, Grade 3', ko: '청음, Grade 3', lessons: ['l2-any', 'l2-deg', 'lw-metre', 'l2-clap', 'l3-sing'], check: 'listen-3' },   // Build CC""")
rep(""" get kicker() { return t('Aural', '청음') + ' · ' + t('Listen and sing', '듣고 노래하기'); }""", """ get kicker() { return t('Aural', '청음') + ' · ' + t('Ear training, Prelim', '청음, Prelim'); }""")
rep(""" get kicker() { return t('Aural', '청음') + ' · ' + t('Listen, clap, write', '듣고, 치고, 적기'); }""", """ get kicker() { return t('Aural', '청음') + ' · ' + t('Ear training, Grade 1', '청음, Grade 1'); }""")
rep(""" get kicker() { return t('Aural', '청음') + ' · ' + t('Ear training, Grades 2–3', '청음, Grade 2–3'); }""", """ get kicker() { return t('Aural', '청음') + ' · ' + t('Ear training, Grade 2', '청음, Grade 2'); }""")
rep("""lsAdd('ls-find', 4, 'Find your note', '내 음 찾기', 'Sing it, then find it: higher or lower?', '부르고, 찾아요: 더 높아? 더 낮아?', lsFindQ);
lsAdd('ls-sing', 5, """, """lsAdd('ls-sing', 4, """)
rep("""lwAdd('lw-metre', 2, 'Two or three?', '두 박? 세 박?', 'Oom-pah or oom-pah-pah.', '쿵-짝, 아니면 쿵-짝-짝.', lwMetreQ);
lwAdd('lw-clap', 3, """, """lwAdd('lw-clap', 2, """)
rep("""lwAdd('lw-phrase', 4, """, """lwAdd('lw-phrase', 3, """)
a = s.index("lwAdd('lw-write', 5, "); b = s.index("\n", a) + 1
s = s[:a] + s[b:]
rep("""l2Add('l2-any', 2, 'Any two notes',""", """l3Add('l2-any', 1, 'Any two notes',""")
rep("""l2Add('l2-deg', 3, 'From the keynote',""", """l3Add('l2-deg', 2, 'From the keynote',""")
rep("""l2Add('l2-clap', 4, 'Clap it back: two or three?',""", """l3Add('l2-clap', 4, 'Clap it back: two or three?',""")
rep("""l2Add('l2-sing', 5, 'Sing a longer tune', '더 긴 선율 따라 부르기', 'Longer, with skips: sing it, then play it.', '더 길고 건너뛰는 선율: 부르고 치기.', lwTapQ(L2SingPad, (n) => ({ fixed: n % L2_PH.length }), ['Listen twice, sing it back with its rhythm, then play it.', '두 번 듣고, 리듬까지 따라 부르고, 쳐요.'], ['Sung and played ✓', '부르고 쳤어요 ✓']));""",
    """l2Add('l2-sing', 3, 'Sing a longer tune', '더 긴 선율 따라 부르기', 'Longer, with skips: sing it, then play it.', '더 길고 건너뛰는 선율: 부르고 치기.', lwTapQ(L2SingPad, (n) => ({ fixed: n % L2_PH.length }), ['Listen twice, sing it back with its rhythm, then play it.', '두 번 듣고, 리듬까지 따라 부르고, 쳐요.'], ['Sung and played ✓', '부르고 쳤어요 ✓']));
l2Add('l2-clap2', 2, 'Clap it back', '따라 치기', 'Heard twice, then clapped back: long, short.', '두 번 듣고 따라 치기: 길게, 짧게.', lwTapQ((p) => <L2ClapPad askMetre={false} {...p}/>, (n) => ({ fixed: n % L2_CLAP.length }), ['Listen twice, then tap it back with the clicks.', '두 번 듣고, 클릭에 맞춰 따라 쳐요.'], ['Clapped back on time ✓', '제때 따라 쳤어요 ✓']));   // Build CC
l3Add('lw-metre', 3, 'Two or three?', '두 박? 세 박?', 'Oom-pah or oom-pah-pah.', '쿵-짝, 아니면 쿵-짝-짝.', lwMetreQ);   // Build CC: from the Grade 1 room
l3Add('l3-sing', 5, 'Sing a longer tune', '더 긴 선율 따라 부르기', 'Longer, with skips: sing it, then play it.', '더 길고 건너뛰는 선율: 부르고 치기.', lwTapQ(L2SingPad, (n) => ({ fixed: (n + 3) % L2_PH.length }), ['Listen twice, sing it back with its rhythm, then play it.', '두 번 듣고, 리듬까지 따라 부르고, 쳐요.'], ['Sung and played ✓', '부르고 쳤어요 ✓']));

// ══ Build CC: Ear Prep on the Home (the Aural door, before Ear training, Prelim): each game a heard question, as the room's ══
LBH_FN['ear-prep'] = (s) => epLbPages(s);
const epAdd = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('ear-prep', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Ear prep', '청음 준비'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const EP_PROMPT = { hml: ['Listen: low, in the middle, or high?', '들어 봐요: 낮은 음, 가운데 음, 높은 음?'], rhythm: ['Two rhythms: the same, or different?', '리듬 두 개: 같을까요, 다를까요?'], tune: ['Two tunes: the same, or different?', '선율 두 개: 같을까요, 다를까요?'], shape: ['Three notes: which way did they go?', '세 음: 어느 쪽으로 갔을까요?'] };
const epWhy = (q) => q.kind === 'hml' ? (q.answer === 'low' ? ['Low: down with the turtle.', '낮은 음: 거북이와 함께 아래.'] : q.answer === 'high' ? ['High: up with the bird.', '높은 음: 새와 함께 위.'] : ['In the middle, near Clara (middle C).', '가운데, 클라라(가운데 도) 근처.'])
  : q.kind === 'shape' ? ['It went ' + q.answer.split('').map(c => (c === 'u' ? 'up' : 'down')).join(', then ') + '.', q.answer.split('').map(c => (c === 'u' ? '위로' : '아래로')).join(', 그다음 ') + ' 갔어요.']
  : q.answer === 'same' ? [q.kind === 'rhythm' ? 'The same rhythm twice.' : 'The same tune twice.', q.kind === 'rhythm' ? '같은 리듬이 두 번.' : '같은 선율이 두 번.'] : [q.kind === 'rhythm' ? 'Different: listen for where the walks and run-nings change.' : 'Different: one note changed.', q.kind === 'rhythm' ? '달라요: 타와 티-티가 어디서 바뀌는지 들어 봐요.' : '달라요: 한 음이 바뀌었어요.'];
const epQ = (kind) => (n, prev) => { const q = genLsQuestion({ kind }, prev && prev.q), spb = 60 / 96;
  const play = () => { if (kind === 'hml') lsPlay(q.d, 1.2); else if (kind === 'shape') lsSeq(q.ds, 620);
    else if (kind === 'rhythm') { const ts = []; lsBar(q.a, 0, spb, ts); lsBar(q.b, 5 * spb * 1000, spb, ts); }
    else { lsSeq(q.a.map(f => hpFingerD('C', 'R', f)), 480); setTimeout(() => lsSeq(q.b.map(f => hpFingerD('C', 'R', f)), 480), 4 * 480 + 700); } };
  const label = (c) => () => <span style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4}}>{kind === 'hml' ? <>{c === 'low' ? turtleIcon(30) : c === 'high' ? birdIcon(30) : lsClara(24)}{LS_HML[c]()}</> : kind === 'shape' ? lsShapePic(c, 56) : LS_SAME[c]()}</span>;
  const why = epWhy(q);
  return { q, key: q.key, kind: 'choice', cols: kind === 'shape' ? 4 : kind === 'hml' ? 3 : 2, prompt: EP_PROMPT[kind], opts: q.choices.map(c => ({ id: c, label: label(c) })), ans: q.answer, ok: (v) => v === q.answer, play,
    fig: () => ({ mid: null }), yes: why, no: [why[0] + ' Listen again: ♪ Again.', why[1] + ' 다시 들어 봐요: ♪ 다시.'] }; };
epAdd('ep-hml', 1, 'Turtle, Clara or bird?', '거북이, 클라라, 새?', 'Low, middle or high: one note at a time.', '낮은, 가운데, 높은: 한 음씩.', epQ('hml'));
epAdd('ep-rhythm', 2, 'Same rhythm, or not?', '같은 리듬일까?', 'Two rhythms: listen to the end of both.', '리듬 두 개: 둘 다 끝까지 들어요.', epQ('rhythm'));
epAdd('ep-tune', 3, 'Same tune, or not?', '같은 선율일까?', 'Two tunes: did one note change?', '선율 두 개: 한 음이 바뀌었을까?', epQ('tune'));
epAdd('ep-shape', 4, 'Which way did it go?', '어느 쪽으로 갔을까?', 'Up to the bird, down to the turtle.', '위로는 새, 아래로는 거북이.', epQ('shape'));
epAdd('ls-find', 5, 'Find your note', '내 음 찾기', 'Sing it, then find it: higher or lower?', '부르고, 찾아요: 더 높아? 더 낮아?', lsFindQ);   // from the old Listen and Sing""")
rep("""const l2DegQ = (n, prev) => {""", """LBH_FN['listen-3'] = (s) => l2LbPages(s, 3);   // Build CC: Ear training, Grade 3
const l3Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-3', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Ear training, Grade 3', '청음, Grade 3'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l2DegQ = (n, prev) => {""")
rep("""LBH_FN['listen-23'] = (s) => l2LbPages(s);""", """LBH_FN['listen-23'] = (s) => l2LbPages(s, 2);""")

# the floor marks: Prelim and Grade 1 apart
rep("""  set('G', 'ls-beat ls-echo ls-updown ls-find ls-sing');   // Build X""", """  set('G', 'ep-hml ep-rhythm ep-tune ep-shape ls-find');   // Build CC: Ear Prep
  set('P1', 'ls-beat ls-echo ls-updown ls-sing');   // Build X; Build CC: Ear training, Prelim""")
rep("""  set('P1', 'lw-home lw-metre lw-clap lw-phrase lw-write');   // Build AE""", """  set('P1', 'lw-home lw-clap lw-phrase');   // Build AE""")
rep("""  set('4', 'spr-tune cpx-dances');   // Build AW: Grade 4 general knowledge in Stories of music (after the composers line, which would mark the dances Grades 2-3)
  return m;""", """  set('4', 'spr-tune cpx-dances');   // Build AW: Grade 4 general knowledge in Stories of music (after the composers line, which would mark the dances Grades 2-3)
  set('23', 'l2-clap2 lw-metre l3-sing');   // Build CC: Ear training, Grades 2 and 3
  // Build CC (her 09:38): Prelim and Grade 1 are a floor each; the Grade 1 floor's rooms are Ear training 1, Accidentals, Key
  // signatures, Terms, 6/8, Intervals, Chords and Form; everything else marked Prelim – Grade 1 is Prelim
  const g1 = new Set(('ac-natural ac-bar ac-play ac-cmp iv-count iv-staff kf-what kf-minor kf-write kf-trans ch-stack ch-staff ch-hands ch-mm ch-ear ch-tonic'
    + ' tmx-build tmx-map fmx-map fmx-phrase fmx-letters fmx-binary fmx-ternary fmx-find fmx-build e8-big e8-dot e8-ls e8-34 e8-read rm-68 lw-home lw-clap lw-phrase').split(' '));
  Object.keys(m).forEach(id => { if (m[id] === 'P1') m[id] = g1.has(id) ? '1' : 'P'; });
  return m;""")
rep("""const HOME_FLOOR_NAME = { G: 'Beginner', P1: 'Prelim – Grade 1', '23': 'Grades 2–3',""", """const HOME_FLOOR_NAME = { G: 'Beginner', P: 'Prelim', '1': 'Grade 1', '23': 'Grades 2–3',""")

# the house: a one-word name too long for a floor's narrow rooms (Accidentals on the Grade 1 floor) takes the size at which
# every word fits, rather than running into the next room
rep("""  if (z == null) { key = 'full'; z = 13.5; }   // a name too long for one line at any size: two lines, ticks kept""",
    """  if (z == null) { key = 'full'; z = [13.5, 12.5, 11.5, 10.5].find(z => rs.every(r => r.full.split(/\\s+/).every(wd => one(wd, r.w, z)))) || 10.5; }   // a name too long for one line at any size: two lines, ticks kept; Build CC: every word fits its room""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
