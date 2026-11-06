#!/usr/bin/env python3
# Phase 479 (her 2026-10-17 09:42: '음악 용어 먼저 만들어주고 그다음 음악 형식 선율과 프레이즈 이 순서로 가자'; the macro-first
# plan; Book rules 14 and 15): chapter 23, Musical Terms, the fifth room of Level 4, built in full: the Lesson Book (page 1
# the expression ladder), its screen lesson (the book with a pad on pages 1 to 6, the ladder again at the end with the
# words the student knows ticked), a 9-level drill, the Workbook and the Teacher copy (both replace the Phase 117 ones).
# The map's order changes with it: Level 4 ends with terms and form; Level 5 is melody, composers, styles, more scales.
#   tmbook479.jsx: the words (TMX), the ladders (speed, volume, beats), the Lesson Book
#   tmapp479.jsx:  the pads, TmxLearn, the drill (Object.assign on TERMS_DRILL)
#   tmwb479.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 478 (chapter 22's chxNbKo, chxMsg, chxBtn, chxStop; chapter 10's SdyStaff; chapter 13's StmMark).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['tmbook479.jsx', 'tmapp479.jsx', 'tmwb479.jsx'])
add += "Object.assign(TERMS_DRILL, { levels: TMX_LEVELS, generate: genTmxQuestion, check: tmxCheck, answerLabel: tmxAnswerLabel, Question: TmxQuestion, Learn: TmxLearn });\n"

# 1. the new code before the Lesson Book registry; terms joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS found %d' % s.count(a))
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("chords: ChordsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", terms: TermsLessonBook };") + s[j:]
rep("intervals: ivxLbPages, chords: chxLbPages };", "intervals: ivxLbPages, chords: chxLbPages, terms: tmxLbPages };")

# 2. the map: Level 4 ends with terms and form; Level 5 is melody, the composers and the styles (her order, 2026-10-17)
rep("""  { ids: ['key-signatures', 'signs', 'intervals', 'chords', 'composers', 'melody'], en: ['Level 4', 'Key signatures, signs, intervals and chords, the composers, and how a tune is shaped.'], ko: ['4층', '조표, 기호, 음정과 화음, 작곡가, 그리고 선율의 모양.'] },
  { ids: ['form', 'terms', 'styles', 'more-scales'], en: ['Level 5', 'How pieces are built, the Italian terms, and the styles of music.'], ko: ['5층', '곡의 짜임, 이탈리아어 용어, 그리고 음악의 스타일.'] },""",
    """  { ids: ['key-signatures', 'signs', 'intervals', 'chords', 'terms', 'form'], en: ['Level 4', 'Key signatures, signs, intervals and chords, the words for how to play, and how a piece is built.'], ko: ['4층', '조표, 기호, 음정과 화음, 음악 용어, 그리고 곡의 짜임.'] },
  { ids: ['melody', 'composers', 'styles', 'more-scales'], en: ['Level 5', 'How a tune is shaped, music through time, and more scales.'], ko: ['5층', '선율의 모양, 시대별 음악, 그리고 더 많은 음계.'] },""")
# form now comes before melody: it builds on the signs (repeats) and the first tunes
rep("form: ['melody', 'signs'], terms: ['dynamics', 'tempo'],", "form: ['signs', 'reading-steps'], terms: ['dynamics', 'tempo'],")

# 3. the toolbox: this room's pads first, then its older tools
rep("  { id: 'term-match', ch: 'terms',", """  { id: 'tmx-map', ch: 'terms', title: 'The expression ladder', blurb: 'Every word for how to play, by family: tap one to hear it and read it.', C: () => <TmxMapPad/> },
  { id: 'tmx-speed', ch: 'terms', title: 'The speed ladder', blurb: 'Largo to Prestissimo: tap a rung, hear its speed.', C: () => <TmxSpeedPad/> },
  { id: 'tmx-change', ch: 'terms', title: 'Changing speed', blurb: 'accel., rall., rit., riten. and a tempo, as beats you can hear.', C: () => <TmxChangePad/> },
  { id: 'tmx-vol', ch: 'terms', title: 'Loud and soft', blurb: 'pp to ff one rung at a time, the hairpins and sf.', C: () => <TmxVolPad/> },
  { id: 'tmx-touch', ch: 'terms', title: 'Touch and character', blurb: 'Legato, staccato, mezzo staccato, and five character words.', C: () => <TmxTouchPad/> },
  { id: 'tmx-build', ch: 'terms', title: 'Little words', blurb: 'poco, molto, sempre, senza, più, meno, con: how they change a term.', C: () => <TmxBuildPad/> },
  { id: 'term-match', ch: 'terms',""")
rep("  'term-match': ['용어 짝 맞추기',", """  'tmx-map': ['표현의 사다리', '어떻게 칠지 알려 주는 말을 종류별로 모았어요. 누르면 소리를 듣고 뜻을 읽어요.'],
  'tmx-speed': ['빠르기 사다리', '라르고부터 프레스티시모까지: 칸을 누르면 그 빠르기가 들려요.'],
  'tmx-change': ['빠르기 변화', '아첼레란도, 랄렌탄도, 리타르단도, 리테누토, 아 템포를 박으로 들어요.'],
  'tmx-vol': ['셈여림', 'pp부터 ff까지 한 칸씩, 헤어핀과 sf.'],
  'tmx-touch': ['터치와 느낌', '레가토, 스타카토, 메조 스타카토, 그리고 느낌을 나타내는 말 다섯 개.'],
  'tmx-build': ['꾸며 주는 말', '포코, 몰토, 셈프레, 센차, 피우, 메노, 콘을 붙이면 뜻이 어떻게 바뀌는지 들어 봐요.'],
  'term-match': ['용어 짝 맞추기',""")
