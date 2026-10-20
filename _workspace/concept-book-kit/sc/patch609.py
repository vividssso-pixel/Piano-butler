import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:80])
    s = s.replace(x, y)

# 1. ScPair can show a minor key's fingering (fing = {RH, LH}, nms = the seven names)
rep("function ScPair({ keyName, n, hideLH, cur }) {\n  const FR = scFingers(keyName, 'RH', n), FL = scFingers(keyName, 'LH', n), cols = FR.length, base = spellScale(keyName).map(prettyNote), top = prettyNote(keyName);",
    "function ScPair({ keyName, n, hideLH, cur, fing, nms }) {\n  const FR = fing ? fing.RH : scFingers(keyName, 'RH', n), FL = fing ? fing.LH : scFingers(keyName, 'LH', n), cols = FR.length, base = nms || spellScale(keyName).map(prettyNote), top = nms ? nms[0] : prettyNote(keyName);")

# 2. the new finder
NEW = r'''
// ── The Scale finder, on the circle of fifths: a dial that turns so the chosen key stands at the top ──
const SFD_MAJ = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F'];
const SFD_MIN = ['A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'Bb', 'F', 'C', 'G', 'D'];
const SFD_TWO = {
  major: { Gb: ['F♯', 'G♭'], Db: ['C♯', 'D♭'], Ab: ['G♯', 'A♭'], Eb: ['D♯', 'E♭'], Bb: ['A♯', 'B♭'] },
  minor: { 'F#': ['F♯', 'G♭'], 'C#': ['C♯', 'D♭'], 'G#': ['G♯', 'A♭'], 'D#': ['D♯', 'E♭'], Bb: ['A♯', 'B♭'] },
};
const SFD_SIGKEY = (key, mode) => mode === 'major' ? key : key === 'D#' ? 'F#' : SFD_MAJ[SFD_MIN.indexOf(key)];   // the major key whose signature the scale uses
function sfdNorm(key, mode) {
  const M = { 'F#': 'Gb', 'C#': 'Db', 'A#': 'Bb', 'D#': 'Eb', 'G#': 'Ab', Cb: 'B' }, m = { Db: 'C#', Gb: 'F#', Ab: 'G#', Eb: 'D#', 'A#': 'Bb' };
  return mode === 'minor' ? (SFD_MIN.includes(key) ? key : (m[key] || 'A')) : (SFD_MAJ.includes(key) ? key : (M[key] || 'C'));
}
const sfdName = (key, mode) => SFD_TWO[mode][key] ? SFD_TWO[mode][key].join(' / ') : prettyNote(key);
// natural or raised minor on the treble staff, with the key signature of its relative major; null when a note would need a double sharp
function sfdMinItems(key, form) {
  const L = 'CDEFGAB', d0 = key[0] === 'B' ? 27 : 28 + L.indexOf(key[0]), nat = spellMinor(key, 'natural'), cur = spellMinor(key, form), coral = [];
  const items = [];
  for (let j = 0; j < 8; j++) {
    const d = d0 + j, raised = j < 7 && cur[j] !== nat[j];
    if (!raised) { items.push(['q', 1, d]); continue; }
    const n0 = nat[j], sg = n0.endsWith('b') ? 'n' : n0.endsWith('#') ? null : '#';
    if (!sg) return null;
    coral.push(j); items.push(['q', 1, d, sg]);
  }
  return { items: items.concat([['||']]), coral };
}
function ScaleFinderDial() {
  const [init] = useState(() => {
    let p = PENDING_SCALE;
    if (!p) { try { const q = new URLSearchParams(location.search), kk = q.get('key'); if (kk) p = parseScaleQuery(kk + (q.get('mode') === 'minor' ? ' minor' : '')); } catch (e) { p = null; } }
    p = p || { key: 'C', mode: 'major' };
    return { mode: p.mode, key: sfdNorm(p.key, p.mode) };
  });
  useEffect(() => { PENDING_SCALE = null; }, []);
  const [mode, setMode] = useState(init.mode), [key, setKey] = useState(init.key);
  const [form, setForm] = useState('harmonic'), [oct, setOct] = useState(1), [stf, setStf] = useState(false), [q, setQ] = useState('');
  const idx0 = (init.mode === 'major' ? SFD_MAJ : SFD_MIN).indexOf(init.key);
  const [rot, setRot] = useState(-idx0 * 30);
  const list = mode === 'major' ? SFD_MAJ : SFD_MIN, idx = Math.max(0, list.indexOf(key));
  const pick = (i, m) => { setMode(m); setKey((m === 'major' ? SFD_MAJ : SFD_MIN)[i]); setRot(r => r + ((((-i * 30 - r) % 360) + 540) % 360 - 180)); setQ(''); };
  const search = (v) => { setQ(v); const r = parseScaleQuery(v); if (r) { const m = r.mode, k = sfdNorm(r.key, m); pick((m === 'major' ? SFD_MAJ : SFD_MIN).indexOf(k), m); setQ(v); } };
  const miss = q && !parseScaleQuery(q);
  const C = 170, RO = 132, RI = 84, ro = 22, ri = 20, tr = 'transform 0.7s cubic-bezier(0.3,0.7,0.2,1)';
  const node = (i, m) => {
    const k = (m === 'major' ? SFD_MAJ : SFD_MIN)[i], a = (-90 + i * 30) * Math.PI / 180, R = m === 'major' ? RO : RI, r = m === 'major' ? ro : ri;
    const x = C + R * Math.cos(a), y = C + R * Math.sin(a), on = i === idx && m === mode, two = SFD_TWO[m][k], sfx = m === 'minor' ? 'm' : '';
    const fs = m === 'major' ? 17 : 14, fs2 = m === 'major' ? 11.5 : 10.5, col = on ? '#fffefa' : NV;
    return <g key={m + k} data-key={k} data-mode={m} data-on={on ? 1 : 0} transform={'translate(' + x + ' ' + y + ')'} onClick={() => pick(i, m)} onKeyDown={(e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i, m); } }} tabIndex={0} role="button" aria-label={sfdName(k, m) + ' ' + (m === 'major' ? t('major', '장조') : t('minor', '단조'))} style={{ cursor: 'pointer', outline: 'none' }}>
      <g style={{ transform: 'rotate(' + (-rot) + 'deg)', transition: tr }}>
        <circle r={r} fill={on ? NV : '#fff'} stroke={NV} strokeWidth={m === 'major' ? 1.6 : 1.3}/>
        {two ? <><text y={-1.5} textAnchor="middle" fontSize={fs2} fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{two[0] + sfx}</text><text y={fs2 - 1} textAnchor="middle" fontSize={fs2} fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{two[1] + sfx}</text></>
          : <text y={fs * 0.34} textAnchor="middle" fontSize={fs} fontWeight="800" fill={col} fontFamily="'Playfair Display', Georgia, serif">{prettyNote(k) + sfx}</text>}
      </g>
    </g>;
  };
  // the facts of the chosen scale
  const kind = mode === 'major' ? t('major', '장조') : t('minor', '단조');
  const sigK = SFD_SIGKEY(key, mode), [sgS, sgN] = SKG_KEY[sigK], sgMark = sgS === '#' ? '♯' : '♭';
  const sigLine = sgN === 0 ? t('No sharps or flats.', '샤프도 플랫도 없어요.') : t('Key signature: ' + sgN + sgMark + ' (' + skgSignNames(sigK).join(' ') + ')', '조표: ' + sgN + sgMark + ' (' + skgSignNames(sigK).join(' ') + ')');
  const relKey = mode === 'major' ? SFD_MIN[idx] : SFD_MAJ[idx], relMode = mode === 'major' ? 'minor' : 'major';
  const relLine = mode === 'major' ? t('Its relative minor is ' + sfdName(relKey, 'minor') + 'm: the same key signature.', '나란한 단조는 ' + sfdName(relKey, 'minor') + ' 단조예요: 조표가 같아요.') : t('Its relative major is ' + sfdName(relKey, 'major') + ': the same key signature.', '나란한 장조는 ' + sfdName(relKey, 'major') + ' 장조예요: 조표가 같아요.');
  const TWINTXT = { 'major:Db': ['Also written C♯ major, with 7 sharps: the same keys on the piano.', 'C♯ 장조(샤프 일곱)로도 적어요. 피아노에서는 같은 건반이에요.'], 'major:Gb': ['Also written F♯ major, with 6 sharps: the same keys on the piano.', 'F♯ 장조(샤프 여섯)로도 적어요. 피아노에서는 같은 건반이에요.'], 'minor:Bb': ['Also written A♯ minor, with 7 sharps: the same keys on the piano.', 'A♯ 단조(샤프 일곱)로도 적어요. 피아노에서는 같은 건반이에요.'], 'minor:D#': ['Also written E♭ minor, with 6 flats: the same keys on the piano.', 'E♭ 단조(플랫 여섯)로도 적어요. 피아노에서는 같은 건반이에요.'] };
  const twin = TWINTXT[mode + ':' + key];
  let K, marks = {}, names = {}, fing = null, nms = null, info, offs, clash = false, staff = null, noteDown = null;
  if (mode === 'major') {
    K = scIdx(key); const N = scNames(key); K.forEach((k, j) => { marks[k] = 'pass'; names[k] = N[j]; });
    info = SCALES[key]; offs = info.octaves[oct].offsets;
    const hl = skgOf(sfdScaleItems(key), key, n => n.byKey);
    staff = { items: sfdScaleItems(key), k: key, coral: [], alt: hl };
  } else {
    info = MINOR_SCALES[key]; const stp = MINOR_FORMS[form].steps, N = spellMinor(key, form).map(prettyAny);
    K = stp.map(x => info.rootPc + x).concat([info.rootPc + 12]);
    K.forEach((k, j) => { marks[k] = (form === 'harmonic' && j === 6) || (form === 'melodic' && (j === 5 || j === 6)) ? 'target' : 'pass'; names[k] = j === 7 ? N[0] : N[j]; });
    fing = info.octaves[oct]; nms = N;
    offs = form === 'harmonic' ? fing.offsets : minorOffsets(form, oct);
    clash = form !== 'harmonic' && ['RH', 'LH'].some(h => fing[h].some((f, i) => f === 1 && [1, 3, 6, 8, 10].includes((info.rootPc + offs[i]) % 12)));
    const mi = sfdMinItems(key, form); if (mi) { const hl = skgOf(mi.items, sigK, n => n.byKey).filter(j => !mi.coral.includes(j)); staff = { items: mi.items, k: sigK, coral: mi.coral, alt: hl }; }
    if (form === 'melodic') { const nn = spellMinor(key, 'natural'); noteDown = t('Coming down it is the natural minor: ', '내려올 때는 자연 단음계예요: ') + [nn[0], nn[6], nn[5], nn[4], nn[3], nn[2], nn[1], nn[0]].map(prettyAny).join(' '); }
  }
  const FORMS = ['natural', 'harmonic', 'melodic'];
  const FNAME = { natural: t('Natural', '자연'), harmonic: t('Harmonic', '화성'), melodic: t('Melodic', '가락') };
  const step = (d) => pick((idx + d + 12) % 12, mode);
  const body = <>
    <div style={scS.title}>{t('Scale finder', '스케일 찾기')}</div>
    <div style={scS.line}>{t('Turn the circle: one step right adds a ♯, one step left adds a ♭.', '원을 돌려 보세요: 오른쪽으로 한 칸이면 ♯이 하나 늘고, 왼쪽으로 한 칸이면 ♭이 하나 늘어요.')}</div>
    <svg data-sfd-dial viewBox="0 0 340 340" width="100%" style={{ display: 'block', maxWidth: 340, margin: '0 auto' }} role="group" aria-label={t('Circle of fifths', '5도권')}>
      <circle cx={C} cy={C} r={RO} fill="none" stroke="rgba(38,41,107,0.14)" strokeWidth="1.5" strokeDasharray="3 5"/>
      <circle cx={C} cy={C} r={RI} fill="none" stroke="rgba(38,41,107,0.14)" strokeWidth="1.5" strokeDasharray="3 5"/>
      <rect x={C - ro - 7} y={C - RO - ro - 7} width={2 * ro + 14} height={RO - RI + ro + ri + 14} rx={ro + 7} fill="#fbe3da" stroke={CO} strokeWidth="2"/>
      <g data-sfd-rot={rot} style={{ transform: 'rotate(' + rot + 'deg)', transformOrigin: C + 'px ' + C + 'px', transition: tr }}>
        {SFD_MAJ.map((_, i) => node(i, 'major'))}{SFD_MIN.map((_, i) => node(i, 'minor'))}
      </g>
      <text x={C} y={C - 14} textAnchor="middle" fontSize={sfdName(key, mode).length > 3 ? 19 : 26} fontWeight="900" fill={NV} fontFamily="'Playfair Display', Georgia, serif">{sfdName(key, mode)}</text>
      <text x={C} y={C + 4} textAnchor="middle" fontSize="11" fontWeight="900" letterSpacing="1.2" fill="var(--muted)">{mode === 'major' ? t('MAJOR', '장조') : t('MINOR', '단조')}</text>
      <text x={C} y={C + 26} textAnchor="middle" fontSize="19" fontWeight="900" fill={CO}>{CLOCK_SIG[mode][idx] === '0' ? '' : CLOCK_SIG[mode][idx]}</text>
      <text x={C - 30} y={C + 48} textAnchor="middle" fontSize="10.5" fontWeight="900" fill={CO}>{t('← ♭', '← ♭')}</text>
      <text x={C + 30} y={C + 48} textAnchor="middle" fontSize="10.5" fontWeight="900" fill={CO}>{t('♯ →', '♯ →')}</text>
    </svg>
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr 1fr', gap: 5, maxWidth: 330, margin: '4px auto 6px' }}>
      <button className="chip" data-sfd-step="-1" style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => step(-1)}>← ♭</button>
      {['major', 'minor'].map(m => <button key={m} className={'chip' + (mode === m ? ' active' : '')} aria-pressed={mode === m} style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => pick(idx, m)}>{m === 'major' ? t('Major', '장조') : t('Minor', '단조')}</button>)}
      <button className="chip" data-sfd-step="1" style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => step(1)}>♯ →</button>
    </div>
    <input value={q} onChange={e => search(e.target.value)} placeholder={t('Or type a key: Bb, f#m…', '또는 입력: Bb, f#m…')} aria-label={t('Type a key', '조 입력')} style={{ display: 'block', width: '100%', maxWidth: 330, boxSizing: 'border-box', margin: '0 auto 4px', padding: '8px 12px', borderRadius: 10, border: '1.5px solid ' + (miss ? '#c8361b' : 'var(--border)'), fontSize: 14, fontFamily: 'inherit' }}/>
    {miss && <div style={{ fontSize: 12, color: '#c8361b', textAlign: 'center' }}>{t('No key called “' + q + '” here. Try a letter with # or b, and “minor” if you need it.', '“' + q + '”(이)라는 조는 없어요. 알파벳에 # 또는 b를 붙이고, 단조면 “minor”를 써 보세요.')}</div>}
    <div style={{ borderTop: '1px solid var(--navy-line)', marginTop: 10, paddingTop: 12 }}>
      <div style={scS.title} data-sfd-title>{sfdName(key, mode)} {kind}</div>
      <div style={{ ...scS.line, minHeight: 0 }}>{sigLine}</div>
      {twin && <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, color: '#5a5d8f', margin: '2px 0 4px' }}>{t(twin[0], twin[1])}</div>}
      {mode === 'minor' && <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3,minmax(0,1fr))', gap: 6, maxWidth: 330, margin: '8px auto 6px' }}>
        {FORMS.map(f => <button key={f} className={'chip' + (form === f ? ' active' : '')} aria-pressed={form === f} style={{ ...KF_BTN, minHeight: 40, padding: '0 2px' }} onClick={() => setForm(f)}>{FNAME[f]}</button>)}
      </div>}
      <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={mode + key + form}/>
      {noteDown && <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, margin: '4px 0' }}>{noteDown}</div>}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(2,minmax(0,1fr))', gap: 6, maxWidth: 330, margin: '10px auto 6px' }}>
        {[1, 2].map(n => <button key={n} className={'chip' + (oct === n ? ' active' : '')} aria-pressed={oct === n} style={{ ...KF_BTN, minHeight: 38 }} onClick={() => setOct(n)}>{n === 1 ? t('1 octave', '1옥타브') : t('2 octaves', '2옥타브')}</button>)}
      </div>
      {clash ? <p style={{ fontSize: 13, color: 'var(--muted)', margin: '8px 0 0', textAlign: 'center', lineHeight: 1.5 }}>{t('No finger numbers for this form: the harmonic fingering would put a thumb on a black key. Look the fingering up in your book.', '이 형태는 손가락 번호를 보여 주지 않아요: 화성 단음계의 손가락 번호로는 엄지가 검은건반에 놓여요. 책에서 찾아보세요.')}</p>
        : <ScPair keyName={mode === 'major' ? key : 'm' + key} n={oct} fing={fing} nms={nms}/>}
      <ScStaffBtn on={stf} set={setStf}/>
      {stf && (staff ? <>
        <SkgStaff items={staff.items} k={staff.k} width={330} o={{ boxS: 26, D: 30, hl: staff.coral, hl2: staff.alt, signHl: staff.coral, underAlt: staff.alt, ksCol: '#2e8a6e', ...skgUnder(staff.items, staff.k, null, staff.coral) }}/>
        <div style={{ textAlign: 'center', fontSize: 12.5, fontWeight: 700, color: '#6d6f9c', marginTop: 4 }}>{t('Green: from the key signature. Coral: a sign written beside the note.', '초록: 조표에 있는 음. 코랄: 음표 옆에 붙이는 표.')}</div>
      </> : <div style={{ textAlign: 'center', fontSize: 13, color: 'var(--muted)', marginTop: 6 }}>{t('This form needs a double sharp, so the staff is left out here.', '이 형태는 겹샤프가 필요해서 오선은 보여 주지 않아요.')}</div>)}
      {scRow(<>
        <button className="ghost-btn" style={scS.back} onClick={() => playScaleNotes(info.rootPc, offs, mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null)}>{t('♪ Hear it up and down', '♪ 올라갔다 내려오며 듣기')}</button>
        <button className="ghost-btn" style={scS.prim} data-sfd-rel onClick={() => pick(idx, relMode)}>{mode === 'major' ? t('Relative minor →', '나란한 단조 →') : t('Relative major →', '나란한 장조 →')}</button>
      </>)}
      <div style={{ textAlign: 'center', fontSize: 13, fontWeight: 700, color: '#5a5d8f', marginTop: 8 }}>{relLine}</div>
    </div>
  </>;
  return scBox('finder', body);
}
const sfdScaleItems = (k) => { const d0 = SC_D0[k]; return Array.from({ length: 8 }, (_, j) => ['q', 1, d0 + j]).concat([['||']]); };
'''
rep("\nconst scDirTag = (dn) =>", NEW + "\nconst scDirTag = (dn) =>")

