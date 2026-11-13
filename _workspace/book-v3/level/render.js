// Level book HTML -> PDF (waits for the shrink-to-fit pass)
const { chromium } = require('playwright');
(async () => { const b = await chromium.launch();
  for (const [h, pdf] of [['levelbook-beginner', process.argv[2]], ['levelbook-prelim', process.argv[2].replace('beginner', 'prelim')], ['levelbook-grade 1', process.argv[2].replace('beginner', 'grade1')]]) {
    const p = await b.newPage(); await p.goto('file:///mnt/user-data/outputs/house-rooms/' + h + '.html');
    await p.waitForSelector('body[data-pruned]', { timeout: 20000 }); await p.waitForTimeout(800);
    await p.pdf({ path: pdf, format: 'A4', printBackground: true }); await p.close(); }
  await b.close(); })();
