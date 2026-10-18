const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?tool=cb-p-scales&lock=1&lang=ko', w: 390, h: 860, dsf: 1 }); await p.waitForTimeout(1300);
  const s0 = await p.evaluate(() => ({ url: location.search, ko: /스케일과 조/.test(document.body.innerText) }));
  console.log('fresh student KO link:', JSON.stringify(s0));
  const pad = await p.$('[data-cb="key-pad"]');
  await (await pad.$('button[role=tab]:nth-child(2)')).click(); await p.waitForTimeout(200);
  await (await pad.$('g[data-key="Gb"]')).click(); await p.waitForTimeout(200);
  await (await pad.$('a')).click(); await p.waitForTimeout(1500);
  const s1 = await p.evaluate(() => ({ url: location.search, text: document.querySelector('.pb-main').innerText.replace(/\s+/g, ' ').slice(0, 400) }));
  console.log('finder:', JSON.stringify(s1));
  await p.goBack(); await p.waitForTimeout(1500);
  const s2 = await p.evaluate(() => ({ url: location.search, ko: /스케일과 조/.test(document.body.innerText), en: /Scales and keys/.test(document.body.innerText) }));
  console.log('after back:', JSON.stringify(s2));
  await p.context().close();
  // teacher in Korean (toggle), opens a ladder chip, then back
  const q = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, dsf: 1, lang: 'ko' }); await q.waitForTimeout(1200);
  console.log('teacher toggled KO url:', await q.evaluate(() => location.search));
  await (await q.$('.cb-ladder a[href*="tool=modes"]')).click(); await q.waitForTimeout(1500);
  const t1 = await q.evaluate(() => ({ url: location.search, ko: /선법/.test(document.body.innerText), back: [...document.querySelectorAll('button')].map(b => b.innerText.trim()).filter(x => /^←/.test(x)) }));
  console.log('teacher chip:', JSON.stringify(t1));
  await q.goBack(); await q.waitForTimeout(1500);
  console.log('teacher back:', JSON.stringify(await q.evaluate(() => ({ url: location.search, ko: /스케일과 조/.test(document.body.innerText) }))));
  await q.context().close();
  await H.close();
})();
