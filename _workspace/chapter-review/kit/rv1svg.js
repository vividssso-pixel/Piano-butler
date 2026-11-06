// Pull the chapter 1 drawings out of the app as plain SVG for the public page
const { start } = require('./contentharness');
const fs = require('fs'); const OUT = '../rv1/svg'; fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const H = await start('drills.t366.html');
  const p = await H.open({ path: '?drill=posture-hands', w: 760, h: 1000, store: { pb_mode_v1: 'teacher' }, reducedMotion: 'reduce' });
  await p.waitForTimeout(600);
  const step = (i) => '#posture-hands-step-' + i;
  const grab = async (sel, name) => { const h = await p.$eval(sel, e => e.outerHTML); fs.writeFileSync(OUT + '/' + name + '.svg', h); console.log(name, h.length); };
  // hero
  await grab('.fade-up svg', 'hero');
  // step 1: stool -- press "Just right"
  await p.click(step(0) + ' button.chip:has-text("Just right")'); await p.waitForTimeout(300);
  await grab(step(0) + ' .try-box svg', 'sit-good');
  for (const [lab, n] of [['Stool too low', 'sit-low'], ['Stool too high', 'sit-high'], ['Too close', 'sit-close'], ['Too far', 'sit-far']]) {
    await p.click(step(0) + ' button.chip:has-text("' + lab + '")'); await p.waitForTimeout(300); await grab(step(0) + ' .try-box svg', n);
  }
  // step 4: hand shape poses
  const chips = await p.$$(step(3) + ' .try-box button.chip');
  console.log('pose chips', chips.length);
  for (let i = 0; i < chips.length; i++) { const lab = await chips[i].innerText(); await chips[i].click(); await p.waitForTimeout(700); await grab(step(3) + ' .try-box svg', 'hand-' + i); console.log('  ', i, lab); }
  // step 5: anatomy, step 6: both hands
  await grab(step(4) + ' .try-box svg', 'anatomy');
  const hands = await p.$$eval(step(5) + ' .try-box svg', els => els.map(e => e.outerHTML));
  hands.forEach((h, i) => fs.writeFileSync(OUT + '/numbers-' + i + '.svg', h)); console.log('hands', hands.length);
  console.log('errs', p._errs.join('|'));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
