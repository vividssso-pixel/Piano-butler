// every page of the Lesson Books and Workbooks (chapters 1-5) and the Workbook's front matter, for a fresh-eyes review
const { start } = require('./contentharness');
const OUT = '/home/claude/pbtest/p425/review/';
(async () => {
  const H = await start(process.env.BUILD || 'drills.t425.html');
  const jobs = [['work', 'front']];
  for (const ch of ['posture-hands', 'first-steps', 'note-names', 'staff', 'whole-staff']) jobs.push(['lesson', ch], ['work', ch]);
  for (const [kind, ch] of jobs) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=en', w: 900, h: 1200 }); await p.waitForTimeout(2600);
    const pages = await p.$$('.bk-page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: OUT + kind + '-' + ch + '-' + String(i + 1).padStart(2, '0') + '.png' });
    console.log(kind, ch, pages.length);
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
