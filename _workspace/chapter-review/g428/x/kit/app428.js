// chapter 6 on screen: each moving part, en and ko, at phone width
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=ledger-lines', w: 390, h: 1000, lang });
    await p.waitForTimeout(2200);
    await p.screenshot({ path: 'app428-' + lang + '-top.png' });
    const boxes = await p.$$('.try-box');
    for (let i = 0; i < boxes.length; i++) await boxes[i].screenshot({ path: 'app428-' + lang + '-box' + (i + 1) + '.png' });
    console.log(lang, boxes.length, 'boxes', p._errs.join('|'));
    await p.context().close();
  }
  await H.close();
})();
