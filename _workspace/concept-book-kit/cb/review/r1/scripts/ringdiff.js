// Compare every 360x360 ring SVG (KeyRing and FifthsRing) between the shipped build t484 and t485, per route.
// Math.random is seeded so the drills ask the same questions in both builds.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SEED = `(() => { let s = 12345; Math.random = () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; }; })();`;
const ROUTES = [
  { path: '?book=lesson&ch=scales', w: 900, h: 1300 },
  { path: '?book=lesson&ch=key-signatures', w: 900, h: 1300 },
  { path: '?book=work&ch=scales', w: 900, h: 1300 },
  { path: '?book=work&ch=key-signatures', w: 900, h: 1300 },
  { path: '?book=teacher&ch=scales', w: 900, h: 1300 },
  { path: '?drill=scales&tab=learn', w: 390, h: 900 },
  { path: '?drill=key-signatures&tab=learn', w: 390, h: 900 },
  { path: '?drill=scales&tab=drill&level=10', w: 390, h: 900, answer: true },
  { path: '?drill=scales&tab=drill&level=10&mode=game', w: 390, h: 900 },
  { path: '?drill=key-signatures&tab=drill&level=10', w: 390, h: 900, answer: true },
  { path: '?drill=scales&tab=learn', w: 390, h: 900, lang: 'ko' },
  { path: '?print=1&drill=scales&level=10&n=6', w: 900, h: 1300 },
];
async function grab(H, r) {
  const p = await H.open({ path: r.path, w: r.w, h: r.h, lang: r.lang });
  await p.addInitScript(SEED); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(900);
  if (r.lang === 'ko') { const b = await p.$('button.chip:has-text("한국어")'); if (b) { await b.click(); await p.waitForTimeout(500); } }
  // open every lesson step (Got it buttons fold; extra steps may need opening): click step headers that are closed
  const get = () => p.$$eval('svg[viewBox="0 0 360 360"]', a => a.map(s => s.outerHTML));
  const before = await get();
  let after = null;
  if (r.answer) { const b = await p.$('.choice-btn'); if (b) { await b.click(); await p.waitForTimeout(700); after = await get(); } }
  const errs = p._errs.slice();
  await p.context().close();
  return { before, after, errs };
}
(async () => {
  const A = await start('drills.t484.html'), B = await start('drills.t485.html');
  let bad = 0;
  for (const r of ROUTES) {
    const a = await grab(A, r), b = await grab(B, r);
    const n = a.before.length, same = a.before.length === b.before.length && a.before.every((x, i) => x === b.before[i]);
    const sameAfter = !r.answer || (JSON.stringify(a.after) === JSON.stringify(b.after));
    if (!same || !sameAfter) bad++;
    console.log((same && sameAfter ? 'SAME ' : 'DIFF ') + r.path + (r.lang ? ' [' + r.lang + ']' : '') + '  rings=' + n + '/' + b.before.length + (r.answer ? ' after-answer=' + (a.after ? a.after.length : '-') + (sameAfter ? ' same' : ' DIFF') : '') + (a.errs.length || b.errs.length ? '  errs484=' + JSON.stringify(a.errs) + ' errs485=' + JSON.stringify(b.errs) : ''));
    if (!same) { for (let i = 0; i < Math.max(a.before.length, b.before.length); i++) if (a.before[i] !== b.before[i]) { const x = a.before[i] || '', y = b.before[i] || ''; let k = 0; while (k < x.length && x[k] === y[k]) k++; console.log('   ring ' + i + ' first diff at ' + k + ':\n   484: ' + x.slice(Math.max(0, k - 80), k + 120) + '\n   485: ' + y.slice(Math.max(0, k - 80), k + 120)); break; } }
  }
  console.log(bad ? bad + ' route(s) differ' : 'all routes identical');
  await A.close(); await B.close();
})();
