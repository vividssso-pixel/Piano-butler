// Phase 425 on the site: chapter 1's guide drawings follow the book -- the rabbit leaves the puppet picture (hero.svg),
// and the ground lines are navy hairlines instead of beige (every drawing of chapter 1's guide page).
//   node fixph425.js <tools/lessons/svg/posture-hands> <dir with fixart.js>
const fs = require('fs'), path = require('path');
const [dir, art] = process.argv.slice(2);
const { fixPuppet } = require(path.resolve(art, 'fixart.js'));
let n = 0;
for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.svg'))) {
  const p = path.join(dir, f); let s = fs.readFileSync(p, 'utf8'), o = s;
  if (f === 'hero.svg') {
    if (!/id="hppuppet/.test(s)) throw new Error('hero.svg is not the puppet picture');
    s = fixPuppet(s).replace('width="540" height="428"', 'width="452" height="428"');
    if (!/viewBox="44 0 226 214" width="452"/.test(s)) throw new Error('hero.svg size');
  }
  s = s.split('#bdb7a6').join('rgba(38,41,107,0.4)');
  if (s !== o) { fs.writeFileSync(p, s); n++; console.log('fixed', f); }
}
console.log(n, 'files');
