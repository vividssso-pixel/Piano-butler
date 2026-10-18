// Screen checks for the concept book: sideways scroll, the table's own scroll box, tap targets under 44,
// smallest text (HTML and SVG), elements wider than their box, colours off the palette.
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const routes = (process.env.ROUTES || '?teacher=1&tool=cb-p-scales,?tool=cb-p-scales&lock=1').split(',');
  const widths = (process.env.W || '320,360,390,1024').split(',').map(Number);
  for (const r of routes) for (const lang of ['en', 'ko']) for (const w of widths) {
    const p = await H.open({ path: r, w, h: 860, lang, dsf: 1 }); await p.waitForTimeout(1200);
    const res = await p.evaluate(() => {
      const root = document.querySelector('[data-cb="key-pad"]') ? document.querySelector('[data-cb="key-pad"]').closest('section, .pb-main') || document.body : document.body;
      const hs = document.documentElement.scrollWidth - document.documentElement.clientWidth;
      // the table's scroll box
      const tb = document.querySelector('[data-cb-row="C"]'); let table = null;
      if (tb) { const box = tb.closest('[role=table]').parentElement; const rows = [...document.querySelectorAll('[data-cb-row]')];
        const lastCell = rows[1].children[rows[1].children.length - 1].getBoundingClientRect(), bb = box.getBoundingClientRect();
        table = { boxW: Math.round(bb.width), scrollW: box.scrollWidth, clientW: box.clientWidth, hidden: box.scrollWidth - box.clientWidth, lastColRight: Math.round(lastCell.right - bb.right) }; }
      // tap targets
      const small = [...document.querySelectorAll('.pb-main button, .pb-main a, .pb-main [role=button], .pb-main g[data-key]')].filter(b => { const r = b.getBoundingClientRect(); const cs = getComputedStyle(b); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && (r.height < 44 || r.width < 44) && !b.closest('[data-cb-tool="build-major"] svg'); })
        .map(b => (b.tagName === 'g' ? 'key:' + b.getAttribute('data-key') : (b.innerText || b.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 22)) + ' ' + Math.round(b.getBoundingClientRect().width) + 'x' + Math.round(b.getBoundingClientRect().height));
      // smallest text
      const sizes = [];
      const tw = document.createTreeWalker(document.querySelector('.pb-main'), NodeFilter.SHOW_TEXT); let n;
      while ((n = tw.nextNode())) { if (!n.nodeValue.trim()) continue; const el = n.parentElement; const rr = el.getBoundingClientRect(); if (!rr.width) continue;
        let px;
        if (el.closest('svg')) { const svg = el.closest('svg'); const vb = svg.viewBox && svg.viewBox.baseVal; const fs = parseFloat(getComputedStyle(el).fontSize); const scale = vb && vb.width ? svg.getBoundingClientRect().width / vb.width : 1; px = fs * scale; }
        else px = parseFloat(getComputedStyle(el).fontSize);
        sizes.push([px, n.nodeValue.trim().slice(0, 18), el.closest('svg') ? 'svg' : 'html', el.closest('[data-cb],[data-cb-tool],[data-lb-screen]') ? (el.closest('[data-cb],[data-cb-tool],[data-lb-screen]').getAttribute('data-cb') || el.closest('[data-cb],[data-cb-tool],[data-lb-screen]').getAttribute('data-cb-tool') || 'step' + el.closest('[data-lb-screen]').getAttribute('data-lb-screen')) : 'head']); }
      sizes.sort((a, b) => a[0] - b[0]);
      const under11 = sizes.filter(s => s[0] < 11);
      // things sticking out of their try-box or page step
      const over = [];
      document.querySelectorAll('.try-box, [data-lb-screen]').forEach(bx => { const br = bx.getBoundingClientRect(); bx.querySelectorAll('button, a, svg, span, div').forEach(c => { const b = c.getBoundingClientRect(); if (b.width && (b.right - br.right > 1.5 || br.left - b.left > 1.5) && !c.closest('[style*="overflow"]')) over.push((c.innerText || c.tagName).trim().slice(0, 16) + ':' + Math.round(b.right - br.right)); }); });
      return { hs, table, nSmall: small.length, small: [...new Set(small)].slice(0, 30), under11: under11.length, smallest: under11.slice(0, 12).map(s => s[0].toFixed(1) + '"' + s[1] + '"' + s[2] + '/' + s[3]), over: [...new Set(over)].slice(0, 10) };
    });
    console.log('\n==', lang, w, r, 'errs', p._errs.join('|').slice(0, 200), '\n', JSON.stringify(res));
    await p.context().close();
  }
  await H.close();
})();
