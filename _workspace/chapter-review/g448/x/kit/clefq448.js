// QA: every drill level, N questions mounted one by one (360px): is any clef's ink cut off by its svg's edge?
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t448.html');
  const p = await H.open({ path: '?lang=en', w: 1024, h: 900 }); await p.waitForTimeout(1500);
  const r = await p.evaluate(async (N) => {
    const out = new Map(), sleep = (ms) => new Promise(r => setTimeout(r, ms));
    const host = document.createElement('div'); host.style.cssText = 'position:absolute;left:0;top:0;width:360px;background:#fff'; document.body.appendChild(host);
    const INK = {};
    const ink = (ch) => { if (INK[ch]) return INK[ch]; const cv = document.createElement('canvas'); cv.width = 160; cv.height = 160; const c2 = cv.getContext('2d'); c2.font = '40px ' + MUSIC_FONT; c2.fillText(ch, 40, 100);
      const px = c2.getImageData(0, 0, 160, 160).data; let minY = 999, maxY = -1, minX = 999; for (let yy = 0; yy < 160; yy++) for (let xx = 0; xx < 160; xx++) if (px[(yy * 160 + xx) * 4 + 3] > 60) { minY = Math.min(minY, yy); maxY = Math.max(maxY, yy); minX = Math.min(minX, xx); }
      return (INK[ch] = { asc: 100 - minY, desc: maxY - 100, l: minX - 40 }); };
    const comp = (el) => { const k = Object.keys(el).find(k => k.startsWith('__reactFiber')); let f = k && el[k]; const names = []; while (f && names.length < 3) { if (typeof f.type === 'function') names.push(f.type.name); f = f.return; } return names.join('<'); };
    const analyse = (root, tag) => {
      root.querySelectorAll('svg text').forEach(tx => {
        const ch = tx.textContent.trim(); if (!['𝄞', '𝄢', '𝄡'].includes(ch)) return;
        const svg = tx.ownerSVGElement; const tm = tx.getScreenCTM(); if (!tm || getComputedStyle(svg).overflow === 'visible') return;
        const k = ink(ch); const cor = (x, y) => { const q = svg.createSVGPoint(); q.x = x; q.y = y; return q.matrixTransform(tm); };
        const sb = svg.getBoundingClientRect(); const sc = sb.height / (svg.viewBox.baseVal && svg.viewBox.baseVal.height || sb.height);
        const sides = { top: (sb.top - cor(0, -k.asc).y) / sc, bot: (cor(0, k.desc).y - sb.bottom) / sc, left: (sb.left - cor(k.l, 0).x) / sc };
        const side = Object.keys(sides).sort((a, b) => sides[b] - sides[a])[0];
        if (sides[side] > 0.3) { const key = comp(svg) + ' ' + ch + ' ' + side + ' ' + sides[side].toFixed(1) + ' vb ' + svg.getAttribute('viewBox'); out.set(key, (out.get(key) || tag)); }
      });
    };
    for (const D of DRILLS) {
      const C = D.concept || D; if (!C.levels || !C.Question) continue;
      for (const L of C.levels) {
        let prev = null;
        for (let k = 0; k < N; k++) {
          let q; try { q = C.generate(L, prev); prev = q; } catch (e) { break; }
          const div = document.createElement('div'); host.appendChild(div);
          const root = ReactDOM.createRoot(div);
          try { root.render(React.createElement(C.Question, { q, given: null, locked: false, onAnswer: () => {}, pixel: false, level: L })); } catch (e) {}
          await sleep(120);
          try { analyse(div, D.id + ' L' + L.n); } catch (e) {}
          root.unmount(); div.remove();
        }
      }
    }
    return [...out.entries()];
  }, +(process.env.N || 12));
  r.forEach(([k, v]) => console.log(v + ' | ' + k));
  console.log('clipped clef kinds: ' + r.length);
  await H.close();
})();
