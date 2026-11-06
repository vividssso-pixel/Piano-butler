const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t371.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=posture-hands&lang=' + lang, w: 520, h: 1000 });
    await p.waitForTimeout(1500);
    const steps = await p.$$eval('[id*="-step-"]', els => els.filter(e => /-step-\d+$/.test(e.id)).map(e => e.id));
    const titles = await p.$$eval('[id*="-step-"]', els => els.filter(e => /-step-\d+$/.test(e.id)).map(e => (e.innerText || '').split('\n')[0].slice(0, 40)));
    const arts = await p.$$eval('.pb-art', els => els.map(e => e.dataset.art));
    const chips = await p.$$eval('.try-box button.chip', els => els.slice(0, 8).map(e => e.innerText.trim()));
    console.log(lang, 'steps', steps.length, JSON.stringify(titles), '\n arts', JSON.stringify(arts), '\n first chips', JSON.stringify(chips), '\n errs', p._errs.join('|').slice(0, 200));
    if (lang === 'en') {
      // play along on the first tune: circles should light up in turn
      const btn = await p.$('button:has-text("Play along")');
      await btn.scrollIntoViewIfNeeded(); await btn.click(); await p.waitForTimeout(1000);
      const lit = await p.$$eval('.try-box span', els => els.filter(e => getComputedStyle(e).backgroundColor === 'rgb(228, 87, 46)').length);
      console.log(' play along: coral circles lit now', lit);
      const fw = await p.$('text=Play: finger walks');
      for (const [sel, file] of [['text=Move with the whole arm', 'app371-arm'], ['text=A round hand', 'app371-hand'], ['button:has-text("Stop")', 'app371-walks'], ['text=My five checks', 'app371-check']]) {
        const el = await p.$(sel); if (!el) { console.log('missing', sel); continue; }
        await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(400);
        const box = await el.evaluate(e => { const b = (e.closest('.try-box') || e.parentElement).getBoundingClientRect(); return { y: b.top + window.scrollY }; });
        await p.evaluate(y => window.scrollTo(0, Math.max(0, y - 120)), box.y); await p.waitForTimeout(300);
        await p.screenshot({ path: '../rv1/' + file + '.png' });
      }
    }
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
