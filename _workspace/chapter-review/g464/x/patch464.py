#!/usr/bin/env python3
# Phase 464 (her 2026-10-13 23:51 '지금부터 추천대로 다 가줘 ... 사전처럼 깔끔하게'; Book rules 14 and 15): chapter 8,
# Time Signatures, built in full with B1-B12 as recommended: the Lesson Book (dictionary entries, LbDefs), its screen
# lesson (the book with what moves, B12), a 10-level drill (B10), the Workbook and the Teacher copy (B11).
#   tsbook464.jsx: LbDefs, tsRaw / TsStaff (rhythms on the treble staff), the Lesson Book
#   tsapp464.jsx:  the pads of pages 2 to 6, TsLearn, the drill (Object.assign on TIMESIG_DRILL)
#   tswb464.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Also: B1 grouping quavers, duplets and triplets, 3/4 or 6/8 move to Rhythm patterns (their steps at the end of its
# lesson); B7 끝세로줄 for the thin-thick end line and 세로줄 for the bar line in the app; A5 the chapter's tools count
# 1 + 2 + (Book rule 12); the toolbox gets the five pads.
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['tsbook464.jsx', 'tsapp464.jsx', 'tswb464.jsx'])

# 1. the new code before the Lesson Book registry; time-signatures joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
s = s[:i] + add + line.replace(" };", ", 'time-signatures': TimeSignaturesLessonBook };") + s[j:]
rep("tones: tnLbPages, pulse: plLbPages, 'note-values': nvLbPages };", "tones: tnLbPages, pulse: plLbPages, 'note-values': nvLbPages, 'time-signatures': tsLbPages };")
# Book rule 14: dictionary entries count as the lesson's words (they go before the picture, like LbSay)
rep("if (lbIsPic(a[i]) && a[i + 1].type === LbSay) {", "if (lbIsPic(a[i]) && (a[i + 1].type === LbSay || a[i + 1].type === LbDefs)) {")

# 2. A5: the chapter's tools count 1 + 2 + (Book rule 12; + is said 'and')
rep("{word === 'and' ? '&' : word}", "{word === 'and' ? '+' : word}")
rep("const SUB_WORDS = { 1: [], 2: ['&'], 3: ['trip', 'let'], 4: ['e', '&', 'a'], 6: ['&', '', '&', '', '&'] };",
    "const SUB_WORDS = { 1: [], 2: ['+'], 3: ['trip', 'let'], 4: ['e', '+', 'a'], 6: ['+', '', '+', '', '+'] };   // Phase 464: + for 'and' (Book rule 12)")
rep("label: s ? '&' : String(i + 1)", "label: s ? '+' : String(i + 1)")
rep("'박 사이에 쳐요, “&”에서.'", "'박 사이에 쳐요, “+”(앤)에서.'")
rep("{isBeat ? p / 2 + 1 : '&'}", "{isBeat ? p / 2 + 1 : '+'}")
rep("labels = half ? ['1', '&', '2', '&']", "labels = half ? ['1', '+', '2', '+']")
rep("t('Count a bar of 2/2: 1 & 2 &', '2/2 한 마디 세기: 1 & 2 &')", "t('Count a bar of 2/2: 1 + 2 +', '2/2 한 마디 세기: 1 + 2 +')")
rep("1 & 2 & 3 &", "1 + 2 + 3 +", 4)
rep("const labels = cut ? ['1', '&', '2', '&']", "const labels = cut ? ['1', '+', '2', '+']")
rep('("1 & 2 &")', '("1 + 2 +")', 2)

# 3. B7: 세로줄 for the bar line, 끝세로줄 for the thin-thick end line; in English the end line is the double bar line
#    (its other name: a final bar line), as in the book
rep("마디선", "세로줄", 9)
rep("세로줄은 마디를 닫는 세로선이라서", "세로줄은 마디를 닫는 줄이라서")
rep("{ k: 'double', en: 'Double bar line', ko: '겹세로줄', d1: 'Two thin lines: a new section starts here, or the key or time signature changes.',",
    "{ k: 'double', en: 'Two thin lines', ko: '겹세로줄', d1: 'Between two sections: a new section starts here, or the key or time signature changes.',")
rep("{ k: 'final', en: 'Final bar line', ko: '끝세로줄', d1: 'Thin then thick: the end of the piece.', d2: '얇은 선 다음에 굵은 선: 곡이 끝났어요.' },",
    "{ k: 'final', en: 'Double bar line', ko: '끝세로줄', d1: 'A thin line and a thick line: the end. Its other name is a final bar line.', d2: '가는 줄과 굵은 줄: 곡의 끝.' },")
