const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  for (const build of ['drills.t484.html', 'drills.t485.html']) {
  const H = await start(build);
  const p = await H.open({ path: '?book=lesson&ch=scales&lang=ko', w: 900, h: 1300, dsf: 3 });
  await p.waitForTimeout(2000);
  const el = await p.evaluateHandle(() => [...document.querySelectorAll('[data-lb-page="7"] div')].find(e => e.textContent.trim() === '나의 다섯 가지 확인' && !e.children.length).parentElement);
  await el.screenshot({ path: '/home/claude/pbtest/cb/review/r2/shots/z-ch16-ko7-title-' + build.slice(8, 12) + '.png' });
  await p.context().close(); await H.close(); }
})();
