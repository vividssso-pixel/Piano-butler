// node pgshot.js BUILD book ch lang pages(out prefix) -- screenshot book pages (.bk-page) by index (1-based)
const { start } = require('./contentharness');
(async () => { const [B, book, ch, lang, pages, out] = process.argv.slice(2);
  const H = await start(B); const p = await H.open({ path: '?book=' + book + '&ch=' + ch + '&lang=' + lang, w: 1100, h: 1400, dsf: 1.5 });
  const els = await p.$$('.bk-page'); for (const n of pages.split(',').map(Number)) if (els[n - 1]) await els[n - 1].screenshot({ path: (out || '/tmp/pg') + '-' + n + '.png' });
  console.log('pages', els.length, p._errs.slice(0, 2)); await H.close(); })();
