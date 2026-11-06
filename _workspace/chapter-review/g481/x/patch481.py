#!/usr/bin/env python3
# Phase 481 (her 2026-10-17 09:42 order: terms, then form, then melody; the macro-first plan; Book rules 14 and 15):
# chapter 25, Melody & Phrasing, the first room of Level 5, built in full: the Lesson Book (page 1 the map of a tune),
# its screen lesson (the book with a pad on pages 1 to 6, a tune of the student's own at the end), a 9-level drill, the
# Workbook and the Teacher copy (both replace the Phase 117 ones).
#   mlbook481.jsx: the tune (MLX_TUNE), MlxRow, the map (MlxMapSvg), the Lesson Book
#   mlapp481.jsx:  the pads, MlxLearn, the drill (Object.assign on MELODY_DRILL)
#   mlwb481.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 480 (chapter 24; chapter 22's chxNbKo, chxBtn; chapter 10's SdyStaff; chapter 9's sskHz).
import sys, re
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['mlbook481.jsx', 'mlapp481.jsx', 'mlwb481.jsx'])
add += "Object.assign(MELODY_DRILL, { levels: MLX_LEVELS, generate: genMlxQuestion, check: mlxCheck, answerLabel: mlxAnswerLabel, Question: MlxQuestion, Learn: MlxLearn });\n"

# 1. the new code before the Lesson Book registry; melody joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS found %d' % s.count(a))
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("form: FormLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", melody: MelodyLessonBook };") + s[j:]
rep("terms: tmxLbPages, form: fmxLbPages };", "terms: tmxLbPages, form: fmxLbPages, melody: mlxLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'tune-anatomy', ch: 'melody',", """  { id: 'mlx-map', ch: 'melody', title: 'The map of a tune', blurb: 'The tune, its question and answer, its motif and notes: tap one to hear it.', C: () => <MlxMapPad/> },
  { id: 'mlx-line', ch: 'melody', title: 'Which line?', blurb: 'Hear a tune; choose the line it makes.', C: () => <MlxLinePad/> },
  { id: 'mlx-phrasing', ch: 'melody', title: 'Phrasing', blurb: 'One phrase, played flat or shaped.', C: () => <MlxPhrasingPad/> },
  { id: 'mlx-qa', ch: 'melody', title: 'Question and answer', blurb: 'Change the last note: which one makes an answer?', C: () => <MlxQaPad/> },
  { id: 'mlx-motif', ch: 'melody', title: 'Find the motif', blurb: 'Mark every bar where the motif comes back.', C: () => <MlxMotifPad/> },
  { id: 'mlx-seq', ch: 'melody', title: 'Repetition and sequence', blurb: 'Add bars: the motif again, a step up or a step down.', C: () => <MlxSeqPad/> },
  { id: 'mlx-build', ch: 'melody', title: 'My tune', blurb: 'A motif, two bars from it, a last note: it ends like a question or like an answer.', C: () => <MlxBuildPad/> },
  { id: 'tune-anatomy', ch: 'melody',""")
rep("  'tune-anatomy': ['리듬 + 음높이 = 선율',", """  'mlx-map': ['선율의 지도', '선율 전체, 질문과 대답, 동기, 음: 눌러서 들어요.'],
  'mlx-line': ['어느 선율선일까요?', '선율을 듣고 그 선율선을 골라요.'],
  'mlx-phrasing': ['프레이징', '프레이즈 하나를 같은 세기로, 또 모양을 살려서 들어요.'],
  'mlx-qa': ['질문과 대답', '마지막 음을 바꿔 봐요: 어느 음이 대답을 만들까요?'],
  'mlx-motif': ['동기 찾기', '동기가 다시 나오는 마디를 모두 찾아요.'],
  'mlx-seq': ['반복과 동형 진행', '마디를 더해요: 동기 그대로, 한 걸음 위로, 한 걸음 아래로.'],
  'mlx-build': ['나의 선율', '동기, 동기로 만든 두 마디, 마지막 음: 질문처럼, 또는 대답처럼 끝나요.'],
  'tune-anatomy': ['리듬 + 음높이 = 선율',""")
rep("'tune-anatomy': ['melody', 0, 1, 'show'],", "'mlx-map': ['melody', 1, 3, 'show ear'], 'mlx-line': ['melody', 1, 3, 'game ear'], 'mlx-phrasing': ['melody', 1, 3, 'show ear'], 'mlx-qa': ['melody', 1, 3, 'show ear'], 'mlx-motif': ['melody', 1, 3, 'game ear'], 'mlx-seq': ['melody', 1, 3, 'show ear'], 'mlx-build': ['melody', 1, 3, 'show ear'], 'tune-anatomy': ['melody', 0, 1, 'show'],")
rep("['fmx-build', 'binary-ternary-spot'],", "['fmx-build', 'binary-ternary-spot'], ['mlx-map', 'tune-anatomy'], ['mlx-phrasing', 'phrase-marks'], ['mlx-qa', 'question-answer'], ['mlx-seq', 'melody-sequence'],")
rep("  'melody': ['tune-anatomy', 'draw-tune', 'phrase-marks', 'question-answer', 'melody-sequence'],",
    "  'melody': ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-build', 'tune-anatomy', 'draw-tune', 'phrase-marks', 'question-answer', 'melody-sequence'],")
