const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const path of ['?book=concept&ch=p-scales&lang=ko', '?book=lesson&ch=scales&lang=ko']) {
    const p = await H.open({ path, w: 900, h: 1300 });
    await p.waitForTimeout(2000);
    const r = await p.evaluate(() => { const pg = document.querySelectorAll('[data-lb-page]'); const out = [];
      pg.forEach(g => { const h = [...g.querySelectorAll('*')].find(e => /^(단계별로 연습하기|어느 음에서나 장음계|나의 다섯 가지 확인|장음계|조표)$/.test(e.textContent.trim()) && e.children.length === 0);
        if (!h) return; const b = h.getBoundingClientRect(), par = h.parentElement; out.push({ page: g.getAttribute('data-lb-page'), tag: h.tagName, txt: h.textContent, cls: h.className, style: h.getAttribute('style'), b: [b.top, b.bottom, b.left, b.right].map(Math.round), parent: par.outerHTML.slice(0, 900) }); }); return out; });
    console.log(path, JSON.stringify(r, null, 1).slice(0, 4000));
    await p.context().close();
  }
  await H.close();
})();
