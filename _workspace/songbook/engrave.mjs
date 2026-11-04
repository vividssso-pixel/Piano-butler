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
  if (o.pre) return [i, `<note xml:id="${i}" dur="${DUR[d]}" loc="${S.pre[p]}" stem.dir="${o.lh ? 'down' : 'up'}">${syl}</note>`];   // the right hand's stems up, the left hand's down
  return [i, o.rhythm ? `<note xml:id="${i}" dur="${DUR[d]}" loc="0" stem.dir="up">${syl}</note>` : `<note xml:id="${i}" dur="${DUR[d]}" pname="${pname}" oct="${oct}"${o.stem ? ` stem.dir="${o.stem}"` : ''}>${syl}</note>`];
}
function chordXml(ps, d, stem) { const i = nid(); return [i, `<chord xml:id="${i}" dur="${DUR[d]}"${stem ? ` stem.dir="${stem}"` : ''}>` + ps.map(p => { const [a, b] = pn(p); return `<note pname="${a}" oct="${b}"/>`; }).join('') + '</chord>']; }
// one line of bars [b0, b1): opts.words, opts.fing, opts.chords, opts.lh (a way), opts.rhythm (one-line staff), opts.meter
function mei(b0, b1, o) {
  let ms = '', ctrl = [];
  for (let b = b0; b < b1; b++) {
    const bar = S.bars[b]; let l1 = '', run = [];
    const flush = () => { if (run.length) l1 += run.length > 1 ? `<beam>${run.join('')}</beam>` : run[0]; run = []; };   // quavers two to a beam
    bar.forEach(([p, d, syl, wp]) => { const [i, x] = noteXml(trp(p, o.tr), d, { syl: o.words ? syl : '', wp: o.words ? wp : '', rhythm: o.rhythm, pre: o.pre, lh: o.lhfing || o.lhdown || (o.mix && (S.hand || {})[p] === 'L') });
      if (d === 'q') { run.push(x); if (run.length === 2) flush(); } else { flush(); l1 += x; }
      if (o.fing) ctrl.push(`<fing startid="#${i}" place="above">${(o.fk ? S[o.fk] : S.rh_finger)[p]}</fing>`);
      if (o.lhfing) ctrl.push(`<fing startid="#${i}" place="below">${S.lh_finger[p]}</fing>`); INFO[i] = { len: LEN[d] }; });
    flush();
    let st2 = '';
    if (o.lh) { const ch = S.chords[b], last = b === S.bars.length - 1, pat = (last && S.lh[o.lh].end) || S.lh[o.lh][ch]; let l2 = '';
      pat.forEach(([ps, d, f]) => { const [i, x] = ps.length > 1 ? chordXml(ps, d, 'up') : noteXml(ps[0], d, { stem: 'up' }); l2 += x; if (f !== '' && f != null) String(f).split(' ').reverse().forEach(ff => ctrl.push(`<fing startid="#${i}" place="below" staff="2">${ff}</fing>`)); });
      st2 = `<staff n="2"><layer n="1">${l2}</layer></staff>`; }
    if (o.chords) ctrl.push(`<harm staff="1" tstamp="1" place="above">${trChord(S.chords[b], o.tr)}</harm>`);
    const right = b === S.bars.length - 1 ? ' right="end"' : '';
    ms += `<measure n="${b + 1}"${right}><staff n="1"><layer n="1">${l1}</layer></staff>${st2}${ctrl.splice(0).join('')}</measure>`;
  }
  const met = (o.key ? ` keysig="${o.key}"` : '') + (o.meter ? ` meter.count="4" meter.unit="4"` : '');
  const sd = o.rhythm || o.pre ? `<staffDef n="1" lines="1" clef.shape="perc" clef.line="1" clef.visible="false"${met}/>`
    : o.lh ? `<staffGrp symbol="brace" bar.thru="true"><staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/><staffDef n="2" lines="5" clef.shape="F" clef.line="4"${met}/></staffGrp>`
    : `<staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/>`;
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef>${o.rhythm || !o.lh ? `<staffGrp>${sd}</staffGrp>` : sd}</scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
}
// the teacher's duet: two treble staves (played an octave higher), the right hand a pattern on the chord's notes a beat each,
// the left hand two notes a half bar; the last bar one chord in each hand
function duetMei(b0, b1, o) {
  const D = S.duet; let ms = '';
  for (let b = b0; b < b1; b++) { const last = b === S.bars.length - 1, ch = S.chords[b];
    const rh = last ? chordXml(D.end.rh, 's')[1] : D.rh[ch].map(p => noteXml(p, 'c')[1]).join('');
    const lh = last ? chordXml(D.end.lh, 's')[1] : [0, 1].map(() => chordXml(D.lh[ch], 'm')[1]).join('');
    ms += `<measure n="${b + 1}"${last ? ' right="end"' : ''}><staff n="1"><layer n="1">${rh}</layer></staff><staff n="2"><layer n="1">${lh}</layer></staff>${o.chords ? `<harm staff="1" tstamp="1" place="above">${ch}</harm>` : ''}</measure>`; }
  const met = o.meter ? ` meter.count="4" meter.unit="4"` : '';
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef><staffGrp symbol="brace" bar.thru="true"><staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/><staffDef n="2" lines="5" clef.shape="G" clef.line="2"${met}/></staffGrp></scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
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
    if (L < 1) {   // a quaver: the beat's number on the beat, '+' (and) between
      out += `<text x="${x0.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${ON}" class="cnt">${Number.isInteger(beat) ? beat + 1 : '+'}</text>`; beat += L; return; }
    for (let k = 0; k < L; k++) { const x = x0 + k * step, held = k > 0;
      out += `<text x="${x.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${held ? HELD : ON}" class="cnt">${beat + k + 1}</text>`;
      if (held) { const xa = x - step + 150, xb = x - 150; if (xb > xa) out += `<line x1="${xa.toFixed(0)}" x2="${xb.toFixed(0)}" y1="${Y - 95}" y2="${Y - 95}" stroke="${HELD}" stroke-width="26" stroke-linecap="round"/>`; } }
    beat += L; });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${out}`);
}
function addBoxes(svg, ex, names, boxSize, pre) {   // names: every box filled in (before the staff the place can't tell the note)
  const ev = []; let m; const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use xlink:href="#[^"]+" transform="translate\((\d+), (\d+)\)/g;
  while ((m = re.exec(svg))) ev.push(+m[2] + 106);
  // the boxes sit in a row of their own: below middle C's ledger line (top line + 4 spaces + a ledger + a head), or below
  // the words when the line has them
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  const sylY = [...svg.matchAll(/class="syl">\s*<text x="[\d.]+" y="(\d+)"/g)].map(m => +m[1]);
  const T = sylY.length ? Math.max(...sylY) + 160 : pre ? sy + 560 : sy + 1110; let out = '';   // before the staff: boxes just under the lowest head
  // each box as wide as its own room allows: a note close to its neighbours gets a narrower box, never touching them
  const room = (k) => Math.min(k ? ev[k] - ev[k - 1] : 1e9, k < ev.length - 1 ? ev[k + 1] - ev[k] : 1e9);
  const minRoom = Math.min(...ev.map((x, k) => room(k)));
  ev.forEach((x, k) => { const B = boxSize || Math.max(150, Math.min(440, minRoom - 50));   // as big as the space allows (her 4 Nov 15:21: too small)   // one size for every box on the line
    out += `<rect x="${x - B / 2}" y="${T}" width="${B}" height="${B}" rx="40" fill="#fff" stroke="${k === 0 && ex ? '#e4572e' : '#26296b'}" stroke-width="22" class="wbox"/>`;
    if (names) out += `<text x="${x}" y="${T + B * 0.76}" text-anchor="middle" font-size="${Math.min(B * 0.8, 260)}" font-weight="700" fill="#26296b" class="cnt">${names[k]}</text>`;
    else if (k === 0 && ex) out += `<text x="${x}" y="${T + B * 0.78}" text-anchor="middle" font-size="${B * 0.76}" font-weight="700" fill="#e4572e" class="cnt">${ex}</text>`; });
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
function addRows(svg, ways, b0, pic, pre) {
  const LX = pre ? -260 : 230;   // before the staff there is no clef to sit under: the row numbers go out to the left
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1]; let Y = sy + 1330, lab = '';
  ways.forEach(w => { svg = addWhen(svg, w, b0, pic, Y); const n = w.slice(3);
    lab += `<circle cx="${LX}" cy="${Y - 100}" r="125" fill="#26296b" class="when"/><text x="${LX}" y="${Y - 10}" text-anchor="middle" font-size="250" font-weight="700" fill="#fff" class="cnt">${n}</text>`;
    const tall = pic && Object.values(S.lh[w]).some(p => p.some(([ps]) => ps.length > 1));
    Y += tall ? 860 : 400; });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${lab}`);
}
// Before the staff the letter goes inside the note (her 4 Nov 12:07): a bigger head with its name in it, joined to its stem;
// filled for a crotchet or quaver (white letter), open for a minim or longer (navy letter). The small engraved head goes.

