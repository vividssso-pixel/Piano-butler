const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/sc/shots/';
(async () => {
  const H = await start('drills.t490.html');
  for (const lang of ['en', 'ko']) for (const w of [320, 390]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 900, lang });
    await p.waitForTimeout(1500); const log = [];
    const hs = async (tag) => { const o = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth); log.push(tag + ' hs=' + o); };
    const pad = p.locator('[data-cb="key-pad"]').first();
    await pad.scrollIntoViewIfNeeded(); await hs('open');
    await pad.screenshot({ path: OUT + `kp-${lang}-${w}-clock-C.png` });
    // tap Gb on the keyboard (black key 6) and read both clock and keyboard
    await pad.locator('svg g[data-key="6"]').click({ force: true }); await p.waitForTimeout(500);
    await pad.screenshot({ path: OUT + `kp-${lang}-${w}-clock-Gb.png` });
    const txt = await pad.evaluate(e => e.innerText.replace(/\s+/g, ' '));
    log.push('after Gb: ' + txt.slice(0, 220));
    await pad.locator('button[role=tab]').nth(1).click(); await p.waitForTimeout(300); await hs('circle');
    await p.waitForTimeout(500); await pad.scrollIntoViewIfNeeded(); await pad.screenshot({ path: OUT + `kp-${lang}-${w}-circle-Gb.png`, timeout: 60000 });
    await pad.locator('svg g[data-key="D"]').first().click({ force: true }); await p.waitForTimeout(300);
    log.push('circle D: ' + (await pad.evaluate(e => e.innerText.replace(/\s+/g, ' '))).slice(0, 200));
    const hts = await pad.evaluate(e => [...e.querySelectorAll('button, a.ghost-btn')].map(b => Math.round(b.getBoundingClientRect().height)));
    log.push('button heights ' + hts.join(','));
    console.log(lang, w, '\n  ' + log.join('\n  '), '\n  errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
