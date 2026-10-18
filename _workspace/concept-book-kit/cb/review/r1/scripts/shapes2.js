const { start } = require('/home/claude/pbtest/kit/contentharness');
const L = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], PC = [0, 2, 4, 5, 7, 9, 11];
const acc = (s) => { let d = 0; for (const ch of s) { if (ch === '♯' || ch === '#') d++; else if (ch === '♭' || ch === 'b') d--; else if (ch === '𝄪') d += 2; else if (ch === '𝄫') d -= 2; } return d; };
const pcOf = (n) => (PC[L.indexOf(n[0])] + acc([...n].slice(1).join('')) + 24) % 12;
const SH = { major: [0,2,4,5,7,9,11], nat: [0,2,3,5,7,8,10], harm: [0,2,3,5,7,8,11], mel: [0,2,3,5,7,9,11], penta: [0,2,4,7,9], chrom: null };
const K12 = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B'];
(async () => {
  const H = await start('drills.t485.html');
  for (const lang of ['en', 'ko']) {
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, lang });
  const pad = await p.$('[data-cb="shapes-pad"]');
  const chips = await pad.$$('button.chip'); let bad = 0, n = 0; const rows = [];
  for (let c = 0; c < chips.length; c++) {
    await chips[c].click(); await p.waitForTimeout(50);
    const sid = Object.keys(SH)[c];
    const keys = await (await pad.$('svg[viewBox="0 0 360 360"]')).$$('g[data-key]');
    for (const k of keys) {
      const id = await k.getAttribute('data-key'); await k.click(); await p.waitForTimeout(30); n++;
      const info = await pad.evaluate(e => { const kids = [...e.children]; const i = kids.findIndex(d => d.querySelector && d.querySelector('svg[viewBox="0 0 360 360"]')); const after = kids.slice(i + 1).map(d => d.innerText.replace(/\s+/g, ' ').trim()); const center = e.querySelector('svg[viewBox="0 0 360 360"] > g:last-child text'); const s = e.querySelector('svg[viewBox="0 0 360 360"]'); const g = [...s.querySelectorAll('g')].find(x => /rotate/.test(x.getAttribute('style') || '')); const rot = parseFloat((g.getAttribute('style').match(/rotate\(([-\d.]+)deg/) || [])[1]); const dots = [...g.querySelectorAll('circle')].map(c => { const x = +c.getAttribute('cx') - 180, y = +c.getAttribute('cy') - 180; return Math.round(((Math.atan2(y, x) * 180 / Math.PI + 90 + rot) % 360 + 360) % 360 / 30) % 12; }); const coral = [...g.querySelectorAll('line')].filter(l => l.getAttribute('stroke') === '#e4572e').length; return { after, center: center ? center.textContent : '', dots, coral, label: s.getAttribute('aria-label') }; });
      const notes = info.after[0].split(' ').filter(Boolean), pat = SH[sid]; let ok = true, why = '';
      const want = (pat || [0,1,2,3,4,5,6,7,8,9,10,11]).map(o => (K12.indexOf(id) + o) % 12);
      if (JSON.stringify(info.dots) !== JSON.stringify(want)) { ok = false; why += ' dots'; }
      if (pat) { if (notes.length !== pat.length + 1) { ok = false; why += ' count' + notes.length; }
        else { const t0 = K12.indexOf(id); notes.slice(0, -1).forEach((nm, i) => { if (pcOf(nm) !== (t0 + pat[i]) % 12) { ok = false; why += ' pc:' + nm; } }); if (notes[0] !== notes[notes.length - 1]) { ok = false; why += ' ends'; }
          if (pat.length === 7) { const ls = notes.slice(0, 7).map(x => x[0]); if (new Set(ls).size !== 7) { ok = false; why += ' letters'; } } } }
      // coral lines = half steps of the shape
      const halves = pat ? pat.map((o, i) => ((pat[(i + 1) % pat.length] - o + 12) % 12 === 1 ? 1 : 0)).reduce((a, b) => a + b, 0) : 12;
      if (info.coral !== halves) { ok = false; why += ' coral' + info.coral; }
      if (!ok) { bad++; console.log('BAD', lang, sid, id, info.after.join(' / '), why); }
      if (lang === 'en' && ['Db','Eb','Gb','Ab','Bb'].includes(id)) rows.push(sid + ' ' + id + ' [' + info.center + ']: ' + info.after.join(' / '));
      if (lang === 'ko' && id === 'Ab' && ['nat','penta','chrom'].includes(sid)) rows.push('KO ' + sid + ' ' + id + ' [' + info.center + ']: ' + info.after.join(' / ') + ' || ' + info.label);
    }
  }
  console.log(lang + ': ' + n + ' combos, ' + bad + ' bad, errs=' + JSON.stringify(p._errs));
  rows.forEach(r => console.log('  ' + r));
  await p.context().close();
  }
  await H.close();
})();
