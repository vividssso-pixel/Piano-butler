#!/usr/bin/env python3
# Phase 483 (her 2026-10-17 09:42 order: composers, styles, genres and periods together on one timeline; the macro-first
# plan; Book rules 14 and 15): chapter 27, Styles & Genres, built in full on chapter 26's timeline of music: the Lesson
# Book (page 1 the timeline, its sound and styles rows its own; pages 2 to 6 texture, the sound of each period, folk,
# blues and jazz, pop), its screen lesson (the book with a pad on pages 1 to 6, a style ear test at the end), a 9-level
# drill, the Workbook and the Teacher copy (both replace the Phase 282/363 ones).
#   mtl483.jsx:    the timeline, as Phase 482 left it, with folk, names left out, and the chapter's own rows larger
#   csbook483.jsx: the chapter's data, its pictures, the Lesson Book
#   csapp483.jsx:  its sounds, the pads, CsxLearn, the drill (Object.assign on STYLES_DRILL)
#   cswb483.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 482 (chapter 26: MusTimeline, cpxStop and the sound owner, useCpxW, cpxChip, cpxKoT).
import sys, re
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
def at(a, start=0):   # an anchor found exactly once (r1: a doubled anchor would patch the wrong place silently)
    if s.count(a) != 1: raise SystemExit('anchor found %d: %s' % (s.count(a), a[:90]))
    return s.index(a, start)
# 0. the timeline: Phase 482's code replaced by its 483 version
i = at("// ─── Phase 482: the timeline of music (chapters 26 and 27 share it).")
j = at("// ─── Phase 482: chapter 26, Composers through Time:", i)
s = s[:i] + open(here + '/mtl483.jsx', encoding='utf-8').read() + '\n' + s[j:]
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['csbook483.jsx', 'csapp483.jsx', 'cswb483.jsx'])
add += "Object.assign(STYLES_DRILL, { levels: CSX_LEVELS, generate: genCsxQuestion, check: csxCheck, answerLabel: csxAnswerLabel, Question: CsxQuestion, Learn: CsxLearn });\n"

# 1. the new code before the Lesson Book registry; styles join the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS found %d' % s.count(a))
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("composers: ComposersLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", styles: StylesLessonBook };") + s[j:]
rep("melody: mlxLbPages, composers: cpxLbPages };", "melody: mlxLbPages, composers: cpxLbPages, styles: csxLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'texture-types', ch: 'styles',", """  { id: 'csx-map', ch: 'styles', title: 'The timeline, heard', blurb: 'The sound of each period and the styles beside them, on one line: tap one to hear it.', C: () => <CsxMapPad/> },
  { id: 'csx-texture', ch: 'styles', title: 'One tune, three textures', blurb: 'Monophony, homophony, polyphony: see them, hear them, then test your ear.', C: () => <CsxTexturePad/> },
  { id: 'csx-era', ch: 'styles', title: 'The sound of each period', blurb: 'Hear a piece from each period and what to listen for.', C: () => <CsxEraPad/> },
  { id: 'csx-penta', ch: 'styles', title: 'Five notes', blurb: 'The pentatonic scale on C or on the black keys: make up a folk tune.', C: () => <CsxPentaPad/> },
  { id: 'csx-blues', ch: 'styles', title: 'Blues and swing', blurb: 'The 12-bar blues swung, a missing chord to find, and straight against swing.', C: () => <CsxBluesPad/> },
  { id: 'csx-pop', ch: 'styles', title: 'A song', blurb: 'A song’s map (verse, chorus, bridge) and the four chords C G Am F.', C: () => <CsxPopPad/> },
  { id: 'csx-ear', ch: 'styles', title: 'Which style?', blurb: 'Hear a few bars: folk, classical, jazz and blues, or pop?', C: () => <CsxGenreEarPad/> },
  { id: 'texture-types', ch: 'styles',""")
rep("  'texture-types': ['텍스처: 목소리는 몇 개?',", """  'csx-map': ['소리로 듣는 타임라인', '시대마다 다른 소리와 그 곁의 스타일을 한 줄에: 눌러서 들어요.'],
  'csx-texture': ['한 선율, 세 가지 텍스처', '모노포니, 호모포니, 폴리포니: 보고, 듣고, 귀로 맞혀요.'],
  'csx-era': ['시대마다 다른 소리', '시대마다 곡 하나를 듣고, 찾아 들을 소리를 봐요.'],
  'csx-penta': ['다섯 음', 'C D E G A나 검은건반 다섯 개의 5음음계: 민요풍 선율을 지어 봐요.'],
  'csx-blues': ['블루스와 스윙', '스윙으로 듣는 12마디 블루스, 빠진 화음 찾기, 스트레이트와 스윙.'],
  'csx-pop': ['노래 한 곡', '노래의 지도(벌스, 후렴, 브리지)와 네 화음 C G Am F.'],
  'csx-ear': ['어떤 스타일일까요?', '몇 마디를 듣고 골라요: 민속 음악, 클래식, 재즈와 블루스, 대중음악.'],
  'texture-types': ['텍스처: 목소리는 몇 개?',""")
