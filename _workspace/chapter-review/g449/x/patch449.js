// Phase 449 (her 2026-10-12 19:17: '퀸즈랜드, 킹스랜드는 아이디어고 가온도 높은음자리표 도 낮은음 자리표 도는 middle c,
// treble c, bass c 그 위로는 high c low c 이렇게 정정해줘'): the five Cs get their real names. Queensland and Kingsland
// stay as the two lands (the idea); no C is named after them, the sea, the sky or Clara any more.
//   Sea C -> low C (C2), Kingsland C -> bass C (C3), Clara's C -> middle C (C4), Queensland C -> treble C (C5),
//   Sky C -> high C (C6); Korean 낮은 도, 낮은음자리표 도, 가운데 도, 높은음자리표 도, 높은 도.
// Lower case in a sentence and in the name tables (they sit beside 'the King's F'); a capital where a label or a sentence
// starts (decided one by one, listed in CAP). Every occurrence is checked against the list it was decided on.
//   node patch449.js <src> <dst>
const fs = require('fs');
const [src, dst] = process.argv.slice(2);
let s = fs.readFileSync(src, 'utf8');
const EN = [["Queensland Cs", "treble Cs"], ["Kingsland Cs", "bass Cs"], ["Clara\\'s Cs", "middle Cs"], ["Clara's Cs", "middle Cs"],
  ["Queensland C", "treble C"], ["Kingsland C", "bass C"], ["Sea C", "low C"], ["Sky C", "high C"], ["Clara\\'s C", "middle C"], ["Clara's C", "middle C"], ["Clara’s C", "middle C"]];
const MAP = Object.fromEntries(EN);
const re = new RegExp(EN.map(([a]) => a.replace(/[\\']/g, m => '\\' + m)).join('|'), 'g');
const SEQ = ["Clara\\'s C","Sky C","Sea C","Clara\\'s C","Queensland C","Kingsland C","Queensland C","Kingsland C","Sky C","Sea C","Clara\\'s C","Clara\\'s C","Kingsland C","Clara\\'s C","Queensland C","Sky C","Sea C","Clara\\'s C","Sea C","Sky C","Clara's C","Clara's C","Clara's C","Clara’s C","Clara's C","Clara's C","Clara's C","Clara's C","Clara’s C","Clara’s C","Clara's C","Clara's C","Clara's C","Kingsland C","Clara\\'s C","Queensland C","Kingsland C","Queensland C","Kingsland C","Clara's C","Queensland C","Kingsland C","Clara's C","Queensland C","Kingsland C","Clara\\'s C","Queensland C","Queensland Cs","Clara's Cs","Kingsland Cs","Queensland C","Clara\\'s C","Kingsland C","Queensland C","Clara\\'s C","Kingsland C","Sky C","Sea C","Sky C","Sky C","Sky C","Sea C","Sea C","Sea C","Clara's C","Clara's C","Clara's C","Queensland C","Kingsland C","Sky C","Sea C","Clara\\'s C","Clara\\'s C","Queensland C","Kingsland C","Sky C","Sea C","Clara\\'s C","Queensland C","Kingsland C","Sky C","Sea C","Clara's C","Clara's C","Sky C","Sky C","Clara's C","Sea C","Sea C","Clara's C","Clara's C","Sea C","Kingsland C","Clara's C","Queensland C","Sky C","Queensland C","Kingsland C","Sky C","Sea C","Sea C","Clara's C","Sky C","Sea C","Kingsland C","Sea C","Sky C","Kingsland C","Queensland C","Clara's C","Sea C","Kingsland C","Clara\\'s C","Queensland C","Sky C","Sea C","Clara\\'s C","Sky C","Sky C","Sea C","Clara's C","Sea C","Sea C","Sky C","Sea C","Clara's C","Sky C","Sky C","Sky C","Sea C","Sea C","Sea C","Clara's C","Sky C","Clara's C"];
// where a label or a sentence starts: a picture's labels, the chips that stand alone, the answer lines, a new sentence
const CAP = new Set([0, 1, 6, 8, 11, 15, 50, 51, 52, 53, 54, 55, 60, 63, 71, 72, 73, 74, 75, 76, 77, 83, 90, 127, 129]);
let k = 0;
s = s.replace(re, (w) => {
  if (SEQ[k] !== w) throw new Error('occurrence ' + k + ': found ' + w + ', decided on ' + SEQ[k]);
  let r = MAP[w]; if (CAP.has(k)) r = r[0].toUpperCase() + r.slice(1);
  k++; return r;
});
if (k !== SEQ.length) throw new Error('found ' + k + ' occurrences, decided on ' + SEQ.length);
// Korean: the particles after C (씨) and after 도 are the same (both end in a vowel)
const KO = [['퀸즈랜드 C', '높은음자리표 도'], ['킹스랜드 C', '낮은음자리표 도'], ['바다 C', '낮은 도'], ['하늘 C', '높은 도'], ['클라라의 C', '가운데 도']];
const KON = { '퀸즈랜드 C': 13, '킹스랜드 C': 14, '바다 C': 16, '하늘 C': 15, '클라라의 C': 25 };
for (const [a, b] of KO) { const n = s.split(a).length - 1; if (n !== KON[a]) throw new Error(a + ': ' + n); s = s.split(a).join(b); }
const rep = (a, b) => { const n = s.split(a).length - 1; if (n !== 1) throw new Error('found ' + n + ': ' + a.slice(0, 80)); s = s.replace(a, () => b); };
// the fold's label said Clara's C in chapter 6 and middle C before it: one name now
rep("text={ledger ? t('middle C', '가운데 도') : t('middle C', '가운데 도')}", "text={t('middle C', '가운데 도')}");
// the five-C chips and the line under them stand alone: a capital there (the table stays lower case for sentences)
rep("const LL_FIVE = [", "const llCap = (w) => w.charAt(0).toUpperCase() + w.slice(1);   // Phase 449: a C's name standing alone\nconst LL_FIVE = [");
rep("onClick={() => tapC(i)}>{LL_C[d]()}</button>", "onClick={() => tapC(i)}>{llCap(LL_C[d]())}</button>");
rep("<b style={{color:BK.coral}}>{LL_C[LL_FIVE[c][0]]()}</b>:", "<b style={{color:BK.coral}}>{llCap(LL_C[LL_FIVE[c][0]]())}</b>:");
// the comment over the landmarks
rep("in the royal names (High C / Low C wait for chapter 6)", "(Phase 449: middle C, treble C and bass C; high C and low C wait for chapter 6)");
fs.writeFileSync(dst, s);
console.log('ok: ' + k + ' English, ' + Object.values(KON).reduce((a, b) => a + b) + ' Korean');
