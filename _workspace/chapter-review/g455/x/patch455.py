#!/usr/bin/env python3
# Phase 455 (her 2026-10-13 'b 전부 추천대로', G1 'not keeping the count steady; playing the first beat and starting the
# count late', G2 'walk, running ... 1+2+3+4+, 1e+a 2e+a', G3 'none'): chapter 3, Pulse & Counting, as a Lesson Book,
# its online lesson (the book on screen with what moves), a 5-level drill, a Workbook and a Teacher copy.
#   plbook455.jsx: the Lesson Book (Phase 446's draft with B3 and B7 applied, and the live parts wired in)
#   plapp455.jsx:  what moves on each page, PlLearn, the drill (Object.assign on PULSE_DRILL, like the tones chapter)
#   plwb455.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Also: LbTune's coral finger circles (B8); the spread pairs pages for tones and pulse like the other book chapters
# (tones' spread had each workbook page facing the page before its own); the toolbox: the pulse room's tools are the
# book's moving parts, strong and weak beats and 'tap the right beat' move to Time signatures (B4), 'count it out loud'
# (1 and 2 and) to Notes and rests; both lessons get those steps at the end, so no other chapter's step links move.
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['plbook455.jsx', 'plapp455.jsx', 'plwb455.jsx'])

# 1. the new code, before the Lesson Book registry; pulse joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook, tones: TonesLessonBook };"
rep(a, add + a.replace("tones: TonesLessonBook };", "tones: TonesLessonBook, pulse: PulseLessonBook };"))
rep("const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages, 'whole-staff': wsLbPages, 'ledger-lines': llLbPages };",
    "const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages, 'whole-staff': wsLbPages, 'ledger-lines': llLbPages, tones: tnLbPages, pulse: plLbPages };   // Phase 455: tones and pulse too, so each workbook page faces its own lesson page")

# 2. LbTune: finger numbers in coral circles (B8)
rep("function LbTune({ name, how, seq, icon }) {", "function LbTune({ name, how, seq, icon, coral }) {   // coral (Phase 455): finger numbers in coral circles, so they never read as the count")
rep(": <span key={i} style={{width:28,height:28,borderRadius:14,background:'#fff',border:'2px solid ' + BK.ink,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14.5,fontWeight:900,color:BK.ink}}>{x}</span>)}",
    ": <span key={i} style={{width:28,height:28,borderRadius:14,background:coral ? BK.coral : '#fff',border:'2px solid ' + (coral ? BK.coral : BK.ink),display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14.5,fontWeight:900,color:coral ? '#fff' : BK.ink}}>{x}</span>)}")

# 3. a drill that is tapped by ear has no printed worksheet
rep("{T && st.tab === 'drill' && <PrintLink drillId={active.id} level={level} />}", "{T && st.tab === 'drill' && !concept.noPrint && <PrintLink drillId={active.id} level={level} />}")
rep("""  if (!concept) {
    return (
      <div style={{maxWidth:600,margin:'40px auto',padding:'0 20px',fontFamily:'Inter,sans-serif',textAlign:'center',color:'#26296b'}}>
        <p>No printable worksheet for this activity yet""", """  if (!concept || concept.noPrint) {
    return (
      <div style={{maxWidth:600,margin:'40px auto',padding:'0 20px',fontFamily:'Inter,sans-serif',textAlign:'center',color:'#26296b'}}>
        <p>No printable worksheet for this activity yet""")

