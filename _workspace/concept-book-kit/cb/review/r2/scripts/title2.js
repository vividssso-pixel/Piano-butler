const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?book=concept&ch=p-scales&lang=ko', w: 900, h: 1300, dsf: 3 });
  await p.waitForTimeout(2000);
  const el = await p.evaluateHandle(() => [...document.querySelectorAll('[data-lb-page="9"] div')].find(e => e.textContent.trim() === '나의 다섯 가지 확인' && !e.children.length));
  const info = await el.evaluate(e => { const cs = getComputedStyle(e); return { td: cs.textDecorationLine, ff: cs.fontFamily, lh: cs.lineHeight, h: e.getBoundingClientRect().height }; });
  console.log(JSON.stringify(info));
  await el.screenshot({ path: '/home/claude/pbtest/cb/review/r2/shots/z-ko9-titleonly.png' });
  await p.context().close(); await H.close();
})();
