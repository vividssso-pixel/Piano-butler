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
  if (o.pre) return [i, `<note xml:id="${i}" dur="${DUR[d]}" loc="${S.pre[p]}" stem.dir="${o.hand === 'LU' ? 'up' : o.hand === 'L' ? 'down' : o.staff5 ? ((o.bass ? BASS_PLACE : STAFF_PLACE)[p] > 4 ? 'down' : 'up') : o.lh ? 'down' : 'up'}">${syl}</note>`];   // on a staff: above the middle line, stems down   // the right hand's stems up, the left hand's down
  return [i, o.rhythm ? `<note xml:id="${i}" dur="${DUR[d]}" loc="0" stem.dir="up">${syl}</note>` : `<note xml:id="${i}" dur="${DUR[d]}" pname="${pname}" oct="${oct}"${o.stem ? ` stem.dir="${o.stem}"` : ''}>${syl}</note>`];
}
function chordXml(ps, d, stem) { const i = nid(); return [i, `<chord xml:id="${i}" dur="${DUR[d]}"${stem ? ` stem.dir="${stem}"` : ''}>` + ps.map(p => { const [a, b] = pn(p); return `<note pname="${a}" oct="${b}"/>`; }).join('') + '</chord>']; }
// one line of bars [b0, b1): opts.words, opts.fing, opts.chords, opts.lh (a way), opts.rhythm (one-line staff), opts.meter
function mei(b0, b1, o) {
  let ms = '', ctrl = [];
  for (let b = b0; b < b1; b++) {
    const bar = S.bars[b]; let l1 = '', run = [];
    const flush = () => { if (run.length) l1 += run.length > 1 ? `<beam>${run.join('')}</beam>` : run[0]; run = []; };   // quavers two to a beam
    bar.forEach(([p, d, syl, wp, fo, lfo]) => { if (p.includes('+')) { flush(); const [i, x] = chordXml(p.split('+').map(q => trp(q, o.tr)), d); l1 += x; INFO[i] = { len: LEN[d] };   // a chord in the right hand (her 6 Nov 14:24: the chords one at a time)
        if (o.fing && fo != null) String(fo).split(' ').forEach(ff => ctrl.push(`<fing startid="#${i}" place="above">${ff}</fing>`)); return; }
      if (p === 'r') { flush(); const i = nid(); l1 += `<rest xml:id="${i}" dur="${DUR[d]}"/>`; INFO[i] = { len: LEN[d], rest: true }; return; }   // a rest (Lesson 8 on)
      const HL = o.mix && (S.hand || {})[p] === 'L';   // a left-hand note in a right-hand line: stem down, finger below
      if (HL && o.lh) { flush(); const i = nid(); l1 += `<note xml:id="${i}" dur="${DUR[d]}" pname="b" oct="4" head.visible="false" stem.visible="false" class="ghost">${o.words && syl ? `<verse n="1"><syl${wp ? ` wordpos="${wp}" con="d"` : ''}>${syl}</syl></verse>` : ''}</note>`; return; }   // both hands (her 6 Nov 10:09): the left hand's note sits on its own staff, written in S.lh
      const [i, x] = noteXml(trp(p, o.tr), d, { syl: o.words ? syl : '', wp: o.words ? wp : '', rhythm: o.rhythm, pre: o.pre, staff5: o.staff5, bass: o.bass, hand: HL ? 'LU' : '', lh: !o.staff5 && (o.lhfing || o.lhdown || HL) });
      if (d === 'q') { run.push(x); if (run.length === 2) flush(); } else { flush(); l1 += x; }
      if (o.fing && HL) ctrl.push(`<fing startid="#${i}" place="below">${lfo != null ? lfo : (S.lh_finger || {})[p]}</fing>`);
      else if (o.fing) ctrl.push(`<fing startid="#${i}" place="above">${fo != null && !o.fk ? fo : (o.fk ? S[o.fk] : S.rh_finger)[p]}</fing>`);   // fo: this note's own finger (G with 4 next to A)
      if (o.lhfing) ctrl.push(`<fing startid="#${i}" place="below">${lfo != null ? lfo : S.lh_finger[p]}</fing>`); INFO[i] = { len: LEN[d] }; });
    flush();
    let st2 = '';
    const CH = (o.src != null && S.more[o.src].chords) || S.chords;   // a tune of its own brings its own chords
    if (o.lh) { const ch = CH[b], last = b === S.bars.length - 1, pat = (last && S.lh[o.lh].end) || S.lh[o.lh][ch]; let l2 = '';
      pat.forEach(([ps, d, f]) => { const [i, x] = ps.length > 1 ? chordXml(ps, d) : noteXml(ps[0], d); l2 += x; if (f !== '' && f != null) String(f).split(' ').reverse().forEach(ff => ctrl.push(`<fing startid="#${i}" place="below" staff="2">${ff}</fing>`)); });
      st2 = `<staff n="2"><layer n="1">${l2}</layer></staff>`; }
    if (o.chords) ctrl.push(`<harm staff="1" tstamp="1" place="above">${o.ask && b > 0 ? '_____' : trChord(CH[b], o.tr)}</harm>`);   // ask: the first name given, the rest to write
    const right = b === S.bars.length - 1 ? ' right="end"' : '';
    ms += `<measure n="${b + 1}"${right}><staff n="1"><layer n="1">${l1}</layer></staff>${st2}${ctrl.splice(0).join('')}</measure>`;
  }
  const met = (o.key ? ` keysig="${o.key}"` : '') + (o.meter ? ` meter.count="${(S.meter || '4/4').split('/')[0]}" meter.unit="${(S.meter || '4/4').split('/')[1]}"` : '');
  const sd = o.staff5 ? `<staffDef n="1" lines="1" clef.shape="${o.bass ? 'F' : 'G'}" clef.line="1"${met}/>`   // a staff drawn to the lettered heads (her 4 Nov 18:11): Verovio gives the clef, we draw the lines
    : o.rhythm || o.pre ? `<staffDef n="1" lines="1" clef.shape="perc" clef.line="1" clef.visible="false"${met}/>`
    : o.lh ? `<staffGrp symbol="brace" bar.thru="true"><staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/><staffDef n="2" lines="5" clef.shape="F" clef.line="4"${met}/></staffGrp>`
    : o.bass ? `<staffDef n="1" lines="5" clef.shape="F" clef.line="4"${met}/>`   // the left hand alone on the King's staff, plain notes (Lesson 8 on)
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
  const met = o.meter ? ` meter.count="${(S.meter || '4/4').split('/')[0]}" meter.unit="${(S.meter || '4/4').split('/')[1]}"` : '';
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef><staffGrp symbol="brace" bar.thru="true"><staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/><staffDef n="2" lines="5" clef.shape="G" clef.line="2"${met}/></staffGrp></scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
}
let INFO = {};
// counts under the rhythm line: the beat a note starts on (coral), the beats it is held (grey, joined by a dash)
const ON = '#e4572e', HELD = '#9a9cc4';
function addCounts(svg) {
  const ev = []; let m; const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use xlink:href="#[^"]+" transform="translate\((\d+), (\d+)\)|<g id="[^"]+" class="barLine"[^>]*>\s*<path d="M(\d+) |<g id="(x\d+)" class="rest">\s*<use [^>]*translate\((\d+), /g;
  while ((m = re.exec(svg))) { if (m[1]) ev.push({ id: m[1], x: +m[2] }); else if (m[5]) ev.push({ id: m[5], x: +m[6] - 20 }); else ev.push({ bar: true, x: +m[4] }); }   // a rest is counted too (in grey: count it, don't clap)
  const sy = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  const HW = 212;   // a black notehead (E0A4 at scale 0.72)
  const per = []; ev.forEach((e, i) => { const n = ev[i + 1]; if (!e.bar && n && !n.bar && !INFO[e.id].rest && !INFO[n.id].rest) per.push((n.x - e.x) / INFO[e.id].len); });
  per.sort((a, b) => a - b); const U = per[Math.floor(per.length / 2)];
  const sylY = [...svg.matchAll(/class="syl">\s*<text x="[\d.]+" y="(\d+)"/g)].map(m => +m[1]); let out = '', beat = 0; const Y = sylY.length ? Math.max(...sylY) : sy + 640, FS = 300;   // the counts first, right under the notes; the words go below them (her 5 Nov 13:15)
  ev.forEach((e, ei) => { if (e.bar) { beat = 0; return; } const L = INFO[e.id].len, x0 = e.x + HW / 2;
    const nx = (ev[ei + 1] || { x: x0 + L * U }).x, step = L > 1 ? Math.min(U, (nx - 120 - x0) / (L - 0.5)) : U;
    if (L < 1) {   // a quaver: the beat's number on the beat, '+' (and) between
      out += `<text x="${x0.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${ON}" class="cnt">${Number.isInteger(beat) ? beat + 1 : '+'}</text>`; beat += L; return; }
    for (let k = 0; k < L; k++) { const x = x0 + k * step, held = k > 0;
      out += `<text x="${x.toFixed(0)}" y="${Y}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${held || INFO[e.id].rest ? HELD : ON}" class="cnt">${beat + k + 1}</text>`;
      if (held) { const xa = x - step + 150, xb = x - 150; if (xb > xa) out += `<line x1="${xa.toFixed(0)}" x2="${xb.toFixed(0)}" y1="${Y - 95}" y2="${Y - 95}" stroke="${HELD}" stroke-width="26" stroke-linecap="round"/>`; } }
    beat += L; });
  if (sylY.length) svg = svg.replace(/class="verse">/g, 'class="verse" transform="translate(0,420)">');
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
    if (names) out += `<text x="${x}" y="${T + B * 0.76}" text-anchor="middle" font-size="${B * 0.66}" font-weight="700" fill="#26296b" class="cnt">${names[k]}</text>`;
    else if (k === 0 && ex) out += `<text x="${x}" y="${T + B * 0.78}" text-anchor="middle" font-size="${B * 0.76}" font-weight="700" fill="#e4572e" class="cnt">${ex}</text>`; });
  return svg.replace(/(<g class="page-margin"[^>]*>)/, `$1${out}`);
}
// A lead sheet's "when" row, under the staff: for each bar, the left hand's pattern for that bar's chord, placed on its beats.
// A single note shows its finger number (coral); two notes together show a coral dot; a note held past its beat runs on
// as a grey line to the end of its length.
function addWhen(svg, way, b0, pic, Y0) {
  const ev = []; let m; const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use xlink:href="#[^"]+" transform="translate\((\d+), (\d+)\)|<g id="[^"]+" class="barLine"[^>]*>\s*<path d="M(\d+) |<g id="(x\d+)" class="rest">\s*<use [^>]*translate\((\d+), /g;
  while ((m = re.exec(svg))) { if (m[1]) ev.push({ id: m[1], x: +m[2] }); else if (m[5]) ev.push({ id: m[5], x: +m[6] - 20 }); else ev.push({ bar: true, x: +m[4] }); }   // a rest is counted too (in grey: count it, don't clap)
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

// a five-line staff spaced to the lettered heads (her 4 Nov 18:11): a line every head-height, E4 on the bottom line
let SP5 = 0;
// the left hand an octave lower on the King's staff (her 4 Nov 19:58): G2 on the bottom line, so C3 in the second space
const BASS_PLACE = { c4: 3, d4: 4, e4: 5, f4: 6, g4: 7, a4: 8, b4: 9 };
const STAFF_PLACE = { g3: -5, a3: -4, b3: -3, c4: -2, d4: -1, e4: 0, f4: 1, g4: 2, a4: 3, b4: 4, c5: 5, d5: 6, e5: 7, f5: 8, g5: 9 };
function drawStaff5(svg, lineY, RY, bass) {
  const sp = 2 * RY, k = sp / 180; SP5 = sp;
  svg = svg.replace(/(<g id="[^"]+" class="staff">\s*)<path d="M(\d+) (\d+) L(\d+) (\d+)" stroke-width="13" \/>/g, (m, a, x1, y1, x2) =>
    a + [0, 1, 2, 3, 4].map(i => `<path d="M${x1} ${lineY - i * sp} L${x2} ${lineY - i * sp}" stroke-width="13" class="s5"/>`).join(''));
  svg = svg.replace(/class="barLine">[\s\S]*?<\/g>/g, g => g.replace(/<path d="M(\d+) (-?[\d.]+) L(\d+) (-?[\d.]+)"/g, (m, x, ya, x2) => `<path d="M${x} ${lineY - 4 * sp} L${x2} ${lineY}"`));
  svg = svg.replace(/(class="clef">\s*<use [^>]*transform=")translate\((\d+), (\d+)\) scale\(([\d.]+), ([\d.]+)\)/, (m, a, x, y, sx) => `${a}translate(${+x - 40}, ${lineY - (bass ? 3 : 1) * sp}) scale(${sx * k * 0.72}, ${sx * k * 0.72})`);
  let mi = 0; const mid = lineY - 2 * sp;
  svg = svg.replace(/(class="meterSig">)([\s\S]*?)(<\/g>)/, (m, a, body, c) => a + body.replace(/transform="translate\((\d+), (\d+)\) scale\(([\d.]+), ([\d.]+)\)"/g, (mm, x, y, sx) => `transform="translate(${+x + 40}, ${mi++ ? mid + sp : mid - sp}) scale(${sx * k * 0.85}, ${sx * k * 0.85})"`) + c);
  return svg;
}
let FIRST_ONLY = false;   // set per job (o.lt1): the letter on each line's first note only
function addLetterHeads(svg, pitches, hs, hm, keepLen, onStaff, staff5, bass) {
  const PL = staff5 ? (bass ? BASS_PLACE : STAFF_PLACE) : (S.place || {});   // on a staff of our own every note has its line or space
  // heads about twice the size, so the places are twice as far apart too (S.pre: E on the line, D hanging just under it, C
  // on a ledger of its own); Verovio's ledger lines go, and the song's ledger notes (S.ledger) get one through their middle.
  // A head never touches its neighbour: where notes are close (quavers) it shrinks to fit.
  const RX0 = 250, RY0 = 195, FS0 = 290;
  if (!onStaff) svg = svg.replace(/<g[^>]*class="ledgerLines[^"]*"[^>]*>[\s\S]*?<\/g>/g, '');   // on the staff the ledgers stay
  const re = /<g id="(x\d+)" class="note">\s*<g class="notehead">\s*<use [^>]*transform="translate\((\d+), (\d+)\)[^>]*\/>\s*<\/g>(\s*<g id="[^"]+" class="stem">\s*<path d="M(\d+) (\d+) L\d+ (\d+)")?/g;
  const at = [...svg.matchAll(re)].map(m => +m[2] + 108), room = (k) => Math.min(k ? at[k] - at[k - 1] : 1e9, k < at.length - 1 ? at[k + 1] - at[k] : 1e9);
  const lineY = +(svg.match(/class="staff"[\s\S]*?<path d="M\d+ (\d+)/) || [0, 0])[1];
  let k = 0; const s = hs || Math.min(1, Math.min(...at.map((x, i) => room(i))) / 2 / RX0 - 0.12);   // one size on the line (or the song's)
  const RX = RX0 * s, RY = RY0 * s, FS = FS0 * s, STEM = staff5 ? Math.round(7 * RY) : 700;   // on our own staff a stem is three and a half spaces
  const beams = [...svg.matchAll(/class="beam">\s*<polygon points="([^"]+)"/g)].map(m => { const xs = m[1].trim().split(/\s+/).map(p => +p.split(',')[0]); return [Math.min(...xs), Math.max(...xs)]; });
  svg = svg.replace(re, (m, id, x, y, st, sx, y1, y2) => {
    if (!INFO[id]) return m;   // the left hand's own staff (o.lh): plain heads
    const L = INFO[id].len, open = L >= 2, p = pitches[k++], name = (FIRST_ONLY && k > 1) ? '' : hm ? S[hm][p] : p[0].toUpperCase(); let cx = +x + 108;
    // S.place: steps of half a head, as on a real staff (E on the line, D touching it from below, C a step further on its
    // ledger); the stem's head end moves with the head, its tip (and any beam) stays
    if (!onStaff) { const ny = p in PL ? lineY - PL[p] * RY : +y;
      // before the staff every stem not on a beam is one long length from its head (her 4 Nov 13:32 and 15:15: not short,
      // all the same, the long one); a beamed one stays on its beam
      if (st) { const down = +y2 > +y1, beamed = beams.some(([a, b]) => +sx >= a - 30 && +sx <= b + 30);
        const tip = beamed ? +y2 : staff5 ? (down ? ny + STEM : ny - STEM) : p in PL ? (down ? Math.max(+y2, ny + STEM) : Math.min(+y2, ny - STEM)) : +y2;   // on our staff: exactly three and a half spaces
        m = m.replace(`M${sx} ${y1} L${sx} ${y2}`, `M${sx} ${ny} L${sx} ${tip}`); }
      y = ny; }
    if (st) cx = +y2 < +y1 ? +sx - RX + 10 : +sx + RX - 10;   // the stem on the head's edge: up on the right, down on the left
    const lline = (yy) => `<line x1="${cx - RX - 110}" x2="${cx + RX + 110}" y1="${yy}" y2="${yy}" stroke="#000" stroke-width="22" class="lledger"/>`;
    let ledger = '';
    if (staff5 && (PL[p] <= -2 || PL[p] >= 10)) { const pl = PL[p];   // every ledger line between the staff and the note (G below middle C has two)
      if (pl <= -2) for (let q = -2; q >= pl; q -= 2) ledger += lline(+y + (pl - q) * RY);
      else for (let q = 10; q <= pl; q += 2) ledger += lline(+y - (q - pl) * RY); }
    else if (!staff5 && (S.ledger || []).includes(p)) ledger = lline(y);
    // drawn where the head was, so it sits over the line and under its own stem
    const head = ledger + `<ellipse cx="${cx}" cy="${y}" rx="${RX}" ry="${RY}" fill="${open ? '#fff' : '#26296b'}" stroke="#26296b" stroke-width="${open ? 26 : 0}" class="lhead"/>`
      + `<text x="${cx}" y="${+y + FS * 0.36}" text-anchor="middle" font-size="${FS}" font-weight="700" fill="${open ? '#26296b' : '#fff'}" class="cnt lname">${name}</text>`;
    return m.replace(/<use [^>]*\/>/, head);
  });
  if (staff5) svg = drawStaff5(svg, lineY, RY, bass);
  // beamed quavers: their stems as long as a crotchet's (her 4 Nov 15:19), so the beam moves to sit that far from the heads
  if (!onStaff) svg = fitBeams(svg, STEM);
  return svg.replace(/class="verse">/g, `class="verse" transform="translate(0,${keepLen ? 480 : 150})">`);   // a left-hand stem down needs the words further down   // the words below the bigger low notes
}
// Hands take turns (her 5 Nov 00:39: the zigzag pieces): one line of notes that steps between the two staves, the right
// hand's on the Queen's staff, the left hand's on the King's (note[6] === 'L'), quavers beamed in fours across both
const STEP = p => 'cdefgab'.indexOf(p[0]) + 7 * +p.replace(/[^0-9]/g, '');   // a diatonic step number, to find the middle line
function zigMei(b0, b1, o) {
  let ms = '';
  for (let b = b0; b < b1; b++) {
    let l1 = '', run = [], ctrl = [];
    const flush = () => { if (run.length) l1 += run.length > 1 ? `<beam>${run.join('')}</beam>` : run[0]; run = []; };
    S.bars[b].forEach(([p, d, syl, wp, f, lf, h]) => { const [pname, oct] = pn(p), i = nid(), L = h === 'L';
      const x = `<note xml:id="${i}" dur="${DUR[d]}" pname="${pname}" oct="${oct}"${L ? ' staff="2"' : ''} stem.dir="${STEP(p) >= (L ? STEP('d3') : STEP('b4')) ? 'down' : 'up'}"/>`;   // the stem rule on each hand's own staff (her 6 Nov 10:24)   // the left hand's stems up, so its fingers below stay clear
      if (d === 'q') { run.push(x); if (run.length === 4) flush(); } else { flush(); l1 += x; }
      if (o.fing && f != null) ctrl.push(`<fing startid="#${i}" staff="${L ? 2 : 1}" place="${L ? 'below' : 'above'}">${f}</fing>`);
      INFO[i] = { len: LEN[d] }; });
    flush();
    const right = b === S.bars.length - 1 ? ' right="end"' : '';
    ms += `<measure n="${b + 1}"${right}><staff n="1"><layer n="1">${l1}</layer></staff><staff n="2"><layer n="1"><mSpace/></layer></staff>${ctrl.join('')}</measure>`;
  }
  const met = o.meter ? ` meter.count="${(S.meter || '4/4').split('/')[0]}" meter.unit="${(S.meter || '4/4').split('/')[1]}"` : '';
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef><staffGrp symbol="brace" bar.thru="true"><staffDef n="1" lines="5" clef.shape="G" clef.line="2"${met}/><staffDef n="2" lines="5" clef.shape="F" clef.line="4"${met}/></staffGrp></scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
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
  spacingLinear: o.words && o.rhythm ? Math.min(o.sl || 0.25, +(process.env.WSL || 0.4)) : (o.sl || 0.25),   // a line with words: as tight as Verovio likes, the words then set the room (her 6 Nov 15:00: bigger notes)
  spacingNonLinear: o.snl || 0.6, font: 'Leipzig', lyricSize: 4.0, lyricTopMinMargin: o.ltm || (o.rhythm ? 2 : 5),
  lyricWordSpace: o.lws || 3.4, lyricSize: o.lys || +(process.env.LYS || 3.6), fingeringScale: 0.9,
  ...(o.staff5 ? { rightMarginClef: 2, leftMarginMeterSig: 2, rightMarginMeterSig: 2 } : { rightMarginClef: 1, leftMarginMeterSig: 1, rightMarginMeterSig: 1 }),   // room round the clef and the time on our big staff (her 4 Nov 21:11)
  ...(o.letters ? { leftMarginNote: 2, rightMarginNote: 1.5, leftMarginBarLine: 1.5, rightMarginBarLine: 2 } : { leftMarginNote: 1, rightMarginNote: 0, leftMarginBarLine: 0, rightMarginBarLine: 0 }),   // set every time: the toolkit keeps options between jobs   // big lettered heads: room round each and off the bar lines (her 4 Nov 13:22)
  ...extra });
const load = (b0, b1, o) => { INFO = {}; id = 0; tk.loadData(o.duet ? duetMei(b0, b1, o) : o.zig ? zigMei(b0, b1, o) : mei(b0, b1, o)); };
const group = (k) => JOBS[k] && JOBS[k][2].zig ? 'zig' : k.replace(/\d+$/, '').replace(/^more[AB]$/, 'more'), natural = {};   // the two More to play tunes print at one size (her 5 Nov 13:51)
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
 if (o.boxes) svg = addBoxes(svg, o.noEx ? '' : S.bars[b0][0][0][0].toUpperCase(), o.names ? S.bars.slice(b0, b1).flat().filter(n => n[0] !== 'r').map(n => n[0][0].toUpperCase()) : null, o.box, o.pre);   // the boxes read the engraved heads, so before the lettered heads replace them
  if (o.rows) svg = addRows(svg, o.rows, b0, o.pic, o.pre);   // the rows read the engraved notes and the line, so before the lettered heads too
  FIRST_ONLY = !!o.lt1; if (o.letters) svg = addLetterHeads(svg, S.bars.slice(b0, b1).flat().map(n => n[0]).filter(p => p !== 'r'), o.hs, o.hm, o.mix, !o.pre, o.staff5, o.bass);   // first, so the fingers clear the stems as they end up
  if (o.lhfing) { const sy = sy0;
    const bots = [...svg.matchAll(/class="stem">\s*<path d="M[\d.]+ (-?[\d.]+) L[\d.]+ (-?[\d.]+)"/g)].map(m => Math.max(+m[1], +m[2]));
    const base = Math.max(sy, ...bots) + 330 + (o.letters && (!o.pre || o.staff5) ? 220 : 0);   // on the staff a lettered head hangs below its stem
    svg = svg.replace(/<g id="[^"]+" class="fing">\s*<text x="\d+" y="(\d+)"/g, (m, y) => +y > sy ? m.replace('class="fing">', `class="fing" transform="translate(0,${base - +y})">`) : m); }
  if (o.fing) { const sy = o.staff5 ? sy0 - 4 * SP5 : sy0;
    const tops = [...svg.matchAll(/class="stem">\s*<path d="M[\d.]+ (-?[\d.]+) L[\d.]+ (-?[\d.]+)"/g)].map(m => Math.min(+m[1], +m[2]));
    const base = Math.min(sy, ...tops) - 130;
    svg = svg.replace(/<g id="[^"]+" class="fing">\s*<text x="\d+" y="(\d+)"/g, (m, y) => +y < sy0 ? m.replace('class="fing">', `class="fing" transform="translate(0,${base - +y})">`) : m);
    // and the chord letters above the fingers
    if (o.chords) svg = svg.replace(/<g id="[^"]+" class="harm">\s*<text x="\d+" y="(\d+)"/g, (m, y) => m.replace('class="harm">', `class="harm" transform="translate(0,${Math.min(0, base - 330 - +y)})">`)); }
  if (o.chords && !o.fing) { const tops = [...svg.matchAll(/class="stem">\s*<path d="M[\d.]+ (-?[\d.]+) L[\d.]+ (-?[\d.]+)"/g)].map(m => Math.min(+m[1], +m[2]));   // the chord names clear of every stem
    const base = Math.min(sy0, ...tops) - 160;
    svg = svg.replace(/<g id="[^"]+" class="harm">\s*<text x="\d+" y="(\d+)"/g, (m, y) => m.replace('class="harm">', `class="harm" transform="translate(0,${Math.min(0, base - +y)})">`)); }
  if (o.counts) svg = addCounts(svg);
  // a left-hand line before the staff (her 12:18): the line and the ledgers mean the treble's places, so they go; the notes
  // keep their high and low, the bar lines stay
  // her 12:22: and the right hand's too -- before the staff no line at all, only the notes' high and low and the bar lines;
  // the staff comes in whole, later
  if (o.pre && !o.staff5) svg = svg.replace(/(<g id="[^"]+" class="staff">\s*)<path d="M\d+ \d+ L\d+ \d+" stroke-width="13" \/>/g, '$1').replace(/<line [^>]*class="lledger"\/>/g, '');
  // before the staff the bar lines reach as far as the notes do (the one-line staff draws them a space each way)
  if (o.pre && !o.staff5) svg = svg.replace(/class="barLine">[\s\S]*?<\/g>/g, g => g.replace(/<path d="M(\d+) (\d+) L(\d+) (\d+)"/g, (m, x, ya, x2, yb) => `<path d="M${x} ${+ya - 260} L${x2} ${+yb + 260}"`));   // the end bar's thick stroke as tall as its thin one (her 4 Nov 12:41)
  // bar numbers lifted clear of the notes
  svg = svg.replace(/class="mNum autogenerated">/g, 'class="mNum autogenerated" transform="translate(-60,-260)">');
  if (o.rows && o.pre) {   // room on the left for the row numbers
    svg = svg.replace(/<svg viewBox="0 0 ([\d.]+) ([\d.]+)"/, (m, w, h) => `<svg viewBox="0 0 ${+w + 25} ${h}"`)
      .replace(/class="definition-scale"([^>]*)viewBox="0 0 ([\d.]+) ([\d.]+)"/, (m, a, w, h) => `class="definition-scale"${a}viewBox="-500 0 ${+w + 500} ${h}"`);
  }
  out[k] = svg; S.bars = SB;
}

// Bars of one width (her 4 Nov 19:58): in every line of a group the bars are the same width and start at the same place,
// so the bar lines stand one under another. Every x after the first note is mapped piecewise, bar by bar.
const staff1 = (svg) => svg.split(/(?=<g id="[^"]+" class="measure)/).map(m => { const a = m.indexOf('class="staff"'), b = m.indexOf('class="staff"', a + 1); return b > 0 ? m.slice(0, b) : m; }).join('');   // the first staff of each bar (both hands: the right hand's)
function barsOf(svg) {
  const body = svg.slice(svg.indexOf('</defs>') > 0 ? svg.indexOf('</defs>') : 0);
  const bars = [...body.matchAll(/class="barLine">\s*<path d="M(-?[\d.]+) /g)].map(m => +m[1]);
  const one = staff1(body);
  const heads = [...one.matchAll(/class="notehead">(?:\s*<line [^>]*\/>)*\s*<(?:use [^>]*translate\((-?[\d.]+),|ellipse cx="(-?[\d.]+)")/g)].map(m => +(m[1] || m[2]));   // a head's own ledger lines come first
  const rests = [...one.matchAll(/class="rest">\s*<use [^>]*translate\((-?[\d.]+),/g)].map(m => +m[1]);
  return { bars, heads, rests, first: heads.length ? Math.min(...heads) : null };
}
function mapX(svg, knotsOld, knotsNew) {
  const f = (x) => { x = +x; if (x <= knotsOld[0]) return x;
    for (let i = 1; i < knotsOld.length; i++) if (x <= knotsOld[i]) return Math.round((knotsNew[i - 1] + (x - knotsOld[i - 1]) * (knotsNew[i] - knotsNew[i - 1]) / (knotsOld[i] - knotsOld[i - 1])) * 10) / 10;
    return x - knotsOld[knotsOld.length - 1] + knotsNew[knotsNew.length - 1]; };
  const cut = svg.indexOf('</defs>'), head = svg.slice(0, cut > 0 ? cut : 0); let body = svg.slice(cut > 0 ? cut : 0);
  const rects = [];   // a rect (a word's hyphen, a box) keeps its two ends on the map: its width follows
  body = body.replace(/<rect ([^>]*)\/?>(<\/rect>)?/g, (m, attrs) => { const x = +(attrs.match(/(?:^| )x="(-?[\d.]+)"/) || [])[1], w = +(attrs.match(/ width="(-?[\d.]+)"/) || [])[1];
    if (isNaN(x) || isNaN(w)) { rects.push(m); return `@@R${rects.length - 1}@@`; }
    let nx = f(x), nw = Math.max(1, f(x + w) - nx);
    if (w < 600) { nx = Math.round((f(x + w / 2) - w / 2) * 10) / 10; nw = w; }   // a small box or hyphen keeps its size: only its middle moves
    rects.push(m.replace(/(^<rect |[ ])x="(-?[\d.]+)"/, `$1x="${nx}"`).replace(/ width="(-?[\d.]+)"/, ` width="${Math.round(nw * 10) / 10}"`)); return `@@R${rects.length - 1}@@`; });
  body = body.replace(/(<use[^>]*transform="translate\()(-?[\d.]+)/g, (m, a, x) => a + f(x))   // a group's own transform (the page margin, a bar number) is relative: left alone
    .replace(/ (x|cx|x1|x2)="(-?[\d.]+)"/g, (m, a, x) => ` ${a}="${f(x)}"`)
    .replace(/ d="([^"]+)"/g, (m, d) => ' d="' + d.replace(/([ML])\s*(-?[\d.]+)/g, (mm, c, x) => c + f(x)) + '"')
    .replace(/ points="([^"]+)"/g, (m, p) => ' points="' + p.trim().split(/\s+/).map(q => { const [x, y] = q.split(','); return f(x) + ',' + y; }).join(' ') + '"');
  body = body.replace(/@@R(\d+)@@/g, (m, i) => rects[+i]);
  return head + body;
}
// A stem stays on its own head (her 6 Nov 10:24: 'stems right on the side of the head'): the spacing moves head and stem
// through different stretches of the line, so after it each plain head gets its stem back at the distance Verovio set
// (up: on the right edge, down: on the left), and a quaver's flag goes with its stem
const NOTE_STEM = /(<g id="([^"]+)" class="note">\s*<g class="notehead">\s*<use [^>]*translate\()(-?[\d.]+)(,[^>]*\/>\s*<\/g>\s*<g id="[^"]+" class="stem">\s*<path d="M)(-?[\d.]+)( -?[\d.]+ L)(-?[\d.]+)( -?[\d.]+"[^>]*\/>(?:\s*<g class="flag">\s*<use [^>]*translate\()?)(-?[\d.]+)?/g;
// a word goes with its own note (her 6 Nov 14:59): a word's left edge can sit in the stretch before its note, so it is set
// again at the distance from its head that Verovio gave it
function keepWords(before, after) {
  const HEAD = /class="notehead">(?:\s*<line [^>]*\/>)*\s*<(?:use [^>]*translate\((-?[\d.]+),|ellipse cx="(-?[\d.]+)")/;
  const parts = (svg) => svg.split(/(?=<g id="[^"]+" class="note")/);
  const off = {}; parts(before).forEach(p => { const id = (p.match(/^<g id="([^"]+)" class="note"/) || [])[1]; if (!id) return; const h = p.match(HEAD), t = p.match(/class="syl">\s*<text x="(-?[\d.]+)"/); if (h && t) off[id] = +t[1] - +(h[1] || h[2]); });
  return parts(after).map(p => { const id = (p.match(/^<g id="([^"]+)" class="note"/) || [])[1]; if (!id || off[id] == null) return p; const h = p.match(HEAD); if (!h) return p;
    const x = Math.round((+(h[1] || h[2]) + off[id]) * 10) / 10; return p.replace(/(class="syl">\s*<text x=")(-?[\d.]+)/, `$1${x}`); }).join('');
}
function keepStems(before, after) {
  const off = {}; for (const m of before.matchAll(NOTE_STEM)) off[m[2]] = [+m[5] - +m[3], m[9] != null ? +m[9] - +m[5] : null];
  return after.replace(NOTE_STEM, (m, a, id, hx, b, sx, c, sx2, d, fx) => { if (!off[id]) return m; const x = Math.round((+hx + off[id][0]) * 10) / 10;
    return a + hx + b + x + c + x + d + (fx != null && off[id][1] != null ? Math.round((x + off[id][1]) * 10) / 10 : (fx ?? '')); });
}
// each note's word (syllable) width, in the line's own units, from its letters (each its own width) and size
function sylOffs(svg) {   // where each note's word starts, from its head (Verovio moves a word with a hyphen further left)
  svg = staff1(svg); const HEAD = /class="notehead">(?:\s*<line [^>]*\/>)*\s*<(?:use [^>]*translate\((-?[\d.]+),|ellipse cx="(-?[\d.]+)")/;
  return svg.split(/(?=<g id="x\d+" class="note">)/).filter(p => /^<g id="x\d+" class="note">/.test(p)).map(p => { const h = p.match(HEAD), t = p.match(/class="syl">\s*<text x="(-?[\d.]+)"/); return h && t ? +t[1] - +(h[1] || h[2]) : -144; });
}
function sylWidths(svg) {
  svg = staff1(svg); const starts = [...svg.matchAll(/<g id="x\d+" class="note">/g)].map(m => m.index); starts.push(svg.length);
  return starts.slice(0, -1).map((st, i) => { const seg = svg.slice(st, starts[i + 1]); const m = seg.match(/class="syl">[\s\S]*?<tspan font-size="(\d+)px">([^<]*)<\/tspan>/);
    return m ? [...m[2]].reduce((a, ch) => a + (/[mwMW]/.test(ch) ? 0.78 : /[iljtfrI.,;:!'’ ]/.test(ch) ? 0.3 : /[A-Z]/.test(ch) ? 0.66 : 0.53), 0) * +m[1] + (/class="syl">[\s\S]*?<rect/.test(seg) ? +m[1] * 0.5 : 0) : 0; });
}
const MIN_FIT = 0.9, EVEN = true, EVEN_K = +(process.env.EVEN_K || 0.6);   // how far toward even beats (1 = all the way)
for (const g of new Set(Object.keys(out).map(group))) {
  const ks = Object.keys(out).filter(k => group(k) === g && !(JOBS[k][2].duet)); if (!ks.length) continue;
  const info = ks.map(k => barsOf(out[k])); if (info.some(i => i.first == null || !i.bars.length)) continue;
  const s = Math.max(...info.map(i => i.first)) - 260;   // where the first bar's music starts, the same in every line
  // each bar column as wide as its widest bar in the group (so words never crowd), then all of them fill the line
  const n = Math.max(...info.map(i => i.bars.length)), same = info.every(i => i.bars.length === n);
  const wid = info.map(i => i.bars.map((b, j) => b - (j ? i.bars[j - 1] : i.first - 260)));   // natural widths, as engraved
  const wordy = ks.some(k => JOBS[k][2].words);   // without words every bar of the same length gets the same width (her 6 Nov 14:24)
  // with words (her 6 Nov 14:59: 'notes leaning to one side'): each bar gets the room its words need, and otherwise every bar
  // the same share (the bars needing more take it, the rest share what is left evenly)
  const needOf = (k) => { const [b0, b1, oo] = JOBS[k], data = (oo.src != null ? S.more[oo.src].bars : S.bars).slice(b0, b1);
    const SK = n => n[0] === 'r' || (oo.lh && oo.mix && (S.hand || {})[n[0]] === 'L'); const sy = sylWidths(out[k]), so = sylOffs(out[k]); let h = 0;
    return data.map(bar => { const it = []; let t = 0; bar.forEach(n => { if (n[0] === 'r') it.push({ r: 1, w: 0, f: 0, t }); else { it.push({ w: sy[h] || 0, f: sy[h] ? so[h] : 0, t }); h++; } t += LEN[n[1]]; });
      if (!it.length) return 600; const a = it[0], z = it[it.length - 1], fix = Math.max(330, 100 - a.f) + Math.max(z.r ? 400 : 330, z.f + z.w - 90) + 212;
      let g = 0, u = 0; for (let i = 1; i < it.length; i++) { const wg = Math.max(300, it[i - 1].f + it[i - 1].w - it[i].f + 150); g += wg; u = Math.max(u, wg / (it[i].t - it[i - 1].t)); }
      return EVENNEED ? fix + u * (z.t - a.t) : fix + g; }); };   // even: every beat as wide as the widest word needs   // the words' room; the beats take what is left
  let col = [...Array(n)].map(() => 1), keep = false;
  const spanAll = Math.min(...info.map(i => i.bars[i.bars.length - 1])) - s;
  let EVENNEED = true; if (same && wordy) { const ev = ks.map(needOf), evTot = [...Array(n)].reduce((a, _, j) => a + Math.max(...ev.map(r => r[j] || 0)), 0); if (evTot > spanAll * +(process.env.EVG || 0)) EVENNEED = false; if (process.env.DBG6) console.log(g, Math.round(evTot), Math.round(spanAll), EVENNEED); }   // all even if the line has room, else only what the words need
  if (same && wordy) { const nd = ks.map(needOf), need = [...Array(n)].map((_, j) => Math.max(...nd.map(r => r[j] || 0)));
    let fixed = new Set(), q = 0;
    for (let it = 0; it < n; it++) { const free = [...Array(n).keys()].filter(j => !fixed.has(j)); q = (spanAll - [...fixed].reduce((a, j) => a + need[j], 0)) / free.length;
      const more = free.filter(j => need[j] > q); if (!more.length) break; more.forEach(j => fixed.add(j)); }
    col = need.map((v, j) => fixed.has(j) ? v : Math.max(q, 1)); if (process.env.DBG5) console.log(g, ks.join(','), JSON.stringify(need.map(Math.round)), Math.round(spanAll), JSON.stringify(col.map(Math.round))); }
  const tot = col.reduce((a, b) => a + b, 0);
  const grow = same && wordy && tot > spanAll ? tot - spanAll : 0;   // the words need more room than the line has: the line grows (the page scales it back), the gaps stay even   // never crowd the words: the bars stay as engraved (only the beats evened inside them)
  if (keep) console.log('bars left as engraved in ' + g + ' (would squeeze to ' + fit.toFixed(2) + ')');
  const E = Math.min(...info.map(i => i.bars[i.bars.length - 1])) + grow;   // one right edge for every line, so the last bar lines stand together too
  ks.forEach((k, j) => { const { bars, first } = info[j], a1 = first - 260, end = E;
    if (keep && JOBS[k][2].noEven) return;
    const span = end - s; let x = s; const nw = keep ? [a1, ...bars] : [s, ...bars.map((b, i) => (x += span * (same ? col[i] / tot : 1 / bars.length)))];
    const s0 = nw[0];
    // and inside each bar the notes stand by the beat (her 5 Nov 00:11: the first bar's gaps): a crotchet is one even step,
    // a minim two; the gap after the bar line keeps its share
    const [b0, b1, oo] = JOBS[k], data = (oo.src != null ? S.more[oo.src].bars : S.bars).slice(b0, b1);
    let ko = [a1], kn = [s0];
    const SKIP = n => n[0] === 'r' || (oo.lh && oo.mix && (S.hand || {})[n[0]] === 'L');   // a rest, or a note the left hand plays on its own staff
    if (process.env.DBG) console.log(k, JSON.stringify(sylWidths(out[k]).map(Math.round)), JSON.stringify(info[j].bars), data.flat().filter(n => !SKIP(n)).length, info[j].heads.length, data.length, bars.length);
    if (EVEN && !oo.rhythm && data.flat().filter(n => !SKIP(n)).length === info[j].heads.length && data.length === bars.length) {
      // as even by the beat as the words allow (her 5 Nov 13:50): try all the way first, then less, until no two words touch
      const sy = sylWidths(out[k]), so = sylOffs(out[k]);
      const build = (K) => { const o = [a1], nn = [s0], hx2 = []; let h = 0, rr = 0, si = 0;   // h: heads seen, si: words (a hidden left-hand note has a word but no head)
        data.forEach((bar, bi) => { const os = bi ? bars[bi - 1] : a1, oe = bars[bi], ns = nw[bi], ne = nw[bi + 1];
          // by the beat, and the notes as a whole centred in the bar (her 6 Nov 10:09: 'never leaning to one side'):
          // the gap after the bar line and the gap before the next one are the same
          // her 6 Nov 14:24 ('check every gap'): each gap is its beats' share of the bar, but never less than its two words need;
          // the notes as a whole are then centred, the gap after the bar line the same as the gap before the next one
          const T = bar.reduce((a, n) => a + LEN[n[1]], 0), W = ne - ns;
          // the items in the bar: notes and rests (a rest takes its place like a note, so it never crowds one)
          const it = []; { let t = 0; bar.forEach(n => { if (n[0] === 'r') it.push({ t, r: true, w: 0, f: 0 }); else { it.push({ t, w: sy[si] || 0, f: sy[si] ? so[si] : 0, gh: SKIP(n) }); si++; } t += LEN[n[1]]; }); }
          const ni = it.length, Lm = Math.max(330, ni ? 100 - it[0].f : 0), Rm = Math.max(ni && it[ni - 1].r ? 400 : 330, ni ? it[ni - 1].f + it[ni - 1].w - 90 : 0);   // a word's own start and end, not only its note's   // a word starts at its note and runs to the right   // a rest is wider than a head   // a head, and its word, never crowd a bar line
          // the beat's step: as big as the bar allows (up to an even quarter of it), found so beats and words fill the room exactly
          const room = W - Lm - Rm, gapAt = (u) => it.map((x, i) => i ? Math.max((x.t - it[i - 1].t) * u, it[i - 1].f + it[i - 1].w - x.f + 150, 300) : 0), sum = (u) => gapAt(u).reduce((a, g) => a + g, 0);
          let lo = 0, hi = W / T; if (sum(hi) > room - 212) { for (let r = 0; r < 30; r++) { const md = (lo + hi) / 2; if (sum(md) > room - 212) hi = md; else lo = md; } hi = lo; }
          const gap = gapAt(hi); if (process.env.DBG7 && bi === 0) console.log(k, JSON.stringify(it.map(x => [x.t, Math.round(x.w), Math.round(x.f)])), JSON.stringify(gap.map(Math.round)), Math.round(hi), Math.round(room));
          let span = gap.reduce((a, g) => a + g, 0), sc = 1;
          if (span > room - 212) { sc = (room - 212) / span; span = room - 212; }
          const gw = ni && it[ni - 1].r ? 270 : 212, lead = Math.max(Lm, (W - span - gw) / 2);   // centred by what is seen: the last glyph's own width counts
          let px = ns + lead; if (process.env.DBG2 && bi === 0) console.log(k, K, 'ns', ns, 'ne', ne, 'os', os, 'oe', oe, 'lead', lead, 'span', span, 'sc', sc, 'heads', info[j].heads.slice(h, h + 4));
          it.forEach((x, i) => { px += i ? gap[i] * sc : 0;
            if (x.gh) { hx2.push(px); return; }   // the hidden note: its word's place, no head to move
            const hx = x.r ? info[j].rests[rr++] : info[j].heads[h++]; if (hx == null) return;
            const ox = ns + (hx - os) * (ne - ns) / (oe - os), nx = ox + K * (px - ox);
            if (!x.r) hx2.push(nx); if (hx > o[o.length - 1] && nx > nn[nn.length - 1]) { o.push(hx); nn.push(nx); } });
          o.push(oe); nn.push(ne); });
        return { o, nn, hx2 }; };
      const fits = ({ hx2 }) => hx2.every((x, i) => i === 0 || !sy.length || (x - hx2[i - 1]) >= (sy[i - 1] ? so[i - 1] + sy[i - 1] - (sy[i] ? so[i] : 0) + 120 : 0));
      const worst = ({ hx2 }) => Math.min(...hx2.map((x, i) => i === 0 || !sy.length ? 1e9 : (x - hx2[i - 1]) - ((sy[i - 1] || 0) + (sy[i] || 0)) / 2 - 120));
      let best = null; for (const K of [1, 0.85, 0.7, 0.55, 0.4, 0.25, 0]) { const c = build(K); if (fits(c)) { best = c; if (process.env.DBG4) console.log(k, 'K', K); break; } }
      if (!best && process.env.DBG4) { const c = build(1); console.log(k, 'no K fits', JSON.stringify(c.hx2.map((x, i) => i && sy[i - 1] ? Math.round((x - c.hx2[i - 1]) - (so[i - 1] + sy[i - 1] - (sy[i] ? so[i] : 0) + 120)) : 0))); }
      if (best) { ko = best.o; kn = best.nn; } else { ko = [a1, ...bars]; kn = nw; }
    } else { ko = [a1, ...bars]; kn = nw; }
    if (process.env.DBG3) console.log(k, JSON.stringify(ko.map(Math.round)), JSON.stringify(kn.map(Math.round)));
    out[k] = keepWords(out[k], keepStems(out[k], mapX(out[k], ko, kn)));
    if (grow) out[k] = out[k].replace(/<svg viewBox="0 0 ([\d.]+) ([\d.]+)"/, (m, w, h) => { const inner = +(out[k].match(/class="definition-scale"[^>]*viewBox="0 0 ([\d.]+)/) || [0, 0])[1];
      return `<svg viewBox="0 0 ${(+w * (inner + grow) / inner).toFixed(1)} ${h}"`; }).replace(/(class="definition-scale"[^>]*viewBox="0 0 )([\d.]+)/, (m, a, w) => a + (+w + grow)); });   // the page grows with the line
}
// Stems back on their heads (her 5 Nov 13:14: 'stems barely hanging on'): the spacing passes move a head and its stem
// through different stretches of the line, so each stem is set again on its own head's edge, up on the right, down on the left
function reattach(svg) {
  const W = 24;   // one stem weight everywhere, a little heavier so it prints the same at every size (her 5 Nov 13:19)
  svg = svg.replace(/(<ellipse cx="(-?[\d.]+)" cy="(-?[\d.]+)" rx="([\d.]+)"[^>]*class="lhead"\/>\s*<text[^>]*>[^<]*<\/text>\s*<\/g>\s*<g id="[^"]+" class="stem">\s*<path d=")M(-?[\d.]+) (-?[\d.]+) L(-?[\d.]+) (-?[\d.]+)"/g,
    (m, pre, cx, cy, rx, x1, y1, x2, y2) => { const up = +y2 < +y1, x = Math.round(+cx + (up ? 1 : -1) * (+rx - W / 2));
      return `${pre}M${x} ${y1} L${x} ${y2}"`; });
  svg = svg.replace(/(class="stem">\s*<path d="[^"]+" )stroke-width="\d+"/g, '$1stroke-width="1.7" vector-effect="non-scaling-stroke"');   // one width on the page, whatever the line's scale (her 5 Nov 13:42)
  // a beam reaches from its first stem to its last, edge to edge
  const stems = [...svg.matchAll(/class="stem">\s*<path d="M(-?[\d.]+) (-?[\d.]+) L-?[\d.]+ (-?[\d.]+)"/g)].map(m => ({ x: +m[1], tip: +m[3] }));
  return svg.replace(/(class="beam">\s*<polygon points=")([^"]+)"/g, (m, pre, pts) => {
    const P = pts.trim().split(/\s+/).map(q => q.split(',').map(Number)), xs = P.map(p => p[0]), ys = P.map(p => p[1]);
    const lo = Math.min(...xs), hi = Math.max(...xs), yt = Math.min(...ys), yb = Math.max(...ys);
    const mine = stems.filter(t => t.x > lo - 120 && t.x < hi + 120 && t.tip >= yt - 60 && t.tip <= yb + 60); if (mine.length < 2) return m;
    const nlo = Math.min(...mine.map(t => t.x)) - W / 2, nhi = Math.max(...mine.map(t => t.x)) + W / 2;
    return pre + P.map(([x, y]) => `${x === lo ? nlo : x === hi ? nhi : x},${y}`).join(' ') + '"'; });
}
// A finger number never sits on a stem (with stems by the rule, the left hand's go down into its numbers): it moves off the stem's end
function clearFingers(svg) {
  const stems = [...svg.matchAll(/class="stem">\s*<path d="M(-?[\d.]+) (-?[\d.]+) L-?[\d.]+ (-?[\d.]+)"/g)].map(m => ({ x: +m[1], lo: Math.min(+m[2], +m[3]), hi: Math.max(+m[2], +m[3]) }));
  const RE = /(<g id="[^"]+" class="fing"(?: transform="translate\(0,(-?[\d.]+)\)")?>\s*<text x=")(-?[\d.]+)(" y=")(-?[\d.]+)("[\s\S]*?<tspan font-size=")(\d+)/g;
  // first where each number would have to go; then every number of that row moves together, so the row stays one straight line
  const F = [...svg.matchAll(RE)].map(m => { const dy = +(m[2] || 0), y = +m[5] + dy, fs = +m[7], x = +m[3];
    const hit = stems.filter(t => Math.abs(t.x - x) < fs * 0.55 && t.hi > y - fs * 0.75 && t.lo < y + 20);
    if (!hit.length) return { y, ny: y };
    const mid = (Math.min(...hit.map(t => t.lo)) + Math.max(...hit.map(t => t.hi))) / 2, down = y > mid;
    return { y, ny: down ? Math.max(...hit.map(t => t.hi)) + fs * 0.85 : Math.min(...hit.map(t => t.lo)) - 60, down, up: !down }; });
  // numbers within a head's height of each other are one row: if one had to move, the whole row takes the furthest place
  const xs = F.map((f, i) => +[...svg.matchAll(RE)][i][3]); const near = (i, k) => k !== i && Math.abs(xs[k] - xs[i]) < 60 && Math.abs(F[k].y - F[i].y) < 800;
  F.forEach((f, i) => { if (F.some((g, k) => near(i, k))) f.stack = true; });   // a chord's stacked numbers keep their own heights
  const row = {}, ys = [...new Set(F.filter(f => !f.stack).map(f => f.y))].sort((a, b) => a - b), rows = [];
  ys.forEach(y => { const r = rows[rows.length - 1]; if (r && y - r[r.length - 1] < 450) r.push(y); else rows.push([y]); });
  rows.forEach(r => { const fs = F.filter(f => !f.stack && r.includes(f.y)); if (!fs.some(f => f.down || f.up)) return;
    const v = fs.some(f => f.down) ? Math.max(...fs.map(f => f.ny)) : Math.min(...fs.map(f => f.ny)); r.forEach(y => { row[y] = v; }); });
  // a chord's numbers: stacked a full line apart, from the lowest up
  const stackY = {}; F.forEach((f, i) => { if (!f.stack || stackY[i] != null) return; const grp = F.map((g, k) => k).filter(k => k === i || near(i, k)).sort((p, q) => F[q].y - F[p].y);
    const fsz = +[...svg.matchAll(RE)][i][7]; grp.forEach((k, n) => { stackY[k] = F[grp[0]].y - n * fsz * 0.95; }); });
  let idx = -1;
  return svg.replace(RE, (m, a, dy, x, c, y, d, fs) => { idx++; dy = +(dy || 0); if (stackY[idx] != null) return a + x + c + Math.round(stackY[idx] - dy) + d + fs;
    const r = row[+y + dy]; return r == null ? m : a + x + c + Math.round(r - dy) + d + fs; });
}
for (const k of Object.keys(out)) out[k] = clearFingers(reattach(out[k]));
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(Object.keys(out).length, 'snippets');