# 4. the toolbox: the pulse room's tools are the book's moving parts
rep("""  { id: 'beat-or-rhythm', ch: 'pulse', title: 'Beat or rhythm?', blurb: 'A tune’s long and short notes against the steady beat: tap one or the other and see what you hit.', C: () => <BeatOrRhythm/> },
  { id: 'beat-groups', ch: 'pulse',""", """  { id: 'beat-or-rhythm', ch: 'pulse', title: 'Beat or rhythm?', blurb: 'Words over a steady beat: tap the beat, then tap the words.', C: () => <PlWordsBeat/> },
  { id: 'count-ring', ch: 'pulse', title: 'Count with the ring', blurb: 'Four circles light up with the click: count 1 2 3 4, four times round.', C: () => <PlCountRing/> },
  { id: 'silent-beats', ch: 'pulse', title: 'Silent beats still count', blurb: 'Play on some beats and keep counting through the silent ones.', C: () => <PlSilentBeats/> },
  { id: 'finger-beat', ch: 'pulse', title: 'A new finger on each beat', blurb: 'Black keys on the beat, a new finger each time, counting out loud.', C: () => <PlFingerBeat/> },
  { id: 'beat-groups', ch: 'time-signatures',""")
rep("""  { id: 'beat-target', ch: 'pulse',""", """  { id: 'beat-target', ch: 'time-signatures',""")
rep("""  { id: 'count-aloud', ch: 'pulse',""", """  { id: 'count-aloud', ch: 'note-values',""")
rep("""  'beat-or-rhythm': ['박일까, 리듬일까?', '튠의 길고 짧은 음과 일정한 박: 둘 중 하나를 쳐 보고 맞힌 곳을 봐요.'],""",
    """  'beat-or-rhythm': ['박일까, 리듬일까?', '꾸준한 박 위의 낱말: 박을 치고, 그다음 낱말을 쳐요.'],
  'count-ring': ['동그라미와 함께 세기', '클릭에 맞춰 동그라미 네 개에 불이 켜져요: 1 2 3 4, 네 바퀴.'],
  'silent-beats': ['조용한 박에서도 계속 세요', '몇 박에서만 치고, 조용한 박에서는 계속 세요.'],
  'finger-beat': ['박마다 다른 손가락', '박마다 다른 손가락으로 검은건반을 치며 소리 내어 세요.'],""")
rep("""'beat-groups': ['rpulse', 0, 2, 'game ear'], 'beat-target': ['rpulse', 0, 2, 'game home'], 'count-aloud': ['rpulse', 0, 1, 'show'],""",
    """'beat-groups': ['rtime', 0, 2, 'game ear'], 'beat-target': ['rtime', 0, 2, 'game home'], 'count-aloud': ['rnotes', 0, 1, 'show'],
  'count-ring': ['rpulse', 0, 1, 'game'], 'silent-beats': ['rpulse', 0, 1, 'game'], 'finger-beat': ['rpulse', 0, 1, 'game home'],""")
rep("""  { id: 'rpulse', name: 'Pulse & counting', when: 'The steady beat, tapping on the right beat, counting out loud', color: '#e4572e' },""",
    """  { id: 'rpulse', name: 'Pulse & counting', when: 'The steady beat, counting out loud, silent beats, beat or rhythm, a new finger on each beat', color: '#e4572e' },""")
rep("""  { id: 'rnotes', name: 'Note values & rests', when: 'Splitting notes, rests, filling bars, the whole-bar rest', color: '#e4572e' },""",
    """  { id: 'rnotes', name: 'Note values & rests', when: 'Splitting notes, rests, filling bars, the whole-bar rest, counting it out loud', color: '#e4572e' },""")
rep("""  { id: 'rtime', name: 'Time signatures', when: 'What the two numbers mean, common and cut time, bar lines, the bottom number, counting along', color: '#e4572e' },""",
    """  { id: 'rtime', name: 'Time signatures', when: 'What the two numbers mean, common and cut time, bar lines, the bottom number, counting along, strong and weak beats', color: '#e4572e' },""")
