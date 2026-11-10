// Alignment check (her 7 Nov 13:11: 'check the alignment before you show me'). Run on a built lesson page; it measures what
// is drawn, in screen pixels, and lists every place where:
//  ledger  a ledger line is not centred on its head, or is longer than a head and a little
//  stem    a stem is not on its head's edge (up: the right edge, down: the left)
//  close   two notes (or a note and the next one's sharp) in one staff sit closer than a third of a head
//  clef    a staff line's start has no clef, a grand staff's lower staff has no bass clef, or a clef runs off the left
//  lean    the notes in a bar lean to one side: the space before them and after them differ by more than a fifth of the bar
// Usage: node align.js lesson.html   (prints each problem, then a count)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
  await p.goto('file://' + process.argv[2]); await p.waitForFunction(() => window.__paged, null, { timeout: 8000 }).catch(() => {}); await p.waitForTimeout(400);
  const r = await p.evaluate(() => {
    const out = [], R = (e) => e.getBoundingClientRect();
    const pages = [...document.querySelectorAll('.pg')];
    const where = (el) => { const pg = pages.findIndex(q => q.contains(el)) + 1; const m = el.closest('[data-snip]'); return 'p' + pg + ' ' + (m ? m.dataset.snip : '?'); };
    const svgs = [...document.querySelectorAll('svg')].filter(s => s.querySelector('g.staff'));
    for (const sv of svgs) {
      const tag = where(sv.querySelector('g.staff'));
      const heads = [...sv.querySelectorAll('g.notehead, ellipse.lhead')].filter(h => !h.closest('.lhead') || h.matches('ellipse.lhead')).map(h => ({ el: h, r: R(h.matches('g.notehead') && h.querySelector('ellipse.lhead') ? h.querySelector('ellipse.lhead') : (h.querySelector('use') || h)) })).filter(h => h.r.width > 1 && getComputedStyle(h.el).visibility !== 'hidden');
      const hw = heads.length ? heads.map(h => h.r.width).sort((a, c) => a - c)[Math.floor(heads.length / 2)] : 10;
      // ledger
      for (const L of sv.querySelectorAll('g.ledgerLines path, line.lledger')) { const l = R(L); if (l.width < 1) continue; const mid = (l.left + l.right) / 2;
        let best = null, bd = 1e9; for (const h of heads) { const d = Math.abs((h.r.left + h.r.right) / 2 - mid) + Math.abs((h.r.top + h.r.bottom) / 2 - (l.top + l.bottom) / 2) * 0.3; if (d < bd) { bd = d; best = h; } }
        if (!best) continue; const hc = (best.r.left + best.r.right) / 2, off = Math.abs(hc - mid);
        if (off > 0.8) out.push(`${tag} ledger off-centre by ${off.toFixed(1)}px`);
        if (l.width > best.r.width * 1.9) out.push(`${tag} ledger too long: ${l.width.toFixed(1)}px for a ${best.r.width.toFixed(1)}px head`); }
      // stems
      for (const n of sv.querySelectorAll('g.note, g.chord')) { if (n.matches('g.chord g.note')) continue; const st = n.querySelector(':scope > g.stem path'); if (!st) continue; const s = R(st); if (s.height < 2) continue;
        const hh = [...n.querySelectorAll('g.notehead')].map(h => R(h.querySelector('ellipse.lhead') || h.querySelector('use') || h)).filter(q => q.width > 1); if (!hh.length) continue;
        const up = s.top < Math.min(...hh.map(q => q.top)) - 1; const edge = up ? Math.max(...hh.map(q => q.right)) : Math.min(...hh.map(q => q.left)), sx = up ? s.right : s.left;
        if (Math.abs(sx - edge) > 1.2) out.push(`${tag} stem ${up ? 'up' : 'down'} ${Math.abs(sx - edge).toFixed(1)}px off its head (${n.id})`); }
      // close: per staff, heads (and accidentals) in x order
      for (const st of sv.querySelectorAll('g.staff')) { const items = [...st.querySelectorAll('g.note, g.rest, g.chord')].filter(n => !n.matches('g.chord g.note')).map(n => { const parts = [...n.querySelectorAll('g.notehead, g.accid, :scope.rest')].map(R).filter(q => q.width > 1); if (n.matches('g.rest')) parts.push(R(n)); if (!parts.length) return null; return { l: Math.min(...parts.map(q => q.left)), r: Math.max(...parts.map(q => q.right)), hr: Math.max(...[...n.querySelectorAll('g.notehead')].map(R).map(q => q.right), -1e9) }; }).filter(Boolean).sort((a, c) => a.l - c.l);
        for (let i = 1; i < items.length; i++) { const gap = items[i].l - (items[i - 1].hr > -1e8 ? items[i - 1].hr : items[i - 1].r); if (gap < hw / 3) out.push(`${tag} close: ${gap.toFixed(1)}px between two notes`); } }
      // clefs
      const svr = R(sv); const staves = [...sv.querySelectorAll('g.measure')][0]?.querySelectorAll(':scope > g.staff') || [];
      staves.forEach((st, i) => { if (st.querySelectorAll(':scope > path').length < 5) return; const c = st.querySelector('g.clef'); if (!c) { if (st.querySelector('path')) out.push(`${tag} clef missing on staff ${i + 1}`); return; } const cr = R(c); if (cr.left < svr.left - 0.5) out.push(`${tag} clef runs off the left`);
        const isF = /#E062/.test(c.innerHTML); if (staves.length === 2 && i === 1 && !isF) out.push(`${tag} lower staff has no bass clef`);
        if (isF) { const lines = [...st.querySelectorAll(':scope > path')].map(R).filter(q => q.height < 2); if (lines.length >= 5) { const top = Math.min(...lines.map(q => q.top)); if (Math.abs(cr.top - top) > hw * 0.6) out.push(`${tag} bass clef not on its staff (${(cr.top - top).toFixed(1)}px from the top line)`); } } });
      // touch: a finger, dynamic, chord name or word touching a stem, a beam, a head, a ledger, a sharp or a bar line
      const ink = (r) => { const t = r.height * 0.17; return { left: r.left, right: r.right, top: r.top + t, bottom: r.bottom - t, width: r.width, height: r.height - 2 * t }; };   // a text's box less its font's empty top and bottom
      const signs = [...sv.querySelectorAll('g.fing text, g.dynam, g.harm text, g.syl text')].map(e => ({ e, r: ink(R(e)) })).filter(q => q.r.width > 1);
      const solid = [...sv.querySelectorAll('g.stem path, g.beam polygon, g.notehead, g.accid, g.ledgerLines path, line.lledger, g.barLine path, g.dots, g.rest')].map(e => ({ e, r: R(e) })).filter(q => q.r.width > 0 || q.r.height > 0);
      const hit = (a, c) => a.left < c.right - 0.3 && c.left < a.right - 0.3 && a.top < c.bottom - 0.3 && c.top < a.bottom - 0.3;
      for (const g of signs) for (const q of solid) if (hit(g.r, q.r)) { out.push(`${tag} touch: '${g.e.textContent.trim()}' on a ${q.e.closest('g[class]').getAttribute('class').split(' ')[0]}`); break; }
      for (let i = 0; i < signs.length; i++) for (let j = i + 1; j < signs.length; j++) if (hit(signs[i].r, signs[j].r)) out.push(`${tag} touch: '${signs[i].e.textContent.trim()}' and '${signs[j].e.textContent.trim()}'`);
      // lean: per measure, staff 1
      for (const m of sv.querySelectorAll('g.measure')) { const st = m.querySelector(':scope > g.staff'); if (!st) continue; const bl = m.querySelector('g.barLine path'); if (!bl) continue;
        const lines = [...st.querySelectorAll(':scope > path')].map(R).filter(q => q.height < 2 && q.width > 20); if (!lines.length) continue;
        const x0b = Math.min(...lines.map(q => q.left)); const x1 = R(bl).left;
        const pre = [...st.querySelectorAll(':scope > g.clef, :scope > g.keySig, :scope > g.meterSig')].map(R).filter(q => q.width > 0);
        const x0 = pre.length ? Math.max(x0b, ...pre.map(q => q.right)) : x0b;
        const its = [...st.querySelectorAll('g.notehead, g.rest, g.accid')].map(R).filter(q => q.width > 1); if (!its.length) continue;
        const L = Math.min(...its.map(q => q.left)) - x0, Rg = x1 - Math.max(...its.map(q => q.right)), W = x1 - x0;
        if (W > 20 && Math.abs(L - Rg) > W * 0.2 && its.length > 1) out.push(`${tag} lean: ${L.toFixed(0)}px before, ${Rg.toFixed(0)}px after in a ${W.toFixed(0)}px bar`); }
    }
    out.push('#stats svgs=' + svgs.length + ' ledgers=' + document.querySelectorAll('g.ledgerLines path, line.lledger').length + ' stems=' + document.querySelectorAll('g.stem path').length + ' heads=' + document.querySelectorAll('g.notehead').length);
    return out;
  });
  r.forEach(x => console.log(x)); console.log(`${r.filter(x => !x.startsWith('#')).length} alignment problems`); await b.close();
})();