rep("'texture-types': ['about', 0, 2, 'show ear'],", "'csx-map': ['about', 0, 3, 'show ear'], 'csx-texture': ['about', 0, 3, 'show ear game'], 'csx-era': ['about', 0, 3, 'show ear'], 'csx-penta': ['about', 0, 3, 'show ear'], 'csx-blues': ['about', 1, 3, 'show ear game'], 'csx-pop': ['about', 0, 3, 'show ear'], 'csx-ear': ['about', 1, 3, 'game ear'], 'texture-types': ['about', 0, 2, 'show ear'],")
rep("['cpx-alive', 'composer-time-machine'],", "['cpx-alive', 'composer-time-machine'], ['csx-texture', 'texture-types'], ['csx-era', 'era-worlds'], ['csx-ear', 'texture-spotter'],")
rep("  'styles': ['texture-types', 'texture-spotter', 'genre-traits', 'swing-feel', 'twelve-bar-blues'],",
    "  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-pop', 'csx-ear', 'texture-types', 'texture-spotter', 'genre-traits', 'swing-feel', 'twelve-bar-blues'],")
# 2a. four tools of this room get icons of their own: the 12-bar grid, the timeline's sound (bands over a wave), five notes (keys), a song (blocks)
a = "  'texture-types': () => ("
i = at(a)
s = s[:i] + """  'csx-blues': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/>{Array.from({ length: 12 }, (_, i) => <rect key={i} x={3 + (i % 4) * 4.7} y={5 + Math.floor(i / 4) * 5} width="4" height="4" rx="0.8" fill={i === 8 ? '#e9a83a' : '#fefbf3'}/>)}</svg>
  ),
  'csx-map': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/>{[[2.5, 8.5], [9, 12.5], [13, 16.5], [17, 19], [19.5, 21.5]].map(([a, b]) => <rect key={a} x={a} y="4" width={b - a - 0.6} height="4.4" rx="0.8" fill="#fefbf3"/>)}<path d="M2.5 14 Q5 10.5 7.5 14 T12.5 14 T17.5 14 T21.5 14" fill="none" stroke="#fefbf3" strokeWidth="1.5"/><rect x="11" y="18" width="10.5" height="2.4" rx="1.2" fill="#e9a83a"/></svg>
  ),
  'csx-penta': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/>{[0, 1, 2, 3, 4, 5, 6].map(i => <rect key={i} x={3 + i * 2.6} y="5" width="2.4" height="14" fill={[0, 1, 2, 4, 5].includes(i) ? '#e9a83a' : '#fefbf3'}/>)}{[0, 1, 3, 4, 5].map(i => <rect key={'b' + i} x={4.6 + i * 2.6} y="5" width="1.5" height="8" fill="#26296b"/>)}</svg>
  ),
  'csx-pop': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/>{[0, 1, 2, 3, 4, 5].map(i => <rect key={i} x={2.5 + i * 3.3} y="8.5" width="2.8" height="7" rx="0.8" fill={i % 2 ? '#e9a83a' : '#fefbf3'}/>)}</svg>
  ),
""" + s[i:]
# 3. the old lesson's ticks (keys 0 to 6) are not this lesson's steps (k1 to k7)
rep("|| id === 'melody' || id === 'composers') && /^\\d+$/.test(String(k)); }", "|| id === 'melody' || id === 'composers' || id === 'styles') && /^\\d+$/.test(String(k)); }")
# 4. search words; 'More in the toolbox' leaves this room's own pads out
rep("  'styles': 'style genre texture monophony homophony polyphony solo melody folk classical jazz blues popular music swing straight eighth notes triplet 12-bar twelve bar blues chords I IV V',",
    "  'styles': 'style genre texture monophony homophony polyphony solo melody folk classical jazz blues popular music swing straight eighth notes triplet 12-bar twelve bar blues chords I IV V pentatonic five notes arirang ornament minimalism nationalism improvisation pop verse chorus bridge four chords',")
