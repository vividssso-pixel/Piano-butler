// Audit: the Beginner floor's Lesson Books and Workbooks as they print today
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/bk/';
require('fs').mkdirSync(SH, { recursive: true });
(async () => {
  const H = await start(process.argv[2] || 'drills.t766.html'); const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  const q0 = await H.open({ path: '?view=path', w: 390, h: 900 }); const ids = await q0.evaluate(() => pathStageIds(PATH_STAGES[0])); await q0.close();
  const rows = [];
  for (const id of ids) for (const kind of ['lesson', 'work']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + id, w: 900, h: 1200, dsf: 1 }); await sleep(1300);
    const info = await p.evaluate(() => { const pages = [...document.querySelectorAll('.bk-page')]; return { n: pages.length, words: pages.map(el => (el.innerText || '').split(/\s+/).filter(Boolean).length), heads: pages.map(el => { const h = el.querySelector('h1,h2,h3,[class*=title]'); return h ? h.innerText.slice(0, 50) : ''; }) }; });
    rows.push([id, kind, info.n, info.words.reduce((a, b) => a + b, 0), info.heads.join(' | ').slice(0, 300)]);
    if (kind === 'lesson' && (id === 'first-steps' || id === 'staff' || id === 'pulse')) { const pages = p.locator('.bk-page'); for (let i = 0; i < Math.min(info.n, 3); i++) await pages.nth(i).screenshot({ path: SH + id + '-' + i + '.png' }); }
    await p.close();
  }
  rows.forEach(r => console.log(r.join('\t')));
  await H.close();
})();
