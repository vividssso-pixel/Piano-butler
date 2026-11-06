// "Set up the stool" in pen: each preset, the footstool, the front view; and what the checks say
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t376.html');
  const p = await H.open({ path: '?tool=sit-check', w: 520, h: 1000 });
  await p.waitForTimeout(600);
  const box = await p.$('[data-pen-sit]');
  const res = [];
  for (const name of ['Just right', 'Stool too low', 'Stool too high', 'Too close', 'Too far']) {
    await p.click('[data-pen-sit] button.chip:text-is("' + name + '")'); await p.waitForTimeout(150);
    res.push([name, await p.$$eval('[data-pen-sit] [data-check]', els => els.map(e => e.dataset.check + ':' + e.dataset.ok).join(' '))]);
    await (await p.$('[data-pen-sit] [role=img]')).screenshot({ path: '../shots/sit376-' + name.replace(/ /g, '') + '.png' });
  }
  await p.click('[data-pen-sit] button.chip:text-is("Stool too high")'); await p.click('[data-pen-sit] input[type=checkbox]'); await p.waitForTimeout(150);
  res.push(['high + footstool', await p.$$eval('[data-pen-sit] [data-check]', els => els.map(e => e.dataset.check + ':' + e.dataset.ok).join(' '))]);
  await (await p.$('[data-pen-sit] [role=img]')).screenshot({ path: '../shots/sit376-footstool.png' });
  // slider sweep: no errors, the good zone exists
  let good = 0;
  for (let h = 0; h <= 30; h += 2) for (let d = 0; d <= 44; d += 4) {
    await p.$eval('#pen-sit-h', (e, v) => { const s = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set; s.call(e, v); e.dispatchEvent(new Event('input', { bubbles: true })); }, String(h));
    await p.$eval('#pen-sit-d', (e, v) => { const s = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set; s.call(e, v); e.dispatchEvent(new Event('input', { bubbles: true })); }, String(d));
    if (await p.$$eval('[data-pen-sit] [data-ok="1"]', els => els.length) === 3) good++;
  }
  res.push(['good cells in sweep (with footstool)', good]);
  await p.click('[data-pen-sit] button.chip:text-is("Front view")'); await p.waitForTimeout(150);
  await (await p.$('[data-pen-sit] [role=img]')).screenshot({ path: '../shots/sit376-front.png' });
  await p.$eval('[data-pen-sit] input[type=range]', (e) => { const s = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set; s.call(e, '45'); e.dispatchEvent(new Event('input', { bubbles: true })); });
  await p.waitForTimeout(150);
  await (await p.$('[data-pen-sit] [role=img]')).screenshot({ path: '../shots/sit376-front-ok.png' });
  console.log(JSON.stringify(res, null, 0), 'errs', p._errs.join(' | ').slice(0, 300));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
