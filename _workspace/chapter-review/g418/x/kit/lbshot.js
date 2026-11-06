// screenshot the Lesson Book pages of a chapter: BUILD=... CH=... TAG=... node lbshot.js
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD), CH = process.env.CH, TAG = process.env.TAG;
  const p = await H.open({ path: '?book=lesson&ch=' + CH + '&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(2600);
  const pages = await p.$$('.bk-page');
  const only = (process.env.PAGES || '').split(',').filter(Boolean).map(Number);
  for (let i = 0; i < pages.length; i++) if (!only.length || only.includes(i + 1)) await pages[i].screenshot({ path: TAG + '-' + (i + 1) + '.png' });
  console.log('pages', pages.length);
  await H.close();
})();
