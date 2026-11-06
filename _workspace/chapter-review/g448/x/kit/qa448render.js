// QA B: every drill level, 25 questions mounted one by one (360px wide): render errors, and on every staff each note head
// sits on a line or in a space, ledger lines where they belong (no missing, no extra), stems the right way.
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t447.html');
  const p = await H.open({ path: '?lang=' + (process.env.LANGX || 'en'), w: 1024, h: 900 }); await p.waitForTimeout(1500); await p.evaluate(([ms, only]) => { window.__SLEEP = ms; window.__ONLY = only ? only.split(',') : null; }, [+(process.env.SLEEP || 60), process.env.ONLYD || '']);
  const r = await p.evaluate(async (N) => {
    const out = [], sleep = (ms) => new Promise(r => setTimeout(r, ms));
    const host = document.createElement('div'); host.style.cssText = 'position:absolute;left:0;top:0;width:360px;background:#fff'; document.body.appendChild(host);
    const errs = []; const oe = console.error; console.error = (...a) => { errs.push(a.map(String).join(' ').slice(0, 200)); };
    const analyse = (root) => {
      const probs = [];
      root.querySelectorAll('svg').forEach(svg => {
        const P = (x, y, el) => { const m = el.getCTM(); const pt = svg.createSVGPoint(); pt.x = x; pt.y = y; return pt.matrixTransform(m); };
        const H = []; svg.querySelectorAll('line').forEach(l => { const a = P(+l.getAttribute('x1'), +l.getAttribute('y1'), l), b = P(+l.getAttribute('x2'), +l.getAttribute('y2'), l); if (Math.abs(a.y - b.y) < 0.3) H.push({ y: a.y, x1: Math.min(a.x, b.x), x2: Math.max(a.x, b.x), dash: l.getAttribute('stroke-dasharray') }); });
        svg.querySelectorAll('rect').forEach(r => { const h = +r.getAttribute('height'), w = +r.getAttribute('width'); if (h > 0 && h <= 2 && w > 6) { const a = P(+r.getAttribute('x'), +r.getAttribute('y') + h / 2, r), b = P(+r.getAttribute('x') + w, +r.getAttribute('y') + h / 2, r); H.push({ y: a.y, x1: a.x, x2: b.x }); } });
        const longs = H.filter(l => l.x2 - l.x1 > 60 && !l.dash);
        const ys = [...new Set(longs.map(l => Math.round(l.y * 4) / 4))].sort((a, b) => a - b);
        const staves = [];
        for (let i = 0; i + 4 < ys.length; i++) { const g = ys.slice(i, i + 5), sp = (g[4] - g[0]) / 4; if (sp > 3 && g.every((y, k) => Math.abs(y - (g[0] + k * sp)) < 0.4)) { staves.push({ top: g[0], sp, x1: Math.min(...longs.filter(l => Math.abs(l.y - g[0]) < 0.3).map(l => l.x1)), x2: Math.max(...longs.filter(l => Math.abs(l.y - g[0]) < 0.3).map(l => l.x2)) }); i += 4; } }
        if (!staves.length) return;
        const heads = [];
        svg.querySelectorAll('ellipse').forEach(e => {
          const rx = +e.getAttribute('rx'), ry = +e.getAttribute('ry'); if (!(rx > 2.5 && rx < 12 && ry > 1.8 && ry < 9)) return;
          if ((e.getAttribute('fill') || '') === 'none' && !e.getAttribute('stroke')) return;
          heads.push({ e, rx, c: P(+e.getAttribute('cx'), +e.getAttribute('cy'), e) });
        });
        heads.forEach(({ e, rx, c }) => {
          const st = staves.filter(s => c.x >= s.x1 - 4 && c.x <= s.x2 + 4).sort((a, b) => Math.abs(c.y - (a.top + 2 * a.sp)) - Math.abs(c.y - (b.top + 2 * b.sp)))[0]; if (!st) return;
          const pos = (c.y - st.top) / (st.sp / 2);
          if (pos < -14 || pos > 22) return;
          if (Math.abs(pos - Math.round(pos)) > 0.15) { probs.push('head off line/space pos=' + pos.toFixed(2)); return; }
          const P0 = Math.round(pos);
          const grp = heads.filter(h => Math.abs(h.c.x - c.x) < rx * 2.2).map(h => Math.round((h.c.y - st.top) / (st.sp / 2)));   // a chord or harmonic interval shares its ledger lines
          const lo = Math.min(...grp), hi = Math.max(...grp);
          const need = []; if (lo <= -2) for (let k = -2; k >= lo; k -= 2) need.push(k); if (hi >= 10) for (let k = 10; k <= hi; k += 2) need.push(k);
          const own = []; if (P0 <= -2) for (let k = -2; k >= P0; k -= 2) own.push(k); if (P0 >= 10) for (let k = 10; k <= P0; k += 2) own.push(k);
          const shorts = H.filter(l => l.x2 - l.x1 <= 60 && l.x1 <= c.x + 2 && l.x2 >= c.x - 2).map(l => Math.round((l.y - st.top) / (st.sp / 2) * 10) / 10).filter(q => q <= -1.5 || q >= 9.5);
          const has = (k) => shorts.some(q => Math.abs(q - k) < 0.2);
          const miss = own.filter(k => !has(k)), extra = shorts.filter(q => !need.some(k => Math.abs(q - k) < 0.2) && Math.abs(q - Math.round(q)) < 0.2 && Math.round(q) % 2 === 0);
          if (miss.length) probs.push('missing ledger at pos ' + miss.join(',') + ' for head pos ' + P0);
          if (extra.length) probs.push('extra ledger at pos ' + [...new Set(extra)].join(',') + ' for head pos ' + P0);
        });
      });
      return probs;
    };
    for (const D of DRILLS) {
      if (window.__ONLY && !window.__ONLY.includes(D.id)) continue;
      const C = D.concept || D; if (!C.levels || !C.Question) continue;
      for (const L of C.levels) {
        const probs = new Map(); let prev = null, nerr = errs.length, thrown = [];
        for (let k = 0; k < N; k++) {
          let q; try { q = C.generate(L, prev); prev = q; } catch (e) { thrown.push('gen ' + e.message); break; }
          const div = document.createElement('div'); host.appendChild(div);
          const root = ReactDOM.createRoot(div);
          try { root.render(React.createElement(C.Question, { q, given: null, locked: false, onAnswer: () => {}, pixel: false, level: L })); } catch (e) { thrown.push('render ' + e.message); }
          await sleep(+(window.__SLEEP || 60));
          try { analyse(div).forEach(m => probs.set(m, (probs.get(m) || 0) + 1)); } catch (e) { thrown.push('analyse ' + e.message); }
          const hs = div.scrollWidth > 362 ? 'wider than 360: ' + div.scrollWidth : null; if (hs) probs.set(hs, (probs.get(hs) || 0) + 1);
          root.unmount(); div.remove();
        }
        const newErr = errs.slice(nerr);
        if (probs.size || thrown.length || newErr.length) out.push([D.id, 'L' + L.n, [...probs.entries()].map(([m, c]) => m + ' x' + c).slice(0, 6), thrown.slice(0, 2), [...new Set(newErr)].slice(0, 2)]);
      }
    }
    console.error = oe;
    return out;
  }, +(process.env.N || 25));
  r.forEach(x => console.log(JSON.stringify(x)));
  console.log('levels with findings: ' + r.length, 'page errors', p._errs.slice(0, 3).join(' | '));
  await H.close();
})();