# 3. the old lesson's ticks (Phase 117: keys 0 to 4) are not this lesson's steps (k1 to k7)
rep("|| id === 'terms' || id === 'form') && /^\\d+$/.test(String(k)); }", "|| id === 'terms' || id === 'form' || id === 'melody') && /^\\d+$/.test(String(k)); }")
# 4. search words; 'More in the toolbox' leaves this room's own pads out; its grades
rep("  'melody': 'melody tune phrase phrasing phrase mark question answer antecedent consequent sequence motif contour breath comma',",
    "  'melody': 'melody tune line contour high point phrase phrasing phrase mark breath mark comma question answer antecedent consequent period cadence motif repetition sequence tonic',")
rep("|chx|tmx|fmx|sac|ts|nv)-/.test(x)", "|chx|tmx|fmx|mlx|sac|ts|nv)-/.test(x)")
# 5. the rebuilt lesson's own count (6 steps); its extra last step (my tune) is not counted
rep("const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6 };", "const STEPS_TOTAL_NOW = { chords: 6, terms: 6, form: 6, melody: 6 };")
rep("chords: 'k7', terms: 'k7', form: 'k7' };", "chords: 'k7', terms: 'k7', form: 'k7', melody: 'k7' };")
# 6. records saved before this drill's rebuild belong to its old levels
m = re.search(r"const REC_SINCE = \{ chords: \d+, terms: \d+, form: \d+ \};", s)
if not m: raise SystemExit('REC_SINCE')
s = s[:m.end() - 3] + ", melody: REC_MELODY };" + s[m.end():]
s = s.replace("REC_MELODY", open(here + '/rec_melody.txt').read().strip())
# 7. the 2025 lesson and drill this room replaces (MelodyLearn, MELODY_LEVELS, genMelodyQuestion, MelodyQuestion): no longer
# reached. The older tools and their data (QA_ENDINGS, MelodyStaff, ...) stay.
b = "  Question: MelodyQuestion, Learn: MelodyLearn,\n};\n"
i = s.index("function MelodyLearn({ onStart }) {\n"); j = s.index(b, i) + len(b)
s = s[:i] + "const MELODY_DRILL = { id: 'melody', label: 'Melody & Phrasing' };   // its levels, lesson and questions: Phase 481 (Object.assign below)\n" + s[j:]
for w in ['MelodyLearn', 'MELODY_LEVELS', 'genMelodyQuestion', 'MelodyQuestion']:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
# 7a. three tools of this room get icons of their own: the line (a contour, its high point), the motif (one bracket over a
# shape, again), my tune (shapes rising, then a held note)
a = "  'melody-sequence': () => ("
i = s.index(a); j = s.index("\n  ),\n", i) + len("\n  ),\n")
s = s[:j] + """  'mlx-line': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2b8c8c"/><polyline points="3,17 7,13 10,15 14,10 17,6 21,13" fill="none" stroke="#fefbf3" strokeWidth="1.6" strokeLinejoin="round" strokeLinecap="round"/><circle cx="3" cy="17" r="1.4" fill="#fefbf3"/><circle cx="7" cy="13" r="1.4" fill="#fefbf3"/><circle cx="10" cy="15" r="1.4" fill="#fefbf3"/><circle cx="14" cy="10" r="1.4" fill="#fefbf3"/><circle cx="21" cy="13" r="1.4" fill="#fefbf3"/><circle cx="17" cy="6" r="2.5" fill="#e9a83a" stroke="#26296b" strokeWidth="0.6"/></svg>
  ),
  'mlx-motif': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2b8c8c"/><path d="M2.5 9 V6.5 H10.5 V9" fill="none" stroke="#e9a83a" strokeWidth="1.4"/><polyline points="3.5,17 5.5,13 7.5,15 9.5,11" fill="none" stroke="#fefbf3" strokeWidth="1.3"/><circle cx="3.5" cy="17" r="1.3" fill="#fefbf3"/><circle cx="5.5" cy="13" r="1.3" fill="#fefbf3"/><circle cx="7.5" cy="15" r="1.3" fill="#fefbf3"/><circle cx="9.5" cy="11" r="1.3" fill="#fefbf3"/><path d="M13.5 7 V4.5 H21.5 V7" fill="none" stroke="#e9a83a" strokeWidth="1.4"/><polyline points="14.5,15 16.5,11 18.5,13 20.5,9" fill="none" stroke="#fefbf3" strokeWidth="1.3"/><circle cx="14.5" cy="15" r="1.3" fill="#fefbf3"/><circle cx="16.5" cy="11" r="1.3" fill="#fefbf3"/><circle cx="18.5" cy="13" r="1.3" fill="#fefbf3"/><circle cx="20.5" cy="9" r="1.3" fill="#fefbf3"/></svg>
  ),
  'mlx-build': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2b8c8c"/><polyline points="2.5,19 4,16.5 5.5,18 7,15.5" fill="none" stroke="#fefbf3" strokeWidth="1.2"/><polyline points="7.5,15 9,12.5 10.5,14 12,11.5" fill="none" stroke="#fefbf3" strokeWidth="1.2"/><polyline points="12.5,11 14,8.5 15.5,10 17,7.5" fill="none" stroke="#e9a83a" strokeWidth="1.4"/><ellipse cx="20" cy="17" rx="2.4" ry="1.7" fill="none" stroke="#fefbf3" strokeWidth="1.4"/></svg>
  ),
""" + s[j:]
# 7b. the old tools kept in this room: the same words as this chapter (숨표, not 쉼표; 동형 진행 and 반복 apart; scale steps
# as chapter 16's N번 음), and the phrase mark is not the breath
rep("{t('The curved line is a phrase mark. Like a comma in a sentence, it shows where a singer takes a breath. Play each line and watch the comma appear.', '곡선은 프레이즈 마크예요. 문장의 쉼표처럼, 가수가 숨 쉬는 곳을 보여줘요. 한 줄씩 재생해서 쉼표가 나타나는 걸 보세요.')}",
    "{t('The curved line is a phrase mark: these notes belong together. The comma after it is a breath mark: breathe there. Play each line and watch the breath mark appear.', '곡선은 프레이즈 표시예요: 이 음들이 한 프레이즈예요. 그 뒤의 콤마(,)는 숨표예요: 거기서 숨을 쉬어요. 한 줄씩 들어 보고 숨표가 나타나는 걸 봐요.')}")
