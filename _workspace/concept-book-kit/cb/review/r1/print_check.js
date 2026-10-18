const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300, dsf: 2 });
    await p.waitForTimeout(800);
    const txt = await p.evaluate(() => document.body.innerText);
    require('fs').writeFileSync('/home/claude/pbtest/cb/review/r1/book-' + lang + '.txt', txt);
    const n = await p.evaluate(() => document.querySelectorAll('.lb-page, .wb-page, [data-page]').length);
    console.log(lang, 'pages-ish', n, 'errs', p._errs);
    // screenshot page 4 and 6 at 2x
    const pages = await p.$$('.lb-page');
    console.log('lb-page count', pages.length);
    for (const i of [3, 5]) if (pages[i]) await pages[i].screenshot({ path: '/home/claude/pbtest/cb/review/r1/p' + (i + 1) + '-' + lang + '.png' });
    await p.context().close();
  }
  const p = await H.open({ path: '?teacher=1&view=toolbox', w: 390, h: 860 });
  const tools = await p.evaluate(() => ['ssc-steps','ssc-g','ssc-f','skg-five','build-major','sharps-order','flats-order','relative-minor','minor-forms','circle-fifths','place-it','build-minor','scale-finder','all-keys','csx-penta','chromatic','modes','cb-p-scales'].map(id => { const t = TOOLS.find(x => x.id === id); return id + ' :: ' + (t ? t.title + ' — ' + t.blurb + ' [ch ' + t.ch + ']' : 'MISSING'); }));
  console.log(tools.join('\n'));
  await p.context().close(); await H.close();
})();
