// Build CY: 'Make your own' opens in the chapter; a tool goes back to its chapter. Usage: node cy774.js drills.t774.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/cy/';
require('fs').mkdirSync(SH, { recursive: true });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t774.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  // every room with something to make: open each in place, it draws, it closes
  const q0 = await H.open({ path: '?', w: 390, h: 900 });
  const rooms = await q0.evaluate(() => { const MX = { 'first-steps': ['black-key-jam'], rhythm: ['make-card'], 'key-signatures': ['transpose'], form: ['form-builder'], melody: ['draw-tune'] };
    const ids = [...new Set(TOOLS.filter(tl => /^mk-/.test(tl.id) && !tl.hidden).map(tl => tl.ch).concat(Object.keys(MX)))]; return ids.filter(id => DRILLS.find(d => d.id === id)); });
  await q0.close();
  console.log('rooms with Make your own:', rooms.length);
  for (const id of rooms) {
    const p = await H.open({ path: '?drill=' + id, w: 390, h: 1400 }); await sleep(500);
    const btns = p.locator('[data-make-tool]'); const n = await btns.count(); let okAll = n > 0, out = [];
    for (let i = 0; i < n; i++) {
      const tid = await btns.nth(i).getAttribute('data-make-tool');
      await btns.nth(i).click(); await sleep(500);
      const open = p.locator('[data-make-open="' + tid + '"]'); const vis = await open.count() ? await open.evaluate(e => ({ h: Math.round(e.getBoundingClientRect().height), w: e.scrollWidth - e.clientWidth })) : null;
      const hrefs = await p.locator('[data-make] a[href*="?tool="]').count();
      const ok = vis && vis.h > 60 && !p._errs.length && hrefs === 0; if (!ok) okAll = false; out.push(tid + ':' + (vis ? vis.h + 'px' : 'none'));
      if (i === 0 && rooms.indexOf(id) < 3) await p.locator('[data-make="' + id + '"]').screenshot({ path: SH + 'make-' + id + '.png' });
      await btns.nth(i).click(); await sleep(250);
      if (await p.locator('[data-make-open]').count()) { okAll = false; out.push('did not close'); }
    }
    const chips = await p.$$eval('a.chip[href*="?tool="]', as => as.map(a => a.getAttribute('href')));
    const chipsOk = chips.every(h => h.includes('&from=' + id));
    say(okAll && chipsOk, id, out.join(' '), '| toolbox chips with from:', chips.length, p._errs.slice(0, 1));
    await p.close();
  }
  // back from a tool
  const back = async (path, want, click) => { const p = await H.open({ path, w: 390, h: 1000 }); await sleep(500);
    const b = p.locator('[data-testid="tool-back"]'); const txt = await b.count() ? (await b.innerText()).trim() : '(none)';
    let after = '';
    if (click && await b.count()) { await b.click(); await sleep(600); after = await p.evaluate(() => document.querySelector('[data-make]') ? 'chapter:' + document.querySelector('[data-make]').getAttribute('data-make') : (document.body.innerText.match(/Toolbox|도구함/) ? 'toolbox' : document.body.innerText.slice(0, 60))); }
    say(want.test(txt + ' ' + after) && !p._errs.length, path, '→', txt, after, p._errs.slice(0, 1)); await p.close(); };
  await back('?tool=black-key-jam&from=first-steps', /← Keyboard Patterns chapter:first-steps/, true);
  await back('?tool=black-key-jam', /← Keyboard Patterns/, false);
  await back('?tool=black-key-jam&lock=1', /\(none\)/, false);
  await back('?tool=black-key-jam&from=first-steps&lang=ko', /← /, false);
  // from the Toolbox (teacher): back to the Toolbox
  { const p = await H.open({ path: '?teacher=1&view=toolbox', w: 390, h: 1200 }); await sleep(700);
    const link = p.locator('button:has-text("Black-key jam"), a:has-text("Black-key jam")').first();
    if (await link.count()) { await link.click(); await sleep(600); const t = (await p.locator('[data-testid="tool-back"]').innerText()).trim(); say(/Toolbox/.test(t), 'from the Toolbox →', t); }
    else console.log('skip: no Black-key jam row on the Toolbox page');
    await p.close(); }
  console.log('bad', bad); await H.close();
})();
