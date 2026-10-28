// Build CS: checks + placement sync, the teacher's plan, the Home for an adult, the checkpoint theory filter
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const NM = '/home/claude/pbtest/kit/node_modules', NM2 = '/home/claude/pbtest/node_modules';
const BUILD = process.argv[2] || 'drills.t765.html';
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/cs/'; fs.mkdirSync(SH, { recursive: true });
const TOKEN = 'abcdefghijklmnopqrstuvwxyz0123456789ABCD';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
let bad = 0; const ok = (c, msg) => { console.log((c ? 'ok  ' : 'BAD ') + msg); if (!c) bad++; };
(async () => {
  const srv = http.createServer((req, res) => { const u = req.url.split('?')[0];
    if (u === '/drills.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end(fs.readFileSync('/home/claude/pbtest/a3/' + BUILD)); }
    if (u === '/blank.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end('<!doctype html><title>b</title>'); }
    res.writeHead(404); res.end('nf'); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  // the mock database
  const DB = { phaseD: false, stores: {}, plan: null, calls: [] };
  const rpc = (fn, a) => {
    DB.calls.push(fn + (a && a.p_store ? ':' + a.p_store : ''));
    if (fn === 'pb_student_info') return { name: 'Mia' };
    if (fn === 'pb_student_today') return { name: 'Mia', lesson: null, ticks: [], pieces: [], checkins: [], server_day: '2026-10-28' };
    if (fn === 'pb_get') { const o = { ref: 'r1', name: 'Mia', stores: DB.stores, server_time: new Date().toISOString() }; if (DB.phaseD) o.plan = DB.plan; return o; }
    if (fn === 'pb_save') {
      const ok0 = ['records','stamps','lesson_steps','steps_total','posture','arm_ex','last_chapter'].concat(DB.phaseD ? ['checks','place'] : []);
      if (!ok0.includes(a.p_store)) return { ok: false, reason: 'store' };
      const cur = DB.stores[a.p_store];
      if ((cur ? cur.rev : 0) !== a.p_base_rev) return { ok: false, reason: 'conflict', rev: cur ? cur.rev : 0, value: cur ? cur.value : null };
      DB.stores[a.p_store] = { value: a.p_value, rev: (cur ? cur.rev : 0) + 1 }; return { ok: true, rev: DB.stores[a.p_store].rev };
    }
    if (fn === 'pb_log') return { ok: true, added: (a.p_rows || []).length, skipped: 0 };
    return { ok: true };
  };
  async function open(o) {
    const ctx = await browser.newContext({ viewport: { width: 390, height: o.h || 1200 } });
    const p = await ctx.newPage(); p._errs = []; p.on('pageerror', e => p._errs.push(e.message));
    const file = u => r => r.fulfill({ path: u, contentType: 'text/javascript' });
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/react/**', file(NM2 + '/react/umd/react.production.min.js'));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/react-dom/**', file(NM2 + '/react-dom/umd/react-dom.production.min.js'));
    await p.route('**/cdnjs.cloudflare.com/ajax/libs/babel-standalone/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
    await p.route('**/fonts.gstatic.com/**', r => r.fulfill({ body: '' }));
    await p.route('**/rest/v1/rpc/**', async r => { const fn = r.request().url().split('/rpc/')[1]; let a = {}; try { a = JSON.parse(r.request().postData() || '{}'); } catch (e) {} r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(rpc(fn, a)) }); });
    await p.goto(base + '/blank.html');
    if (o.store) await p.evaluate((st) => { for (const k in st) localStorage.setItem(k, st[k]); }, o.store);
    await p.goto(base + '/drills.html' + (o.path || '')); await p.waitForSelector('#root *'); await sleep(o.wait || 2500);
    if (o.lang === 'ko') { const b = await p.$('button.chip:has-text("한국어")'); if (b) { await b.click(); await sleep(500); } }
    return p;
  }
  const now = Date.now();
  const checksA = JSON.stringify({ rooms: { 'note-values': { pass: now - 9e5, best: 10, last: 10, tries: 1, review: { due: now + 6e8, stage: 1 } } }, floors: { '0a': { at: now - 5e5, right: 11, total: 14, review: ['staff'] } } });
  const placeA = JSON.stringify({ piano: 4, theory: 1, at: now - 1e6 });
  const linked = { pb_mode_v1: 'student', pb_link_token_v1: TOKEN, pb_link_name_v1: 'Mia', pb_sync_owner_v1: 'r1', pb_checks_v1: checksA, pb_place_v1: placeA };
  // 1. before the database step: the two stores are refused once, quietly
  let p = await open({ store: linked });
  const c1 = DB.calls.filter(c => c === 'pb_save:checks' || c === 'pb_save:place').length;
  await p.evaluate(() => { const c = JSON.parse(localStorage.getItem('pb_checks_v1')); c.rooms.staff = { pass: Date.now(), best: 9, last: 9, tries: 1, review: { due: Date.now() + 6e8, stage: 1 } }; localStorage.setItem('pb_checks_v1', JSON.stringify(c)); });
  await sleep(4500);
  const c2 = DB.calls.filter(c => c === 'pb_save:checks').length;
  ok(c1 === 2 && !DB.stores.checks && !p._errs.length, 'before phaseD: checks and place refused once each (' + c1 + '), nothing stored, no errors ' + p._errs.slice(0, 1));
  console.log('     a local change after the refusal: ' + (c2 - 1) + ' more save(s) of checks (0 expected this session)');
  ok(c2 - 1 === 0, 'no retry of a refused store in the same session');
  await p.close();
  // 2. after: what the device already holds is sent though unchanged; the plan arrives
  DB.phaseD = true; DB.plan = { piano: 4, theory: 1, home: true }; DB.calls = [];
  p = await open({ store: { ...linked, pb_sync_revs_v1: '{}', pb_sync_dirty_v1: '{}' } });
  ok(DB.stores.checks && DB.stores.checks.value.rooms['note-values'] && DB.stores.place && DB.stores.place.value.piano === 4, 'after phaseD: checks and place sent once without a change');
  const plan = await p.evaluate(() => localStorage.getItem('pb_plan_v1'));
  ok(plan && JSON.parse(plan).home === true, 'the plan is kept on the device: ' + plan);
  const homeBtn = p.locator('[data-testid="today-home"]');
  ok(await homeBtn.count() === 1, 'Today shows the Home button for an adult');
  await p.screenshot({ path: SH + 'today-adult.png', fullPage: false });
  await homeBtn.click(); await sleep(700);
  const homeHas = await p.evaluate(() => !!document.querySelector('[data-testid="home"], [data-testid="concept-home"]') || /Pitch|음높이/.test(document.body.innerText));
  ok(homeHas && !p._errs.length, 'the Home opens for the adult ' + p._errs.slice(0, 1));
  await p.screenshot({ path: SH + 'home-adult.png', fullPage: false });
  const back = p.locator('button.ghost-btn', { hasText: /Today|오늘/ });
  ok(await back.count() >= 1, 'a way back to Today from the Home');
  await p.close();
  // 2b. the adult goes into the Home: Pitch, Keys and staff, a lesson, back
  DB.plan = { home: true }; DB.calls = [];
  p = await open({ store: linked });
  await p.locator('[data-testid="today-home"]').click(); await sleep(600);
  await p.locator('button, [role=button]', { hasText: /^Pitch/ }).first().click(); await sleep(600);
  await p.screenshot({ path: SH + 'home-adult-pitch.png' });
  ok(await p.locator('button.ghost-btn', { hasText: /Today|오늘/ }).count() === 0, 'one way back at a time (Today only on the Home itself)');
  await p.locator('button, [role=button]', { hasText: /^Keys and staff/ }).first().click(); await sleep(600);
  const kb = p.locator('button, [role=button]', { hasText: 'Naming the white keys' }).first();
  ok(await kb.count() === 1, 'the adult sees the Keys and staff lessons');
  if (await kb.count()) { await kb.click(); await sleep(800); }
  await p.screenshot({ path: SH + 'home-adult-lesson.png' });
  ok(/the small house|black-key/.test(await p.evaluate(() => document.body.innerText)) && !p._errs.length, 'a Home lesson opens for the adult ' + p._errs.slice(0, 1));
  await p.close();
  // 3. no Home for a child (plan without home), the checkpoint theory cut, the house starts on the plan's floor
  DB.plan = { piano: 5, theory: 1 }; DB.calls = [];
  p = await open({ store: { ...linked, pb_plan_v1: JSON.stringify({ piano: 4, theory: 1, home: true }) } });
  ok(await p.locator('[data-testid="today-home"]').count() === 0, 'a child: no Home button once the plan says so');
  await p.evaluate(() => { localStorage.setItem('pb_mode_v1', 'student'); });
  const here = await p.evaluate(() => { const all = pathIds(); return placeNext(all, id => true); });
  ok(here === 'listen-4', 'plan floor 5 (Grade 4), theory 1: the next room is ' + here + ' (theory rooms T4 wait)');
  await p.close();
  p = await open({ path: '?view=path&teacher=0', store: { pb_mode_v1: 'student', pb_plan_v1: JSON.stringify({ piano: 5, theory: 1 }) }, wait: 1200 });
  const door = p.locator('[data-door]'); if (await door.count()) { await door.first().click(); await sleep(1200); }
  const fc = p.locator('[data-testid="floor-check"]'); const floorKey = await fc.getAttribute('data-floor');
  const cut = await p.locator('[data-testid="floor-theory-cut"]').count();
  console.log('     checkpoint floor ' + floorKey + ', cut note ' + cut + ': ' + (cut ? await p.locator('[data-testid="floor-theory-cut"]').innerText() : ''));
  ok(cut === 1, 'the floor checkpoint asks theory only up to the theory grade');
  await fc.screenshot({ path: SH + 'floor-cut.png' });
  await fc.locator('[data-testid="floor-check-start"]').click(); await sleep(400);
  const firstRoom = await p.evaluate(() => { const r = document.querySelector('[data-testid="check-run"]'); return r ? r.innerText.slice(0, 120) : ''; });
  console.log('     first question: ' + firstRoom.replace(/\s+/g, ' ').slice(0, 100));
  ok(!p._errs.length, 'no errors ' + p._errs.slice(0, 1));
  await p.close();
  // 4. a conflict merges both devices' checks
  DB.phaseD = true; DB.plan = null; DB.calls = [];
  DB.stores = { checks: { rev: 3, value: { rooms: { tones: { pass: now - 2e6, best: 8, last: 8, tries: 2, review: { due: now + 1e8, stage: 1 } } }, floors: { '1': { at: now - 1e5, right: 10, total: 15, review: [] } } } } };
  p = await open({ store: { ...linked, pb_sync_revs_v1: JSON.stringify({ checks: 2 }), pb_sync_dirty_v1: JSON.stringify({ checks: 1 }) } });
  const m = DB.stores.checks.value;
  ok(m.rooms.tones && m.rooms['note-values'] && m.floors['1'] && m.floors['0a'] && DB.stores.checks.rev === 4, 'conflict: both devices’ rooms and floors kept (rev ' + DB.stores.checks.rev + ')');
  const plan2 = await p.evaluate(() => localStorage.getItem('pb_plan_v1'));
  ok(plan2 === null, 'a cleared plan is removed from the device');
  await p.close();
  console.log('bad', bad);
  await browser.close(); srv.close();
})();
