const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r2/shots/orig/';
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?book=concept&ch=p-scales&lang=ko', w: 900, h: 1300 });
  const secs = await p.$$('section');
  for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: OUT + 'pko-' + (i + 1) + '.png' });
  // detect lines that start with a lone syllable-word fragment: dump line boxes of every text block
  const lines = await p.evaluate(() => {
    const out = [];
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const blocks = new Map();
    let n;
    while ((n = walker.nextNode())) {
      if (!n.nodeValue.trim()) continue;
      const el = n.parentElement; if (!el || el.closest('svg')) continue;
      let b = el; while (b && getComputedStyle(b).display === 'inline') b = b.parentElement;
      if (!blocks.has(b)) blocks.set(b, []);
      const r = document.createRange();
      for (let i = 0; i < n.nodeValue.length; i++) { r.setStart(n, i); r.setEnd(n, i + 1); const rc = r.getClientRects()[0]; if (rc) blocks.get(b).push([Math.round(rc.top), n.nodeValue[i]]); }
    }
    for (const [b, chars] of blocks) {
      const byTop = []; let cur = null;
      for (const [top, c] of chars) { if (!cur || Math.abs(top - cur.top) > 13) { cur = { top, s: '' }; byTop.push(cur); } cur.s += c; }
      if (byTop.length > 1) out.push(byTop.map(x => x.s).join(' ⏎ '));
    }
    return out;
  });
  require('fs').writeFileSync(OUT + 'print-lines.txt', lines.join('\n'));
  await p.context().close();
  for (const w of [390, 360]) {
    const s = await H.open({ path: '?teacher=1&tool=cb-p-scales&lang=ko', w, h: 860, lang: 'ko' });
    // open all steps
    const L = await s.evaluate(() => {
      const out = [];
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      const blocks = new Map(); let n;
      while ((n = walker.nextNode())) {
        if (!n.nodeValue.trim()) continue;
        const el = n.parentElement; if (!el || el.closest('svg')) continue;
        let b = el; while (b && getComputedStyle(b).display === 'inline') b = b.parentElement;
        if (!blocks.has(b)) blocks.set(b, []);
        const r = document.createRange();
        for (let i = 0; i < n.nodeValue.length; i++) { r.setStart(n, i); r.setEnd(n, i + 1); const rc = r.getClientRects()[0]; if (rc) blocks.get(b).push([Math.round(rc.top), n.nodeValue[i]]); }
      }
      for (const [b, chars] of blocks) { const byTop = []; let cur = null;
        for (const [top, c] of chars) { if (!cur || Math.abs(top - cur.top) > 13) { cur = { top, s: '' }; byTop.push(cur); } cur.s += c; }
        if (byTop.length > 1) out.push(byTop.map(x => x.s).join(' ⏎ ')); }
      return out;
    });
    require('fs').writeFileSync(OUT + 'screen-lines-' + w + '.txt', L.join('\n'));
    await s.context().close();
  }
  await H.close();
})();