# 3. major staff: use the same call shape (hl via skgOf) -- staff.alt above already carries it

# 4. register
rep("{ id: 'scale-finder', ch: 'scales', title: 'Scale finder', blurb: 'Three short steps: scales that start on a white key, on a black key, then all twelve a half step apart. Right hand, left hand, both.', C: () => <ScaleFinder/> },",
    "{ id: 'scale-finder', ch: 'scales', title: 'Scale finder', blurb: 'Turn the circle of fifths to any major or minor key: the keyboard, both hands’ fingering, the key signature.', C: () => <ScaleFinderDial/> },")
rep("'scale-finder': ['스케일 찾기', '세 단계: 흰건반으로 시작하는 스케일, 검은건반으로 시작하는 스케일, 반음씩 올라가는 열두 조. 오른손, 왼손, 양손 순서예요.'],",
    "'scale-finder': ['스케일 찾기', '5도권을 돌려서 어떤 장조·단조든 찾아요: 건반, 양손 손가락 번호, 조표.'],")
rep("'scale-finder': ['Three short steps: white keys, black keys, all twelve.', '세 단계: 흰건반, 검은건반, 열두 조.'],",
    "'scale-finder': ['Turn the circle of fifths to any key.', '5도권을 돌려 어느 조든 찾아요.'],")
