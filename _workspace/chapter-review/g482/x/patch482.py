#!/usr/bin/env python3
# Phase 482 (her 2026-10-17 09:42 order: composers, styles, genres and periods together on one timeline; the macro-first
# plan; Book rules 14 and 15): the timeline of music (shared with chapter 27) and chapter 26, Composers through Time, built
# in full: the Lesson Book (page 1 the timeline; pages 2 to 5 the periods; page 6 who lived when), its screen lesson (the
# book with a pad on pages 1 to 6, "in order" at the end), a 9-level drill, the Workbook and the Teacher copy (both replace
# the Phase 304-305 ones).
#   mtl482.jsx:    the timeline (MusTimeline), its rows' data
#   cpbook482.jsx: the chapter's composers (CPX_PAGES), the who's who, the Lesson Book
#   cpapp482.jsx:  the pads, CpxLearn, the drill (Object.assign on COMPOSERS_DRILL)
#   cpwb482.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 481 (chapter 25; chapter 22's chxNbKo, chxBtn; Phases 304-305's CMP, CMP_PERIODS, CMP_HEAR).
import sys, re
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['mtl482.jsx', 'cpbook482.jsx', 'cpapp482.jsx', 'cpwb482.jsx'])
add += "Object.assign(COMPOSERS_DRILL, { levels: CPX_LEVELS, generate: genCpxQuestion, check: cpxCheck, answerLabel: cpxAnswerLabel, Question: CpxQuestion, Learn: CpxLearn });\n"

# 1. the new code before the Lesson Book registry; composers join the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS found %d' % s.count(a))
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("melody: MelodyLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", composers: ComposersLessonBook };") + s[j:]
rep("form: fmxLbPages, melody: mlxLbPages };", "form: fmxLbPages, melody: mlxLbPages, composers: cpxLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'era-worlds', ch: 'composers',", """  { id: 'cpx-map', ch: 'composers', title: 'The timeline of music', blurb: 'Five periods, their keyboards and their composers on one line: tap one to hear it.', C: () => <MtlMapPad/> },
  { id: 'cpx-baroque', ch: 'composers', title: 'Baroque composers', blurb: 'Vivaldi, Bach, Handel and Scarlatti: their lives, a piece each, and how they sound.', C: () => <CpxPeriodPad k={0}/> },
  { id: 'cpx-classical', ch: 'composers', title: 'Classical composers', blurb: 'Haydn, Clementi, Mozart and Beethoven: their lives, a piece each, and how they sound.', C: () => <CpxPeriodPad k={1}/> },
  { id: 'cpx-romantic', ch: 'composers', title: 'Romantic composers', blurb: 'Schubert, Chopin, the Schumanns, Liszt, Brahms and Tchaikovsky.', C: () => <CpxPeriodPad k={2}/> },
  { id: 'cpx-modern', ch: 'composers', title: 'Modern and Contemporary composers', blurb: 'Debussy to Hisaishi: 1900 to today.', C: () => <CpxPeriodPad k={3}/> },
  { id: 'cpx-alive', ch: 'composers', title: 'Who was alive?', blurb: 'Choose a year: the composers a line down from it crosses light up.', C: () => <CpxAlivePad/> },
  { id: 'cpx-order', ch: 'composers', title: 'In order of birth', blurb: 'Four composers: tap them in the order they were born.', C: () => <CpxOrderPad/> },
  { id: 'era-worlds', ch: 'composers',""")
rep("  'era-worlds': ['시대 속으로", """  'cpx-map': ['음악의 타임라인', '다섯 시대, 그 시대의 건반 악기와 작곡가를 한 줄에: 눌러서 들어요.'],
  'cpx-baroque': ['바로크 작곡가', '비발디, 바흐, 헨델, 스카를라티: 언제 살았는지, 곡 하나씩, 그리고 어떤 소리인지.'],
  'cpx-classical': ['고전주의 작곡가', '하이든, 클레멘티, 모차르트, 베토벤: 언제 살았는지, 곡 하나씩, 그리고 어떤 소리인지.'],
  'cpx-romantic': ['낭만주의 작곡가', '슈베르트, 쇼팽, 슈만 부부, 리스트, 브람스, 차이콥스키.'],
  'cpx-modern': ['근대와 현대 작곡가', '드뷔시부터 히사이시까지: 1900년부터 오늘날까지.'],
  'cpx-alive': ['누가 살아 있었을까?', '해를 골라요: 그해에서 내려온 선이 지나는 작곡가가 밝게 표시돼요.'],
  'cpx-order': ['태어난 차례대로', '네 명의 작곡가: 태어난 차례대로 눌러요.'],
  'era-worlds': ['시대 속으로""")
rep("'era-worlds': ['about', 0, 3, 'show'],", "'cpx-map': ['about', 0, 3, 'show ear'], 'cpx-baroque': ['about', 0, 3, 'show ear'], 'cpx-classical': ['about', 0, 3, 'show ear'], 'cpx-romantic': ['about', 0, 3, 'show ear'], 'cpx-modern': ['about', 0, 3, 'show ear'], 'cpx-alive': ['about', 0, 3, 'show'], 'cpx-order': ['about', 1, 3, 'game'], 'era-worlds': ['about', 0, 3, 'show'],")
rep("['mlx-map', 'tune-anatomy'],", "['mlx-map', 'tune-anatomy'], ['cpx-baroque', 'era-worlds'], ['cpx-classical', 'era-worlds'], ['cpx-romantic', 'era-worlds'], ['cpx-modern', 'era-worlds'], ['cpx-alive', 'composer-time-machine'],")
rep("  'composers': ['era-worlds', 'movement-map', 'composer-time-machine', 'composer-cards', 'who-am-i', 'name-that-tune'],",
    "  'composers': ['cpx-map', 'cpx-baroque', 'cpx-classical', 'cpx-romantic', 'cpx-modern', 'cpx-alive', 'cpx-order', 'era-worlds', 'movement-map', 'composer-time-machine', 'composer-cards', 'who-am-i', 'name-that-tune'],")
