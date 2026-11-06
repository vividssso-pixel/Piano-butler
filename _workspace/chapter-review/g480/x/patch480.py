#!/usr/bin/env python3
# Phase 480 (her 2026-10-17 09:42 order: terms, then form, then melody; the macro-first plan; Book rules 14 and 15):
# chapter 24, Musical Form, the last room of Level 4, built in full: the Lesson Book (page 1 the map of a piece), its
# screen lesson (the book with a pad on pages 1 to 6, a piece of the student's own at the end), a 9-level drill, the
# Workbook and the Teacher copy (both replace the Phase 117 ones).
#   fmbook480.jsx: the phrases (FMX_PH), FmxRow, the map (FmxMapSvg), the binary and ternary roads, the Lesson Book
#   fmapp480.jsx:  the pads, FmxLearn, the drill (Object.assign on FORM_DRILL)
#   fmwb480.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 479 (chapter 23; chapter 22's chxNbKo, chxBtn, chxStop, chxCircle; chapter 20's SgnRoad; chapter 10's SdyStaff).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['fmbook480.jsx', 'fmapp480.jsx', 'fmwb480.jsx'])
add += "Object.assign(FORM_DRILL, { levels: FMX_LEVELS, generate: genFmxQuestion, check: fmxCheck, answerLabel: fmxAnswerLabel, Question: FmxQuestion, Learn: FmxLearn });\n"

# 1. the new code before the Lesson Book registry; form joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS found %d' % s.count(a))
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("terms: TermsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", form: FormLessonBook };") + s[j:]
rep("chords: chxLbPages, terms: tmxLbPages };", "chords: chxLbPages, terms: tmxLbPages, form: fmxLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'form-shapes', ch: 'form',", """  { id: 'fmx-map', ch: 'form', title: 'The map of a piece', blurb: 'The piece, its sections, phrases, bars and beats: tap one to hear it.', C: () => <FmxMapPad/> },
  { id: 'fmx-phrase', ch: 'form', title: 'The phrase', blurb: 'Two phrases, each to its resting note.', C: () => <FmxPhrasePad/> },
  { id: 'fmx-letters', ch: 'form', title: 'Same or different', blurb: 'Give four phrases their letters: same music, same letter.', C: () => <FmxLetterPad/> },
  { id: 'fmx-binary', ch: 'form', title: 'Binary form', blurb: 'A and B, each played twice: hear the road.', C: () => <FmxRoadPad kind="bin"/> },
  { id: 'fmx-ternary', ch: 'form', title: 'Ternary form', blurb: 'A, B, then D.C. back to A.', C: () => <FmxRoadPad kind="ter"/> },
  { id: 'fmx-find', ch: 'form', title: 'Find the form', blurb: 'Hear each section, give the letters, name the form.', C: () => <FmxFindPad/> },
  { id: 'fmx-build', ch: 'form', title: 'Build a piece', blurb: 'A first, then A and B sections in any order: binary, ternary, or your own.', C: () => <FmxBuildPad/> },
  { id: 'form-shapes', ch: 'form',""")
rep("  'form-shapes': ['2부, 3부, 론도 형식',", """  'fmx-map': ['곡의 지도', '곡 전체, 부분, 프레이즈, 마디, 박: 눌러서 들어요.'],
  'fmx-phrase': ['프레이즈', '프레이즈 두 개를 쉬는 음까지 들어요.'],
  'fmx-letters': ['같은 음악, 새 음악', '네 프레이즈에 글자를 붙여요: 같은 음악은 같은 글자.'],
  'fmx-binary': ['2부 형식', 'A와 B를 두 번씩: 길을 따라 들어요.'],
  'fmx-ternary': ['3부 형식', 'A, B, 그다음 D.C.에서 A로 돌아가요.'],
  'fmx-find': ['형식 찾기', '부분을 하나씩 듣고 글자를 붙인 다음 형식 이름을 골라요.'],
  'fmx-build': ['곡 만들기', 'A로 시작해 A와 B 부분을 마음대로 놓아요: 2부 형식, 3부 형식, 또는 나만의 곡.'],
  'form-shapes': ['2부, 3부, 론도 형식',""")
rep("'form-shapes': ['melody', 0, 2, 'show'],", "'fmx-map': ['melody', 1, 3, 'show ear'], 'fmx-phrase': ['melody', 1, 2, 'show ear'], 'fmx-letters': ['melody', 1, 3, 'game ear'], 'fmx-binary': ['melody', 2, 3, 'show ear'], 'fmx-ternary': ['melody', 2, 3, 'show ear'], 'fmx-find': ['melody', 2, 3, 'game ear'], 'fmx-build': ['melody', 1, 3, 'show ear'], 'form-shapes': ['melody', 0, 2, 'show'],")
rep("['tmx-build', 'term-match'],", "['tmx-build', 'term-match'], ['fmx-map', 'form-shapes'], ['fmx-phrase', 'form-shapes'], ['fmx-letters', 'same-or-new'], ['fmx-binary', 'binary-ternary-spot'], ['fmx-ternary', 'binary-ternary-spot'], ['fmx-find', 'binary-ternary-spot'], ['fmx-build', 'binary-ternary-spot'],")
rep("  'form': ['form-shapes', 'form-builder', 'same-or-new', 'rondo-refrain', 'binary-ternary-spot'],",
    "  'form': ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'form-shapes', 'form-builder', 'same-or-new', 'rondo-refrain', 'binary-ternary-spot'],")
