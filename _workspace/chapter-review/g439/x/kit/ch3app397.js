// Phase 397 checks: the chapter 3 app lesson is the book on screen; the drill's levels; the printed books fit.
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t397.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=note-names', w: 390, h: 900, lang });
    await p.waitForTimeout(900);
    const titles = await p.$$eval('section[id^="note-names-step-"]', els => els.map(e => e.querySelector('button span span:last-child').textContent));
    const EN = ['A to G on the keys', 'The letter wheel', 'Forwards up, backwards down', 'Name it at a glance', 'Skip a letter', 'Play by letter names', 'My five checks'];
    const KO = ['건반 위의 A부터 G', '글자 관람차', '위로는 앞으로, 아래로는 거꾸로', '보자마자 이름 대기', '한 글자 건너뛰기', '음이름 보고 연주하기', '나의 다섯 가지 확인'];
    ok(JSON.stringify(titles) === JSON.stringify(lang === 'en' ? EN : KO), 'T1 ' + lang + ' steps = book pages: ' + titles.join(' / '));
    const parts = await p.evaluate(() => {
      const q = (i, sel) => !!document.querySelector('#note-names-step-' + i + ' ' + sel);
      return [q(0, '[data-which-letter]'), q(1, '.try-box svg'), q(2, '.try-box svg'), q(3, '[data-who-lives]'), q(4, '.card'), q(5, '[data-word-keys]'), q(6, '[data-five-checks]')];
    });
    ok(parts.every(Boolean), 'T2 ' + lang + ' moving parts on steps 1-7: ' + JSON.stringify(parts));
    const scroll = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    ok(scroll <= 1, 'T3 ' + lang + ' no sideways scroll (' + scroll + ')');
    const txt = await p.evaluate(() => document.body.innerText);
    ok(!/count to two|둘 세기/.test(txt), 'T3b ' + lang + ' no count-to-two');
    ok(!/on the staff, in the next chapter|다음 챕터 오선보/.test(txt), 'T3c ' + lang + ' no staff line');
    ok(p._errs.length === 0, 'T4 ' + lang + ' no errors ' + p._errs.join('|').slice(0, 150));
    await p.context().close();
  }
  let p = await H.open({ path: '?drill=note-names', w: 390, h: 900 });
  await p.waitForTimeout(700);
  await p.evaluate(() => document.querySelector('#note-names-step-3 [data-who-lives]').scrollIntoView({ block: 'center' }));
  await p.click('#note-names-step-3 [data-who-lives] [data-key="2"]');
  await p.waitForTimeout(300);
  let msg = await p.$eval('#note-names-step-3 [data-who-lives]', e => e.innerText);
  ok(/Dog/.test(msg), 'T5 who-lives answers D = Dog: ' + msg.split('\n').slice(-1)[0]);
  // the skip page's chain: two chips, no staff
  const chips = await p.$$eval('#note-names-step-4 button.chip', els => els.map(e => e.textContent.trim()));
  ok(chips.includes('Step') && chips.includes('Skip') && !chips.includes('3rd') && !chips.includes('Staff'), 'T6 chain chips ' + chips.join(','));
  // the song
  await p.evaluate(() => document.querySelector('#note-names-step-5 [data-word-keys]').scrollIntoView({ block: 'center' }));
  for (const k of [11, 9, 7]) { await p.click('#note-names-step-5 [data-word-keys] [data-key="' + k + '"]'); await p.waitForTimeout(120); }
  msg = await p.$eval('#note-names-step-5 [data-word-keys]', e => e.innerText);
  ok(/You played BAG!/.test(msg), 'T7 spell it: B A G played');
  const txt5 = await p.evaluate(() => document.querySelector('#note-names-step-5').innerText + document.querySelector('#first-steps-step-3, body').innerText);
  ok(!/Hot Cross Buns/.test(txt5), 'T7b no Hot Cross Buns in the chapter');
  // drill levels
  const tab = await p.$('button:has-text("Drill")'); await tab.click(); await p.waitForTimeout(700);
  const lv = await p.$$eval('button.chip', els => els.map(e => e.textContent.trim()).filter(x => /^Level/.test(x)));
  ok(lv.length === 5, 'T8 five levels: ' + lv.join(','));
  await (await p.$('button:has-text("Level 5")')).click(); await p.waitForTimeout(900);
  let dt = await p.evaluate(() => document.body.innerText);
  ok(/Skip a letter, up or down/.test(dt) && /skip a letter (up|down)/.test(dt), 'T9 level 5 asks a skip');
  ok(!/3rd|5th|octave/i.test(dt.split('Skip a letter, up or down')[1] || ''), 'T9b no interval words in level 5');
  await (await p.$('button:has-text("Level 4")')).click(); await p.waitForTimeout(900);
  dt = await p.evaluate(() => document.body.innerText);
  ok(/next letter (up|down)/.test(dt), 'T10 level 4 next letter');
  ok(p._errs.length === 0, 'T11 drill no errors ' + p._errs.join('|').slice(0, 200));
  await p.context().close();
  // tones: the black-key level (Phase 437: level 5 of Tones & Semitones, four names of one sign)
  p = await H.open({ path: '?drill=tones&tab=drill&level=5', w: 390, h: 900 });
  await p.waitForTimeout(900);
  dt = await p.evaluate(() => document.body.innerText);
  ok(/Name the black keys/.test(dt) && /Name the black key/.test(dt), 'T12 tones level 5 names black keys');
  const ch4 = await p.$$eval('.choice-btn', els => els.length);
  ok(ch4 === 4, 'T12b 4 choices (' + ch4 + ')');
  ok(p._errs.length === 0, 'T13 tones no errors ' + p._errs.join('|').slice(0, 200));
  await p.context().close();
  // books
  for (const [kind, n] of [['lesson', 8], ['work', 7], ['teacher', 2], ['spread', 15]]) {   // Phase 415: the spread ends with the five checks facing the paper check-up
    p = await H.open({ path: '?book=' + kind + '&ch=note-names&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(1800);
    const info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
    ok(info.length === n && info.every(v => v <= 1), 'T14 ' + kind + ': ' + info.length + ' pages, overflow ' + JSON.stringify(info));
    ok(p._errs.length === 0, 'T15 ' + kind + ' no errors ' + p._errs.join('|').slice(0, 200));
    if (kind === 'lesson') { const strips = await p.$$eval('[data-lb-teacher]', els => els.length); ok(strips === 0, 'T16 no teacher strips in the printed book'); }
    await p.context().close();
  }
  p = await H.open({ path: '?drill=note-names&teacher=1', w: 390, h: 900, store: { pb_mode_v1: 'teacher' } });
  await p.waitForTimeout(900);
  const appStrips = await p.$$eval('[data-lb-teacher]', els => els.length);
  ok(appStrips === 0, 'T17 no teacher strips in the app teacher view (Phase 399) (' + appStrips + ')');
  ok(p._errs.length === 0, 'T18 teacher view no errors');
  await p.context().close();
  await H.close(); process.exit(process.exitCode || 0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
