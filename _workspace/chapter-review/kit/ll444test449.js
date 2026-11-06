// Phase 429 checks (was 428: 'ladder' for 'rung', guides, the lid): chapter 6 applied -- the books, the app lesson (the book on screen) and its moving parts, the 7-level drill
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD);
  for (const [kind, want] of [['lesson', 7], ['work', 6], ['teacher', 2], ['spread', 13]]) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?book=' + kind + '&ch=ledger-lines&lang=' + lang, w: 900, h: 1200 });
    await p.waitForTimeout(2400);
    const r = await p.evaluate(() => ({ n: document.querySelectorAll('.bk-page').length, over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }), ask: document.querySelectorAll('[data-lb-ask]').length, text: document.body.innerText }));
    ok(r.n === want && r.over.every(x => x <= 0), 'B1 ' + kind + ' ' + lang + ': ' + r.n + ' pages (want ' + want + '), overflow ' + JSON.stringify(r.over));
    ok(r.ask === 0 && p._errs.length === 0, 'B2 ' + kind + ' ' + lang + ' no draft marks, no errors ' + p._errs.join('|').slice(0, 200));
    if (kind === 'lesson') ok(lang === 'en' ? /In this chapter/.test(r.text) : /이 챕터에서는/.test(r.text) && !/In this chapter/.test(r.text), 'B3 ' + lang + ' contents heading in its language');
    await p.context().close();
  }
  // every chapter's Korean book says 이 챕터에서는 (A8)
  for (const ch of ['posture-hands', 'first-steps', 'note-names', 'staff', 'whole-staff']) {
    const p = await H.open({ path: '?book=lesson&ch=' + ch + '&lang=ko', w: 900, h: 1200 });
    await p.waitForTimeout(1800);
    const tx = await p.evaluate(() => document.body.innerText);
    ok(/이 챕터에서는/.test(tx) && !/In this chapter/.test(tx), 'B4 ' + ch + ' ko contents heading');
    await p.context().close();
  }
  for (const [ch, kind] of [['staff', 'lesson'], ['staff', 'work'], ['staff', 'teacher'], ['whole-staff', 'lesson'], ['whole-staff', 'work'], ['whole-staff', 'teacher'], ['ledger-lines', 'lesson'], ['ledger-lines', 'work'], ['ledger-lines', 'teacher']]) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + ch + '&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(1800);
    const r = await p.evaluate(() => ({ t: document.body.innerText + ' ' + [...document.querySelectorAll('[aria-label]')].map(e => e.getAttribute('aria-label')).join(' '), dots: document.querySelectorAll('line[stroke-dasharray="2.2 3"]').length }));
    ok(!/\brungs?\b/i.test(r.t), 'W1 ' + ch + ' ' + kind + ': no "rung" (' + ((r.t.match(/.{20}\brungs?\b.{10}/i) || [''])[0]) + ')');
    if (ch === 'ledger-lines' && kind === 'work') {
      ok(r.dots >= 55, 'W2 dotted guide lines to draw on: ' + r.dots);
      ok(/The missing notes/.test(r.t) && !/e\.g\.\s*\n?\s*1\s*\n?\s*2\s*\n?\s*3\s*\n?\s*F/.test(r.t), 'W3 no numbers over the missing notes');
      ok(/a lid on top/.test(r.t), 'W4 neat or not checks the lid');
    }
    await p.context().close();
  }
  // the app lesson: the book on screen -- six steps named like the book pages, the moving parts work
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=ledger-lines', w: 390, h: 1200, lang });
    await p.waitForTimeout(2200);
    const r = await p.evaluate(() => ({ text: document.body.innerText, sw: document.documentElement.scrollWidth - document.documentElement.clientWidth }));
    const want = lang === 'en' ? ['Clara\'s ladder is a ledger line', 'Up into the sky', 'Down into the sea', 'Between the lands', 'Five Cs', 'My five checks'] : ['클라라의 발판은 덧줄', '하늘로 올라가기', '바다로 내려가기', '두 나라 사이', '다섯 C', '나의 다섯 가지 확인'];
    ok(want.every(w => r.text.includes(w)), 'L1 ' + lang + ' steps follow the book: ' + want.filter(w => !r.text.includes(w)).join(','));
    ok(!/treble staff|bass staff|A · C · E|C A F/.test(r.text), 'L2 ' + lang + ' no treble/bass staff, no lists (middle C is its name from Phase 449)');
    ok(r.sw <= 0, 'L3 ' + lang + ' no sideways scroll (' + r.sw + ')');
    ok(p._errs.length === 0, 'L4 ' + lang + ' no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  // the moving parts, through the toolbox pages
  const tool = async (id) => { const p = await H.open({ path: '?tool=' + id, w: 390, h: 1100 }); await p.waitForTimeout(1500); return p; };
  { // draw the rungs: A5 needs one rung -- 0 is a gap, 2 is one too many, 1 is neat
    const p = await H.open({ path: '?drill=ledger-lines', w: 390, h: 1200 }); await p.waitForTimeout(2000);
    const box = await p.$('.try-box:has-text("Draw the ladders")');
    ok(!!box, 'M1 the rung tool is on step 1');
    if (box) {
      const click = async (txt) => { const b = await box.$('button:has-text("' + txt + '")'); if (b) { await b.click(); await p.waitForTimeout(250); } return !!b; };
      await click('Check'); const t0 = await box.innerText();
      await click('+ ladder'); await click('+ ladder'); await click('Check'); const t2 = await box.innerText();
      await click('− ladder'); await click('Check'); const t1 = await box.innerText();
      const nextNote = async (k) => { await click('Next note'); for (let i = 0; i < k; i++) await click('+ ladder'); await click('Check'); return box.innerText(); };
      await nextNote(2); await nextNote(1); const tl = await nextNote(1);
      ok(/That is a lid ?[:·,.] a note in a space gets no line on top of it/.test(tl.replace(/\u00a0-\u2060-/g, ' --')), 'M2b G over Queensland with one ladder is a lid');
      ok(/gap/.test(t0) && /too many/.test(t2) && /Neat! 1 ladder: A sits on ladder 1 over Queensland/.test(t1), 'M2 gap, one too many, neat: ' + [t0, t2, t1].map(x => x.split('\n').find(l => /gap|many|Neat/.test(l))).join(' / '));
    }
    // the sky ladder: F, then six steps up to E on rung 3
    const sky = await p.$('.try-box:has-text("Climb up into the sky")');
    ok(!!sky, 'M3 the sky ladder is on step 2');
    if (sky) { for (let i = 0; i < 4; i++) { const b = await sky.$('button:has-text("Step up")'); await b.click(); await p.waitForTimeout(150); } const tx = await sky.innerText(); ok(/C ?[:·,.] on ladder 2 over Queensland · high C/.test(tx.replace(/\n/g, ' ')), 'M4 four steps up from F is high C on rung 2: ' + tx.split('\n').filter(l => /rung|high/.test(l)).join(' | ')); }
    const sea = await p.$('.try-box:has-text("Climb down into the sea")');
    ok(!!sea, 'M5 the sea ladder is on step 3');
    if (sea) { for (let i = 0; i < 6; i++) { const b = await sea.$('button:has-text("Step down")'); await b.click(); await p.waitForTimeout(150); } const tx = await sea.innerText(); ok(/A ?[:·,.] on ladder 3 under Kingsland/.test(tx.replace(/\n/g, ' ')), 'M6 six steps down from G is A on rung 3: ' + tx.split('\n').filter(l => /rung/.test(l)).join(' | ')); }
    const tw = await p.$('.try-box:has-text("The same key, two ways")');
    ok(!!tw, 'M7 the twins are on step 4');
    if (tw) { const tx = (await tw.innerText()).replace(/\n/g, ' '); ok(/on ladder 2 under Queensland/.test(tx) && /Kingsland's top line/.test(tx), 'M8 A3 shown both ways'); }
    const cs = await p.$('.try-box:has-text("C hop")');
    ok(!!cs, 'M9 the five Cs are on step 5');
    if (cs) {
      const b = await cs.$('button:has-text("High C")'); await b.click(); await p.waitForTimeout(200);
      ok(/High C ?[:·,.] on ladder 2 over Queensland/.test((await cs.innerText()).replace(/\n/g, ' ').replace(/\u00a0-\u2060-/g, ' --')), 'M10 high C named and placed');
      const h = await cs.$('button:has-text("C hop")'); await h.click(); await p.waitForTimeout(200);
      const L = await cs.$('.choice-btn:has-text("B")'); await L.click(); await p.waitForTimeout(300);
      ok(/From high C, a step down: B/.test(await cs.innerText()), 'M11 the hop explains itself');
    }
    ok(p._errs.length === 0, 'M12 no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  // the drill: seven levels, each renders a question; the answers stay on the book's notes
  for (let lv = 1; lv <= 7; lv++) {
    const p = await H.open({ path: '?drill=ledger-lines&tab=drill&level=' + lv, w: 390, h: 1000 });
    await p.waitForTimeout(1600);
    const startBtn = await p.$('button:has-text("Start")'); if (startBtn) { await startBtn.click(); await p.waitForTimeout(700); }
    const r = await p.evaluate(() => ({ t: document.body.innerText, btns: [...document.querySelectorAll('.choice-btn')].map(b => b.innerText.trim()), keys: document.querySelectorAll('svg rect').length }));
    const lab = ['One ladder: Queensland', 'One ladder: Kingsland', 'Two ladders, both lands', 'High C and low C', 'Between the lands', 'Up to three ladders, fast', 'Find it on the keys'][lv - 1];
    ok(r.t.includes(lab), 'D' + lv + ' level label shown: ' + lab);
    if (lv <= 6) {
      ok(r.btns.length === 7, 'D' + lv + 'b seven letter buttons (' + r.btns.length + ')');
      const d = await p.evaluate(() => { const e = document.querySelector('ellipse[data-d]'); return e ? +e.getAttribute('data-d') : null; });
      const right = 'CDEFGAB'[((d % 7) + 7) % 7], wrong = right === 'C' ? 'D' : 'C';
      const b = await p.$('.choice-btn:text-is("' + wrong + '")'); if (b) { await b.click(); await p.waitForTimeout(600); }
      const after = await p.evaluate(() => document.body.innerText);
      ok(/(ladder \d (over|under) (Queensland|Kingsland)|just (over|under)|top line|bottom line)/.test(after), 'D' + lv + 'c the answer says where in the lands\' words');
    }
    ok(p._errs.length === 0, 'D' + lv + 'd no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  await H.close();
})();
