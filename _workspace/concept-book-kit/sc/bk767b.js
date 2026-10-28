const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/bk/';
(async () => {
  const H = await start(process.env.B || 'drills.t766.html'); const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  const [kind, ch, pages] = [process.argv[2], process.argv[3], (process.argv[4] || '0').split(',').map(Number)];
  const p = await H.open({ path: '?book=' + kind + '&ch=' + ch, w: 900, h: 1200, dsf: 1 }); await sleep(1500);
  const pg = p.locator('.bk-page'); const n = await pg.count();
  for (const i of pages) if (i < n) await pg.nth(i).screenshot({ path: SH + kind + '-' + ch + '-' + i + '.png' });
  console.log('pages', n);
  await H.close();
})();
