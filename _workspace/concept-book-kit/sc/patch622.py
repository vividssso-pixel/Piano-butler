import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
rep("gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: 5, maxWidth: 330, margin: '4px auto 6px' }}>", "gridTemplateColumns: '1fr 2.6fr 1fr', gap: 5, maxWidth: 330, margin: '4px auto 6px', alignItems: 'center' }}>")
old = s[s.index("      {['major', 'minor'].map(m => <button key={m} className={'chip'"):s.index("      <button className=\"chip\" data-sfd-step=\"1\"")]
new = """      <div style={{ display: 'grid', gridTemplateColumns: '1fr auto 1fr', gap: 4, alignItems: 'center' }}>
        <button className={'chip' + (mode === 'major' ? ' active' : '')} aria-pressed={mode === 'major'} style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => pick(idx, 'major')}>{t('Major', '장조')}</button>
        <div data-sfd-rel aria-hidden="true" style={{ textAlign: 'center', fontSize: 10, fontWeight: 900, color: CO, lineHeight: 1.1, minWidth: 44 }}><div style={{ fontSize: 15 }}>⇄</div>{t('relative', '나란한 조')}</div>
        <button className={'chip' + (mode === 'minor' ? ' active' : '')} aria-pressed={mode === 'minor'} style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => pick(idx, 'minor')}>{t('Minor', '단조')}</button>
      </div>
"""
s = s.replace(old, new)
rep("""        <button className="ghost-btn" style={scS.prim} data-sfd-rel onClick={() => pick(idx, relMode)}>{mode === 'major' ? t('Relative minor →', '나란한 단조 →') : t('Relative major →', '나란한 장조 →')}</button>\n""", "")
open(b, 'w', encoding='utf-8').write(s)
