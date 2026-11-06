// today's chapter 5 app lesson (before the review) -- screenshots for the pack
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  const p = await H.open({ path: '?drill=whole-staff', w: 420, h: 900 });
  await p.waitForTimeout(2500);
  const H0 = await p.evaluate(() => document.documentElement.scrollHeight);
  console.log('height', H0, p._errs.join('|'));
  let i = 0;
  for (let y = 0; y < Math.min(H0, 5400); y += 900) { await p.evaluate(yy => window.scrollTo(0, yy), y); await p.waitForTimeout(400); await p.screenshot({ path: 'app419-' + (++i) + '.png' }); }
  // the drill: level 1 question
  const p2 = await H.open({ path: '?drill=whole-staff&tab=drill&level=1', w: 420, h: 900 });
  await p2.waitForTimeout(2500); await p2.screenshot({ path: 'app419-drill.png' });
  await H.close();
})();
