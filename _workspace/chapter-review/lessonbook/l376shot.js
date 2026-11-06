// The chapter 1 online lesson (Phase 376): full-page shots, errors, and where each step sits
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t376.html');
  for (const [w, tag, lang] of [[390, 'phone', 'en'], [900, 'desk', 'en'], [390, 'phoneko', 'ko']]) {
    const p = await H.open({ path: '?drill=posture-hands' + (lang === 'ko' ? '' : ''), w, h: 900, lang });
    await p.waitForTimeout(800);
    const info = await p.evaluate(() => ({
      steps: [...document.querySelectorAll('section[id^="posture-hands-step-"]')].map(s => [s.id, Math.round(s.getBoundingClientRect().top + scrollY), s.querySelector('span span:last-child') && s.querySelector('button span span:last-child').textContent]),
      sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, h: document.documentElement.scrollHeight,
      pen: !!document.querySelector('[data-pen-sit] svg path'), screens: document.querySelectorAll('.lb-screen').length }));
    console.log(tag, JSON.stringify(info), 'errs', p._errs.join(' | ').slice(0, 400));
    await p.screenshot({ path: '../shots/l376-' + tag + '.png', fullPage: true });
    await p.context().close();
  }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
