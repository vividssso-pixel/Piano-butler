// Apply the chapter 2 Lesson Book DRAFT (fs382.jsx) to a copy of drills.src.html and compile it.
// The real source is untouched: the draft lives only in a build file until Sohyun's ticks.
// Run from the repo root:
//   node _workspace/chapter-review/lessonbook/applyfs382.js drills.src.html _workspace/chapter-review/lessonbook/drills.fs382.html
const fs = require('fs'), path = require('path'), cp = require('child_process');
const src = process.argv[2] || 'drills.src.html';
const out = process.argv[3] || path.join(__dirname, 'drills.fs382.html');
let s = fs.readFileSync(src, 'utf8');
const jsx = fs.readFileSync(path.join(__dirname, 'fs382.jsx'), 'utf8');
function rep(a, b, what) { const n = s.split(a).length - 1; if (n !== 1) throw new Error(what + ': expected 1 match, got ' + n); s = s.replace(a, () => b); }
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook };",
    jsx + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };",
    'lesson books');
const tmp = out.replace(/\.html$/, '.src.html');
fs.writeFileSync(tmp, s);
cp.execFileSync('node', [path.join(process.cwd(), 'tools', 'precompile.js'), tmp, out], { stdio: 'inherit' });
console.log('draft build:', out, '(open ?book=lesson&ch=first-steps&draft=1)');
