// Phase 405: APPLY chapter 4 (Reading the Staff) -- her go-ahead "f.1 응" (2026-10-09 22:41).
// The Lesson Book v4 goes into the app: the book on screen as the lesson, the 7 drill levels (3 new question kinds),
// a Workbook facing the book, a Teacher copy, and the royals' final designs everywhere (nnClara -> Clara A).
//   node patch405.js <drills.src.html>     (edits the file in place; run precompile after)
const fs = require('fs'), path = require('path');
const src = process.argv[2];
let s = fs.readFileSync(src, 'utf8');
const jsx = fs.readFileSync(path.join(__dirname, 'sf405.jsx'), 'utf8');
function rep(a, b, what) { const n = s.split(a).length - 1; if (n !== 1) throw new Error(what + ': expected 1 match, got ' + n); s = s.replace(a, () => b); }

// 1. Princess Clara's final design everywhere (chapter 3's houses, the resident icons, the Workbook cells)
const iCl = s.indexOf('function nnClara(cx, cy, k = 1) {');
const jCl = s.indexOf('function nnDog(cx, cy, k = 1) {');
if (iCl < 0 || jCl < iCl) throw new Error('nnClara block not found');
s = s.slice(0, iCl) + 'function nnClara(cx, cy, k = 1) { return sfClara(cx, cy, k); }   // Phase 405: Clara A (Royals-new-looks), drawn with the chapter-4 cast\n' + s.slice(jCl);

// 2. the old 4-step staff lesson goes; the new StaffLearn (the book on screen) is declared with the chapter-4 code
const iL = s.indexOf('function StaffLearn({ onStart }) {');
const jL = s.indexOf("// ─── Chapter 5: The Whole Staff (Phase 402) ───");
if (iL < 0 || jL < iL) throw new Error('StaffLearn block not found');
s = s.slice(0, iL) + '// Phase 405: StaffLearn is now the Lesson Book opened on screen -- declared beside the chapter-4 pages (sfLbPages).\n\n' + s.slice(jL);

// 3. chapter 5 keeps the fold (w4: folding belongs with the three Cs) -- a Fold step after Landmarks
rep(`      <Step title={t('Landmarks', '기준이 되는 음')}>
      <ExplStaff3/>
      <StaffExplorer/>
      <LandmarkHop/>
      </Step>`, `      <Step title={t('Landmarks', '기준이 되는 음')}>
      <ExplStaff3/>
      <StaffExplorer/>
      <LandmarkHop/>
      </Step>
      <Step title={t('Fold at middle C', '가운데 도에서 접기')}>
      <FoldStaff/>
      </Step>`, 'whole-staff fold step');

// 4. the drill: 7 levels, one idea at a time (her d3)
rep(`const STAFF_LEVELS = [   // Phase 402: the nine notes from the King's F to the Queen's G (her new levels come with the chapter-4 apply)
  { n: 1, label: "The Queen's five: C D E F G",      kind: 'name', range: [28, 32], clef: 'treble', time: 7 },
  { n: 2, label: "The King's five: F G A B C",       kind: 'name', range: [24, 28], clef: 'bass', time: 7 },
  { n: 3, label: 'Around middle C: both staves',     kind: 'name', range: [24, 32], clef: 'grand', time: 8 },
  { n: 4, label: 'Find it on the keys',              kind: 'key', range: [24, 32], clef: 'grand', time: 10 },
];`, `const STAFF_LEVELS = [   // Phase 405 (her d3): one idea per level, all within the nine notes round middle C
  { n: 1, label: 'Line or space?',                   kind: 'ls', range: [30, 38], clef: 'treble', time: 6 },
  { n: 2, label: 'Step or skip? Up or down?',        kind: 'ss', range: [30, 38], clef: 'treble', time: 8 },
  { n: 3, label: "The Queen's five: C D E F G",      kind: 'name', range: [28, 32], clef: 'treble', time: 7 },
  { n: 4, label: "The King's five: F G A B C",       kind: 'name', range: [24, 28], clef: 'bass', time: 7 },
  { n: 5, label: 'Around Clara: both staves',        kind: 'name', range: [24, 32], clef: 'grand', time: 8 },
  { n: 6, label: 'Write it: tap where it goes',      kind: 'write', range: [24, 32], clef: 'grand', time: 9 },
  { n: 7, label: 'Find it on the keys',              kind: 'key', range: [24, 32], clef: 'grand', time: 10 },
];`, 'staff levels');
rep(`function genStaffQuestion(lv, prev) {
  const uid = Math.random();
  let d, clef;
  const rnd = (a, b) => a + Math.floor(Math.random() * (b - a + 1));`, `function genStaffQuestion(lv, prev) {
  const uid = Math.random();
  const rnd = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  if (lv.kind === 'ls') {   // Phase 405: one note -- on a line, or in a space?
    let d; for (let n = 0; n < 12; n++) { d = rnd(lv.range[0], lv.range[1]); if (!prev || prev.d !== d) break; }
    return { kind: 'ls', key: 'ls' + d + uid, d, clef: lv.clef, staff: lv.clef, answer: (d - CLEFS[lv.clef].low) % 2 === 0 ? 'line' : 'space', uid };
  }
  if (lv.kind === 'ss') {   // Phase 405: two notes -- step or skip, up or down?
    let a, b;
    for (let n = 0; n < 24; n++) {
      a = rnd(lv.range[0], lv.range[1]);
      const gap = Math.random() < 0.5 ? 1 : 2, dir = Math.random() < 0.5 ? 1 : -1;
      b = a + gap * dir;
      if (b >= lv.range[0] && b <= lv.range[1] && !(prev && prev.a === a && prev.b === b)) break;
      b = null;
    }
    if (b == null) { a = lv.range[0]; b = a + 1; }
    return { kind: 'ss', key: 'ss' + a + '-' + b + uid, a, b, d: b, clef: lv.clef, staff: lv.clef, answer: (Math.abs(b - a) === 1 ? 'step' : 'skip') + '-' + (b > a ? 'up' : 'down'), uid };
  }
  if (lv.kind === 'write') {   // Phase 405: a letter -- tap the line or space where it goes (any octave counts)
    let d; for (let n = 0; n < 12; n++) { d = rnd(lv.range[0], lv.range[1]); if (!prev || dName(prev.d) !== dName(d)) break; }
    const staff = lv.clef === 'grand' ? (d > 28 ? 'treble' : d < 28 ? 'bass' : 'treble') : lv.clef;
    return { kind: 'write', key: 'w' + d + uid, d, clef: lv.clef, staff, answer: dName(d), uid };
  }
  let d, clef;`, 'gen kinds');
