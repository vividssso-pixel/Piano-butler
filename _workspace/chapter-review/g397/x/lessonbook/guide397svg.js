// Phase 397: the chapter 3 guide page's drawings = the Lesson Book's own pen-and-ink drawings, as SVG files
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const OUT = path.resolve(__dirname, 'p397/svg/note-names');
const NAMES = { 1: ['hero'], 2: ['a-to-g'], 3: ['wheel'], 4: ['forwards-backwards'], 5: ['who-lives'], 6: ['skip'], 7: ['play-cde'] };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t397.html');
  const p = await H.open({ path: '?book=lesson&ch=note-names&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(1600);
  const got = await p.evaluate(() => [...document.querySelectorAll('.lb-page')].map(pg => [...pg.querySelectorAll('[role=img]')].filter(d => d.querySelector('svg')).map(d => ({ label: d.getAttribute('aria-label') || '', svg: d.querySelector('svg').outerHTML }))));
  fs.mkdirSync(OUT, { recursive: true });
  const fix = (svg) => { const m = /viewBox="([\d.\- ]+)"/.exec(svg), [, , w, h] = m[1].split(' ').map(Number);
    return svg.replace(/<svg[^>]*?viewBox="[^"]+"[^>]*>/, (t) => '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + m[1] + '" width="' + Math.round(w * 2) + '" height="' + Math.round(h * 2) + '">'); };
  let n = 0;
  got.forEach((arts, i) => (NAMES[i + 1] || []).forEach((name, k) => { if (!arts[k]) { console.log('MISSING', i + 1, k); return; } fs.writeFileSync(OUT + '/' + name + '.svg', fix(arts[k].svg)); n++; console.log(name, arts[k].label.slice(0, 70)); }));
  console.log(n, 'svgs, errs', p._errs.join('|'));
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
