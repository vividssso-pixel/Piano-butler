#!/usr/bin/env python3
# Phase 460 (her 2026-10-13 20:57 '추천대로 가보자': B4-B13 as recommended): chapter 5, Notes & Rests, as a Lesson Book,
# its online lesson (the book on screen with what moves, B12), a 9-level drill (B10), a Workbook and a Teacher copy (B11).
#   nvbook460.jsx: the Lesson Book (Phase 458's draft v2 with B4, B5 applied and the live parts wired in)
#   nvapp460.jsx:  each page's rhythm pad, NvLearn, the drill (Object.assign on NOTEVAL_DRILL)
#   nvwb460.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Also (B9): rests on the staff, fix the bar, fill the bar and 'which bar did you hear?' move to Time signatures; dotted
# notes, the dot lab and 'one beat = one apple' (semiquavers) to Rhythm patterns; both lessons get those steps at the end.
# 'Count it out loud' counts 1 + 2 + (Book rule 12). The old note shapes learn the breve and double dots (drill level 9,
# Book rule 13). A drill level can have no printed worksheet (the tapped levels).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['nvbook460.jsx', 'nvapp460.jsx', 'nvwb460.jsx'])

# 1. the new code before the Lesson Book registry; note-values joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook, 'whole-staff': WholeStaffLessonBook, 'ledger-lines': LedgerLessonBook, tones: TonesLessonBook, pulse: PulseLessonBook };"
rep(a, add + a.replace("pulse: PulseLessonBook };", "pulse: PulseLessonBook, 'note-values': NotesRestsLessonBook };"))
rep("tones: tnLbPages, pulse: plLbPages };", "tones: tnLbPages, pulse: plLbPages, 'note-values': nvLbPages };")

# 2. the old note shapes: the breve and double dots (drill level 9)
rep("const NV_KO = { semibreve: '온', minim: '2분', crotchet: '4분', quaver: '8분', semiquaver: '16분', demisemiquaver: '32분' };",
    "const NV_KO = { breve: '겹온', semibreve: '온', minim: '2분', crotchet: '4분', quaver: '8분', semiquaver: '16분', demisemiquaver: '32분' };")
rep("""  const beats = v.base * (o.dot ? 1.5 : 1);
  const ukEn = (o.dot ? 'dotted ' : '') + v.id + (o.rest ? ' rest' : '');
  const us = (o.dot ? 'dotted ' : '') + v.us + (o.rest ? ' rest' : ' note');
  const ko = (o.dot ? '점' : '') + NV_KO[v.id] + (o.rest ? '쉼표' : '음표');""", """  const beats = v.base * (o.dd ? 1.75 : o.dot ? 1.5 : 1);   // dd (Phase 460): double-dotted
  const ukEn = (o.dd ? 'double-dotted ' : o.dot ? 'dotted ' : '') + v.id + (o.rest ? ' rest' : '');
  const us = (o.dd ? 'double-dotted ' : o.dot ? 'dotted ' : '') + v.us + (o.rest ? ' rest' : ' note');
  const ko = (o.dd ? '겹점' : o.dot ? '점' : '') + NV_KO[v.id] + (o.rest ? '쉼표' : '음표');""")
rep("return { key: (o.rest ? 'r:' : 'n:') + (o.dot ? '.' : '') + v.id, id: v.id, base: v.base, dot: !!o.dot, rest: !!o.rest, beats,",
    "return { key: (o.rest ? 'r:' : 'n:') + (o.dd ? '..' : o.dot ? '.' : '') + v.id, id: v.id, base: v.base, dot: !!o.dot || !!o.dd, dd: !!o.dd, rest: !!o.rest, beats,")
rep("""  if (d >= 4) return <g><line x1={cx - 12} y1="44" x2={cx + 12} y2="44" stroke={ink} strokeWidth="1.2"/><rect x={cx - 8} y="44" width="16" height="7" fill={ink}/></g>;""",
    """  if (d >= 8) return <g><line x1={cx - 10} y1="37" x2={cx + 10} y2="37" stroke={ink} strokeWidth="1.2"/><line x1={cx - 10} y1="51" x2={cx + 10} y2="51" stroke={ink} strokeWidth="1.2"/><rect x={cx - 4} y="37" width="8" height="14" fill={ink}/></g>;   // the breve rest fills a space
  if (d >= 4) return <g><line x1={cx - 12} y1="44" x2={cx + 12} y2="44" stroke={ink} strokeWidth="1.2"/><rect x={cx - 8} y="44" width="16" height="7" fill={ink}/></g>;""")
