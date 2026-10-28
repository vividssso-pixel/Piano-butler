const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/cs/';
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start('drills.t765.html');
  for (const lang of ['en', 'ko']) {
    for (const [name, nameKo, clicks] of [['Naming the white keys', '흰건반 이름 붙이기', [0, 1, 6]], ['Black keys', '검은건반', [3]]]) {
      const p = await H.open({ path: '?view=home&area=pitch&concept=p-staff', w: 390, h: 1400, lang, store: { pb_mode_v1: 'teacher' } });
      const b = p.locator('button, [role=button]', { hasText: lang === 'ko' ? nameKo : name }).first();
      if (!(await b.count())) { console.log('no lesson button', name, lang); await p.close(); continue; }
      await b.click(); await sleep(900);
      let at = 0;
      for (const c of clicks) {
        while (at < c) { const g = p.locator('button', { hasText: at === 0 ? /One by one|하나씩/ : /Next|다음/ }).first(); if (!(await g.count())) break; await g.click(); await sleep(350); at++; }
        await p.screenshot({ path: SH + 'kq-' + name.split(' ')[0] + '-' + c + '-' + lang + '.png', fullPage: false });
      }
      console.log(lang, name, 'errors', p._errs.slice(0, 2));
      await p.close();
    }
  }
  await H.close();
})();
