// Print the concept book to PDF (the real print path), EN and KO
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300 });
    await p.waitForTimeout(2500);
    await p.emulateMedia({ media: 'print' });
    await p.pdf({ path: OUT + 'book-' + lang + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
    console.log(lang, 'errs', p._errs.join('|'));
    await p.context().close();
  }
  await H.close();
})();
