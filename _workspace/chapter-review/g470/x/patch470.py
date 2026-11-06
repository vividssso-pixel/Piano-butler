#!/usr/bin/env python3
# Phase 470 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15): chapter 14, Rhythm
# Patterns, built in full: the Lesson Book (dictionary entries), its screen lesson (the book with what moves on pages 2 to
# 6), a 9-level drill, the Workbook and the Teacher copy.
#   srhbook470.jsx: the rhythm row (srhRaw, SrhStaff: every note on G, the hearts and the count), the Lesson Book
#   srhapp470.jsx:  the sound (srhRun), the pads of pages 2 to 6, SrhLearn, the drill (Object.assign on RHYTHM_DRILL)
#   srhwb470.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 469 (chapter 10's sdyCircle and sdyCol, chapter 11's sskRowN, chapter 12's sprTick are used).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['srhbook470.jsx', 'srhapp470.jsx', 'srhwb470.jsx'])

# 1. the new code before the Lesson Book registry; rhythm joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("tempo: TempoLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", rhythm: RhythmLessonBook };") + s[j:]
rep("'pitch-range': sprLbPages, tempo: stmLbPages };", "'pitch-range': sprLbPages, tempo: stmLbPages, rhythm: srhLbPages };")

# 2. the toolbox: this room's moving parts first
rep("  { id: 'beam-apples', ch: 'rhythm',", """  { id: 'srh-beams', ch: 'rhythm', title: 'Grouping quavers', blurb: 'Two quavers on a beat, four on half a 4/4 bar: listen, then tap them.', C: () => <SrhPad page={2}/> },
  { id: 'srh-alone', ch: 'rhythm', title: 'A quaver alone', blurb: 'The flag and the quaver rest: rest, then play on the +.', C: () => <SrhPad page={3}/> },
  { id: 'srh-dot', ch: 'rhythm', title: 'The dotted crotchet', blurb: 'Long, short: 1 2 +. Listen, then tap it and hold.', C: () => <SrhPad page={4}/> },
  { id: 'srh-up', ch: 'rhythm', title: 'Before beat 1', blurb: 'Count in, count the missing beats, then start: the anacrusis.', C: () => <SrhPad page={5}/> },
  { id: 'srh-read', ch: 'rhythm', title: 'Count, clap, play', blurb: 'New lines: find the count, say it, then tap them.', C: () => <SrhPad page={6}/> },
  { id: 'beam-apples', ch: 'rhythm',""")
rep("  'beam-apples': ['한 박 = 사과 하나 (빔)',", """  'srh-beams': ['8분음표 묶기', '한 박에 8분음표 둘, 4/4의 반 마디에 넷: 듣고, 쳐 봐요.'],
  'srh-alone': ['혼자 있는 8분음표', '꼬리와 8분쉼표: 쉬었다가 +에서 쳐요.'],
  'srh-dot': ['점4분음표', '길게, 짧게: 1 2 +. 듣고, 길이만큼 누르며 쳐 봐요.'],
  'srh-up': ['첫 박보다 먼저', '한 마디를 미리 세고 모자란 박도 센 다음 시작해요: 여린내기.'],
  'srh-read': ['세기, 손뼉 치기, 피아노 치기', '새 줄을 소리 내어 센 다음 쳐 봐요.'],
  'beam-apples': ['한 박 = 사과 하나 (빔)',""")
rep("  'stm-sf': ['rtempo', 0, 1, 'game ear'],", "  'srh-beams': ['rrhythm', 1, 2, 'game ear'], 'srh-alone': ['rrhythm', 1, 2, 'game ear'], 'srh-dot': ['rrhythm', 1, 2, 'game ear'], 'srh-up': ['rrhythm', 1, 2, 'game ear'], 'srh-read': ['rrhythm', 1, 2, 'game ear home'],\n  'stm-sf': ['rtempo', 0, 1, 'game ear'],")
rep("['stm-steady', 'tap-tempo'],", "['stm-steady', 'tap-tempo'], ['srh-beams', 'grouping'], ['srh-alone', 'beam-apples'], ['srh-dot', 'dot-lab'], ['srh-up', 'anacrusis'], ['srh-read', 'rhythm-cards-all'],")
rep("  'rhythm': ['rhythm-cards-all', 'count-more', 'anacrusis', 'make-card', 'beam-apples', 'dotted-notes', 'dot-lab', 'grouping', 'duplets', 'regroup'],", "  'rhythm': ['srh-beams', 'srh-alone', 'srh-dot', 'srh-up', 'srh-read', 'rhythm-cards-all', 'count-more', 'anacrusis', 'make-card', 'beam-apples', 'dotted-notes', 'dot-lab', 'grouping', 'duplets', 'regroup'],")
# 3. shared fixes the reviewers found (Phase 470):
#  - the drill's Korean answer line read '정답은 1½박' (no copula) in every chapter: '정답: …'
rep("t('it was ' + drill.answerLabel(q), '정답은 ' + drill.answerLabel(q))", "t('it was ' + drill.answerLabel(q), '정답: ' + drill.answerLabel(q))")
#  - chapter 5's tap pad and tap levels: a note still held when the line ends stops with it; once answered (or out of
#    time) a run can no longer answer again
rep("""    T.at(r, r.at[4] + n * r.spb + 0.05, () => {
      setLit(-1); setPhase('done');""", """    T.at(r, r.at[4] + n * r.spb + 0.05, () => {
      if (held.current) { held.current(); held.current = null; }
      setLit(-1); setPhase('done');""")
rep("""      T.at(r, r.at[4] + n * r.spb + 0.05, () => {
        setPhase('scoring'); setLit(-1);""", """      T.at(r, r.at[4] + n * r.spb + 0.05, () => {
        if (held.current) { held.current(); held.current = null; }
        setPhase('scoring'); setLit(-1);""")
rep("""  useEffect(() => { T.clear(); stopClicks(); setPhase('ready'); setLit(-1); setGrow({}); taps.current = []; }, [q.uid]);""",
"""  useEffect(() => { T.clear(); stopClicks(); setPhase('ready'); setLit(-1); setGrow({}); taps.current = []; }, [q.uid]);
  useEffect(() => { if (given) { T.clear(); if (held.current) { held.current(); held.current = null; } } }, [given]);""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
