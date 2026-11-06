const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const ch of ['posture-hands', 'first-steps', 'note-names', 'staff']) {
    const p = await H.open({ path: '?book=spread&ch=' + ch + '&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(2600);
    const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map(e => e.hasAttribute('data-spread-blank') ? 'blank' : ((e.querySelector('.lb-head span, .wb-head span') || {}).textContent || '').replace('Piano Butler · ', '').slice(0, 12) + ':' + ((e.textContent.match(/On paper|My five checks|Lesson step \d|Check-up/) || [''])[0])));
    console.log(ch, r.length, r.join(' | '), p._errs.length ? 'ERR ' + p._errs[0] : '');
    await p.context().close();
  }
  await H.close();
})();
