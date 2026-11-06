// Apply the chapter 3 Lesson Book DRAFT (nn396.jsx) to a copy of drills.src.html and compile it.
// The real source is untouched: the draft lives only in the draft build until Sohyun's answers.
//   node applynn396.js <drills.src.html> <out.html>
const fs = require('fs'), path = require('path'), cp = require('child_process');
const src = process.argv[2], out = process.argv[3];
let s = fs.readFileSync(src, 'utf8');
const jsx = fs.readFileSync(path.join(__dirname, 'nn396.jsx'), 'utf8');
function rep(a, b, what) { const n = s.split(a).length - 1; if (n !== 1) throw new Error(what + ': expected 1 match, got ' + n); s = s.replace(a, () => b); }
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };",
    jsx + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook };",
    'lesson books');
// B1 answered (Phase 392): the name "The Musical Alphabet" is in drills.src.html itself now
// B7 (draft only): the proposed drill levels -- black keys move to Tones & Semitones, interval numbers to Intervals
rep(`  { n: 4, label: 'Black keys too (sharps & flats)', octaves: 2, black: true, dirs: ['key2name', 'name2key'], time: 7 },
  { n: 5, label: 'Letter steps · next letter up or down', octaves: 1, black: false, dirs: ['step'], time: 6 },
  { n: 6, label: 'Letter jumps · 3rds to octaves, up or down', octaves: 1, black: false, dirs: ['jump'], time: 8 },`,
  `  { n: 4, label: 'Next letter up or down', octaves: 1, black: false, dirs: ['step'], time: 6 },
  { n: 5, label: 'Skip a letter, up or down', octaves: 1, black: false, dirs: ['jump'], time: 8 },`, 'draft levels');
const tmp = out.replace(/\.html$/, '.src.html');
fs.writeFileSync(tmp, s);
cp.execFileSync('node', [path.join(__dirname, '..', 'precompile.js'), tmp, out], { stdio: 'inherit' });
console.log('draft build:', out);