rep("|chx|tmx|fmx|mlx|cpx|sac|ts|nv)-/.test(x)", "|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv)-/.test(x)")
# 5. the rebuilt lesson's own count (6 steps); its extra last step (which style?) is not counted
rep("const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6, composers: 6 };", "const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6, composers: 6, styles: 6 };")
rep("melody: 'k7', composers: 'k7' };", "melody: 'k7', composers: 'k7', styles: 'k7' };")
# 6. records saved before this drill's rebuild belong to its old levels
m = re.search(r"const REC_SINCE = \{ chords: \d+, terms: \d+, form: \d+, melody: \d+, composers: \d+ \};", s)
if not m: raise SystemExit('REC_SINCE')
s = s[:m.end() - 3] + ", styles: REC_STYLES };" + s[m.end():]
s = s.replace("REC_STYLES", open(here + '/rec_styles.txt').read().strip())
# 7. the 2025 lesson and drill this room replaces (StylesLearn, STYLES_LEVELS, genStylesQuestion, StylesQuestion): no longer
# reached. The older tools and their data (TEXTURE_TYPES, GENRE_TRAITS, SwingFeel, TwelveBarBlues, BLUES_12, ...) stay.
b = "  Question: StylesQuestion, Learn: StylesLearn,\n};\n"
i = at("function StylesLearn({ onStart }) {\n"); j = at(b, i) + len(b)
s = s[:i] + "const STYLES_DRILL = { id: 'styles', label: 'Styles & Genres' };   // its levels, lesson and questions: Phase 483 (Object.assign below)\n" + s[j:]
for w in ['StylesLearn', 'STYLES_LEVELS', 'genStylesQuestion', 'StylesQuestion']:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
# 7a. what the 2025 room left unreachable: its paper pages, its Workbook and Teacher copy (and their data)
i = at("  if (id === 'styles') return [\n"); j = s.index("  ];\n", i) + 5; s = s[:i] + s[j:]
i = at("// ─── Book 4: Styles & Genres (chapter 'styles')"); j = at("// ─── Phase 363: workbooks + teacher copies for the last three chapters", i)
gone = re.findall(r'^(?:const|function) ([A-Za-z_][A-Za-z0-9_]*)', s[i:j], re.M)
s = s[:i] + s[j:]
rep(", styles: StylesWorkbook", ""); rep(", styles: StylesTeacher", "")
i = at("// Styles: a passport page for each era, and walking vs skipping for straight vs swing\n"); j = at("function TermsWorkbook({ startNo = 1 }) {", i)
gone2 = re.findall(r'^(?:const|function) ([A-Za-z_][A-Za-z0-9_]*)', s[i:j], re.M)
s = s[:i] + s[j:]
for w in gone2:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
for w in gone + ['StylesWorkbook', 'StylesTeacher']:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
# 8. (r1) every printed worksheet: the answer key stays on one page with its heading, and Korean answers break between words
rep("      <div style={{marginTop:30,paddingTop:14,borderTop:'2px solid #26296b'}}>\n        <div style={{fontSize:15,fontWeight:900,marginBottom:8}}>Answer key</div>\n        <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill, minmax(150px, 1fr))',gap:6,fontSize:13}}>",
    "      <div style={{marginTop:30,paddingTop:14,borderTop:'2px solid #26296b',breakInside:'avoid'}}>\n        <div style={{fontSize:15,fontWeight:900,marginBottom:8}}>Answer key</div>\n        <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill, minmax(150px, 1fr))',gap:6,fontSize:13,wordBreak:'keep-all',overflowWrap:'anywhere'}}>")
# 9. (r1) the room's older genre tool says folk music and 즉흥 연주 as this chapter does
rep("t('Folk music', '포크 (민속 음악)')", "t('Folk music', '민속 음악')")
rep("'즉흥연주와 스윙 리듬을 바탕으로 해요:", "'즉흥 연주와 스윙 리듬을 바탕으로 해요:")
rep("t('What makes each style different?', '각 스타일은 무엇이 다를까요')", "t('What makes each style different?', '스타일마다 무엇이 다를까요?')")
rep("  'genre-traits': ['스타일마다 무엇이 다를까?', '민요, 클래식, 재즈와 블루스, 대중음악: 각각의 특징.'],", "  'genre-traits': ['스타일마다 무엇이 다를까?', '민속 음악, 클래식, 재즈와 블루스, 대중음악: 각각의 특징.'],")
print('removed', len(gone) + len(gone2), 'helpers')
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
