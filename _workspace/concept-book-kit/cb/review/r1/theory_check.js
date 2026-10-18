// Theory check for the Phase 485 concept book: evaluate the page's own cbSpell7 / cbNames / cbMidi / cbTonic / cbSteps
// and compare with an independent speller.
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860 });
  const out = await p.evaluate(() => {
    const L = ['C','D','E','F','G','A','B'], PC = [0,2,4,5,7,9,11];
    const pcOf = (n) => (PC[L.indexOf(n[0])] + (n.slice(1).match(/#/g)||[]).length - (n.slice(1).match(/b/g)||[]).length + 24) % 12;
    // independent: each letter once from the tonic's letter; accidentals as needed
    const ref7 = (tonic, pat) => pat.map((o, i) => { const Lt = L[(L.indexOf(tonic[0]) + i) % 7]; let d = ((pcOf(tonic) + o - PC[L.indexOf(Lt)]) % 12 + 12) % 12; if (d > 6) d -= 12;
      if (Math.abs(d) > 2) return '??'; return Lt + (d > 0 ? '#'.repeat(d) : 'b'.repeat(-d)); });
    const res = { shapes: [], errs: [], rows: [] };
    const KEYS = KEY12; // the clock's keys
    // what a theory book would expect as the tonic spelling for each clock key and shape
    const expectMinor = { C:'C', Db:'C#', D:'D', Eb:'Eb', E:'E', F:'F', Gb:'F#', G:'G', Ab:'G#', A:'A', Bb:'Bb', B:'B' };
    for (const sh of CB_SHAPES) {
      for (const k of KEYS) {
        const tn = cbTonic(k, sh), names = cbNames(k, sh), midi = cbMidi(k, sh), steps = cbSteps(sh.pat);
        const row = { sh: sh.id, k, tn, names: names && names.join(' '), down: sh.down ? cbSpell7(tn, sh.down).join(' ') : '', steps, midi: midi.join(',') };
        res.rows.push(row);
        // tonic spelling
        const wantTn = (sh.id === 'major' || sh.id === 'penta' || sh.id === 'chrom') ? k : expectMinor[k];
        if (tn !== wantTn) res.errs.push(sh.id + ' ' + k + ': tonic ' + tn + ' want ' + wantTn);
        // pitch classes of names = tonic pc + pattern
        if (names) {
          const pats = sh.id === 'penta' ? [0,2,4,7,9] : sh.pat;
          names.forEach((n, i) => { if ((pcOf(n) - pcOf(names[0]) + 12) % 12 !== pats[i]) res.errs.push(sh.id + ' ' + k + ': ' + n + ' at ' + i + ' wrong pc'); });
          if (sh.id !== 'penta') { const r = ref7(tn, sh.pat).join(' '); if (r !== names.join(' ')) res.errs.push(sh.id + ' ' + k + ': ' + names.join(' ') + ' vs ref ' + r);
            // each letter once
            const lets = names.map(n => n[0]); if (new Set(lets).size !== 7) res.errs.push(sh.id + ' ' + k + ': letters repeat'); }
          else { // pentatonic = major degrees 1 2 3 5 6, spelled as the major scale
            const maj = spellScale(k); const want = [0,1,2,4,5].map(i => maj[i]).join(' '); if (want !== names.join(' ')) res.errs.push('penta ' + k + ' ' + names.join(' ') + ' vs ' + want); }
          if (names.some(n => /[^#b]/.test(n.slice(1)))) res.errs.push(sh.id + ' ' + k + ': odd accidental');
        }
        // midi: up = tonic + pat, top octave, down = reverse of (down || pat)
        const pc = pbKeyPc(k), b = 60 + pc - (pc > 6 ? 12 : 0);
        const up = sh.pat.map(o => b + o), dn = [...(sh.down || sh.pat)].reverse().map(o => b + o);
        const want = [...up, b + 12, ...dn].join(',');
        if (want !== midi.join(',')) res.errs.push(sh.id + ' ' + k + ': midi');
        if ((midi[0] % 12) !== pcOf(tn)) res.errs.push(sh.id + ' ' + k + ': midi tonic pc ' + midi[0] % 12 + ' vs ' + pcOf(tn));
        // names vs midi
        if (names) names.forEach((n, i) => { if (pcOf(n) !== (sh.id === 'penta' ? (b + [0,2,4,7,9][i]) % 12 : midi[i] % 12)) res.errs.push(sh.id + ' ' + k + ': name/midi ' + n); });
      }
    }
    // major table vs spellScale
    res.table = CB_TABLE.map(k => k + ': ' + spellScale(k).join(' ') + ' | ' + (KEY_SIGS.find(x => x.major === k) || {}).count);
    CB_TABLE.forEach(k => { const r = ref7(k, [0,2,4,5,7,9,11]).join(' '), s = spellScale(k).join(' '); if (r !== s) res.errs.push('table ' + k + ': ' + s + ' vs ' + r); });
    // all 15 KEY_SIGS majors and their relative minors (natural / harmonic / melodic)
    res.ks = KEY_SIGS.map(x => { const nat = ref7(x.minor, [0,2,3,5,7,8,10]).join(' '); const accs = x.type ? (x.type === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, x.count) : [];
      // check: natural minor uses exactly the key signature
      const ok = nat.split(' ').every(n => n.length === 1 ? !accs.some(a => a[0] === n) : accs.includes(n));
      return x.major + ' / ' + x.minor + 'm: ' + accs.join(' ') + ' | nat ' + nat + (ok ? '' : '  <-- MISMATCH'); });
    // relative minor = degree 6, 3 half steps below
    KEY_SIGS.forEach(x => { if (spellScale(x.major)[5] !== x.minor) res.errs.push('relative ' + x.major + ': deg6 ' + spellScale(x.major)[5] + ' vs ' + x.minor); });
    res.steps = CB_SHAPES.map(sh => sh.id + ': ' + cbSteps(sh.pat));
    res.sharpPos = SHARP_POS; res.flatPos = FLAT_POS; res.fifths = FIFTHS.map((k, i) => k + ' ' + FIFTHS_SIG[i]);
    res.sigkeys = CB_SIGKEYS;
    // naming rules on page 4 from the data: sharps: last sharp + half step; flats: last but one
    res.naming = KEY_SIGS.filter(x => x.type).map(x => { const o = (x.type === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, x.count), last = o[o.length - 1];
      let name = x.type === 'sharp' ? null : (o.length > 1 ? o[o.length - 2] : 'F');
      if (x.type === 'sharp') { const pcL = pcOf(last), up = (pcL + 1) % 12; const letter = L[(L.indexOf(last[0]) + 1) % 7]; let d = ((up - PC[L.indexOf(letter)]) % 12 + 12) % 12; if (d > 6) d -= 12; name = letter + (d === 1 ? '#' : d === -1 ? 'b' : ''); }
      return x.major + ': rule gives ' + name + (name === x.major ? '' : '  <-- MISMATCH'); });
    return res;
  });
  console.log('ERRORS:', out.errs.length ? out.errs : 'none');
  console.log('\nSTEPS:', out.steps.join('\n'));
  console.log('\nTABLE:\n' + out.table.join('\n'));
  console.log('\nKEY_SIGS:\n' + out.ks.join('\n'));
  console.log('\nNAMING:\n' + out.naming.join('\n'));
  console.log('\nFIFTHS:', out.fifths.join(' | '));
  console.log('\nPOS', JSON.stringify(out.sharpPos), JSON.stringify(out.flatPos), JSON.stringify(out.sigkeys));
  console.log('\nROWS (shape key tonic: names | down | midi):');
  for (const r of out.rows) console.log(r.sh.padEnd(6), r.k.padEnd(3), r.tn.padEnd(3), ':', (r.names || '(none)').padEnd(28), r.down ? '| down ' + r.down : '', '|', r.midi);
  console.log('page errors:', p._errs);
  await p.context().close(); await H.close();
})();
