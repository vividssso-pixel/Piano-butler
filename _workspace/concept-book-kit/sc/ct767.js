const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/bk/';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t767.html');
  for (const kind of ['lesson', 'work', 'spread', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=first-steps', w: 900, h: 1200 }); await sleep(1300);
    const info = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map(el => el.scrollHeight - el.clientHeight));
    console.log(kind, 'pages', info.length, 'overflow', info.filter(x => x > 2).length, p._errs.slice(0, 1));
    await p.close();
  }
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=first-steps', w: 390, h: 1600, lang }); await sleep(800);
    const n = await p.locator('.lb-challenge').count(), j = await p.locator('.lb-joke').count();
    // open all steps if folded
    const txt = await p.evaluate(() => document.body.innerText.includes('House race') || document.body.innerText.includes('집 경주'));
    await p.screenshot({ path: SH + 'screen-fs-' + lang + '.png', fullPage: false });
    const ans = p.locator('.lb-joke button'); if (await ans.count()) { await ans.click(); await sleep(200); }
    const jt = await p.locator('.lb-joke').first().innerText().catch(() => '');
    console.log(lang, 'challenges', n, 'jokes', j, 'house race text', txt, '| joke:', jt.replace(/\s+/g, ' '), p._errs.slice(0, 1));
    await p.close();
  }
  await H.close();
})();
