const { start } = require('./contentharness');
const fs = require('fs');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t369.html');
  const p = await H.open({ path: '?book=lesson&ch=posture-hands&lang=en&draft=1', w: 900, h: 1200 });
  await p.waitForTimeout(1200);
  const info = await p.$$eval('.lb-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return { over: b.scrollHeight - b.clientHeight, h: Math.round(e.getBoundingClientRect().height) }; }));
  console.log('pages', info.length, JSON.stringify(info), 'errs', p._errs.join('|').slice(0, 300), 'db', p._reqs.filter(u => /supabase/.test(u)).length);
  await p.pdf({ path: '../rv1/lb369.pdf', preferCSSPageSize: true, printBackground: true });
  await p.context().close();
  const q = await H.open({ path: '?book=lesson&ch=posture-hands&lang=en', w: 900, h: 1200 });
  await q.waitForTimeout(900);
  console.log('final: asks shown', await q.$$eval('[data-lb-ask]', e => e.length));
  await q.pdf({ path: '../rv1/lb369-final.pdf', preferCSSPageSize: true, printBackground: true });
  await q.context().close();
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
