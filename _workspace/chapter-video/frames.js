const { chromium } = require('/tmp/tw/w/node_modules/playwright-core');
const fs = require('fs');
const tl = JSON.parse(fs.readFileSync('timeline.json'));
const mode = process.argv[2] || 'stills';
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const pg = await b.newPage({ viewport: { width: 1280, height: 720 } });
  pg.on('pageerror', e => console.log('ERR', e.message));
  await pg.goto('file:///tmp/vid/scene.html');
  console.log(JSON.stringify(await pg.evaluate(t => init(t), tl)));
  if (mode === 'stills') {
    for (const t of (process.argv[3] || '3,10.5,20,25,29,38.5,42').split(',').map(Number)) { await pg.evaluate(t => render(t), t); await pg.screenshot({ path: 'still-' + t + '.png' }); }
  } else {
    fs.mkdirSync('fr', { recursive: true });
    const n = Math.round(tl.duration * tl.fps);
    for (let i = 0; i < n; i++) { await pg.evaluate(t => render(t), i / tl.fps); await pg.screenshot({ path: 'fr/' + String(i).padStart(5, '0') + '.jpg', type: 'jpeg', quality: 92 }); }
    console.log('frames', n);
  }
  await b.close();
})();
