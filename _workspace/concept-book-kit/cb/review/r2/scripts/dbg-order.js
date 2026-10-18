const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 390, h: 860, lang: 'en', dsf: 1 }); await p.waitForTimeout(1300);
  const r = await p.evaluate(() => { const els = [...document.querySelectorAll('.pb-main *')].filter(e => (/Flats come B E A D|Flats B E A D|E♯ B♯|F♯ C♯ G♯ D♯/.test(e.textContent)) && e.children.length < 4);
    return els.slice(0, 6).map(e => { const rects = []; const tw = document.createTreeWalker(e, NodeFilter.SHOW_TEXT); let n; const r = document.createRange(); let s = ''; let lastTop = null;
      while ((n = tw.nextNode())) for (let i = 0; i < n.nodeValue.length; i++) { r.setStart(n, i); r.setEnd(n, i + 1); const rc = r.getClientRects()[0]; if (rc && !/[♯♭♮]/.test(n.nodeValue[i]) && lastTop !== null && rc.top > lastTop + 8) s += ' ⏎ '; if (rc && !/[♯♭♮]/.test(n.nodeValue[i])) lastTop = rc.top; s += n.nodeValue[i]; }
      return e.tagName + ': ' + s.slice(0, 220); }); });
  console.log(r.join('\n'));
  await H.close();
})();
