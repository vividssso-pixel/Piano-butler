// Precise overlap: shapes pad (or key pad) Listen, then press Play in the in-book order-of-sharps tool.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const PATCH = `(() => { window.__src = []; const P = AudioScheduledSourceNode.prototype, s0 = P.start, s1 = P.stop;
  P.start = function (w) { this.__r = { t0: (w || this.context.currentTime), t1: Infinity }; window.__src.push(this.__r); return s0.apply(this, arguments); };
  P.stop = function (w) { if (this.__r) this.__r.t1 = Math.min(this.__r.t1, w == null ? this.context.currentTime : w); return s1.apply(this, arguments); }; })();`;
(async () => {
  const H = await start('drills.t485.html');
  for (const first of ['shapes-pad', 'key-pad']) for (const tool of ['sharps-order', 'build-major']) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 390, h: 860, dsf: 1 }); await p.addInitScript(PATCH); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(1200);
    const pad = await p.$('[data-cb="' + first + '"]'); const lb = await pad.$('button:has-text("Listen")'); await lb.scrollIntoViewIfNeeded(); await lb.click(); await p.waitForTimeout(700);
    const tb = await p.$('[data-cb-tool="' + tool + '"]');
    const btns = await tb.$$('button'); const names = []; for (const b of btns) names.push((await b.innerText()).trim().slice(0, 14));
    let target = null; for (const b of btns) { const tx = (await b.innerText()).trim(); if (/Play|▶|Listen|T$|^T$/.test(tx)) { target = b; break; } }
    const m = await p.evaluate(() => ({ n: window.__src.length, now: getAudio().currentTime }));
    if (target) { await target.scrollIntoViewIfNeeded(); await target.click(); }
    await p.waitForTimeout(2500);
    const r = await p.evaluate((m) => { const a = window.__src.slice(0, m.n), b = window.__src.slice(m.n);
      const still = a.filter(x => x.t0 > m.now + 0.25 && x.t1 > x.t0 + 0.02);
      const lastOld = still.length ? Math.max(...still.map(x => x.t0)) - m.now : null;
      const firstNew = b.length ? Math.min(...b.map(x => x.t0)) - m.now : null;
      return { oldStill: still.length, oldLastStart: lastOld && lastOld.toFixed(2), newCount: b.length, newFirstStart: firstNew && firstNew.toFixed(2) }; }, m);
    console.log(first, '->', tool, 'button', target ? 'found' : 'none', JSON.stringify(names.slice(0, 8)), JSON.stringify(r));
    await p.context().close();
  }
  await H.close();
})();
