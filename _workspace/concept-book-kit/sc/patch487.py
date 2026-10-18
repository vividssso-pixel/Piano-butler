#!/usr/bin/env python3
# Phase 487b: Keys cleaned up. One tool, the Key finder, absorbs the key-signature cards.
# (rule 16; her 2026-10-18 23:47 'father charles goes down ... 샵이나 플랫 하나씩 직접 자기가 눌러서 ... 통합으로 단순하게')
# Runs on the output of patch486 + patch486b.  python3 patch487.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

# 1. the component, placed before the Key Signatures hero
KF = r'''// Phase 487 (rule 16): the one key tool. Add the sharps or flats one at a time (the sentence lights up, each one sounds),
// tap any key on the circle, place them yourself, find the relative minor. The old cards stay as hidden cards.
const KF_WORDS = { sharp: ['Father', 'Charles', 'Goes', 'Down', 'And', 'Ends', 'Battle'], flat: ['Battle', 'Ends', 'And', 'Down', 'Goes', 'Charles’', 'Father'] };
function KeyFinder() {
  const [type, setType] = useState('sharp');
  const [n, setN] = useState(0);
  const [clef, setClef] = useState('treble');
  const [auto, setAuto] = useState(false);
  const [sec, setSec] = useState(null);
  const order = type === 'sharp' ? SHARP_ORDER : FLAT_ORDER;
  const sym = type === 'sharp' ? '♯' : '♭';
  const k = KEY_BY_COUNT(type, n);
  const words = KF_WORDS[type];
  useEffect(() => {
    if (!auto) return;
    if (n >= 7) { setAuto(false); return; }
    const id = setTimeout(() => { playKey(pcOfName(order[n]), 0.5); setN(x => x + 1); }, 850);
    return () => clearTimeout(id);
  }, [auto, n]);
  function add() { if (n >= 7) return; setAuto(false); playKey(pcOfName(order[n]), 0.5); setN(n + 1); }
  function less() { setAuto(false); setN(Math.max(0, n - 1)); }
  function pickType(ty) { setAuto(false); setType(ty); setN(0); }
  function pickKey(ks) { setAuto(false); if (ks.type) setType(ks.type); setN(ks.count); }
  const slot = CIRCLE.findIndex(c => c.maj.includes(k.major));
  const names = CIRCLE[slot].maj;
  const R = 92, r = 60, cx = 120, cy = 118;
  const pt = (i, rad) => { const a = -Math.PI / 2 + i * Math.PI / 6; return [cx + rad * Math.cos(a), cy + rad * Math.sin(a)]; };
  const chipStyle = { padding: '8px 14px', fontSize: 14, minHeight: 40 };
  return (
    <div className="try-box" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px',margin:'4px 0 16px'}}>
      <div style={{fontSize:15,fontWeight:800,marginBottom:2}}>{t('Key signatures', '조표')}</div>
      <div style={{fontSize:13,color:'#6d6f9c',lineHeight:1.5,marginBottom:8}}>{t('Add the sharps (or flats) one at a time and say the sentence as you go. Or tap a key on the circle.', '샤프(또는 플랫)를 하나씩 더하면서 문장을 말해 봐요. 또는 5도권에서 조를 눌러 봐요.')}</div>
      <div style={{display:'flex',flexWrap:'wrap',gap:6,alignItems:'center',justifyContent:'space-between',marginBottom:6}}>
        <div style={{display:'flex',gap:4}}>
          {[['sharp', '♯ ' + t('Sharps', '샤프')], ['flat', '♭ ' + t('Flats', '플랫')]].map(([ty, l]) => <button key={ty} className={'chip' + (type === ty ? ' active' : '')} aria-pressed={type === ty} style={chipStyle} onClick={() => pickType(ty)}>{l}</button>)}
        </div>
        <div style={{display:'flex',gap:4}}>
          {['treble', 'bass'].map(c => <button key={c} className={'chip' + (clef === c ? ' active' : '')} aria-pressed={clef === c} style={chipStyle} onClick={() => setClef(c)}>{c === 'treble' ? t('𝄞 treble', '𝄞 높은음') : t('𝄢 bass', '𝄢 낮은음')}</button>)}
        </div>
      </div>
      <KSStaff count={n} type={type} width={170} clef={clef} upto={n ? n - 1 : undefined} numbers/>
      <div style={{display:'flex',justifyContent:'center',gap:10,fontSize:15,fontWeight:900,margin:'2px 0 4px',minHeight:22}}>
        {order.map((nm, i) => <span key={nm} style={{opacity:i < n ? 1 : 0.18,color:i === n - 1 ? '#c8361b' : 'var(--text)',transition:'opacity 0.3s'}}>{prettyNote(nm)}</span>)}
      </div>
      <div style={{display:'flex',flexWrap:'wrap',gap:'0 6px',justifyContent:'center',fontSize:14,fontWeight:700,lineHeight:1.5}}>
        {words.map((w, i) => <span key={i} style={{opacity:i < n ? 1 : 0.25,color:i === n - 1 ? '#c8361b' : 'var(--text)',fontWeight:i === n - 1 ? 900 : 700,transition:'opacity 0.3s'}}>{w}</span>)}
      </div>
      {type === 'flat' && <div style={{textAlign:'center',fontSize:12,color:'var(--muted)',marginTop:2}}>{t('the same sentence backwards', '같은 문장을 거꾸로')}</div>}
      <div style={{textAlign:'center',fontSize:15,fontWeight:800,minHeight:22,marginTop:6}}>
        {n === 0 ? t('No sharps or flats = C major / A minor', '샤프·플랫 없음 = C장조 / A단조') : n + sym + ' = ' + majName(k) + ' / ' + minName(k)}
      </div>
      <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center',marginTop:8}}>
        <button className="ghost-btn" style={{minHeight:40}} disabled={n === 0} onClick={less}>{t('− One off', '− 하나 빼기')}</button>
        <button className="ghost-btn" style={{minHeight:40,fontWeight:900}} disabled={n === 7} onClick={add}>{t('+ Next one', '+ 다음 하나')}</button>
        <button className="ghost-btn" style={{minHeight:40}} onClick={() => { setN(0); setAuto(true); }}>{t('▶ Play', '▶ 재생')}</button>
      </div>
      <div style={{fontSize:12,fontWeight:800,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'0.05em',margin:'14px 0 2px',textAlign:'center'}}>{t('Every key on one clock', '모든 조를 시계 하나에')}</div>
      <svg viewBox="0 0 240 236" style={{width:'100%',maxWidth:340,display:'block',margin:'0 auto'}}>
        <circle cx={cx} cy={cy} r={R + 16} fill="#f8f3e6" stroke="#e9e2d2"/>
        <circle cx={cx} cy={cy} r={r - 16} fill="#fff" stroke="#e9e2d2"/>
        <text x="6" y="14" fontSize="9" fontWeight="800" fill="#6d78b8">{t('↺ flats', '↺ 플랫')}</text>
        <text x="234" y="14" textAnchor="end" fontSize="9" fontWeight="800" fill="#e4572e">{t('sharps ↻', '샤프 ↻')}</text>
        {CIRCLE.map((c, i) => {
          const [x, y] = pt(i, R), [ix, iy] = pt(i, r);
          const on = i === slot;
          const minors = c.maj.map(m => KEY_SIGS.find(q => q.major === m).minor);
          const cur = c.maj.indexOf(k.major);
          const target = KEY_SIGS.find(q => q.major === (on && c.maj.length > 1 ? c.maj[(cur + 1) % c.maj.length] : c.maj[0]));
          return (
            <g key={i} role="button" aria-label={prettyNote(c.maj[0])} onClick={() => pickKey(target)} style={{cursor:'pointer'}}>
              <circle cx={x} cy={y} r="21" fill="transparent"/>
              <circle cx={x} cy={y} r="15" fill={on ? '#26296b' : '#fff'} stroke={on ? '#26296b' : '#dbd2bd'}/>
              <text x={x} y={y + (c.maj.length > 1 ? -1 : 4)} textAnchor="middle" fontSize={c.maj.length > 1 ? 9 : 12} fontWeight="900" fill={on ? '#fff' : '#26296b'}>{prettyNote(c.maj[0])}</text>
              {c.maj.length > 1 && <text x={x} y={y + 9} textAnchor="middle" fontSize="8" fontWeight="700" fill={on ? '#fbe3da' : '#a3a5c2'}>{prettyNote(c.maj[1])}</text>}
              <text x={ix} y={iy + 3} textAnchor="middle" fontSize="8.5" fontWeight="700" fill={on ? '#e4572e' : '#a3a5c2'}>{prettyNote(minors[on ? Math.max(0, cur) : 0]).toLowerCase()}</text>
            </g>
          );
        })}
        <text x={cx} y={cy - 2} textAnchor="middle" fontSize="12" fontWeight="900" fill="#26296b">{prettyNote(k.major)}</text>
        <text x={cx} y={cy + 12} textAnchor="middle" fontSize="9" fontWeight="700" fill="#a3a5c2">{sigLabel(k)}</text>
      </svg>
      {names.length > 1 && (
        <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'4px 0'}}>
          {names.map(m => { const ks = KEY_SIGS.find(q => q.major === m); return <button key={m} className={'chip' + (k.major === m ? ' active' : '')} aria-pressed={k.major === m} style={chipStyle} onClick={() => pickKey(ks)}>{prettyNote(m)}{t(' major', ' 장조')} · {sigLabel(ks)}</button>; })}
        </div>
      )}
      <div style={{display:'flex',gap:6,flexWrap:'wrap',marginTop:12}}>
        {[['place', t('Place them yourself', '직접 놓아 보기')], ['minor', t('Relative minor', '나란한조')]].map(([id, l]) => <button key={id} className={'chip' + (sec === id ? ' active' : '')} style={{padding:'9px 16px',fontSize:14,minHeight:40}} aria-pressed={sec === id} onClick={() => setSec(sec === id ? null : id)}>{l}</button>)}
      </div>
      {sec === 'place' && <div className="kf-nest" style={{marginTop:10}}><PlaceIt key={type} initType={type}/></div>}
      {sec === 'minor' && <div className="kf-nest" style={{marginTop:10}}><RelativeMinor key={k.major} initKey={k.major}/></div>}
    </div>
  );
}

'''
rep("// Phase 201 (2026-09-29): Key Signatures hero, chapter 15 of 24.", KF + "// Phase 201 (2026-09-29): Key Signatures hero, chapter 15 of 24.")

