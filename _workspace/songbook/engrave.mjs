// Engrave one song's lesson snippets from its data: the tune with words, the rhythm with counts, and the four ways to play.
// Usage: node engrave.mjs song.json out.json
import createVerovioModule from 'verovio/wasm';
import { VerovioToolkit } from 'verovio/esm';
import fs from 'fs';
const M = await createVerovioModule(); const tk = new VerovioToolkit(M);
const S = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const DUR = { s: '1', m: '2', c: '4', q: '8' }, LEN = { s: 4, m: 2, c: 1, q: 0.5 };
let id = 0; const nid = () => 'x' + (++id);
const pn = (p) => [p[0], p.slice(1)];
// move a pitch up by letter steps (C to G is 4): the tune keeps its shape and its finger numbers; a chord letter moves the same way
const L7 = 'cdefgab', trp = (p, k) => { if (!k) return p; const i = L7.indexOf(p[0]) + k; return L7[i % 7] + (+p.slice(1) + Math.floor(i / 7)); };
const trChord = (c, k) => trp(c.toLowerCase() + '4', k)[0].toUpperCase();
function noteXml(p, d, o = {}) {
  const [pname, oct] = pn(p); const i = nid(); o.ids && o.ids.push(i);
  const syl = o.syl ? `<verse n="1"><syl${o.wp ? ` wordpos="${o.wp}" con="d"` : ''}>${o.syl}</syl></verse>` : '';
  const loc = o.loc != null ? ` loc="${o.loc}"` : '';
  return [i, o.rhythm ? `<note xml:id="${i}" dur="${DUR[d]}" loc="0" stem.dir="up">${syl}</note>` : `<note xml:id="${i}" dur="${DUR[d]}" pname="${pname}" oct="${oct}"${o.stem ? ` stem.dir="${o.stem}"` : ''}>${syl}</note>`];
}
function chordXml(ps, d, stem) { const i = nid(); return [i, `<chord xml:id="${i}" dur="${DUR[d]}"${stem ? ` stem.dir="${stem}"` : ''}>` + ps.map(p => { const [a, b] = pn(p); return `<note pname="${a}" oct="${b}"/>`; }).join('') + '</chord>']; }
// one line of bars [b0, b1): opts.words, opts.fing, opts.chords, opts.lh (a way), opts.rhythm (one-line staff), opts.meter
function mei(b0, b1, o) {
  let ms = '', ctrl = [];
  for (let b = b0; b < b1; b++) {
    const bar = S.bars[b]; let l1 = '';
    bar.forEach(([p, d, syl, wp]) => { const [i, x] = noteXml(trp(p, o.tr), d, { syl: o.words ? syl : '', wp: o.words ? wp : '', rhythm: o.rhythm }); l1 += x;
      if (o.fing) ctrl.push(`<fing startid="#${i}" place="above">${S.rh_finger[p]}</fing>`); INFO[i] = { len: LEN[d] }; });
    let st2 = '';
    if (o.lh) { const ch = S.chords[b], last = b === S.bars.length - 1, pat = (last && S.lh[o.lh].end) || S.lh[o.lh][ch]; let l2 = '';
      pat.forEach(([ps, d, f]) => { const [i, x] = ps.length > 1 ? chordXml(ps, d, 'up') : noteXml(ps[0], d, { stem: 'up' }); l2 += x; if (f !== '' && f != null) String(f).split(' ').reverse().forEach(ff => ctrl.push(`<fing startid="#${i}" place="below" staff="2">${ff}</fing>`)); });
      st2 = `<staff n="2"><layer n="1">${l2}</layer></staff>`; }
    if (o.chords) ctrl.push(`<harm staff="1" tstamp="1" place="above">${trChord(S.chords[b], o.tr)}</harm>`);
    const right = b === S.bars.length - 1 ? ' right="end"' : '';
    ms += `<measure n="${b + 1}"${right}><staff n="1"><layer n="1">${l1}</layer></staff>${st2}${ctrl.splice(0).join('')}</measure>`;
  }
  const met = (o.key ? ` keysig="${o.key}"` : '') + (o.meter ? ` meter.count="4" meter.unit="4"` : '');
  const sd = o.rhythm ? `<staffDef n="1" lines="1" clef.shape="perc" clef.line="1" clef.visible="false"${met}/>`
    : o.lh ? `<staffGrp symbol="brace" bar.thru="true"><staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/><staffDef n="2" lines="5" clef.shape="F" clef.line="4"${met}/></staffGrp>`
    : `<staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/>`;
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef>${o.rhythm || !o.lh ? `<staffGrp>${sd}</staffGrp>` : sd}</scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
}
let INFO = {};
// counts under the rhythm line: the beat a note starts on (coral), the beats it is held (grey, joined by a dash)
const ON = '#e4572e', HELD = '#9a9cc4';
function addCounts(svg) {
  const ev = []; let m; const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use xlink:href="#[^"]+" transform="translate\((\d+), (\d+)\)|<g id="[^"]+" class="barLine"[^>]*>\s*<path d="M(\d+) /g;
  while ((m = re.exec(svg))) { if (m[1]) ev.push({ id: m[1], x: +m[2] }); else ev.push({ bar: true, x: +m[4] }); }
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  const HW = 212;   // a black notehead (E0A4 at scale 0.72)
  const per = []; ev.forEach((e, i) => { const n = ev[i + 1]; if (!e.bar && n && !n.bar) per.push((n.x - e.x) / INFO[e.id].len); });
  per.sort((a, b) => a - b); const U = per[Math.floor(per.length / 2)];
  const sylY = [...svg.matchAll(/class="syl">\s*<text x="[\d.]+" y="(\d+)"/g)].map(m => +m[1]); let out = '', beat = 0; const Y = (sylY.length ? Math.max(...sylY) : sy + 640) + 420, FS = 300;
  ev.forEach((e, ei) => { if (e.bar) { beat = 0; return; } const L = INFO[e.id].len, x0 = e.x + HW / 2;
    const nx = (ev[ei + 1] || { x: x0 + L * U }).x, step = L > 1 ? Math.min(U, (nx - 120 - x0) / (L - 0.5)) : U;
    for (let k = 0; k < L; k++) { const x = x0 + k * step, held = k > 0;
      out += `<text x="${x.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${held ? HELD : ON}" class="cnt">${beat + k + 1}</text>`;
      if (held) { const xa = x - step + 150, xb = x - 150; if (xb > xa) out += `<line x1="${xa.toFixed(0)}" x2="${xb.toFixed(0)}" y1="${Y - 95}" y2="${Y - 95}" stroke="${HELD}" stroke-width="26" stroke-linecap="round"/>`; } }
    beat += L; });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${out}`);
}
function addBoxes(svg, ex) {
  const ev = []; let m; const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use xlink:href="#[^"]+" transform="translate\((\d+), (\d+)\)/g;
  while ((m = re.exec(svg))) ev.push(+m[2] + 106);
  // the boxes sit in a row of their own: below middle C's ledger line (top line + 4 spaces + a ledger + a head), or below
  // the words when the line has them
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  const sylY = [...svg.matchAll(/class="syl">\s*<text x="[\d.]+" y="(\d+)"/g)].map(m => +m[1]);
  const T = sylY.length ? Math.max(...sylY) + 160 : sy + 1110; let out = '';
  ev.forEach((x, k) => { out += `<rect x="${x - 190}" y="${T}" width="380" height="380" rx="40" fill="#fff" stroke="${k === 0 && ex ? '#e4572e' : '#26296b'}" stroke-width="22" class="wbox"/>`;
    if (k === 0 && ex) out += `<text x="${x}" y="${T + 295}" text-anchor="middle" font-size="290" font-weight="700" fill="#e4572e" class="cnt">${ex}</text>`; });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${out}`);
}
// A lead sheet's "when" row, under the staff: for each bar, the left hand's pattern for that bar's chord, placed on its beats.
// A single note shows its finger number (coral); two notes together show a coral dot; a note held past its beat runs on
// as a grey line to the end of its length.
function addWhen(svg, way, b0, pic, Y0) {
  const ev = []; let m; const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use xlink:href="#[^"]+" transform="translate\((\d+), (\d+)\)|<g id="[^"]+" class="barLine"[^>]*>\s*<path d="M(\d+) /g;
  while ((m = re.exec(svg))) { if (m[1]) ev.push({ id: m[1], x: +m[2] }); else ev.push({ bar: true, x: +m[4] }); }
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1], HW = 212, Y = Y0 || sy + 1330;
  // the x of every beat in every bar, from the notes' own onsets (a held note's later beats spaced evenly to the next event)
  const bars = [[]]; ev.forEach((e, i) => { if (e.bar) { bars.push([]); return; } const L = INFO[e.id].len, x0 = e.x + HW / 2, nx = (ev[i + 1] || { x: x0 + 600 }).x;
    const step = L > 1 ? (nx - 120 - x0) / (L - 0.5) : 0; for (let k = 0; k < L; k++) bars[bars.length - 1].push(x0 + k * step); });
  let out = '';
  bars.filter(b => b.length).forEach((bx, j) => { const b = b0 + j, last = b === S.bars.length - 1, pat = (last && S.lh[way].end) || S.lh[way][S.chords[b]]; let beat = 0;
    pat.forEach(([ps, d, f]) => { const L = LEN[d], x = bx[beat], xe = beat + L < bx.length ? bx[beat + L] - 130 : bx[bx.length - 1] + 330;
      if (ps.length > 1 && pic && f) {   // the chord's picture, first line only: its notes stacked, a third a head apart (so a
        // root-position triad's heads touch), a dashed ring where a note is still to come
        const st = ps.map(p => L7.indexOf(p[0]) + 7 * +p.slice(1)), lo = Math.min(...st), hi = Math.max(...st), D = 240;
        for (let k = lo; k <= hi; k += 2) { const cy = Y - 100 + (hi - k) / 2 * D, has = st.includes(k);   // the top note on the row, the rest below
          out += has ? `<circle cx="${x.toFixed(0)}" cy="${cy.toFixed(0)}" r="${D / 2}" fill="${ON}" class="when"/>`
                     : `<circle cx="${x.toFixed(0)}" cy="${cy.toFixed(0)}" r="${D / 2 - 12}" fill="#fff" stroke="${ON}" stroke-width="16" stroke-dasharray="34 26" class="when"/>`; } }
      else if (ps.length > 1) out += `<circle cx="${x.toFixed(0)}" cy="${Y - 100}" r="70" fill="${ON}" class="when"/>`;
      else out += `<text x="${x.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="290" font-weight="700" fill="${ON}" class="cnt when">${f}</text>`;
      if (L > 1) out += `<line x1="${(x + 140).toFixed(0)}" x2="${xe.toFixed(0)}" y1="${Y - 100}" y2="${Y - 100}" stroke="${HELD}" stroke-width="26" stroke-linecap="round"/>`;
      beat += L; }); });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${out}`);
}
// all the ways under one tune: a row each, numbered in the left margin; a row with chord pictures is taller
function addRows(svg, ways, b0, pic) {
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1]; let Y = sy + 1330, lab = '';
  ways.forEach(w => { svg = addWhen(svg, w, b0, pic, Y); const n = w.slice(3);
    lab += `<circle cx="230" cy="${Y - 100}" r="125" fill="#26296b" class="when"/><text x="230" y="${Y - 10}" text-anchor="middle" font-size="250" font-weight="700" fill="#fff" class="cnt">${n}</text>`;
    const tall = pic && Object.values(S.lh[w]).some(p => p.some(([ps]) => ps.length > 1));
    Y += tall ? 860 : 400; });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${lab}`);
}
const JOBS = {
  sing1: [0, 4, { words: 1, meter: 1, boxes: 1 }], sing2: [4, 8, { words: 1, boxes: 1, noEx: 1 }],
  rhy1: [0, 4, { words: 1, rhythm: 1, meter: 1, counts: 1, pw: 1350 }], rhy2: [4, 8, { words: 1, rhythm: 1, counts: 1, pw: 1350 }],   // bigger: the first thing a child reads
  play1: [0, 4, { fing: 1, chords: 1, meter: 1, rows: ['way2', 'way3', 'way4'] }],   // the tune once, every way under it
  play2: [4, 8, { fing: 1, chords: 1, rows: ['way2', 'way3', 'way4'] }],
  g1: [0, 4, { fing: 1, chords: 1, meter: 1, tr: 4, key: '1s' }], g2: [4, 8, { fing: 1, chords: 1, tr: 4, key: '1s' }],   // Move it: bars 1 to 4 in G, one sharp, the same fingers
};
const out = {};
for (const [k, [b0, b1, o]] of Object.entries(JOBS)) {
  INFO = {}; id = 0;
  tk.setOptions({ pageWidth: o.pw || 1750, adjustPageHeight: true, adjustPageWidth: false, scale: 50, header: 'none', footer: 'none', svgViewBox: true,
    pageMarginTop: 30, pageMarginBottom: o.rows ? 500 : o.counts || o.boxes ? 300 : 40, pageMarginLeft: 20, pageMarginRight: 20, breaks: 'none', spacingLinear: 0.25, spacingNonLinear: 0.6, font: 'Leipzig', lyricSize: 4.0, lyricTopMinMargin: o.rhythm ? 2 : 5, lyricWordSpace: 2.6, fingeringScale: 0.9 });
  tk.loadData(mei(b0, b1, o)); let svg = tk.renderToSVG(1);
  // fingers above the staff: Verovio clears the staff but not a stem that rises past it (G's, A's), so set them all on one
  // line, clear of the highest stem
  if (o.fing) { const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
    const tops = [...svg.matchAll(/class="stem">\s*<path d="M\d+ (\d+) L\d+ (\d+)"/g)].map(m => Math.min(+m[1], +m[2]));
    const base = Math.min(sy, ...tops) - 130;
    svg = svg.replace(/<g id="[^"]+" class="fing">\s*<text x="\d+" y="(\d+)"/g, (m, y) => +y < sy ? m.replace('class="fing">', `class="fing" transform="translate(0,${base - +y})">`) : m);
    // and the chord letters above the fingers
    if (o.chords) svg = svg.replace(/<g id="[^"]+" class="harm">\s*<text x="\d+" y="(\d+)"/g, (m, y) => m.replace('class="harm">', `class="harm" transform="translate(0,${Math.min(0, base - 330 - +y)})">`)); }
  if (o.counts) svg = addCounts(svg); if (o.boxes) svg = addBoxes(svg, o.noEx ? '' : S.bars[b0][0][0][0].toUpperCase()); if (o.rows) svg = addRows(svg, o.rows, b0, o.pic);
  out[k] = svg;
}
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(Object.keys(out).length, 'snippets');
