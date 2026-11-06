#!/usr/bin/env python3
# Phase 468 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 12, Pitch, Hz & Range,
# built in full: the Lesson Book (dictionary entries), its screen lesson (the book with what moves on pages 2 to 6), a
# 9-level drill, the Workbook and the Teacher copy.
#   sprbook468.jsx: the instruments (SprInst, SprFiddle), the 88 keys (SprKeys88), the Lesson Book
#   sprapp468.jsx:  the pads of pages 2 to 6, SprLearn, the drill (Object.assign on PITCH_RANGE_DRILL)
#   sprwb468.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 467 (chapter 10's code is already there: sdyQ, SdyPaper, sdyCol, sdyCircle are used).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['sprbook468.jsx', 'sprapp468.jsx', 'sprwb468.jsx'])

# 1. the new code before the Lesson Book registry; pitch-range joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("dynamics: DynamicsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", 'pitch-range': PitchRangeLessonBook };") + s[j:]
rep("'reading-steps': sskLbPages, dynamics: sdyLbPages };", "'reading-steps': sskLbPages, dynamics: sdyLbPages, 'pitch-range': sprLbPages };")

# 2. the toolbox: this room's moving parts first
rep("  { id: 'hz-explorer', ch: 'pitch-range',", """  { id: 'spr-zone', ch: 'pitch-range', title: 'Low, middle or high?', blurb: 'Hear a note low, middle or high on the keys, then say where it was.', C: () => <SprZonePad/> },
  { id: 'spr-big', ch: 'pitch-range', title: 'Big is low, small is high', blurb: 'Xylophone bars, then pairs: which one sounds higher?', C: () => <SprBigPad/> },
  { id: 'spr-fam', ch: 'pitch-range', title: 'Which family?', blurb: 'Thirteen instruments: their families and how they make their sound.', C: () => <SprFamilyPad/> },
  { id: 'spr-ladder', ch: 'pitch-range', title: 'The violin family', blurb: 'Hear each one’s lowest note, then put them in order.', C: () => <SprLadderPad/> },
  { id: 'spr-range', ch: 'pitch-range', title: 'Who plays where?', blurb: 'An instrument’s range on the 88 keys; which can play lower?', C: () => <SprRangePad/> },
  { id: 'hz-explorer', ch: 'pitch-range',""")
rep("  'hz-explorer': ['음은 얼마나 높을까? 헤르츠',", """  'spr-zone': ['낮은 음? 가운데 음? 높은 음?', '건반의 낮은 곳, 가운데, 높은 곳의 음을 듣고, 어디였는지 골라요.'],
  'spr-big': ['크면 낮고, 작으면 높아요', '실로폰 막대, 그리고 둘 중 어느 쪽이 더 높은 소리를 낼까요?'],
  'spr-fam': ['어느 가족일까요?', '악기 열세 개: 가족과 소리 내는 방법.'],
  'spr-ladder': ['바이올린 가족', '저마다 가장 낮은 음을 듣고, 차례로 놓아요.'],
  'spr-range': ['누가 어디를 연주할까요?', '88건반 위의 음역; 어느 쪽이 더 낮게 낼 수 있을까요?'],
  'hz-explorer': ['음은 얼마나 높을까? 헤르츠',""")
rep("'hz-explorer': ['about', 1, 3, 'show ear']", "'spr-zone': ['about', 0, 1, 'game ear'], 'spr-big': ['about', 0, 1, 'game ear'], 'spr-fam': ['about', 0, 2, 'game'], 'spr-ladder': ['about', 0, 2, 'game ear'], 'spr-range': ['about', 0, 3, 'show game'], 'hz-explorer': ['about', 1, 3, 'show ear']")
rep("['sdy-tie', 'tie-slur'],", "['sdy-tie', 'tie-slur'], ['spr-zone', 'range-chart'], ['spr-big', 'size-pitch'], ['spr-fam', 'size-pitch'], ['spr-ladder', 'size-pitch'], ['spr-range', 'range-chart'],")
rep("  'pitch-range': ['hz-explorer', 'string-lab', 'size-pitch', 'octave-ladder', 'range-chart'],", "  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-range', 'size-pitch', 'string-lab', 'range-chart', 'hz-explorer', 'octave-ladder'],")
# 3. 'easier after': chapter 2 (low on the left, high on the right) and the staff (the two clefs)
rep("tones: ['whole-staff'], 'pitch-range': ['first-steps'],", "tones: ['whole-staff'], 'pitch-range': ['first-steps', 'staff'],")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
