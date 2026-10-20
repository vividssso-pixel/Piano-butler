import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
# node: major on the outer ring, relative minor on the inner ring, both always shown
i0 = s.index("  const node = (i) => {"); i1 = s.index("  // the facts of the chosen scale")
s = s[:i0] + """  const node = (i, m) => {
    const L = m === 'major' ? SFD_MAJ : SFD_MIN, k = L[i], RR = m === 'major' ? 134 : 82, rr = m === 'major' ? 24 : 21, a = (-90 + i * 30) * Math.PI / 180, x = C + RR * Math.cos(a), y = C + RR * Math.sin(a);
    const on = i === idx && m === mode, pair = i === idx && !on, two = SFD_TWO[m][k], sx = m === 'minor' ? 'm' : '', col = on ? '#fffefa' : NV, fs1 = m === 'major' ? 20 : 15, fs2 = m === 'major' ? 12 : 10.5;
    return <g key={m + k} data-key={k} data-mode={m} data-on={on ? 1 : 0} transform={'translate(' + x + ' ' + y + ')'} onClick={() => pick(i, m)} onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i, m); } }} tabIndex={0} role="button" aria-label={sfdName(k, m) + ' ' + (m === 'major' ? t('major', '장조') : t('minor', '단조'))} style={{ cursor: 'pointer', outline: 'none' }}>
      <g style={{ transform: 'rotate(' + (-rot) + 'deg)', transition: tr }}>
        <circle r={rr} fill={on ? NV : '#fff'} stroke={on ? NV : pair ? CO : NV} strokeWidth={pair ? 2.2 : 1.6}/>
        {two ? <><text y={-fs2 * 0.2} textAnchor="middle" fontSize={fs2} fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{two[0] + sx}</text><text y={fs2 * 1.0} textAnchor="middle" fontSize={fs2} fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{two[1] + sx}</text></>
          : <text y={fs1 * 0.34} textAnchor="middle" fontSize={fs1} fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{prettyNote(k) + sx}</text>}
      </g>
    </g>;
  };
""" + s[i1:]
rep("const C = 170, R = 120, r = 28, tr =", "const C = 170, tr =")
rep("  const sfx = mode === 'minor' ? 'm' : '';\n", "")
# dial svg
d0 = s.index("      <circle cx={C} cy={C} r={R} fill=\"none\"", s.index("data-sfd-dial")); d1 = s.index("    </svg>", d0)
s = s[:d0] + """      <circle cx={C} cy={C} r={134} fill="none" stroke="rgba(38,41,107,0.14)" strokeWidth="1.5" strokeDasharray="3 5"/>
      <circle cx={C} cy={C} r={82} fill="none" stroke="rgba(38,41,107,0.14)" strokeWidth="1.5" strokeDasharray="3 5"/>
      <rect x={C - 31} y={C - 134 - 24 - 7} width={62} height={134 - 82 + 24 + 21 + 14} rx={31} fill="#fbe3da" stroke={CO} strokeWidth="2"/>
      <g data-sfd-rot={rot} style={{ transform: 'rotate(' + rot + 'deg)', transformOrigin: C + 'px ' + C + 'px', transition: tr }}>
        {SFD_MAJ.map((_, i) => node(i, 'major'))}{SFD_MIN.map((_, i) => node(i, 'minor'))}
      </g>
      <text x={C} y={C - 8} textAnchor="middle" fontSize={sfdName(key, mode).length > 3 ? 19 : 28} fontWeight="900" fill={NV} fontFamily="'Playfair Display', Georgia, serif">{sfdName(key, mode)}</text>
      <text x={C} y={C + 8} textAnchor="middle" fontSize="10" fontWeight="900" letterSpacing="1.2" fill="var(--muted)">{mode === 'major' ? t('MAJOR', '장조') : t('MINOR', '단조')}</text>
      <text x={C} y={C + 30} textAnchor="middle" fontSize="19" fontWeight="900" fill={CO}>{CLOCK_SIG[mode][idx] === '0' ? '' : CLOCK_SIG[mode][idx]}</text>
""" + s[d1:]
# controls: only the two steps
c0 = s.index("    <div style={{ display: 'grid', gridTemplateColumns: '1fr 2.6fr 1fr'", s.index("data-sfd-dial")); c1 = s.index("    <input value={q}", c0)
s = s[:c0] + """    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, maxWidth: 330, margin: '4px auto 6px' }}>
      <button className="chip" data-sfd-step="-1" style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => step(-1)}>{t('← one ♭ more', '← ♭ 하나 더')}</button>
      <button className="chip" data-sfd-step="1" style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => step(1)}>{t('one ♯ more →', '♯ 하나 더 →')}</button>
    </div>
""" + s[c1:]
open(b, 'w', encoding='utf-8').write(s)
