#!/usr/bin/env python3
# Phase 402: 26 chapters -- a new chapter 5, The Whole Staff ('whole-staff'), between Reading the Staff and Ledger Lines
# (Sohyun 2026-10-09, chapter 4 review: "five notes first, what grows from there goes later, in its own section"; the
# rhymes come later; flash cards and writing live in the drill). Chapter 4 now reads only the nine notes from the King's F
# to the Queen's G round middle C; the whole staff (her rhymes, the five landmarks, fast reading, writing) moves to
# chapter 5 as a shell -- the online lesson's own steps, unchanged -- until its review. Ledger Lines becomes chapter 6.
#   python3 patch402.py <drills.src.html>
import sys, json, re
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. chapter 4's online lesson: the name (a5) and only its own steps; the alto clef is out of the chapter (a2)
old_learn = s[s.index("function StaffLearn({ onStart }) {"):s.index("const STAFF_LEVELS = [")]
rep(old_learn, """function StaffLearn({ onStart }) {
  // Phase 402: the rhymes, the landmarks, flash cards and writing moved to chapter 5 (The Whole Staff); the alto clef is out
  return (
    <Lesson id="staff" title={t('Reading the Staff', '오선보 읽기')} intro={<>{t('The staff is a map of the keyboard: going up the staff is going right on the piano.', '오선보는 건반의 지도예요: 오선보에서 위로 올라가는 것은 피아노에서 오른쪽으로 가는 것과 같아요.')}</>} onStart={onStart}>
      <Step title={t('What is the staff?', '오선보란 무엇일까요?')}>
      <StaffBasics/>
      </Step>
      <Step title={t('Line, space, line, space', '줄, 칸, 줄, 칸')}>
      <ExplStaff2/>
      <StaffClimb/>
      </Step>
      <Step title={t('Two staves, two clefs', '두 개의 오선, 두 개의 음자리표')}>
      <ClefBasics/>
      <div style={{fontSize:15,fontWeight:800,margin:'14px 0 2px'}}>{t("Why they're called the G clef and the F clef", '왜 G음자리표와 F음자리표라고 부를까요')}</div>
      <ClefStory/>
      </Step>
      <Step title={t('Fold at middle C', '가운데 도에서 접기')}>
      <FoldStaff/>
      </Step>
    </Lesson>
  );
}

// ─── Chapter 5: The Whole Staff (Phase 402) ───
// Every note on both staves: the rhymes (Sohyun's own sentences), the five landmarks, fast reading and writing. For now
// the online lesson's former chapter-4 steps; its Lesson Book comes with its own chapter review.
function WholeStaffLearn({ onStart }) {
  return (
    <Lesson id="whole-staff" title={t('The Whole Staff', '오선 전체 읽기')} intro={<>{t('From the nine notes round middle C to every line and space on both staves.', '가운데 도 둘레의 아홉 음에서, 두 오선의 모든 줄과 칸으로.')}</>} onStart={onStart}>
      <Step title={t('The rhymes', '외우는 문장')}>
      <ExplStaff1/>
      <MnemonicStaff/>
      </Step>
      <Step title={t('Landmarks', '기준이 되는 음')}>
      <ExplStaff3/>
      <StaffExplorer/>
      <LandmarkHop/>
      </Step>
      <Step title={t('Fast flash cards', '빠른 플래시 카드')}>
      <ExplStaff4/>
      <FlashCards/>
      </Step>
      <Step title={t('Write them', '직접 써보기')}>
      <ExplStaff5/>
      <WriteTheNote/>
      </Step>
    </Lesson>
  );
}

""", 'staff learn')
# 2. the drills: chapter 4 = the nine notes; chapter 5 = the whole staff (no ledger lines but middle C's own)
rep("""const STAFF_LEVELS = [
  { n: 1, label: 'Treble clef notes',               kind: 'name', range: [29, 39], clef: 'treble', time: 7 },
  { n: 2, label: 'Bass clef notes',                 kind: 'name', range: [17, 27], clef: 'bass', time: 7 },
  { n: 3, label: 'Both clefs + ledger lines',        kind: 'name', range: null, clef: 'mixed', time: 8 },
  { n: 4, label: 'Find it on the keyboard (exact octave)', kind: 'key', range: [21, 41], clef: 'grand', time: 10 },
];""", """const STAFF_LEVELS = [   // Phase 402: the nine notes from the King's F to the Queen's G (her new levels come with the chapter-4 apply)
  { n: 1, label: "The Queen's five: C D E F G",      kind: 'name', range: [28, 32], clef: 'treble', time: 7 },
  { n: 2, label: "The King's five: F G A B C",       kind: 'name', range: [24, 28], clef: 'bass', time: 7 },
  { n: 3, label: 'Around middle C: both staves',     kind: 'name', range: [24, 32], clef: 'grand', time: 8 },
  { n: 4, label: 'Find it on the keys',              kind: 'key', range: [24, 32], clef: 'grand', time: 10 },
];
const WHOLE_STAFF_LEVELS = [   // Phase 402: chapter 5; notes beyond the staves wait for chapter 6 (Ledger Lines)
  { n: 1, label: 'Treble clef notes',                kind: 'name', range: [29, 39], clef: 'treble', time: 7 },
  { n: 2, label: 'Bass clef notes',                  kind: 'name', range: [17, 27], clef: 'bass', time: 7 },
  { n: 3, label: 'Both clefs',                       kind: 'name', ranges: { treble: [28, 39], bass: [17, 28] }, clef: 'mixed', time: 8 },
  { n: 4, label: 'Find it on the keyboard (exact octave)', kind: 'key', range: [21, 39], clef: 'grand', time: 10 },
];""", 'levels')
rep("""    if (lv.clef === 'mixed') { clef = Math.random() < 0.5 ? 'treble' : 'bass'; d = clef === 'treble' ? rnd(26, 42) : rnd(14, 30); }""",
    """    if (lv.clef === 'mixed') { clef = Math.random() < 0.5 ? 'treble' : 'bass'; d = lv.ranges ? rnd(...lv.ranges[clef]) : clef === 'treble' ? rnd(26, 42) : rnd(14, 30); }""", 'mixed ranges')