rep("  'bar-lines': ['세로줄 (겹세로줄, 도돌이표)',", "  'bar-lines': ['세로줄 (끝세로줄, 도돌이표)',")

# 4. the toolbox: this room's moving parts first; B1's moves to Rhythm patterns
rep("""  { id: 'nv-walk', ch: 'note-values',""", """  { id: 'ts-bars', ch: 'time-signatures', title: 'Bars on the click', blurb: 'Three bars of 3/4 and the repeat sign: listen, then tap and hold each note.', C: () => <TsPad page={2}/> },
  { id: 'ts-numbers', ch: 'time-signatures', title: 'Count each time signature', blurb: '2/4, 3/4, 4/4 and C on the click: listen, then tap.', C: () => <TsPad page={3}/> },
  { id: 'ts-strong', ch: 'time-signatures', title: 'Tap the strong beat', blurb: 'Plain clicks: count out loud and tap only on 1.', C: () => <TsStrongPad/> },
  { id: 'ts-build', ch: 'time-signatures', title: 'Build a bar', blurb: 'Add notes and rests until the bar is full, then play it.', C: () => <TsBuildBar/> },
  { id: 'ts-tie', ch: 'time-signatures', title: 'Hear the tie', blurb: 'The same two bars with the tie and without it.', C: () => <TsTiePad/> },
  { id: 'nv-walk', ch: 'note-values',""")
for tid in ['grouping', 'duplets', 'regroup']:
    rep("  { id: '" + tid + "', ch: 'time-signatures',", "  { id: '" + tid + "', ch: 'rhythm',")
rep("  'nv-walk': ['4분음표 걷기',", """  'ts-bars': ['클릭에 맞춰 마디를', '3/4 세 마디와 도돌이표: 들어 보고, 음마다 누르고 있어요.'],
  'ts-numbers': ['박자표마다 세요', '2/4, 3/4, 4/4, C를 클릭에 맞춰: 들어 보고, 쳐 봐요.'],
  'ts-strong': ['센박에 쳐요', '같은 클릭: 소리 내어 세면서 1에서만 쳐요.'],
  'ts-build': ['마디 만들기', '마디가 꽉 찰 때까지 음표와 쉼표를 넣고 들어 봐요.'],
  'ts-tie': ['붙임줄 들어 보기', '같은 두 마디를 붙임줄이 있게, 없이.'],
  'nv-walk': ['4분음표 걷기',""")
rep("'split-it': ['rnotes', 1, 1, 'show'], 'nv-walk':", "'split-it': ['rnotes', 1, 1, 'show'], 'ts-bars': ['rtime', 0, 1, 'game ear'], 'ts-numbers': ['rtime', 0, 1, 'game ear'], 'ts-strong': ['rtime', 0, 1, 'game ear'], 'ts-build': ['rtime', 0, 1, 'game ear'], 'ts-tie': ['rtime', 0, 1, 'show ear'], 'nv-walk':")
rep(" ['finger-friends', 'finger-numbers'], ['accidental-cards', 'sharp-flat'],", " ['finger-friends', 'finger-numbers'], ['accidental-cards', 'sharp-flat'], ['ts-bars', 'bar-lines'], ['ts-numbers', 'time-sig-numbers'], ['ts-strong', 'beat-groups'], ['ts-build', 'fill-bar'], ['ts-tie', 'tie-slur'],")
rep("  'time-signatures': ['time-sig-numbers', 'count-along', 'common-cut', 'bar-lines', 'beat-doubler', 'regroup', 'grouping', 'duplets', 'beat-groups', 'beat-target', 'rest-grouping', 'fix-the-bar', 'fill-bar', 'heard-bar'],",
    "  'time-signatures': ['ts-bars', 'ts-numbers', 'ts-strong', 'ts-build', 'ts-tie', 'bar-lines', 'beat-groups', 'beat-target', 'fill-bar', 'fix-the-bar', 'rest-grouping', 'heard-bar', 'count-along', 'time-sig-numbers', 'common-cut', 'beat-doubler'],")
