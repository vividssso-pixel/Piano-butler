const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const kind of ['spread', 'teacher']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=ledger-lines&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(2600); await p.emulateMedia({ media: 'print' });
    await p.pdf({ path: 'pdf431-' + kind + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
    await p.context().close();
  }
  await H.close();
})();
