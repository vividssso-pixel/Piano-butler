const { start } = require('/home/claude/pbtest/kit/contentharness');
const PATCH = `(() => { window.__src = []; const P = AudioScheduledSourceNode.prototype, s0 = P.start, s1 = P.stop;
  P.start = function (w) { this.__r = { t0: w || 0, t1: Infinity, f: this.frequency ? this.frequency.value : 0 }; window.__src.push(this.__r); return s0.apply(this, arguments); };
  P.stop = function (w) { if (this.__r) this.__r.t1 = Math.min(this.__r.t1, w == null ? this.context.currentTime : w); return s1.apply(this, arguments); }; })();`;
(async () => {
  const H = await start('drills.t485.html');
  for (const which of [0, 1]) for (const wait of [700, 2500]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, dsf: 1 }); await p.addInitScript(PATCH); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(1200);
    const sp = (await p.$$('[data-cb="shapes-pad"]'))[which]; const b = await sp.$('button:has-text("Listen")'); await b.scrollIntoViewIfNeeded(); await b.click(); await p.waitForTimeout(wait);
    const now = await p.evaluate(() => getAudio().currentTime);
    await p.evaluate(() => window.scrollTo(0, 0)); const back = await p.$('button:has-text("← Toolbox")'); await back.click(); await p.waitForTimeout(600);
    const r = await p.evaluate((now) => ({ total: window.__src.length, still: window.__src.filter(x => x.t0 > now + 0.15 && x.t1 > x.t0 + 0.02).map(x => [(x.t0 - now).toFixed(2), x.t1 === Infinity ? 'inf' : (x.t1 - now).toFixed(2), Math.round(x.f)]) , view: location.search }), now);
    console.log('pad', which, 'wait', wait, JSON.stringify(r));
    await p.context().close();
  }
  await H.close();
})();
