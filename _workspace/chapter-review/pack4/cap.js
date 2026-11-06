const { start } = require('../contentharness');
(async () => {
  let H = await start('drills.sf401.html');
  let p = await H.open({ path: '?book=lesson&ch=staff&lang=en&draft=1', w: 900, h: 1200 });
  await p.waitForTimeout(3500);
  await p.pdf({ path: 'pack4/lesson-draft.pdf', preferCSSPageSize: true, printBackground: true });
  await p.context().close(); await H.close();
  H = await start('drills.t400.html');
  for (const kind of ['work', 'teacher']) {
    p = await H.open({ path: '?book=' + kind + '&ch=staff&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(3000);
    console.log(kind, (await p.$$('.bk-page')).length);
    await p.pdf({ path: 'pack4/' + kind + '.pdf', preferCSSPageSize: true, printBackground: true });
    await p.context().close();
  }
  // the online lesson as it is today: the head with its 8 steps
  p = await H.open({ path: '?drill=staff', w: 390, h: 1100 });
  await p.waitForTimeout(1500);
  await p.screenshot({ path: 'pack4/app-head.png' });
  const tab = await p.$('button:has-text("Drill")'); await tab.click(); await p.waitForTimeout(700);
  for (const n of [1, 2, 3, 4]) { await (await p.$('button:has-text("Level ' + n + '")')).click(); await p.waitForTimeout(900); await p.screenshot({ path: 'pack4/drill-l' + n + '.png', clip: { x: 0, y: 120, width: 390, height: 640 } }); }
  console.log('errs', p._errs.join('|'));
  await H.close(); process.exit(0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
