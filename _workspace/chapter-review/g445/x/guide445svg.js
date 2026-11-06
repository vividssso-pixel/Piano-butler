// Phase 445: the chapter 11 guide page's drawings = the Lesson Book's own, as SVG files (the first picture of each page)
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const OUT = path.resolve(__dirname, process.env.OUTDIR || '../fix445/site/svg/tones');
const NAMES = { 1: ['hero'], 2: ['half-step'], 3: ['whole-step'], 4: ['white-half-steps'], 5: ['sharp-flat'], 6: ['staff-treble', 'staff-bass'] };
(async () => {
  const H = await start(process.env.BUILD);
  const p = await H.open({ path: '?book=lesson&ch=tones&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(2600);
  const got = await p.evaluate(() => [...document.querySelectorAll('.lb-page')].map(pg => [...pg.querySelectorAll('[role=img]')].map(d => ({ label: d.getAttribute('aria-label'), svg: (d.tagName === 'svg' ? d : d.querySelector('svg')).outerHTML }))));
  fs.mkdirSync(OUT, { recursive: true });
  const fix = (svg) => { const m = /viewBox="([\d.\- ]+)"/.exec(svg), [, , w, h] = m[1].split(' ').map(Number);
    return svg.replace(/<svg[^>]*?viewBox="[^"]+"[^>]*>/, () => '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + m[1] + '" width="' + Math.round(w * 2) + '" height="' + Math.round(h * 2) + '">'); };
  let n = 0;
  got.forEach((arts, i) => (NAMES[i + 1] || []).forEach((name, k) => { const a = arts[k]; if (!a) { console.log('MISSING', i + 1, k); return; } fs.writeFileSync(OUT + '/' + name + '.svg', fix(a.svg)); n++; console.log(name, (a.label || '').slice(0, 80)); }));
  console.log(n + ' svgs, errs', p._errs.join('|'));
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
