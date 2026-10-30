// collect each chapter's lesson text (en, ko) from the Lesson Book pages
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => { const H = await start(process.argv[2]); const q0 = await H.open({ path: '?drill=staff', w: 900, h: 900 }); await sleep(600); const ids = await q0.evaluate(() => pathIds()); await q0.close();
  const out = {};
  for (const id of ids) { out[id] = {}; for (const lang of ['en', 'ko']) { const p = await H.open({ path: '?book=lesson&ch=' + id + '&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await sleep(1000);
    out[id][lang] = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map(pg => [...pg.querySelectorAll('.lb-say, .lb-piano, .lb-guess, .lb-challenge, .lb-remember, [class*=lb-]')].length ? pg.innerText : pg.innerText)); await p.close(); } }
  require('fs').writeFileSync(process.argv[3], JSON.stringify(out)); console.log('chapters', ids.length); await H.close(); })();
