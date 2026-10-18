const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 390, h: 860, dsf: 1 }); await p.waitForTimeout(1500);
  const r = await p.evaluate(() => [...document.querySelectorAll('[data-cb-tool],[data-cb]')].map(e => (e.getAttribute('data-cb-tool') ? 'tool:' + e.getAttribute('data-cb-tool') : 'pad:' + e.getAttribute('data-cb')) + ' in step ' + (e.closest('[data-lb-screen]') ? e.closest('[data-lb-screen]').getAttribute('data-lb-screen') : '-') + ' buttons=' + [...e.querySelectorAll('button')].map(b => b.innerText.trim().slice(0, 10)).slice(0, 12).join('|')));
  console.log(r.join('\n'));
  await H.close();
})();
