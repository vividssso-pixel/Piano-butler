const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD);
  const p = await H.open({ path: '?book=work&ch=staff&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(2000);
  const r = await p.evaluate(() => {
    if (typeof sfWorkbook !== 'function') return 'no global';
    const W = sfWorkbook(), C = sfChkData();
    const path = W.s4.path, ok = path.every((c, i) => i === 0 || Math.abs(c[0] - path[i - 1][0]) + Math.abs(c[1] - path[i - 1][1]) === 1);
    const Fs = []; W.s4.grid.forEach((row, r) => row.forEach((d, c) => { if (d === 24) Fs.push(r + ',' + c); }));
    return { pathOk: ok, path: JSON.stringify(path), fCount: Fs.length, pathLen: path.length, home: W.s2.home.map(sfSSName), hi: W.s2.hi.map(x => x.a > x.b ? 'first' : 'second'), s3: W.s3.home.map(x => dName(x.d)).join(' '), s4: W.s4.home.map(x => dName(x.d)).join(' '), bingo: JSON.stringify(W.s6.win), chkB: C.ss.map(sfSSName) };
  });
  console.log(JSON.stringify(r, null, 1));
  await H.close();
})();
