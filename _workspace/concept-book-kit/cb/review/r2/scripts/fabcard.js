const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/';
(async () => {
  const H = await start('drills.t485.html');
  for (const w of [390, 900]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, dsf: 1 }); await p.waitForTimeout(1300);
    await p.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight)); await p.waitForTimeout(400);
    const r = await p.evaluate(() => { const m = document.querySelector('.pb-main'); const fab = [...document.querySelectorAll('button')].find(b => getComputedStyle(b).position === 'fixed' && b.getBoundingClientRect().bottom > innerHeight - 120);
      const fr = fab && fab.getBoundingClientRect(); let under = [];
      if (fr) document.querySelectorAll('.pb-main button, .pb-main a, .pb-main p, .pb-main div').forEach(e => { if (e.children.length) return; const b = e.getBoundingClientRect(); if (b.width && b.bottom > fr.top && b.top < fr.bottom && b.right > fr.left && b.left < fr.right) under.push((e.innerText || e.tagName).trim().slice(0, 20)); });
      return { pad: getComputedStyle(m).paddingBottom, fab: fr && [Math.round(fr.left), Math.round(fr.top), Math.round(fr.width)], under: under.slice(0, 5) }; });
    console.log('fab', w, JSON.stringify(r));
    await p.context().close();
    const q = await H.open({ path: '?teacher=1&view=toolbox', w, h: 860, dsf: 1 }); await q.waitForTimeout(1500);
    const card = await q.evaluate(() => { const a = [...document.querySelectorAll('a')].find(x => /concept=|book=concept/.test(x.getAttribute('href') || '')); if (!a) return null; const c = a.parentElement; return { btns: [...c.querySelectorAll('a,button')].map(b => b.innerText.trim() + ' ' + Math.round(b.getBoundingClientRect().width) + 'x' + Math.round(b.getBoundingClientRect().height)), href: a.getAttribute('href'), left: Math.round(c.getBoundingClientRect().left) }; });
    console.log('card', w, JSON.stringify(card));
    await q.context().close();
  }
  await H.close();
})();