rep("  'rhythm': ['rhythm-cards-all', 'count-more', 'anacrusis', 'make-card', 'beam-apples', 'dotted-notes', 'dot-lab'],",
    "  'rhythm': ['rhythm-cards-all', 'count-more', 'anacrusis', 'make-card', 'beam-apples', 'dotted-notes', 'dot-lab', 'grouping', 'duplets', 'regroup'],")
rep("{ id: 'rtime', name: 'Time signatures', when: 'What the two numbers mean, common and cut time, bar lines, the bottom number, counting along, strong and weak beats, rests on the staff, filling bars', color: '#e4572e' },",
    "{ id: 'rtime', name: 'Time signatures', when: 'Bars and bar lines, the repeat sign, the two numbers and common time, strong and weak beats, rests on the staff, filling bars, the tie; cut time and the bottom number', color: '#e4572e' },")
rep("  rtime: ['박자표', '두 숫자의 뜻, 보통박자와 얼라 브레베, 세로줄, 아래 숫자, 따라 세기, 강한 박과 약한 박, 오선 위의 쉼표, 마디 채우기'],",
    "  rtime: ['박자표', '마디와 세로줄, 도돌이표, 두 숫자와 보통박자, 센박과 여린박, 오선 위의 쉼표, 마디 채우기, 붙임줄; 알라 브레베와 아래 숫자'],")
rep("  ['p5', 'beat', 'Rests and bar lines; 2/4, 3/4, 4/4', ['count-along', 'bar-lines', 'fill-bar']],", "  ['p5', 'beat', 'Rests and bar lines; 2/4, 3/4, 4/4', ['ts-bars', 'ts-numbers', 'ts-build']],")
rep("""      <Step title={t('Dot lab', '점 실험실')}>
      <DotLab/>
      </Step>
    </Lesson>""", """      <Step title={t('Dot lab', '점 실험실')}>
      <DotLab/>
      </Step>
      <Step title={t('Grouping notes to show the beat', '박을 보여주는 음표 묶기')}>
      <GroupingGame/>
      </Step>
      <Step title={t('Duplets, triplets and more', '듀플릿, 셋잇단음표, 그 이상')}>
      <DupletDemo/>
      </Step>
      <Step title={t('3/4 or 6/8?', '3/4일까 6/8일까?')}>
      <RegroupQuavers/>
      </Step>
    </Lesson>""")


# 5. her 2026-10-14 00:36 '6번,23번만 바꾸자': chapter 6 'The Staff & the Two Clefs' / '오선과 두 음자리표', chapter 23 'Composers' /
#    '작곡가' (the guide page's search title stays 'Reading the Staff for Beginners')
rep("id: 'staff', label: 'Reading the Staff', levels: STAFF_LEVELS", "id: 'staff', label: 'The Staff & the Two Clefs', levels: STAFF_LEVELS")
rep("{ id: 'staff', label: 'Reading the Staff', concept: STAFF_DRILL", "{ id: 'staff', label: 'The Staff & the Two Clefs', concept: STAFF_DRILL")
rep("id: 'composers', label: 'Famous Composers', levels: COMPOSERS_LEVELS", "id: 'composers', label: 'Composers', levels: COMPOSERS_LEVELS")
rep("{ id: 'composers', label: 'Famous Composers', concept: COMPOSERS_DRILL", "{ id: 'composers', label: 'Composers', concept: COMPOSERS_DRILL")
rep("'staff': '오선보 읽기', 'whole-staff': '줄과 칸 이름'", "'staff': '오선과 두 음자리표', 'whole-staff': '줄과 칸 이름'")
rep("'composers': '유명한 작곡가들',", "'composers': '작곡가',")
rep("t('Reading the Staff', '오선보 읽기')", "t('The Staff & the Two Clefs', '오선과 두 음자리표')", 2)
rep("t('Famous composers', '유명한 작곡가들')", "t('Composers', '작곡가')")

# 6. a Korean drop capital sits in the middle of its square (the printed openers; QA review)
rep("""  .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { float: left;""", """  html[lang="ko"] .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { font-family: inherit; font-size: 2.25em; padding: 4px 10px 9px; }
  .lb-opener .bk-body > p.lb-say:first-of-type::first-letter { float: left;""")

# 7. the 'easier after' line in Korean: a comma between the two chapters (the · already sits after each number)
rep("{i > 0 && (LANG === 'ko' ? ' · ' : i === show.length - 1 ? ' and ' : ', ')}", "{i > 0 && (LANG === 'ko' ? ', ' : i === show.length - 1 ? ' and ' : ', ')}")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
