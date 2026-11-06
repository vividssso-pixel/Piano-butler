// Which top-level declarations of street425.jsx can anything reach? Roots: names used by the rest of the app.
//   node prune428.js <street425.jsx> <built t425.src.html> [--write <out.jsx>]
const fs = require('fs'), path = require('path');
const parser = require(path.resolve(__dirname, '../node_modules/@babel/parser'));
const [file, built] = [process.argv[2], process.argv[3]], outAt = process.argv.indexOf('--write');
const code = fs.readFileSync(file, 'utf8'), app = fs.readFileSync(built, 'utf8');
const rest = app.split(code.slice(0, 400))[0] + (app.split(code.slice(-400))[1] || '');
if (rest.length > app.length - code.length + 10 || !app.includes(code.slice(0, 400))) throw new Error('block not found in the build');
const ast = parser.parse(code, { sourceType: 'script', plugins: ['jsx'] });
const decl = {};   // name -> node
ast.program.body.forEach(n => {
  if (n.type === 'FunctionDeclaration') decl[n.id.name] = n;
  else if (n.type === 'VariableDeclaration') n.declarations.forEach(d => { if (d.id.type === 'Identifier') decl[d.id.name] = n; else if (d.id.type === 'ObjectPattern') d.id.properties.forEach(p => { decl[p.value.name] = n; }); });
});
const names = Object.keys(decl), word = (s, nm) => new RegExp('(^|[^A-Za-z0-9_$.])' + nm.replace(/\$/g, '\\$') + '(?![A-Za-z0-9_$])').test(s);
const refs = {}; names.forEach(nm => { const src = code.slice(decl[nm].start, decl[nm].end); refs[nm] = names.filter(o => o !== nm && word(src, o)); });
const live = new Set(names.filter(nm => word(rest, nm))), queue = [...live];
while (queue.length) { const nm = queue.pop(); refs[nm].forEach(o => { if (!live.has(o)) { live.add(o); queue.push(o); } }); }
const dead = names.filter(nm => !live.has(nm));
console.log('roots', names.filter(nm => word(rest, nm)).join(' '));
console.log('dead', dead.length, dead.join(' '));
if (outAt > 0) {
  const nodes = [...new Set(dead.map(nm => decl[nm]))].filter(n => (n.type !== 'VariableDeclaration') || n.declarations.every(d => d.id.type === 'Identifier' && dead.includes(d.id.name)));
  // whole lines: from the comment lines right above a declaration to the end of its last line; overlapping cuts merge
  const lines = code.split('\n'), starts = []; let acc = 0; lines.forEach(l => { starts.push(acc); acc += l.length + 1; });
  const lineOf = (i) => { let lo = 0, hi = starts.length - 1; while (lo < hi) { const m = (lo + hi + 1) >> 1; if (starts[m] <= i) lo = m; else hi = m - 1; } return lo; };
  let cuts = nodes.map(n => { let a = lineOf(n.start), b = lineOf(n.end - 1); while (a > 0 && /^\s*\/\//.test(lines[a - 1])) a--; return [a, b]; }).sort((x, y) => x[0] - y[0]);
  const merged = []; cuts.forEach(c => { const l = merged[merged.length - 1]; if (l && c[0] <= l[1] + 1) l[1] = Math.max(l[1], c[1]); else merged.push([...c]); });
  const drop = new Set(); merged.forEach(([a, b]) => { for (let i = a; i <= b; i++) drop.add(i); });
  const out = lines.filter((_, i) => !drop.has(i)).join('\n');
  fs.writeFileSync(process.argv[outAt + 1], out); console.log('wrote', process.argv[outAt + 1], code.length, '->', out.length);
}