rep("""  Question: StaffQuestion, Learn: StaffLearn,
};
""", """  Question: StaffQuestion, Learn: StaffLearn,
};
const WHOLE_STAFF_DRILL = {
  id: 'whole-staff', label: 'The Whole Staff', levels: WHOLE_STAFF_LEVELS, generate: genStaffQuestion,
  check: STAFF_DRILL.check, answerLabel: STAFF_DRILL.answerLabel,
  Question: StaffQuestion, Learn: WholeStaffLearn,
};
""", 'drill')
rep("""  { id: 'staff', label: 'Reading the Staff', concept: STAFF_DRILL, track: 'pitch' },
""", """  { id: 'staff', label: 'Reading the Staff', concept: STAFF_DRILL, track: 'pitch' },
  { id: 'whole-staff', label: 'The Whole Staff', concept: WHOLE_STAFF_DRILL, track: 'pitch' },
""", 'DRILLS')
rep("""'staff': '오선보 읽기', 'reading-steps'""", """'staff': '오선보 읽기', 'whole-staff': '오선 전체 읽기', 'reading-steps'""", 'CHAPTER_KO')
# 3. the toolbox: the moved activities belong to chapter 5
for tid in ['rhymes', 'landmarks', 'flash-cards', 'landmark-hop', 'write-note']:
    rep("  { id: '%s', ch: 'staff'," % tid, "  { id: '%s', ch: 'whole-staff'," % tid, 'tool ' + tid)
rep("""  'staff': ['staff-basics', 'rhymes', 'clef-basics', 'clef-story', 'staff-climb', 'fold', 'landmarks', 'landmark-hop', 'flash-cards', 'write-note', 'alto-clef'],""",
    """  'staff': ['staff-basics', 'staff-climb', 'clef-basics', 'clef-story', 'fold', 'alto-clef'],
  'whole-staff': ['rhymes', 'landmarks', 'landmark-hop', 'flash-cards', 'write-note'],""", 'tool order')