function fitBeams(svg, L) {
  let out = '', i = 0;
  for (;;) {
    const j = svg.indexOf('class="beam">', i); if (j < 0) { out += svg.slice(i); break; }
    const start = svg.lastIndexOf('<g', j); let depth = 0, end = -1;
    const re = /<g[\s>]|<\/g>/g; re.lastIndex = start; let m;
    while ((m = re.exec(svg))) { if (m[0] === '</g>') { depth--; if (depth === 0) { end = m.index + 4; break; } } else depth++; }
    if (end < 0) { out += svg.slice(i); break; }
    let g = svg.slice(start, end);
    const stems = [...g.matchAll(/class="stem">\s*<path d="M([\d.]+) (-?[\d.]+) L([\d.]+) (-?[\d.]+)"/g)];
    if (stems.length) {
      const up = +stems[0][4] < +stems[0][2], heads = stems.map(s => +s[2]), old = +stems[0][4];
      const tip = up ? Math.min(...heads) - L : Math.max(...heads) + L, d = tip - old;
      g = g.replace(/class="stem">(\s*)<path d="M([\d.]+) (-?[\d.]+) L([\d.]+) (-?[\d.]+)"/g, (mm, sp, x1, y1, x2, y2) => `class="stem">${sp}<path d="M${x1} ${y1} L${x2} ${+y2 + d}"`);
      g = g.replace(/<polygon points="([^"]+)"/, (mm, pts) => `<polygon points="${pts.trim().split(/\s+/).map(p => { const [x, y] = p.split(','); return x + ',' + (+y + d); }).join(' ')}"`);
    }
    out += svg.slice(i, start) + g; i = end;
  }
  return out;
}
function addLetterHeads(svg, pitches, hs, hm, keepLen, onStaff) {
  // heads about twice the size, so the places are twice as far apart too (S.pre: E on the line, D hanging just under it, C
  // on a ledger of its own); Verovio's ledger lines go, and the song's ledger notes (S.ledger) get one through their middle.
  // A head never touches its neighbour: where notes are close (quavers) it shrinks to fit.
  const RX0 = 250, RY0 = 195, FS0 = 290, STEM = 700;
  if (!onStaff) svg = svg.replace(/<g[^>]*class="ledgerLines[^"]*"[^>]*>[\s\S]*?<\/g>/g, '');   // on the staff the ledgers stay
  const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use [^>]*transform="translate\((\d+), (\d+)\)[^>]*\/>\s*<\/g>(\s*<g id="[^"]+" class="stem">\s*<path d="M(\d+) (\d+) L\d+ (\d+)")?/g;
  const at = [...svg.matchAll(re)].map(m => +m[2] + 108), room = (k) => Math.min(k ? at[k] - at[k - 1] : 1e9, k < at.length - 1 ? at[k + 1] - at[k] : 1e9);
  const lineY = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  let k = 0; const s = hs || Math.min(1, Math.min(...at.map((x, i) => room(i))) / 2 / RX0 - 0.12);   // one size on the line (or the song's)
  const RX = RX0 * s, RY = RY0 * s, FS = FS0 * s;
  const beams = [...svg.matchAll(/class="beam">\s*<polygon points="([^"]+)"/g)].map(m => { const xs = m[1].trim().split(/\s+/).map(p => +p.split(',')[0]); return [Math.min(...xs), Math.max(...xs)]; });
  svg = svg.replace(re, (m, id, x, y, st, sx, y1, y2) => {
    const L = INFO[id].len, open = L >= 2, p = pitches[k++], name = hm ? S[hm][p] : p[0].toUpperCase(); let cx = +x + 108;
    // S.place: steps of half a head, as on a real staff (E on the line, D touching it from below, C a step further on its
    // ledger); the stem's head end moves with the head, its tip (and any beam) stays
    if (!onStaff) { const ny = S.place && p in S.place ? lineY - S.place[p] * RY : +y;
      // before the staff every stem not on a beam is one long length from its head (her 4 Nov 13:32 and 15:15: not short,
      // all the same, the long one); a beamed one stays on its beam
      if (st) { const down = +y2 > +y1, beamed = beams.some(([a, b]) => +sx >= a - 30 && +sx <= b + 30);
        const tip = beamed ? +y2 : S.place && p in S.place ? (down ? Math.max(+y2, ny + STEM) : Math.min(+y2, ny - STEM)) : +y2;
        m = m.replace(`M${sx} ${y1} L${sx} ${y2}`, `M${sx} ${ny} L${sx} ${tip}`); }
      y = ny; }
    if (st) cx = +y2 < +y1 ? +sx - RX + 10 : +sx + RX - 10;   // the stem on the head's edge: up on the right, down on the left
    const ledger = (S.ledger || []).includes(p) ? `<line x1="${cx - RX - 110}" x2="${cx + RX + 110}" y1="${y}" y2="${y}" stroke="#000" stroke-width="22" class="lledger"/>` : '';
    // drawn where the head was, so it sits over the line and under its own stem
    const head = ledger + `<ellipse cx="${cx}" cy="${y}" rx="${RX}" ry="${RY}" fill="${open ? '#fff' : '#26296b'}" stroke="#26296b" stroke-width="${open ? 26 : 0}" class="lhead"/>`
      + `<text x="${cx}" y="${+y + FS * 0.36}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${open ? '#26296b' : '#fff'}" class="cnt lname">${name}</text>`;
    return m.replace(/<use [^>]*\/>/, head);
  });
  // beamed quavers: their stems as long as a crotchet's (her 4 Nov 15:19), so the beam moves to sit that far from the heads
  if (!onStaff) svg = fitBeams(svg, STEM);
  return svg.replace(/class="verse">/g, `class="verse" transform="translate(0,${keepLen ? 480 : 150})">`);   // a left-hand stem down needs the words further down   // the words below the bigger low notes
}
const JOBS = S.jobs || {
  sing1: [0, 4, { words: 1, meter: 1, fing: 1, pw: 1500 }], sing2: [4, 8, { words: 1, fing: 1, pw: 1500 }],   // page 1: the whole song (her 4 Nov 13:13)
  name1: [0, 4, { meter: 1, boxes: 1, pw: 1500 }], name2: [4, 8, { boxes: 1, noEx: 1, pw: 1500 }],   // page 2: its letter names to write
  rhy1: [0, 4, { words: 1, rhythm: 1, meter: 1, counts: 1, pw: 1350, sl: 0.4 }], rhy2: [4, 8, { words: 1, rhythm: 1, counts: 1, pw: 1350, sl: 0.4 }],   // bigger: the first thing a child reads
  play1: [0, 4, { fing: 1, chords: 1, meter: 1, rows: ['way2', 'way3', 'way4'] }],   // the tune once, every way under it
  play2: [4, 8, { fing: 1, chords: 1, rows: ['way2', 'way3', 'way4'] }],
  duet1: [0, 4, { duet: 1, meter: 1, pw: 2300 }], duet2: [4, 8, { duet: 1, pw: 2300 }],   // small: the teacher reads it
  g1: [0, 4, { fing: 1, chords: 1, meter: 1, tr: 4, key: '1s' }], g2: [4, 8, { fing: 1, chords: 1, tr: 4, key: '1s' }],   // Move it: bars 1 to 4 in G, one sharp, the same fingers
};
// Two passes, so that every line of a group (rhy1, rhy2...; sing1, sing2...) comes out at one size and ends at the right
// margin: first each line's natural width, then every line of the group justified to the group's widest.
const opts = (o, extra) => ({ adjustPageHeight: true, adjustPageWidth: false, scale: 50, header: 'none', footer: 'none', svgViewBox: true,
  pageMarginTop: 30, pageMarginBottom: o.rows ? 500 : o.counts || o.boxes ? 300 : 40, pageMarginLeft: o.pml || 20, pageMarginRight: 20,
  spacingLinear: o.sl || 0.25, spacingNonLinear: o.snl || 0.6, font: 'Leipzig', lyricSize: 4.0, lyricTopMinMargin: o.ltm || (o.rhythm ? 2 : 5),
  lyricWordSpace: o.lws || 2.6, lyricSize: o.lys || 4.0, fingeringScale: 0.9,
  ...(o.letters ? { leftMarginNote: 2, rightMarginNote: 1.5, leftMarginBarLine: 1.5, rightMarginBarLine: 2 } : { leftMarginNote: 1, rightMarginNote: 0, leftMarginBarLine: 0, rightMarginBarLine: 0 }),   // set every time: the toolkit keeps options between jobs   // big lettered heads: room round each and off the bar lines (her 4 Nov 13:22)
  ...extra });
