// Layout check for everything that is not the music (her 7 Nov 14:04: '곡 뿐만아니라 나머지들도 아직 안맞아'): boxes, text,
// keyboards, ticks, pictures. On every page it lists where:
//  out      something runs past the page's margins or past the box it sits in
//  clip     text is cut off inside its box
//  overlap  two blocks side by side or one above the other overlap
//  tight    a box's content touches its border (less than 5px of padding)
//  touch    two blocks one under the other have no gap (less than 3px)
//  centre   a narrower line of music is not centred
//  widow    a paragraph ends with one short word alone on its last line
//  row      the items of one row do not start at the same height
//  cut      a drawn shape (clef, note, stem, key) is cut by the edge of its picture or of a box that hides overflow (her 27 Nov 17:33)
// Usage: node layout.js lesson.html
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 900, height: 1200 } });
  await p.goto('file://' + process.argv[2]); await p.waitForFunction(() => window.__paged, null, { timeout: 8000 }).catch(() => {}); await p.waitForTimeout(500);
  const r = await p.evaluate(() => {
    const out = [], R = (e) => e.getBoundingClientRect(), cs = (e) => getComputedStyle(e);
    const name = (e) => (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : e.tagName.toLowerCase()) + (e.dataset && e.dataset.snip ? '[' + e.dataset.snip + ']' : '');
    const text = (e) => (e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    const shown = (e) => { const s = cs(e); return s.display !== 'none' && s.visibility !== 'hidden' && !e.closest('[hidden]') && R(e).width > 0 && R(e).height > 0; };
    [...document.querySelectorAll('.pg')].forEach((pg, pi) => {
      const P = 'p' + (pi + 1), pr = R(pg), ps = cs(pg), L = pr.left + parseFloat(ps.paddingLeft) - 1.5, Rt = pr.right - parseFloat(ps.paddingRight) + 1.5;
      const els = [...pg.querySelectorAll('*')].filter(e => !(e instanceof SVGElement) || e.tagName === 'svg').filter(e => !e.closest('.foot, .top, .rule, .shd') && !e.classList.contains('n2'))   /* .n2: a Music Box 2 note cell, an svg that fills its box on purpose so the staff lines run through; lesson.py checks the notes inside it itself (NOTE OUT OF BOX) */.filter(shown);   // .shd: a faint note-shape shadow behind a letter (her 18 Nov 19:02), drawn on purpose past its box
      for (const e of els) {
        const er = R(e);
        if (er.left < L || er.right > Rt) out.push(`${P} out: ${name(e)} '${text(e)}' runs ${er.left < L ? 'left ' + (L - er.left).toFixed(1) : 'right ' + (er.right - Rt).toFixed(1)}px past the margin`);
        const par = e.parentElement; if (par && par !== pg && !(e instanceof SVGElement && e.tagName !== 'svg')) { const q = R(par), s = cs(par);
          if (s.overflow !== 'visible' || s.borderTopWidth !== '0px') { if (er.right > q.right + 1 || er.left < q.left - 1 || er.bottom > q.bottom + 1) out.push(`${P} out: ${name(e)} '${text(e)}' sticks out of ${name(par)}`); } }
        const s = cs(e);
        if ((s.overflow === 'hidden' || s.overflowY === 'hidden') && (e.scrollHeight > e.clientHeight + 2 || e.scrollWidth > e.clientWidth + 2) && !e.classList.contains('body') && !e.classList.contains('pg')) out.push(`${P} clip: ${name(e)} '${text(e)}' cut off`);
        // a bordered box: its content at least 5px in from the border
        if (parseFloat(s.borderTopWidth) > 0.5 && parseFloat(s.borderLeftWidth) > 0.5 && e.children.length && !(e instanceof SVGElement)) {
          const kids = [...e.children].filter(shown).filter(k => !k.classList.contains('shd')); if (kids.length) { const top = Math.min(...kids.map(k => R(k).top)), bot = Math.max(...kids.map(k => R(k).bottom)), lf = Math.min(...kids.map(k => R(k).left)), rt = Math.max(...kids.map(k => R(k).right));
            const d = Math.min(top - er.top, er.bottom - bot, lf - er.left, er.right - rt); if (d < 5) out.push(`${P} tight: ${name(e)} '${text(e)}' content ${d.toFixed(1)}px from its border`); } }
        // siblings: overlap, and no gap one under the other
        const kids = e instanceof SVGElement ? [] : [...e.children].filter(shown).filter(k => cs(k).position !== 'absolute' && !cs(k).display.startsWith('inline') || ['inline-block', 'inline-flex'].includes(cs(k).display));   // inline words wrap across lines: their boxes are not blocks
        for (let i = 0; i < kids.length; i++) for (let j = i + 1; j < kids.length; j++) { const a = R(kids[i]), c = R(kids[j]);
          const ox = Math.min(a.right, c.right) - Math.max(a.left, c.left), oy = Math.min(a.bottom, c.bottom) - Math.max(a.top, c.top);
          if (ox > 1 && oy > 1) out.push(`${P} overlap: ${name(kids[i])} '${text(kids[i])}' and ${name(kids[j])} '${text(kids[j])}' by ${Math.min(ox, oy).toFixed(1)}px`); }
        if (!['flex', 'grid', 'inline-flex'].includes(s.display) || s.flexDirection === 'column') for (let i = 1; i < kids.length; i++) { const a = R(kids[i - 1]), c = R(kids[i]);
          const g = c.top - a.bottom, horiz = Math.min(a.right, c.right) - Math.max(a.left, c.left);
          if (horiz > 10 && g >= -0.5 && g < 3 && cs(kids[i - 1]).display === 'block' && cs(kids[i]).display === 'block' && !kids[i].classList.contains('sp') && !kids[i - 1].classList.contains('sp')
              && (parseFloat(cs(kids[i]).borderTopWidth) > 0 || parseFloat(cs(kids[i - 1]).borderBottomWidth) > 0 || kids[i].classList.contains('mus') || kids[i - 1].classList.contains('mus')))
            out.push(`${P} touch: ${name(kids[i - 1])} and ${name(kids[i])} only ${g.toFixed(1)}px apart`); }
        // a row (flex or grid, row direction): its items start level, unless the row centres them on purpose
        if (['flex', 'grid'].includes(s.display) && s.flexDirection !== 'column' && kids.length > 1 && !['center', 'end', 'flex-end', 'baseline'].includes(s.alignItems)) {
          const rows = {}; kids.forEach(k => { const t = Math.round(R(k).top / 6); (rows[t] = rows[t] || []).push(k); });
          const tops = kids.map(k => R(k).top), lines = []; tops.forEach(t => { if (!lines.some(l => Math.abs(l - t) < 20)) lines.push(t); });
          lines.forEach(l => { const inRow = kids.filter(k => Math.abs(R(k).top - l) < 20); const ts = inRow.map(k => R(k).top); if (inRow.length > 1 && Math.max(...ts) - Math.min(...ts) > 1.5) out.push(`${P} row: ${name(e)} '${text(e)}' items start ${(Math.max(...ts) - Math.min(...ts)).toFixed(1)}px apart`); }); }
      }
      // narrower music lines centred
      for (const m of pg.querySelectorAll('.mus')) { if (!shown(m)) continue; const mr = R(m), q = R(m.parentElement); if (mr.width < q.width - 4 && !(['flex', 'grid'].includes(cs(m.parentElement).display) && cs(m.parentElement).flexDirection !== 'column' && m.parentElement.querySelectorAll(':scope > .mus').length > 1)) {   // lines side by side in a row are not centred one by one
        const dl = mr.left - q.left, dr = q.right - mr.right; if (Math.abs(dl - dr) > 2 && !m.parentElement.matches('.lpm, .trk, .lpat, .bas, .pos, .kbs, .nbk, .toolm')) out.push(`${P} centre: ${name(m)} ${dl.toFixed(0)}px left, ${dr.toFixed(0)}px right`); } }
      // a short last word alone on its line
      for (const e of pg.querySelectorAll('p, .how, .lead, .cap2, .tog span, .lst span, .wow, .act')) { if (!shown(e) || e.children.length > 6 || e.closest('.bgt')) continue;   // a music table with the class 'lead' is not a paragraph
        const rg = document.createRange(); rg.selectNodeContents(e); const lines = {}; for (const rc of rg.getClientRects()) { if (rc.width < 1) continue; const k = Math.round(rc.top); lines[k] = Math.max(lines[k] || 0, rc.right) - 0; }
        const rects = [...rg.getClientRects()].filter(q => q.width > 0.5); if (rects.length < 2) continue;
        const ys = [...new Set(rects.map(q => Math.round(q.top / 4)))]; if (ys.length < 2) continue;
        const last = rects.filter(q => Math.round(q.top / 4) === Math.max(...ys)), w = Math.max(...last.map(q => q.right)) - Math.min(...last.map(q => q.left));
        if (w < Math.min(40, R(e).width * 0.1)) out.push(`${P} widow: '${text(e)}…' ends with ${w.toFixed(0)}px alone on its last line`); }
    });
    document.querySelectorAll('.pg').forEach((pg, pi) => { const P = 'p' + (pi + 1), seen = {};
      for (const e of pg.querySelectorAll('svg path, svg ellipse, svg circle, svg line, svg rect, svg text, svg polygon, svg polyline')) {
        if (!shown(e) || e.closest('defs, clipPath') || e.closest('[clip-path]')) continue; const er = R(e); if (er.width < 0.5 && er.height < 0.5) continue;
        for (let a = e.parentElement; a && a !== pg.parentElement; a = a.parentElement) { const st = cs(a); const svgRoot = a.tagName.toLowerCase() === 'svg';
          const tbl = a.classList && a.classList.contains('bgt');   // a clef may reach outside its own picture, never outside its table
          if (!(st.overflowX !== 'visible' || st.overflowY !== 'visible' || a === pg || tbl)) continue; if (a.classList && a.classList.contains('body')) continue;
          const q = R(a), d = Math.max(q.left - er.left, er.right - q.right, q.top - er.top, er.bottom - q.bottom);
          if (d > 1.2) { const side = d === q.left - er.left ? 'left' : d === er.right - q.right ? 'right' : d === q.top - er.top ? 'top' : 'bottom';
            const host = a.closest('.exb, .g2, .bgt, .mb-hands, .lt, figure') || a, k = name(host) + side + (svgRoot ? 's' : 'b');
            if (!seen[k]) { seen[k] = 1; out.push(`${P} cut: a ${e.tagName} in ${name(host)} '${text(host)}' is cut ${d.toFixed(1)}px at the ${side} by ${name(a)}`); } break; } } } });
    document.querySelectorAll('.pg').forEach((pg, pi) => { const P = 'p' + (pi + 1);   // text in a table cell must stay inside its cell (words, counts, letters)
      for (const td of pg.querySelectorAll('.bgt td')) { if (!shown(td) || !td.textContent.trim()) continue; const q = R(td);
        if (td.matches('.cnm')) { const nb = [td.previousElementSibling, td.nextElementSibling]; if (nb.every(x => !x || !x.textContent.trim())) continue; }   // a chord name may reach into an empty neighbour in its borderless row
        for (const t of [...td.querySelectorAll('*')].concat([td])) { for (const n of t.childNodes) { if (n.nodeType !== 3 || !n.textContent.trim()) continue;
          const rg = document.createRange(); rg.selectNodeContents(n); const r = rg.getBoundingClientRect(); const h = t.closest('.hbx>span'), hq = h ? R(h) : q;   // in a split box, each half's text stays in its half
          if (r.left < Math.max(q.left, hq.left) - 1.5 || r.right > Math.min(q.right, hq.right) + 1.5) out.push(`${P} spill: '${n.textContent.trim()}' runs out of its box by ${Math.max(q.left - r.left, r.right - q.right).toFixed(1)}px`); } } } });
    return [...new Set(out)];
  });
  r.forEach(x => console.log(x)); console.log(`${r.length} layout problems`); await b.close();
})();
