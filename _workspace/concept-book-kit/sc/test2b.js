const { start } = require('/home/claude/pbtest/kit/contentharness');
const route = [
  ['ch16-learn', '?teacher=1&drill=scales&tab=learn'], ['ch19-learn', '?teacher=1&drill=key-signatures&tab=learn'],
  ['book-en', '?book=concept&ch=p-scales&lang=en'], ['book-ko', '?book=concept&ch=p-scales&lang=ko'],
  ['screen', '?teacher=1&tool=cb-p-scales'], ['student-screen', '?tool=cb-p-scales&lock=1'],
];
async function grab(H, path, lang, toolbox) {
  const p = await H.open({ path, w: 390, h: 900, lang }); await p.waitForTimeout(1200);
  if (toolbox) { const b = p.locator('text=/^(Toolbox|도구함)$/').first(); if (await b.count()) { await b.click(); await p.waitForTimeout(900); } }
  const o = await p.evaluate(() => ({ lines: document.body.innerText.split('\n').map(x => x.trim()).filter(Boolean), hs: document.documentElement.scrollWidth - document.documentElement.clientWidth }));
  o.errs = p._errs.slice(); await p.context().close(); return o;
}
(async () => {
  const out = {};
  for (const b of ['drills.t489.html', 'drills.t490.html']) {
    const H = await start(b);
    for (const [k, r] of route) for (const lang of ['en', 'ko']) out[b + '|' + k + '|' + lang] = await grab(H, r, lang, false);
    for (const lang of ['en', 'ko']) out[b + '|toolbox|' + lang] = await grab(H, '?teacher=1', lang, true);
    await H.close();
  }
  const keys = Object.keys(out).filter(k => k.startsWith('drills.t489'));
  for (const k of keys) {
    const a = out[k], n = out[k.replace('t489', 't490')];
    const sa = new Set(a.lines), sn = new Set(n.lines);
    const gone = a.lines.filter(x => !sn.has(x)), add = n.lines.filter(x => !sa.has(x));
    console.log((gone.length + add.length ? 'DIFF ' : 'same ') + k.slice(13) + ' hs ' + a.hs + '->' + n.hs + ' errs ' + n.errs.length);
    if (gone.length + add.length) { console.log('   -', JSON.stringify(gone.slice(0, 14))); console.log('   +', JSON.stringify(add.slice(0, 14))); }
  }
})();
