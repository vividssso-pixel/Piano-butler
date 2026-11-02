// Engraved rhythm snippets with counts placed on the beat: onset count (coral) under the note, held counts (soft) at their beats, joined by dashes.
import createVerovioModule from 'verovio/wasm';
import { VerovioToolkit } from 'verovio/esm';
import fs from 'fs';
const M = await createVerovioModule(); const tk = new VerovioToolkit(M);
const D = { b: 'breve', s: '1', m: '2', c: '4', q: '8', x: '16' };
const LEN = { b: 8, s: 4, m: 2, c: 1, q: 0.5, x: 0.25 };   // in crotchets
let id = 0, LOC = 0, STEM = 'up', SRC2 = null, TIES = [], pend = null, INFO = {};
function note(tok, tupScale) {
  if (tok === 'R') { id++; INFO['n' + id] = { len: 0, labels: [] }; return `<mRest xml:id="n${id}"/>`; }
  let [t, cnt] = tok.split('/'); let tie = ''; if (t.endsWith('~')) { tie = 'i'; t = t.slice(0, -1); }
  let rest = false; if (t[0] === 'r') { rest = true; t = t.slice(1); }
  let dots = 0; while (t.endsWith('.')) { dots++; t = t.slice(0, -1); }
  let len = LEN[t] * (dots === 1 ? 1.5 : dots === 2 ? 1.75 : 1) * tupScale;
  id++; const nid = 'n' + id; INFO[nid] = { len, labels: cnt ? cnt.split('_') : [] };
  const dd = dots ? ` dots="${dots}"` : '';
  if (!rest) { if (pend) { TIES.push([pend, nid]); INFO[nid].tied = true; pend = null; } if (tie) pend = nid; }
  if (rest) return `<rest xml:id="${nid}" dur="${D[t]}"${dd}/>`;
  return `<note xml:id="${nid}" dur="${D[t]}"${dd} loc="${LOC}" stem.dir="${STEM}"/>`;
}
function layer(bar) {
  let out = '', sc = 1;
  for (const t of bar.trim().split(/\s+/).filter(Boolean)) {
    if (t === '[') { out += '<beam>'; continue; } if (t === ']') { out += '</beam>'; continue; }
    if (t === '{') { out += '<tuplet num="3" numbase="2" num.visible="true" bracket.visible="false"><beam>'; sc = 2 / 3; continue; } if (t === '}') { out += '</beam></tuplet>'; sc = 1; continue; }
    if (t === '(') { out += '<tuplet num="2" numbase="3" num.visible="true" bracket.visible="false"><beam>'; sc = 3 / 2; continue; } if (t === ')') { out += '</beam></tuplet>'; sc = 1; continue; }
    if (t === '<') { out += '<tuplet num="3" numbase="2" num.visible="true" bracket.visible="true">'; sc = 2 / 3; continue; } if (t === '>') { out += '</tuplet>'; sc = 1; continue; }
    out += note(t, sc);
  }
  return out;
}
function mei(src, meter, lines) {
  const bars = src.split('|'); let ms = '';
  const bars2 = SRC2 ? SRC2.split('|') : null;
  bars.forEach((b, i) => { let l1, l2 = '';
    if (bars2) { LOC = 1; STEM = 'up'; l1 = layer(b); LOC = -1; STEM = 'down'; l2 = `<layer n="2">${layer(bars2[i])}</layer>`; LOC = 0; STEM = 'up'; } else l1 = layer(b);
    ms += `<measure n="${i + 1}"${i === bars.length - 1 ? ' right="end"' : ''}><staff n="1"><layer n="1">${l1}</layer>${l2}</staff></measure>`; });
  const tieXml = TIES.map(([a, b]) => `<tie startid="#${a}" endid="#${b}"/>`).join('');
  if (tieXml) ms = ms.replace(/<\/staff>/, '</staff>' + tieXml);
  TIES = []; pend = null;
  const m = meter ? (meter === 'C' ? ' meter.sym="common"' : meter === 'C|' ? ' meter.sym="cut"' : ` meter.count="${meter.split('/')[0]}" meter.unit="${meter.split('/')[1]}"`) : '';
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef><staffGrp><staffDef n="1" lines="${lines}" clef.shape="perc" clef.line="1" clef.visible="false"${m}/></staffGrp></scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
}
const ON = '#e4572e', HELD = '#9a9cc4';
function addCounts(svg) {
  // events in order: notes/rests (id n#) with their glyph x, and bar lines
  const ev = []; let m;
  const re = /<g id="(n\d+)" class="(note|rest|mRest)"[\s\S]*?<use xlink:href="#[^"]+" x="(\d+)" y="(\d+)" height="(\d+)px" width="(\d+)px"|<g id="[^"]+" class="barLine"[^>]*>\s*<path d="M(\d+) /g;
  while ((m = re.exec(svg))) {
    if (m[1]) ev.push({ id: m[1], x: +m[3], w: +m[6] }); else ev.push({ bar: true, x: +m[7] });
  }
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  const HW = 212 * (ev.find(e => !e.bar) || { w: 720 }).w / 720;   // a black notehead's width
  // pixels per crotchet: median over notes followed directly by a note
  const per = []; ev.forEach((e, i) => { const n = ev[i + 1]; if (!e.bar && n && !n.bar && INFO[e.id].len) per.push((n.x - e.x) / INFO[e.id].len); });
  per.sort((a, b) => a - b); const U = per.length ? per[Math.floor(per.length / 2)] : 600;
  let out = ''; const Y = sy + (SRC2 ? 980 : 640), FS = 300; let lastX = null;
  ev.forEach(e => { if (e.bar) return; const inf = INFO[e.id]; if (!inf.labels.length) return;
    const x0 = e.x + HW / 2, step = inf.len * U / inf.labels.length;
    inf.labels.forEach((l, k) => { const x = x0 + k * step; const held = k > 0 || inf.tied;
      if (k === 0 && inf.tied && lastX != null) { const xa = lastX + 150, xb = x - 150; if (xb > xa) out += `<line x1="${xa.toFixed(0)}" x2="${xb.toFixed(0)}" y1="${Y - 95}" y2="${Y - 95}" stroke="${HELD}" stroke-width="26" stroke-linecap="round"/>`; }
      lastX = x;
      out += `<text x="${x.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${held ? HELD : ON}" class="cnt">${l.replace('&', '&amp;')}</text>`;
      if (k > 0) { const xa = x0 + (k - 1) * step + 150, xb = x - 150; if (xb > xa) out += `<line x1="${xa.toFixed(0)}" x2="${xb.toFixed(0)}" y1="${Y - 95}" y2="${Y - 95}" stroke="${HELD}" stroke-width="26" stroke-linecap="round"/>`; }
    });
  });
  // put the counts in the same group as the music (inside the page-margin group)
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${out}`);
}
const S = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')); const out = {};
for (const [k, v] of Object.entries(S)) {
  INFO = {}; id = 0; LOC = (v.lines ?? 1) === 5 ? 4 : 0; SRC2 = v.src2 || null;
  tk.setOptions({ pageWidth: v.w || 2000, adjustPageHeight: true, adjustPageWidth: true, scale: 50, header: 'none', footer: 'none', svgViewBox: true, pageMarginTop: 10, pageMarginBottom: 60, pageMarginLeft: 10, pageMarginRight: 30, breaks: 'none', spacingLinear: v.sp ?? 0.05, spacingNonLinear: 1.0, font: 'Leipzig' });
  tk.loadData(mei(v.src, v.meter || '', v.lines ?? 1));
  out[k] = addCounts(tk.renderToSVG(1));
}
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(Object.keys(out).length);
