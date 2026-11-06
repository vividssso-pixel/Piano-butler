// Phase 426: the townhouse for the website's lesson guides front page (lessons/index.html), replacing street425gen.js.
// Drawn by the app's own code (townhouseSvg + penSvg in the built drills page); rooms with a published guide page are
// in dark ink and become links, the others are grey and lose their button. Writes <OUT>/house-wide.svg (the wide
// house: every floor's rooms in one row, big screens), house-tall.svg (phones) and <OUT>/../house-og.svg.
//   BUILD=drills.tNNN.html OUT=<svg/index> node house428gen.js '{"posture-hands":"posture-and-hand-shape.html", ...}'
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const PUB = JSON.parse(process.argv[2] || '{}');
const OUT = path.resolve(__dirname, process.env.OUT || '../guide/tools/lessons/svg/index');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t426.html');
  const p = await H.open({ path: '?book=work&ch=front&lang=en', w: 900, h: 900 });
  await p.evaluate(() => Promise.all([document.fonts.load('700 12px Cinzel'), document.fonts.load("700 15px 'Cormorant Garamond'"), document.fonts.load("italic 700 17px 'Cormorant Garamond'")]));
  const svgs = await p.evaluate((PUB) => {
    rdCtx = null;
    const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(id => PUB[id] ? 'print' : 'new') }; });
    const nums = {}; stages.flatMap(x => x.ids).forEach((id, k) => { nums[id] = k + 1; });
    const out = {};
    for (const [L, o] of [['wide', { wide: true, dimNew: true }], ['tall', { dimNew: true }], ['og', { wide: true, dimNew: true }]]) { const h = townhouseSvg({ stages, here: null, nums }, o); out[L] = penSvg([{ k: 'raw', svg: h.svg }], { vb: h.vb, id: 'hh' + L }); }
    return out;
  }, PUB);
  fs.mkdirSync(OUT, { recursive: true });
  for (const k of ['wide', 'tall', 'og']) {
    let s = svgs[k].replace(/<g data-chapter="([^"]+)" data-status="[^"]*" data-here="0" role="button" tabindex="0" aria-label="([^"]*)" style="cursor:pointer">(<rect [^>]*\/>)<\/g>/g,
      (m, id, label, rect) => PUB[id] ? '<a tabindex="-1" href="' + PUB[id] + '" aria-label="' + label + ': read the guide">' + rect + '</a>' : '');
    // the drawing is decoration (build.py hides it from screen readers); the list under it is the real way in, so its links stay out of the tab order
    if (k === 'og') s = s.replace(/<a tabindex="-1" href="[^"]*" aria-label="[^"]*">(<rect [^>]*\/>)<\/a>/g, '');   // a picture only
    fs.writeFileSync(k === 'og' ? path.join(OUT, '..', 'house-og.svg') : OUT + '/house-' + k + '.svg', s);
    console.log(k, s.length, 'links', (s.match(/<a tabindex/g) || []).length, 'buttons left', (s.match(/role="button"/g) || []).length, (/viewBox="([^"]+)"/.exec(s) || [])[1]);
  }
  console.log('errs', p._errs.join('|'));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
