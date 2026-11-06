// Phase 425: the street for the website's lesson guides front page (lessons/index.html), replacing house379gen.js.
// Drawn by the app's own code (houseShapes + penSvg in the built drills page); windows with a published guide page
// become links and the others lose their button. Writes <OUT>/house-wide.svg, house-tall.svg (the names stay, so
// the page's {{svg:house-wide}} / {{svg:house-tall}} keep working) and <OUT>/../house-og.svg (the sharing picture).
//   BUILD=drills.t425.html OUT=../p425/guide/svg/index node street425gen.js '{"posture-hands":"posture-and-hand-shape.html"}'
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const PUB = JSON.parse(process.argv[2] || '{}');
const OUT = path.resolve(__dirname, process.env.OUT || '../guide/tools/lessons/svg/index');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t425.html');
  const p = await H.open({ path: '?book=work&ch=front&lang=en', w: 900, h: 900 });
  const svgs = await p.evaluate((PUB) => {
    const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(id => PUB[id] ? 'print' : 'new') }; });
    const nums = {}; stages.flatMap(x => x.ids).forEach((id, k) => { nums[id] = k + 1; });
    const out = {};
    for (const L of ['wide', 'tall', 'og']) { const h = houseShapes({ stages, here: null, nums, print: true }, L); out[L] = penSvg(h.shapes, { vb: [0, 0, h.W, h.H], id: 'hh' }); }
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
