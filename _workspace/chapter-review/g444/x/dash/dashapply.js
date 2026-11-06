const fs = require('fs'); const [, , inp, outp] = process.argv;
let h = fs.readFileSync(inp, 'utf8');
const items = JSON.parse(fs.readFileSync('/tmp/claude-0/dash/items.json', 'utf8'));
const out = {}; for (const f of fs.readdirSync('/tmp/claude-0/dash').filter(f => /^out_\d+\.json$/.test(f)).sort()) for (const a of JSON.parse(fs.readFileSync('/tmp/claude-0/dash/' + f, 'utf8'))) out[a.id] = a;
let n = 0;
for (const it of [...items].sort((a, b) => b.s - a.s)) {
  if (h.slice(it.s, it.e) !== it.raw) throw new Error('mismatch ' + it.id);
  const v = out[it.id]; if (v && v.raw != null) { h = h.slice(0, it.s) + v.raw + h.slice(it.e); n++; }
}
fs.writeFileSync(outp, h); console.log('applied', n);