# 2. PlaceIt and RelativeMinor can start from the finder's choice
rep("function PlaceIt() {\n  const [type, setType] = useState('sharp');", "function PlaceIt({ initType = 'sharp' }) {\n  const [type, setType] = useState(initType);")
rep("function RelativeMinor() {\n  const [key, setKey] = useState('C');", "function RelativeMinor({ initKey = 'C' }) {\n  const [key, setKey] = useState(initKey);")
rep("{REL_KEYS.map(k =>", "{(REL_KEYS.includes(initKey) ? REL_KEYS : [...REL_KEYS, initKey]).map(k =>")

# 3. nested boxes inside the finder: no second TRY IT ribbon, no extra margin
rep("    .try-box::before { content: 'TRY IT';", "    .kf-nest .try-box::before { display: none; }\n    .kf-nest .try-box { margin: 0 !important; }\n    .try-box::before { content: 'TRY IT';")

# 4. the card, and the cards it absorbs (hidden, not deleted)
rep("  { id: 'skg-every', ch: 'key-signatures',",
    "  { id: 'key-finder', ch: 'key-signatures', title: 'Key finder', blurb: 'Every key in one place: add the sharps or flats one at a time, tap the circle, place them yourself, find the relative minor.', C: () => <KeyFinder/> },\n  { id: 'skg-every', ch: 'key-signatures',")