const load = (b0, b1, o) => { INFO = {}; id = 0; tk.loadData(o.duet ? duetMei(b0, b1, o) : mei(b0, b1, o)); };
const group = (k) => k.replace(/\d+$/, ''), natural = {};
for (const [k, [b0, b1, o]] of Object.entries(JOBS)) {
  const SB = S.bars; if (o.src != null) S.bars = S.more[o.src].bars;   // a More to play tune (S.more) engraved like the song
  tk.setOptions(opts(o, { pageWidth: o.pw || 1750, breaks: 'none' })); load(b0, b1, o);
  const w = +tk.renderToSVG(1).match(/viewBox="[^"]+"/g)[1].split(' ')[2]; natural[group(k)] = Math.max(natural[group(k)] || 0, w); S.bars = SB;
}
const out = {};
for (const [k, [b0, b1, o]] of Object.entries(JOBS)) {
  const SB = S.bars; if (o.src != null) S.bars = S.more[o.src].bars;   // a More to play tune (S.more) engraved like the song
  tk.setOptions(opts(o, { pageWidth: Math.ceil(natural[group(k)] / 10) + 8, breaks: 'auto', minLastJustification: 0 })); load(b0, b1, o);
  if (tk.getPageCount() > 1) console.log('warning: ' + k + ' broke over a page');
  let svg = tk.renderToSVG(1);
  // fingers above the staff: Verovio clears the staff but not a stem that rises past it (G's, A's), so set them all on one
  // line, clear of the highest stem
  // left-hand fingers below a line whose stems go down: below the lowest stem
  const sy0 = +(svg.match(/class="staff">\s*<path d="M\d+ (\d+)/) || svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];   // the line's height, read before anything moves
 if (o.boxes) svg = addBoxes(svg, o.noEx ? '' : S.bars[b0][0][0][0].toUpperCase(), o.names ? S.bars.slice(b0, b1).flat().map(n => n[0][0].toUpperCase()) : null, o.box, o.pre);   // the boxes read the engraved heads, so before the lettered heads replace them
  if (o.rows) svg = addRows(svg, o.rows, b0, o.pic, o.pre);   // the rows read the engraved notes and the line, so before the lettered heads too
  if (o.letters) svg = addLetterHeads(svg, S.bars.slice(b0, b1).flat().map(n => n[0]), o.hs, o.hm, o.mix, !o.pre);   // first, so the fingers clear the stems as they end up
  if (o.lhfing) { const sy = sy0;
    const bots = [...svg.matchAll(/class="stem">\s*<path d="M[\d.]+ (-?[\d.]+) L[\d.]+ (-?[\d.]+)"/g)].map(m => Math.max(+m[1], +m[2]));
    const base = Math.max(sy, ...bots) + 330;
    svg = svg.replace(/<g id="[^"]+" class="fing">\s*<text x="\d+" y="(\d+)"/g, (m, y) => +y > sy ? m.replace('class="fing">', `class="fing" transform="translate(0,${base - +y})">`) : m); }
  if (o.fing) { const sy = sy0;
    const tops = [...svg.matchAll(/class="stem">\s*<path d="M[\d.]+ (-?[\d.]+) L[\d.]+ (-?[\d.]+)"/g)].map(m => Math.min(+m[1], +m[2]));
    const base = Math.min(sy, ...tops) - 130;
    svg = svg.replace(/<g id="[^"]+" class="fing">\s*<text x="\d+" y="(\d+)"/g, (m, y) => +y < sy ? m.replace('class="fing">', `class="fing" transform="translate(0,${base - +y})">`) : m);
    // and the chord letters above the fingers
    if (o.chords) svg = svg.replace(/<g id="[^"]+" class="harm">\s*<text x="\d+" y="(\d+)"/g, (m, y) => m.replace('class="harm">', `class="harm" transform="translate(0,${Math.min(0, base - 330 - +y)})">`)); }
  if (o.counts) svg = addCounts(svg);
  // a left-hand line before the staff (her 12:18): the line and the ledgers mean the treble's places, so they go; the notes
  // keep their high and low, the bar lines stay
  // her 12:22: and the right hand's too -- before the staff no line at all, only the notes' high and low and the bar lines;
  // the staff comes in whole, later
  if (o.pre) svg = svg.replace(/(<g id="[^"]+" class="staff">\s*)<path d="M\d+ \d+ L\d+ \d+" stroke-width="13" \/>/g, '$1').replace(/<line [^>]*class="lledger"\/>/g, '');
  // before the staff the bar lines reach as far as the notes do (the one-line staff draws them a space each way)
  if (o.pre) svg = svg.replace(/class="barLine">[\s\S]*?<\/g>/g, g => g.replace(/<path d="M(\d+) (\d+) L(\d+) (\d+)"/g, (m, x, ya, x2, yb) => `<path d="M${x} ${+ya - 260} L${x2} ${+yb + 260}"`));   // the end bar's thick stroke as tall as its thin one (her 4 Nov 12:41)
  // bar numbers lifted clear of the notes
  svg = svg.replace(/class="mNum autogenerated">/g, 'class="mNum autogenerated" transform="translate(-60,-260)">');
  if (o.rows && o.pre) {   // room on the left for the row numbers
    svg = svg.replace(/<svg viewBox="0 0 ([\d.]+) ([\d.]+)"/, (m, w, h) => `<svg viewBox="0 0 ${+w + 25} ${h}"`)
      .replace(/class="definition-scale"([^>]*)viewBox="0 0 ([\d.]+) ([\d.]+)"/, (m, a, w, h) => `class="definition-scale"${a}viewBox="-500 0 ${+w + 500} ${h}"`);
  }
  out[k] = svg; S.bars = SB;
}
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(Object.keys(out).length, 'snippets');