old_prev = "if (id === 'scale-finder') return <span style={{display:'flex',gap:5,flexWrap:'wrap'}}>{['C', 'D', 'E', 'F', 'G', 'A', 'B'].map((n, i) => <span key={n} style={{display:'inline-flex',alignItems:'center',justifyContent:'center',minWidth:34,height:34,borderRadius:17,background:i === 0 ? '#26296b' : '#fffefa',color:i === 0 ? '#fffefa' : '#26296b',border:'1.5px solid #26296b',fontWeight:800,fontSize:15}}>{n}</span>)}</span>;"
rep(old_prev, "if (id === 'scale-finder') return <svg width=\"64\" height=\"64\" viewBox=\"0 0 64 64\" aria-hidden=\"true\">{Array.from({ length: 12 }, (_, i) => <circle key={i} cx={32 + 26 * Math.sin(i * Math.PI / 6)} cy={32 - 26 * Math.cos(i * Math.PI / 6)} r={i === 0 ? 5 : 3.2} fill={i === 0 ? '#e4572e' : '#26296b'}/>)}</svg>;")
rep('<svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><circle cx="10" cy="10" r="6.5" fill="none" stroke="#fefbf3" strokeWidth="1.8"/><line x1="14.5" y1="14.5" x2="20" y2="20" stroke="#fefbf3" strokeWidth="2" strokeLinecap="round"/><circle cx="10" cy="10" r="2.2" fill="#e9a83a"/></svg>',
    '<svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{Array.from({ length: 12 }, (_, i) => <circle key={i} cx={12 + 7.5 * Math.sin(i * Math.PI / 6)} cy={12 - 7.5 * Math.cos(i * Math.PI / 6)} r={i === 0 ? 2.1 : 1.2} fill={i === 0 ? "#e9a83a" : "#fefbf3"}/>)}</svg>')
open(b, 'w', encoding='utf-8').write(s)
print('ok')
