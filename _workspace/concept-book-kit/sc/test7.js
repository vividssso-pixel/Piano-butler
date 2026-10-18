const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t487.html');
  for (const lang of ['en','ko']) {
    const p = await H.open({ path: '?teacher=1', w: 390, h: 900, lang });
    const b = p.locator('text=/^(Toolbox|도구함)$/').first(); await b.click(); await p.waitForTimeout(900);
    const txt = await p.evaluate(() => document.body.innerText);
    const names = lang==='en' ? ['Key finder','Circle of fifths','Order of sharps','Order of flats','Place the key signature','Relative minor','All 15 key signatures','G major','F major','Every F','Name the key','Transpose a tune','Key signature and accidental','Scale finder'] : ['조 찾기','5도권','샤프의 순서','플랫의 순서','조표 자리 찾기','나란한조','조표 15개 전부','G장조','F장조','모든 F','조 이름','조표와 임시표','스케일 찾기'];
    console.log(lang, names.map(n => n + ':' + (txt.split(n).length - 1)).join(' | '), 'errs', JSON.stringify(p._errs));
    await p.screenshot({ path: '/home/claude/pbtest/sc/shots/kf-' + lang + '-toolbox.png', fullPage: true });
  }
  await H.close();
})();
