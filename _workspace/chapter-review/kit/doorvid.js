// a short film of the door: the hall, the door opens, the house rises above it (CDP screencast frames + timestamps)
const { start } = require('./contentharness');
const fs = require('fs');
(async () => {
  const H = await start('drills.t426.html');
  const full = (n) => { const o = {}; for (let i = 0; i < n; i++) o[i] = 1; return o; };
  const store = { pb_lesson_steps_v1: JSON.stringify({ 'posture-hands': full(6), 'first-steps': full(9), 'note-names': full(8), staff: { 0: 1, 1: 1 } }), pb_steps_total_v1: JSON.stringify({ 'posture-hands': 6, 'first-steps': 9, 'note-names': 8, staff: 7 }) };
  fs.rmSync('p425/vid', { recursive: true, force: true }); fs.mkdirSync('p425/vid');
  const p = await H.open({ path: '?view=map', w: 390, h: 760, store, dsf: 2 }); await p.waitForTimeout(600);
  const door = await p.$('[data-door]'); await door.scrollIntoViewIfNeeded(); await p.evaluate(() => window.scrollBy(0, 140)); await p.waitForTimeout(400);
  const cdp = await p.context().newCDPSession(p); const frames = [];
  cdp.on('Page.screencastFrame', async (f) => { frames.push({ t: f.metadata.timestamp, d: f.data }); try { await cdp.send('Page.screencastFrameAck', { sessionId: f.sessionId }); } catch (e) {} });
  await cdp.send('Page.startScreencast', { format: 'png', everyNthFrame: 1, maxWidth: 780, maxHeight: 1520 });
  await p.waitForTimeout(1400);
  const b = await door.boundingBox(); await p.mouse.click(b.x + b.width / 2, b.y + b.height / 2);
  await p.waitForTimeout(2600);
  for (let i = 0; i < 16; i++) { await p.evaluate(() => window.scrollBy(0, -24)); await p.waitForTimeout(45); }
  await p.waitForTimeout(1500);
  await cdp.send('Page.stopScreencast');
  frames.forEach((f, i) => fs.writeFileSync('p425/vid/f' + String(i).padStart(4, '0') + '_' + Math.round(f.t * 1000) + '.png', Buffer.from(f.d, 'base64')));
  console.log('frames', frames.length);
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
