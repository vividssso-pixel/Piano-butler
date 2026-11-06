const { chromium } = require('playwright-core');
const fs = require('fs');
const REACT = fs.readFileSync('node_modules/react/umd/react.production.min.js'), RDOM = fs.readFileSync('node_modules/react-dom/umd/react-dom.production.min.js');
const PAGE = process.argv[2] || 'drills.html';
const TOKEN = 'T'.repeat(36);
let pass = 0, fail = 0; const ok = (c, m) => { if (c) pass++; else { fail++; console.log('FAIL', m); } };
const ld = (() => { const d = new Date(); d.setDate(d.getDate() - 3); return d.toISOString().slice(0, 10); })();
const HW = 'Intervals, step 2 [chapter:intervals]\nC major scale, hands separate\nMinuet in G, bars 1-8';
const server = { ticks: [], calls: [], tickFn: true, hasTicksField: true };
async function setup(ctx) {
  await ctx.route(/cdnjs\.cloudflare\.com\/.*react-dom/, r => r.fulfill({ body: RDOM, contentType: 'application/javascript' }));
  await ctx.route(/cdnjs\.cloudflare\.com\/.*react\.production/, r => r.fulfill({ body: REACT, contentType: 'application/javascript' }));
  await ctx.route(/googletagmanager|googlesyndication|fonts\.g/, r => r.fulfill({ body: '' }));
  await ctx.route(/supabase\.co\/rest\/v1\/rpc\/(\w+)/, async r => {
    const fn = /rpc\/(\w+)/.exec(r.request().url())[1]; const a = JSON.parse(r.request().postData() || '{}');
    server.calls.push({ fn, a });
    const j = (o) => r.fulfill({ body: JSON.stringify(o), contentType: 'application/json' });
    if (fn === 'pb_student_info') return j({ name: 'Mia' });
    if (fn === 'pb_student_today') { const o = { name: 'Mia', lesson: { date: ld, homework: HW }, pieces: [], checkins: [], server_day: ld }; if (server.hasTicksField) o.ticks = server.ticks.slice(); return j(o); }
    if (fn === 'pb_hw_tick' && server.tickFn) {
      if (a.p_on) { if (!server.ticks.includes(a.p_item)) server.ticks.push(a.p_item); } else server.ticks = server.ticks.filter(x => x !== a.p_item);
      return j({ ok: true, ticks: server.ticks });
    }
    return r.fulfill({ status: 404, body: '{}' });
  });
}
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const ctx = await b.newContext({ viewport: { width: 420, height: 900 } });
  await setup(ctx);
  const pg = await ctx.newPage();
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  const url = 'http://127.0.0.1:8811/' + PAGE + '#k=' + TOKEN;
  // a play of the chapter yesterday (after the lesson) -> auto tick
  await pg.goto('http://127.0.0.1:8811/' + PAGE + '?nothing=1');
  await pg.evaluate(() => localStorage.clear());
  await pg.evaluate((at) => localStorage.setItem('pb_drill_records_v1', JSON.stringify({ 'intervals|1|lesson': { plays: 1, best: 8, lastAt: at, history: [{ at, score: 8, correct: 8, total: 10 }] } })), Date.now() - 86400000);
  await pg.goto(url); await pg.waitForSelector('[data-testid=hw-item]', { timeout: 15000 });
  await pg.waitForTimeout(600);
  const txt = async () => (await pg.textContent('[data-testid=today]'));
  ok((await pg.$$('[data-testid=hw-item]')).length === 3, '3 items');
  ok((await pg.textContent('[data-testid=hw-count]')).trim() === '1 of 3 done', 'count 1 of 3 (auto) got ' + await pg.textContent('[data-testid=hw-count]'));
  ok((await pg.$$('[data-testid=hw-auto]')).length === 1, 'one auto label');
  ok(await pg.$eval('[data-testid=hw-item] button[role=checkbox]', e => e.disabled && e.getAttribute('aria-checked') === 'true'), 'auto item checked + disabled');
  ok((await txt()).includes('This week'), 'kicker This week');
  await pg.screenshot({ path: 'shot-1.png', fullPage: false });
  // manual tick
  server.calls = [];
  await pg.click('button[aria-label="C major scale, hands separate"]'); await pg.waitForTimeout(500);
  ok(server.ticks.includes('C major scale, hands separate'), 'server got the tick');
  ok((await pg.textContent('[data-testid=hw-count]')).trim() === '2 of 3 done', 'count 2 of 3');
  ok(Object.keys(await pg.evaluate(() => JSON.parse(localStorage.getItem('pb_today_ticks_dirty_v1') || '{}'))).length === 0, 'dirty empty after save');
  // reload: comes back from the server
  await pg.evaluate(() => localStorage.removeItem('pb_today_ticks_v1'));
  await pg.reload(); await pg.waitForSelector('[data-testid=hw-item]'); await pg.waitForTimeout(800);
  ok(await pg.$eval('button[aria-label="C major scale, hands separate"]', e => e.getAttribute('aria-checked') === 'true'), 'tick restored from server');
  // teacher-side change: server tick removed elsewhere (another device unticked) -> server wins
  server.ticks = [];
  await pg.reload(); await pg.waitForSelector('[data-testid=hw-item]'); await pg.waitForTimeout(800);
  ok(await pg.$eval('button[aria-label="C major scale, hands separate"]', e => e.getAttribute('aria-checked') === 'false'), 'server untick wins');
  // offline save: stays local + dirty, sent on next visit
  server.tickFn = false;
  await pg.click('button[aria-label="Minuet in G, bars 1-8"]'); await pg.waitForTimeout(500);
  ok(await pg.$eval('button[aria-label="Minuet in G, bars 1-8"]', e => e.getAttribute('aria-checked') === 'true'), 'offline tick shows');
  ok(Object.keys(await pg.evaluate(() => JSON.parse(localStorage.getItem('pb_today_ticks_dirty_v1') || '{}'))).length === 1, 'offline tick is dirty');
  await pg.reload(); await pg.waitForSelector('[data-testid=hw-item]'); await pg.waitForTimeout(800);
  ok(await pg.$eval('button[aria-label="Minuet in G, bars 1-8"]', e => e.getAttribute('aria-checked') === 'true'), 'dirty tick survives a load while offline');
  server.tickFn = true;
  await pg.reload(); await pg.waitForSelector('[data-testid=hw-item]'); await pg.waitForTimeout(900);
  ok(server.ticks.includes('Minuet in G, bars 1-8'), 'dirty tick sent next visit');
  ok(Object.keys(await pg.evaluate(() => JSON.parse(localStorage.getItem('pb_today_ticks_dirty_v1') || '{}'))).length === 0, 'dirty cleared');
  // untick sends off
  await pg.click('button[aria-label="Minuet in G, bars 1-8"]'); await pg.waitForTimeout(500);
  ok(!server.ticks.includes('Minuet in G, bars 1-8'), 'untick reaches server');
  // clicking the auto item does nothing
  server.calls = [];
  await pg.click('[data-testid=hw-item] button[role=checkbox]', { force: true }); await pg.waitForTimeout(300);
  ok(!server.calls.some(c => c.fn === 'pb_hw_tick'), 'auto item not clickable');
  ok(errs.length === 0, 'no page errors: ' + errs.join(' | '));
  await pg.close();

  // a device with ticks from before Phase 451 sends them up the first time
  const pg2 = await ctx.newPage();
  server.ticks = []; server.calls = [];
  await pg2.goto('http://127.0.0.1:8811/' + PAGE + '?nothing=1');
  await pg2.evaluate(([who, ld]) => { localStorage.clear(); localStorage.setItem('pb_today_ticks_v1', JSON.stringify({ [who + '|' + ld + '|C major scale, hands separate']: 1 })); }, [TOKEN.slice(0, 8), ld]);
  await pg2.goto(url); await pg2.waitForSelector('[data-testid=hw-item]'); await pg2.waitForTimeout(900);
  ok(server.ticks.includes('C major scale, hands separate'), 'old local tick sent up once');
  ok((await pg2.textContent('[data-testid=hw-count]')).trim() === '1 of 3 done', 'no auto without plays; count 1 of 3');
  await pg2.close();

  // an older database (no ticks field, no pb_hw_tick): local ticks as before, nothing breaks
  const pg3 = await ctx.newPage(); const e3 = []; pg3.on('pageerror', e => e3.push(e.message));
  server.hasTicksField = false; server.tickFn = false; server.ticks = [];
  await pg3.goto('http://127.0.0.1:8811/' + PAGE + '?nothing=1'); await pg3.evaluate(() => localStorage.clear());
  await pg3.goto(url); await pg3.waitForSelector('[data-testid=hw-item]'); await pg3.waitForTimeout(600);
  await pg3.click('button[aria-label="Minuet in G, bars 1-8"]'); await pg3.waitForTimeout(400);
  await pg3.reload(); await pg3.waitForSelector('[data-testid=hw-item]'); await pg3.waitForTimeout(600);
  ok(await pg3.$eval('button[aria-label="Minuet in G, bars 1-8"]', e => e.getAttribute('aria-checked') === 'true'), 'old database: local tick kept');
  ok(e3.length === 0, 'old db no errors ' + e3.join('|'));
  await pg3.close();

  // a visitor with no link: no Today, no rpc (fresh browser profile)
  const ctx2 = await b.newContext(); await setup(ctx2); const pg4 = await ctx2.newPage(); server.calls = [];
  await pg4.goto('http://127.0.0.1:8811/' + PAGE); await pg4.waitForTimeout(2000);
  ok(!(await pg4.$('[data-testid=today]')) && server.calls.length === 0, 'no link: no Today, no calls ' + JSON.stringify(server.calls.map(c => c.fn)));
  await b.close();
  console.log('pass', pass, 'fail', fail);
})();
