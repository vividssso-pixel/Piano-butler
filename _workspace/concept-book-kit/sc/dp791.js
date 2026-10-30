// Build DP: calls 34 to 37. Usage: node dp791.js drills.t791.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t791.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  // 34: the lit room: the house's 'here' room carries the glow
  const h = await H.open({ path: '?view=path', w: 420, h: 1600 }); await sleep(1500);
  const glow = await h.evaluate(() => { const r = document.querySelector('[data-house] [data-here="1"]'); const svg = document.querySelector('[data-house] svg, [data-house]'); return { here: !!r, glow: svg ? (svg.innerHTML.match(/url\(#thglow\)/g) || []).length : -1, grad: !!document.querySelector('#thglow') }; });
  say(glow.glow === 1 && glow.grad, '34 the lit room: one glow, on the room you are in', JSON.stringify(glow));
  await h.close();
  // 35 and 36: the placement: 'I don't know' counts as a miss; a one-skill miss still climbs and marks rooms to review
  const p = await H.open({ path: '?view=path&start=1', w: 420, h: 1600 }); await sleep(1200);
  await p.locator('[data-testid="place-start"]').click(); await sleep(900);
  let climbedWithReview = false, dunnoSeen = false, rounds = 0;
  const phases = [];
  for (let round = 0; round < 60; round++) {
    const phase = await p.locator('[data-testid="placement"]').getAttribute('data-phase'); phases.push(phase);
    if (phase === 'done') break;
    if (phase === 'climb' || phase === 'lower' || phase === 'turn') { const txt = await p.locator('[data-testid="place-step"]').innerText(); if (/review|다시/.test(txt)) climbedWithReview = true; await p.locator('[data-testid="place-next"]').click(); await sleep(700); continue; }
    if (phase !== 'run') break;
    rounds++;
    // this floor: miss the first two questions of one skill (the first question's skill) by 'I don't know' and a wrong answer; the rest right
    let target = null, missed = 0;
    for (let q = 0; q < 6; q++) {
      const info = await p.evaluate(() => { const k = document.querySelector('[data-testid="check-run"]'); if (!k) return null; const kick = k.previousElementSibling && k.previousElementSibling.innerText || ''; const m = (k.innerText.match(/^\s*(\d+)\s·/m) || [])[1]; const id = m ? pathIds().find(x => bkChapterNo(x) === +m) : null; return { id, skill: id ? PLACE_SKILL(id) : null, n: k.getAttribute('data-n') }; });
      if (!info) break;
      if (target == null) target = info.skill;
      if (info.skill === target && missed < 2) { if (missed === 0 && await p.locator('[data-testid="check-dunno"]').count()) { await p.locator('[data-testid="check-dunno"]').click(); dunnoSeen = true; } else await p.evaluate(() => window.__pbCheckForce(false)); missed++; }
      else await p.evaluate(() => window.__pbCheckForce(true));
      await sleep(300);
      const nx = p.locator('[data-testid="check-run"] button.primary-btn'); if (await nx.count()) { await nx.click(); await sleep(500); }
    }
    await sleep(600);
  }
  const phase = await p.locator('[data-testid="placement"]').getAttribute('data-phase');
  const res = phase === 'done' ? await p.locator('[data-testid="place-result"]').innerText() : '';
  console.log('      phases', phases.join(' '));
  say(dunnoSeen, "35 'I don't know' button used in the placement");
  say(phase === 'done' && /know|모르겠/.test(res), '35 the result counts them', JSON.stringify(res.match(/.*(know|모르겠).*/) || '')[0]);
  say(climbedWithReview && (await p.locator('[data-testid="place-review"]').count()) === 1, '36 a one-skill miss climbed with rooms to review', 'rounds', rounds, 'review block', await p.locator('[data-testid="place-review"]').count());
  const saved = await p.evaluate(() => { try { return JSON.parse(localStorage.getItem('pb_place_v1')); } catch (e) { return null; } });
  say(saved && Array.isArray(saved.review) && saved.review.length > 0, '36 the placement saves the rooms to review', JSON.stringify(saved));
  await p.evaluate(() => { location.href = location.pathname + '?view=path'; }); await sleep(2500);
  const tags = await p.evaluate(() => (document.querySelector('[data-house]').innerHTML.match(/>(review|다시)</g) || []).length);
  say(tags > 0, '36 the house marks the rooms to review', tags);
  await p.close();
  // 37: the finder: one keyboard for both hands, one tap one note; the Quick line on the Home; the card in a scales room
  const f = await H.open({ path: '?tool=scale-finder&key=D', w: 420, h: 1600 }); await sleep(1200);
  const kb = await f.evaluate(() => { const k = document.querySelector('[data-sf-hands]'); if (!k) return null; const txt = k.innerText; return { one: document.querySelectorAll('[data-sf-hands] svg').length, names: (k.querySelector('svg').textContent.match(/F♯|C♯|G♭|D♭/g) || []).join(' '), txt: txt.slice(0, 80) }; });
  say(kb && kb.one === 1 && /F♯/.test(kb.names) && !/G♭|D♭/.test(kb.names), '37 one keyboard, black keys spelt for D major', JSON.stringify(kb));
  await f.locator('[data-sf-step]').click(); await sleep(300); await f.locator('[data-sf-step]').click(); await sleep(300);
  const lit = await f.evaluate(() => [...document.querySelectorAll('[data-sf-hands] svg rect')].filter(r => r.getAttribute('fill') === '#fbe3da' || r.getAttribute('fill') === '#e4572e').length);
  say(lit === 1 && !f._errs.length, '37 hands together: one tap, one note lit', lit, f._errs.slice(0, 1));
  await f.close();
  const g = await H.open({ path: '?teacher=1&view=home', w: 420, h: 1200 }); await sleep(900);
  say((await g.locator('[data-testid="home-quick"] [data-quick="scale-finder"]').count()) === 1, '37 the Quick line on the Home');
  await g.locator('[data-quick="scale-finder"]').click(); await sleep(900);
  say(/tool=scale-finder/.test(await g.evaluate(() => location.search)), '37 Quick opens the finder', await g.evaluate(() => location.search));
  await g.close();
  const r = await H.open({ path: '?drill=scale-play', w: 420, h: 2400 }); await sleep(1200);
  const more = await r.evaluate(() => { const a = [...document.querySelectorAll('a.chip[href*="tool=scale-finder"]')]; return { n: a.length, title: (document.body.innerText.match(/More to play with|더 놀아 보기/) || [''])[0], old: /More in the toolbox|툴박스에 더/.test(document.body.innerText) }; });
  say(more.n >= 1 && more.title && !more.old, '37 the finder card in Playing Scales; no Toolbox wording', JSON.stringify(more));
  await r.close();
  console.log('bad', bad); await H.close();
})();
