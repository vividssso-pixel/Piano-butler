// Build CV online checks: the stopwatch on 'Beat your time', the house plaques and next-on-path by grade,
// the ears' middle C icon, the Home's fold texts. Usage: node cv771.js drills.t771.html
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/bk/';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t771.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  // 1. the stopwatch: open steps until a time challenge shows; start, wait, stop; the best stays after a reload
  for (const lang of ['en', 'ko']) {
    const store = {};
    let p = await H.open({ path: '?drill=first-steps', w: 390, h: 1600, lang, store }); await sleep(600);
    const heads = p.locator('section > button:has(span)');
    const n = await heads.count(); let found = !!(await p.locator('.lb-challenge[data-kind="time"]').count());
    for (let i = 0; i < n && !found; i++) { await heads.nth(i).click(); await sleep(250); if (await p.locator('.lb-challenge[data-kind="time"]').count()) found = true; }
    say(found, lang, 'a time challenge online');
    if (!found) { await p.close(); continue; }
    const btn = p.locator('[data-testid="lb-timer"]').first();
    const lbl0 = await btn.innerText(); await btn.click(); await sleep(1300); const lbl1 = await btn.innerText(); await btn.click(); await sleep(200);
    const last = await p.locator('[data-testid="lb-timer-last"]').first().innerText().catch(() => '');
    const saved = await p.evaluate(() => localStorage.getItem('pb_beat_v1'));
    say(/Start|시작/.test(lbl0) && /■ 1\.\d s/.test(lbl1) && /1\.\d s/.test(last) && /"beat\d+":1\.\d/.test(saved || ''), lang, 'timer', JSON.stringify([lbl0, lbl1, last, saved]));
    await p.locator('.lb-challenge[data-kind="time"]').first().screenshot({ path: SH + 'cv-timer-' + lang + '.png' });
    // reload: the best is shown
    await p.reload(); await sleep(700);
    for (let i = 0; i < n && !(await p.locator('.lb-challenge[data-kind="time"]').count()); i++) { await p.locator('section > button:has(span)').nth(i).click(); await sleep(200); if (await p.locator('.lb-challenge[data-kind="time"]').count()) break; }
    const best = await p.locator('[data-testid="lb-timer-best"]').first().innerText().catch(() => '');
    say(/1\.\d s/.test(best), lang, 'best after reload', best, p._errs.slice(0, 1));
    await p.close();
  }
  // 2. the map: plaques by grade only; no "Floor 1" / "1층" anywhere on the path view
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?view=path', w: 390, h: 1400, lang }); await sleep(900);
    const txt = await p.evaluate(() => document.body.innerText + ' ' + [...document.querySelectorAll('svg text')].map(x => x.textContent).join(' '));
    const hasFloorNo = /FLOOR \d|Floor \d|\d층 ·|floor \d/.test(txt);
    say(!hasFloorNo && /BEGINNER/.test(txt), lang, 'map: grades only', (txt.match(/(FLOOR|Floor|floor) ?\d|\d층/g) || []).slice(0, 4));
    await p.screenshot({ path: SH + 'cv-map-' + lang + '.png' });
    await p.close();
  }
  // 3. floorName and the checkpoint names
  { const p = await H.open({ path: '?', w: 390, h: 900 }); await sleep(500);
    const r = await p.evaluate(() => [floorName(0), floorName(0, true), floorName(2), chkFloorName(checkFloors()[0]), checkFloors().map(chkFloorName).slice(0, 3).join(' | ')]);
    say(r[0] === 'Beginner' && r[1] === 'BEGINNER' && r[2] === 'Grade 1', 'floorName', JSON.stringify(r)); await p.close(); }
  // 4. the ears: turtle, middle C, bird online; no Clara anywhere in the ear-prep room
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=ear-prep', w: 390, h: 1600, lang }); await sleep(600);
    const txt = await p.evaluate(() => document.body.innerText);
    say(!/Clara|클라라/.test(txt) && /middle C|가운데 도/.test(txt), lang, 'ear-prep: no Clara', p._errs.slice(0, 1));
    await p.close();
  }
  // 5. rooms after the key names: no Clara (staff, whole staff, ledger lines, tones, hand positions)
  for (const id of ['staff', 'whole-staff', 'ledger-lines', 'tones', 'hand-positions', 'scale-play']) for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=' + id, w: 390, h: 1600, lang }); await sleep(500);
    const heads = p.locator('section > button:has(span)'); const n = await heads.count(); let txt = '';
    for (let i = 0; i < n; i++) { await heads.nth(i).click(); await sleep(120); txt += await p.evaluate(() => document.body.innerText); }
    say(!/Clara|클라라/.test(txt) && !p._errs.length, id, lang, 'no Clara in', n, 'steps', p._errs.slice(0, 1));
    await p.close();
  }
  console.log('bad', bad); await H.close();
})();