# 3. the old lesson's ticks (Phase 117: 6 steps, keys 0 to 5) are not this lesson's steps (k1 to k7)
rep("|| id === 'chords' || id === 'terms') && /^\\d+$/.test(String(k)); }", "|| id === 'chords' || id === 'terms' || id === 'form') && /^\\d+$/.test(String(k)); }")
# 4. search words; 'More in the toolbox' leaves this room's own pads out; its grades
rep("  'form': 'form binary ternary rondo ABA AB ABACA section refrain episode structure same new repeat',",
    "  'form': 'form binary ternary rondo ABA AB AABB ABACA section phrase phrase mark resting note bar beat map repetition contrast letters refrain episode structure same different new repeat D.C. al Fine',")
rep("|chx|tmx|sac|ts|nv)-/.test(x)", "|chx|tmx|fmx|sac|ts|nv)-/.test(x)")
rep("'form': 'Prelim–G3',", "'form': 'G1–G3',")
# 5. the rebuilt lesson's own count (6 steps); its extra last step (my piece) is not counted
rep("const STEPS_TOTAL_NOW = { chords: 6, terms: 6 };", "const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6 };")
rep("chords: 'k7', terms: 'k7' };", "chords: 'k7', terms: 'k7', form: 'k7' };")
# 6. shared (chapter 20's road): a bar may end with a plain double bar line (dbl), the end of a section with no sign
rep("const sgnDbl = (bars, i, skip) => i < bars.length - 1 && ((bars[i].fine && !skip.has('fine')) || (bars[i + 1] && bars[i + 1].coda));",
    "const sgnDbl = (bars, i, skip) => i < bars.length - 1 && ((bars[i].fine && !skip.has('fine')) || bars[i].dbl || (bars[i + 1] && bars[i + 1].coda));")
# 7. shared (chapter 10's staves): a long phrase mark under the notes clears every note inside it, not only at its middle
a = "      if (!inside && apex > yTop && apex < yBot + 2 && lines.some(L => Math.abs(L - apex) < 1.6)) apex += 2.2;"
rep(a, "      if (!inside && !tie && b - a > 1) span.slice(1, -1).forEach(n => { const tt = (n.x - A.x) / (B.x - A.x); if (tt <= 0.02 || tt >= 0.98) return;\n"
       "        const r = (dotY(n) != null ? Math.max(n.y + 8.5, dotY(n) + 5) : n.y + 8.5) + 1.2, need = (r - (1 - tt) * (1 - tt) * y1 - tt * tt * y2 + tt * (1 - tt) * (y1 + y2)) / (4 * tt * (1 - tt));\n"
       "        if (need > apex) apex = need; });\n" + a)
# 7b. Korean shown in this room: 튠 and 프레이즈 마크 are this chapter's 선율 and 프레이즈 표시
rep("'처음 튠이 끝에 다시 나오는지 들어 봐요.'", "'처음 선율이 끝에 다시 나오는지 들어 봐요.'")
rep("'튠이란, 프레이즈 마크, 묻고 답하기, 시퀀스; 2부·3부·론도 형식'", "'선율이란, 프레이즈 표시, 묻고 답하기, 시퀀스; 2부·3부·론도 형식'")
# 8. records: a rebuilt drill's levels are new, so records saved before its rebuild are not theirs (chapters 22 and 23 too)
rep("function getRecord(drillId, level, mode) { return loadRecords()[recordKey(drillId, level, mode)] || null; }",
    "// a rebuilt drill's levels are new: a record saved before the rebuild (ms) belongs to the old levels, so it is not shown\n"
    "const REC_SINCE = { chords: 1792186864000, terms: 1792197545000, form: 1792201375000 };\n"
    "function getRecord(drillId, level, mode) { const r = loadRecords()[recordKey(drillId, level, mode)] || null; return r && REC_SINCE[drillId] && !(+r.lastAt >= REC_SINCE[drillId]) ? null : r; }")
# 9. the 2025 lesson and drill this room replaces (FormLearn, SongForms, FORM_LEVELS, SHAPE_FACTS, genFormQuestion,
# FormQuestion): no longer reached. The older tools' helpers stay (FORM_COLOR, playFormSeq, SON_PAIRS, RONDO_SEQUENCE,
# genBTExample, SONG_SHAPES).
i = s.index("function SongForms() {\n"); j = s.index("// Four chords in C major.", i); s = s[:i] + s[j:]
b = "  Question: FormQuestion, Learn: FormLearn,\n};\n"
i = s.index("function FormLearn({ onStart }) {\n"); j = s.index(b, i) + len(b)
s = s[:i] + "const FORM_DRILL = { id: 'form', label: 'Musical Form' };   // its levels, lesson and questions: Phase 480 (Object.assign below)\n" + s[j:]
for w in ['SongForms', 'FormLearn', 'FORM_LEVELS', 'SHAPE_FACTS', 'genFormQuestion(', 'FormQuestion']:
    import re
    if re.search(r'\b' + re.escape(w) + (r'\b' if w[-1] != '(' else ''), s): raise SystemExit('still used: ' + w)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
