const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t376.html');
  for (const id of ['sit-check', 'arm-moves', 'hand-shape', 'finger-numbers', 'finger-walks', 'posture-check', 'arm-alignment', 'finger-friends']) {
    const p = await H.open({ path: '?tool=' + id, w: 390, h: 900 }); await p.waitForTimeout(500);
    const r = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, pen: document.querySelectorAll('[data-pen-sit], [data-warmups], [data-round-hand], [data-finger-numbers]').length, h: document.body.innerText.length }));
    console.log(id.padEnd(15), JSON.stringify(r), p._errs.join('|').slice(0, 150));
    await p.context().close();
  }
  await H.close();
})();