for tid in ['skg-g', 'skg-f', 'sharps-order', 'flats-order', 'place-it', 'relative-minor', 'circle-fifths', 'all-keys']:
    rep("  { id: '%s', ch: 'key-signatures'," % tid, "  { id: '%s', hidden: true, ch: 'key-signatures'," % tid)

# 5. Korean name, meta, concept, icon, chapter list
rep("  'circle-fifths': ['5도권', '모든 조를 시계 하나에.'],",
    "  'circle-fifths': ['5도권', '모든 조를 시계 하나에.'],\n  'key-finder': ['조 찾기', '조 하나로: 샤프나 플랫을 하나씩 더하고, 5도권을 눌러 보고, 직접 놓아 보고, 나란한조를 찾아요.'],")
rep("'circle-fifths': ['scales', 2, 3, 'show'],", "'circle-fifths': ['scales', 2, 3, 'show'], 'key-finder': ['scales', 1, 3, 'show write'],")
rep("'all-keys': 'p-scales',", "'all-keys': 'p-scales', 'key-finder': 'p-scales',")
rep("['all-keys', 'circle-fifths'],", "['all-keys', 'circle-fifths'], ['key-finder', 'circle-fifths'],")
rep("'key-signatures': ['skg-every', 'skg-g',", "'key-signatures': ['key-finder', 'skg-every', 'skg-g',")

