const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t373.html');
  const p = await H.open({ path: '?book=spread&ch=posture-hands&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(1600);
  const info = await p.$$eval('section.bk-page', els => els.map(e => { const kind = e.dataset.spreadCover ? 'cover' : e.classList.contains('lb-page') ? 'L' + e.dataset.lbPage : 'W'; const b = e.querySelector('.bk-body'); return kind + ':' + (b ? b.scrollHeight - b.clientHeight : 0) + ':' + Math.round(e.getBoundingClientRect().height); }));
  console.log('spread pages', info.length, JSON.stringify(info), 'errs', p._errs.join('|').slice(0, 200), 'db', p._reqs.filter(u => /supabase/.test(u)).length);
  await p.pdf({ path: '../rv1/spread373.pdf', preferCSSPageSize: true, printBackground: true });
  await p.context().close();
  const q = await H.open({ path: '?view=toolbox&sec=books&lang=en', w: 900, h: 1200, store: { pb_mode_v1: 'teacher' } });
  await q.waitForTimeout(1200);
  const links = await q.$$eval('a[href*="book=spread"]', els => els.map(e => e.getAttribute('href') + ' | ' + e.innerText));
  console.log('shelf spread links', JSON.stringify(links));
  await q.context().close();
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
