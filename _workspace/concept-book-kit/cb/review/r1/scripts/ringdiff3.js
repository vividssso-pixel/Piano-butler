// Interactive ring comparison t484 vs t485: tap every key of every ring on the scales/key-signatures lessons, and play
// through ten level-10 drill questions (lesson and game mode), capturing every ring after every action.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SEED = `(() => { let s = 777; Math.random = () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; }; })();`;
const rings = (p) => p.$$eval('svg[viewBox="0 0 360 360"]', a => a.map(s => s.outerHTML.replace(/<\/?tspan[^>]*>/g, '').replace(/ (font-size|font-weight|style|role|aria-hidden|aria-label)="[^"]*"/g, '')));
async function openSeeded(H, path, w = 390, h = 900, store) {
  const p = await H.open({ path, w, h, store });
  await p.addInitScript(SEED); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(900);
  return p;
}
async function lessonTaps(H, path, store) {
  const p = await openSeeded(H, path, 390, 900, store), snaps = [];
  // open every collapsed step header so extra steps (My twelve keys) mount
  for (let pass = 0; pass < 3; pass++) {
    const heads = await p.$$('[aria-expanded="false"]');
    for (const hd of heads) { try { await hd.click({ timeout: 800 }); await p.waitForTimeout(150); } catch (e) {} }
  }
  snaps.push(await rings(p));
  const n = (await rings(p)).length;
  for (let r = 0; r < n; r++) {
    for (let k = 0; k < 12; k++) {
      const g = await p.$$('svg[viewBox="0 0 360 360"]');
      if (!g[r]) break;
      const keys = await g[r].$$('g[data-key]');
      if (!keys[k]) break;
      try { await keys[k].click({ timeout: 1000 }); } catch (e) { continue; }
      await p.waitForTimeout(80);
      snaps.push(await rings(p));
    }
  }
  const errs = p._errs.slice(); await p.context().close(); return { snaps, errs };
}
async function drillRun(H, path, game, store) {
  const p = await openSeeded(H, path, 390, 900, store), snaps = [];
  if (game) { const s = await p.$('button:has-text("PRESS START"), button:has-text("Start")'); if (s) { await s.click(); await p.waitForTimeout(500); } }
  for (let q = 0; q < 10; q++) {
    snaps.push(await rings(p));
    const btn = await p.$(game ? '.pixel-choice' : '.choice-btn');
    if (!btn) break;
    await btn.click(); await p.waitForTimeout(game ? 300 : 600);
    snaps.push(await rings(p));
    const nx = await p.$('button:has-text("Next")'); if (nx) { await nx.click(); await p.waitForTimeout(400); } else await p.waitForTimeout(1200);
  }
  const errs = p._errs.slice(); await p.context().close(); return { snaps, errs };
}
const cmp = (a, b) => { if (a.snaps.length !== b.snaps.length) return 'snap count ' + a.snaps.length + ' vs ' + b.snaps.length; for (let i = 0; i < a.snaps.length; i++) if (JSON.stringify(a.snaps[i]) !== JSON.stringify(b.snaps[i])) return 'snap ' + i + ' differs'; return null; };
(async () => {
  const A = await start('drills.t484.html'), B = await start('drills.t485.html');
  const keysStore = { pb_my_keys_v1: JSON.stringify(['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']) };
  const jobs = [
    ['scales learn taps', (H) => lessonTaps(H, '?drill=scales&tab=learn')],
    ['key-sigs learn taps', (H) => lessonTaps(H, '?drill=key-signatures&tab=learn')],
    ['scales lv10 lesson', (H) => drillRun(H, '?drill=scales&tab=drill&level=10', false)],
    ['scales lv10 lesson, 12 keys', (H) => drillRun(H, '?drill=scales&tab=drill&level=10', false, keysStore)],
    ['scales lv10 game', (H) => drillRun(H, '?drill=scales&tab=drill&level=10&mode=game', true)],
    ['keysig lv10 lesson', (H) => drillRun(H, '?drill=key-signatures&tab=drill&level=10', false)],
  ];
  for (const [name, fn] of jobs) {
    const a = await fn(A), b = await fn(B), d = cmp(a, b);
    const ringCount = a.snaps.reduce((s, x) => s + x.length, 0);
    console.log((d ? 'DIFF ' : 'SAME ') + name + '  snapshots=' + a.snaps.length + ' rings captured=' + ringCount + (d ? '  (' + d + ')' : '') + (a.errs.length || b.errs.length ? '  errs484=' + JSON.stringify(a.errs) + ' errs485=' + JSON.stringify(b.errs) : ''));
  }
  await A.close(); await B.close();
})();
