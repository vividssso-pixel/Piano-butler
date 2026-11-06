// QA A: every drill, every level: 400 questions -- the answer is among the choices, choices are unique, check() accepts
// the answer and refuses the other choices, the answer label renders, nothing is undefined/NaN in the question text.
const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t447.html');
  const p = await H.open({ path: '?lang=en', w: 1024, h: 900 }); await p.waitForTimeout(1200);
  const r = await p.evaluate(() => {
    const out = [];
    const seen = (v) => { if (v && typeof v === 'object' && v.key !== undefined) return 'K:' + v.key; try { return JSON.stringify(v); } catch (e) { return String(v); } };
    DRILLS.forEach(D => {
      const C = D.concept || D; if (!C || !C.levels || !C.generate) { out.push([D.id, 'no levels/generate']); return; }
      C.levels.forEach(L => {
        const bad = []; let prev = null, n = 0, kinds = new Set();
        for (let k = 0; k < 400; k++) {
          let q; try { q = C.generate(L, prev); } catch (e) { bad.push('generate throws: ' + e.message); break; }
          prev = q; n++; if (q && q.kind) kinds.add(q.kind);
          if (!q) { bad.push('null question'); break; }
          const txt = seen(q);
          if (/undefined|NaN|null,"choices"/.test(txt) && !/"answer":null/.test(txt)) { if (bad.length < 3) bad.push('suspicious: ' + txt.slice(0, 160)); }
          if (Array.isArray(q.choices)) {
            const keys = q.choices.map(seen);
            if (new Set(keys).size !== keys.length) bad.push('duplicate choices ' + keys.join('|').slice(0, 120));
            const ansKey = q.kind === 'fill' ? seen(q.missing) : (typeof q.answer === 'string' && q.choices[0] && q.choices[0].key !== undefined ? 'K:' + q.answer : seen(q.answer));
            if (q.answer !== undefined && q.kind !== 'build' && !keys.includes(ansKey)) bad.push('answer not in choices: ' + seen(q.answer) + ' / ' + keys.join('|').slice(0, 120));
            const ansObj = q.kind === 'fill' ? q.missing : (q.choices.find(c => seen(c) === ansKey) !== undefined && q.choices[0] && q.choices[0].key !== undefined ? q.answer : q.answer);
            if (C.check && q.answer !== undefined && q.kind !== 'build') {
              try { if (!C.check(q, ansObj)) bad.push('check rejects answer ' + seen(q.answer)); } catch (e) { bad.push('check throws ' + e.message); }
              q.choices.forEach(c => { const cv = (c && c.key !== undefined && q.kind !== 'fill') ? c.key : c; try { if (seen(c) !== ansKey && C.check(q, cv)) bad.push('check accepts wrong ' + seen(c) + ' (answer ' + seen(q.answer) + ')'); } catch (e) {} });
            }
          } else if (C.check && q.answer !== undefined && q.answer !== null) {
            try { if (!C.check(q, q.answer)) bad.push('check rejects answer ' + seen(q.answer)); } catch (e) { bad.push('check throws ' + e.message); }
          }
          if (C.answerLabel) { try { const l = C.answerLabel(q); if (l == null || /undefined|NaN/.test(String(l))) bad.push('answerLabel ' + l); } catch (e) { bad.push('answerLabel throws ' + e.message); } }
          if (bad.length > 6) break;
        }
        out.push([D.id, 'L' + L.n + ' ' + (L.label || '').slice(0, 30), n, [...kinds].join(','), [...new Set(bad)].slice(0, 4)]);
      });
    });
    return out;
  });
  r.forEach(x => { if (x.length === 2 || (x[4] && x[4].length)) console.log('PROBLEM', JSON.stringify(x)); });
  console.log(r.length + ' levels checked; problems: ' + r.filter(x => x.length === 2 || (x[4] && x[4].length)).length);
  await H.close();
})();
