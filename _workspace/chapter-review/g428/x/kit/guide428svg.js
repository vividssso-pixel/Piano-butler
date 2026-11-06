// Phase 428: the chapter 6 guide page's drawings = the Lesson Book's own, as SVG files (the first picture of each page)
const { start } = require('./contentharness'); const fs = require('fs'), path = require('path');
const OUT = path.resolve(__dirname, process.env.OUTDIR || '../ch6/a428/site/svg/ledger-lines');
const NAMES = { 1: 'hero', 2: 'ledger-line', 3: 'sky', 4: 'sea', 5: 'between', 6: 'five-cs' };
(async () => {
  const H = await start(process.env.BUILD);
  const p = await H.open({ path: '?book=lesson&ch=ledger-lines&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(2600);
  const got = await p.evaluate(() => [...document.querySelectorAll('.lb-page')].map(pg => [...pg.querySelectorAll('[role=img]')].map(d => ({ label: d.getAttribute('aria-label'), svg: (d.tagName === 'svg' ? d : d.querySelector('svg')).outerHTML }))));
  fs.mkdirSync(OUT, { recursive: true });
  const fix = (svg) => { const m = /viewBox="([\d.\- ]+)"/.exec(svg), [, , w, h] = m[1].split(' ').map(Number);
    return svg.replace(/<svg[^>]*?viewBox="[^"]+"[^>]*>/, () => '<svg xmlns="http://www.w3.org/2000/svg" viewBox="' + m[1] + '" width="' + Math.round(w * 2) + '" height="' + Math.round(h * 2) + '">'); };
  let n = 0;
  got.forEach((arts, i) => { const name = NAMES[i + 1]; if (!name) return; const a = arts[0]; if (!a) { console.log('MISSING', i + 1); return; } fs.writeFileSync(OUT + '/' + name + '.svg', fix(a.svg)); n++; console.log(name, (a.label || '').slice(0, 80)); });
  console.log(n + ' svgs, errs', p._errs.join('|'));
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
