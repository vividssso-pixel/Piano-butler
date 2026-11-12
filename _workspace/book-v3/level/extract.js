// Pull every block of the Handbook and Workbook pages as HTML, keyed like regions.js, for the Level books.
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = { hb: {}, wb: {}, css: {} };
  const H = '/mnt/user-data/outputs/house-rooms/';
  for (const [kind, f] of [['hb','handbook-before'],['hb','handbook-pitch'],['hb','handbook-time2'],['hb','handbook-expression'],['hb','handbook-play'],['wb','workbook-before'],['wb','workbook-pitch'],['wb','workbook-time2'],['wb','workbook-expression'],['wb','workbook-play']]) {
    const p = await b.newPage({ viewport: { width: 820, height: 1160 } });
    await p.goto('file://' + H + f + '.html'); await p.waitForTimeout(1800);
    const r = await p.evaluate((kind) => {
      const res = {}; let wbn = 0;
      document.querySelectorAll('section.pg').forEach(s => {
        const ft = s.querySelector('.foot span'); if (!ft) return; const n = +ft.textContent;
        const body = s.querySelector('.body'); if (!body) return;
        const kids = []; [...body.children].forEach(c => { if (c.classList.contains('leadrow')) { kids.push(c.querySelector('.lead') || c); const sc = c.querySelector('.secret1'); if (sc) kids.push(sc); } else kids.push(c); });
        let ex = 0; const blocks = [];
        kids.forEach(c => {
          const cls = (typeof c.className === 'string' ? c.className : '').split(' ')[0] || c.tagName.toLowerCase();
          let key = cls;
          if (cls === 'secret1') key = (c.querySelector('.sl') || {}).textContent?.toLowerCase().includes('rule') ? 'rule' : 'secret';
          if (cls === 'inact2' || cls === 'inact') { const bh = (c.querySelector('.bh') || {}).textContent || ''; const m = bh.match(/(\d+)/); key = 'ex' + (m ? m[1] : ++ex); }
          if (/^h[1-4]$/.test(cls)) key = 'h:' + c.textContent.trim();
          blocks.push({ key, html: c.outerHTML, title: (c.querySelector('h2,h3,.it,.tt,b') || {}).textContent || '' });
        });
        res[kind === 'wb' ? (s.querySelector('.top span:last-child') || {}).textContent + '|' + n : n] = blocks;
      });
      return res;
    }, kind);
    Object.assign(out[kind], kind === 'wb' ? Object.fromEntries(Object.entries(r).map(([k, v]) => [f + '|' + k, v])) : r);
    out.css[f] = await p.evaluate(() => [...document.querySelectorAll('style')].map(s => s.textContent).join('\n'));
    await p.close();
  }
  fs.writeFileSync('/tmp/claude-0/lvl/blocks.json', JSON.stringify(out)); console.log(Object.keys(out.hb).length, Object.keys(out.wb).length); await b.close();
})();
