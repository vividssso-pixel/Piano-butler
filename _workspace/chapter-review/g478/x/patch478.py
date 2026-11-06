#!/usr/bin/env python3
# Phase 478 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15; her 2026-10-17 02:05 macro-first
# plan): chapter 22, Chords, the fourth room of Level 4, built in full: the Lesson Book (page 1 the chord clock), its
# screen lesson (the book with a pad on pages 1 to 6, I IV V again at the end in the student's keys), a 9-level drill,
# the Workbook and the Teacher copy (both replace the Phase 117 ones).
#   chbook478.jsx: the chord staff (ChxStaff), the keys with half steps counted, the chord clock, the Lesson Book
#   chapp478.jsx:  the pads, ChxLearn, the drill (Object.assign on CHORDS_DRILL)
#   chwb478.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 477 (chapter 21's IVX_N, ivxScale, IVX_TONIC_D, ivxNoteTxt, ivxNbKo, ivxAns, ivxCircle, ivxTicks).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['chbook478.jsx', 'chapp478.jsx', 'chwb478.jsx'])
add += "Object.assign(CHORDS_DRILL, { levels: CHX_LEVELS, generate: genChxQuestion, check: chxCheck, answerLabel: chxAnswerLabel, Question: ChxQuestion, Learn: ChxLearn });\n"

# 1. the new code before the Lesson Book registry; chords joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
if s.count(a) != 1: raise SystemExit('LESSON_BOOKS found %d' % s.count(a))
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("intervals: IntervalsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", chords: ChordsLessonBook };") + s[j:]
rep("signs: sgnLbPages, intervals: ivxLbPages };", "signs: sgnLbPages, intervals: ivxLbPages, chords: chxLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'triad-stack', ch: 'chords',", """  { id: 'chx-clock', ch: 'chords', title: 'The chord clock', blurb: 'Every major triad is one shape: 4 half steps, then 3.', C: () => <ChxClockPad/> },
  { id: 'chx-stack', ch: 'chords', title: 'Stack a triad', blurb: 'Skip a letter, skip a letter: root, 3rd, 5th, on the white keys.', C: () => <ChxStackPad/> },
  { id: 'chx-mm', ch: 'chords', title: 'Major or minor triad?', blurb: 'Count the half steps: 4 + 3 or 3 + 4.', C: () => <ChxMinorPad/> },
  { id: 'chx-tonic', ch: 'chords', title: 'The tonic triad', blurb: 'The scale’s 1st, 3rd and 5th notes: C, G, D, F and B♭ major.', C: () => <ChxTonicPad/> },
  { id: 'chx-145', ch: 'chords', title: 'I, IV and V: play them', blurb: 'The triads on the 1st, 4th and 5th notes, in C, G, D or F major.', C: () => <ChxPrimaryPad/> },
  { id: 'chx-hands', ch: 'chords', title: 'Blocked or broken?', blurb: 'Together, or one after the other: right hand and left.', C: () => <ChxHandsPad/> },
  { id: 'triad-stack', ch: 'chords',""")
rep("  'triad-stack': ['3화음 쌓기', '근음, 3음, 5음: 눈사람.'],", """  'chx-clock': ['화음 시계', '장3화음은 모두 같은 모양: 반 걸음 4개, 그다음 3개.'],
  'chx-stack': ['3화음 쌓기', '하나 건너, 하나 건너: 흰건반의 근음, 3음, 5음.'],
  'chx-mm': ['장3화음? 단3화음?', '반 걸음을 세어요: 4 + 3, 또는 3 + 4.'],
  'chx-tonic': ['으뜸화음', '음계의 1번, 3번, 5번 음: C, G, D, F, B♭장조.'],
  'chx-145': ['I, IV, V 치기', '1번, 4번, 5번 음 위의 3화음: C, G, D, F장조.'],
  'chx-hands': ['함께? 펼쳐서?', '함께, 또는 한 음씩 차례로: 오른손과 왼손.'],
  'triad-stack': ['근음, 3음, 5음', '아무 음에서나 시작해요.'],""")