rep(`const STAFF_DRILL = {
  id: 'staff', label: 'Reading the Staff', levels: STAFF_LEVELS, generate: genStaffQuestion,
  check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer,
  answerLabel: (q) => withSolfa(dName(q.d)) + ' (' + dLabel(q.d) + (q.d === 28 ? t(', middle C', ', 가운데 도') : '') + ')',
  Question: StaffQuestion, Learn: StaffLearn,
};`, `const SF_SS_LABELS = () => ({ 'step-up': t('a step up', '한 걸음 위로'), 'step-down': t('a step down', '한 걸음 아래로'), 'skip-up': t('a skip up', '건너뛰기 위로'), 'skip-down': t('a skip down', '건너뛰기 아래로') });
const STAFF_DRILL = {
  id: 'staff', label: 'Reading the Staff', levels: STAFF_LEVELS, generate: genStaffQuestion,
  check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer,
  answerLabel: (q) => q.kind === 'ls' ? (q.answer === 'line' ? t('a line note', '줄 음표') : t('a space note', '칸 음표'))
    : q.kind === 'ss' ? SF_SS_LABELS()[q.answer]
    : q.kind === 'write' ? withSolfa(q.answer)
    : withSolfa(dName(q.d)) + ' (' + dLabel(q.d) + (q.d === 28 ? t(', middle C', ', 가운데 도') : '') + ')',
  Question: (props) => props.q.kind === 'ls' ? <SfLsQuestion {...props}/> : props.q.kind === 'ss' ? <SfSsQuestion {...props}/> : props.q.kind === 'write' ? <SfWriteQuestion {...props}/> : <StaffQuestion {...props}/>,
  Learn: StaffLearn,
};`, 'staff drill');

// 5. Korean names for the new level labels
rep(`const LEVEL_KO = {
`, `const LEVEL_KO = {
  'Line or space?': '줄일까, 칸일까?',
  'Step or skip? Up or down?': '한 걸음일까, 건너뛰기일까? 위로? 아래로?',
  "The Queen's five: C D E F G": '여왕의 다섯 음: C D E F G',
  "The King's five: F G A B C": '왕의 다섯 음: F G A B C',
  'Around Clara: both staves': '클라라 둘레: 두 오선',
  'Write it: tap where it goes': '직접 쓰기: 들어갈 자리를 탭',
  'Find it on the keys': '건반에서 찾기',
  'Around middle C: both staves': '가운데 도 둘레: 두 오선',
`, 'level ko');

// 6. the chapter-4 code itself, then the registries
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook };",
    jsx + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook };", 'lesson books');
rep("const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages };",
    "const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages, staff: sfLbPages };", 'lb page fns');
rep('const WORKBOOKS = { front: FrontMatter, staff: StaffWorkbook,', 'const WORKBOOKS = { front: FrontMatter, staff: SfWorkbook,', 'workbooks');
rep('const TEACHER_COPIES = { staff: StaffTeacher,', 'const TEACHER_COPIES = { staff: SfTeacher,', 'teacher copies');

// 7. the fold tool belongs to chapter 5 now (w4)
rep("  { id: 'fold', ch: 'staff', title: 'Fold at middle C (grand staff)', blurb: 'The treble and bass staves are mirror images.', C: () => <><ExplStaff3/><FoldStaff/></> },",
    "  { id: 'fold', ch: 'whole-staff', title: 'Fold at middle C (grand staff)', blurb: 'The treble and bass staves are mirror images.', C: () => <><ExplStaff3/><FoldStaff/></> },", 'fold tool');
rep("  'staff': ['staff-basics', 'staff-climb', 'clef-basics', 'clef-story', 'fold', 'alto-clef'],\n  'whole-staff': ['rhymes', 'landmarks', 'landmark-hop', 'flash-cards', 'write-note'],",
    "  'staff': ['staff-basics', 'staff-climb', 'clef-basics', 'clef-story', 'alto-clef'],\n  'whole-staff': ['rhymes', 'landmarks', 'landmark-hop', 'fold', 'flash-cards', 'write-note'],", 'tool order');

fs.writeFileSync(src, s);
console.log('patch405 ok');
