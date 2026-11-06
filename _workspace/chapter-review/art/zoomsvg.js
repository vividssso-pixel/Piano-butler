// Render SVG files large with Chromium: node zoomsvg.js out.png width file1.svg file2.svg ...
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const [out, w, ...files] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: +w, height: 400 } });
  await p.setContent('<body style="margin:0;background:#fff">' + files.map(f => '<div style="border-bottom:1px solid #ddd">' + fs.readFileSync(f, 'utf8').replace(/<svg ([^>]*?)width="[^"]*" height="[^"]*"/, '<svg $1style="width:100%;height:auto;display:block"') + '</div>').join('') + '</body>');
  await p.screenshot({ path: out, fullPage: true }); await b.close();
})();
