// English and Korean screen line breaks inside runs of note letters (B E A D / G C F).
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) for (const w of [320, 360, 390]) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w, h: 860, lang, dsf: 1 }); await p.waitForTimeout(1300);
    const r = await p.evaluate(() => { const out = []; const tw = document.createTreeWalker(document.querySelector('.pb-main'), NodeFilter.SHOW_TEXT); const ch = []; let n;
      while ((n = tw.nextNode())) { const el = n.parentElement; if (!el || el.closest('svg')) continue; const r = document.createRange();
        for (let i = 0; i < n.nodeValue.length; i++) { r.setStart(n, i); r.setEnd(n, i + 1); const rc = r.getClientRects()[0]; ch.push({ c: n.nodeValue[i], l: rc ? rc.left : null, t: rc ? rc.top : null }); } ch.push({ c: '\n', l: null }); }
      const vis = ch.map((x, i) => [x, i]).filter(([x]) => x.l !== null && x.c.trim() && x.c !== '⁠');
      for (let k = 0; k < vis.length - 1; k++) { const [a, ia] = vis[k], [b, ib] = vis[k + 1]; if (!(b.l < a.l - 2 && b.t > a.t + 4)) continue;
        if (ch.slice(ia, ib).some(x => x.c === '\n')) continue;
        const before = ch.slice(Math.max(0, ia - 6), ia + 1).map(x => x.c).join(''), after = ch.slice(ib, ib + 6).map(x => x.c).join('');
        if (/(^|[\s(:])[A-G][♯♭♮]?$/.test(before.replace(/⁠/g, '')) && /^[A-G][♯♭♮]?([\s,.)⁠]|$)/.test(after)) out.push(ch.slice(Math.max(0, ia - 16), ia + 1).map(x => x.c).join('') + ' / ' + ch.slice(ib, ib + 16).map(x => x.c).join('')); }
      return [...new Set(out)]; });
    console.log(lang, w, JSON.stringify(r));
    await p.context().close();
  }
  await H.close();
})();
