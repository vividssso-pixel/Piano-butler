// Contact sheet of the six moving warm-ups: the still (book) frame, then frames through one round
const { start } = require('./contentharness'); const fs = require('fs');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t376.html');
  const p = await H.open({ path: '?drill=posture-hands', w: 900, h: 900 });
  const rows = await p.evaluate(() => WARM_UPS.map(w => [w.id, [null, 0.08, 0.2, 0.32, 0.45, 0.58, 0.7, 0.86, 0.95].map(ph => penSvg(w.f(ph, w.who || 'girl'), { vb: w.vb, id: 'h' + w.id + String(ph).replace('.', '') }))]));
  const html = '<body style="margin:0;background:#fff;font-family:sans-serif">' + rows.map(([id, svgs]) => '<div style="display:flex;gap:4px;align-items:center;border-bottom:1px solid #ddd"><b style="width:60px;font-size:11px">' + id + '</b>' + svgs.map(s => '<div style="width:150px;height:120px;background:#faf6ec">' + s.replace('<svg ', '<svg width="100%" height="100%" ') + '</div>').join('') + '</div>').join('') + '</body>';
  const q = await p.context().newPage(); await q.setViewportSize({ width: 1440, height: 800 }); await q.setContent(html);
  await q.screenshot({ path: '../shots/warmsheet.png', fullPage: true });
  console.log('errs', p._errs.join('|'));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
