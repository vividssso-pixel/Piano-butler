#!/usr/bin/env python3
# Phase 477 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15; her 2026-10-17 02:05 macro-first
# plan): chapter 21, Intervals, the third room of Level 4, built in full: the Lesson Book (page 1 the interval ladder), its
# screen lesson (the book with a pad on pages 2 to 6, the ladder again at the end in the student's keys), a 9-level drill,
# the Workbook and the Teacher copy (both replace the Phase 116 ones).
#   ivbook477.jsx: the interval staff (IvxStaff), the keys with numbers, the ladder, the Lesson Book
#   ivapp477.jsx:  the pads, IvxLearn, the drill (Object.assign on INTERVALS_DRILL)
#   ivwb477.jsx:   the Workbook (pages 2 to 8) and the Teacher copy
# Base: Phase 476 (pbKeysFor, pbKeysRow, pbKeysHead, pbBoxes; chapter 19's helpers).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['ivbook477.jsx', 'ivapp477.jsx', 'ivwb477.jsx'])
add += "Object.assign(INTERVALS_DRILL, { levels: IVX_LEVELS, generate: genIvxQuestion, check: ivxCheck, answerLabel: ivxAnswerLabel, Question: IvxQuestion, Learn: IvxLearn });\n"

# 1. the new code before the Lesson Book registry; intervals joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("signs: SignsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", intervals: IntervalsLessonBook };") + s[j:]
rep("'key-signatures': skgLbPages, signs: sgnLbPages };", "'key-signatures': skgLbPages, signs: sgnLbPages, intervals: ivxLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'interval-ruler', ch: 'intervals',", """  { id: 'ivx-ladder', ch: 'intervals', title: 'The interval ladder', blurb: 'Every interval from one note, a 2nd to an octave: tap a number to hear it.', C: () => <IvxMapPad/> },
  { id: 'ivx-count', ch: 'intervals', title: 'Count an interval', blurb: 'Count both notes: the lower note is 1.', C: () => <IvxCountPad set="p2"/> },
  { id: 'ivx-hand', ch: 'intervals', title: 'Intervals in the hand', blurb: 'C or G position: thumb and finger 3 make a 3rd.', C: () => <IvxHandPad/> },
  { id: 'ivx-big', ch: 'intervals', title: '6th, 7th or octave?', blurb: 'The intervals wider than the hand.', C: () => <IvxCountPad set="p4"/> },
  { id: 'ivx-mh', ch: 'intervals', title: 'Melodic or harmonic?', blurb: 'One after the other, or together.', C: () => <IvxCountPad set="p5"/> },
  { id: 'ivx-tonic', ch: 'intervals', title: 'Above the tonic', blurb: 'Major or perfect, from the tonic of C, G, D or F major.', C: () => <IvxTonicPad/> },
  { id: 'interval-ruler', ch: 'intervals',""")
rep("  'interval-ruler': ['음정 자', '1부터 줄과 칸을 세어요.'],", """  'ivx-ladder': ['음정 사다리', '한 음에서 2도부터 옥타브까지 모든 음정: 음정을 누르면 들려요.'],
  'ivx-count': ['음정 세기', '두 음을 모두 세요: 아래 음이 1이에요.'],
  'ivx-hand': ['손 안의 음정', 'C 자리, G 자리: 엄지와 3번 손가락은 3도.'],
  'ivx-big': ['6도, 7도, 옥타브?', '다섯 손가락 자리보다 넓은 음정.'],
  'ivx-mh': ['선율적? 화성적?', '한 음씩 차례로, 또는 두 음 함께.'],
  'ivx-tonic': ['으뜸음 위의 음정', 'C, G, D, F장조의 으뜸음에서: 장음정? 완전음정?'],
  'interval-ruler': ['음정 자', '1부터 줄과 칸을 세어요.'],""")
rep("'interval-ruler': ['intervals', 1, 2, 'show'],", "'ivx-ladder': ['intervals', 1, 3, 'show ear'], 'ivx-count': ['intervals', 1, 2, 'game ear'], 'ivx-hand': ['intervals', 1, 2, 'show ear'], 'ivx-big': ['intervals', 1, 2, 'game ear'], 'ivx-mh': ['intervals', 1, 2, 'game ear'], 'ivx-tonic': ['intervals', 2, 3, 'show ear'], 'interval-ruler': ['intervals', 1, 2, 'show'],")
rep("['sgn-pause', 'road-map'],", "['sgn-pause', 'road-map'], ['ivx-ladder', 'scale-intervals'], ['ivx-count', 'interval-ruler'], ['ivx-hand', 'interval-ruler'], ['ivx-big', 'interval-ruler'], ['ivx-mh', 'interval-ear'], ['ivx-tonic', 'scale-intervals'],")
rep("  'intervals': ['step-skip', 'interval-ruler', 'letter-hop', 'semitone-counter', 'scale-intervals', 'interval-ear', 'invert-interval', 'tritone'],",
    "  'intervals': ['ivx-ladder', 'ivx-count', 'ivx-hand', 'ivx-big', 'ivx-mh', 'ivx-tonic', 'step-skip', 'interval-ruler', 'letter-hop', 'semitone-counter', 'scale-intervals', 'interval-ear', 'invert-interval', 'tritone'],")
# 3. the old lesson's ticks (Phase 105: 5 steps, keys 0 to 4) are not this lesson's steps (k1 to k7)
rep("function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs') && /^\\d+$/.test(String(k)); }",
    "function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs' || id === 'intervals') && /^\\d+$/.test(String(k)); }")
# 4. search words; 'More in the toolbox' leaves this room's own pads out
rep("  'intervals': 'interval second third fourth fifth sixth seventh octave unison major minor perfect augmented diminished',",
    "  'intervals': 'interval ladder second third fourth fifth sixth seventh octave unison melodic harmonic tonic above the tonic major minor perfect augmented diminished',")
rep("!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|sac|ts|nv)-/.test(x)", "!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|sac|ts|nv)-/.test(x)")
# 5. older tools: Korean names that match this chapter's words
rep("  'letter-hop': ['글자 따라 뛰기 (음정 세기)', '시작 음이 1이에요.'],", "  'letter-hop': ['음이름 따라 뛰기', '시작 음이 1이에요.'],")
rep("  'scale-intervals': ['장조 스케일로 빨리 찾기 (음정)', 'M2 M3 P4 P5 M6 M7 P8.'],", "  'scale-intervals': ['장조 음계로 빨리 찾기 (음정)', '장2 장3 완전4 완전5 장6 장7 완전8.'],")
# 6. a printed page has no game board (chapters 19, 20 and 21)
rep("function BoardTrack({ b, pixel }) {\n", "function BoardTrack({ b, pixel }) {\n  try { if (new URLSearchParams(location.search).get('print') === '1') return null; } catch (e) {}\n")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
