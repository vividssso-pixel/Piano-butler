const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t486.html');
  const p = await H.open({ path: '?teacher=1&tool=scale-finder', w: 390, h: 900 });
  const bad = await p.evaluate(() => {
    const out = [], PC = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
    const pc = (n) => ((PC[n[0]] + (n.slice(1).split('#').length - 1) - (n.slice(1).split('b').length - 1) + 12) % 12);
    const rows = [];
    for (const k of MINOR_PATH) for (const f of ['natural', 'harmonic', 'melodic']) {
      const nm = spellMinor(k, f), st = MINOR_FORMS[f].steps, root = pc(k.replace('x', '##'));
      const letters = nm.map(n => n[0]);
      if (new Set(letters).size !== 7) out.push(k + ' ' + f + ' letters ' + nm.join(' '));
      nm.forEach((n, i) => { const nn = n.replace(/x/g, '##'); if (pc(nn) !== (root + st[i]) % 12) out.push(k + ' ' + f + ' wrong pitch at ' + (i + 1) + ': ' + n); });
      rows.push(k + ' ' + f + ': ' + nm.join(' '));
    }
    return { out, rows: rows.length };
  });
  console.log('minor spelling problems:', JSON.stringify(bad));
  // the clash rule: how many minor/form pairs hide fingers
  const clash = await p.evaluate(() => { const r = []; for (const k of MINOR_PATH) for (const f of ['natural', 'melodic']) for (const o of [1, 2]) { const info = MINOR_SCALES[k], e = info.octaves[o], offs = minorOffsets(f, o); if (['RH', 'LH'].some(h => e[h].some((x, i) => x === 1 && [1, 3, 6, 8, 10].includes((info.rootPc + offs[i]) % 12)))) r.push(k + ' ' + f + ' ' + o + 'oct'); } return r; });
  console.log('fingers hidden for:', clash.join(', '));
  await p.context().close();
  for (const path of ['?teacher=1&tool=modes', '?teacher=1&tool=build-major', '?teacher=1&tool=minor-forms', '?teacher=1&tool=major-fingering', '?tool=ssc-g&lock=1', '?kit=scale-finder,ssc-steps,ssc-g&kn=Scales&lock=1', '?teacher=1&tool=scale-finder&key=Bb&mode=minor']) {
    const q = await H.open({ path, w: 390, h: 900 });
    const t = await q.evaluate(() => document.body.innerText.replace(/\s+/g, ' ').slice(150, 330));
    console.log(path, '| errs', JSON.stringify(q._errs), '|', t);
    await q.context().close();
  }
  await H.close();
})();
