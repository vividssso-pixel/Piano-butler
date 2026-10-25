import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
LW = open(os.path.join(here, 'lwx.jsx'), encoding='utf-8').read()
LWH = open(os.path.join(here, 'lwh.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AE (the syllabus check's 'Ears for Grade 1'): Listen, Clap, Write, the second aural room, at the end of the second
# Prelim - Grade 1 floor. The Grade 1 aural tests (the tonic after an unfinished phrase; a passage in two or three, played twice,
# clapped back; a phrase with its rhythm, sung back) and the theory's listening (two or three beats; two bars of crotchets and
# minims written down). On the Home it joins the Aural door after Listen and sing.
rep("""const SIX_EIGHT_DRILL = { id: 'six-eight', label: '6/8 Time' };""",
    """const SIX_EIGHT_DRILL = { id: 'six-eight', label: '6/8 Time' };
const LISTEN_WRITE_DRILL = { id: 'listen-write', label: 'Listen, Clap, Write', noPrint: true };   // Build AE: its lessons and questions with its Lesson Book (lwLbPages)""")
rep("""  { id: 'form', label: 'Musical Form', concept: FORM_DRILL, track: 'reading' },""",
    """  { id: 'form', label: 'Musical Form', concept: FORM_DRILL, track: 'reading' },
  { id: 'listen-write', label: 'Listen, Clap, Write', concept: LISTEN_WRITE_DRILL, track: 'start' },   // Build AE""")
rep("""'listen-sing': '듣고 노래하기', """, """'listen-sing': '듣고 노래하기', 'listen-write': '듣고, 치고, 적기', """)
rep("""'listen-sing': ['Listen & sing', '듣고 노래'],""", """'listen-sing': ['Listen & sing', '듣고 노래'], 'listen-write': ['Listen & write', '듣고 적기'],""")
rep("""const HOUSE_ICONS = {"six-eight": """, """const HOUSE_ICONS = {"listen-write": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><path d=\\"M24 36 L40 14 L45 18 L29 40 Z\\" stroke=\\"#e4572e\\"/><path d=\\"M24 36 L22 43 L29 40\\" stroke=\\"#e4572e\\"/>", "six-eight": """)
rep("""'listen-sing': 'listen sing aural ear training echo rhythm clap beat up down high low find note sing back pitch',""",
    """'listen-sing': 'listen sing aural ear training echo rhythm clap beat up down high low find note sing back pitch',
  'listen-write': 'aural ear grade 1 tonic home note unfinished phrase duple triple two three beats clap back sing phrase rhythm dictation write rhythm contour shape',""")
rep("""'listen-sing': ['pulse', 'hand-positions'],""", """'listen-sing': ['pulse', 'hand-positions'], 'listen-write': ['listen-sing', 'time-signatures'],""")
rep("""{ ids: ['key-signatures', 'minor-scales', 'signs', 'intervals', 'chords', 'terms', 'form'], en: ['Prelim – Grade 1', 'Key signatures and minor scales, signs, intervals and chords, the words for how to play, and how a piece is built.'], ko: ['Prelim – Grade 1', '조표와 단음계, 기호, 음정과 화음, 음악 용어, 그리고 곡의 짜임.'] }""",
    """{ ids: ['key-signatures', 'minor-scales', 'signs', 'intervals', 'chords', 'terms', 'form', 'listen-write'], en: ['Prelim – Grade 1', 'Key signatures and minor scales, signs, intervals and chords, the words for how to play, how a piece is built, and listening a step further.'], ko: ['Prelim – Grade 1', '조표와 단음계, 기호, 음정과 화음, 음악 용어, 곡의 짜임, 그리고 한 걸음 더 듣기.'] }""")
rep("""const thArea = (id) => { if (id === 'listen-sing') return 'aural';""", """const thArea = (id) => { if (id === 'listen-sing' || id === 'listen-write') return 'aural';""")
rep("""
// ─── Chapter 2: Keyboard Patterns (Phase 387""", LW + """
// ─── Chapter 2: Keyboard Patterns (Phase 387""")
rep("""'listen-sing': ListenSingLessonBook,""", """'listen-sing': ListenSingLessonBook, 'listen-write': ListenWriteLessonBook,""")
rep("""'listen-sing': lsLbPages,""", """'listen-sing': lsLbPages, 'listen-write': lwLbPages,""")
rep("""    { id: 'au-ls', en: 'Listen and sing', ko: '듣고 노래하기', lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-find', 'ls-sing'], check: 'listen-sing' },""",
    """    { id: 'au-ls', en: 'Listen and sing', ko: '듣고 노래하기', lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-find', 'ls-sing'], check: 'listen-sing' },
    { id: 'au-lw', en: 'Listen, clap, write', ko: '듣고, 치고, 적기', lessons: ['lw-home', 'lw-metre', 'lw-clap', 'lw-phrase', 'lw-write'], check: 'listen-write' },   // Build AE""")
rep("""  set('P1', 'e8-big e8-dot e8-ls e8-34 e8-read');   // Build AD""", """  set('P1', 'e8-big e8-dot e8-ls e8-34 e8-read');   // Build AD
  set('P1', 'lw-home lw-metre lw-clap lw-phrase lw-write');   // Build AE""")
rep("""lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""", LWH + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
