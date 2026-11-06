const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t371.html');
  const p = await H.open({ path: '?drill=posture-hands&lang=en', w: 520, h: 1100 });
  await p.waitForTimeout(1500);
  const y = await p.evaluate(() => { const el = [...document.querySelectorAll('.try-box')].find(b => /Move with the whole arm/.test(b.innerText)); return el.getBoundingClientRect().top + window.scrollY; });
  await p.evaluate(y => window.scrollTo(0, y - 10), y); await p.waitForTimeout(500);
  await p.screenshot({ path: '../rv1/app371-arm.png' });
  const order = await p.evaluate(() => { const el = [...document.querySelectorAll('.try-box')].find(b => /Move with the whole arm/.test(b.innerText)); return [...el.querySelectorAll('button.chip')].map(b => b.innerText.trim()).slice(0, 6); });
  console.log(JSON.stringify(order));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