rep("'triad-stack': ['harmony', 1, 3, 'show'],", "'chx-clock': ['harmony', 1, 3, 'show ear'], 'chx-stack': ['harmony', 1, 2, 'show ear'], 'chx-mm': ['harmony', 1, 3, 'show ear'], 'chx-tonic': ['harmony', 1, 3, 'show ear'], 'chx-145': ['harmony', 2, 3, 'show ear'], 'chx-hands': ['harmony', 1, 2, 'game ear'], 'triad-stack': ['harmony', 1, 3, 'show'],")
rep("['ivx-tonic', 'scale-intervals'],", "['ivx-tonic', 'scale-intervals'], ['chx-clock', 'major-minor'], ['chx-stack', 'triad-stack'], ['chx-mm', 'major-minor'], ['chx-tonic', 'key-chords'], ['chx-145', 'primary-triads'], ['chx-hands', 'primary-triads'],")
rep("  'chords': ['triad-stack', 'major-minor', 'key-chords', 'primary-triads', 'inversions', 'cadences', 'chord-extensions', 'seventh-chords'],",
    "  'chords': ['chx-clock', 'chx-stack', 'chx-mm', 'chx-tonic', 'chx-145', 'chx-hands', 'triad-stack', 'major-minor', 'key-chords', 'primary-triads', 'inversions', 'cadences', 'chord-extensions', 'seventh-chords'],")
# 3. the old lesson's ticks (Phase 117: 8 steps, keys 0 to 7) are not this lesson's steps (k1 to k7)
rep("function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs' || id === 'intervals') && /^\\d+$/.test(String(k)); }",
    "function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs' || id === 'intervals' || id === 'chords') && /^\\d+$/.test(String(k)); }")
# 4. search words; 'More in the toolbox' leaves this room's own pads out
rep("  'chords': 'chord triad inversion cadence roman numeral seventh ninth eleventh thirteenth extension',",
    "  'chords': 'chord triad root third fifth major minor tonic triad primary triads I IV V blocked broken chord clock inversion cadence roman numeral seventh ninth eleventh thirteenth extension',")
rep("!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|sac|ts|nv)-/.test(x)", "!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|sac|ts|nv)-/.test(x)")
# 5. older tools: this chapter's words (장3화음, 3음, 줄 and 칸); no snowman in the blurb
rep("{ id: 'triad-stack', ch: 'chords', title: 'Stack a triad', blurb: 'Root, 3rd, 5th: the snowman.'", "{ id: 'triad-stack', ch: 'chords', title: 'Root, 3rd, 5th', blurb: 'Start on any note.'")
rep("<div style={actTitle}>{t('Stack a triad', '삼화음 쌓기')}</div>", "<div style={actTitle}>{t('Root, 3rd, 5th', '근음, 3음, 5음')}</div>")
rep("{t('A triad is three notes stacked in 3rds, like building a 3-layer cake, or stacking a snowman: the bottom scoop is the ', '삼화음은 3도씩 쌓은 세 음이에요. 3단 케이크를 쌓거나 눈사람을 만드는 것과 비슷해요: 맨 아래는 ')}", "{t('A triad is three notes stacked in 3rds: the bottom note is the ', '3화음은 3도씩 쌓은 세 음이에요. 맨 아래는 ')}")
rep("{t(' (the foundation), then the ', ' (기초), 그 위에 ')}", "{t(', then the ', ', 그 위에 ')}")
rep("{t(' as the top scoop. On the staff they sit line-line-line or space-space-space, like a snowman\\u2019s three balls; on the keyboard, skip a white key each time.', ' 이 얹혀요. 오선지에서는 줄-줄-줄 또는 칸-칸-칸으로 나란히 앉고, 건반에서는 매번 흰건반 하나씩 건너뛰면 돼요.')}",
    "{t(' at the top. On the staff: all lines or all spaces; on the keys, skip a white key each time.', '이 있어요. 오선에서는 모두 줄 또는 모두 칸에 있고, 건반에서는 흰건반을 하나씩 건너뛰어요.')}")
