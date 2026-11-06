// Phase 450 (her 2026-10-12 19:17, on the tipped-boat thumb: '엄지가 나머지 손가락 안으로 자유롭게 인앤아웃 왔다갔다 하는것도
// 체크하는 것도 있었으면 좋겠어 팔꿈치 움직이던것 처럼 ... 손가락 각각누를 때마다 다른 손가락들은 발란스잡듯이 애니메이션으로'):
// the book's thumb picture (hand-thumb: the right hand seen from the front of the keyboard), drawn in pen so it can move.
//   d: the finger that presses (1 thumb .. 5 little finger, 0 none), dp: how far down (0..1)
//   th: the thumb in and out (0 out, playing on the side of its tip .. 1 in, under fingers 2, 3 and 4)
//   ghost: (the book's still picture) the thumb out, and where it goes in, in light coral; book: the book picture's marks
const HF_X = [0, 42, 66, 90, 114, 138];   // fingertip x of fingers 1-5; finger f plays white key f (C D E F G)
function handFront450({ d = 0, dp = 0, th = 0, nums = false, path = false, ghost = false, book = false, cap }) {
  const s = [], KX = (k) => 6 + 24 * k;
  // the keys (props: drawn straight); the key being played sinks and turns coral
  for (const k of [0, 1, 3, 4, 5, 6]) s.push({ k: 'rc', x: KX(k + 1) - 7, y: 88, w: 14, h: 16, rx: 1.5, f: PEN_N, solid: true, nw: true });
  for (let k = 0; k < 8; k++) { const down = k === d ? 3 * dp : 0;
    s.push({ k: 'rc', x: KX(k), y: 104 + down, w: 24, h: 30 - down, rx: 0, f: k === d && dp > 0.15 ? '#fbe3da' : PEN_P, s: PEN_N, sw: 1.6, nw: true }); }
  // the hand leans a little toward the finger that plays (its weight goes into that key); the others stay on their keys
  const lean = d ? dp * (HF_X[d] - 102) * 0.05 : 0, sink = d ? dp * 1.2 : 0;
  const tipY = (f) => 101 + (f === d ? 3 * dp : 0);
  const fingers = [];
  for (let f = 2; f <= 5; f++) { const cx = HF_X[f];
    fingers.push(...penLimb([[cx + lean, 52 + sink], [cx + 1.5 + lean * 0.45, 78 + sink * 0.5], [cx, tipY(f)]], 13, f === d && dp > 0.15 ? '#fbe3da' : PEN_P, PEN_N, 1.8)); }
  // the thumb: out = the book's picture (out, then the tip bends in); in = under the fingers, its tip under finger 4
  const e = pEase(Math.max(0, Math.min(1, th)));
  const mix = (a, b) => [a[0] + (b[0] - a[0]) * e, a[1] + (b[1] - a[1]) * e];
  const tb = [64 + lean, 62 + sink], tj = mix([32, 82], [74, 88]), tt = mix([42, tipY(1)], [110, 93]);
  const thumb = penLimb([tb, tj, tt], 15, d === 1 && dp > 0.15 ? '#fbe3da' : PEN_P, PEN_N, 1.9);
  const nailAng = 30 + 45 * e, nail = mix([34.5, 93], [106, 90]);
  const nailEl = { k: 'el', c: [0, 0], rx: 3.4, ry: 6.4, f: PEN_P, s: PEN_N, w: 1.3, m: [Math.cos(nailAng * Math.PI / 180), Math.sin(nailAng * Math.PI / 180), -Math.sin(nailAng * Math.PI / 180), Math.cos(nailAng * Math.PI / 180), nail[0], nail[1]] };
  s.push({ k: 'rc', x: 72 + lean, y: 4, w: 64, h: 30, rx: 0, f: PEN_N, s: PEN_N, sw: 2, ch: true });   // the sleeve, going away
  const under = e > 0.05;
  if (under) s.push(...thumb.map(x => ({ ...x, ch: true })), { ...nailEl, ch: true });   // under the fingers: they cover it
  s.push(...fingers.map(x => ({ ...x, ch: true })));
  if (!under) s.push(...thumb.map(x => ({ ...x, ch: true })));
  s.push({ k: 'rc', x: 54 + lean, y: 26 + sink, w: 98, h: 40, rx: 17, f: PEN_P, s: PEN_N, sw: 2.2, ch: true });   // the back of the hand
  for (let f = 2; f <= 5; f++) s.push({ ...penCurve([['M', [HF_X[f] - 6 + lean, 62 + sink]], ['Q', [HF_X[f] + lean, 67 + sink], [HF_X[f] + 6 + lean, 62 + sink]]], 1.2, PEN_N), ch: true });
  if (!under) s.push({ ...nailEl, ch: true });
  if (under && path) s.push({ k: 'pl', p: [tb, tj, tt], s: PEN_C, w: 17.5, op: 0.18, nw: true }, { ...penPoly([tj, tt], 1.6, PEN_C), dash: '3 2.6', nw: true });   // where the thumb is, under the fingers
  if (book) {   // the book picture's marks: the side of the tip, the tip bending in, the tipped boat
    s.push({ k: 'el', c: [40.5, 103.5], rx: 3.6, ry: 3.6, f: PEN_C, nw: true });
    s.push({ ...penCurve([['M', [16, 76]], ['Q', [12, 98], [31, 106]]], 2, PEN_C), nw: true }, { ...penCurve([['M', [26, 101]], ['L', [31, 106]], ['L', [24, 108]]], 2, PEN_C), nw: true });
    const bm = (x, y) => [170 + x * Math.cos(-24 * Math.PI / 180) - y * Math.sin(-24 * Math.PI / 180), 14 + x * Math.sin(-24 * Math.PI / 180) + y * Math.cos(-24 * Math.PI / 180)];
    s.push({ k: 'pa', seg: [['M', bm(-12, 0)], ['L', bm(12, 0)], ['L', bm(8, 6)], ['L', bm(-8, 6)], ['Z']], f: PEN_P, s: PEN_N, w: 1.6, nw: true });
    s.push({ k: 'pa', seg: [['M', bm(-1, -1)], ['L', bm(-1, -14)], ['L', bm(8, -2)], ['Z']], f: PEN_C, nw: true });
    s.push({ ...penText(44, 147, t('the side of the tip', '손끝 옆면'), { size: 9, weight: 800, anchor: 'middle' }), halo: true });
  }
  if (ghost) {   // where the thumb goes in: under fingers 2, 3 and 4
    const gb = [64, 62], gj = [74, 88], gt = [110, 93];
    s.push({ k: 'pl', p: [gb, gj, gt], s: PEN_C, w: 17.5, op: 0.2, nw: true }, { ...penPoly([gj, gt], 1.6, PEN_C), dash: '3 2.6', nw: true });
    s.push({ ...penText(150, 147, t('in and out', '들어갔다 나와요'), { size: 9, weight: 800, anchor: 'middle' }), halo: true });
  }
  if (nums) for (let f = 1; f <= 5; f++) {   // the finger numbers, the one that plays in coral
    const x = f === 1 ? 20 : HF_X[f] + lean, y = f === 1 ? 66 : 44 + sink, on = f === d && dp > 0.15;
    s.push({ k: 'el', c: [x, y], rx: 7, ry: 7, f: on ? PEN_C : PEN_P, s: on ? PEN_C : PEN_N, w: 1.4, nw: true });
    s.push(penText(x, y + 3.6, String(f), { size: 10, weight: 900, anchor: 'middle', fill: on ? '#fff' : PEN_N }));
  }
  if (cap) s.push({ ...penText(102, 147, cap, { size: 9, weight: 800, anchor: 'middle' }), halo: true });
  return s;
}
// thumb in and out: rest, in, hold, out, rest
function wuThumbTunnel(ph) {
  const p = ph == null ? 0.5 : ph;
  const th = p < 0.12 ? 0 : p < 0.42 ? (p - 0.12) / 0.3 : p < 0.6 ? 1 : p < 0.88 ? 1 - (p - 0.6) / 0.28 : 0;
  return handFront450({ th, path: true, cap: t('in under 2, 3, 4, and out', '2, 3, 4번 아래로 들어갔다 나와요') });
}
// one plays, the others balance: 1 2 3 4 5 4 3 2, each finger down and up again
const HF_SEQ = [1, 2, 3, 4, 5, 4, 3, 2];
function wuFingerBalance(ph) {
  if (ph == null) return handFront450({ d: 3, dp: 1, nums: true, cap: t('one plays, the others balance', '하나가 치고, 나머지는 균형') });
  const b = ph * HF_SEQ.length, i = Math.floor(b) % HF_SEQ.length, q = b - Math.floor(b);
  const dp = q < 0.3 ? pEase(q / 0.3) : q < 0.6 ? 1 : q < 0.85 ? 1 - pEase((q - 0.6) / 0.25) : 0;
  return handFront450({ d: HF_SEQ[i], dp, nums: true, cap: t('one plays, the others balance', '하나가 치고, 나머지는 균형') });
}
// the book's still picture (page 4): the thumb on the side of its tip, and where it goes in (her 2026-10-12 21:17 '응')
function thumbBook450() { return handFront450({ book: true, ghost: true }); }
const THUMB_MOVES = [
  { id: 'tunnel', who: '', vb: [0, 0, 204, 152], ms: 3600, f: wuThumbTunnel },
  { id: 'balance', who: '', vb: [0, 0, 204, 152], ms: 5600, f: wuFingerBalance },
];
function ThumbMoves450() {
  const cards = [
    [t('Thumb in and out', '엄지 인앤아웃'), t('Check the thumb is free: it slides in under fingers 2, 3 and 4, and back out. The hand stays round and still.', '엄지가 자유로운지 확인해요: 2, 3, 4번 손가락 아래로 쏙 들어갔다가 다시 나와요. 손은 둥글게, 가만히 있어요.')],
    [t('One plays, four balance', '하나가 치고, 넷이 균형'), t('One finger at a time goes down into its key. The others rest on their keys and keep the hand balanced.', '한 번에 한 손가락씩 건반 속으로 내려가요. 나머지 손가락은 자기 건반 위에 가만히 얹혀서 손의 균형을 잡아요.')],
  ];
  const [seed, setSeed] = useState({});
  return (
    <div data-thumb-moves style={{display:'grid',gridTemplateColumns:'repeat(auto-fill, minmax(min(100%, 220px), 1fr))',gap:14,margin:'4px 0 8px'}}>
      {THUMB_MOVES.map((w, i) => (
        <div key={w.id} data-thumb-move={w.id} style={{border:'1px solid #ece6d8',borderRadius:12,padding:'8px 10px 10px',display:'flex',flexDirection:'column',gap:5}}>
          <button onClick={() => setSeed(x => ({ ...x, [w.id]: (x[w.id] || 0) + 1 }))} aria-label={t('Watch from the start: ', '처음부터 보기: ') + cards[i][0]}
            style={{background:BK.soft,border:'none',borderRadius:8,height:160,display:'flex',alignItems:'center',justifyContent:'center',overflow:'hidden',padding:0,cursor:'pointer'}}>
            <WarmPic key={(seed[w.id] || 0)} w={w} h={150}/>
          </button>
          <div style={{fontFamily:LB_SERIF,fontSize:16.5,fontWeight:800,color:BK.ink}}>{cards[i][0]}</div>
          <div style={{fontSize:13.5,color:BK.ink,lineHeight:1.4}}>{cards[i][1]}</div>
        </div>))}
    </div>
  );
}
