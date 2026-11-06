// items for the dash rewrite: every string / JSX text / template piece with a reader-visible double dash
const fs = require('fs'); const parser = require('/home/claude/pbtest/node_modules/@babel/parser');
const h = fs.readFileSync(process.argv[2], 'utf8'); const open = '<script id="app-jsx" type="text/jsx-raw">';
const base = h.indexOf(open) + open.length, j = h.indexOf('</script>', base); const src = h.slice(base, j);
const ast = parser.parse(src, { sourceType: 'script', plugins: ['jsx'] });
const items = [];
(function walk(n) { if (!n || typeof n.type !== 'string') return;
  for (const k in n) { if (['loc', 'leadingComments', 'trailingComments', 'innerComments', 'extra'].includes(k)) continue; const v = n[k];
    if (Array.isArray(v)) v.forEach(x => x && typeof x.type === 'string' && walk(x)); else if (v && typeof v.type === 'string') walk(v); }
  let val = null; if (n.type === 'StringLiteral' || n.type === 'JSXText') val = n.value; else if (n.type === 'TemplateElement') val = n.value.cooked;
  if (val != null && /(^|[^-])--([^->]|$)/.test(val) && /( --|-- )/.test(val)) items.push({ s: n.start, e: n.end, kind: n.type });
})(ast.program);
items.sort((a, b) => a.s - b.s);
const out = items.map((it, k) => { const ls = src.lastIndexOf('\n', it.s) + 1, le = src.indexOf('\n', it.e); const line = src.slice(ls, le < 0 ? src.length : le);
  const pre = src.slice(Math.max(ls, it.s - 260), it.s), post = src.slice(it.e, Math.min(le < 0 ? src.length : le, it.e + 260));
  return { id: k, kind: it.kind, s: base + it.s, e: base + it.e, raw: h.slice(base + it.s, base + it.e), before: pre, after: post }; });
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(out.length, 'items');
