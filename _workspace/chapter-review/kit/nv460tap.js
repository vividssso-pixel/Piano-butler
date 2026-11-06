const { start } = require('./contentharness');
const SPB = 60 / 66;
const tapIn = async (p, scope, btnText, beats) => p.evaluate(({ scope, btnText, beats, SPB }) => new Promise(res => {
  const root = scope ? document.querySelector(scope) : document;
  const btn = [...root.querySelectorAll('button')].find(b => b.textContent.trim().startsWith(btnText) && !b.disabled);
  if (!btn) return res('no button');
  btn.click();
  const ctx = window.__pbAudio, t0 = ctx.currentTime + 0.18, lat = outLatency(ctx);
  beats.forEach(b => setTimeout(() => window.dispatchEvent(new KeyboardEvent('keydown', { code: 'Space', key: ' ' })), Math.max(0, (t0 + b * SPB + lat - ctx.currentTime) * 1000)));
  res('ok');
}), { scope, btnText, beats, SPB });
(async () => {
  const H = await start(process.env.BUILD);
  // the lesson's pads
  const p = await H.open({ path: '?drill=note-values', w: 430, h: 900, lang: 'en' }); await p.waitForTimeout(1500);
  for (const [pg, beats, label] of [[5, [4, 5, 5.5, 6, 7, 7.5], 'pad5 right'], [5, [4, 5, 6, 7], 'pad5 quavers as one'], [6, [4, 5, 7], 'pad6 right'], [6, [4, 5, 6, 7], 'pad6 tap in the rest'], [3, [4, 6], 'pad3 right']]) {
    await p.evaluate((pg) => document.querySelector('[data-nv="pad' + pg + '"]').scrollIntoView(), pg);
    console.log(label, await tapIn(p, '[data-nv="pad' + pg + '"]', '▶ Tap it', beats));
    await p.waitForTimeout(8500);
    console.log('   ', await p.evaluate((pg) => [...document.querySelectorAll('[data-nv="pad' + pg + '"] div')].map(d => d.textContent).filter(t => /^Notes on time/.test(t)).join(' | '), pg));
  }
  console.log('errs', p._errs.join('|').slice(0, 300)); await p.context().close();
  // the drill: a fixed bar
  for (const [lv, row, beats, label] of [[4, [['q', 1], ['p', 1], ['h', 2]], [4, 5, 5.5, 6], 'L4 right'], [4, [['q', 1], ['p', 1], ['h', 2]], [4, 5, 5.5, 6, 7], 'L4 tapped the held beat'], [6, [['q', 1], ['q', 1], ['r', 1], ['q', 1]], [4, 5, 7], 'L6 right'], [6, [['q', 1], ['q', 1], ['r', 1], ['q', 1]], [4, 5, 6, 7], 'L6 tapped the rest']]) {
    const q = await H.open({ path: '?drill=note-values&tab=drill&level=' + (lv === 4 ? 5 : 4), w: 430, h: 900, lang: 'en' }); await q.waitForTimeout(1200);
    await q.evaluate(({ row, lv }) => { const g = NOTEVAL_DRILL.generate; NOTEVAL_DRILL.generate = (L, prev) => (L.kind === 'tap' || L.kind === 'tapr') ? { kind: L.kind, row, key: 'fix' + Math.random(), uid: Math.random() } : g(L, prev); }, { row, lv });
    await q.evaluate((lv) => [...document.querySelectorAll('button')].find(b => b.textContent.trim() === 'Level ' + lv).click(), lv); await q.waitForTimeout(800);
    console.log(label, await tapIn(q, '.card', '▶ Start', beats));
    await q.waitForTimeout(9000);
    console.log('   ', await q.evaluate(() => [...document.querySelectorAll('.card div')].map(d => d.textContent).filter(t => /^Notes on time|correct$/.test(t)).slice(0, 3).join(' | ')), q._errs.join('|').slice(0, 200));
    await q.context().close();
  }
  await H.close();
})();