rep("'term-cards': ['words', 1, 3, 'home show'],", "'tmx-map': ['words', 1, 3, 'show ear'], 'tmx-speed': ['words', 1, 2, 'show ear'], 'tmx-change': ['words', 1, 2, 'show ear'], 'tmx-vol': ['words', 1, 2, 'show ear'], 'tmx-touch': ['words', 1, 2, 'show ear'], 'tmx-build': ['words', 2, 3, 'show ear'], 'term-cards': ['words', 1, 3, 'home show'],")
rep("['chx-hands', 'primary-triads'],", "['chx-hands', 'primary-triads'], ['tmx-map', 'term-cards'], ['tmx-speed', 'tempo-race'], ['tmx-change', 'tempo-race'], ['tmx-vol', 'dyn-order'], ['tmx-touch', 'touch-lengths'], ['tmx-build', 'term-match'],")
rep("  'terms': ['term-sort', 'term-cards', 'term-mixer', 'term-match'],",
    "  'terms': ['tmx-map', 'tmx-speed', 'tmx-change', 'tmx-vol', 'tmx-touch', 'tmx-build', 'term-sort', 'term-cards', 'term-mixer', 'term-match'],")
# 4. the old lesson's ticks (Phase 117: 7 steps, keys 0 to 6) are not this lesson's steps (k1 to k7)
rep("function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs' || id === 'intervals' || id === 'chords') && /^\\d+$/.test(String(k)); }",
    "function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs' || id === 'intervals' || id === 'chords' || id === 'terms') && /^\\d+$/.test(String(k)); }")
# 5. search words; 'More in the toolbox' leaves this room's own pads out
rep("  'terms': 'italian term tempo word meaning',",
    "  'terms': 'italian term tempo word meaning speed largo lento adagio andante moderato allegretto allegro vivace presto prestissimo accelerando rallentando ritardando ritenuto a tempo dynamics crescendo sforzando legato staccato mezzo staccato sostenuto cantabile leggiero maestoso espressivo molto poco sempre senza piu meno con moto mosso expression ladder',")
rep("!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|sac|ts|nv)-/.test(x)", "!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|sac|ts|nv)-/.test(x)")
# 6. the rebuilt lesson's own count (6 steps), never the old synced 7; its extra last step (the ladder again) is not counted
rep("const STEPS_TOTAL_NOW = { chords: 6 };", "const STEPS_TOTAL_NOW = { chords: 6, terms: 6 };")
rep("const STEP_EXTRA = { scales: '6', 'key-signatures': 'k7', intervals: 'k7', chords: 'k7' };", "const STEP_EXTRA = { scales: '6', 'key-signatures': 'k7', intervals: 'k7', chords: 'k7', terms: 'k7' };")
# 7. the chapter's grades now (Preliminary to Grade 2)
rep("signs: 'G1–G2', terms: 'G1–G4',", "signs: 'G1–G2', terms: 'Prelim–G2',")
# 8. a tempo heard as it reads: the first speed, held back, then the first speed again (h.back)
rep("const bpm = h.bpm || (h.rubato ? 100 * (1 + 0.35 * Math.sin(i * 1.3)) : h.sudden ? (i < N / 2 ? h.from : h.to) : h.from + (h.to - h.from) * u) || 100;",
    "const bpm = h.bpm || (h.rubato ? 100 * (1 + 0.35 * Math.sin(i * 1.3)) : h.back ? (i >= N / 3 && i < 2 * N / 3 ? h.to : h.from) : h.sudden ? (i < N / 2 ? h.from : h.to) : h.from + (h.to - h.from) * u) || 100;")
rep("['A tempo', '', 'return to former speed', 'Changing speed', 1, { from: 70, to: 140, sudden: true }],",
    "['A tempo', '', 'return to former speed', 'Changing speed', 1, { from: 120, to: 72, back: true }],")   # the toolbox's Term cards and Term match too
# 9. chapter 10's staff marks: a slur over notes that also have staccato dots (mezzo staccato) goes clear of the dots
#    (chapter 10 never puts both on one note, so its pages do not change)
rep("      const end = (n) => { const y = n.y + 8.5 + (n.end === n.y ? 1.5 : 0); if (y < yTop - 2 || y > yBot + 2.5) return y;",
    "      const dotY = (n) => { const d = dots.find(q => Math.abs(q.x - n.x) < 0.5 && q.y > n.y); return d ? d.y : null; };\n      const end = (n) => { const dy = dotY(n); if (dy != null) return dy + 5.5; const y = n.y + 8.5 + (n.end === n.y ? 1.5 : 0); if (y < yTop - 2 || y > yBot + 2.5) return y;")
rep("let apex = inside ? A.y + 7.9 : Math.max(y1, y2, ...span.slice(1, -1).map(n => n.y + 8.5)) + (tie ? 4.5 : Math.min(9, 3 + 1.5 * (b - a)));",
    "let apex = inside ? A.y + 7.9 : Math.max(y1, y2, ...span.slice(1, -1).map(n => dotY(n) != null ? Math.max(n.y + 8.5, dotY(n) + 5) : n.y + 8.5)) + (tie ? 4.5 : Math.min(9, 3 + 1.5 * (b - a)));")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
