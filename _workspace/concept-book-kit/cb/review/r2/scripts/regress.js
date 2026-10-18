// Shared components, old (t484) vs new (t485): sideways scroll, anything poking past the viewport or past its rounded
// box, the five-checks rows, REMEMBER bands, the header. Chapters 16 and 19, posture, the build-major and order tools.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const routes = (process.env.ROUTES || '?teacher=1&drill=scales&tab=learn,?teacher=1&drill=key-signatures&tab=learn,?teacher=1&drill=posture-hands&tab=learn,?teacher=1&drill=first-steps&tab=learn,?teacher=1&tool=build-major,?teacher=1&tool=sharps-order,?teacher=1&tool=flats-order,?drill=scales&tab=learn&lock=1').split(',');
  const builds = ['drills.t484.html', 'drills.t485.html'];
  const res = {};
  for (const b of builds) {
    const H = await start(b);
    for (const r of routes) for (const lang of ['en', 'ko']) for (const w of (process.env.W || '320,390').split(',').map(Number)) {
      const p = await H.open({ path: r, w, h: 800, lang, dsf: 1 }); await p.waitForTimeout(1300);
      const o = await p.evaluate((vw) => {
        const hs = document.documentElement.scrollWidth - document.documentElement.clientWidth;
        const past = []; document.querySelectorAll('.pb-main *').forEach(e => { const b = e.getBoundingClientRect(); if (b.width && b.right > vw + 0.5 && !e.closest('[style*="overflow-x"],[style*="overflow: auto"]')) past.push((e.innerText || e.tagName).trim().replace(/\s+/g, ' ').slice(0, 18) + ':' + Math.round(b.right - vw)); });
        // the five-checks rows: buttons past the row's own border
        const five = []; document.querySelectorAll('button').forEach(bt => { if (!/Got it|됐어요/.test(bt.innerText)) return; const row = bt.parentElement.parentElement; const rb = row.getBoundingClientRect(), bb = bt.getBoundingClientRect(); if (bb.right > rb.right + 0.5) five.push(Math.round(bb.right - rb.right)); });
        const rem = [...document.querySelectorAll('.lb-remember')].map(r => { const rr = r.getBoundingClientRect(); let over = 0; r.querySelectorAll('*').forEach(c => { const b = c.getBoundingClientRect(); if (b.width) over = Math.max(over, b.right - rr.right); }); return Math.round(over); }).filter(x => x > 1);
        return { hs, past: [...new Set(past)].slice(0, 6), five: [...new Set(five)], rem };
      }, w);
      res[b + '|' + r + '|' + lang + '|' + w] = o;
      if (process.env.SHOT && w === 320 && lang === 'en') await p.screenshot({ path: OUT + 'rg-' + b.slice(8, 12) + '-' + r.replace(/[^a-z]/g, '').slice(6, 30) + '.png', fullPage: true });
      await p.context().close();
    }
    await H.close();
  }
  for (const k of Object.keys(res).filter(k => k.startsWith('drills.t485'))) {
    const old = res[k.replace('t485', 't484')], nw = res[k];
    const same = JSON.stringify(old) === JSON.stringify(nw);
    console.log((same ? 'same ' : 'DIFF ') + k.slice(17) + '\n   484 ' + JSON.stringify(old) + '\n   485 ' + JSON.stringify(nw));
  }
})();
