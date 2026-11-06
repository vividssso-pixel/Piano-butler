const { start } = require('./contentharness');
(async () => {
  const H = await start('drills.t366.html');
  for (const [lv, answer] of [[1, true], [2, true], [3, false]]) {
    const p = await H.open({ path: '?drill=posture-hands&tab=drill&level=' + lv + '&mode=lesson', w: 420, h: 1100, store: { pb_mode_v1: 'student' } });
    await p.waitForTimeout(600);
    if (answer) { const b = await p.$$('button.choice-btn'); await b[1].click(); await p.waitForTimeout(500); }
    const card = await p.$('button.choice-btn'); const box = await p.evaluate(() => { const q = [...document.querySelectorAll('div')].find(d => /^Question 1/.test(d.innerText || '') && d.getBoundingClientRect().height > 300); const r = (q || document.body).getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; });
    await p.screenshot({ path: '../rv1/dq' + lv + '.png', clip: { x: Math.max(0, box.x - 4), y: Math.max(0, box.y - 4), width: Math.min(420, box.w + 8), height: Math.min(1100 - box.y, box.h + 8) } });
    console.log(lv, JSON.stringify(box));
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
