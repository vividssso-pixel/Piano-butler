import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
LS = open(os.path.join(here, 'lsx.jsx'), encoding='utf-8').read()
LSH = open(os.path.join(here, 'lsh.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build X (the decision board's build queue, item 1; her 25 Oct pick of room 6, 'Listen and sing'): chapter 6 on the Beginner
# floor, the first aural room. Its Lesson Book (7 pages) is its online lesson; its drill has six heard levels (no paper: every
# question is a sound). On the Home it opens a seventh door, Aural, with the chapter's five lessons and the ear lessons the
# other rooms already had. The chapter code: lsx.jsx; its Home lessons: lsh.jsx.
rep("""const HAND_POS_DRILL = { id: 'hand-positions', label: 'Hand Positions' };""",
    """const HAND_POS_DRILL = { id: 'hand-positions', label: 'Hand Positions' };
const LISTEN_DRILL = { id: 'listen-sing', label: 'Listen and Sing', noPrint: true };   // Build X: its lessons and questions with its Lesson Book (lsLbPages)""")
rep("""  { id: 'hand-positions', label: 'Hand Positions', concept: HAND_POS_DRILL, track: 'start' },   // Build T""",
    """  { id: 'hand-positions', label: 'Hand Positions', concept: HAND_POS_DRILL, track: 'start' },   // Build T
  { id: 'listen-sing', label: 'Listen and Sing', concept: LISTEN_DRILL, track: 'start' },   // Build X""")
rep("""'hand-positions': '손 자리', 'pulse': '박과 세기',""", """'hand-positions': '손 자리', 'listen-sing': '듣고 노래하기', 'pulse': '박과 세기',""")
rep("""'hand-positions': ['Hand positions', '손 자리'],""", """'hand-positions': ['Hand positions', '손 자리'], 'listen-sing': ['Listen & sing', '듣고 노래'],""")
rep("""const HOUSE_ICONS = {"hand-positions": """, """const HOUSE_ICONS = {"listen-sing": "<path d=\\"M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31\\"/><ellipse cx=\\"29\\" cy=\\"33\\" rx=\\"6\\" ry=\\"4.5\\" fill=\\"#e4572e\\" stroke=\\"none\\" transform=\\"rotate(-20 29 33)\\"/><path d=\\"M34.6 31.6V10Q40 12 42 18\\" stroke=\\"#e4572e\\"/>", "hand-positions": """)
rep("""  'hand-positions': 'hand position c position g position five finger thumb middle c both hands together mirror move',""",
    """  'hand-positions': 'hand position c position g position five finger thumb middle c both hands together mirror move',
  'listen-sing': 'listen sing aural ear training echo rhythm clap beat up down high low find note sing back pitch',""")
rep("""'hand-positions': ['note-names'],""", """'hand-positions': ['note-names'], 'listen-sing': ['pulse', 'hand-positions'],""")
rep("""
// ─── Chapter 2: Keyboard Patterns (Phase 387""", LS + """
// ─── Chapter 2: Keyboard Patterns (Phase 387""")
rep("""const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'hand-positions': HandPositionsLessonBook,""", """const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'hand-positions': HandPositionsLessonBook, 'listen-sing': ListenSingLessonBook,""")
rep("""const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'hand-positions': hpLbPages,""", """const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'hand-positions': hpLbPages, 'listen-sing': lsLbPages,""")
# the Home: a seventh door, Aural (the chapter's five lessons; then the ear lessons other rooms already had, in floor order)
rep("""  about: { lessons: [], groups: [   // Build W""", """  aural: { lessons: [], groups: [   // Build X: the Aural door
    { id: 'au-ls', en: 'Listen and sing', ko: '듣고 노래하기', lessons: ['ls-beat', 'ls-echo', 'ls-updown', 'ls-find', 'ls-sing'], check: 'listen-sing' },
    { id: 'au-more', en: 'More listening', ko: '더 듣기', lessons: ['hear-find', 'echo', 'touch-ear', 'ch-ear', 'iv-mh', 'iv-ear', 'csx-ear'] },
  ] },
  about: { lessons: [], groups: [   // Build W""")
rep("""  set('G', 'name-reveal step-updown letter-chain find-every ac-two');""", """  set('G', 'name-reveal step-updown letter-chain find-every ac-two');
  set('G', 'ls-beat ls-echo ls-updown ls-find ls-sing');   // Build X""")
rep("""const homeCatById = (id) => TOOL_CATS.find(c => c.id === id) || HOME_VIRTUAL.find(c => c.id === id) || HOME_STAFF.find(c => c.id === id);""",
    """const HOME_AURAL = { id: 'aural', area: 'aural', get name() { return t('Aural', '청음'); } };   // Build X: the Aural door (no Toolbox concept of its own)
const homeCatById = (id) => TOOL_CATS.find(c => c.id === id) || HOME_VIRTUAL.find(c => c.id === id) || HOME_STAFF.find(c => c.id === id) || (id === 'aural' ? HOME_AURAL : undefined);""")
rep("""        <button style={homeRow(false)} onClick={() => go({ ha: null, hc: 'about', hs: null })}>""", """        <button style={homeRow(false)} onClick={() => go({ ha: null, hc: 'aural', hs: null })}>
          <HomeAreaIcon id="aural"/>
          <span style={{flex:1,minWidth:0,display:'block'}}><span style={{...homeTitle,fontSize:24}}>{t('Aural', '청음')}</span><span style={homeSub}>{t('Listening, singing back, clapping back', '듣고, 따라 부르고, 따라 치기')}</span></span>
          <HomeChev on/>
        </button>
        <button style={homeRow(false)} onClick={() => go({ ha: null, hc: 'about', hs: null })}>""")
rep("""  if (id === 'about') return <svg {...p}>""", """  if (id === 'aural') return <svg {...p}><path d="M9 15C4 21 4 29 9 35M16 19C13 22 13 28 16 31"/><ellipse cx="29" cy="33" rx="6" ry="4.5" fill="#e4572e" stroke="#e4572e" transform="rotate(-20 29 33)"/><path d="M34.6 31.6V10Q40 12 42 18" stroke="#e4572e"/></svg>;   // Build X
  if (id === 'about') return <svg {...p}>""")
rep("""lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""", LSH + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers',""")
# Chapter 5's contents list was in English on the Korean page
rep("""{[['C position', 2], ['G position', 3], ['Move between them', 4], ['Hands together', 5], ['Taking turns', 6], ['Play: tunes in C and G', 7], ['My five checks', 8]].map(""",
    """{[[t('C position', 'C 자리'), 2], [t('G position', 'G 자리'), 3], [t('Move between them', '자리 옮기기'), 4], [t('Hands together', '양손 함께'), 5], [t('Taking turns', '번갈아 치기'), 6], [t('Play: tunes in C and G', '연주: C 자리·G 자리 곡'), 7], [t('My five checks', '나의 다섯 가지 확인'), 8]].map(""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
