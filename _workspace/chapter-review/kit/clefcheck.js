// every clef on a page: where the font's own G line (treble), F line (bass) or C line (alto) lands, against the staff's line, in staff spaces
const { start } = require('/home/claude/pbtest/kit/contentharness');
const FEAT = { '𝄞': [256, 'G', 1], '𝄢': [644.5, 'F', 3], '𝄡': [500, 'C', 2] };   // font units; which line counted from the bottom (0-based)
(async () => {
  const H = await start(process.env.BUILD || 'drills.t446.html');
  const p0 = await H.open({ path: '', w: 1024, h: 900 }); await p0.waitForTimeout(1000);
  const ids = await p0.evaluate(() => DRILLS.map(d => d.id)); const books = await p0.evaluate(() => Object.keys(LESSON_BOOKS)); await p0.context().close();
  const paths = ids.map(i => '?drill=' + i).concat(books.flatMap(b => ['lesson', 'work', 'teacher'].map(k => '?book=' + k + '&ch=' + b)));
  const all = [];
  for (const path of (process.env.ONLY ? process.env.ONLY.split(',') : paths)) {
    const p = await H.open({ path: path + '&lang=en', w: 1024, h: 900 }); await p.waitForTimeout(path.includes('book') ? 3800 : 3800);
    const r = await p.evaluate((FEAT) => {
      const out = [];
      document.querySelectorAll('svg text').forEach(tx => {
        const f = FEAT[tx.textContent.trim()]; if (!f) return;
        const svg = tx.ownerSVGElement; const m = tx.getScreenCTM(); if (!m) return;
        const pt = svg.createSVGPoint(); pt.x = 0; pt.y = -f[0] * (+tx.getAttribute('font-size') || 40) / 1000; const fy = pt.matrixTransform(m).y;
        const lines = [...svg.querySelectorAll('line')].map(l => { const a = svg.createSVGPoint(); a.x = +l.getAttribute('x1'); a.y = +l.getAttribute('y1'); const b = svg.createSVGPoint(); b.x = +l.getAttribute('x2'); b.y = +l.getAttribute('y2'); const lm = l.getScreenCTM(); const A = a.matrixTransform(lm), B = b.matrixTransform(lm); return { y: A.y, y2: B.y, w: Math.abs(B.x - A.x), x1: Math.min(A.x, B.x), x2: Math.max(A.x, B.x) }; })
          .filter(l => Math.abs(l.y - l.y2) < 0.5 && l.w > 40)
          .concat([...svg.querySelectorAll('rect')].filter(r => +r.getAttribute('height') <= 2 && +r.getAttribute('width') > 40).map(r => { const lm = r.getScreenCTM(); const a = svg.createSVGPoint(); a.x = +r.getAttribute('x'); a.y = +r.getAttribute('y') + (+r.getAttribute('height')) / 2; const b = svg.createSVGPoint(); b.x = a.x + (+r.getAttribute('width')); b.y = a.y; const A = a.matrixTransform(lm), B = b.matrixTransform(lm); return { y: A.y, y2: B.y, w: B.x - A.x, x1: A.x, x2: B.x }; }));
        const cb = tx.getBoundingClientRect(); const cx = cb.left + cb.width / 2;
        const ys = [...new Set(lines.filter(l => l.x1 <= cx + 2 && l.x2 >= cx - 2).map(l => Math.round(l.y * 10) / 10))].sort((a, b) => a - b);
        // staves: 5 equally spaced lines
        let best = null;
        for (let i = 0; i + 4 < ys.length; i++) { const g = ys.slice(i, i + 5), sp = (g[4] - g[0]) / 4; if (g.every((y, k) => Math.abs(y - (g[0] + k * sp)) < 0.6) && sp > 2) { const mid = (g[0] + g[4]) / 2; const dist = Math.abs(mid - (cb.top + cb.height / 2)); if (!best || dist < best.dist) best = { g, sp, dist }; } }
        if (!best) { out.push({ c: f[1], err: null }); return; }
        const lineY = best.g[4 - f[2]];
        out.push({ c: f[1], err: Math.round((fy - lineY) / best.sp * 100) / 100, sp: Math.round(best.sp * 10) / 10 });
      });
      return out;
    }, FEAT);
    if (r.length) { const bad = r.filter(x => x.err == null || Math.abs(x.err) > 0.12); all.push([path, r.length, bad.length, r.map(x => x.c + ':' + x.err).slice(0, 8).join(' ')]); }
    await p.context().close();
  }
  all.forEach(a => console.log(a.join(' | ')));
  await H.close();
})();
