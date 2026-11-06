// Phase 379: the house for the website's lesson guides front page (lessons/index.html).
// Drawn by the app's own code (houseShapes + penSvg in the built drills page), then rooms with a published guide
// page become links and the others lose their button. Writes tools/lessons/svg/index/house-wide.svg and house-tall.svg.
//   BUILD=drills.t378b.html node house379gen.js '{"posture-hands":"posture-and-hand-shape.html"}'
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const PUB = JSON.parse(process.argv[2] || '{}');
const OUT = path.resolve(__dirname, '../guide/tools/lessons/svg/index');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t378b.html');
  const p = await H.open({ path: '?book=work&ch=front&lang=en', w: 900, h: 900 });
  const svgs = await p.evaluate((PUB) => {
    const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(id => PUB[id] ? 'print' : 'new') }; });
    const nums = {}; stages.flatMap(x => x.ids).forEach((id, k) => { nums[id] = k + 1; });
    const out = {};
    for (const wide of [true, false]) { const h = houseShapes({ stages, here: null, nums, print: true }, wide); out[wide ? 'wide' : 'tall'] = penSvg(h.shapes, { vb: [0, 0, h.W, h.H], id: 'hh' }); }
    return out;
  }, PUB);
  fs.mkdirSync(OUT, { recursive: true });
  for (const k of ['wide', 'tall']) {
    let s = svgs[k].replace(/<g data-chapter="([^"]+)" data-status="[^"]*" data-here="0" role="button" tabindex="0" aria-label="([^"]*)" style="cursor:pointer">(<rect [^>]*\/>)<\/g>/g,
      (m, id, label, rect) => PUB[id] ? '<a tabindex="-1" href="' + PUB[id] + '" aria-label="' + label + ': read the guide">' + rect + '</a>' : '');
    // the drawing is decoration (build.py hides it from screen readers); the list under it is the real way in, so its links stay out of the tab order
    fs.writeFileSync(OUT + '/house-' + k + '.svg', s);
    console.log(k, s.length, 'links', (s.match(/<a tabindex/g) || []).length, 'buttons left', (s.match(/role="button"/g) || []).length);
  }
  console.log('errs', p._errs.join('|'));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