# 4. the maps and lists that every chapter has
rep("""'note-names': 'Prelim', pulse:""", """'note-names': 'Prelim', 'whole-staff': 'Prelim–G1', pulse:""", 'grade')
rep("""  'staff': () => <StaffHero/>, 'reading-steps'""", """  'staff': () => <StaffHero/>, 'whole-staff': () => <StaffHero/>, 'reading-steps'""", 'hero')
rep("""'staff': 'pitch', 'reading-steps': 'steps',""", """'staff': 'pitch', 'whole-staff': 'pitch', 'reading-steps': 'steps',""", 'cat')
rep("""const CAT_CHAPTER_ORDER = { pitch: ['staff'],""", """const CAT_CHAPTER_ORDER = { pitch: ['staff', 'whole-staff'],""", 'cat order')
rep("""  'staff': 'staff stave clef treble bass alto space',
""", """  'staff': 'staff stave clef treble bass space grand staff middle c',
  'whole-staff': 'staff treble bass rhymes every good boy face all cows eat grass landmarks lines spaces',
""", 'keywords')
rep("""  { name: 'Preliminary', ids: ['staff', 'ledger-lines',""", """  { name: 'Preliminary', ids: ['staff', 'whole-staff', 'ledger-lines',""", 'syllabus')
rep("""  'staff': ['The staff', '오선'], 'ledger-lines'""", """  'staff': ['The staff', '오선'], 'whole-staff': ['Whole staff', '오선 전체'], 'ledger-lines'""", 'CH_SHORT')
# 5. the house: room pictures by chapter id (chapter numbers move), and a room for chapter 5
ORDER25 = ["posture-hands", "first-steps", "note-names", "staff", "ledger-lines", "tones", "pulse", "note-values", "time-signatures", "rhythm", "reading-steps", "tempo", "intervals", "scales", "key-signatures", "chords", "melody", "form", "dynamics", "signs", "terms", "piano-story", "composers", "pitch-range", "styles"]
m = re.search(r'^const HOUSE_ICONS = (\{.*?\});(   // .*)$', s, re.M)
icons = json.loads(m.group(1))
assert sorted(icons, key=int) == [str(i) for i in range(1, 26)]
new = {}
for k in range(1, 26):
    new[ORDER25[k - 1]] = icons[str(k)]
    if ORDER25[k - 1] == 'staff':
        # the whole staff: a grand staff with a brace, notes on both staves
        new['whole-staff'] = ('<path d="M9 3 H44 M9 5.8 H44 M9 8.6 H44 M9 11.4 H44 M9 14.2 H44 M9 19.8 H44 M9 22.6 H44 M9 25.4 H44 M9 28.2 H44 M9 31 H44" stroke-width="0.9"/>'
            '<path d="M9 3 V31" stroke-width="1.6"/><path d="M6 3 Q3 4 4 10 Q5 15.5 2.4 17 Q5 18.5 4 24 Q3 30 6 31" stroke-width="1.3"/>'
            '<ellipse cx="18" cy="12.8" rx="2.5" ry="1.8" transform="rotate(-20 18 12.8)" fill="#26296b" stroke="none"/>'
            '<ellipse cx="25" cy="8.6" rx="2.5" ry="1.8" transform="rotate(-20 25 8.6)" fill="#26296b" stroke="none"/>'
            '<ellipse cx="32" cy="4.4" rx="2.5" ry="1.8" transform="rotate(-20 32 4.4)" fill="#26296b" stroke="none"/>'
            '<ellipse cx="38" cy="26.8" rx="2.5" ry="1.8" transform="rotate(-20 38 26.8)" fill="#26296b" stroke="none"/>')
s = s[:m.start()] + 'const HOUSE_ICONS = ' + json.dumps(new, ensure_ascii=False) + ';   // the room pictures from the house design (48 x 34 each), by chapter id (Phase 402: by id, not number)' + s[m.end():]
rep("""    const ic = HOUSE_ICONS[num], k = wide""", """    const ic = HOUSE_ICONS[r.id], k = wide""", 'icon lookup')
rep("""  // the rooms' insides (in chapter order, so the buttons are met 1 to 25)""", """  // the rooms' insides (in chapter order, so the buttons are met 1 to 26)""", 'comment')
# 6. the chapter strip art (old-style printed lesson pages): the whole staff, its line and space letters
rep("""  // steps move to the very next note; skips jump over one
  'reading-steps': () => <g>""", """  // the whole staff (Phase 402): every line and space, with their letters
  'whole-staff': () => <g>
    <AClef/>
    {[66, 58, 50, 42, 34].map((y, i) => <ANote key={'l' + i} x={100 + i * 26} y={y} stem={0}/>)}
    {[62, 54, 46, 38].map((y, i) => <ANote key={'s' + i} x={240 + i * 24} y={y} c={ART_C} stem={0}/>)}
    <AText x={152} y={90} size={11} serif={false} weight={700}>E G B D F</AText>
    <AText x={276} y={90} size={11} c={ART_C} serif={false} weight={700}>F A C E</AText>
  </g>,
  // steps move to the very next note; skips jump over one
  'reading-steps': () => <g>""", 'art')
open(src, 'w', encoding='utf-8').write(s); print('patch402 ok')
