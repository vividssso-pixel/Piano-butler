const { chromium } = require('playwright-core');
const fs = require('fs');
const core = require('@babel/core');
const file = process.argv[2] || 'teacher-dashboard.html';
const h = fs.readFileSync(file, 'utf8');
const i = h.indexOf('<script type="text/babel">') + '<script type="text/babel">'.length;
let src = h.slice(i, h.indexOf('</script>', i));
const cut = src.indexOf('// Check session before rendering');
src = src.slice(0, cut) + '\nwindow.__T = { StudentLinkPanel, ThisWeekCard, hwLines, latestHomeworkLog };\n';
const out = core.transformSync(src, { presets: [[require.resolve('@babel/preset-react'), { runtime: 'classic' }]], babelrc: false, configFile: false }).code;
new Function('React', 'ReactDOM', out.replace(/^/, 'return;')); // syntax check
const REACT = fs.readFileSync('node_modules/react/umd/react.production.min.js', 'utf8'), RDOM = fs.readFileSync('node_modules/react-dom/umd/react-dom.production.min.js', 'utf8');
let pass = 0, fail = 0; const ok = (c, m) => { if (c) pass++; else { fail++; console.log('FAIL', m); } };
const day = (n) => { const d = new Date(); d.setDate(d.getDate() + n); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); };
const LD = day(-3);
const stub = `
window.__FX = null;
function q(table){ const f=[]; const b={ select(){return b}, eq(k,v){f.push(['eq',k,v]);return b}, gte(k,v){f.push(['gte',k,v]);return b}, order(){return b}, limit(){return b}, maybeSingle(){ b._one=true; return b},
  then(res,rej){ const fx=window.__FX[table]; if(fx===undefined||fx==='ERR') return Promise.resolve({data:null,error:{message:'relation does not exist'}}).then(res,rej);
    let rows=fx.filter(r=>f.every(([op,k,v])=> op==='eq' ? String(r[k])===String(v) : String(r[k])>=String(v)));
    return Promise.resolve({data: b._one ? (rows[0]||null) : rows, error:null}).then(res,rej);} }; return b; }
window._supabase = { from: q };
window.requireAuth = () => Promise.resolve(null);
`;
const page = `<!doctype html><html><head><meta charset="utf-8"><script src="https://cdn.tailwindcss.com"></script></head><body style="background:#f8f5ee;padding:16px"><div id="root"></div>
<script>${REACT}</script><script>${RDOM}</script><script>${stub}</script><script>${out}</script></body></html>`;
if (!process.env.KEEP) fs.writeFileSync('dash_harness.html', page);
(async () => {
  const px = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined;
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', proxy: px, args: ['--ignore-certificate-errors'] });
  const pg = await b.newPage({ viewport: { width: 760, height: 900 } });
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto('file://' + process.cwd() + '/dash_harness.html'); await pg.waitForTimeout(1500);
  const student = { id: 7, name: 'Mia Kim' };
  const logs = [
    { id: 3, studentId: 7, date: day(0), type: 'regular', homework: '' },
    { id: 2, studentId: 7, date: LD, type: 'regular', homework: '1. Intervals, step 2 [chapter:intervals]\n2. C major scale, hands separate\n3. Minuet in G, bars 1-8\n4. Practice dice [tool:practice-dice]' },
    { id: 1, studentId: 7, date: day(-10), type: 'regular', homework: 'Old week' },
  ];
  const mount = async (fx, lg) => {
    await pg.evaluate(([fx, student, lg]) => { window.__FX = fx; const el = document.getElementById('root'); if (window.__r) window.__r.unmount(); window.__r = ReactDOM.createRoot(el); window.__r.render(React.createElement(window.__T.StudentLinkPanel, { student, logs: lg })); }, [fx, student, lg]);
    await pg.waitForTimeout(700);
  };
  const base = { student_links: [{ student_id: 7, display_name: 'Mia', token: 'x'.repeat(36), active: true }], practice_checkins: [], progress_store: [] };
  const playAt = new Date(LD + 'T00:00:00'); playAt.setDate(playAt.getDate() + 1); playAt.setHours(16);
  const before = new Date(LD + 'T00:00:00'); before.setHours(-5);
  await mount({ ...base, homework_ticks: [{ student_id: 7, lesson_date: LD, item: 'C major scale, hands separate', at: new Date().toISOString() }, { student_id: 7, lesson_date: day(-10), item: 'Minuet in G, bars 1-8', at: new Date().toISOString() }],
    practice_log: [{ student_id: 7, at: before.toISOString(), drill: 'chords' }, { student_id: 7, at: playAt.toISOString(), drill: 'intervals' }] }, logs);
  ok(!!(await pg.$('[data-testid=this-week]')), 'card shows');
  const rows = await pg.$$eval('[data-testid=this-week-row]', es => es.map(e => e.textContent));
  ok(rows.length === 4, '4 rows ' + rows.length);
  ok(/Intervals, step 2.*✓ played/.test(rows[0]), 'chapter played ' + rows[0]);
  ok(/C major.*✓ ticked/.test(rows[1]), 'ticked ' + rows[1]);
  ok(/Minuet.*not yet/.test(rows[2]), 'other lesson tick ignored ' + rows[2]);
  ok(/Practice dice.*not yet/.test(rows[3]) && !/\[tool/.test(rows[3]), 'tool line label ' + rows[3]);
  ok((await pg.textContent('[data-testid=this-week-count]')).trim() === '2 of 4 done', 'count');
  ok(!(await pg.textContent('[data-testid=this-week]')).includes('migrations/'), 'no SQL note when table exists');
  await pg.screenshot({ path: 'dash-1.png', clip: await (await pg.$('[data-testid=this-week]')).boundingBox() });
  // played before the lesson does not count
  await mount({ ...base, homework_ticks: [], practice_log: [{ student_id: 7, at: before.toISOString(), drill: 'intervals' }] }, logs);
  ok(/not yet/.test((await pg.$$eval('[data-testid=this-week-row]', es => es.map(e => e.textContent)))[0]), 'play before lesson day not counted');
  // table missing: note shown, plays still shown
  await mount({ ...base, homework_ticks: 'ERR', practice_log: [{ student_id: 7, at: playAt.toISOString(), drill: 'intervals' }] }, logs);
  ok((await pg.textContent('[data-testid=this-week]')).includes('migrations/2026-10-12_phaseC_this-week.sql'), 'SQL note when table missing');
  ok((await pg.textContent('[data-testid=this-week-count]')).trim() === '1 of 4 done', 'plays still counted');
  // no homework at all
  await mount({ ...base, homework_ticks: [], practice_log: [] }, [{ id: 1, studentId: 7, date: day(0), type: 'regular', homework: '' }]);
  ok((await pg.textContent('[data-testid=this-week]')).includes('No homework yet'), 'empty state');
  // absent log with homework is skipped
  const T = await pg.evaluate(() => { const L = window.__T.latestHomeworkLog; return [L([{ id: 5, date: '2026-10-11', type: 'absent', homework: 'x' }, { id: 4, date: '2026-10-05', type: 'regular', homework: 'y' }]).id, L([{ id: 8, date: '2026-10-05', homework: 'a' }, { id: 9, date: '2026-10-05', homework: 'b' }]).id]; });
  ok(T[0] === 4 && T[1] === 9, 'latest log rule ' + T);
  // keys match the student page (list marks removed, mark kept in key)
  const K = await pg.evaluate(() => window.__T.hwLines('- Scales [chapter:scales]\n2) Hello').map(x => x.key + '|' + x.text + '|' + x.chapter));
  ok(K[0] === 'Scales [chapter:scales]|Scales|scales' && K[1] === 'Hello|Hello|null', 'keys ' + K);
  // no link -> no card
  await mount({ ...base, student_links: [], homework_ticks: [], practice_log: [] }, logs);
  ok(!(await pg.$('[data-testid=this-week]')), 'no link no card');
  ok(errs.length === 0, 'errors ' + errs.join('|'));
  await b.close(); console.log('pass', pass, 'fail', fail);
})();
