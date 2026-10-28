const http = require('http'), fs = require('fs');
const { chromium } = require('playwright');
const NM = '/home/claude/pbtest/node_modules';
const PAGE = process.argv[2] || 'td766.html';
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/dash/'; fs.mkdirSync(SH, { recursive: true });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
let bad = 0; const ok = (c, m) => { console.log((c ? 'ok  ' : 'BAD ') + m); if (!c) bad++; };
(async () => {
  const srv = http.createServer((req, res) => { const u = req.url.split('?')[0];
    if (u === '/teacher-dashboard.html') { res.writeHead(200, { 'content-type': 'text/html' }); return res.end(fs.readFileSync(PAGE)); }
    if (u === '/auth.js') { res.writeHead(200, { 'content-type': 'text/javascript' }); return res.end(fs.readFileSync('auth.js')); }
    res.writeHead(404); res.end('nf'); });
  await new Promise(r => srv.listen(0, r)); const base = 'http://localhost:' + srv.address().port;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const now = Date.now();
  const fixture = (o = {}) => ({ missing: o.missing || [], tables: {
    students: [{ id: 's1', user_id: 'u1', name: 'Mia Kim', grade: 'Grade 3', track: 'exam', lesson_day: 'Monday', lesson_time: '16:00', created_at: '2026-09-01T00:00:00Z', extra: '{}' }],
    lesson_logs: [], lesson_overrides: [], practice_checkins: [], practice_log: [], homework_ticks: [],
    student_links: [{ student_id: 's1', token: 'abcdefghijklmnopqrstuvwxyz0123456789ABCD', display_name: 'Mia', active: true }],
    progress_store: o.empty ? [] : [
      { student_id: 's1', store: 'place', value: { piano: 4, theory: 3, at: now - 3 * 864e5 }, rev: 1 },
      { student_id: 's1', store: 'checks', value: { rooms: {
        'listen-3': { pass: now - 2 * 864e5, best: 9, last: 9, tries: 1, review: { due: now - 864e5, stage: 1 } },
        'harmony-23': { best: 6, last: 6, tries: 2 },
        'note-values': { pass: now - 20 * 864e5, best: 10, last: 10, tries: 1, review: { due: 9e15, stage: 3 } },
        'staff': { pass: now - 19 * 864e5, best: 8, last: 8, tries: 1, review: { due: now + 9 * 864e5, stage: 2 } } },
        floors: { '0a': { at: now - 10 * 864e5, right: 12, total: 14, review: ['staff'] }, '4': { at: now - 864e5, right: 9, total: 15, review: ['harmony-23', 'rhythm-23'] } } }, rev: 3 } ],
    student_plan: [] } });
  async function open(o) {
    const ctx = await browser.newContext({ viewport: { width: o.w || 1100, height: 1400 } });
    const p = await ctx.newPage(); p._errs = []; p.on('pageerror', e => p._errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') p._errs.push('console: ' + m.text()); });
    const file = (f) => r => r.fulfill({ path: f, contentType: 'text/javascript' });
    await p.route('**/unpkg.com/react@18/**', file(NM + '/react/umd/react.production.min.js'));
    await p.route('**/unpkg.com/react-dom@18/**', file(NM + '/react-dom/umd/react-dom.production.min.js'));
    await p.route('**/unpkg.com/@babel/standalone/**', file(NM + '/@babel/standalone/babel.min.js'));
    await p.route('**/cdn.tailwindcss.com/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.route('**/cdn.sheetjs.com/**', r => r.fulfill({ body: '', contentType: 'text/javascript' }));
    await p.route('**/cdn.jsdelivr.net/npm/@supabase/**', file(__dirname + '/mocksb.js'));
    await p.route('**/fonts.googleapis.com/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
    await p.route('**/cdn.jsdelivr.net/gh/**', r => r.fulfill({ body: '', contentType: 'text/css' }));
    await p.addInitScript((fx) => { window.__DB = fx; }, fixture(o));
    await p.goto(base + '/teacher-dashboard.html'); await sleep(2500);
    return p;
  }
  const toStudent = async (p) => { await p.locator('button', { hasText: /^Students$/ }).first().click(); await sleep(600); await p.locator('text=Mia Kim').first().click(); await sleep(1500); };
  // A: placement + checks, no plan yet (phaseD run)
  let p = await open({});
  await toStudent(p);
  const sec = p.locator('[data-testid="drill-start"]');
  ok(await sec.count() === 1, 'the Start and checks section is on the student page');
  const place = await p.locator('[data-testid="drill-place"]').innerText();
  ok(/Floor 5 · Grade 3/.test(place) && /Theory Grade 3/.test(place), 'placement shown: ' + place.replace(/\s+/g, ' '));
  const rows = await p.locator('[data-testid="drill-checks"] tbody tr').count();
  ok(rows === 2, 'two floors with checks (Beginner, Grade 3): ' + rows);
  const due = await p.locator('[data-testid="checks-due"]').innerText();
  ok(/Ear Training, Grade 3/.test(due) && !/Notes/.test(due), 'review due: ' + due);
  const eff = await p.locator('[data-testid="plan-effect"]').innerText();
  ok(/Floor 5 · Grade 3/.test(eff) && /Theory Grade 3/.test(eff), 'effect line: ' + eff);
  await sec.screenshot({ path: SH + 'section.png' });
  // set a plan: Floor 6 (Grade 4), Theory Grade 1, Home on -> saved
  await p.locator('[data-testid="plan-floor"]').selectOption('5');
  await p.locator('[data-testid="plan-theory"]').selectOption('1');
  await p.locator('[data-testid="plan-home"]').check();
  await p.locator('[data-testid="plan-save"]').click(); await sleep(400);
  const saved = await p.evaluate(() => JSON.stringify(window.__DB.tables.student_plan));
  ok(/"piano":5/.test(saved) && /"theory":1/.test(saved) && /"home":true/.test(saved), 'plan saved: ' + saved);
  const eff2 = await p.locator('[data-testid="plan-effect"]').innerText();
  ok(/Floor 6 · Grade 4/.test(eff2) && /Theory Grade 1/.test(eff2), 'effect follows the plan: ' + eff2);
  await sec.screenshot({ path: SH + 'section-saved.png' });
  // clear it -> row removed
  await p.locator('[data-testid="plan-floor"]').selectOption(''); await p.locator('[data-testid="plan-theory"]').selectOption(''); await p.locator('[data-testid="plan-home"]').uncheck();
  await p.locator('[data-testid="plan-save"]').click(); await sleep(400);
  ok(await p.evaluate(() => window.__DB.tables.student_plan.length) === 0, 'an empty plan removes the row');
  ok(!p._errs.length, 'no errors ' + p._errs.slice(0, 2));
  await p.close();
  // B: phaseD not run: student_plan missing -> the note, no selects
  p = await open({ missing: ['student_plan'], empty: true });
  await toStudent(p);
  ok(await p.locator('[data-testid="plan-needs-sql"]').count() === 1 && await p.locator('[data-testid="plan-floor"]').count() === 0, 'without the database step: a note instead of the setting');
  ok(await p.locator('[data-testid="checks-empty"]').count() === 1, 'no checks yet: one line');
  await p.locator('[data-testid="drill-start"]').screenshot({ path: SH + 'section-nosql.png' });
  ok(!p._errs.length, 'no errors ' + p._errs.slice(0, 2));
  await p.close();
  // C: phone width
  p = await open({ w: 390 }); await toStudent(p);
  const ov = await p.evaluate(() => { const el = document.querySelector('[data-testid="drill-start"]'); return el ? el.scrollWidth - el.clientWidth : -1; });
  ok(ov <= 1, 'phone width: no overflow of the section (' + ov + ')');
  await p.locator('[data-testid="drill-start"]').screenshot({ path: SH + 'section-390.png' });
  await p.close();
  console.log('bad', bad);
  await browser.close(); srv.close();
})();
