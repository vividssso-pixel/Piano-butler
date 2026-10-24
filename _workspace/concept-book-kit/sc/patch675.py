import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build M (her question 2026-10-24 11:34, "why only D?"): Three kinds of minor keeps its explanation on D (her card), and its
# Your turn lets her pick the minor key: C, C♯, D, E, F, F♯, G, A, B♭, B (her minor keys, from C up; G♯ and D♯ minor wait,
# their raised 7th is a double sharp the staff cannot draw yet). The keys, names, staff and key signature follow the key.
# the staff for any minor key, in the keyboard's octave (C4 to B4 start): the notes from the tonic, a sign wherever the note is not what the key signature says
rep("""function scMinItems(form, dir) {
  const up = [29, 30, 31, 32, 33, 34, 35, 36], idx = dir === 'up' ? up : up.slice().reverse();
  const sign = (j) => form === 'harmonic' && j === 6 ? '#' : form === 'melodic' && dir === 'up' && j === 5 ? 'n' : form === 'melodic' && dir === 'up' && j === 6 ? '#' : null;
  return idx.map((d, q) => { const j = dir === 'up' ? q : 7 - q, sg = sign(j); return sg ? ['q', 1, d, sg] : ['q', 1, d]; }).concat([['||']]);
}""", """function scMinItems(form, dir, key = 'D') {
  const L = 'CDEFGAB'.indexOf(key[0]), d0 = 28 + L, up = Array.from({ length: 8 }, (_, j) => d0 + j), idx = dir === 'up' ? up : up.slice().reverse();
  const KS = KEY_SIGS.find(x => x.minor === key), sig = !KS || !KS.type ? [] : (KS.type === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, KS.count);
  const nm = spellMinor(key, form === 'melodic' && dir === 'down' ? 'natural' : form), acc = (n) => n.length > 1 ? n.slice(1) : '';
  const sign = (j) => { const n = nm[j % 7], a = acc(n), ka = acc(sig.find(x => x[0] === n[0]) || n[0]); return a === ka ? null : a === '' ? 'n' : a; };
  return idx.map((d, q) => { const j = dir === 'up' ? q : 7 - q, sg = sign(j); return sg ? ['q', 1, d, sg] : ['q', 1, d]; }).concat([['||']]);
}
const scMinRel = (key) => (KEY_SIGS.find(x => x.minor === key) || { major: 'F' }).major;
const SC_MINK = ['C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'A', 'Bb', 'B'];""")
rep("""  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [fm, setFm] = useState('harmonic'), [at, setAt] = useState(0), [bad, setBad] = useState(null);
  const P = useScPlay([view, i, fm]);""", """  const [i, setI] = useState(0), [nonce, setNonce] = useState(0), [fm, setFm] = useState('harmonic'), [at, setAt] = useState(0), [bad, setBad] = useState(null), [mkey, setMkey] = useState('D');
  const P = useScPlay([view, i, fm, mkey]);""")
rep("""  const mk = (f) => { const stp = MINOR_FORMS[f].steps, K = stp.map(x => 2 + x).concat([14]), N = spellMinor('D', f).map(prettyAny).concat(['D']), marks = {}, names = {};""",
    """  const mk = (f, key = 'D') => { const r0 = MINOR_SCALES[key].rootPc, stp = MINOR_FORMS[f].steps, K = stp.map(x => r0 + x).concat([r0 + 12]), N = spellMinor(key, f).map(prettyAny).concat([prettyNote(key)]), marks = {}, names = {};""")
rep("""    const M = mk(fm), K = M.K, D = fm === 'melodic' ? mk('natural') : M,""", """    const M = mk(fm, mkey), K = M.K, D = fm === 'melodic' ? mk('natural', mkey) : M, KN = prettyNote(mkey), rel = scMinRel(mkey),
      itU = scMinItems(fm, 'up', mkey), shown = (j) => { const it = itU[j], n = M.N[j]; return it && it[3] === 'n' ? n + '♮' : n; },""")
rep("""done ? (fm === 'melodic' ? t('That is D melodic minor: up with B♮ and C♯, down as the natural minor.', 'D 가락 단음계예요: 올라갈 때는 B♮과 C♯, 내려올 때는 자연 단음계예요.') : t('That is D ' + fl.toLowerCase() + ' minor, up and down.', 'D ' + fl + ' 단음계를 올라가고 내려왔어요.'))""",
    """done ? (fm === 'melodic' ? t('That is ' + KN + ' melodic minor: up with ' + shown(5) + ' and ' + shown(6) + ', down as the natural minor.', KN + ' 가락 단음계예요: 올라갈 때는 ' + shown(5) + '과 ' + shown(6) + ', 내려올 때는 자연 단음계예요.') : t('That is ' + KN + ' ' + fl.toLowerCase() + ' minor, up and down.', KN + ' ' + fl + ' 단음계를 올라가고 내려왔어요.'))""")
rep("""prettyAny(spellMinor('D', 'melodic')[bad === K[5] ? 5 : 6]) + '.', '그 건반이 아니에요. 내려올 때 가락 단음계는 자연 단음계를 쳐요: ' + prettyAny(spellMinor('D', 'melodic')[bad === K[5] ? 5 : 6])""",
    """prettyAny(spellMinor(mkey, 'melodic')[bad === K[5] ? 5 : 6]) + '.', '그 건반이 아니에요. 내려올 때 가락 단음계는 자연 단음계를 쳐요: ' + prettyAny(spellMinor(mkey, 'melodic')[bad === K[5] ? 5 : 6])""")