rep("""  rpulse: ['박과 세기', '일정한 박, 맞는 박에 두드리기, 소리 내어 세기'],
  rnotes: ['음표 길이와 쉼표', '음표 나누기, 쉼표, 마디 채우기, 온마디 쉼표'],
  rtime: ['박자표', '두 숫자의 뜻, 보통박자와 얼라 브레베, 세로줄, 아래 숫자, 따라 세기'],""",
    """  rpulse: ['박과 세기', '꾸준한 박, 소리 내어 세기, 조용한 박, 박과 리듬, 박마다 다른 손가락'],
  rnotes: ['음표 길이와 쉼표', '음표 나누기, 쉼표, 마디 채우기, 온마디 쉼표, 소리 내어 세기'],
  rtime: ['박자표', '두 숫자의 뜻, 보통박자와 얼라 브레베, 세로줄, 아래 숫자, 따라 세기, 강한 박과 약한 박'],""")
rep(""" ['finger-friends', 'finger-numbers'], ['accidental-cards', 'sharp-flat']].forEach(""",
    """ ['finger-friends', 'finger-numbers'], ['accidental-cards', 'sharp-flat'], ['count-ring', 'count-aloud'], ['silent-beats', 'beat-target'], ['finger-beat', 'finger-numbers']].forEach(""")
rep("""  'pulse': ['steady-beat', 'beat-or-rhythm', 'beat-groups', 'beat-target', 'count-aloud'],""",
    """  'pulse': ['steady-beat', 'count-ring', 'silent-beats', 'beat-or-rhythm', 'finger-beat'],""")
rep("""  'note-values': ['note-value-tree', 'rest-grouping', 'note-rest-match', 'split-it', 'beam-apples', 'dotted-notes', 'dot-lab', 'fix-the-bar', 'fill-bar', 'heard-bar'],""",
    """  'note-values': ['note-value-tree', 'rest-grouping', 'note-rest-match', 'split-it', 'beam-apples', 'dotted-notes', 'dot-lab', 'fix-the-bar', 'fill-bar', 'heard-bar', 'count-aloud'],""")
rep("""  'time-signatures': ['time-sig-numbers', 'count-along', 'common-cut', 'bar-lines', 'beat-doubler', 'regroup', 'grouping', 'duplets'],""",
    """  'time-signatures': ['time-sig-numbers', 'count-along', 'common-cut', 'bar-lines', 'beat-doubler', 'regroup', 'grouping', 'duplets', 'beat-groups', 'beat-target'],""")
rep("""  ['p2', 'beat', 'Crotchets: counts 1 2 3 4 out loud', ['count-aloud']],""", """  ['p2', 'beat', 'Crotchets: counts 1 2 3 4 out loud', ['count-ring', 'count-aloud']],""")
rep("""  ['p4', 'beat', 'Taps only on the beat asked for', ['beat-target']],""", """  ['p4', 'beat', 'Taps only on the beat asked for', ['silent-beats', 'beat-target']],""")

# 5. strong and weak beats (B4) and 'tap the right beat' at the end of the Time signatures lesson; counting out loud
# with 1 and 2 at the end of the Notes and rests lesson (both lessons get their own Lesson Books later)
rep("""      <Step title={t('Duplets, triplets and more', '듀플릿, 셋잇단음표, 그 이상')}>
      <DupletDemo/>
      </Step>
    </Lesson>""", """      <Step title={t('Duplets, triplets and more', '듀플릿, 셋잇단음표, 그 이상')}>
      <DupletDemo/>
      </Step>
      <Step title={t('Strong and weak beats', '강한 박과 약한 박')}>
      <BeatGroups/>
      </Step>
      <Step title={t('Tap the right beat', '맞는 박에 치기')}>
      <ExplPulse1/>
      <BeatTarget/>
      </Step>
    </Lesson>""")
rep("""      <Step title={t('Which bar did you hear?', '어떤 마디를 들었을까요?')}>
      <HeardBar/>
      </Step>
      </Lesson>""", """      <Step title={t('Which bar did you hear?', '어떤 마디를 들었을까요?')}>
      <HeardBar/>
      </Step>
      <Step title={t('Count it out loud', '소리 내어 세기')}>
      <ExplPulse2/>
      <CountAloud/>
      </Step>
      </Lesson>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