rep("title: 'Phrase marks: where to breathe',", "title: 'Phrase marks and breath marks',")
rep("  'phrase-marks': ['프레이즈 마크: 숨 쉬는 곳',", "  'phrase-marks': ['프레이즈 표시와 숨표',")
rep("{t('A question phrase ends on an unstable note (2, 4, 5 or 7): it wants to keep going. An answer phrase ends on the tonic (1): it feels finished.', '질문 프레이즈는 불안정한 음 (2, 4, 5, 7도)에서 끝나요: 계속되고 싶어해요. 대답 프레이즈는 으뜸음(1도)에서 끝나요: 끝난 느낌이에요.')}",
    "{t('A question phrase ends on a note that is not the tonic (2, 4, 5 or 7): it wants to keep going. An answer phrase ends on the tonic (1): it feels finished.', '질문 프레이즈는 으뜸음이 아닌 음(2·4·5·7번 음)에서 끝나요: 계속 가고 싶어 해요. 대답 프레이즈는 으뜸음(1번 음)에서 끝나요: 끝난 느낌이에요.')}")
rep("  'question-answer': ['묻는 프레이즈일까, 답하는 프레이즈일까?', '불안정 (2, 4, 5, 7) 아니면 집 (1)?'],", "  'question-answer': ['질문일까, 대답일까?', '2·4·5·7번 음일까, 으뜸음일까?'],")
rep("{t('A sequence repeats a short pattern, but starts one step higher each time. Reveal each repetition and listen for the climbing shape.', '시퀀스는 짧은 패턴을 반복하지만, 매번 한 음씩 높게 시작해요. 하나씩 열어보고 올라가는 모양을 들어보세요.')}",
    "{t('A sequence plays a short pattern again straight after, starting one step higher each time. Reveal each step and listen for the climbing shape.', '동형 진행: 같은 모양이 바로 이어서 한 걸음씩 높은 음에서 다시 시작해요. 하나씩 열어 보고 올라가는 모양을 들어 봐요.')}")
rep("{t('Each repetition (' + shown + ' of 3 so far) is the exact same two-note shape, just moved up one scale step.', '지금까지 ' + shown + '/3번 반복: 매번 똑같은 두 음 모양이지만, 한 음씩 위로 옮겨갔어요.')}",
    "{t('Each step (' + shown + ' of 3 so far) is the exact same two-note shape, just moved up one scale step.', '지금까지 3개 중 ' + shown + '개: 매번 똑같은 두 음 모양을 한 걸음씩 위로 옮겼어요.')}")
