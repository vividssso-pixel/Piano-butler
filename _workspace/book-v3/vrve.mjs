// Pitched snippets on a real staff (treble, bass or grand), with labels under the notes.
// note token: c4  f#4  bb3  en5  c4:2 (minim)  c4/C (label)  ; '|' bar line ; chord: (c4.e4.g4)
import createVerovioModule from 'verovio/wasm';
import { VerovioToolkit } from 'verovio/esm';
import fs from 'fs';
const M = await createVerovioModule(); const tk = new VerovioToolkit(M);
let id = 0; let MEAS = {}; let CUR = 0;
const ACC = { '#': 's', 'b': 'f', 'n': 'n', 'x': 'x', 'bb': 'ff' };
function one(tok, dflt) {
  let [t, lab] = tok.split('/'); let dur = dflt; const explicit = t.includes(':');
  const arts = t.split('!'); t = arts.shift(); const art = arts.map(a => `<artic artic="${a}"/>`).join('');
  let grace = ''; if (/^g[a-g]/.test(t)) { grace = ' grace="unacc" stem.mod="1slash"'; t = t.slice(1); } else if (t[0] === 'G') { grace = ' grace="acc"'; t = t.slice(1); } if (t.includes(':')) [t, dur] = t.split(':'); let dots = ''; if (String(dur).endsWith('.')) { dur = dur.slice(0, -1); dots = ' dots="1"'; }   // c4:4. = dotted crotchet
  if (t === 'r') { id++; MEAS[id] = CUR; return `<rest xml:id="n${id}" dur="${dur}"/>`; }
  if (t === 's') { id++; return `<space xml:id="n${id}" dur="${dur}"/>`; }
  const chord = t.startsWith('(');
  const ps = chord ? t.slice(1, -1).split('.') : [t];
  const notes = ps.map(p => { const m = p.match(/^([a-g])(bb|#|b|n|x)?(\d)$/); id++; MEAS[id] = CUR; return `<note xml:id="n${id}" pname="${m[1]}" oct="${m[3]}"${m[2] ? ` accid="${ACC[m[2]]}"` : ''}${chord ? '' : ` dur="${grace && !explicit ? 8 : dur}"${dots}${grace}`}/>`; });
  if (!chord && art) notes[0] = notes[0].replace('/>', `>${art}</note>`).replace('></note>', '/>');
  const syl = lab ? `<verse n="1"><syl>${lab.replace(/_/g, ' ')}</syl></verse>` : '';
  if (chord) { notes[0] = notes[0].replace('/>', `>${syl}</note>`); return `<chord dur="${dur}">${notes.join('')}</chord>`; }
  if (notes[0].endsWith('</note>')) return syl ? notes[0].replace('</note>', `${syl}</note>`) : notes[0];
  return notes[0].replace('/>', `>${syl}</note>`);
}
function layer(src, dflt) { return src.trim().split(/\s+/).filter(Boolean).map(t => t === '[' ? '<beam>' : t === ']' ? '</beam>' : one(t, dflt)).join(''); }   // [ ] beam a group
function mei(v) {
  const dflt = v.dur || '1';
  const staves = v.clef === 'GF' ? [['G', 2, v.src], ['F', 4, v.src2 || '']] : [[v.clef || 'G', v.cline || (v.clef === 'F' ? 4 : 2), v.src]];
  const bars = staves.map(s => s[2].split('|'));
  const n = Math.max(...bars.map(b => b.length));
  let ms = '';
  const parts = [];
  for (let i = 0; i < n; i++) {
    CUR = i;
    parts.push(`<measure n="${i + 1}"${v.nobar ? ' right="invis"' : i === n - 1 ? ' right="end"' : ''}>` + staves.map((s, k) => `<staff n="${k + 1}"><layer n="1">${(bars[k][i] || '').trim() ? layer(bars[k][i], dflt) : `<space dur="1"/>`}</layer></staff>`).join(''));
  }
  const ctl = parts.map(() => '');
  const D = { dyn: (a, t) => `<dynam startid="#n${a}" place="below">${t}</dynam>`, hair: (a, b, f) => `<hairpin form="${f}" startid="#n${a}" endid="#n${b}" place="below"/>`,
    ferm: a => `<fermata startid="#n${a}"/>`, trill: a => `<trill startid="#n${a}"/>`, mord: (a, f) => `<mordent startid="#n${a}" form="${f || 'lower'}"/>`, turn: a => `<turn startid="#n${a}"/>`,
    ped: (a, d, f) => `<pedal startid="#n${a}" dir="${d}"${f ? ` form="${f}"` : ''}/>`, dir: (a, ...t) => `<dir startid="#n${a}" place="above"><rend fontstyle="italic">${t.join(' ')}</rend></dir>`,
    dirb: (a, ...t) => `<dir startid="#n${a}" place="below"><rend fontstyle="italic">${t.join(' ')}</rend></dir>`,
    slur: (a, b, c) => `<slur startid="#n${a}" endid="#n${b}" curvedir="${c || 'above'}"/>`, tie: (a, b) => `<tie startid="#n${a}" endid="#n${b}"/>`,
    tempo: (a, ...t) => `<tempo startid="#n${a}" place="above">${t.join(' ')}</tempo>` };
  for (const c of (v.ctl || [])) { const [k, a, ...r] = c.split(' '); ctl[MEAS[+a] || 0] += D[k](+a, ...r.map(x => isNaN(x) ? x.replace(/_/g, ' ') : +x)); }
  ms = parts.map((p, i) => p + ctl[i] + '</measure>').join('');
  if (false) ms = ms.replace('</measure>', (v.ties || []).map(([a, b]) => `<tie startid="#n${a}" endid="#n${b}"/>`).join('') + (v.slurs || []).map(([a, b]) => `<slur startid="#n${a}" endid="#n${b}" curvedir="${v.slurdir || 'below'}"/>`).join('') + '</measure>');   // one-bar snippets: ties and slurs by note number
  const key = v.key ? ` key.sig="${v.key}"` : '';
  const sd = staves.map((s, k) => `<staffDef n="${k + 1}" lines="5" clef.shape="${s[0]}" clef.line="${s[1]}"${key}${v.meter ? ` meter.count="${v.meter.split('/')[0]}" meter.unit="${v.meter.split('/')[1]}"` : ''}/>`).join('');
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef><staffGrp${staves.length > 1 && !v.nobrace ? ' symbol="brace" bar.thru="true"' : ''}>${sd}</staffGrp></scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
}
const S = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); const out = {};
for (const [k, v] of Object.entries(S)) {
  id = 0; MEAS = {};
  tk.setOptions({ pageWidth: v.w || 2100, adjustPageHeight: true, adjustPageWidth: true, scale: 50, header: 'none', footer: 'none', svgViewBox: true, pageMarginTop: 20, pageMarginBottom: 20, pageMarginLeft: v.clef === 'GF' ? 60 : 10, pageMarginRight: 30, breaks: 'none', spacingLinear: v.sp ?? 0.5, spacingNonLinear: 0.6, lyricSize: 4.2, lyricTopMinMargin: 4, font: 'Leipzig' });
  tk.loadData(mei(v));
  out[k] = tk.renderToSVG(1);
}
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(Object.keys(out).length);
