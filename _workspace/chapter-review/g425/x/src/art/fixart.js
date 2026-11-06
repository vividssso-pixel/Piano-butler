// Phase 425: the rabbit leaves chapter 1's pictures (the butler is a fox now, and only in his portrait):
// 'puppet' -- the string hangs from above instead of from the rabbit's rod; 'mirror' -- the brother and the sister
// face each other (whichever one is the reader, the other one calls the finger).
function topParts(v) {
  const i = v.indexOf('</defs>') + 7, out = []; let depth = 0, start = null;
  const re = /<(\/?)g\b[^>]*?>|<[a-z]+\b[^>]*\/>|<(path|text|line|rect|circle|ellipse|polyline|polygon)\b[^>]*>[\s\S]*?<\/\2>/g; re.lastIndex = i; let m;
  while ((m = re.exec(v))) {
    const tag = m[0], a = m.index, b = re.lastIndex;
    if (/^<g\b/.test(tag) && !tag.endsWith('/>')) { if (depth === 0) start = a; depth++; }
    else if (/^<\/g/.test(tag)) { depth--; if (depth === 0) out.push([start, b]); }
    else if (depth === 0) out.push([a, b]);
    if (v.startsWith('</svg>', b)) break;
  }
  return out;
}
function fixPuppet(v) {
  const P = topParts(v); if (P.length !== 9) throw new Error('puppet parts ' + P.length);
  const keep = P.filter((_, n) => ![1, 3, 4].includes(n)).map(([a, b]) => v.slice(a, b));
  if (!/^<g transform="translate\(-12.80 30.28\) scale\(0.86\)">/.test(v.slice(...P[1])) || !/^<path d="M81.8,82.2 Q111.9,26.0 142.0,40.0"/.test(v.slice(...P[3]))) throw new Error('puppet: not the rabbit');
  const head = v.slice(0, P[0][0]).replace('viewBox="0 0 270 214"', 'viewBox="44 0 226 214"');
  return head + keep.join('') + '<line x1="142" y1="2" x2="142" y2="40" stroke="#26296b" stroke-width="1.2" stroke-linecap="round"/>' + v.slice(P[8][1]);
}
function fixMirror(v) {
  const P = topParts(v); if (P.length !== 7) throw new Error('mirror parts ' + P.length);
  const part = n => v.slice(...P[n]);
  if (!/^<g transform="translate\(123.20 6.48\) scale\(0.76\)">/.test(part(3))) throw new Error('mirror: not the rabbit');
  const inner = s => s.slice(s.indexOf('>') + 1, s.lastIndexOf('</g>'));
  const flip = s => '<g transform="translate(240 0) scale(-1 1)">' + inner(s) + '</g>';
  // the one facing you is the other child: the sister when the reader is the brother (or not chosen), the brother when she is the reader
  const other = '<g data-who="boy">' + flip(part(1)) + '</g><g data-who="girl" display="none">' + flip(part(2)) + '</g>';
  const call = part(5).replace('font-size="9.5"', 'font-size="8.6"').replace('x="120"', 'x="114"');   // the call fits between the two children
  if (call === part(5)) throw new Error('mirror: the call');
  return v.slice(0, P[0][0]) + part(0) + part(1) + part(2) + other + part(4) + call + part(6) + v.slice(P[6][1]);
}
module.exports = { fixPuppet, fixMirror };
if (require.main === module) {
  const fs = require('fs'), d = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/';
  const p = fixPuppet(fs.readFileSync(d + 'puppet.svg', 'utf8')), m = fixMirror(fs.readFileSync(d + 'mirror.svg', 'utf8'));
  fs.writeFileSync('puppet.svg', p); fs.writeFileSync('mirror.svg', m);
  fs.writeFileSync('art.html', '<body style="margin:0;background:#fff"><div style="width:540px">' + p.replace('<svg ', '<svg width="540" ') + '</div><div style="width:540px">' + m.replace('<svg ', '<svg width="540" ') + '</div></body>');
  console.log('ok', p.length, m.length);
}
