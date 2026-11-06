// Phase 419 checks: chapter 5 applied -- the books, the app lesson (the book on screen), the 7-level drill
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD);
  for (const [kind, want] of [['lesson', 7], ['work', 6], ['teacher', 2], ['spread', 13]]) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=whole-staff&lang=' + lang, w: 900, h: 1200 });
    await p.waitForTimeout(2400);
    const r = await p.evaluate(() => ({ n: document.querySelectorAll('.bk-page').length, over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }), ask: document.querySelectorAll('[data-lb-ask]').length }));
    ok(r.n === want && r.over.every(x => x <= 0), 'B1 ' + kind + ' ' + lang + ': ' + r.n + ' pages (want ' + want + '), overflow ' + JSON.stringify(r.over));
    ok(r.ask === 0 && p._errs.length === 0, 'B2 ' + kind + ' ' + lang + ' no draft marks, no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  // the app lesson: the book on screen -- six steps named like the book pages, moving parts present
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=whole-staff', w: 390, h: 1200, lang });
    await p.waitForTimeout(2200);
    const r = await p.evaluate(() => ({ text: document.body.innerText, steps: [...document.querySelectorAll('[data-step], .step-title, h3')].length, sw: document.documentElement.scrollWidth - document.documentElement.clientWidth }));
    const want = lang === 'en' ? ['Clef check first', 'Treble clef', 'Bass clef', 'Fold at Clara', 'Five landmarks', 'My five checks'] : ['음자리표 확인 먼저', '높은음자리표', '낮은음자리표', '클라라의 발판에서 접기', '다섯 랜드마크', '나의 다섯 가지 확인'];
    ok(want.every(w => r.text.includes(w)), 'L1 ' + lang + ' steps follow the book: ' + want.filter(w => !r.text.includes(w)).join(','));
    ok(!/High C|Low C|ledger line|Treble G|Bass F/.test(r.text), 'L2 ' + lang + ' no High/Low C, no ledger-line word, no Treble G/Bass F');
    ok(r.sw <= 0, 'L3 ' + lang + ' no sideways scroll (' + r.sw + ')');
    ok(p._errs.length === 0, 'L4 ' + lang + ' no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  // the drill: seven levels, each renders a question
  for (let lv = 1; lv <= 7; lv++) {
    const p = await H.open({ path: '?drill=whole-staff&tab=drill&level=' + lv, w: 390, h: 1000 });
    await p.waitForTimeout(1600);
    const startBtn = await p.$('button:has-text("Start")'); if (startBtn) { await startBtn.click(); await p.waitForTimeout(700); }
    const r = await p.evaluate(() => ({ t: document.body.innerText, svg: document.querySelectorAll('svg').length, btns: [...document.querySelectorAll('.choice-btn')].map(b => b.innerText.trim()) }));
    const lab = ['Clef check: treble or bass?', 'Treble clef: every line and space', 'Bass clef: every line and space', 'The five landmarks', 'Landmark hop', 'Both clefs, fast', 'Find it on the keys'][lv - 1];
    ok(r.t.includes(lab), 'D' + lv + ' level label shown: ' + lab);
    if (lv === 1) {
      ok(r.btns.join('|') === 'Treble clef|Bass clef', 'D1b crown buttons: ' + r.btns.join('|'));
      const b = await p.$('.choice-btn'); if (b) { await b.click(); await p.waitForTimeout(500); }
      const after = await p.evaluate(() => document.body.innerText);
      ok(/This note is/.test(after), 'D1c the answer names the land and the note');
    }
    if (lv >= 2 && lv <= 6) ok(r.btns.length === 7, 'D' + lv + 'b seven letter buttons (' + r.btns.length + ')');
    ok(p._errs.length === 0, 'D' + lv + 'c no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  await H.close();
})();
