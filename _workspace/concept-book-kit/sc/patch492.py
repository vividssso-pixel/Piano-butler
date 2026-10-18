#!/usr/bin/env python3
# Phase 492: Key finder becomes four short steps (her 2026-10-19 01:03 teaching order + 01:28 'keep it simple, one look').
# 1 the order of sharps/flats, 2 sharps: tap the last one, the key lights on a piano, 3 flats: tap the second-to-last,
# 4 major to minor side by side, 5 before a piece. The old everything-at-once Key finder stays as 'Free play'.
# One picture, one line, one button per screen.   python3 patch492.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

rep("function KeyFinder() {\n  const [type, setType] = useState('sharp');", "function KeyFinderFree() {\n  const [type, setType] = useState('sharp');")

NEW = r'''// ── Phase 492: the Key finder in four steps ──
const KF_BTN = { minHeight: 44, fontWeight: 800, fontSize: 15 };
function KfChain({ hi }) {
  const items = [t('Read it', '읽기'), t('Name the key', '조 찾기'), t('Play its scale', '스케일 치기')];
  return (
    <div role="img" aria-label={items.map((l, i) => hi.includes(i) ? '[' + l + ']' : l).join(' → ')} style={{display:'flex',flexWrap:'nowrap',justifyContent:'center',alignItems:'center',gap:3,marginBottom:8}}>
      {items.map((l, i) => <React.Fragment key={i}>{i > 0 && <span style={{color:'#a3a5c2',fontWeight:800,fontSize:12}}>→</span>}<span style={{flex:'1 1 0',minWidth:0,textAlign:'center',lineHeight:1.2,padding:'5px 4px',borderRadius:14,fontSize:11.5,fontWeight:800,background:hi.includes(i) ? '#e4572e' : '#efe8d6',color:hi.includes(i) ? '#fff' : '#26296b'}}>{l}</span></React.Fragment>)}
    </div>
  );
}
function KfNext({ go, label }) {
  return <div style={{textAlign:'center',marginTop:14}}><button className="ghost-btn" style={{...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={go}>{label || t('Next →', '다음 →')}</button></div>;
}
// sharps or flats: the order, then the tap that finds the key, on one screen
function KfFind({ type, go, setKi }) {
  const sharp = type === 'sharp', sym = sharp ? '♯' : '♭', order = sharp ? SHARP_ORDER : FLAT_ORDER, words = KF_WORDS[type];
  const [n, setN] = useState(3);
  const [lit, setLit] = useState(3);
  const [found, setFound] = useState(false);
  const [wrong, setWrong] = useState(null);
  const timers = useRef([]);
  const tiny = useCbNarrow(380);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const k = KEY_BY_COUNT(type, n), want = sharp ? n - 1 : n - 2, auto = want < 0;
  const done = found || auto;
  useEffect(() => { if (auto) { const j = KEY_SIGS.findIndex(q => q.major === k.major); if (j >= 0) setKi(j); } }, [auto, k.major]);
  const tonic = pcOfName(k.major), marks = {};
  if (done) { if (sharp) marks[pcOfName(order[want])] = 'mate'; marks[tonic] = 'pick'; }
  const pickN = (i) => { clear(); setN(i); setLit(i); setFound(false); setWrong(null); };
  const say = () => { clear(); setLit(0); for (let i = 0; i < n; i++) timers.current.push(setTimeout(() => { playKey(pcOfName(order[i]), 0.45); setLit(i + 1); }, 350 + i * 520)); };
  const tap = (i) => { if (done) return; if (i === want) { setFound(true); playKey(tonic, 0.6); const j = KEY_SIGS.findIndex(q => q.major === k.major); if (j >= 0) setKi(j); } else { setWrong(i); setTimeout(() => setWrong(null), 700); } };
  return (<>
    <KfChain hi={[0, 1]}/>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',minHeight:27,textWrap:'balance'}}>
      {done ? <span style={{animation:'fadeUp 0.3s both',display:'inline-block'}}>{n}{sym} → <span style={{color:'#c0431f'}}>{majName(k)}</span></span> : t('What key has ' + n + sym + '?', (sharp ? '샤프 ' : '플랫 ') + n + '개는 무슨 조?')}
    </div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + (tiny ? 4 : 7) + ', minmax(0, 1fr))',gap:4,marginBottom:6}}>
      {[1, 2, 3, 4, 5, 6, 7].map(i => <button key={i} className={'chip' + (n === i ? ' active' : '')} aria-pressed={n === i} style={{...KF_BTN,minWidth:44,padding:'0 2px',fontSize:14}} onClick={() => pickN(i)}>{i}{sym}</button>)}
    </div>
    <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200}/></div>
    <div style={{display:'flex',flexWrap:'wrap',gap:'0 6px',justifyContent:'center',fontSize:14,fontWeight:700,lineHeight:1.5,margin:'2px 0',textWrap:'balance'}}>
      {words.map((w, i) => <span key={i} style={{opacity:i < lit ? 1 : 0.22,color:i === lit - 1 ? '#c8361b' : '#26296b',fontWeight:i === lit - 1 ? 900 : 700,transition:'opacity 0.3s'}}>{w}</span>)}
    </div>
    {!sharp && <div style={{textAlign:'center',fontSize:12,color:'#5a5d8f',marginTop:-1}}>{t('the same sentence backwards', '같은 문장을 거꾸로')}</div>}
    <div style={{textAlign:'center',margin:'4px 0 10px'}}><button className="ghost-btn" style={{...KF_BTN,minWidth:120}} onClick={say}>{t('▶ Say the order', '▶ 순서 듣기')}</button></div>
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',marginBottom:6}}>{auto ? t('Only one: it is F.', '하나뿐이면 F예요.') : sharp ? t('Now tap the last ♯.', '이제 마지막 샤프를 눌러요.') : t('Now tap the second-to-last ♭.', '이제 뒤에서 두 번째 플랫을 눌러요.')}</div>
    {!auto && <div style={{display:'flex',gap:4,justifyContent:'center',marginBottom:8}}>
      {order.slice(0, n).map((nm, i) => <button key={nm} aria-label={prettyNote(nm)} className="chip" style={{...KF_BTN,flex:'1 1 0',minWidth:0,maxWidth:56,padding:'0 2px',fontSize:15,
        background:done && i === want ? '#26296b' : '#fff',color:done && i === want ? '#fffefa' : '#26296b',borderColor:wrong === i ? '#e4572e' : undefined,borderWidth:wrong === i ? 2.5 : undefined,opacity:done && i !== want ? 0.35 : 1}} onClick={() => tap(i)}>{prettyNote(nm)}</button>)}
    </div>}
    <div style={{maxWidth:300,margin:'0 auto'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels/></div>
    <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#5a5d8f',minHeight:20,marginTop:6}}>{done && !auto ? (sharp ? t('A half step up from the last ♯.', '마지막 샤프의 반음 위!') : t('That ♭ is the key.', '그 플랫이 바로 그 조!')) : ''}</div>
    <KfNext go={go}/>
  </>);
}
function KfNav({ i, setI, children }) {
  const m = KEY_SIGS.length, step = (d) => setI((i + d + m) % m);
  return (
    <div style={{display:'flex',alignItems:'center',gap:6,justifyContent:'center'}}>
      <button className="ghost-btn" aria-label={t('Previous key', '이전 조')} style={{...KF_BTN,minWidth:44,padding:0}} onClick={() => step(-1)}>‹</button>
      <div style={{flex:'1 1 auto',minWidth:0}}>{children}</div>
      <button className="ghost-btn" aria-label={t('Next key', '다음 조')} style={{...KF_BTN,minWidth:44,padding:0}} onClick={() => step(1)}>›</button>
    </div>
  );
}
const cbNoteElName = (nm, tail) => <>{prettyNote(nm)}{tail}</>;
function KfMinor({ i, setI, go }) {
  const ks = KEY_SIGS[i], marks = {}; marks[pcOfName(ks.minor)] = 'mate'; marks[pcOfName(ks.major)] = 'pick';
  const card = (txt, strong) => <div style={{flex:'1 1 0',minWidth:0,textAlign:'center',padding:'8px 4px',borderRadius:12,fontWeight:900,fontSize:16,background:strong ? '#e4572e' : '#fbe3da',color:strong ? '#fff' : '#26296b',border:'1.5px solid ' + (strong ? '#c0431f' : '#e9b9a6')}}>{txt}</div>;
  return (<>
    <KfChain hi={[1]}/>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'}}>{t('Is it major or minor?', '장조일까, 단조일까?')}</div>
    <KfNav i={i} setI={setI}>
      <div style={{maxWidth:200,margin:'0 auto'}}><KSStaff count={ks.count} type={ks.type} width={170}/></div>
      <div style={{display:'flex',gap:6}}>{card(cbNoteElName(ks.major, t(' major', '장조')), true)}{card(cbNoteElName(ks.minor, t(' minor', '단조')), false)}</div>
    </KfNav>
    <div style={{maxWidth:300,margin:'10px auto 0'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels onTap={(x) => { const j = KEY_SIGS.findIndex(q => pcOfName(q.major) === x); if (j >= 0) setI(j); }}/></div>
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 0'}}>{t('The same signature has both. From the major, count 3 half steps down.', '조표는 같아요. 장조에서 반음 3칸 아래로 내려가면 단조.')}</div>
    <KfNext go={go}/>
  </>);
}
function KfPiece({ i, setI }) {
  const ks = KEY_SIGS[i];
  return (<>
    <KfChain hi={[2]}/>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'}}>{t('Before you play the piece', '곡을 치기 전에')}</div>
    <KfNav i={i} setI={setI}>
      <div style={{maxWidth:200,margin:'0 auto'}}><KSStaff count={ks.count} type={ks.type} width={170}/></div>
      <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:20,fontWeight:900,color:'#26296b'}}>{majName(ks)} · {minName(ks)}</div>
    </KfNav>
    <div style={{textAlign:'center',marginTop:14}}><a className="ghost-btn" style={{...KF_BTN,display:'inline-flex',alignItems:'center',textDecoration:'none',background:'#26296b',color:'#fffefa',borderColor:'#26296b',padding:'0 20px'}} href={cbHref('tool=scale-finder&key=' + encodeURIComponent(ks.major))}>{t('▶ Play its scale', '▶ 스케일 치러 가기')}</a></div>
  </>);
}
function KeyFinder() {
  const [step, setStep] = useState(1);
  const [ki, setKi] = useState(1);
  const names = [null, t('Sharps', '샤프'), t('Flats', '플랫'), t('Major and minor', '장조와 단조'), t('Before a piece', '곡 치기 전에')];
  const go = () => setStep(s => Math.min(4, s + 1));
  if (step === 0) return (
    <div className="try-box" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px',margin:'4px 0 16px'}}>
      <button className="ghost-btn" style={{...KF_BTN,marginBottom:6}} onClick={() => setStep(1)}>{t('← The four steps', '← 네 단계')}</button>
      <KeyFinderFree/>
    </div>);
  return (
    <div className="try-box" data-kf-steps style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>
      <div role="tablist" aria-label={t('Four steps', '네 단계')} style={{display:'flex',gap:4,marginBottom:6}} onKeyDown={(e) => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!d) return; e.preventDefault(); const nv = ((step - 1 + d + 4) % 4) + 1; setStep(nv); const el = document.getElementById('kf-tab-' + nv); if (el) el.focus(); }}>
        {[1, 2, 3, 4].map(i => <button key={i} id={'kf-tab-' + i} role="tab" tabIndex={step === i ? 0 : -1} aria-selected={step === i} aria-label={names[i]} className={'chip' + (step === i ? ' active' : '')} style={{...KF_BTN,flex:'1 1 0',minWidth:0,padding:'0 2px',fontSize:14}} onClick={() => setStep(i)}>{i}</button>)}
      </div>
      <div style={{height:8}}/>
      {step === 1 && <KfFind key="sharp" type="sharp" go={go} setKi={setKi}/>}
      {step === 2 && <KfFind key="flat" type="flat" go={go} setKi={setKi}/>}
      {step === 3 && <KfMinor i={ki} setI={setKi} go={go}/>}
      {step === 4 && <KfPiece i={ki} setI={setKi}/>}
      <div style={{textAlign:'center',marginTop:12}}><button className="ghost-btn" style={{minHeight:44,fontSize:13,fontWeight:700,color:'#5a5d8f'}} onClick={() => setStep(0)}>{t('Free play', '자유롭게')}</button></div>
    </div>
  );
}

'''
rep("// Phase 201 (2026-09-29): Key Signatures hero, chapter 15 of 24.", NEW + "// Phase 201 (2026-09-29): Key Signatures hero, chapter 15 of 24.")

# bigger-label option exists from Phase 490 (TapKeyboard bigLabels). Tool blurbs
rep("blurb: 'Every key in one place: add the sharps or flats one at a time, tap the circle, place them yourself, find the relative minor.'",
    "blurb: 'Four short steps: sharps, flats, major and minor, before a piece.'")
rep("'조 하나로: 샤프나 플랫을 하나씩 더하고, 5도권을 눌러 보고, 직접 놓아 보고, 나란한조를 찾아요.'", "'네 단계: 샤프, 플랫, 장조와 단조, 곡 치기 전에.'")
rep("'key-finder': ['Add the sharps or flats one at a time. Tap any key on the circle.', '샤프나 플랫을 하나씩 더해 봐요. 5도권에서 조를 눌러 봐요.'],",
    "'key-finder': ['Four short steps to find any key.', '조를 찾는 네 단계예요.'],")
open(dst, 'w', encoding='utf-8').write(s)
print('patched 492', len(s))
