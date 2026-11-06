// Phase 376: the chapter 1 online lesson is the Lesson Book opened on screen.
//   T1 six steps, one per book page after the opener, titled as the book (EN and KO)
//   T2 each step holds its book page's words and its moving part; the old tools are gone from the lesson
//   T3 teacher strips: shown in the teacher view, hidden in the student view
//   T4 saved ticks from the old 8-step lesson stay on their steps (storeAs)
//   T5 finger walks: Play along lights the circles; warm-ups play; no sideways scroll on a phone; no errors
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t376.html');
  const EN = ['Sit at the piano', 'Let the arm carry the hand', 'A round hand', 'Finger numbers', 'Play: finger walks', 'My five checks'];
  const KO = ['피아노 앞에 앉기', '팔이 손을 데려가요', '둥근 손', '손가락 번호', '연주: 손가락 걷기', '나의 다섯 가지 확인'];
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=posture-hands', w: 390, h: 900, lang });
    await p.waitForTimeout(800);
    const titles = await p.$$eval('section[id^="posture-hands-step-"]', els => els.map(e => e.querySelector('button span span:last-child').textContent));
    ok(JSON.stringify(titles) === JSON.stringify(lang === 'en' ? EN : KO), 'T1 ' + lang + ' steps = book pages: ' + titles.join(' / '));
    const parts = await p.evaluate(() => {
      const q = (i, sel) => !!document.querySelector('#posture-hands-step-' + i + ' ' + sel);
      return [q(0, '[data-pen-sit] svg path'), document.querySelectorAll('#posture-hands-step-1 [data-warm]').length === 6, q(2, '[data-round-hand] svg'), q(3, '[data-finger-numbers] .pb-art'),
        !!document.querySelector('#posture-hands-step-4 button') && /Play along|따라 치기/.test(document.querySelector('#posture-hands-step-4').innerText), q(5, '[data-five-checks]')];
    });
    ok(parts.every(Boolean), 'T2 ' + lang + ' moving parts in steps 1-6: ' + JSON.stringify(parts));
    const words = await p.evaluate((lang) => {
      const txt = (i) => document.querySelector('#posture-hands-step-' + i).innerText;
      const need = lang === 'en' ? [[0, 'Two things to set'], [0, 'At the piano'], [1, 'from the big parts of the body to the small'], [2, 'as if a roller sat under your forearm'], [3, 'starting from the thumb'], [3, 'The mirror game'], [4, 'Start small'], [5, 'tick how each one is going']]
        : [[0, '맞출 것은 두 가지'], [0, '피아노 앞에서'], [1, '큰 몸 부분부터 작은 부분까지'], [2, '롤러'], [3, '엄지부터 1번에서 5번까지'], [3, '거울 게임'], [4, '작게 시작해요'], [5, '하나씩 어떤지 표시해요']];
      return need.filter(([i, w]) => !txt(i).includes(w)).map(x => x.join(':'));
    }, lang);
    ok(words.length === 0, 'T2 ' + lang + ' the book\'s words are on their steps' + (words.length ? ' -- missing ' + words.join(', ') : ''));
    const old = await p.evaluate(() => /Move with the whole arm|팔 전체로 움직이기|Feel the arm weight|Meet your fingers/.test(document.querySelector('.fade-up').innerText));
    ok(!old, 'T2 ' + lang + ' the old 8-step tools are gone from the lesson');
    const strips = await p.$$eval('[data-lb-teacher]', e => e.length);
    ok(strips === 0, 'T3 ' + lang + ' student view: no teacher strips (' + strips + ')');
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    ok(sw <= 390, 'T5 ' + lang + ' no sideways scroll at 390 px (' + sw + ')');
    ok(p._errs.length === 0, 'T5 ' + lang + ' no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  // teacher view
  { const p = await H.open({ path: '?drill=posture-hands&teacher=1', w: 900, h: 900 }); await p.waitForTimeout(700);
    const n = await p.$$eval('[data-lb-teacher]', e => e.length); ok(n === 0, 'T3 teacher view: no teacher strips (Phase 399) (' + n + ')'); await p.context().close(); }
  // saved ticks: the old keys 0,1,3,5,6,7 are the six steps; old keys 2 and 4 (arm weight, meet your fingers) no longer count
  for (const [done, want] of [[{ 0: true, 1: true, 3: true, 5: true, 6: true, 7: true }, '6 of 6'], [{ 2: true, 4: true }, '0 of 6'], [{ 0: true, 7: true }, '2 of 6']]) {
    const p = await H.open({ path: '?drill=posture-hands', w: 900, h: 900, store: { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': done }) } });
    await p.waitForTimeout(600);
    const txt = await p.evaluate(() => (document.body.innerText.match(/\d+ of \d+ steps done/) || [''])[0]);
    ok(txt.startsWith(want), 'T4 old ticks ' + JSON.stringify(Object.keys(done)) + ' -> ' + txt);
    await p.context().close();
  }
  // play along lights circles; a warm-up plays
  { const p = await H.open({ path: '?drill=posture-hands', w: 520, h: 1000 }); await p.waitForTimeout(700);
    const btn = await p.$('#posture-hands-step-4 button:has-text("Play along")'); await btn.scrollIntoViewIfNeeded(); await btn.click(); await p.waitForTimeout(300);   // (beat 1 is a "3"; beat 2, from 833 ms, is a hold)
    const lit = await p.$$eval('#posture-hands-step-4 .try-box span', els => els.filter(e => getComputedStyle(e).backgroundColor === 'rgb(228, 87, 46)' && e.textContent === '3').length);
    ok(lit >= 1, 'T5 Play along lights a circle (' + lit + ')');
    await p.click('[data-warm="balloon"] button'); await p.waitForTimeout(400);
    const a = await p.$eval('[data-warm="balloon"] [aria-hidden] svg, [data-warm="balloon"] svg', e => e.innerHTML.length); await p.waitForTimeout(500);
    const b = await p.$eval('[data-warm="balloon"] svg', e => e.innerHTML);
    await p.waitForTimeout(300); const c = await p.$eval('[data-warm="balloon"] svg', e => e.innerHTML);
    ok(b !== c, 'T5 the wrist balloon moves when tapped');
    ok(p._errs.length === 0, 'T5 no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close(); }
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