rep("function NoteShape({ base, dot, cx, ink, beamed }) {", "function NoteShape({ base, dot, dd, cx, ink, beamed }) {")
rep("""      {dot && <circle cx={cx + 14} cy={HEAD_Y - 2} r="2.6" fill={ink}/>}
    </g>""", """      {base >= 8 && <g stroke={ink} strokeWidth="1.6">{[-14.5, -12, 12, 14.5].map(dx => <line key={dx} x1={cx + dx} x2={cx + dx} y1={HEAD_Y - 8} y2={HEAD_Y + 8}/>)}</g>}
      {dot && <circle cx={cx + (base >= 8 ? 19 : 14)} cy={HEAD_Y - 2} r="2.6" fill={ink}/>}
      {dd && <circle cx={cx + (base >= 8 ? 26 : 21)} cy={HEAD_Y - 2} r="2.6" fill={ink}/>}
    </g>""")
rep(": <NoteShape base={item.base} dot={item.dot} cx={w / 2 - (item.dot ? 5 : 2)} ink={ink}/>}",
    ": <NoteShape base={item.base} dot={item.dot} dd={item.dd} cx={w / 2 - (item.dd ? 8 : item.dot ? 5 : 2)} ink={ink}/>}")

# 3. a level of its own can have no printed worksheet (the tapped levels)
rep("{T && st.tab === 'drill' && !concept.noPrint && <PrintLink drillId={active.id} level={level} />}",
    "{T && st.tab === 'drill' && !concept.noPrint && !(concept.levels.find(l => l.n === level) || {}).noPrint && <PrintLink drillId={active.id} level={level} />}")
rep("  if (!concept || concept.noPrint) {\n", "  if (!concept || concept.noPrint || (lv && lv.noPrint)) {\n")

# 4. the toolbox: this room's tools are the book's moving parts (and the old reference tools); B9's moves
rep("""  { id: 'count-aloud', ch: 'note-values', title: 'Count it out loud', blurb: '1 2 3 4, or 1 and 2 and: lights up as the bar plays.', C: () => <><ExplPulse2/><CountAloud/></> },""",
    """  { id: 'count-aloud', ch: 'note-values', title: 'Count it out loud', blurb: '1 2 3 4, or 1 + 2 +: lights up as the bar plays.', C: () => <><ExplPulse2/><CountAloud/></> },
  { id: 'nv-walk', ch: 'note-values', title: 'Walk the crotchets', blurb: 'One beat each: listen, then tap them with the click.', C: () => <NvPad page={2}/> },
  { id: 'nv-hold', ch: 'note-values', title: 'Play, then hold', blurb: 'Minims last two beats: watch the sound line grow, then tap.', C: () => <NvPad page={3}/> },
  { id: 'nv-long', ch: 'note-values', title: 'Hold 3 beats, hold 4', blurb: 'The dotted minim and the semibreve, against the click.', C: () => <NvPad page={4}/> },
  { id: 'nv-run', ch: 'note-values', title: 'Walk and run', blurb: 'Two quavers on one beat: 1 + 2 +.', C: () => <NvPad page={5}/> },
  { id: 'nv-rests', ch: 'note-values', title: 'Count the silence', blurb: 'Tap the notes, not the rests, and keep counting.', C: () => <NvPad page={6}/> },""")
for tid in ['beam-apples', 'dot-lab', 'dotted-notes']:
    rep("  { id: '" + tid + "', ch: 'note-values',", "  { id: '" + tid + "', ch: 'rhythm',")
for tid in ['fix-the-bar', 'heard-bar', 'rest-grouping', 'fill-bar']:
    rep("  { id: '" + tid + "', ch: 'note-values',", "  { id: '" + tid + "', ch: 'time-signatures',")
rep("  'count-aloud': ['소리 내어 세기', '1 2 3 4, 또는 1 앤 2 앤: 마디가 연주되는 동안 불이 켜져요.'],",
    """  'count-aloud': ['소리 내어 세기', '1 2 3 4, 또는 1 + 2 +: 마디가 연주되는 동안 불이 켜져요.'],
  'nv-walk': ['4분음표 걷기', '한 박씩: 들어 보고, 클릭에 맞춰 쳐 봐요.'],
  'nv-hold': ['치고, 누르고 있어요', '2분음표는 두 박: 소리 줄이 자라는 걸 보고, 쳐 봐요.'],
  'nv-long': ['3박, 4박 누르기', '점2분음표와 온음표를 클릭에 맞춰요.'],
  'nv-run': ['걷고, 달려요', '한 박에 8분음표 둘: 1 + 2 +.'],
  'nv-rests': ['쉬면서 세요', '쉼표 말고 음을 치고, 계속 세요.'],""")
