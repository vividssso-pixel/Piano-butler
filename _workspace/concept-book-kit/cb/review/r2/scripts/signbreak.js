// Does a sharp/flat/natural ever part from the letter before it or the syllable after it (a line break between them)?
const { start } = require('/home/claude/pbtest/kit/contentharness');
const probe = () => {
  const out = []; const tw = document.createTreeWalker(document.querySelector('.pb-main') || document.body, NodeFilter.SHOW_TEXT);
  const chars = []; let n;
  while ((n = tw.nextNode())) { const el = n.parentElement; if (!el || el.closest('svg')) continue; const r = document.createRange();
    for (let i = 0; i < n.nodeValue.length; i++) { r.setStart(n, i); r.setEnd(n, i + 1); const rc = r.getClientRects()[0]; if (rc && rc.width) chars.push({ c: n.nodeValue[i], l: rc.left, r: rc.right, t: rc.top, b: rc.bottom, blk: (() => { let b = el; while (b && getComputedStyle(b).display.startsWith('inline')) b = b.parentElement; return b; })() }); } }
  for (let i = 1; i < chars.length - 1; i++) { const c = chars[i]; if (!/[♯♭♮𝄪]/.test(c.c)) continue;
    const p = chars[i - 1], q = chars[i + 1];
    if (p.blk === c.blk && /[A-G]/.test(p.c) && c.l < p.l - 2) out.push('letter|sign: ' + chars.slice(Math.max(0, i - 8), i + 4).map(x => x.c).join(''));
    if (q.blk === c.blk && /[가-힣A-Za-z]/.test(q.c) && q.l < c.l - 2) out.push('sign|next: ' + chars.slice(Math.max(0, i - 6), i + 6).map(x => x.c).join('')); }
  return [...new Set(out)];
};
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await p.waitForTimeout(2200);
    console.log('print', lang, JSON.stringify(await p.evaluate(probe)));
    await p.context().close();
    for (const w of [320, 360, 390]) {
      const s = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, lang, dsf: 1 }); await s.waitForTimeout(1300);
      console.log('screen', lang, w, JSON.stringify(await s.evaluate(probe)));
      await s.context().close();
    }
  }
  await H.close();
})();
