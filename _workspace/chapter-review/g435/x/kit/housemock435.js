const { start } = require('/home/claude/pbtest/kit/contentharness'); const fs = require('fs');
(async () => {
  const L = JSON.parse(fs.readFileSync('/home/claude/pbtest/plan435/levels.json'));
  const H = await start('drills.t433.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=work&ch=front&lang=' + lang, w: 1000, h: 1400, dsf: 2 });
    await p.evaluate(() => Promise.all([document.fonts.load('700 12px Cinzel'), document.fonts.load("700 15px 'Cormorant Garamond'"), document.fonts.load("italic 700 17px 'Cormorant Garamond'")]));
    const svgs = await p.evaluate((L) => {
      rdCtx = null;
      if (!DRILLS.find(d => d.id === 'accidentals')) { const tn = DRILLS.find(d => d.id === 'tones'); DRILLS.push({ ...tn, id: 'accidentals', label: 'Accidentals' }); }
      CH_SHORT['accidentals'] = ['Accidentals', '임시표']; HOUSE_ICONS['accidentals'] = '<path d="M17 7 V26 M27 13 V32"/><path d="M17 16 L27 12.5 M17 24 L27 20.5" stroke-width="2.6"/><path d="M36 5 V31"/>';
      const nums = {}; let k = 0; L.forEach(l => l.ids.forEach(id => { nums[id] = ++k; }));
      const stages = L.map((l, i) => ({ s: { en: l.en, ko: l.ko }, i, ids: l.ids, st: l.ids.map(id => ['posture-hands', 'first-steps', 'note-names', 'staff', 'whole-staff', 'ledger-lines'].includes(id) ? 'done' : id === 'tones' ? 'started' : 'new') }));
      const src = townhouseSvg.toString().replace('for(let k=6;k>=0;k--)', 'for(let k=view.stages.length-1;k>=0;k--)').replace("'Start · climb up, one room at a time','출발 · 한 방씩 위로 올라가요'", "'Start · floor by floor, any room first','출발 · 한 층씩, 방은 마음대로'");
      CH_SHORT['tones'] = ['Tones & semitones', '온음과 반음'];
      const f = new Function('return ' + src)();
      const out = {};
      for (const [nm, o] of [['wide', { wide: true }], ['tall', {}]]) { const h = f({ stages, here: 'tones', nums }, o); out[nm] = penSvg([{ k: 'raw', svg: h.svg }], { vb: h.vb, id: 'hm' + nm }); }
      return out;
    }, L);
    for (const nm of ['wide', 'tall']) {
      await p.evaluate((svg) => { document.body.innerHTML = '<div id="mock" style="width:' + (svg.includes('viewBox="0 0 720') ? 900 : 420) + 'px;background:#fff">' + svg.replace('<svg ', '<svg style="width:100%;display:block" ') + '</div>'; }, svgs[nm]);
      await p.waitForTimeout(300); await (await p.$('#mock')).screenshot({ path: '/home/claude/pbtest/plan435/house-' + nm + '-' + lang + '.png' });
    }
    for (const nm of ['wide', 'tall']) fs.writeFileSync('/home/claude/pbtest/plan435/house-' + nm + '-' + lang + '.svg', svgs[nm]);
    console.log(lang, Object.entries(svgs).map(([k, v]) => k + ':' + v.length + ':' + v.slice(0, 60)).join(' | '), p._errs.slice(0, 2));
    await p.context().close();
  }
  await H.close();
})();
