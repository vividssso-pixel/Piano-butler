// Steps 2-6 of the new chapter 1 lesson: interactions work, nothing errors, and a shot of each step
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t376.html');
  const p = await H.open({ path: '?drill=posture-hands', w: 390, h: 900, lang: process.env.KO ? 'ko' : 'en' });
  await p.waitForTimeout(600);
  const out = {};
  // warm-ups: play one, then watch all briefly
  await p.click('[data-warm="dive"] button'); await p.waitForTimeout(900);
  out.warmPlaying = await p.$$eval('[data-warm] button[aria-pressed="true"]', e => e.length);
  await p.click('[data-warmups] .ghost-btn'); await p.waitForTimeout(500);
  out.warmAll = await p.$eval('[data-warmups] .ghost-btn', e => e.textContent);
  await p.click('[data-warmups] .ghost-btn');
  // round hand: each chip
  const chips = await p.$$('[data-round-hand] button.chip');
  out.handChips = chips.length;
  for (const c of chips) { await c.click(); await p.waitForTimeout(520); }
  out.handText = await p.$eval('[data-round-hand]', e => e.innerText.split('\n').slice(-2).join(' ').slice(0, 120));
  await chips[1].click(); await p.waitForTimeout(700);   // roller on
  await (await p.$('[data-round-hand] [role=img]')).screenshot({ path: '../shots/l376-roller.png' });
  await chips[0].click();
  // fingers: tap left 4 through the button, then play the game once
  await p.click('[data-finger-numbers] button[aria-label$=" 4"]'); await p.waitForTimeout(100);
  out.fingerText = await p.$eval('[data-finger-numbers]', e => e.innerText.split('\n').filter(Boolean).slice(-3).join(' | '));
  // stars
  await p.click('[data-five-checks] button[aria-pressed="false"]'); await p.waitForTimeout(100);
  out.stars = await p.$$eval('[data-five-checks] button[aria-pressed="true"]', e => e.length);
  out.store = await p.evaluate(() => localStorage.getItem('pb_five_checks_v1'));
  out.sw = await p.evaluate(() => document.documentElement.scrollWidth);
  out.errs = p._errs.join(' | ');
  console.log(JSON.stringify(out, null, 1));
  for (let i = 1; i <= 5; i++) { const el = await p.$('#posture-hands-step-' + i); await el.screenshot({ path: '../shots/l376-step' + (i + 1) + (process.env.KO ? 'ko' : '') + '.png' }); }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
