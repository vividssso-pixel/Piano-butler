// Block and label positions on every Handbook page, as fractions of the page (for "Read and listen" cues).
// Usage: node regions.js out.json file1.html [file2.html ...]
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = {};
  for (const f of process.argv.slice(3)) {
    const p = await b.newPage({ viewport: { width: 820, height: 1160 } });
    await p.goto('file://' + f); await p.waitForTimeout(1800);
    const r = await p.evaluate(() => {
      const res = {};
      document.querySelectorAll('section.pg').forEach(s => {
        const ft = s.querySelector('.foot span'); if (!ft) return; const n = +ft.textContent; const S = s.getBoundingClientRect();
        const box = e => { const R = e.getBoundingClientRect(); return [(R.left - S.left) / S.width, (R.top - S.top) / S.height, R.width / S.width, R.height / S.height].map(v => +v.toFixed(4)); };
        const blocks = []; let ex = 0;
        const body = s.querySelector('.body'); if (!body) return;
        const kids = [];
        [...body.children].forEach(c => { if (c.classList.contains('leadrow')) { kids.push(c.querySelector('.lead') || c); const sc = c.querySelector('.secret1'); if (sc) kids.push(sc); } else kids.push(c); });
        kids.forEach(c => {
          const cls = (c.className && c.className.baseVal === undefined ? c.className : '').split(' ')[0] || c.tagName.toLowerCase();
          let key = cls;
          if (cls === 'secret1') key = (c.querySelector('.sl') || {}).textContent?.toLowerCase().includes('rule') ? 'rule' : 'secret';
          if (cls === 'inact2' || cls === 'inact') { const bh = (c.querySelector('.bh') || {}).textContent || ''; const m = bh.match(/(\d+)/); key = 'ex' + (m ? m[1] : ++ex); }
          if (/^h[1-4]$/.test(cls)) key = 'h:' + c.textContent.trim();
          const labs = [...c.querySelectorAll('svg text')].map(t => [t.textContent.trim(), box(t)]).filter(x => x[0] && x[0].length <= 12);
          const rs = c.querySelector('.ires'); blocks.push(rs ? { key, cls, box: box(c), labs, res: box(rs) } : { key, cls, box: box(c), labs });
        });
        res[n] = blocks;
      });
      return res;
    });
    Object.assign(out, r); await p.close();
  }
  fs.writeFileSync(process.argv[2], JSON.stringify(out)); console.log(Object.keys(out).length, 'pages'); await b.close();
})();
