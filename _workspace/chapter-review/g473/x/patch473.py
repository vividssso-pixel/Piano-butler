#!/usr/bin/env python3
# Phase 473 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 18, The Piano's
# Story, the last room of Level 3, built in full: the Lesson Book (dictionary entries), its screen lesson (the book with
# a pad on pages 2 to 6), a 9-level drill, the Workbook and the Teacher copy (both replace the Phase 363 ones).
#   spsbook473.jsx: the drawings (grand, upright, harpsichord, clavichord, the three ways to sound a string, the action,
#                   the pedals, the timeline) and the Lesson Book
#   spsapp473.jsx:  the pads of pages 2 to 6, SpsLearn, the drill (Object.assign on PIANO_STORY_DRILL)
#   spswb473.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 472 (chapter 17's SacStaff draws the Workbook's tunes; chapter 12's SprKeys88 the 88 keys; actionNote).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['spsbook473.jsx', 'spsapp473.jsx', 'spswb473.jsx'])

# 1. the new code before the Lesson Book registry; piano-story joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("accidentals: AccidentalsLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", 'piano-story': PianoStoryLessonBook };") + s[j:]
rep("scales: sscLbPages, accidentals: sacLbPages };", "scales: sscLbPages, accidentals: sacLbPages, 'piano-story': spsLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'keyboard-ancestors', ch: 'piano-story',", """  { id: 'sps-sound', ch: 'piano-story', title: 'Pluck, push or strike', blurb: 'Harpsichord, clavichord, piano: press gently or hard and hear; then a listening quiz.', C: () => <SpsPad page={2}/> },
  { id: 'sps-softloud', ch: 'piano-story', title: 'Piano and forte', blurb: 'The first piano on a timeline; soft, loud, getting louder: the piano can, the harpsichord cannot.', C: () => <SpsPad page={3}/> },
  { id: 'sps-action', ch: 'piano-story', title: 'Key, hammer, damper', blurb: 'Hold a key: the hammer strikes and comes back, the damper moves off. Then name the parts.', C: () => <SpsPad page={4}/> },
  { id: 'sps-pedals', ch: 'piano-story', title: 'The pedals', blurb: 'The sustain and soft pedals: press them and play; then hear: pedal or not?', C: () => <SpsPad page={5}/> },
  { id: 'sps-keys', ch: 'piano-story', title: 'Grand, upright, 88 keys', blurb: 'The lowest A, middle C and the highest C; count the eight Cs.', C: () => <SpsPad page={6}/> },
  { id: 'keyboard-ancestors', ch: 'piano-story',""")
rep("  'keyboard-ancestors': ['클라비코드, 하프시코드, 피아노',", """  'sps-sound': ['뜯기, 밀기, 치기', '하프시코드, 클라비코드, 피아노: 살살, 세게 눌러 들어 보고, 듣기 퀴즈도 해요.'],
  'sps-softloud': ['피아노와 포르테', '연표 속 최초의 피아노. 여리게, 세게, 점점 세게: 피아노는 되고, 하프시코드는 안 돼요.'],
  'sps-action': ['건반, 해머, 댐퍼', '건반을 누르고 있으면 해머가 현을 치고 되돌아오고, 댐퍼가 현에서 떨어져요. 부분 이름도 맞혀요.'],
  'sps-pedals': ['페달', '댐퍼 페달과 소프트 페달을 밟고 쳐 봐요. 그다음 들어 봐요: 페달을 밟았을까요?'],
  'sps-keys': ['그랜드, 업라이트, 88건반', '가장 낮은 A, 가운데 도, 가장 높은 C를 들어요. C 여덟 개도 세어요.'],
  'keyboard-ancestors': ['클라비코드, 하프시코드, 피아노',""")
rep("  'keyboard-ancestors': ['about', 0, 3, 'show ear'],", "  'sps-sound': ['about', 0, 2, 'game ear'], 'sps-softloud': ['about', 0, 2, 'game ear'], 'sps-action': ['about', 0, 2, 'show game ear'], 'sps-pedals': ['about', 0, 2, 'game ear'], 'sps-keys': ['about', 0, 2, 'show ear'],\n  'keyboard-ancestors': ['about', 0, 3, 'show ear'],")
rep("['spr-zone', 'range-chart'],", "['spr-zone', 'range-chart'], ['sps-sound', 'keyboard-ancestors'], ['sps-softloud', 'keyboard-ancestors'], ['sps-action', 'keyboard-ancestors'], ['sps-pedals', 'pedal'], ['sps-keys', 'range-chart'],")
rep("  'piano-story': ['keyboard-ancestors', 'piano-timeline', 'piano-action', 'eras'],", "  'piano-story': ['sps-sound', 'sps-softloud', 'sps-action', 'sps-pedals', 'sps-keys', 'keyboard-ancestors', 'piano-timeline', 'piano-action', 'eras'],")
# 3. 'easier after': chapter 10 (p and f) and chapter 12 (strings, the 88 keys)
rep("composers: ['piano-story'], melody:", "composers: ['piano-story'], 'piano-story': ['dynamics', 'pitch-range'], melody:")
# 4. the Styles chapter's eras page went with the old lesson's step 5 (the eras): it now goes with the toolbox's eras tool
rep("const bkStepLabel = (st) => st === 'all' ? 'All lesson steps' :", "const bkStepLabel = (st) => /^tool /.test(String(st)) ? 'Toolbox: ' + ({ eras: 'The style eras' }[String(st).slice(5)] || String(st).slice(5)) : st === 'all' ? 'All lesson steps' :")
rep("function bkStepLink(chId, st) {\n  const n = bkStepNo(st), ch = bkStepChapter(chId, st);", "function bkStepLink(chId, st) {\n  if (/^tool /.test(String(st))) return bkLink('tool=' + String(st).slice(5));\n  const n = bkStepNo(st), ch = bkStepChapter(chId, st);")
rep("    { id: 'er', name: 'The style eras', step: 'story 5', page: '5' },", "    { id: 'er', name: 'The style eras', step: 'tool eras', page: '5' },")
rep('    <WbTop step="story 5"/>', '    <WbTop step="tool eras"/>')
rep("This page goes with The Piano's Story lesson, step 5 (the strip's code opens it).", "This page goes with The style eras in the toolbox (the strip's code opens it).")
rep("Page 5 (the style eras) goes with The Piano's Story lesson, step 5.", "Page 5 (the style eras) goes with The style eras in the toolbox.")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
