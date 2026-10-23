import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build G: Rhythm group 5 'More rhythm' (semiquavers, triplets, 6/8 counted in quavers as she does, 2/2, syncopation, swing).
# The rhythm chapter's renderer learns (all optional, defaults unchanged): a time signature's bottom number, triplets ('t3'),
# three quavers beamed in 6/8 ('e3'), and counts / hearts every o.countStep / o.heartStep with o.countFn.
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + "\n".join(open(SC + f, encoding='utf-8').read() for f in ['iv.jsx', 'ch.jsx', 'pg.jsx', 'rq.jsx', 'rq2.jsx', 'rq3.jsx']) + s[j:]

rep("const SRH_LEN = { q: 1, h: 2, hd: 3, w: 4, qd: 1.5, e: 0.5, er: 0.5, p: 1, p4: 2, s4: 1, r: 1, hr: 2 };", "const SRH_LEN = { q: 1, h: 2, hd: 3, w: 4, qd: 1.5, e: 0.5, er: 0.5, p: 1, p4: 2, s4: 1, r: 1, hr: 2, t3: 1, e3: 1.5 };")
rep("const SRH_HEADS = { p: 2, p4: 4, s4: 4 };", "const SRH_HEADS = { p: 2, p4: 4, s4: 4, t3: 3, e3: 3 };")
rep("const srhW = (k, len, D, wide) => k === 'box' ?", "const srhW = (k, len, D, wide) => k === 't3' ? Math.max(D, 80) : k === 'e3' ? Math.max(1.5 * D, 84) : k === 'box' ?")
rep("    if (k === 'ts') { [[it[1], G(36)], [4, G(32)]].forEach(", "    if (k === 'ts') { [[it[1], G(36)], [it[2] || 4, G(32)]].forEach(")
rep("    else if (SRH_HEADS[k]) out.push(srhGroup(mine.map(([, i]) => soundX[i]), y, mine.map(([s]) => c(s.h)), k === 's4' ? 2 : 1, o.hl === j ? cor : col));",
    "    else if (SRH_HEADS[k]) { out.push(srhGroup(mine.map(([, i]) => soundX[i]), y, mine.map(([s]) => c(s.h)), k === 's4' ? 2 : 1, o.hl === j ? cor : col)); if (k === 't3') { const xa = soundX[mine[0][1]], xb = soundX[mine[mine.length - 1][1]]; out.push('<text x=\"' + pFix((xa + xb) / 2 + 6.4) + '\" y=\"' + pFix(y - 36.5) + '\" text-anchor=\"middle\" font-family=\"Playfair Display, Georgia, serif\" font-style=\"italic\" font-size=\"13\" font-weight=\"900\" fill=\"' + col + '\">3</text>'); } }")
rep("      mine.forEach(([s, i]) => cells.push({ x: soundX[i], tx: srhCount(s.b - barB),", "      mine.forEach(([s, i]) => cells.push({ x: soundX[i], tx: (o.countFn || srhCount)(s.b - barB),")
rep("""      for (let P = Math.ceil(b - barB - 1e-6); P < b + len - barB - 1e-6; P++) { const B = P + barB, at = mine.find(([s]) => Math.abs(s.b - B) < 1e-6), bx = at ? soundX[at[1]] : nx + (B - b) / len * w;
        beats.push(bx); if (!at) cells.push({ x: bx, tx: srhCount(P), si: -1, rest: srhRest(k), light: !srhRest(k) }); }""",
    """      const cs = o.countStep || 1, hs = o.heartStep || cs;
      for (let P = Math.ceil((b - barB) / cs - 1e-6) * cs; P < b + len - barB - 1e-6; P += cs) { const B = P + barB, at = mine.find(([s]) => Math.abs(s.b - B) < 1e-6), bx = at ? soundX[at[1]] : nx + (B - b) / len * w;
        if (Math.abs(P / hs - Math.round(P / hs)) < 1e-6) beats.push(bx); if (!at) cells.push({ x: bx, tx: (o.countFn || srhCount)(P), si: -1, rest: srhRest(k), light: !srhRest(k) }); }""")

rep("""    { id: 'rb-patterns', en: 'Rhythm patterns', ko: '리듬 패턴', lessons: ['rp-beams', 'rp-alone', 'rp-dot', 'rp-up', 'rp-read'], check: 'rhythm' },
""", """    { id: 'rb-patterns', en: 'Rhythm patterns', ko: '리듬 패턴', lessons: ['rp-beams', 'rp-alone', 'rp-dot', 'rp-up', 'rp-read'], check: 'rhythm' },
    { id: 'rb-more', en: 'More rhythm', ko: '더 나아가는 리듬', lessons: ['rm-semi', 'rm-trip', 'rm-68', 'rm-cut', 'rm-sync', 'rm-swing'], check: 'time-signatures', level: 9 },
""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
