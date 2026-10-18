const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t487.html');
  for (const lang of ['en','ko']) {
    const p = await H.open({ path: '?teacher=1&tool=sharps-order', w: 390, h: 900, lang });
    for (const id of ['sharps-order','flats-order','place-it','relative-minor','circle-fifths','all-keys','skg-g','skg-f','skg-five','transpose']) {
      await p.goto(p.url().replace(/tool=[a-z-]+/, 'tool=' + id)); await p.waitForTimeout(500);
      const n = await p.evaluate(() => document.body.innerText.length);
      console.log(lang, id, n);
    }
    console.log(lang, 'errs', JSON.stringify(p._errs));
    const q = await H.open({ path: '?teacher=1&book=concept&ch=p-scales', w: 390, h: 900, lang });
    await q.waitForTimeout(600); console.log(lang, 'book errs', JSON.stringify(q._errs));
    const t = await H.open({ path: '?teacher=1', w: 390, h: 900, lang });
    await t.locator('text=' + (lang==='en'?'Toolbox':'도구함')).first().click().catch(()=>{}); await t.waitForTimeout(500);
    const txt = await t.evaluate(() => document.body.innerText);
    console.log(lang, 'toolbox has Key finder/조 찾기:', /Key finder|조 찾기/.test(txt), 'circle card visible:', /Circle of fifths|5도권/.test(txt), 'errs', JSON.stringify(t._errs));
  }
  await H.close();
})();
