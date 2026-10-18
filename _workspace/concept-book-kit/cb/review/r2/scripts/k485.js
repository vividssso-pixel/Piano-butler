const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/orig/';
const what = (process.env.WHAT || 'book,screen').split(',');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t485.html');
  if (what.includes('book')) for (const lang of (process.env.LANGS || 'en,ko').split(',')) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300 }); await p.waitForTimeout(2600);
    const pages = await p.$$('[data-lb-page]');
    for (const pg of pages) { const n = await pg.getAttribute('data-lb-page'); await pg.screenshot({ path: OUT + 'cb-' + lang + '-' + n + '.png' }); }
    const fit = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); const kids = [...b.children]; const last = kids[kids.length - 1].getBoundingClientRect(), bb = b.getBoundingClientRect();
      return Math.round(b.scrollHeight - b.clientHeight) + '/' + Math.round(bb.bottom - last.bottom); }));
    const pic = await p.evaluate(() => [...document.querySelectorAll('[data-lb-page]')].map(pg => { const pic = pg.querySelector('.lb-pic'); if (!pic) return '-';
      const pb = pic.getBoundingClientRect(); let lo = 1e9, hi = -1e9;
      pic.querySelectorAll(':scope > *:not(svg)').forEach(c => { const b = c.getBoundingClientRect(); if (b.height > 0) { lo = Math.min(lo, b.top); hi = Math.max(hi, b.bottom); } });
      return Math.round(lo - pb.top) + '/' + Math.round(pb.bottom - hi) + ' f' + ((hi - lo) / pb.height).toFixed(2); }));
    console.log('book', lang, pages.length, 'over/free', fit.join(' '), '| pic', pic.join('  '), p._errs.join('|').slice(0, 300)); await p.context().close();
  }
  if (what.includes('screen')) for (const lang of (process.env.LANGS || 'en,ko').split(',')) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, lang, dsf: 1.5 }); await p.waitForTimeout(1800);
    await p.screenshot({ path: OUT + 'scr-' + lang + '.png', fullPage: true });
    const hor = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    console.log('screen', lang, 'hscroll', hor, 'errs', p._errs.join('|').slice(0, 300)); await p.context().close();
  }
  await H.close();
})();
