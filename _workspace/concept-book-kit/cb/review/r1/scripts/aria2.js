const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860 });
  const r = await p.$$eval('[role=img]', a => a.filter(x => !x.getAttribute('aria-label')).map(x => x.outerHTML.slice(0, 200) + ' IN ' + (x.closest('[data-cb]') ? x.closest('[data-cb]').getAttribute('data-cb') : (x.closest('[data-cb-tool]') ? x.closest('[data-cb-tool]').getAttribute('data-cb-tool') : '?'))));
  console.log(r);
  // svg without role/aria in the pads (KSStaff)
  const ks = await p.$$eval('[data-cb] svg', a => a.map(s => (s.getAttribute('role') || '-') + '|' + (s.getAttribute('aria-label') || s.getAttribute('aria-hidden') || '-')));
  console.log(ks);
  await p.context().close(); await H.close();
})();