# 2a. two tools of this room get icons of their own: the timeline (bands over lives), in order (lives rising, numbered)
a = "  'composer-time-machine': () => ("
i = s.index(a); j = s.index("\n  ),\n", i) + len("\n  ),\n")
s = s[:j] + """  'cpx-map': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/>{[[2.5, 8.5], [9, 12.5], [13, 16.5], [17, 19], [19.5, 21.5]].map(([a, b]) => <rect key={a} x={a} y="4" width={b - a - 0.6} height="4.4" rx="0.8" fill="#fefbf3"/>)}<rect x="4" y="11" width="7" height="2.2" rx="1.1" fill="#fefbf3"/><rect x="8" y="14.5" width="8" height="2.2" rx="1.1" fill="#fefbf3"/><rect x="12" y="18" width="8" height="2.2" rx="1.1" fill="#e9a83a"/></svg>
  ),
  'cpx-order': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3f9a7e"/>{[[3, 17, '1'], [8.5, 13, '2'], [14, 9, '3']].map(([x, y, n]) => <g key={n}><rect x={x} y={y} width="7" height="2.4" rx="1.2" fill={n === '3' ? '#e9a83a' : '#fefbf3'}/><text x={x + 3.5} y={y - 1.4} textAnchor="middle" fontSize="5.6" fontWeight="900" fill="#fefbf3">{n}</text></g>)}</svg>
  ),
""" + s[j:]
# 3. the old lesson's ticks (Phases 304-305: keys 0 to 5) are not this lesson's steps (k1 to k7)
rep("|| id === 'form' || id === 'melody') && /^\\d+$/.test(String(k)); }", "|| id === 'form' || id === 'melody' || id === 'composers') && /^\\d+$/.test(String(k)); }")
# 4. search words; 'More in the toolbox' leaves this room's own pads out
m = re.search(r"  'composers': 'composer composers famous history era period [^']*'", s)
if not m: raise SystemExit('search words')
s = s[:m.end() - 1] + " harpsichord fortepiano keyboard counterpoint alberti rubato virtuoso contemporaries alive born died lifeline'" + s[m.end():]
rep("|chx|tmx|fmx|mlx|sac|ts|nv)-/.test(x)", "|chx|tmx|fmx|mlx|cpx|sac|ts|nv)-/.test(x)")
# 5. the rebuilt lesson's own count (6 steps); its extra last step (in order) is not counted
rep("const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6 };", "const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6, composers: 6 };")
rep("form: 'k7', melody: 'k7' };", "form: 'k7', melody: 'k7', composers: 'k7' };")
# 6. records saved before this drill's rebuild belong to its old levels
m = re.search(r"const REC_SINCE = \{ chords: \d+, terms: \d+, form: \d+, melody: \d+ \};", s)
if not m: raise SystemExit('REC_SINCE')
s = s[:m.end() - 3] + ", composers: REC_COMPOSERS };" + s[m.end():]
s = s.replace("REC_COMPOSERS", open(here + '/rec_composers.txt').read().strip())
# 7. the 2026 lesson and drill this room replaces (ComposersLearn, COMPOSERS_LEVELS, genComposersQuestion, ComposersQuestion):
# no longer reached. The older tools and their data (CMP, CMP_HEAR, EraWorlds, WhoAmI, ...) stay.
b = "  check: (q, ans) => ans === q.answer, answerLabel: (q) => q.answer, Question: ComposersQuestion, Learn: ComposersLearn,\n};\n"
i = s.index("function ComposersLearn({ onStart }) {\n"); j = s.index(b, i) + len(b)
s = s[:i] + "const COMPOSERS_DRILL = { id: 'composers', label: 'Composers through Time' };   // its levels, lesson and questions: Phase 482 (Object.assign below)\n" + s[j:]
for w in ['ComposersLearn', 'COMPOSERS_LEVELS', 'genComposersQuestion', 'ComposersQuestion', 'CMP_GENERIC']:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
rep("  { id: 'composers', label: 'Composers', concept: COMPOSERS_DRILL, track: 'about' },", "  { id: 'composers', label: 'Composers through Time', concept: COMPOSERS_DRILL, track: 'about' },")
rep("'styles': '스타일과 장르', 'composers': '작곡가',", "'styles': '스타일과 장르', 'composers': '시대와 작곡가',")
# 7a. what the 2026 room left unreachable: its paper pages, its Workbook and Teacher copy (and their data)
i = s.index("  if (id === 'composers') return [\n"); j = s.index("  ];\n", i) + 5; s = s[:i] + s[j:]
i = s.index("const CW_ERA_IDS = CMP_ERA_IDS;\n"); j = s.index("function ComposersTeacher() {", i); j = s.index("\n}\n", j) + 3
s = s[:i] + s[j:]
rep(" composers: ComposersWorkbook,", ""); rep(" composers: ComposersTeacher,", "")
for w in ['ComposersWorkbook', 'ComposersTeacher', 'cwWorkbook', 'cwConcepts', 'CwLifeChart', 'CW_PARTY', 'cwAlive']:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
# 8. helpers only the removed drill used
for w, line in [('cmpEraName', "const cmpEraName = (id) => cmpEra(id).name;\n"), ('cmpQuote', None)]:
    if line is None:
        i = s.index('const cmpQuote = '); j = s.index('\n', i) + 1; line = s[i:j]
    s = s.replace(line, '', 1)
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
