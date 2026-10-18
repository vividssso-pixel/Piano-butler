// The concept book on screen (?teacher=1&tool=cb-p-scales): errors, sideways scroll, the two pads tapped through (every
// shape x every key; the key pad on every key of both rings), the notes each shape shows checked against an independent
// speller, sound stopping when the pad goes away, the hidden tool and search, the student link, the Toolbox card, links.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r1/shots';
const L = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], PC = [0, 2, 4, 5, 7, 9, 11];
const pcOf = (n) => (PC[L.indexOf(n[0])] + (n.slice(1).match(/♯|#/g) || []).length - (n.slice(1).match(/♭|b/g) || []).length + 24) % 12;
const SHAPES = { major: [0, 2, 4, 5, 7, 9, 11], nat: [0, 2, 3, 5, 7, 8, 10], harm: [0, 2, 3, 5, 7, 8, 11], mel: [0, 2, 3, 5, 7, 9, 11], penta: [0, 2, 4, 7, 9], chrom: null };
const SOUNDHOOK = `(() => {
  window.__osc = [];
  const S = OscillatorNode.prototype.start, P = OscillatorNode.prototype.stop;
  OscillatorNode.prototype.start = function (t) { this.__i = window.__osc.length; window.__osc.push({ start: t, stop: null, ctx: this.context }); return S.apply(this, arguments); };
  OscillatorNode.prototype.stop = function (t) { if (this.__i != null) window.__osc[this.__i].stop = t; return P.apply(this, arguments); };
})();`;
(async () => {
  const fs = require('fs'); fs.mkdirSync(OUT, { recursive: true });
  const H = await start('drills.t485.html');
  const log = (...a) => console.log(...a);
  for (const lang of ['en', 'ko']) for (const w of [390, 320]) {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w, h: 860, lang, dsf: 1 });
    await p.waitForTimeout(1200);
    const sw = await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]);
    const wide = await p.evaluate(() => { const W = document.documentElement.clientWidth, out = []; document.querySelectorAll('#root *').forEach(e => { const r = e.getBoundingClientRect(); if (r.width && r.right > W + 1) out.push(e.tagName + (e.getAttribute('data-cb') ? '[' + e.getAttribute('data-cb') + ']' : '') + ' ' + Math.round(r.right)); }); return out.slice(0, 8); });
    const steps = await p.$$eval('h3, [class*=step] ', a => a.length);
    log(lang + ' ' + w + 'px: scroll ' + sw.join('/') + (sw[0] > sw[1] ? ' SIDEWAYS' : '') + (wide.length ? ' wide: ' + JSON.stringify(wide) : '') + ' errs=' + JSON.stringify(p._errs));
    if (w === 390) await p.screenshot({ path: OUT + '/scr-' + lang + '-' + w + '.png', fullPage: true });
    await p.context().close();
  }
  // ── the key pad: every key on both rings ──
  {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860 });
    const pad = await p.$('[data-cb="key-pad"]');
    const rings = await pad.$$('svg[viewBox="0 0 360 360"]');
    const seen = [];
    for (let r = 0; r < rings.length; r++) {
      const keys = await rings[r].$$('g[data-key]');
      for (const k of keys) { const id = await k.getAttribute('data-key'); await k.click(); await p.waitForTimeout(60);
        const txt = await pad.evaluate(e => e.innerText.replace(/\s+/g, ' '));
        const notes = await pad.$$eval('div > span[style*="border-radius"]', a => a.map(s => s.textContent));
        seen.push([r ? 'circle' : 'clock', id, notes.join(' '), (txt.match(/(?:major|장조)[^▶]*?(?:\)|없음|flats|플랫 없음)/) || [''])[0]]); }
    }
    seen.forEach(s => log('  keypad ' + s.join(' | ')));
    log('keypad errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  // ── the shapes pad: every shape on every key; the notes against an independent check; the dots against the shape ──
  {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860 });
    const pad = await p.$('[data-cb="shapes-pad"]');
    const chips = await pad.$$('button.chip');
    let bad = 0, n = 0;
    for (let c = 0; c < chips.length; c++) {
      await chips[c].click(); await p.waitForTimeout(60);
      const shName = await chips[c].innerText(), sid = ['major', 'nat', 'harm', 'mel', 'penta', 'chrom'][c];
      const keys = await (await pad.$('svg[viewBox="0 0 360 360"]')).$$('g[data-key]');
      for (const k of keys) {
        const id = await k.getAttribute('data-key'); await k.click(); await p.waitForTimeout(40); n++;
        const lines = await pad.evaluate(e => [...e.querySelectorAll(':scope > div')].map(d => d.innerText.replace(/\s+/g, ' ').trim()));
        const notesLine = lines[3] || '', down = lines.find(x => /^Coming down|^내려올/.test(x)) || '';
        const names = notesLine.split(' ').filter(Boolean);
        const pat = SHAPES[sid];
        let ok = true, why = '';
        if (pat) {
          if (names.length !== pat.length + 1) { ok = false; why = 'count ' + names.length; }
          else { const t0 = pcOf(names[0]); names.slice(0, -1).forEach((nm, i) => { if (pcOf(nm) !== (t0 + pat[i]) % 12) { ok = false; why += ' ' + nm + '@' + i; } });
            if (sid !== 'penta') { const ls = names.slice(0, 7).map(x => x[0]); if (new Set(ls).size !== 7) { ok = false; why += ' letters ' + ls.join(''); } }
            if (pcOf(names[0]) !== ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'].indexOf(id)) { ok = false; why += ' tonic'; } }
        }
        // the shape's dots: positions on the clock = the shape turned to the key
        const dots = await pad.evaluate(e => { const s = e.querySelector('svg[viewBox="0 0 360 360"]'); const g = [...s.querySelectorAll('g')].find(x => /rotate/.test(x.getAttribute('style') || '')); if (!g) return null; const rot = parseFloat((g.getAttribute('style').match(/rotate\(([-\d.]+)deg/) || [])[1]); const cs = [...g.querySelectorAll('circle')].map(c => { const x = +c.getAttribute('cx') - 180, y = +c.getAttribute('cy') - 180; return Math.round(((Math.atan2(y, x) * 180 / Math.PI + 90 + rot) % 360 + 360) % 360 / 30) % 12; }); return cs; });
        const want = (pat || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]).map(o => (['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'].indexOf(id) + o) % 12);
        if (!dots || JSON.stringify(dots) !== JSON.stringify(want)) { ok = false; why += ' dots ' + JSON.stringify(dots); }
        if (!ok) { bad++; log('  BAD ' + sid + ' ' + id + ': ' + notesLine + ' ' + down + ' ' + why); }
        else if (/^(B|Eb|Db|Gb|Ab|F)$/.test(id) && (sid === 'harm' || sid === 'mel' || sid === 'nat')) log('  ok ' + sid + ' ' + id + ': ' + notesLine + (down ? ' / ' + down : '') + ' / ' + lines[4]);
      }
    }
    log('shapes: ' + n + ' combos, ' + bad + ' bad; errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  // ── sound: the pads stop their notes when they go away ──
  {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, store: { pb_sound_v1: JSON.stringify({ piano: false }) } });
    await p.addInitScript(SOUNDHOOK); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(900);
    for (const which of ['key-pad', 'shapes-pad']) {
      const pad = await p.$('[data-cb="' + which + '"]');
      const b = await pad.$('button.ghost-btn'); await b.click(); await p.waitForTimeout(400);
      const r = await p.evaluate(() => { const o = window.__osc, now = o.length ? o[0].ctx.currentTime : 0; return { n: o.length, future: o.filter(x => x.stop > now + 0.3).length, now }; });
      log(which + ' listen: oscillators=' + r.n + ' still scheduled beyond now=' + r.future);
      // play again (stop() first in the pad): the first run must be cut
      await b.click(); await p.waitForTimeout(200);
      const r2 = await p.evaluate(() => { const o = window.__osc, now = o[0].ctx.currentTime; return { n: o.length, future: o.filter(x => x.stop > now + 0.3).length }; });
      log(which + ' listen twice: oscillators=' + r2.n + ' beyond now=' + r2.future);
    }
    // leave the tool while the shapes pad plays
    const pad = await p.$('[data-cb="shapes-pad"]'); await (await pad.$('button.chip')).click(); await (await pad.$('button.ghost-btn')).click(); await p.waitForTimeout(300);
    const back = await p.$('button:has-text("←")'); const bt = back ? await back.innerText() : null; if (back) await back.click(); await p.waitForTimeout(500);
    const r3 = await p.evaluate(() => { const o = window.__osc, now = o[0].ctx.currentTime; return { n: o.length, future: o.filter(x => x.stop > now + 0.3).length, view: location.search }; });
    log('after leaving via "' + bt + '": still scheduled beyond now=' + r3.future + ' of ' + r3.n + ' url=' + r3.view + ' errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  await H.close();
})();