# 6. the exam kit and the concept book's steps point at the Key finder
rep("['has a theory exam coming', ['sharps-order', 'place-it', 'scale-finder',", "['has a theory exam coming', ['key-finder', 'scale-finder',")
rep("X('The order of sharps and flats (Key signatures); a major key’s relative minor, natural and harmonic (Minor scales).', '샤프와 플랫의 순서(조표), 장조의 나란한조, 자연단음계와 화성단음계(단음계).'), ['scale-finder', 'sharps-order', 'flats-order', 'relative-minor']",
    "X('The order of sharps and flats, a major key’s relative minor (Key finder); natural and harmonic minor (Scale finder).', '샤프와 플랫의 순서, 장조의 나란한조(조 찾기), 자연단음계와 화성단음계(스케일 찾기).'), ['key-finder', 'scale-finder']")
rep("X('The circle of fifths; placing a key signature (Key signatures); the melodic minor (Minor scales); the major pentatonic on C and G (Other scales).', '5도권, 조표 자리 찾기(조표), 가락단음계(단음계), C와 G의 장조 5음음계(다른 음계).'), ['circle-fifths', 'place-it', 'csx-penta', 'scale-finder']",
    "X('The circle of fifths; placing a key signature (Key finder); the melodic minor (Scale finder); the major pentatonic on C and G (Other scales).', '5도권, 조표 자리 찾기(조 찾기), 가락단음계(스케일 찾기), C와 G의 장조 5음음계(다른 음계).'), ['key-finder', 'csx-penta', 'scale-finder']")
rep("X('All fifteen key signatures (The circle of fifths); double sharps (G♯ minor’s F𝄪); the chromatic scale (Other scales); the modes.', '조표 15개 전부(5도권), 겹샤프(G♯단조의 F𝄪), 반음계(다른 음계), 선법.'), ['all-keys', 'chromatic', 'scale-finder']",
    "X('All fifteen key signatures (Key finder); double sharps (G♯ minor’s F𝄪); the chromatic scale (Other scales); the modes (Scale finder).', '조표 15개 전부(조 찾기), 겹샤프(G♯단조의 F𝄪), 반음계(다른 음계), 선법(스케일 찾기).'), ['key-finder', 'chromatic', 'scale-finder']")

# 7. the Major/Minor direction row of the relative-minor card wraps instead of clipping at 320
rep("      <div style={{display:'flex',gap:4,marginBottom:6}}>\n        {[['down', t('Major → minor'", "      <div style={{display:'flex',gap:4,marginBottom:6,flexWrap:'wrap'}}>\n        {[['down', t('Major → minor'")

open(dst, 'w', encoding='utf-8').write(s)
print('patched 487', len(s))