rep("'rest-grouping': ['rnotes', 2, 3, 'show']", "'rest-grouping': ['rtime', 2, 3, 'show']")
rep("'dotted-notes': ['rnotes', 1, 2, 'show']", "'dotted-notes': ['rrhythm', 1, 2, 'show']")
rep("'dot-lab': ['rnotes', 1, 2, 'show ear'], 'beam-apples': ['rnotes', 0, 1, 'show'], 'fix-the-bar': ['rnotes', 1, 2, 'game'], 'heard-bar': ['rnotes', 1, 2, 'ear game'],",
    "'dot-lab': ['rrhythm', 1, 2, 'show ear'], 'beam-apples': ['rrhythm', 0, 1, 'show'], 'fix-the-bar': ['rtime', 1, 2, 'game'], 'heard-bar': ['rtime', 1, 2, 'ear game'],")
rep("'split-it': ['rnotes', 1, 1, 'show'],", "'split-it': ['rnotes', 1, 1, 'show'], 'nv-walk': ['rnotes', 0, 1, 'game ear'], 'nv-hold': ['rnotes', 0, 1, 'game ear'], 'nv-long': ['rnotes', 0, 1, 'game ear'], 'nv-run': ['rnotes', 0, 1, 'game ear'], 'nv-rests': ['rnotes', 0, 1, 'game ear'],")
rep("'fill-bar': ['rnotes', 1, 2, 'game write home']", "'fill-bar': ['rtime', 1, 2, 'game write home']")
rep("""  { id: 'rnotes', name: 'Note values & rests', when: 'Splitting notes, rests, filling bars, the whole-bar rest, counting it out loud', color: '#e4572e' },
  { id: 'rtime', name: 'Time signatures', when: 'What the two numbers mean, common and cut time, bar lines, the bottom number, counting along, strong and weak beats', color: '#e4572e' },
  { id: 'rrhythm', name: 'Compound time & rhythm patterns', when: '6/8 and compound time, grouping quavers, duplets and triplets, rhythm cards, harder rhythms, anacrusis', color: '#e4572e' },""",
    """  { id: 'rnotes', name: 'Notes & rests', when: 'Crotchets, minims, dotted minims, semibreves, quaver pairs and their rests, counted out loud', color: '#e4572e' },
  { id: 'rtime', name: 'Time signatures', when: 'What the two numbers mean, common and cut time, bar lines, the bottom number, counting along, strong and weak beats, rests on the staff, filling bars', color: '#e4572e' },
  { id: 'rrhythm', name: 'Compound time & rhythm patterns', when: '6/8 and compound time, grouping quavers, duplets and triplets, rhythm cards, harder rhythms, anacrusis, dotted notes, semiquavers', color: '#e4572e' },""")
rep("""  rnotes: ['음표 길이와 쉼표', '음표 나누기, 쉼표, 마디 채우기, 온마디 쉼표, 소리 내어 세기'],
  rtime: ['박자표', '두 숫자의 뜻, 보통박자와 얼라 브레베, 세로줄, 아래 숫자, 따라 세기, 강한 박과 약한 박'],
  rrhythm: ['겹박자와 리듬 패턴', '6/8과 겹박자, 8분음표 묶기, 2잇단음표와 셋잇단음표, 리듬 카드, 어려운 리듬, 여린내기'],""",
    """  rnotes: ['음표와 쉼표', '4분음표, 2분음표, 점2분음표, 온음표, 8분음표 둘과 쉼표, 소리 내어 세기'],
  rtime: ['박자표', '두 숫자의 뜻, 보통박자와 얼라 브레베, 세로줄, 아래 숫자, 따라 세기, 강한 박과 약한 박, 오선 위의 쉼표, 마디 채우기'],
  rrhythm: ['겹박자와 리듬 패턴', '6/8과 겹박자, 8분음표 묶기, 2잇단음표와 셋잇단음표, 리듬 카드, 어려운 리듬, 여린내기, 점음표, 16분음표'],""")
rep(" ['finger-friends', 'finger-numbers'], ['accidental-cards', 'sharp-flat'],", " ['finger-friends', 'finger-numbers'], ['accidental-cards', 'sharp-flat'], ['nv-walk', 'count-aloud'], ['nv-hold', 'split-it'], ['nv-long', 'note-value-tree'], ['nv-run', 'beam-apples'], ['nv-rests', 'note-rest-naming'],")
rep("""  'note-values': ['note-value-tree', 'rest-grouping', 'note-rest-match', 'split-it', 'beam-apples', 'dotted-notes', 'dot-lab', 'fix-the-bar', 'fill-bar', 'heard-bar', 'count-aloud'],""",
    """  'note-values': ['nv-walk', 'nv-hold', 'nv-long', 'nv-run', 'nv-rests', 'count-aloud', 'note-value-tree', 'note-rest-match', 'split-it'],""")
