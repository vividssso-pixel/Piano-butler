#!/usr/bin/env python3
# Phase 469 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 13, Tempo Race,
# built in full: the Lesson Book (dictionary entries), its screen lesson (the book with what moves on pages 2 to 6), a
# 9-level drill, the Workbook and the Teacher copy.
#   stmbook469.jsx: the words, the metronome (StmMetronome, StmMark), the tunes (StmTune), the Lesson Book
#   stmapp469.jsx:  the pads of pages 2 to 6, StmLearn, the drill (Object.assign on TEMPO_DRILL)
#   stmwb469.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 468 (chapter 10's SdyStaff and SdyPaper and chapter 12's sprTick and sprBoxN are used).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['stmbook469.jsx', 'stmapp469.jsx', 'stmwb469.jsx'])

# 1. the new code before the Lesson Book registry; tempo joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("'pitch-range': PitchRangeLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", tempo: TempoLessonBook };") + s[j:]
rep("dynamics: sdyLbPages, 'pitch-range': sprLbPages };", "dynamics: sdyLbPages, 'pitch-range': sprLbPages, tempo: stmLbPages };")

# 2. the toolbox: this room's moving parts first
rep("  { id: 'metronome', ch: 'tempo',", """  { id: 'stm-sf', ch: 'tempo', title: 'Slow or fast?', blurb: 'One tune slow and fast; then listen and say which.', C: () => <StmSlowFastPad/> },
  { id: 'stm-words', ch: 'tempo', title: 'Four tempo words', blurb: 'Adagio, Andante, Moderato, Allegro: hear each one, then name it.', C: () => <StmWordsPad/> },
  { id: 'stm-read', ch: 'tempo', title: 'Read it, count in, play', blurb: 'The tempo word over the first bar; a count-in; find the word on a page.', C: () => <StmReadPad/> },
  { id: 'stm-metro', ch: 'tempo', title: 'The metronome', blurb: 'Set a number, watch the weight, hear the beat; ♩ = 60 or 120?', C: () => <StmMetroPad/> },
  { id: 'stm-steady', ch: 'tempo', title: 'Keep the tempo', blurb: 'Tap with the clicks, then keep going alone; steady, rushing or dragging?', C: () => <StmSteadyPad/> },
  { id: 'metronome', ch: 'tempo',""")
rep("  'tempo-race': ['템포 경주',", """  'stm-sf': ['느리게? 빠르게?', '한 선율을 느리게, 빠르게; 그다음 듣고 골라요.'],
  'stm-words': ['빠르기말 네 개', '아다지오, 안단테, 모데라토, 알레그로: 하나씩 듣고, 이름을 맞혀요.'],
  'stm-read': ['읽고, 미리 세고, 치기', '첫 마디 위의 빠르기말, 미리 세기, 악보에서 빠르기말 찾기.'],
  'stm-metro': ['메트로놈', '숫자를 맞추고, 추를 보고, 박을 들어요. ♩ = 60일까요, 120일까요?'],
  'stm-steady': ['빠르기 지키기', '똑딱에 맞춰 치다가 혼자 계속; 꾸준하게? 서두르기? 끌기?'],
  'tempo-race': ['템포 경주',""")
rep("  'tempo-race': ['rtempo', 0, 2, 'show ear'],", "  'stm-sf': ['rtempo', 0, 1, 'game ear'], 'stm-words': ['rtempo', 0, 1, 'game ear'], 'stm-read': ['rtempo', 0, 2, 'game'], 'stm-metro': ['rtempo', 0, 2, 'show ear'], 'stm-steady': ['rtempo', 0, 2, 'game'], 'tempo-race': ['rtempo', 0, 2, 'show ear'],")
rep("['spr-range', 'range-chart'],", "['spr-range', 'range-chart'], ['stm-sf', 'tempo-walk'], ['stm-words', 'tempo-race'], ['stm-read', 'tempo-race'], ['stm-metro', 'metronome'], ['stm-steady', 'tap-tempo'],")
rep("  'tempo': ['tempo-walk', 'tempo-race', 'tap-tempo', 'same-tune-tempo', 'speed-change', 'metronome'],", "  'tempo': ['stm-sf', 'stm-words', 'stm-read', 'stm-metro', 'stm-steady', 'metronome', 'tempo-walk', 'tempo-race', 'tap-tempo', 'same-tune-tempo', 'speed-change'],")
# 3. 'easier after': chapter 3 (a steady beat) and chapter 5 (the crotchet)
rep("  tempo: ['pulse'], rhythm: ['time-signatures'],", "  tempo: ['pulse', 'note-values'], rhythm: ['time-signatures'],")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
