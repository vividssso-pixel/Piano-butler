#!/usr/bin/env python3
# Phase 466 (her 2026-10-14 06:54 '계속 가줘'; Book rules 14 and 15): chapter 9, Steps & Skips, built in full: the Lesson
# Book (dictionary entries), its screen lesson (the book with what moves on pages 2 to 6), a 9-level drill, the Workbook
# and the Teacher copy.
#   sskbook466.jsx: sskRaw / SskStaff (tunes on one staff), the step and position pictures, the Lesson Book
#   sskapp466.jsx:  the pads of pages 2 to 6, SskLearn, the drill (Object.assign on READING_STEPS_DRILL)
#   sskwb466.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Also: a step is 한 걸음 in Korean everywhere (MOVE_KO and the old drill's words said 한 칸); the toolbox gets the five pads.
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['sskbook466.jsx', 'sskapp466.jsx', 'sskwb466.jsx'])

# 1. the new code before the Lesson Book registry; reading-steps joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
s = s[:i] + add + line.replace(" };", ", 'reading-steps': ReadingStepsLessonBook };") + s[j:]
rep("'note-values': nvLbPages, 'time-signatures': tsLbPages };", "'note-values': nvLbPages, 'time-signatures': tsLbPages, 'reading-steps': sskLbPages };")

# 2. a step is 한 걸음 (the chapter's word, and chapter 6's)
rep("const MOVE_KO = { same: '같은 음', 'step up': '한 칸 위로', 'step down': '한 칸 아래로',", "const MOVE_KO = { same: '같은 음', 'step up': '한 걸음 위로', 'step down': '한 걸음 아래로',")
rep("const RS_KO = { Down: '아래로', Same: '같은 음', Up: '위로', Step: '한 칸', Skip: '건너뛰기' };", "const RS_KO = { Down: '아래로', Same: '같은 음', Up: '위로', Step: '한 걸음', Skip: '건너뛰기' };")
rep("  'step-skip': ['한 칸, 건너뛰기, 같은 음?', '방향과 거리로 읽어요.'],", "  'step-skip': ['한 걸음, 건너뛰기, 같은 음?', '방향과 거리로 읽어요.'],")

# 3. the toolbox: this room's moving parts first
rep("""  { id: 'mini-tune', ch: 'reading-steps',""", """  { id: 'ssk-shape', ch: 'reading-steps', title: 'Which way does it go?', blurb: 'Listen to a tune, then say up, down or the same for each note.', C: () => <SskShapePad/> },
  { id: 'ssk-step', ch: 'reading-steps', title: 'Step, skip or the same', blurb: 'A move on the staff and on the keys, in both clefs.', C: () => <SskStepPad/> },
  { id: 'ssk-cpos', ch: 'reading-steps', title: 'C position', blurb: 'Each hand: tap the keys, then name the finger.', C: () => <SskPosPad pos="C"/> },
  { id: 'ssk-gpos', ch: 'reading-steps', title: 'G position', blurb: 'Each hand: tap the keys, then name the finger.', C: () => <SskPosPad pos="G"/> },
  { id: 'ssk-read', ch: 'reading-steps', title: 'Read a tune', blurb: 'Four tunes, each hand in C and G position: listen, then play.', C: () => <SskReadPad/> },
  { id: 'mini-tune', ch: 'reading-steps',""")
rep("  'mini-tune': ['짧은 튠 읽기', '박을 세며 읽는 도 자리 튠.'],", """  'ssk-shape': ['어디로 갈까요?', '선율을 듣고, 음마다 위로, 아래로, 같은 음을 골라요.'],
  'ssk-step': ['한 걸음, 건너뛰기, 같은 음', '오선과 건반에서 보는 움직임, 두 음자리표 모두.'],
  'ssk-cpos': ['C 자리', '양손 각각: 건반을 눌러 보고, 손가락을 골라요.'],
  'ssk-gpos': ['G 자리', '양손 각각: 건반을 눌러 보고, 손가락을 골라요.'],
  'ssk-read': ['선율 읽기', '선율 넷, C 자리와 G 자리의 양손: 듣고, 쳐 봐요.'],
  'mini-tune': ['짧은 튠 읽기', '박을 세며 읽는 도 자리 튠.'],""")
