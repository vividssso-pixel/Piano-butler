// The staff-and-keyboard map: under the grand staff of C3..C5, draw a keyboard whose white keys sit exactly under the notes,
// dashed guides from the staff down to each key, letter names on the keys, middle C in coral.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const S = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch(); const p = await b.newPage();
  await p.setContent('<body style="margin:0">' + S.map + '</body>');
  S.map = await p.evaluate(() => {
    const NS = 'http://www.w3.org/2000/svg', o = document.querySelector('svg'), inner = o.querySelector('svg.definition-scale');
    const g0 = inner.querySelector('g.page-margin');
    const heads = [...inner.querySelectorAll('g.note')].map(n => { const h = n.querySelector('g.notehead').getBBox(); return { n, cx: h.x + h.width / 2, w: h.width }; });
    const xs = [...new Set(heads.map(h => Math.round(h.cx)))].sort((a, b) => a - b);   // 15 columns
    const W = (xs[xs.length - 1] - xs[0]) / (xs.length - 1);
    heads.filter(h => Math.round(h.cx) === xs[7]).forEach(h => h.n.querySelectorAll('use, path').forEach(e => { e.setAttribute('fill', '#e4572e'); e.setAttribute('stroke', '#e4572e'); }));
    let low = 0; inner.querySelectorAll('g.staff path, g.note, g.ledgerLines').forEach(e => { const bb = e.getBBox(); low = Math.max(low, bb.y + bb.height); });
    const top = low + 260, KH = W * 3.4, BW = W * 0.6, BH = KH * 0.6, x0 = xs[0] - W / 2, names = 'CDEFGAB';
    let s = '';
    xs.forEach((x, i) => s += `<line x1="${x}" x2="${x}" y1="${low + 60}" y2="${top - 20}" stroke="#9a9cc4" stroke-width="10" stroke-dasharray="40 40"/>`);
    xs.forEach((x, i) => s += `<rect x="${x - W / 2}" y="${top}" width="${W}" height="${KH}" fill="${i === 7 ? '#fde6dd' : '#fff'}" stroke="#26296b" stroke-width="18"/>`);
    xs.forEach((x, i) => { if (i < xs.length - 1 && 'CDFGA'.includes(names[i % 7])) s += `<rect x="${x + W / 2 - BW / 2}" y="${top}" width="${BW}" height="${BH}" rx="12" fill="#26296b"/>`; });
    xs.forEach((x, i) => s += `<text x="${x}" y="${top + KH - 70}" text-anchor="middle" font-size="230" font-weight="700" fill="${i === 7 ? '#e4572e' : '#26296b'}" class="kbl">${names[i % 7]}</text>`);
    s += `<rect x="${x0}" y="${top}" width="${W * xs.length}" height="${KH}" fill="none" stroke="#26296b" stroke-width="30"/>`;
    s += `<text x="${xs[7]}" y="${top + KH + 300}" text-anchor="middle" font-size="230" font-weight="700" fill="#e4572e" class="kbl">middle C</text>`;
    const g = document.createElementNS(NS, 'g'); g.innerHTML = s; g0.appendChild(g);
    const bb = g.getBBox(); const iv = inner.getAttribute('viewBox').split(' ').map(Number), ov = o.getAttribute('viewBox').split(' ').map(Number);
    const need = bb.y + bb.height + 250 - iv[3];   // page-margin translate is tiny vs this; add room
    if (need > 0) { iv[3] += need + 120; ov[3] += (need + 120) * ov[2] / iv[2]; inner.setAttribute('viewBox', iv.join(' ')); o.setAttribute('viewBox', ov.map(v => +v.toFixed(2)).join(' ')); }
    return o.outerHTML;
  });
  fs.writeFileSync(process.argv[3], JSON.stringify(S)); await b.close(); console.log('map ok');
})();
