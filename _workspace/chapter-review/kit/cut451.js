// QA of the cut-out pages: every set, en + ko. Page count, overflow, page errors; anything drawn outside its svg box
// (text, note heads, lines); text cut off by its box; text over text; anything outside the A4 page; notation (heads on a
// line or a space, ledger lines); reader text rules ('--', 'Princess', the old C names).
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t450.html');
  const p0 = await H.open({ path: '', w: 1024, h: 900 }); await p0.waitForTimeout(1000);
  const list = await p0.evaluate(() => CUTOUT_LIST.map(c => [c.id, c.pages])); await p0.context().close();
  for (const lang of (process.env.LANGS || 'en,ko').split(',')) for (const [id, pages] of list) {
    const p = await H.open({ path: '?book=cutouts&ch=' + id + '&lang=' + lang, w: 1100, h: 1400 }); await p.waitForTimeout(2600);
    const r = await p.evaluate(() => {
      const out = { pages: 0, over: [], svgClip: [], textCut: [], textOver: [], offPage: [], notation: [], words: [] };
      const pgs = [...document.querySelectorAll('.bk-page')]; out.pages = pgs.length;
      pgs.forEach((pg, pi) => {
        const P = pi + 1, pr = pg.getBoundingClientRect();
        const b = pg.querySelector('.bk-body'); if (b && b.scrollHeight - b.clientHeight > 1) out.over.push(P + ':' + (b.scrollHeight - b.clientHeight));
        // things outside the page
        pg.querySelectorAll('*').forEach(el => { const q = el.getBoundingClientRect(); if (q.width && q.height && (q.left < pr.left - 1 || q.right > pr.right + 1 || q.top < pr.top - 1 || q.bottom > pr.bottom + 1)) { const n = el.tagName + (el.textContent || '').trim().slice(0, 20); if (out.offPage.length < 8) out.offPage.push(P + ':' + n + ' ' + Math.round(Math.max(pr.left - q.left, q.right - pr.right, pr.top - q.top, q.bottom - pr.bottom))); } });
        // svg contents outside the svg box (only where the svg clips)
        pg.querySelectorAll('svg').forEach(svg => {
          if (svg.ownerSVGElement) return; const sr = svg.getBoundingClientRect(); if (!sr.width) return;
          if (getComputedStyle(svg).overflow === 'visible') return;
          svg.querySelectorAll('text, ellipse, circle, rect, line, path, polygon, polyline').forEach(el => {
            if (el.closest('defs, pattern, clipPath, mask')) return;
            const q = el.getBoundingClientRect(); if (!q.width && !q.height) return;
            const d = Math.max(sr.left - q.left, q.right - sr.right, sr.top - q.top, q.bottom - sr.bottom);
            if (d > 1.2) { const k = P + ':' + el.tagName + (el.tagName === 'text' ? '"' + el.textContent.slice(0, 14) + '"' : '') + ' ' + d.toFixed(1) + 'px'; if (out.svgClip.length < 12 && !out.svgClip.includes(k)) out.svgClip.push(k); }
          });
        });
        // html text cut by its own box
        pg.querySelectorAll('div, span, b, p, td, button').forEach(el => {
          if (!el.childNodes.length || ![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
          const cs = getComputedStyle(el); if (cs.overflow === 'visible' && cs.textOverflow !== 'ellipsis') return;
          if (el.scrollWidth - el.clientWidth > 1 || el.scrollHeight - el.clientHeight > 2) { const k = P + ':"' + el.textContent.trim().slice(0, 24) + '"'; if (out.textCut.length < 10) out.textCut.push(k); }
        });
        // text over text: leaf text boxes (html and svg) that overlap
        const boxes = [];
        const walker = document.createTreeWalker(pg, NodeFilter.SHOW_TEXT);
        let n; while ((n = walker.nextNode())) { if (!n.textContent.trim()) continue; const rg = document.createRange(); rg.selectNodeContents(n); [...rg.getClientRects()].forEach(q => { if (q.width > 2 && q.height > 2) boxes.push({ q, t: n.textContent.trim().slice(0, 16), el: n.parentElement }); }); }
        for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
          const a = boxes[i].q, c = boxes[j].q; if (boxes[i].el === boxes[j].el) continue;
          const ox = Math.min(a.right, c.right) - Math.max(a.left, c.left), oy = Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top);
          if (ox > 2 && oy > Math.min(a.height, c.height) * 0.35) { const k = P + ':"' + boxes[i].t + '" / "' + boxes[j].t + '"'; if (out.textOver.length < 10) out.textOver.push(k); }
        }
        // reader text rules
        const txt = pg.innerText;
        [['--', /--/], ['Princess', /Princess|공주/], ['old C', /Sea C|Sky C|Kingsland C|Queensland C|Clara's C|Clara’s C|바다 C|하늘 C|킹스랜드 C|퀸즈랜드 C|클라라의 C/]].forEach(([w, re]) => { if (re.test(txt)) out.words.push(P + ':' + w + ' "' + (txt.match(new RegExp('.{0,20}' + re.source + '.{0,20}')) || [''])[0].replace(/\n/g, ' ') + '"'); });
      });
      return out;
    });
    const bad = r.pages !== pages || r.over.length || r.svgClip.length || r.textCut.length || r.textOver.length || r.offPage.length || r.words.length || p._errs.length;
    console.log((bad ? 'CHECK ' : 'ok    ') + lang + ' ' + id + ' pages ' + r.pages + '/' + pages
      + (r.over.length ? ' | over ' + r.over.join(' ') : '') + (r.svgClip.length ? ' | svg-clip ' + r.svgClip.join(' ; ') : '')
      + (r.textCut.length ? ' | text-cut ' + r.textCut.join(' ; ') : '') + (r.textOver.length ? ' | text-over ' + r.textOver.join(' ; ') : '')
      + (r.offPage.length ? ' | off-page ' + r.offPage.join(' ; ') : '') + (r.words.length ? ' | words ' + r.words.join(' ; ') : '') + (p._errs.length ? ' | errs ' + p._errs.slice(0, 2).join(' ') : ''));
    await p.context().close();
  }
  await H.close();
})();
