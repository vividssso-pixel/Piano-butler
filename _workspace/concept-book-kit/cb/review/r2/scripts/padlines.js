const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 1024, h: 900, lang, dsf: 1 }); await p.waitForTimeout(1300);
    const pad = await p.$('[data-cb="key-pad"]');
    for (const k of ['B', 'Db', 'Gb', 'F']) { const g = await pad.$$('g[data-key="' + k + '"]'); await g[g.length - 1].click(); await p.waitForTimeout(150);
      console.log(lang, 'keypad', k, JSON.stringify(await pad.evaluate(el => [...el.querySelectorAll('div')].map(d => d.innerText).filter(x => /major|장조/.test(x) && x.length < 160).slice(-1)[0]))); }
    const sp = (await p.$$('[data-cb="shapes-pad"]'))[0];
    await (await sp.$('button:has-text("' + (lang === 'ko' ? '가락' : 'Melodic') + '")')).click(); await p.waitForTimeout(150);
    const gs = await sp.$$('g[data-key="Ab"]'); if (gs.length) { await gs[0].click(); await p.waitForTimeout(150); }
    console.log(lang, 'shapes melodic Ab', JSON.stringify(await sp.evaluate(el => el.innerText.replace(/\s+/g, ' ').slice(0, 600))));
    await p.context().close();
  }
  await H.close();
})();