rep("  'melody-sequence': ['시퀀스: 같은 모양, 새 음높이', '패턴이 매번 한 칸씩 높아지며 다시 나와요.'],", "  'melody-sequence': ['동형 진행: 같은 모양, 새 음높이', '같은 모양이 매번 한 걸음씩 높아지며 다시 나와요.'],")
rep("<li>학생이 쉬운 곡(다섯 손가락 튠)을 쳐요.", "<li>학생이 쉬운 곡(다섯 손가락 자리에서 치는 곡)을 쳐요.")
rep("'오선을 눌러 여덟 음을 하나씩 위아래로 옮기고, 내 튠을 연주해 봐요. 선이 모양을 보여 줘요.", "'오선을 눌러 여덟 음을 하나씩 위아래로 옮기고, 내 튠을 연주해 봐요. 선율선이 모양을 보여 줘요.")
rep("'튠은 “핫 크로스 번” (전래 동요)이에요.'", "'이 튠은 “핫 크로스 번”(전래 동요)이에요.'")
rep("'리듬 (튠)'", "'리듬(튠)'")
n4 = s.count('악구'); s = s.replace('악구', '프레이즈')
rep("  'melody': '선율과 프레이즈',", "  'melody': '선율과 프레이징',")
# 7c. the map of chapter 24 also: a group of buttons (not a picture) when it can be tapped, each part saying when it is on
i = s.index('function FmxMapSvg('); a = 'return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label}'; j = s.index(a, i)
s = s[:j] + 'return <svg viewBox={`0 0 ${W} ${H}`} role={onTap ? \'group\' : \'img\'} aria-label={label}' + s[j + len(a):]
rep("role: 'button', tabIndex: 0, 'aria-label': lab, style: { cursor: 'pointer' } } : {};", "role: 'button', tabIndex: 0, 'aria-label': lab, 'aria-pressed': !!on(kind, i), className: 'fmx-part', style: { cursor: 'pointer' } } : {};")
rep("    {FMX_LEVELS6.map(k => <React.Fragment key={k}>{lab(k)}</React.Fragment>)}", "    {onTap && <style>{'.fmx-part:focus{outline:none}.fmx-part:focus-visible>rect:first-of-type{stroke:#e4572e;stroke-width:3;stroke-dasharray:5 3}'}</style>}\n    {FMX_LEVELS6.map(k => <React.Fragment key={k}>{lab(k)}</React.Fragment>)}")
# 7d. what the 2025 room left unreachable: its paper pages, its Workbook and Teacher copy
i = s.index("  if (id === 'melody') return [\n"); j = s.index("  ];\n", i) + 5; s = s[:i] + s[j:]
for f in ['PaperContour', 'PaperPhrase', 'PaperQA', 'PaperSequence', 'MelodyWorkbook', 'MelodyTeacher']:
    i = s.index('function ' + f + '('); j = s.index('\n}\n', i) + 3; s = s[:i] + s[j:]
rep(" melody: MelodyWorkbook,", ""); rep(" melody: MelodyTeacher,", "")
for w in ['PaperContour', 'PaperPhrase', 'PaperQA', 'PaperSequence', 'MelodyWorkbook', 'MelodyTeacher']:
    if re.search(r'\b' + w + r'\b', s): raise SystemExit('still used: ' + w)
# 8. Korean: this chapter's words everywhere (선율, not 튠; 프레이즈 표시, not 프레이즈 마크; 동형 진행 for the sequence tool)
n1 = s.count('튠(선율)'); s = s.replace('튠(선율)', '선율')
if s.count('튠으로'): raise SystemExit('튠으로')
n2 = s.count('튠'); s = s.replace('튠', '선율')
n3 = s.count('프레이즈 마크'); s = s.replace('프레이즈 마크', '프레이즈 표시')
# 9. the room comes after chapter 24 (its phrase, phrase mark and repetition) and chapter 9; the group's words
m = re.search(r"melody: \['reading-steps', 'signs'\]", s)
if not m: raise SystemExit('ROOM_AFTER.melody')
s = s[:m.start()] + "melody: ['reading-steps', 'form']" + s[m.end():]
rep("when: 'What a tune is, phrase marks, question and answer, sequences; binary, ternary and rondo form'", "when: 'The line of a tune, phrasing, question and answer, motif and sequence; binary, ternary and rondo form'")
rep("'선율이란, 프레이즈 표시, 묻고 답하기, 시퀀스; 2부·3부·론도 형식'", "'선율선, 프레이징, 질문과 대답, 동기와 동형 진행; 2부·3부·론도 형식'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', n1, n2, n3)
