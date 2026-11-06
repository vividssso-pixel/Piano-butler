#!/usr/bin/env python3
# Phase 471 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 16, Scales, built
# in full: the Lesson Book (dictionary entries), its screen lesson (the book with a listen-and-tap keyboard on pages 2 to
# 6), a 9-level drill, the Workbook and the Teacher copy.
#   sscbook471.jsx: the scale keyboard (SscKeys) and staff (SscStaff), the Lesson Book
#   sscapp471.jsx:  the pads of pages 2 to 6, SscLearn, the drill (Object.assign on SCALES_DRILL)
#   sscwb471.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 470 (chapter 11's TnPKeys, tnAcc and tnSign, chapter 10's sdyCircle, chapter 12's sprTick are used).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['sscbook471.jsx', 'sscapp471.jsx', 'sscwb471.jsx'])

# 1. the new code before the Lesson Book registry; scales joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("rhythm: RhythmLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", scales: ScalesLessonBook };") + s[j:]
rep("tempo: stmLbPages, rhythm: srhLbPages };", "tempo: stmLbPages, rhythm: srhLbPages, scales: sscLbPages };")

# 2. the toolbox: this room's moving parts first
rep("  { id: 'minor-forms', ch: 'scales',", """  { id: 'ssc-steps', ch: 'scales', title: 'The major scale’s steps', blurb: 'C major on the keys: whole, whole, half, whole, whole, whole, half. Listen, then play it.', C: () => <SscPad page={2}/> },
  { id: 'ssc-fingers', ch: 'scales', title: 'Fingers on C major', blurb: 'Each hand’s fingering, the thumb under and 3 over.', C: () => <SscPad page={3}/> },
  { id: 'ssc-degrees', ch: 'scales', title: 'Find the degrees', blurb: 'Tap a key of C major: its number, 1 to 8.', C: () => <SscPad page={4}/> },
  { id: 'ssc-g', ch: 'scales', title: 'G major and its F♯', blurb: 'Listen, then play G major up.', C: () => <SscPad page={5}/> },
  { id: 'ssc-f', ch: 'scales', title: 'F major and its B♭', blurb: 'Listen, then play F major up, with the right hand’s fingering.', C: () => <SscPad page={6}/> },
  { id: 'minor-forms', ch: 'scales',""")
rep("  'scale-finder': ['스케일 찾기',", """  'ssc-steps': ['장음계의 걸음', '건반의 C장조 음계: 온, 온, 반, 온, 온, 온, 반. 듣고, 쳐 봐요.'],
  'ssc-fingers': ['C장조 손가락', '한 손씩 손가락 번호: 엄지 밑으로 넣기와 3번 넘기기.'],
  'ssc-degrees': ['음의 번호 찾기', 'C장조 음계의 건반을 눌러요: 번호 1에서 8.'],
  'ssc-g': ['G장조와 F♯', '듣고, G장조 음계를 올라가며 쳐 봐요.'],
  'ssc-f': ['F장조와 B♭', '듣고, F장조 음계를 오른손 손가락 번호대로 쳐 봐요.'],
  'scale-finder': ['스케일 찾기',""")
rep("  'build-minor': ['scales', 2, 3, 'game write'],", "  'ssc-steps': ['scales', 1, 2, 'game ear'], 'ssc-fingers': ['scales', 1, 2, 'show game'], 'ssc-degrees': ['scales', 1, 2, 'game'], 'ssc-g': ['scales', 1, 2, 'game ear'], 'ssc-f': ['scales', 1, 2, 'game ear'],\n  'build-minor': ['scales', 2, 3, 'game write'],")
rep("['srh-read', 'rhythm-cards-all'],", "['srh-read', 'rhythm-cards-all'], ['ssc-steps', 'major-shape'], ['ssc-fingers', 'major-fingering'], ['ssc-degrees', 'degree-names'], ['ssc-g', 'build-major'], ['ssc-f', 'scale-finder'],")
rep("  'scales': ['major-shape', 'build-major', 'degree-names', 'major-fingering', 'scale-finder', 'minor-forms', 'build-minor', 'minor-fingering', 'modes'],", "  'scales': ['ssc-steps', 'ssc-fingers', 'ssc-degrees', 'ssc-g', 'ssc-f', 'scale-finder', 'major-shape', 'build-major', 'degree-names', 'major-fingering', 'minor-forms', 'build-minor', 'minor-fingering', 'modes'],")
# 3. the chapter's lesson is now 'scales' itself (as every chapter's): the old 'scales-major' and 'scales-minor' lessons'
# ticks and totals no longer count towards it
rep("    if (k !== id && k.indexOf(id + '-') !== 0) return;\n    const d = done[k] || {};", "    if (k !== id && k.indexOf(id + '-') !== 0) return;\n    if (k === 'scales-major' || k === 'scales-minor') return;   // Phase 471: lessons that are gone\n    const d = done[k] || {};")

# 4. the REMEMBER band's label never breaks (Korean '기억해요' fell onto two lines next to a long line)
rep("<span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS}}>{t('Remember', '기억해요')}</span>", "<span style={{fontSize:9.5,fontWeight:800,color:BK.coral,...VIC_CAPS,whiteSpace:'nowrap',flex:'0 0 auto'}}>{t('Remember', '기억해요')}</span>")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
