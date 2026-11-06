#!/usr/bin/env python3
# Phase 475 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 20, Signs, the second
# room of Level 4, built in full: the Lesson Book (dictionary entries), its screen lesson (the book with a pad on pages 2
# to 6), a 9-level drill, the Workbook and the Teacher copy (both replace the Phase 116 ones).
#   sgnbook475.jsx: the road (bars with their signs), its order (sgnOrder), the staff with the signs (SgnStaff), the Lesson Book
#   sgnapp475.jsx:  the pads of pages 2 to 6, SgnLearn, the drill (Object.assign on SIGNS_DRILL)
#   sgnwb475.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 474 (chapter 19's SkgStaff and pads are the models; chapter 12's sskRaw draws the notes).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['sgnbook475.jsx', 'sgnapp475.jsx', 'sgnwb475.jsx'])

# 1. the new code before the Lesson Book registry; signs joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("'key-signatures': KeySigLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", signs: SignsLessonBook };") + s[j:]
rep("'piano-story': spsLbPages, 'key-signatures': skgLbPages };", "'piano-story': spsLbPages, 'key-signatures': skgLbPages, signs: sgnLbPages };")

# 2. the toolbox: this room's pads first, then its older tools
rep("  { id: 'dc-ds-coda', ch: 'signs',", """  { id: 'sgn-rep', ch: 'signs', title: 'Repeat signs', blurb: 'Back to the start-repeat sign, or to the beginning: listen to the road, then tap the bars in order.', C: () => <SgnPad page={2}/> },
  { id: 'sgn-volta', ch: 'signs', title: '1st and 2nd time bars', blurb: 'The 1st time bar, back, then the 2nd: listen to the road, then tap the bars in order.', C: () => <SgnPad page={3}/> },
  { id: 'sgn-dc', ch: 'signs', title: 'D.C. al Fine', blurb: 'Back to the beginning, then up to Fine: listen to the road, then tap the bars in order.', C: () => <SgnPad page={4}/> },
  { id: 'sgn-ds', ch: 'signs', title: 'D.S. al Fine', blurb: 'Back to the sign, then up to Fine: listen to the road, then tap the bars in order.', C: () => <SgnPad page={5}/> },
  { id: 'sgn-pause', ch: 'signs', title: 'The pause', blurb: 'Without and with the pauses, over a note and over a rest: hear the difference.', C: () => <SgnPad page={6}/> },
  { id: 'dc-ds-coda', ch: 'signs',""")
rep("  'dc-ds-coda': ['D.C., D.S., Fine, Coda', '각 기호가 어디로 보내는지.'],", """  'sgn-rep': ['도돌이표', '시작 도돌이표로, 없으면 처음으로: 길을 듣고, 치는 차례대로 마디 번호를 눌러요.'],
  'sgn-volta': ['1번 괄호와 2번 괄호', '1번 괄호를 치고 돌아가서 2번 괄호로: 길을 듣고, 치는 차례대로 마디 번호를 눌러요.'],
  'sgn-dc': ['D.C. al Fine', '처음으로 돌아가 Fine까지: 길을 듣고, 치는 차례대로 마디 번호를 눌러요.'],
  'sgn-ds': ['D.S. al Fine', '세뇨로 돌아가 Fine까지: 길을 듣고, 치는 차례대로 마디 번호를 눌러요.'],
  'sgn-pause': ['늘임표', '늘임표 없이 한 번, 늘임표대로 한 번. 음표 위, 쉼표 위: 차이를 들어 봐요.'],
  'dc-ds-coda': ['D.C., D.S., Fine, Coda', '각 기호가 어디로 보내는지.'],""")
rep("'road-map': ['words', 1, 2, 'game'],", "'sgn-rep': ['words', 1, 2, 'game ear'], 'sgn-volta': ['words', 1, 2, 'game ear'], 'sgn-dc': ['words', 1, 2, 'game ear'], 'sgn-ds': ['words', 1, 2, 'game ear'], 'sgn-pause': ['words', 1, 2, 'show ear'], 'road-map': ['words', 1, 2, 'game'],")
rep("['dc-ds-coda', 'road-map'],", "['dc-ds-coda', 'road-map'], ['sgn-rep', 'road-map'], ['sgn-volta', 'road-map'], ['sgn-dc', 'dc-ds-coda'], ['sgn-ds', 'dc-ds-coda'], ['sgn-pause', 'road-map'],")
rep("  'signs': ['road-map', 'dc-ds-coda', 'ottava', 'ornaments', 'grace-write'],",
    "  'signs': ['sgn-rep', 'sgn-volta', 'sgn-dc', 'sgn-ds', 'sgn-pause', 'road-map', 'dc-ds-coda', 'ottava', 'ornaments', 'grace-write'],")
# 3. the old lesson's ticks (Phase 116: 6 steps, keys 0 to 5, under the same id) are not this lesson's steps: the new steps
#    keep theirs as k1 to k6 (Step storeAs), and the counts skip the old ones (chapter 19's skgOldStep, now for both rooms)
rep("function skgOldStep(id, k) { return id === 'key-signatures' && /^\\d+$/.test(String(k)); }",
    "function skgOldStep(id, k) { return (id === 'key-signatures' || id === 'signs') && /^\\d+$/.test(String(k)); }")
# 4. the chapter's grade tag and search words follow the new chapter (AMEB Music Craft: repeat signs Grade 1, the rest
#    Grade 2; ABRSM: D.C. and fine Grade 1, D.S., the pause and repeat marks Grade 2)
rep("signs: 'Prelim–G2'", "signs: 'G1–G2'")
rep("  'signs': 'repeat sign dal segno da capo coda fine ottava tie slur',",
    "  'signs': 'repeat sign start repeat end repeat 1st and 2nd time bars volta da capo dal segno segno fine pause fermata coda ottava tie slur',")
# 5. 'More in the toolbox' leaves this room's own pads out (they are the lesson's pictures)
rep("!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sac|ts|nv)-/.test(x)", "!/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|sac|ts|nv)-/.test(x)")
# 6. the screen lesson's 'Easier after' line: this room builds on chapter 8 (bars, the repeat sign) and chapter 9 (C position)
rep("signs: ['reading-steps', 'dynamics']", "signs: ['time-signatures', 'reading-steps']")
# 7. chapter 8's bar-line tool names the two repeat signs as this chapter does (시작 도돌이표 / 끝 도돌이표)
rep("ko: '도돌이표 시작', d1: 'Thick then thin, dots on the right: play from here again.', d2: '굵은 선 다음에 얇은 선, 오른쪽에 점: 여기서부터 다시 연주해요.'",
    "ko: '시작 도돌이표', d1: 'Thick then thin, dots on the right: play from here again.', d2: '굵은 줄과 가는 줄 뒤의 점 두 개: 여기서부터 다시 쳐요.'")
rep("ko: '도돌이표 끝', d1: 'Dots on the left, then thin and thick: go back to the start-repeat (or to the beginning).', d2: '왼쪽에 점, 그다음 얇은 선과 굵은 선: 도돌이표 시작(없으면 맨 처음)으로 돌아가요.'",
    "ko: '끝 도돌이표', d1: 'Dots on the left, then thin and thick: go back to the start-repeat (or to the beginning).', d2: '가는 줄과 굵은 줄 앞의 점 두 개: 시작 도돌이표로, 없으면 처음으로 돌아가요.'")
# 8. chapter 10's list of marks names the pause as this chapter does (늘임표 first, its other name 페르마타)
rep("t('Fermata (pause)', '페르마타 (늘임표)')", "t('Pause (fermata)', '늘임표 (페르마타)')")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
