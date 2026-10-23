import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build B (her calls 2026-10-23): intervals and chords count the keys between (her own method);
# chords gain diminished / augmented triads and 7th chords; I IV V becomes I IV V7; inversions take 7th chords.

# ── re-splice the three lesson files (kq, iv, ch) at their markers
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'iv.jsx', encoding='utf-8').read() + "\n" + open(SC + 'ch.jsx', encoding='utf-8').read() + s[j:]

# ── 1. ScKeys: spans = brackets over a run of keys with a count on top ([first, last, label, colour]; last < first = no keys, label only)
rep("function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol, nums, ring, mw, oct, clean, inKey, plain }) {",
    "function ScKeys({ marks, onTap, arcs, spans, nonce, names, ks, ncol, nums, ring, mw, oct, clean, inKey, plain }) {")
rep("""    </g>; });
  return (<div style={{maxWidth:mw || 330,margin:'0 auto'}}>""",
    """    </g>; });
  const brackets = (spans || []).map(([a, b, lab, col], j) => { const c = col || '#26296b', xa = white(a) ? kx(a) - 16 : kx(a) - 10, xb = white(b) ? kx(b) + 16 : kx(b) + 10, xm = b < a ? (kx(a) + kx(b)) / 2 : (xa + xb) / 2;
    return <g key={'sp' + j + ':' + a + ':' + b + ':' + nonce} style={{pointerEvents:'none',animation:'fadeUp 0.3s both'}}>
      {b >= a && <path d={'M' + xa + ',-3 V-12 H' + xb + ' V-3'} fill="none" stroke={c} strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"/>}
      <text x={xm} y="-17" textAnchor="middle" fontSize="18" fontWeight="900" fill={c} style={{fontVariantNumeric:'tabular-nums'}}>{lab}</text></g>; });
  return (<div style={{maxWidth:mw || 330,margin:'0 auto'}}>""")
rep("overlay={<g aria-hidden=\"true\">{arrows}{Object.entries(inKey ? {} : (names || {}))",
    "overlay={<g aria-hidden=\"true\">{brackets}{arrows}{Object.entries(inKey ? {} : (names || {}))")

# ── 2. Chords on the Home: three groups, the middle one now all the kinds of chords
rep("    { id: 'ch-majmin', en: 'Major and minor', ko: '장3화음과 단3화음', lessons: ['ch-mm', 'ch-ear'], check: 'chords', level: 3 },",
    "    { id: 'ch-kinds', en: 'Kinds of chords', ko: '화음의 종류', lessons: ['ch-mm', 'ch-da', 'ch-7th', 'ch-ear'], check: 'chords', level: 3 },")

# ── 3. chord drill levels point at the new lesson numbers (1 stack, 2 staff, 3 hands, 4 mm, 5 dim/aug, 6 7th, 7 ear, 8 tonic, 9 I IV V7, 10 inversions)
for kind, old, new in [('mm', '4', '4'), ('ear', '5', '7'), ('tonic', '6', '8'), ('roman', '7', '9'), ('spellR', '7', '9')]:
    a = "num: '" + old + "'"
    i = s.index("const CHX_LEVELS = ["); j = s.index("];", i)
    blk = s[i:j]; k = blk.index("kind: '" + kind + "'"); ls = blk.rindex("\n", 0, k); le = blk.index("\n", k)
    line = blk[ls:le]; assert a in line, (kind, line[:80])
    s = s[:i] + blk[:ls] + line.replace(a, "num: '" + new + "'") + blk[le:] + s[j:]

open(dst, 'w', encoding='utf-8').write(s); print('ok')
