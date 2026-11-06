// Every printed page (Lesson Books, Workbooks, teacher pages, cut-outs; en + ko): does the body overflow its A4 page?
// Prints, per path, the overflowing pages (index:px). Compare two builds by running twice.
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t448b.html');
  const p0 = await H.open({ path: '', w: 1024, h: 900 }); await p0.waitForTimeout(1000);
  const reg = await p0.evaluate(() => ({ l: Object.keys(LESSON_BOOKS), w: Object.keys(WORKBOOKS) })); await p0.context().close();
  let paths = reg.l.map(b => '?book=lesson&ch=' + b).concat(reg.w.map(b => '?book=work&ch=' + b), reg.w.map(b => '?book=teacher&ch=' + b), ['?book=cutouts&ch=all']);
  paths = paths.flatMap(x => [x + '&lang=en', x + '&lang=ko']);
  if (process.env.PART) { const [k, n] = process.env.PART.split('/').map(Number); paths = paths.filter((_, i) => i % n === k); }
  for (const path of paths) {
    const p = await H.open({ path, w: 1024, h: 900 }); await p.waitForTimeout(3000);
    const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
    const over = info.map((v, i) => [i + 1, v]).filter(([, v]) => v > 1);
    console.log(path + ' | pages ' + info.length + ' | over ' + over.map(([i, v]) => i + ':' + v).join(' '));
    await p.context().close();
  }
  await H.close();
})();
