// node pgshot2.js BUILD path out -- screenshot every .bk-page of a book url (e.g. '?book=lesson&ch=tones&lang=en&draft=1')
const { start } = require('./contentharness');
(async () => { const [B, path, out] = process.argv.slice(2);
  const H = await start(B); const p = await H.open({ path, w: 1100, h: 1400, dsf: 1.5 }); await p.waitForTimeout(1200);
  const els = await p.$$('.bk-page'); for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: out + '-' + (i + 1) + '.png' });
  console.log('pages', els.length, p._errs.slice(0, 3)); await H.close(); })();