rep("  'mini-tune': ['steps', 0, 1, 'game'],", "  'ssk-shape': ['steps', 0, 1, 'game ear'], 'ssk-step': ['steps', 0, 1, 'show'], 'ssk-cpos': ['steps', 0, 1, 'game'], 'ssk-gpos': ['steps', 0, 1, 'game'], 'ssk-read': ['steps', 0, 1, 'game ear'],\n  'mini-tune': ['steps', 0, 1, 'game'],")
rep(" ['ts-bars', 'bar-lines'],", " ['ts-bars', 'bar-lines'], ['ssk-shape', 'complete-melody'], ['ssk-step', 'step-skip'], ['ssk-cpos', 'five-positions'], ['ssk-gpos', 'five-positions'], ['ssk-read', 'mini-tune'],")
rep("  'reading-steps': ['mini-tune', 'echo', 'hear-find', 'complete-melody', 'five-positions'],", "  'reading-steps': ['ssk-shape', 'ssk-step', 'ssk-cpos', 'ssk-gpos', 'ssk-read', 'hear-find', 'echo', 'mini-tune', 'five-positions', 'complete-melody'],")
rep("{ id: 'steps', name: 'Reading tunes: pitch + rhythm', when: 'Reading tiny tunes, completing a melody, five-finger positions in all 12 keys, sight-reading cards', color: '#e4572e' },",
    "{ id: 'steps', name: 'Reading tunes: pitch + rhythm', when: 'Up, down or the same; steps and skips; C and G positions; reading a tune; all 12 positions; sight-reading cards', color: '#e4572e' },")
rep("  steps: ['튠 읽기: 음높이 + 리듬', '짧은 튠 읽기, 선율 완성하기, 12개 조의 다섯 손가락 자리, 초견 카드'],",
    "  steps: ['선율 읽기: 음높이 + 리듬', '위로, 아래로, 같은 음; 한 걸음과 건너뛰기; C 자리와 G 자리; 선율 읽기; 12개 자리 모두; 초견 카드'],")
rep("  ['k6', 'keys', 'C position, both hands', ['five-positions']],", "  ['k6', 'keys', 'C position, both hands', ['ssk-cpos', 'five-positions']],")
rep("  ['r3', 'read', 'Reads by steps and skips', ['step-skip']],", "  ['r3', 'read', 'Reads by steps and skips', ['ssk-step', 'step-skip']],")
rep("  ['r4', 'read', 'Reads a tiny tune', ['mini-tune']],", "  ['r4', 'read', 'Reads a tiny tune', ['ssk-read', 'mini-tune']],")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')

# 4. keys in the screen tools: the finger numbers and letters readable on a lit key (navy on pale coral, white on coral);
#    a wrong key only outlined (the read pad)
s = open(dst, encoding='utf-8').read()
rep("  pick:   { white: '#e4572e', black: '#e4572e', stroke: '#c0431f', sw: 1.5 },   // Phase 462: the key you tapped",
    "  pick:   { white: '#e4572e', black: '#e4572e', stroke: '#c0431f', sw: 1.5, text: '#fff' },   // Phase 462: the key you tapped (Phase 466: white words on it)")
rep("  mate:   { white: '#fbe3da', black: '#e4572e', stroke: '#e9b9a6', sw: 1 },     // Phase 462: the keys that go with it",
    "  mate:   { white: '#fbe3da', black: '#e4572e', stroke: '#e9b9a6', sw: 1, text: '#26296b' },     // Phase 462: the keys that go with it (Phase 466: navy words on it)\n  miss:   { white: '#fff', black: '#26296b', stroke: '#e4572e', sw: 2.5, text: '#e4572e' },     // Phase 466: a wrong key, outlined")
rep("<text x={k.x + whiteW / 2} y={labels ? whiteH - (solfaOn() ? 48 : 38) : whiteH - (sf ? 26 : 12)} textAnchor=\"middle\" fontSize={labels ? 19 : 15} fontWeight=\"900\"\n                  fill={m ? m.stroke : '#26296b'}",
    "<text x={k.x + whiteW / 2} y={labels ? whiteH - (solfaOn() ? 48 : 38) : whiteH - (sf ? 26 : 12)} textAnchor=\"middle\" fontSize={labels ? 19 : 15} fontWeight=\"900\"\n                  fill={m ? (m.text || m.stroke) : '#26296b'}")
