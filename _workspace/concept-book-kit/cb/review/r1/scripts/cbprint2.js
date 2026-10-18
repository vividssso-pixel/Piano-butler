// The printed concept book: page count, overflow, svg content spilling out of its viewBox, text clipped, and a PNG of
// every page (EN, KO). Also: an unknown ch, ch=all, and the print route for other chapters still working.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r1/shots/new';
(async () => {
  require('fs').mkdirSync(OUT, { recursive: true });
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=concept&ch=p-scales&lang=' + lang, w: 900, h: 1300 });
    await p.waitForTimeout(2500);
    const r = await p.evaluate(() => [...document.querySelectorAll('section.bk-page')].map((e, i) => {
      const b = e.querySelector('.bk-body'); const kids = [...b.children]; const last = kids[kids.length - 1].getBoundingClientRect();
      // elements whose box sticks out of the page body
      const bb = b.getBoundingClientRect(), outs = [];
      e.querySelectorAll('.bk-body *').forEach(el => { const q = el.getBoundingClientRect(); if (q.width && q.height && (q.right > bb.right + 1 || q.left < bb.left - 1)) outs.push(el.tagName + '.' + (el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className) + ' ' + Math.round(q.left - bb.left) + '..' + Math.round(q.right - bb.left)); });
      // svg text overlapping another svg text (labels on top of each other)
      const svgs = [...e.querySelectorAll('svg')]; let overlap = 0; const olist = [];
      svgs.forEach(s => { const ts = [...s.querySelectorAll('text')].map(t => ({ t: t.textContent, r: t.getBoundingClientRect() })).filter(x => x.r.width > 0);
        for (let a = 0; a < ts.length; a++) for (let c = a + 1; c < ts.length; c++) { const A = ts[a].r, C = ts[c].r; const ix = Math.min(A.right, C.right) - Math.max(A.left, C.left), iy = Math.min(A.bottom, C.bottom) - Math.max(A.top, C.top); if (ix > 1.5 && iy > 1.5) { overlap++; if (olist.length < 6) olist.push(ts[a].t + ' / ' + ts[c].t); } } });
      return { page: i + 1, over: b.scrollHeight - b.clientHeight, free: Math.round(bb.bottom - last.bottom), outs: outs.slice(0, 5), overlap, olist };
    }));
    console.log('== ' + lang + ' pages: ' + r.length + (p._errs.length ? ' ERR ' + p._errs.join(' | ') : ''));
    r.forEach(x => console.log('  p' + x.page + ' over=' + x.over + ' free=' + x.free + (x.outs.length ? ' OUT ' + JSON.stringify(x.outs) : '') + (x.overlap ? ' textOverlap=' + x.overlap + ' ' + JSON.stringify(x.olist) : '')));
    const secs = await p.$$('section.bk-page');
    for (let i = 0; i < secs.length; i++) await secs[i].screenshot({ path: OUT + '/cb-' + lang + '-' + (i + 1) + '.png' });
    // requests to a database (there should be none)
    const db = p._reqs.filter(u => /supabase|rest\/v1/.test(u)); if (db.length) console.log('  DB requests: ' + db.length);
    await p.context().close();
  }
  for (const path of ['?book=concept&ch=nope', '?book=concept&ch=all', '?book=concept', '?book=concept&ch=p-scales&pages=7', '?book=lesson&ch=scales', '?book=work&ch=scales']) {
    const p = await H.open({ path, w: 900, h: 1300 }); await p.waitForTimeout(1500);
    const n = await p.$$eval('section.bk-page', a => a.length), txt = (await p.evaluate(() => document.body.innerText)).slice(0, 120).replace(/\s+/g, ' ');
    const vis = await p.$$eval('section.bk-page', a => a.filter(s => getComputedStyle(s).display !== 'none').length);
    console.log(path + ' -> sections=' + n + ' visible=' + vis + ' errs=' + JSON.stringify(p._errs) + ' text="' + txt + '"');
    await p.context().close();
  }
  await H.close();
})();
