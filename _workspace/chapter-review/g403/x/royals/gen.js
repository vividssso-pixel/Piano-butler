// Clara redesign sheet (Phase 403): four options, big, in the family line-up, and at book size on a staff
const { start } = require('../contentharness'); const fs = require('fs'), path = require('path');
(async () => {
  const H = await start(process.env.BUILD || 'drills.sf402.html');
  const p = await H.open({ path: '?book=lesson&ch=staff&lang=en', w: 900, h: 900 });
  await p.waitForTimeout(1500);
  await p.addScriptTag({ content: fs.readFileSync(path.join(__dirname, 'opts.js'), 'utf8') });
  await p.addScriptTag({ content: fs.readFileSync(path.join(__dirname, 'royals.js'), 'utf8') });
  const out = await p.evaluate(() => {
    const claras = { now: nnClara, A: clA, B: clB, C: clC, D: clD };
    const big = {}, line = {}, staff = {};
    for (const [id, f] of Object.entries(claras)) big['cl-' + id] = penSvg(f(30, 36, 2.1), { vb: [0, 0, 60, 72] });
    for (const [id, f] of Object.entries({ now: sfQueen, A: qnA, B: qnB })) big['qn-' + id] = penSvg(f(30, 36, 2.1), { vb: [0, 0, 60, 72] });
    for (const [id, f] of Object.entries({ now: sfKing, A: kgA, B: kgB })) big['kg-' + id] = penSvg(f(30, 36, 2.1), { vb: [0, 0, 60, 72] });
    line.now = penSvg([...sfKing(24, 34, 1.25), ...nnClara(64, 36, 1.0), ...sfQueen(104, 34, 1.25), ...nnGrandma(146, 34, 1.1)], { vb: [0, 0, 170, 58] });
    line.nu = penSvg([...kgA(24, 34, 1.25), ...clA(64, 36, 1.0), ...qnA(104, 34, 1.25), ...nnGrandma(146, 34, 1.1)], { vb: [0, 0, 170, 58] });
    const rung = (f) => { const L = []; for (let i = 0; i < 5; i++) L.push({ ...penLine([4, 12 + i * 8], [116, 12 + i * 8], 1.1), nw: true }); L.push({ ...penLine([50, 52], [74, 52], 1.3), nw: true }, { k: 'el', c: [62, 52], rx: 5.4, ry: 3.9, f: PEN_C, nw: true }, { k: 'el', c: [62, 52], rx: 2.4, ry: 1.8, f: PEN_P, nw: true }, { ...penLine([59, 52], [65, 52], 1.1), nw: true }); return penSvg([...L, ...f(36, 54, 0.85)], { vb: [0, 0, 120, 72] }); };
    for (const [id, f] of Object.entries(claras)) staff['cl-' + id] = rung(f);
    return { big, line, staff };
  });
  const CL = { now: ['Now', 'long hair and a crown -- a small Queen'], A: ['A \u00b7 Braids', 'two braids with coral bows, a small tiara'], B: ['B \u00b7 Ballerina bun', 'a bun, a tiara band with three gems, a coral sash'], C: ['C \u00b7 Bob and bow', 'a short bob, a tiara, a coral bow like the butler\u2019s'], D: ['D \u00b7 Curls', 'curly hair, a tiara and a flower clip, a dotted dress'] };
  const QN = { now: ['Now', 'the current Queen'], A: ['A \u00b7 Hair up', 'swept-up hair, pearl earrings and necklace, coral lips, a taller jewelled crown'], B: ['B \u00b7 Wavy hair + cape', 'long wavy hair, a royal cape with an ermine trim over the coral gown, the same tall crown'] };
  const KG = { now: ['Now', 'the current King (the dark beard reads as a mask)'], A: ['A \u00b7 White beard', 'a white beard and moustache with the mouth showing, bushy brows, a jewelled crown with a cross, an ermine collar'], B: ['B \u00b7 Curly moustache', 'no beard: a big curly moustache, rosy cheeks, side hair, the same crown and collar'] };
  const sec = (title, names, pre, withStaff) => `<h2>${title}</h2><div class="opts">` + Object.keys(names).map(id => `<div class="opt ${id === 'now' ? 'now' : ''}">${out.big[pre + id]}${withStaff ? out.staff[pre + id] : ''}<h3>${names[id][0]}</h3><p>${names[id][1]}</p></div>`).join('') + '</div>';
  const css = `body{margin:0;font-family:Inter,sans-serif;color:#26296b;background:#fff} .pg{width:210mm;padding:10mm 13mm} h1{font-family:'Playfair Display',Georgia,serif;font-size:21pt;margin:0} h2{font-family:'Playfair Display',Georgia,serif;font-size:14pt;margin:5mm 0 2mm} .sub{color:#4a4d86;font-size:10pt;margin:1mm 0 2mm}
    .opts{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm} .opt{border:0.6px solid #d9d4c4;border-radius:2mm;padding:2mm;text-align:center} .opt h3{margin:1mm 0 0;font-size:10pt} .opt p{margin:0.6mm 0 0;font-size:7.6pt;color:#4a4d86;line-height:1.35} .opt svg{width:72%;height:auto;display:block;margin:0 auto} .opt svg + svg{width:100%;margin-top:1mm}
    .now{background:#f5f1e6} .line{margin-top:2mm} .line svg{width:60%;display:block} .cap{font-size:8pt;color:#4a4d86;margin:0.5mm 0 0}`;
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><div class="pg">
    <h1>The royals: new looks</h1><p class="sub">Princess Clara gets a tiara (not the Queen's crown); the King gets a face; the Queen gets more queen. Small previews: Clara at book size beside middle C.</p>
    ${sec('Princess Clara', CL, 'cl-', true)}
    ${sec('The Queen', QN, 'qn-', false)}
    ${sec('The King', KG, 'kg-', false)}
    <h2>Together</h2><div class="line">${out.line.now}<p class="cap">Now: the King, Clara, the Queen, Grandma</p></div><div class="line">${out.line.nu}<p class="cap">New (A + A + A): King A, Clara A, Queen A, Grandma</p></div>
  </div></body></html>`;
  fs.writeFileSync(path.join(__dirname, 'sheet.html'), html);
  const q = await p.context().newPage(); await q.setViewportSize({ width: 800, height: 1100 }); await q.goto('file://' + path.join(__dirname, 'sheet.html')); await q.waitForTimeout(500);
  await q.screenshot({ path: path.join(__dirname, 'sheet.png'), fullPage: true });
  await q.pdf({ path: path.join(__dirname, 'sheet.pdf'), format: 'A4', printBackground: true });
  console.log('errs', p._errs.join('|')); await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
