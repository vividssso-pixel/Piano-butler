const fs = require('fs'); const parser = require('/home/claude/pbtest/node_modules/@babel/parser');
const h = fs.readFileSync(process.argv[2], 'utf8'); const open = '<script id="app-jsx" type="text/jsx-raw">';
const base = h.indexOf(open) + open.length, j = h.indexOf('</script>', base); const src = h.slice(base, j);
const ast = parser.parse(src, { sourceType: 'script', plugins: ['jsx'] });
const re = [], left = [];
(function walk(n) { if (!n || typeof n.type !== 'string') return;
  for (const k in n) { if (['loc', 'leadingComments', 'trailingComments', 'innerComments', 'extra'].includes(k)) continue; const v = n[k];
    if (Array.isArray(v)) v.forEach(x => x && typeof x.type === 'string' && walk(x)); else if (v && typeof v.type === 'string') walk(v); }
  if (n.type === 'RegExpLiteral' && /--/.test(n.pattern)) re.push(src.slice(n.start, n.end) + '   @' + src.slice(0, n.start).split('\n').length);
  let val = null; if (n.type === 'StringLiteral' || n.type === 'JSXText') val = n.value; else if (n.type === 'TemplateElement') val = n.value.cooked;
  if (val != null && /( --|-- )/.test(val)) left.push(JSON.stringify(val).slice(0, 100) + '   @' + src.slice(0, n.start).split('\n').length);
})(ast.program);
console.log('regex with --:', re.length); re.forEach(x => console.log('  ' + x.slice(0, 160)));
console.log('strings with --:', left.length); left.forEach(x => console.log('  ' + x));
