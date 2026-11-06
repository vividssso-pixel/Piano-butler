const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=note-values&tab=drill&level=1', w: 900, h: 900, lang }); await p.waitForTimeout(1500);
    const r = await p.evaluate(() => {
      const out = []; const D = NOTEVAL_DRILL;
      for (const lv of D.levels) { let prev = null, bad = 0, keys = new Set(), msg = '';
        for (let i = 0; i < 400; i++) { const q = D.generate(lv, prev); prev = q; keys.add(q.key);
          let ans = q.answer;
          if (q.kind === 'tap' || q.kind === 'tapr') ans = { ok: true };
          else if (!q.choices.some(c => c === q.answer || (typeof c === 'number' && Math.abs(c - q.answer) < 1e-9))) { bad++; msg = 'answer not in choices ' + JSON.stringify(q.choices) + ' ' + q.answer; }
          if (!D.check(q, ans)) { bad++; msg = 'check false ' + q.kind; }
          if (q.choices && new Set(q.choices.map(String)).size !== q.choices.length) { bad++; msg = 'dup choices ' + q.choices; }
          const lab = D.answerLabel(q); if (!lab || /undefined|NaN/.test(lab)) { bad++; msg = 'label ' + lab; }
          if (q.choices && q.choices.some(c => typeof c === 'number' && D.check(q, c) && Math.abs(c - q.answer) > 1e-9)) { bad++; msg = 'two right'; }
        }
        out.push(lv.n + ' ' + lv.kind + ' bad ' + bad + ' distinct ' + keys.size + (msg ? ' :: ' + msg : '') + ' e.g. ' + D.answerLabel(D.generate(lv, null)));
      }
      return out;
    });
    console.log(lang + '\n' + r.join('\n'), p._errs.join('|'));
    await p.context().close();
  }
  await H.close();
})();
