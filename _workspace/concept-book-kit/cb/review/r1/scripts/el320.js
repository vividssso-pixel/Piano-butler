const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 320, h: 760, dsf: 2 });
  const shots = { sigs: '[role=img][aria-label^="The seven sharps"]', keypad: '[data-cb="key-pad"]', shapes: '[data-cb="shapes-pad"]', ladder: '.cb-ladder' };
  for (const [k, sel] of Object.entries(shots)) { const e = await p.$(sel); if (!e) { console.log('missing', k); continue; } await e.scrollIntoViewIfNeeded(); await e.screenshot({ path: '/home/claude/pbtest/cb/review/r1/shots/el320-' + k + '.png' }); }
  // p6 figures grid (still picture of step 5)
  const figs = await p.$$('[aria-label$="on the keyboard clock."]'); if (figs[0]) { const g = await figs[0].evaluateHandle(e => e.closest('.lb-pic')); await g.asElement().screenshot({ path: '/home/claude/pbtest/cb/review/r1/shots/el320-figs.png' }); }
  // sigs key labels vs sign x positions
  const al = await p.evaluate(() => { const box = document.querySelector('[role=img][aria-label^="The seven sharps"]'); const out = []; box.querySelectorAll(':scope > div').forEach(d => { const svgs = d.querySelectorAll('svg'); if (svgs.length < 2) return; const staff = svgs[0], lab = svgs[1]; const signs = [...staff.querySelectorAll('path,text,g')].filter(x => x.getAttribute('fill') === '#e4572e' || (x.getAttribute('stroke') === '#e4572e')).map(x => { const r = x.getBoundingClientRect(); return Math.round(r.left + r.width / 2); }); const labs = [...lab.querySelectorAll('text')].slice(1).map(x => { const r = x.getBoundingClientRect(); return Math.round(r.left + r.width / 2); }); out.push({ signs: [...new Set(signs)].slice(0, 9), labs }); }); return out; });
  console.log(JSON.stringify(al));
  await p.context().close(); await H.close();
})();
