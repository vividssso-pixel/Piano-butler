// reg674, sturdier: each page's context is closed after it, and if the browser falls over on a page that page is named
// (CRASH) and the browser restarted, so one bad page cannot hide the rest. Usage: node reg807.js drills.t807.html [en|ko|both]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const B = process.argv[2] || 'drills.t807.html', LANGS = (process.argv[3] && process.argv[3] !== 'both') ? [process.argv[3]] : ['en', 'ko'];
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  let H = await start(B);
  const q0 = await H.open({ path: '?teacher=1&view=home&area=pitch', w: 390, h: 900, lang: 'en' }); await sleep(400);
  const info = await q0.evaluate(() => { const L = [], D = []; Object.values(HOME_LIVE).forEach(v => { (v.lessons || []).forEach(x => L.push(x)); (v.groups || []).forEach(g => { g.lessons.forEach(x => L.push(x)); if (g.check) D.push([g.check, g.level || 1]); }); if (v.check) D.push([v.check, 1]); }); return { L, D }; });
  await q0.context().close();
  let bad = 0, crash = 0, n = 0;
  const visit = async (label, path, press, wait) => {
    let q = null;
    try {
      q = await H.open({ path, w: 390, h: 1000, lang: label[0] }); await sleep(wait);
      if ((q._errs || []).length) { bad++; console.log('ERR', label.join(' '), q._errs[0]); }
      const b = q.locator(press); if (await b.count()) { await b.first().click(); await sleep(250); if ((q._errs || []).length) { bad++; console.log('ERR after a tap', label.join(' '), q._errs[0]); } }
      await q.context().close().catch(() => {});
    } catch (e) { crash++; console.log('CRASH', label.join(' '), String(e.message).split('\n')[0]); try { await H.close(); } catch (e2) {} H = await start(B); }
    if (++n % 100 === 0) console.error('…', n);
  };
  for (const lang of LANGS) {
    for (const id of info.L) await visit([lang, 'lesson', id], '?teacher=1&tool=' + id, 'button:has-text("One by one"), button:has-text("하나씩")', 350);
    for (const [d, l] of info.D) await visit([lang, 'drill', d, l], `?teacher=1&view=home&drill=${d}&tab=drill&level=${l}&mode=lesson`, '.choice-btn', 500);
  }
  console.log('lessons', info.L.length, 'drills', info.D.length, 'errors', bad, 'crashes', crash);
  await H.close(); process.exit(0);
})();
