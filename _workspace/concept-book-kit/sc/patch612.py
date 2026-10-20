import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def cut(start, end, new):
    global s
    i = s.index(start); j = s.index(end, i) + len(end)
    assert s.count(start) == 1
    s = s[:i] + new + s[j:]
# 1. one ring of twelve (the Major / Minor chips swap its labels), the relative key in the centre
NEWDIAL = r'''  const C = 170, R = 120, r = 28, tr = 'transform 0.7s cubic-bezier(0.3,0.7,0.2,1)';
  const sfx = mode === 'minor' ? 'm' : '';
  const node = (i) => {
    const k = list[i], a = (-90 + i * 30) * Math.PI / 180, x = C + R * Math.cos(a), y = C + R * Math.sin(a), on = i === idx, two = SFD_TWO[mode][k], col = on ? '#fffefa' : NV;
    return <g key={k} data-key={k} data-mode={mode} data-on={on ? 1 : 0} transform={'translate(' + x + ' ' + y + ')'} onClick={() => pick(i, mode)} onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i, mode); } }} tabIndex={0} role="button" aria-label={sfdName(k, mode) + ' ' + (mode === 'major' ? t('major', '장조') : t('minor', '단조'))} style={{ cursor: 'pointer', outline: 'none' }}>
      <g style={{ transform: 'rotate(' + (-rot) + 'deg)', transition: tr }}>
        <circle r={r} fill={on ? NV : '#fff'} stroke={NV} strokeWidth="1.6"/>
        {two ? <><text y={-2} textAnchor="middle" fontSize="13" fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{two[0] + sfx}</text><text y={13} textAnchor="middle" fontSize="13" fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{two[1] + sfx}</text></>
          : <text y={7} textAnchor="middle" fontSize="21" fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{prettyNote(k) + sfx}</text>}
      </g>
    </g>;
  };
'''
cut("  const C = 170, RO = 132, RI = 84, ro = 22, ri = 20, tr = 'transform 0.7s cubic-bezier(0.3,0.7,0.2,1)';\n", "    </g>;\n  };\n", NEWDIAL)
cut("      <circle cx={C} cy={C} r={RO} fill=\"none\"", "{t('♯ →', '♯ →')}</text>\n", r'''      <circle cx={C} cy={C} r={R} fill="none" stroke="rgba(38,41,107,0.14)" strokeWidth="1.5" strokeDasharray="3 5"/>
      <rect x={C - r - 7} y={C - R - r - 7} width={2 * r + 14} height={2 * r + 14} rx={r + 7} fill="#fbe3da" stroke={CO} strokeWidth="2"/>
      <g data-sfd-rot={rot} style={{ transform: 'rotate(' + rot + 'deg)', transformOrigin: C + 'px ' + C + 'px', transition: tr }}>
        {list.map((_, i) => node(i))}
      </g>
      <text x={C} y={C - 20} textAnchor="middle" fontSize={sfdName(key, mode).length > 3 ? 21 : 30} fontWeight="900" fill={NV} fontFamily="'Playfair Display', Georgia, serif">{sfdName(key, mode)}</text>
      <text x={C} y={C - 2} textAnchor="middle" fontSize="11" fontWeight="900" letterSpacing="1.2" fill="var(--muted)">{mode === 'major' ? t('MAJOR', '장조') : t('MINOR', '단조')}</text>
      <text x={C} y={C + 26} textAnchor="middle" fontSize="22" fontWeight="900" fill={CO}>{CLOCK_SIG[mode][idx] === '0' ? '' : CLOCK_SIG[mode][idx]}</text>
      <text x={C} y={C + 48} textAnchor="middle" fontSize="12" fontWeight="800" fill="var(--muted)">{t('relative ', '나란한 ') + sfdName(relKey, relMode) + (relMode === 'minor' ? 'm' : '')}</text>
      <text x={C - 40} y={C + 72} textAnchor="middle" fontSize="11" fontWeight="900" fill={CO}>← ♭</text>
      <text x={C + 40} y={C + 72} textAnchor="middle" fontSize="11" fontWeight="900" fill={CO}>♯ →</text>
''')
# 2. fingering on two keyboards, with the 1-2-3 / 1-2-3-4 colours on the keys
cut("      {clash ? <p style={{ fontSize: 13", "nms={nms}/>}\n", r'''      {clash ? <p style={{ fontSize: 13, color: 'var(--muted)', margin: '8px 0 0', textAlign: 'center', lineHeight: 1.5 }}>{t('No finger numbers for this form: the harmonic fingering would put a thumb on a black key. Look the fingering up in your book.', '이 형태는 손가락 번호를 보여 주지 않아요: 화성 단음계의 손가락 번호로는 엄지가 검은건반에 놓여요. 책에서 찾아보세요.')}</p>
        : (() => { const e = mode === 'major' ? info.octaves[oct] : fing, nmz = mode === 'major' ? spellScale(key) : spellMinor(key, form), nz = nmz.concat([nmz[0]]);
          return <div data-sfd-fing>
            <div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', margin: '4px 0' }}>{t('RIGHT HAND', '오른손')}</div>
            <ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={e.RH} hand="RH" names={nz}/>
            <div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', margin: '10px 0 4px' }}>{t('LEFT HAND', '왼손')}</div>
            <ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={e.LH} hand="LH" names={nz}/>
            <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', marginTop: 8, fontSize: 12.5, fontWeight: 800, color: '#26296b' }}>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: SEGMENT_COLORS.three.fill, border: '1.5px solid ' + SEGMENT_COLORS.three.stroke }}/>1-2-3</span>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: SEGMENT_COLORS.four.fill, border: '1.5px solid ' + SEGMENT_COLORS.four.stroke }}/>1-2-3-4</span>
            </div>
          </div>; })()}
''')
open(b, 'w', encoding='utf-8').write(s); print('ok')
