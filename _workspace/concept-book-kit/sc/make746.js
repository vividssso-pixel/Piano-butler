const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => { const H = await start(process.argv[2]); const S = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/';
  const rooms = ['pulse', 'reading-steps', 'chords', 'dynamics', 'tempo', 'minor-scales', 'intervals', 'accidentals', 'styles', 'listen-6', 'scales-6', 'arps-6', 'harmony-6', 'listen-7', 'scales-7', 'arps-7', 'pieces-78', 'listen-8', 'scales-8', 'arps-8'];
  let i = 0;
  for (const r of rooms) { const lang = i++ % 2 ? 'ko' : 'en'; const p = await H.open({ path: '?drill=' + r + '&tab=learn', w: 390, h: 1200, lang, dsf: 1.5 }); await p.waitForTimeout(1200);
    const m = p.locator('[data-make="' + r + '"]'); const n = await m.count();
    let line = r + ' ' + lang + ' make:' + n; if (n) { line += ' | ' + (await m.innerText()).replace(/\n/g, ' / ').slice(0, 140); if (['chords', 'arps-8', 'listen-7', 'scales-6'].includes(r)) { await m.scrollIntoViewIfNeeded(); await p.screenshot({ path: S + 'make-' + r + '.png' }); } }
    console.log(line, p._errs.length ? p._errs : ''); await p.close(); }
  await H.close(); })();
