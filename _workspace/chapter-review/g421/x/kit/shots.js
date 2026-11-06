// BUILD=... TAG=... node shots.js  -> screenshots of chosen book pages
const { start } = require(process.env.HARNESS || '../kit/contentharness');
const path = require('path');
(async () => {
  const H = await start(process.env.BUILD), TAG = process.env.TAG, OUT = process.env.OUT || '.';
  const jobs = JSON.parse(process.env.JOBS);   // [[book, ch, [pages]]]
  for (const [book, ch, pages] of jobs) {
    const p = await H.open({ path: '?book=' + book + '&ch=' + ch + '&lang=en', w: 900, h: 1200, dsf: +(process.env.DSF || 1) });
    await p.waitForTimeout(2600);
    const els = await p.$$('.bk-page');
    for (const n of pages) if (els[n - 1]) await els[n - 1].screenshot({ path: path.join(OUT, TAG + '-' + book + '-' + ch + '-' + n + '.png') });
    console.log(book, ch, els.length);
    await p.context().close();
  }
  await H.close();
})();
