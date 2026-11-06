const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t369.html');
  for (const lv of [1, 2, 3]) {
    const p = await H.open({ path: '?drill=posture-hands&tab=drill&level=' + lv + '&lang=en', w: 520, h: 900 });
    await p.waitForTimeout(1500);
    // press a start button if the drill waits for one
    const btn = await p.$('button:has-text("Start")'); if (btn) { await btn.click().catch(() => {}); await p.waitForTimeout(800); }
    const arts = await p.$$eval('.pb-art', els => els.map(e => e.dataset.art + ':' + Math.round(e.getBoundingClientRect().width) + 'x' + Math.round(e.getBoundingClientRect().height)));
    const lit = await p.$$eval('.pb-art svg [fill="#e4572e"]', els => els.length);
    console.log('level', lv, JSON.stringify(arts), 'coral parts', lit, 'errs', p._errs.join('|').slice(0, 200));
    await p.screenshot({ path: '../rv1/drill369-' + lv + '.png' });
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
