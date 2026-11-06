// Phase 463: the guides' changed drawings: chapter 3's beat-or-rhythm (walk, run-ning) and chapter 6's steps and skips
// (now two staves: steps up and down; skips line to line and space to space, up and down), stacked into one SVG
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const OUT = path.resolve(__dirname, process.env.OUTDIR);
const grab = async (H, ch, page) => { const p = await H.open({ path: '?book=lesson&ch=' + ch + '&lang=en', w: 900, h: 1200 }); await p.waitForTimeout(2600);
  const got = await p.evaluate((n) => [...document.querySelectorAll('[data-lb-page="' + n + '"] [role=img]')].map(d => ({ label: d.getAttribute('aria-label'), svg: (d.tagName === 'svg' ? d : d.querySelector('svg')).outerHTML })), page);
  await p.context().close(); return got; };
const vb = (svg) => /viewBox="([\d.\- ]+)"/.exec(svg)[1].split(' ').map(Number);
const solo = (svg) => { const [x, y, w, h] = vb(svg); return svg.replace(/<svg[^>]*?viewBox="[^"]+"[^>]*>/, () => '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + [x, y, w, h].join(' ') + '" width="' + Math.round(w * 2) + '" height="' + Math.round(h * 2) + '">'); };
const stack = (svgs, gap = 6) => { let y = 0, W = 0; const parts = svgs.map(s => { const [x0, y0, w, h] = vb(s); W = Math.max(W, w);
  const inner = s.replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, ''); const out = '<svg x="0" y="' + y + '" width="' + w + '" height="' + h + '" viewBox="' + [x0, y0, w, h].join(' ') + '">' + inner + '</svg>'; y += h + gap; return out; });
  const H = y - gap; return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + W + ' ' + H + '" width="' + Math.round(W * 2) + '" height="' + Math.round(H * 2) + '">' + parts.join('') + '</svg>'; };
(async () => {
  const H = await start(process.env.BUILD);
  const pl = await grab(H, 'pulse', 5); fs.writeFileSync(OUT + '/pulse/beat-rhythm.svg', solo(pl[0].svg)); console.log('beat-rhythm', pl[0].label.slice(0, 80));
  const sf = await grab(H, 'staff', 3); fs.writeFileSync(OUT + '/staff/steps-skips.svg', stack(sf.map(a => a.svg))); console.log('steps-skips', sf.length, 'staves');
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
