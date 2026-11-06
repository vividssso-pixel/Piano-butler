// Every clef on every page (drills, Lesson Books, Workbooks, teacher pages, cut-outs): is its ink cut off by its svg's edge?
// Independent of finding a staff. Prints the React component that owns the svg.
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t448.html');
  const p0 = await H.open({ path: '', w: 1024, h: 900 }); await p0.waitForTimeout(1000);
  const reg = await p0.evaluate(() => ({ d: DRILLS.map(d => d.id), l: Object.keys(LESSON_BOOKS), w: Object.keys(WORKBOOKS) })); await p0.context().close();
  let paths = reg.d.map(i => '?drill=' + i).concat(reg.l.map(b => '?book=lesson&ch=' + b), reg.w.map(b => '?book=work&ch=' + b), reg.w.map(b => '?book=teacher&ch=' + b), ['?book=cutouts&ch=all']);
  if (process.env.PART) { const [k, n] = process.env.PART.split('/').map(Number); paths = paths.filter((_, i) => i % n === k); }
  if (process.env.ONLY) paths = process.env.ONLY.split(',');
  const found = new Map(); let total = 0;
  for (const path of paths) {
    const p = await H.open({ path: path + '&lang=en', w: 1024, h: 900 }); await p.waitForTimeout(3500);
    const r = await p.evaluate(() => {
      const out = []; let n = 0;
      if (!window.__ink) window.__ink = {};
      const ink = (ch) => { if (window.__ink[ch]) return window.__ink[ch]; const cv = document.createElement('canvas'); cv.width = 160; cv.height = 160; const c2 = cv.getContext('2d'); c2.font = '40px ' + MUSIC_FONT; c2.fillText(ch, 40, 100);
        const px = c2.getImageData(0, 0, 160, 160).data; let minY = 999, maxY = -1, minX = 999; for (let yy = 0; yy < 160; yy++) for (let xx = 0; xx < 160; xx++) if (px[(yy * 160 + xx) * 4 + 3] > 60) { minY = Math.min(minY, yy); maxY = Math.max(maxY, yy); minX = Math.min(minX, xx); }
        return (window.__ink[ch] = { asc: 100 - minY, desc: maxY - 100, l: minX - 40 }); };
      const comp = (el) => { const k = Object.keys(el).find(k => k.startsWith('__reactFiber')); let f = k && el[k]; const names = []; while (f && names.length < 3) { if (typeof f.type === 'function') names.push(f.type.name); f = f.return; } return names.join('<'); };
      document.querySelectorAll('svg text').forEach(tx => {
        const ch = tx.textContent.trim(); if (!['𝄞', '𝄢', '𝄡'].includes(ch)) return;
        const svg = tx.ownerSVGElement; const tm = tx.getScreenCTM(); if (!tm) return; n++;
        if (getComputedStyle(svg).overflow === 'visible') return;
        const k = ink(ch); const cor = (x, y) => { const q = svg.createSVGPoint(); q.x = x; q.y = y; return q.matrixTransform(tm); };
        const sb = svg.getBoundingClientRect(); const vb = svg.viewBox.baseVal; const sc = vb && vb.height ? sb.height / vb.height : 1;
        const sides = { top: (sb.top - cor(0, -k.asc).y) / sc, bot: (cor(0, k.desc).y - sb.bottom) / sc, left: (sb.left - cor(k.l, 0).x) / sc };
        const side = Object.keys(sides).sort((a, b) => sides[b] - sides[a])[0];
        if (sides[side] > 0.3) out.push(comp(svg) + ' ' + ch + ' ' + side + ' ' + sides[side].toFixed(1) + ' vb ' + svg.getAttribute('viewBox'));
      });
      return { out, n };
    });
    total += r.n;
    r.out.forEach(k => { if (!found.has(k)) found.set(k, path); });
    await p.context().close();
  }
  [...found.entries()].sort((a, b) => a[0].localeCompare(b[0])).forEach(([k, v]) => console.log(v + ' | ' + k));
  console.log('clefs checked: ' + total + ', clipped kinds: ' + found.size);
  await H.close();
})();
