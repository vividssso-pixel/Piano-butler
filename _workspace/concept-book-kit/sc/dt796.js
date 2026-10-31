// Builds DS and DT: the limiter, the stems, and The Piano's Story, Grade 8 and Diplomas. Usage: node dt796.js drills.t796.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t796.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  // DS: every sound goes out through one limiter
  const a = await H.open({ path: '?view=home', w: 420, h: 900 });
  const lim = await a.evaluate(async () => { const ctx = new OfflineAudioContext(1, 44100, 44100); const o = pbOut(ctx); return { node: o.constructor.name, same: pbOut(ctx) === o, th: o.threshold.value }; });
  say(lim.node === 'DynamicsCompressorNode' && lim.same, 'DS one limiter per context', JSON.stringify(lim));
  await a.close();
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=piano-story-8', w: 420, h: 1600, dsf: 1, lang }); await sleep(1500);
    const nSteps = await p.locator('section > button').count();
    const pads = []; for (let k = 0; k < nSteps; k++) { if (k) { await p.locator('section > button').nth(k).click(); await sleep(400); } (await p.evaluate(() => [...document.querySelectorAll('[data-pm]')].map(e => e.getAttribute('data-pm')))).forEach(x => { if (!pads.includes(x)) pads.push(x); }); }
    say(['actions', 'compass', 'pedals8', 'modern', 'mine'].every(x => pads.includes(x)) && !p._errs.length, lang, 'five pads', JSON.stringify(pads), p._errs.slice(0, 1));
    const open = async (pad) => { for (let k = 0; k < nSteps; k++) { if (await p.locator('[data-pm="' + pad + '"]').count()) return; await p.locator('section > button').nth(k).click(); await sleep(300); } };
    // step 1: press the Viennese key, then the quiz
    await open('actions'); await p.locator('[data-ps8-press="vienna"]').click(); await sleep(300);
    await p.locator('[data-pm="actions"] button', { hasText: lang === 'ko' ? '빈? 런던?' : 'Vienna or London?' }).click(); await sleep(200);
    await p.locator('[data-ps8-act="vienna"]').click(); await sleep(200);
    say(/Yes|It is|맞아요|정답/.test(await p.locator('[data-pm="actions"]').innerText()), lang, 'actions: press and quiz');
    // step 2: Graf's compass is 78 keys; the quiz answers
    await open('compass'); await p.locator('[data-ps8-comp="graf"]').click(); await sleep(200);
    const ct = await p.locator('[data-pm="compass"]').innerText();
    await p.locator('[data-pm="compass"] button', { hasText: lang === 'ko' ? '칠 수 있었을까' : 'Could it play' }).click(); await sleep(200);
    await p.locator('[data-ps8-first]').first().click(); await sleep(200);
    say(/C1–F7/.test(ct) && /78/.test(ct) && /Yes|It is|맞아요|정답/.test(await p.locator('[data-pm="compass"]').innerText()), lang, 'compass: Graf C1–F7, 78 keys; the quiz');
    // step 3: the slider to Mozart's Walter shows knee levers; una corda's card
    await open('pedals8'); await p.locator('[data-ps8-year]').fill('4'); await sleep(200);
    const pt = await p.locator('[data-pm="pedals8"]').innerText();
    await p.locator('[data-ps8-mark="una"]').click(); await sleep(200);
    const ut = await p.locator('[data-pm="pedals8"]').innerText();
    say(/Walter|발터/.test(pt) && /two strings|두 줄/.test(ut), lang, 'pedals: the Walter stop and una corda today');
    // step 4: build: all five inventions, Chopin and Liszt appear; the repeat toy counts
    await open('modern'); for (const id of ['esc', 'iron', 'felt', 'cross', 'k88']) { await p.locator('[data-ps8-inv="' + id + '"]').click(); await sleep(100); }
    const mt = await p.locator('[data-pm="modern"]').innerText();
    const tap = p.locator('[data-ps8-repeat] button.primary-btn'); for (let i = 0; i < 6; i++) { await tap.click(); await sleep(40); }
    const rt = await p.locator('[data-ps8-repeat]').innerText();
    say(/Pleyel|플레옐/.test(mt) && /6 (taps|번)|6번/.test(rt), lang, 'modern: all five, Chopin and Liszt; the repeat toy', JSON.stringify(rt.split('\n').find(l => /tap|번/.test(l))));
    // step 5: choose Chopin, say two, saved
    await open('mine'); await p.locator('[data-ps8-mine="chopin"]').click(); await p.locator('[data-ps8-ask="range"]').click(); await p.locator('[data-ps8-ask="pedal"]').click(); await sleep(200);
    const sv = await p.evaluate(() => { try { return JSON.parse(localStorage.getItem('pb_ps8_mine')); } catch (e) { return null; } });
    say(sv && sv.id === 'chopin' && sv.said && sv.said.chopin && sv.said.chopin.range && sv.said.chopin.pedal && !p._errs.length, lang, 'mine: saved', JSON.stringify(sv), p._errs.slice(0, 1));
    await p.close();
    // the drill
    const d = await H.open({ path: '?drill=piano-story-8&tab=drill&level=1', w: 420, h: 1200, dsf: 1, lang }); await sleep(1200);
    const gen = await d.evaluate(() => PS8_LEVELS.map(L => { let ok = 0; for (let i = 0; i < 40; i++) { const q = genPs8Question(L, null); if (PIANO_STORY_8_DRILL.check(q, q.answer) && q.choices.includes(q.answer) && PIANO_STORY_8_DRILL.answerLabel(q)) ok++; } return L.kind + ':' + ok; }));
    say(gen.every(x => /:40$/.test(x)), lang, 'the drill generates', gen.join(' '));
    for (const lv of [1, 2, 3, 4]) { await d.evaluate((lv) => { location.href = location.pathname + '?drill=piano-story-8&tab=drill&level=' + lv; }, lv); await sleep(1200);
      const n = await d.locator('.choice-btn').count(); if (n) { await d.locator('.choice-btn').first().click(); await sleep(400); }
      say(n >= 2 && !d._errs.length, lang, 'level ' + lv, n, d._errs.slice(0, 1)); }
    await d.close();
    for (const id of ['ps8-act', 'ps8-comp', 'ps8-ped', 'ps8-modern', 'ps8-mine']) { const h = await H.open({ path: '?tool=' + id, w: 420, h: 1200, dsf: 1, lang }); await sleep(1000);
      const n = await h.evaluate(() => document.body.innerText.length); say(n > 150 && !h._errs.length, lang, 'Home: ' + id, n, h._errs.slice(0, 1)); await h.close(); }
  }
  // the house: the attic has the room
  const g = await H.open({ path: '?view=path', w: 420, h: 1600 }); await sleep(1500);
  const doors = await g.locator('[data-house] [data-door]').count(); for (let i = 0; i < doors; i++) { if (await g.locator('[data-house] [data-chapter="piano-story-8"]').count()) break; await g.locator('[data-house] [data-door]').nth(i).click(); await sleep(800); }
  const room = await g.evaluate(() => { const r = document.querySelector('[data-house] [data-chapter="piano-story-8"]'); return r ? (r.getAttribute('aria-label') || r.textContent.slice(0, 30)) : null; });
  say(room != null && !g._errs.length, 'the house has the room', room); await g.close();
  for (const [b, w] of [['lesson', 900], ['work', 900], ['teacher', 900]]) { const k = await H.open({ path: '?book=' + b + '&ch=piano-story-8', w, h: 1300, dsf: 1 }); await sleep(1800);
    const pr = await k.evaluate(() => ({ n: document.querySelectorAll('.bk-page').length, over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
    say(pr.n >= 2 && pr.over.every(x => x <= 2) && !k._errs.length, 'print ' + b, pr.n, JSON.stringify(pr.over), k._errs.slice(0, 1)); await k.close(); }
  console.log('bad', bad); await H.close();
})();
