const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t369.html');
  for (const k of ['', 'girl', 'boy']) {
    const p = await H.open({ path: '?book=lesson&ch=posture-hands&lang=en' + (k ? '&kid=' + k : ''), w: 900, h: 1200 });
    await p.waitForTimeout(900);
    const r = await p.$$eval('[data-who]', els => { const o = { girl: 0, boy: 0 }; els.forEach(e => { if (getComputedStyle(e).display !== 'none') o[e.getAttribute('data-who')]++; }); return o; });
    console.log('kid=' + (k || 'turns'), JSON.stringify(r), 'errs', p._errs.length);
    if (k) await p.pdf({ path: '../rv1/lb369-' + k + '.pdf', preferCSSPageSize: true, printBackground: true });
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
