// Build DQ: Knowing Your Pieces, Grade 8 and Diplomas. Usage: node dq793.js drills.t793.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t793.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=pieces-8', w: 420, h: 1600, dsf: 1, lang }); await sleep(1500);
    // the steps' pads
    // open every step (an accordion: one open at a time), noting its pad
    const pads = await p.evaluate(() => [...document.querySelectorAll('[data-pm]')].map(e => e.getAttribute('data-pm')));
    const nSteps = await p.locator('section > button').count();
    for (let k = 0; k < nSteps; k++) { await p.locator('section > button').nth(k).click(); await sleep(400); const pm = await p.evaluate(() => [...document.querySelectorAll('[data-pm]')].map(e => e.getAttribute('data-pm'))); pm.forEach(x => { if (!pads.includes(x)) pads.push(x); }); }
    const openStep = async (pad) => { for (let k = 0; k < nSteps; k++) { if (await p.locator('[data-pm="' + pad + '"]').count()) return; await p.locator('section > button').nth(k).click(); await sleep(300); } };
    await openStep('arc');
    say(['arc', 'title', 'conv', 'piano', 'viva'].every(x => pads.includes(x)) && !p._errs.length, lang, 'five pads on the chapter', JSON.stringify(pads), p._errs.slice(0, 1));
    // the arc: tapping a tension moves the climax
    const before = await p.locator('[data-pm="arc"]').innerText();
    await p.locator('[data-pa-ten="0:5"]').click(); await sleep(200);
    const after = await p.locator('[data-pm="arc"]').innerText();
    const cl = (after.split('\n').find(l => /^(The climax|클라이맥스):/.test(l)) || ''); say(before !== after && /: A \(/.test(cl), lang, 'the arc: the climax moves to A', JSON.stringify(cl.slice(0, 40)));
    const saved = await p.evaluate(() => { try { return JSON.parse(localStorage.getItem('pb_piece_arc')); } catch (e) { return null; } });
    say(saved && saved.ten && saved.ten[0] === 5, lang, 'the arc is saved', JSON.stringify(saved));
    // the title quiz
    await openStep('title'); await p.locator('[data-pm="title"] button', { hasText: lang === 'ko' ? '어떤 제목' : 'Which title' }).click(); await sleep(300);
    const nb = await p.locator('[data-pm="title"] .choice-btn').count();
    await p.locator('[data-pm="title"] .choice-btn').first().click(); await sleep(300);
    const tt = await p.locator('[data-pm="title"]').innerText();
    say(nb === 4 && /Yes|It is|맞아요|정답/.test(tt), lang, 'the title quiz: four choices, an answer', nb);
    // the conventions quiz
    await openStep('conv'); await p.locator('[data-pm="conv"] button', { hasText: lang === 'ko' ? '어느 시대' : 'Which period' }).click(); await sleep(300);
    const nc = await p.locator('[data-pm="conv"] .choice-btn').count();
    await p.locator('[data-pm="conv"] .choice-btn').first().click(); await sleep(300);
    say(nc === 4 && /Yes|That is|맞아요|정답/.test(await p.locator('[data-pm="conv"]').innerText()), lang, 'the conventions quiz', nc);
    // the piano quiz
    await openStep('piano'); await p.locator('[data-pm="piano"] button', { hasText: lang === 'ko' ? '어떤 피아노' : 'Which piano' }).click(); await sleep(300);
    const qm = await p.locator('[data-pm="piano"] [data-p8-stop]').allInnerTexts();
    await p.locator('[data-pm="piano"] [data-p8-stop="2"]').click(); await sleep(300);
    say(qm.every(x => /\?/.test(x)) && /Yes|It is|맞아요|정답/.test(await p.locator('[data-pm="piano"]').innerText()), lang, 'the piano quiz: hidden stops, an answer');
    // the viva cards
    await openStep('viva'); await p.locator('[data-viva-yes]').click(); await sleep(200); await p.locator('[data-viva-no]').click(); await sleep(200);
    const dots = await p.evaluate(() => [...document.querySelectorAll('[data-viva-dot]')].map(e => e.getAttribute('data-viva-dot')).sort().join(''));
    const vs = await p.evaluate(() => { try { return JSON.parse(localStorage.getItem('pb_p8_viva')); } catch (e) { return null; } });
    say(dots === '01' && vs && Object.values(vs)[0] && Object.keys(Object.values(vs)[0]).length === 2 && !p._errs.length, lang, 'viva cards: said and not yet, saved', dots, p._errs.slice(0, 1));
    await p.close();
    // the drill: every level generates and checks
    const d = await H.open({ path: '?drill=pieces-8&tab=drill&level=1', w: 420, h: 1200, dsf: 1, lang }); await sleep(1200);
    const gen = await d.evaluate(() => { const out = []; for (const L of P8_LEVELS) { let ok = 0; for (let i = 0; i < 40; i++) { const q = genP8Question(L, null); if (PIECES_8_DRILL.check(q, q.answer) && q.choices.includes(q.answer) && PIECES_8_DRILL.answerLabel(q)) ok++; } out.push(L.kind + ':' + ok); } return out; });
    say(gen.every(x => /:40$/.test(x)), lang, 'the drill generates', gen.join(' '));
    for (const lv of [1, 2, 3, 4]) {
      await d.evaluate((lv) => { location.href = location.pathname + '?drill=pieces-8&tab=drill&level=' + lv; }, lv); await sleep(1200);
      const n = await d.locator('.choice-btn').count(); if (n) { await d.locator('.choice-btn').first().click(); await sleep(400); }
      say(n >= 4 && !d._errs.length, lang, 'level ' + lv + ' renders and answers', n, d._errs.slice(0, 1));
    }
    await d.close();
    // the Home lessons and the 'Make your own'
    for (const id of ['p8-arc', 'p8-title', 'p8-conv', 'p8-piano', 'mk-viva']) {
      const h = await H.open({ path: '?tool=' + id, w: 420, h: 1200, dsf: 1, lang }); await sleep(1000);
      const txt = await h.evaluate(() => document.body.innerText.length);
      say(txt > 150 && !h._errs.length, lang, 'Home: ' + id, txt, h._errs.slice(0, 1));
      await h.close();
    }
  }
  // the house: the fourth room on the Grade 8 floor
  const g = await H.open({ path: '?view=path', w: 420, h: 1600 }); await sleep(1500);
  if (await g.locator('[data-house] [data-door]').count()) { await g.locator('[data-house] [data-door]').first().click(); await sleep(1500); }
  const room = await g.evaluate(() => { const r = document.querySelector('[data-house] [data-chapter="pieces-8"]'); return r ? (r.getAttribute('aria-label') || r.textContent.slice(0, 30)) : null; });
  say(room != null, 'the house has the room', room);
  await g.close();
  // print: the book, the workbook and the teacher copy render without overflow
  for (const [b, w] of [['lesson', 900], ['work', 900], ['teacher', 900]]) {
    const k = await H.open({ path: '?book=' + b + '&ch=pieces-8', w, h: 1300, dsf: 1 }); await sleep(1800);
    const pr = await k.evaluate(() => ({ n: document.querySelectorAll('.bk-page').length, over: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight) }));
    say(pr.n >= 2 && pr.over.every(x => x <= 2) && !k._errs.length, 'print ' + b + ': pages', pr.n, 'overflow', JSON.stringify(pr.over), k._errs.slice(0, 1));
    await k.close();
  }
  console.log('bad', bad); await H.close();
})();
