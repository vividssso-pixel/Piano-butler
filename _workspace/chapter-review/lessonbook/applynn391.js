// Apply the chapter 3 Lesson Book DRAFT (nn391.jsx) to a copy of drills.src.html and compile it.
// The real source is untouched: the draft lives only in the draft build until Sohyun's answers.
//   node applynn391.js <drills.src.html> <out.html>
const fs = require('fs'), path = require('path'), cp = require('child_process');
const src = process.argv[2], out = process.argv[3];
let s = fs.readFileSync(src, 'utf8');
const jsx = fs.readFileSync(path.join(__dirname, 'nn391.jsx'), 'utf8');
function rep(a, b, what) { const n = s.split(a).length - 1; if (n !== 1) throw new Error(what + ': expected 1 match, got ' + n); s = s.replace(a, () => b); }
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };",
    jsx + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook };",
    'lesson books');
// B1 (draft only): the proposed chapter name, so the page heads match the opener
rep("{ id: 'note-names', label: 'Note Names', concept: NOTE_NAMES_DRILL, track: 'pitch' },",
    "{ id: 'note-names', label: 'The Musical Alphabet', concept: NOTE_NAMES_DRILL, track: 'pitch' },", 'name');
const tmp = out.replace(/\.html$/, '.src.html');
fs.writeFileSync(tmp, s);
cp.execFileSync('node', [path.join(__dirname, '..', 'precompile.js'), tmp, out], { stdio: 'inherit' });
console.log('draft build:', out);