rep("""  'rhythm': ['rhythm-cards-all', 'count-more', 'anacrusis', 'make-card'],""", """  'rhythm': ['rhythm-cards-all', 'count-more', 'anacrusis', 'make-card', 'beam-apples', 'dotted-notes', 'dot-lab'],""")
rep("""'regroup', 'grouping', 'duplets', 'beat-groups', 'beat-target'],""", """'regroup', 'grouping', 'duplets', 'beat-groups', 'beat-target', 'rest-grouping', 'fix-the-bar', 'fill-bar', 'heard-bar'],""")
rep("""  ['p3', 'beat', 'Minims, dotted minims, semibreves: keeps counting', ['count-aloud', 'split-it']],""", """  ['p3', 'beat', 'Minims, dotted minims, semibreves: keeps counting', ['nv-hold', 'nv-long']],""")
rep("""  ['p7', 'beat', 'Quavers: 1 & 2 &', ['count-aloud', 'beat-target']],""", """  ['p7', 'beat', 'Quavers: 1 + 2 +', ['nv-run', 'count-aloud']],""")
rep("""  ['cuts long notes short / doesn’t count rests', ['count-aloud', 'fill-bar', 'beat-target']],""", """  ['cuts long notes short / doesn’t count rests', ['nv-hold', 'nv-rests', 'count-aloud']],""")

# 5. the moved steps at the end of their new lessons (no other step links move)
rep("""      <Step title={t('Tap the right beat', '맞는 박에 치기')}>
      <ExplPulse1/>
      <BeatTarget/>
      </Step>
    </Lesson>""", """      <Step title={t('Tap the right beat', '맞는 박에 치기')}>
      <ExplPulse1/>
      <BeatTarget/>
      </Step>
      <Step title={t('Writing rests correctly', '쉼표를 올바르게 쓰기')}>
      <RestGrouping/>
      </Step>
      <Step title={t('Fix the bar', '마디 고치기')}>
      <FixTheBar/>
      </Step>
      <Step title={t('Fill the bar', '마디 채우기')}>
      <FillTheBar/>
      </Step>
      <Step title={t('Which bar did you hear?', '어떤 마디를 들었을까요?')}>
      <HeardBar/>
      </Step>
    </Lesson>""")
rep("""      <Step title={t('Make your own', '직접 만들어보기')}>
      <RhythmComposer/>
      </Step>
    </Lesson>""", """      <Step title={t('Make your own', '직접 만들어보기')}>
      <RhythmComposer/>
      </Step>
      <Step title={t('One beat = one apple', '한 박 = 사과 한 개')}>
      <BeamApples/>
      </Step>
      <Step title={t('Dotted notes', '점음표')}>
      <DottedNotesCard/>
      </Step>
      <Step title={t('Dot lab', '점 실험실')}>
      <DotLab/>
      </Step>
    </Lesson>""")

# 6. counting out loud: 1 + 2 + (Book rule 12; + is said 'and')
rep("""  const [ands, setAnds] = useState(false); // count "1 2 3 4", or "1 and 2 and\"""", """  const [ands, setAnds] = useState(false); // count "1 2 3 4", or "1 + 2 +" (said "and")""")
rep("""{t('Count it: ', '소리 내어 세기: ')}{useAnd ? t('1 and 2 and', '1 앤 2 앤') : '1 2 3 4'}""", """{t('Count it: ', '소리 내어 세기: ')}{useAnd ? '1 + 2 +' : '1 2 3 4'}""")
rep("""{[[false, '1 2 3 4'], [true, t('1 and 2 and', '1 앤 2 앤')]].map(""", """{[[false, '1 2 3 4'], [true, '1 + 2 +']].map(""")
rep("""{t('Quavers are half a beat, so they need the “and”: two quavers = “1 and”.', '8분음표는 반 박이라서 “앤”이 필요해요: 8분음표 두 개 = “1 앤”.')}""",
    """{t('Quavers are half a beat, so they need the +: two quavers = 1 +. Say + as “and”.', '8분음표는 반 박이라서 +가 필요해요: 8분음표 두 개 = 1 +. +는 “앤”이라고 읽어요.')}""")
rep("""{w === 'and' && LANG === 'ko' ? '앤' : w}""", """{w === 'and' ? '+' : w}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