rep("<div style={actTitle}>{t('Major or minor?', '장화음일까, 단화음일까?')}</div>", "<div style={actTitle}>{t('Major or minor?', '장3화음일까, 단3화음일까?')}</div>")
rep("{t('Major and minor triads are almost twins: same root, same top note, only the ', '장화음과 단화음은 거의 쌍둥이예요: 근음도 같고 맨 위 음도 같은데, ')}", "{t('Major and minor triads are almost twins: same root, same top note, only the ', '장3화음과 단3화음은 거의 쌍둥이예요: 근음도 같고 맨 위 음도 같은데, ')}")
rep("{t(' moves, by a single semitone. Think of a face: major is a big smile, minor is the exact same face with the corners of the mouth pulled down just a little. Flip it and listen: major = a ', '만 반음 움직여요. 얼굴 표정을 떠올려보세요: 장화음은 활짝 웃는 얼굴, 단화음은 똑같은 얼굴인데 입꼬리만 살짝 내려간 거예요. 눌러서 바꿔보고 들어보세요: 장화음은 ')}",
    "{t(' moves, by a single half step. Think of a face: major is a big smile, minor is the exact same face with the corners of the mouth pulled down just a little. Flip it and listen: major = a ', '만 반 걸음 움직여요. 얼굴 표정을 떠올려보세요: 장3화음은 활짝 웃는 얼굴, 단3화음은 똑같은 얼굴인데 입꼬리만 살짝 내려간 거예요. 눌러서 바꿔보고 들어보세요: 장3화음은 ')}")
rep("{t(' (4 semitones) then a minor 3rd (3); minor = the reverse.', ' (반음 4개) 다음 단3도 (반음 3개), 단화음은 그 반대예요.')}", "{t(' (4 half steps) then a minor 3rd (3); minor = the reverse.', ' (반 걸음 4개) 다음 단3도 (반 걸음 3개), 단3화음은 그 반대예요.')}")
rep("  'major-minor': ['장화음일까 단화음일까', '가운데 음을 바꿔 봐요.'],", "  'major-minor': ['장3화음일까 단3화음일까', '3음을 바꿔 봐요.'],")
rep("t('Root, 3rd, 5th', '근음, 3도, 5도'), t('Start on any note (the root), add the note a 3rd above, then the note a 5th above. Line-line-line or space-space-space.', '아무 음(근음)에서 시작해서 3도 위 음, 5도 위 음을 더해요. 선-선-선 또는 칸-칸-칸이에요.')",
    "t('Root, 3rd, 5th', '근음, 3음, 5음'), t('Start on any note (the root), add the note a 3rd above, then the note a 5th above. Line-line-line or space-space-space.', '아무 음(근음)에서 시작해서 3도 위 음, 5도 위 음을 더해요. 줄-줄-줄 또는 칸-칸-칸이에요.')")
rep("'장화음 = 장3도 + 단3도. 단화음 = 단3도 + 장3도. 근음과 5도는 그대로예요.'", "'장3화음 = 장3도 + 단3도. 단3화음 = 단3도 + 장3도. 근음과 5음은 그대로예요.'")
# 6. a rebuilt lesson's own count: synced totals merge with Math.max, so the 2025 lesson's 8 steps would come back
rep("function chapterStatus(id, totals) {", "const STEPS_TOTAL_NOW = { chords: 6 };   // rebuilt lessons: their own count, never an older, larger synced total\nfunction chapterStatus(id, totals) {")
rep("const n = stepsDone(id), tot = (totals || loadStepTotals())[id];", "const n = stepsDone(id), tot = STEPS_TOTAL_NOW[id] || (totals || loadStepTotals())[id];")
rep("of += +totals[k] || 0;", "of += STEPS_TOTAL_NOW[k] || +totals[k] || 0;")
# 7. the screen lesson's extra last step (the whole again) is not one of the chapter's steps (chapters 16, 19, 21, 22)
rep("function stepsDone(id) { const d = loadDone()[id] || {}; return Object.keys(d).filter(k => d[k] && !skgOldStep(id, k)).length; }",
    "const STEP_EXTRA = { scales: '6', 'key-signatures': 'k7', intervals: 'k7', chords: 'k7' };   // the screen lesson's extra last step (not counted)\nfunction stepsDone(id) { const d = loadDone()[id] || {}; return Object.keys(d).filter(k => d[k] && !skgOldStep(id, k) && STEP_EXTRA[id] !== k).length; }")
rep("n += Object.keys(d).filter(i => d[i] && !skgOldStep(k, i)).length;", "n += Object.keys(d).filter(i => d[i] && !skgOldStep(k, i) && STEP_EXTRA[k] !== i).length;")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
