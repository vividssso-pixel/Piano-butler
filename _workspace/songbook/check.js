// Every sign inside its row: lyrics, fingers, chords and counts clear of noteheads and of each other; answer boxes clear of notes.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(require('fs').existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {}); const p = await b.newPage();
  await p.goto('file://' + process.argv[2]); await p.waitForTimeout(400);
  const r = await p.evaluate(() => {
    const bad = [], R = (e) => e.getBoundingClientRect(), hit = (a, c, m = 0.5) => a.left < c.right - m && c.left < a.right - m && a.top < c.bottom - m && c.top < a.bottom - m;
    document.querySelectorAll('.mus').forEach((mu, i) => {
      const key = mu.dataset.snip || i;
      const heads = [...mu.querySelectorAll('g.notehead use')].map(R);
      const stems = [...mu.querySelectorAll('g.stem path')].map(R);
      // the ink of each label, not its font box: canvas gives the glyphs' own ascent and descent; then 1.5px of air all round
      const cx = document.createElement('canvas').getContext('2d');
      const ink = (t) => { const r = R(t), cs = getComputedStyle(t); cx.font = cs.fontWeight + ' 100px ' + cs.fontFamily; const m = cx.measureText(t.textContent.trim());
        const fa = m.fontBoundingBoxAscent, fd = m.fontBoundingBoxDescent, k = r.height / (fa + fd), a = 1.5;
        return { left: r.left - a, right: r.right + a, top: r.top + (fa - m.actualBoundingBoxAscent) * k - a, bottom: r.top + (fa + m.actualBoundingBoxDescent) * k + a }; };
      const texts = [...mu.querySelectorAll('text')].filter(t => t.textContent.trim()).map(t => ({ t: t.textContent.trim(), r: ink(t) }));
      const boxes = [...mu.querySelectorAll('rect.wbox')].map(R);
      texts.forEach(a => { heads.forEach(h => { if (hit(a.r, h)) bad.push([key, 'text/head', a.t, (h.bottom - a.r.top).toFixed(1) + 'px of ' + a.r.height.toFixed(1)]); }); stems.forEach(h => { if (hit(a.r, h, 0.2)) bad.push([key, 'text/stem', a.t]); }); });
      for (let x = 0; x < texts.length; x++) for (let y = x + 1; y < texts.length; y++) if (hit(texts[x].r, texts[y].r, 1)) bad.push([key, 'text/text', texts[x].t + ' ' + texts[y].t, (Math.min(texts[x].r.bottom, texts[y].r.bottom) - Math.max(texts[x].r.top, texts[y].r.top)).toFixed(1) + 'px of ' + texts[x].r.height.toFixed(1)]);
      boxes.forEach(bx => heads.forEach(h => { if (hit(bx, h)) bad.push([key, 'box/head']); }));
    });
    return { n: document.querySelectorAll('.mus').length, bad };
  });
  console.log(r.n, 'snippets;', r.bad.length, 'clashes'); r.bad.slice(0, 30).forEach(x => console.log(' ', x.join(' | ')));
  await b.close();
})();
