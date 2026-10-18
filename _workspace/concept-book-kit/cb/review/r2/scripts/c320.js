const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/orig/';
(async () => {
  const H = await start(process.env.BUILD || 'drills.t485.html');
  const routes = ['?teacher=1&drill=scales&tab=learn', '?teacher=1&drill=key-signatures&tab=learn', '?teacher=1&tool=build-major', '?teacher=1&tool=sharps-order', '?teacher=1&tool=cb-p-scales', '?teacher=1&drill=posture-hands&tab=learn'];
  for (const lang of ['en', 'ko']) for (const r of routes) {
    const p = await H.open({ path: r, w: 320, h: 760, lang, dsf: 1 }); await p.waitForTimeout(1500);
    // open every step so its content renders
    for (let k = 0; k < 12; k++) { const b = await p.$$('section button[aria-expanded="false"]'); if (!b.length) break; try { await b[0].click(); } catch (e) {} await p.waitForTimeout(80); }
    const res = await p.evaluate(() => {
      const hs = document.documentElement.scrollWidth - document.documentElement.clientWidth;
      const rem = [...document.querySelectorAll('.lb-remember')].map(r => { const rr = r.getBoundingClientRect(); let over = 0; r.querySelectorAll('*').forEach(c => { const b = c.getBoundingClientRect(); if (b.width) over = Math.max(over, b.right - rr.right); }); return Math.round(over); });
      const small = [...document.querySelectorAll('button, a.chip, a.ghost-btn')].filter(b => { const r = b.getBoundingClientRect(); return r.width > 0 && r.height > 0 && r.height < 40 && !b.closest('.lb-pic') && getComputedStyle(b).visibility !== 'hidden'; }).map(b => (b.innerText || b.getAttribute('aria-label') || '').trim().slice(0, 14) + ':' + Math.round(b.getBoundingClientRect().height));
      const boxOver = [...document.querySelectorAll('.try-box')].map(bx => { const br = bx.getBoundingClientRect(); let o = 0; bx.querySelectorAll('button').forEach(c => { const b = c.getBoundingClientRect(); if (b.width) o = Math.max(o, b.right - br.right); }); return Math.round(o); }).filter(x => x > 0);
      return { hs, remOver: rem.filter(x => x > 1), small: [...new Set(small)].slice(0, 12), boxOver };
    });
    console.log(lang, r, JSON.stringify(res), p._errs.join('|').slice(0, 200));
    if (lang === 'en' && /scales&|key-sig|build-major/.test(r)) await p.screenshot({ path: OUT + 'c320-' + r.replace(/[^a-z]/g, '').slice(0, 30) + '.png', fullPage: true });
    await p.context().close();
  }
  await H.close();
})();
