// Whole-page DOM diff t484 vs t485 on routes the patch should not change (and the toolbox, which should change by one card).
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SEED = `(() => { let s = 99; Math.random = () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; }; })();`;
const R = ['KO?drill=key-signatures&tab=learn', 'KO?drill=scales&tab=learn', 'KO?teacher=1&view=toolbox', 'KO?teacher=1&tool=relative-minor', 'KO?teacher=1&tool=all-keys', 'KO?teacher=1&tool=build-major', 'KO?teacher=1&tool=circle-fifths', 'KO?teacher=1&tool=minor-forms', 'KO?teacher=1&tool=modes', 'KO?teacher=1&tool=sharps-order', 'KO?teacher=1&tool=place-it', 'KO?teacher=1&tool=transpose'];
async function html(H, path0) { const ko = path0.startsWith('KO'), path = ko ? path0.slice(2) : path0; const p = await H.open({ path, lang: ko ? 'ko' : undefined, w: path.includes('book=') ? 900 : 390, h: 1200 }); await p.addInitScript(SEED); await p.reload(); await p.waitForSelector('#root *'); if (ko) { const b = await p.$('button.chip:has-text("한국어")'); if (b) { await b.click(); await p.waitForTimeout(600); } } await p.waitForTimeout(1500); const h = await p.evaluate(() => document.getElementById('root').innerHTML); await p.context().close(); return h; }
(async () => {
  const A = await start('drills.t484.html'), B = await start('drills.t485.html');
  for (const r of R) { const a = await html(A, r), b = await html(B, r);
    if (a === b) { console.log('SAME ' + r + ' (' + a.length + ' chars)'); continue; }
    let i = 0; while (a[i] === b[i]) i++; let j = 0; while (a[a.length - 1 - j] === b[b.length - 1 - j] && j < Math.min(a.length, b.length) - i) j++;
    console.log('DIFF ' + r + ' len ' + a.length + ' -> ' + b.length + '\n   484: ' + a.slice(i - 60, a.length - j + 20).slice(0, 300) + '\n   485: ' + b.slice(i - 60, b.length - j + 20).slice(0, 600));
  }
  await A.close(); await B.close();
})();
