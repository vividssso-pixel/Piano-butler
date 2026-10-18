// One sound at a time, and silence when leaving: record every audio source's start and stop time.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const PATCH = `(() => { window.__src = []; const P = AudioScheduledSourceNode.prototype, s0 = P.start, s1 = P.stop;
  P.start = function (w) { this.__r = { t0: w || (this.context && this.context.currentTime) || 0, t1: Infinity, made: performance.now() }; window.__src.push(this.__r); return s0.apply(this, arguments); };
  P.stop = function (w) { if (this.__r) this.__r.t1 = Math.min(this.__r.t1, w == null ? this.context.currentTime : w); return s1.apply(this, arguments); }; })();`;
(async () => {
  const H = await start('drills.t485.html');
  const open = async (path) => { const p = await H.open({ path, w: 390, h: 860, dsf: 1 }); await p.addInitScript(PATCH); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(1200); return p; };
  const mark = (p) => p.evaluate(() => ({ n: window.__src.length, now: (window.__ctxNow = (() => { try { return getAudio().currentTime; } catch (e) { return 0; } })()) }));
  // count notes made before the mark that still sound after it (start later than now+0.15 and not stopped before it starts)
  const still = (p, m) => p.evaluate((m) => window.__src.slice(0, m.n).filter(r => r.t0 > m.now + 0.15 && r.t1 > r.t0 + 0.02).length, m);
  const after = (p, m) => p.evaluate((m) => window.__src.slice(m.n).length, m);
  const click = async (p, sel, txt) => { const els = await p.$$(sel); for (const e of els) { const t = (await e.innerText()).trim(); if (!txt || t.includes(txt)) { await e.scrollIntoViewIfNeeded(); await e.click(); return true; } } return false; };
  const tests = [
    ['key pad, then shapes pad', '?tool=cb-p-scales&lock=1', async (p) => { await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(700); const m = await mark(p); await click(p, '[data-cb="shapes-pad"] button', 'Listen'); await p.waitForTimeout(400); return m; }],
    ['shapes pad 6, then shapes pad 7', '?tool=cb-p-scales&lock=1', async (p) => { const sp = await p.$$('[data-cb="shapes-pad"]'); await (await sp[0].$('button:has-text("Listen")')).click(); await p.waitForTimeout(700); const m = await mark(p); await (await sp[1].$('button:has-text("Listen")')).click(); await p.waitForTimeout(400); return m; }],
    ['chapter-16 pad (step 1), then key pad', '?tool=cb-p-scales&lock=1', async (p) => { const st = await p.$('[data-lb-screen="2"]'); await (await st.$('button:has-text("Listen")')).click(); await p.waitForTimeout(700); const m = await mark(p); await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(400); return m; }],
    ['key pad, then chapter-16 pad', '?tool=cb-p-scales&lock=1', async (p) => { await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(700); const m = await mark(p); const st = await p.$('[data-lb-screen="2"]'); await (await st.$('button:has-text("Listen")')).click(); await p.waitForTimeout(400); return m; }],
    ['circle pad, then key pad', '?tool=cb-p-scales&lock=1', async (p) => { await click(p, '[data-cb="circle-pad"] button', 'Listen'); await p.waitForTimeout(700); const m = await mark(p); await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(400); return m; }],
    ['key pad, same Listen twice', '?tool=cb-p-scales&lock=1', async (p) => { await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(700); const m = await mark(p); await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(400); return m; }],
    ['shapes pad, then pick another key', '?tool=cb-p-scales&lock=1', async (p) => { const sp = await p.$('[data-cb="shapes-pad"]'); await (await sp.$('button:has-text("Listen")')).click(); await p.waitForTimeout(700); const m = await mark(p); await (await sp.$('g[data-key="D"]')).click(); await p.waitForTimeout(400); return m; }],
    ['shapes pad, then leave (← Toolbox)', '?teacher=1&tool=cb-p-scales', async (p) => { const sp = await p.$('[data-cb="shapes-pad"]'); await (await sp.$('button:has-text("Listen")')).click(); await p.waitForTimeout(700); const m = await mark(p); await p.evaluate(() => window.scrollTo(0, 0)); await click(p, 'button', '← Toolbox'); await p.waitForTimeout(600); return m; }],
    ['key pad, then leave (← Toolbox)', '?teacher=1&tool=cb-p-scales', async (p) => { await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(700); const m = await mark(p); await p.evaluate(() => window.scrollTo(0, 0)); await click(p, 'button', '← Toolbox'); await p.waitForTimeout(600); return m; }],
    ['circle pad, then leave (← Toolbox)', '?teacher=1&tool=cb-p-scales', async (p) => { await click(p, '[data-cb="circle-pad"] button', 'Listen'); await p.waitForTimeout(700); const m = await mark(p); await p.evaluate(() => window.scrollTo(0, 0)); await click(p, 'button', '← Toolbox'); await p.waitForTimeout(600); return m; }],
    ['chapter-16 pad (step 1), then leave', '?teacher=1&tool=cb-p-scales', async (p) => { const st = await p.$('[data-lb-screen="2"]'); await (await st.$('button:has-text("Listen")')).click(); await p.waitForTimeout(700); const m = await mark(p); await p.evaluate(() => window.scrollTo(0, 0)); await click(p, 'button', '← Toolbox'); await p.waitForTimeout(600); return m; }],
    ['build-major tool (in book), then key pad', '?tool=cb-p-scales&lock=1', async (p) => { const bm = await p.$('[data-cb-tool="build-major"]'); const bts = await bm.$$('button'); for (const b of bts) { if ((await b.innerText()).trim() === 'T') { await b.click(); break; } } await p.waitForTimeout(150); const m = await mark(p); await click(p, '[data-cb="key-pad"] button', 'Listen'); await p.waitForTimeout(400); return m; }],
    ['shapes pad, then a tool in the book plays (order of sharps)', '?tool=cb-p-scales&lock=1', async (p) => { const sp = await p.$('[data-cb="shapes-pad"]'); await (await sp.$('button:has-text("Listen")')).click(); await p.waitForTimeout(700); const m = await mark(p); const so = await p.$('[data-cb-tool="sharps-order"]'); const b = await so.$('button:has-text("Play")'); if (b) { await b.scrollIntoViewIfNeeded(); await b.click(); } await p.waitForTimeout(400); return m; }],
  ];
  for (const [name, path, fn] of tests) {
    const p = await open(path);
    const m = await fn(p);
    const s = await still(p, m), a = await after(p, m);
    console.log((s ? 'OVERLAP ' : 'ok      ') + name + ': first sound still scheduled after the second action = ' + s + ' notes; notes started after = ' + a + (p._errs.length ? ' errs ' + p._errs.join('|') : ''));
    await p.context().close();
  }
  await H.close();
})();
