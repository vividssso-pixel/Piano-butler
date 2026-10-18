// Whole-page DOM diff t484 vs t485 on routes the patch should not change (and the toolbox, which should change by one card).
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SEED = `(() => { let s = 99; Math.random = () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; }; })();`;
const R = ['?book=lesson&ch=scales', '?book=lesson&ch=key-signatures', '?book=lesson&ch=chords', '?book=work&ch=scales', '?book=teacher&ch=key-signatures', '?book=spread&ch=first-steps', '?book=lesson&ch=posture-hands&lang=ko', '?drill=scales&tab=learn', '?drill=key-signatures&tab=learn', '?teacher=1&view=toolbox', '?teacher=1&view=toolbox&lang=ko', '?view=chapters'];
async function html(H, path) { const p = await H.open({ path, w: path.includes('book=') ? 900 : 390, h: 1200 }); await p.addInitScript(SEED); await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(1500); const h = await p.evaluate(() => document.getElementById('root').innerHTML); await p.context().close(); return h; }
(async () => {
  const A = await start('drills.t484.html'), B = await start('drills.t485.html');
  for (const r of R) { const a = await html(A, r), b = await html(B, r);
    if (a === b) { console.log('SAME ' + r + ' (' + a.length + ' chars)'); continue; }
    let i = 0; while (a[i] === b[i]) i++; let j = 0; while (a[a.length - 1 - j] === b[b.length - 1 - j] && j < Math.min(a.length, b.length) - i) j++;
    console.log('DIFF ' + r + ' len ' + a.length + ' -> ' + b.length + '\n   484: ' + a.slice(i - 60, a.length - j + 20).slice(0, 300) + '\n   485: ' + b.slice(i - 60, b.length - j + 20).slice(0, 600));
  }
  await A.close(); await B.close();
})();
