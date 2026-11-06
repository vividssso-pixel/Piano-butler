// Apply the chapter 4 Lesson Book DRAFT (sf401.jsx) to a copy of drills.src.html and compile it (draft build only).
//   node applysf401.js <drills.src.html> <out.html>
const fs = require('fs'), path = require('path'), cp = require('child_process');
const src = process.argv[2], out = process.argv[3];
let s = fs.readFileSync(src, 'utf8');
const jsx = fs.readFileSync(path.join(__dirname, 'sf401.jsx'), 'utf8');
function rep(a, b, what) { const n = s.split(a).length - 1; if (n !== 1) throw new Error(what + ': expected 1 match, got ' + n); s = s.replace(a, () => b); }
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook };",
    jsx + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook, staff: StaffLessonBook };", 'lesson books');
// B6 (draft only): the proposed drill levels -- the labels show in the opener's drill strip; ledger-line notes move to chapter 5
rep(`const STAFF_LEVELS = [
  { n: 1, label: 'Treble clef notes',               kind: 'name', range: [29, 39], clef: 'treble', time: 7 },
  { n: 2, label: 'Bass clef notes',                 kind: 'name', range: [17, 27], clef: 'bass', time: 7 },
  { n: 3, label: 'Both clefs + ledger lines',        kind: 'name', range: null, clef: 'mixed', time: 8 },
  { n: 4, label: 'Find it on the keyboard (exact octave)', kind: 'key', range: [21, 41], clef: 'grand', time: 10 },
];`, `const STAFF_LEVELS = [
  { n: 1, label: 'Line or space?',                   kind: 'name', range: [30, 38], clef: 'treble', time: 7 },
  { n: 2, label: 'Step or skip, up or down?',        kind: 'name', range: [30, 38], clef: 'treble', time: 7 },
  { n: 3, label: 'Treble clef notes',                kind: 'name', range: [29, 39], clef: 'treble', time: 7 },
  { n: 4, label: 'Bass clef notes',                  kind: 'name', range: [17, 27], clef: 'bass', time: 7 },
  { n: 5, label: 'Both clefs and middle C',          kind: 'name', range: null, clef: 'mixed', time: 8 },
  { n: 6, label: 'Find it on the keys',              kind: 'key', range: [24, 32], clef: 'grand', time: 10 },
];`, 'draft levels');
const tmp = out.replace(/\.html$/, '.src.html');
fs.writeFileSync(tmp, s);
cp.execFileSync('node', [path.join(__dirname, '..', 'precompile.js'), tmp, out], { stdio: 'inherit' });
console.log('draft build:', out);