rep("""      : at === 0 ? t('Start on D. Then tap ' + word(0) + '.', 'D에서 시작해요. 그다음 ' + word(0) + ' 건반을 눌러요.')
      : at === 7 ? (fm === 'melodic' ? t('Now come back down. Melodic minor comes down as the natural minor. From D, tap ' + word(at) + '.', '이제 내려와요. 가락 단음계는 내려올 때 자연 단음계예요. D에서 ' + word(at) + ' 건반을 눌러요.') : t('Now come back down. From D, tap ' + word(at) + '.', '이제 내려와요. D에서 ' + word(at) + ' 건반을 눌러요.'))""",
    """      : at === 0 ? t('Start on ' + KN + '. Then tap ' + word(0) + '.', KN + '에서 시작해요. 그다음 ' + word(0) + ' 건반을 눌러요.')
      : at === 7 ? (fm === 'melodic' ? t('Now come back down. Melodic minor comes down as the natural minor. From ' + KN + ', tap ' + word(at) + '.', '이제 내려와요. 가락 단음계는 내려올 때 자연 단음계예요. ' + KN + '에서 ' + word(at) + ' 건반을 눌러요.') : t('Now come back down. From ' + KN + ', tap ' + word(at) + '.', '이제 내려와요. ' + KN + '에서 ' + word(at) + ' 건반을 눌러요.'))""")
rep("""      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {SC_MF.map(f => <button key={f} className={'chip' + (fm === f ? ' active' : '')} aria-pressed={fm === f} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setFm(f); setAt(0); setBad(null); setNonce(n => n + 1); playKey(2, 0.5); }}>{MINOR_FORMS[f].label}</button>)}
      </div>""", """      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:5,maxWidth:330,margin:'0 auto 6px'}}>
        {SC_MINK.map(k => <button key={k} className={'chip' + (mkey === k ? ' active' : '')} aria-pressed={mkey === k} style={{...KF_BTN,minHeight:38,padding:'0 2px',fontSize:14}} onClick={() => { clear(); setMkey(k); setAt(0); setBad(null); setNonce(n => n + 1); playKey(MINOR_SCALES[k].rootPc, 0.5); }}>{prettyNote(k)}</button>)}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:330,margin:'0 auto 6px'}}>
        {SC_MF.map(f => <button key={f} className={'chip' + (fm === f ? ' active' : '')} aria-pressed={fm === f} style={{...KF_BTN,minHeight:40,padding:'0 4px'}} onClick={() => { clear(); setFm(f); setAt(0); setBad(null); setNonce(n => n + 1); playKey(MINOR_SCALES[mkey].rootPc, 0.5); }}>{MINOR_FORMS[f].label}</button>)}
      </div>""")
rep("""      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + fm} onTap={tap}/>
      {(() => {   // the staff with its key signature (B♭); each note appears as she taps it: key-signature notes green, accidentals coral
        const dn = at >= 7 && go, cnt = dn ? at - 6 : at + 1, all = scMinItems(fm, dn ? 'down' : 'up'), items = all.slice(0, cnt).concat([['||']]);
        const acc = dn ? (fm === 'harmonic' ? [1] : []) : (fm === 'harmonic' ? [6] : fm === 'melodic' ? [5, 6] : []), ks = dn ? [2] : (fm === 'melodic' ? [] : [5]);
        const on = (l) => l.filter(j => j < cnt);
        return <SkgStaff key={'tr' + fm + (dn ? 'd' : 'u') + cnt} items={items} k="F" width={330} o={{ boxS: 26, D: 30, hl: on(acc), hl2: on(ks), signHl: on(acc), underAlt: on(ks), ksCol: '#2e8a6e', ...skgUnder(items, 'F', null, on(acc)) }}/>;
      })()}""", """      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + fm + mkey} onTap={tap}/>
      {(() => {   // the staff with the key's key signature; each note appears as she taps it: key-signature notes green, accidentals coral
        const dn = at >= 7 && go, cnt = dn ? at - 6 : at + 1, all = scMinItems(fm, dn ? 'down' : 'up', mkey), items = all.slice(0, cnt).concat([['||']]);
        const sigL = skgSigns(rel).map(([, l]) => l), acc = all.map((it, j) => it[3] ? j : -1).filter(j => j >= 0), ks = all.map((it, j) => it[2] != null && !it[3] && sigL.includes('CDEFGAB'[((it[2] % 7) + 7) % 7]) ? j : -1).filter(j => j >= 0);
        const on = (l) => l.filter(j => j < cnt);
        return <SkgStaff key={'tr' + fm + mkey + (dn ? 'd' : 'u') + cnt} items={items} k={rel} width={330} o={{ boxS: 26, D: 30, hl: on(acc), hl2: on(ks), signHl: on(acc), underAlt: on(ks), ksCol: '#2e8a6e', ...skgUnder(items, rel, null, on(acc)) }}/>;
      })()}""")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
