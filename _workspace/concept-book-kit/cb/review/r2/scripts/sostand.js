const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  for (const b of ['drills.t484.html', 'drills.t485.html']) {
    const H = await start(b);
    for (const lang of ['ko', 'en']) for (const w of [320, 390]) {
      const p = await H.open({ path: '?teacher=1&tool=sharps-order', w, h: 860, lang, dsf: 1 }); await p.waitForTimeout(1200);
      const r = await p.evaluate(() => [...document.querySelectorAll('.pb-main button')].filter(x => /One|Next|Play|하나|재생/.test(x.innerText)).map(x => x.innerText.replace(/\n/g, '/') + ' ' + Math.round(x.getBoundingClientRect().height)));
      console.log(b, lang, w, JSON.stringify(r));
      await p.context().close();
    }
    await H.close();
  }
})();