rep("""              <text x={k.x + whiteW / 2} y={whiteH - 12} textAnchor="middle" fontSize="13" fontWeight="800"
                fill={m ? m.stroke : '#6d6f9c'} style={{pointerEvents:'none'}}>{k.info.names[0]}</text>""",
    """              <text x={k.x + whiteW / 2} y={whiteH - 12} textAnchor="middle" fontSize="13" fontWeight="800"
                fill={m ? (m.text || m.stroke) : '#6d6f9c'} style={{pointerEvents:'none'}}>{k.info.names[0]}</text>""")
rep("fontSize=\"10.5\" fontWeight=\"800\" fill={m ? m.stroke : '#6d6f9c'} style={{pointerEvents:'none'}}>{solfa(names[k.i])}</text>}", "fontSize=\"10.5\" fontWeight=\"800\" fill={m ? (m.text || m.stroke) : '#6d6f9c'} style={{pointerEvents:'none'}}>{solfa(names[k.i])}</text>}")
rep("fill={m ? m.stroke : '#8f91b3'} style={{pointerEvents:'none'}}>{solfa(k.info.names[0])}</text>", "fill={m ? (m.text || m.stroke) : '#8f91b3'} style={{pointerEvents:'none'}}>{solfa(k.info.names[0])}</text>")
# 5. Korean: the book's word order for a move (위로 한 걸음, 아래로 건너뛰기)
rep("const MOVE_KO = { same: '같은 음', 'step up': '한 걸음 위로', 'step down': '한 걸음 아래로', 'skip up': '건너뛰어 위로', 'skip down': '건너뛰어 아래로',",
    "const MOVE_KO = { same: '같은 음', 'step up': '위로 한 걸음', 'step down': '아래로 한 걸음', 'skip up': '위로 건너뛰기', 'skip down': '아래로 건너뛰기',")
# 6. the chapter's older tools say 한 걸음 and 선율 too (the book's words)
def region(a, b):
    global s
    i = s.index(a); j = s.index(b, i)
    seg = s[i:j]
    seg = seg.replace('한 칸/줄 올라가면', '한 걸음 올라가면').replace('한 칸을 건너뛰면', '하나를 건너뛰면').replace('한 칸', '한 걸음').replace('튠', '선율')
    s = s[:i] + seg + s[j:]
region("function ExplReadingSteps1()", "function ExplTerms1()")
region("function StepSkip()", "const RS_LEVELS = [")
region("function EchoTune()", "\nfunction ", )
rep("[[1, t('steps', '한 칸')], [2, t('steps + skips', '한 칸 + 건너뛰기')]", "[[1, t('steps', '한 걸음')], [2, t('steps + skips', '한 걸음 + 건너뛰기')]")
rep("  'mini-tune': ['짧은 튠 읽기', '박을 세며 읽는 도 자리 튠.'],", "  'mini-tune': ['짧은 선율 읽기', 'C 자리에서 박을 세며 읽는 선율.'],")
rep("  'echo': ['튠 따라 치기 (귀로 듣고)', '3-5개 음을 듣고 다시 쳐 봐요.'],", "  'echo': ['선율 따라 치기 (귀로 듣고)', '3~5개 음을 듣고 다시 쳐 봐요.'],")
rep("  'hear-find': ['듣고 찾기', '들은 튠은 어느 악보일까? 어떤 음이 다르게 연주됐을까?'],", "  'hear-find': ['듣고 찾기', '들은 선율은 어느 악보일까요? 어떤 음이 다르게 연주됐을까요?'],")
rep("  'complete-melody': ['선율 완성하기', '튠을 마무리하는 끝음을 골라요.'],", "  'complete-melody': ['선율 완성하기', '선율을 마무리하는 끝음을 골라요.'],")
# 7. 'easier after': Line and Space Names (where G on line 1 and C in space 2 of the bass staff are learned) and Time Signatures
rep("'reading-steps': ['staff', 'time-signatures']", "'reading-steps': ['whole-staff', 'time-signatures']")
open(dst, 'w', encoding='utf-8').write(s)
print('ok 2')
