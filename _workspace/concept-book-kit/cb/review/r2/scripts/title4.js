const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?book=concept&ch=p-scales&lang=ko', w: 900, h: 1300, dsf: 3 });
  await p.waitForTimeout(2000);
  const el = await p.evaluateHandle(() => [...document.querySelectorAll('[data-lb-page="9"] div')].find(e => e.textContent.trim() === '나의 다섯 가지 확인' && !e.children.length).parentElement);
  await el.evaluate(e => e.scrollIntoView({ block: 'center' }));
  const b = await el.boundingBox();
  const hits = await p.evaluate(([x, y]) => document.elementsFromPoint(x, y).slice(0, 8).map(e => e.tagName + '.' + (e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className) + ' ' + (e.getAttribute('style') || '').slice(0, 100)), [b.x + 280, b.y + 50.5]);
  console.log(hits.join('\n'));
  await el.evaluate(e => { e.children[2].style.visibility = 'hidden'; });
  await el.screenshot({ path: '/home/claude/pbtest/cb/review/r2/shots/z-ko9-norule.png' });
  await el.evaluate(e => { e.children[2].style.visibility = ''; e.children[1].style.visibility = 'hidden'; });
  await el.screenshot({ path: '/home/claude/pbtest/cb/review/r2/shots/z-ko9-notitle.png' });
  await p.context().close(); await H.close();
})();
