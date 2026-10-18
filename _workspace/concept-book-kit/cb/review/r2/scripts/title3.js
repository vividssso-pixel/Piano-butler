const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?book=concept&ch=p-scales&lang=ko', w: 900, h: 1300, dsf: 3 });
  await p.waitForTimeout(2000);
  const el = await p.evaluateHandle(() => [...document.querySelectorAll('[data-lb-page="9"] div')].find(e => e.textContent.trim() === '나의 다섯 가지 확인' && !e.children.length).parentElement);
  const info = await el.evaluate(e => [...e.querySelectorAll('*')].map(c => { const b = c.getBoundingClientRect(); return c.tagName + ' ' + Math.round(b.top) + '-' + Math.round(b.bottom) + ' x' + Math.round(b.left) + '-' + Math.round(b.right) + ' ' + (c.getAttribute('style') || '').slice(0, 60); }));
  console.log(info.join('\n'));
  // what's painted at the line? elementsFromPoint
  const b = await el.boundingBox();
  const hits = await p.evaluate(([x, y]) => document.elementsFromPoint(x, y).slice(0, 6).map(e => e.tagName + '.' + e.className + ' ' + (e.getAttribute('style') || '').slice(0, 80)), [b.x + 160, b.y + 52]);
  console.log('box', JSON.stringify(b), '\n', hits.join('\n'));
  await el.screenshot({ path: '/home/claude/pbtest/cb/review/r2/shots/z-ko9-titlegrp.png' });
  await p.context().close(); await H.close();
})();
