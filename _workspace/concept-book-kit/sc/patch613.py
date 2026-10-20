import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:80])
    s = s.replace(x, y)
# ScKeys: optional width and octave count
rep("function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol, nums, ring }) {", "function ScKeys({ marks, onTap, arcs, nonce, names, ks, ncol, nums, ring, mw, oct }) {")
rep("  return (<div style={{maxWidth:330,margin:'0 auto'}}>\n    <TapKeyboard octaves={2} extraC labels={arcs.length ? 'white' : 'all'}", "  return (<div style={{maxWidth:mw || 330,margin:'0 auto'}}>\n    <TapKeyboard octaves={oct || 2} extraC labels={arcs.length ? 'white' : 'all'}")
# the staff button
rep("t('Hide the staff', '오선 숨기기') : t('Write it on the staff', '오선에 써 보기')", "t('Hide the staff', '스태프 숨기기') : t('Show on the staff', '스태프로 보여주기')")
# the finder: one pair of keyboards (the lessons' look; coral = a group of 3, blue = a group of 4), no second keyboard
i = s.index("      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={mode + key + form}/>\n      {noteDown")
j = s.index("      <ScStaffBtn on={stf} set={setStf}/>\n      {stf && (staff ?")
NEW = r'''      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2,minmax(0,1fr))', gap: 6, maxWidth: 330, margin: '8px auto 6px' }}>
        {[1, 2].map(n => <button key={n} className={'chip' + (oct === n ? ' active' : '')} aria-pressed={oct === n} style={{ ...KF_BTN, minHeight: 38 }} onClick={() => setOct(n)}>{n === 1 ? t('1 octave', '1옥타브') : t('2 octaves', '2옥타브')}</button>)}
      </div>
      {clash ? <>
        <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={mode + key + form} mw={520}/>
        <p style={{ fontSize: 13, color: 'var(--muted)', margin: '8px 0 0', textAlign: 'center', lineHeight: 1.5 }}>{t('No finger numbers for this form: the harmonic fingering would put a thumb on a black key. Look the fingering up in your book.', '이 형태는 손가락 번호를 보여 주지 않아요: 화성 단음계의 손가락 번호로는 엄지가 검은건반에 놓여요. 책에서 찾아보세요.')}</p></>
        : (() => { const e = mode === 'major' ? info.octaves[oct] : fing, KK = offs.map(o => info.rootPc + o), kn = mode === 'major' ? key : 'm' + key;
          const paint = (hand) => { const F = e[hand], mk = {}, nm = {}, nc = {}; scRuns(kn, hand, F).forEach(g => { for (let q = g.from; q < g.from + g.len; q++) { mk[KK[q]] = g.kind === 3 ? 'target' : g.kind === 4 ? 'fof' : 'pass'; nc[KK[q]] = g.kind === 3 ? SC_G3 : g.kind === 4 ? SC_G4 : '#26296b'; } }); F.forEach((f, q) => { nm[KK[q]] = String(f); }); return { mk, nm, nc }; };
          const row = (hand, label) => { const P = paint(hand); return <div style={{ marginTop: hand === 'RH' ? 4 : 10 }}>
            <div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', marginBottom: 2 }}>{label}</div>
            <div style={{ overflowX: 'auto' }}><div style={{ minWidth: oct === 2 ? 640 : 0 }}><ScKeys nums ks={KK} marks={P.mk} names={P.nm} ncol={P.nc} arcs={[]} nonce={hand + key + mode + form + oct} mw={oct === 2 ? 640 : 520} oct={oct === 2 ? 3 : 2}/></div></div></div>; };
          return <div data-sfd-fing>
            {row('RH', t('RIGHT HAND', '오른손'))}{row('LH', t('LEFT HAND', '왼손'))}
            <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', marginTop: 8, fontSize: 12.5, fontWeight: 800, color: '#26296b' }}>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: '#fbe3da', border: '1.5px solid #e4572e' }}/>{t('1-2-3', '1-2-3')}</span>
              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: '#dfe9f8', border: '1.5px solid #3b4fa8' }}/>{t('1-2-3-4', '1-2-3-4')}</span>
            </div>
          </div>; })()}
      {noteDown && <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, margin: '6px 0' }}>{noteDown}</div>}
'''
s = s[:i] + NEW + s[j:]
open(b, 'w', encoding='utf-8').write(s); print('ok')
