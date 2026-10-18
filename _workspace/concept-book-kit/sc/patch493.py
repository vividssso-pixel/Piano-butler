#!/usr/bin/env python3
# Phase 493: Scale finder in three short steps (her 2026-10-19 01:01 teaching order; 01:28 'simple, one look'):
# 1 scales that start on a white key, 2 scales that start on a black key, 3 all twelve, a half step apart; each with the hands
# in her order: right, left, both. The old Scale finder stays as 'Free play' (and is what every link with ?key= and every lesson step opens).
#   python3 patch493.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

rep("function ScaleFinder({ ext, onKey } = {}) {\n  const init = PENDING_SCALE", "function ScaleFinderFree({ ext, onKey } = {}) {\n  const init = PENDING_SCALE")

NEW = r'''// ── Phase 493: the Scale finder in three steps ──
const SF12 = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B'];
function SfChain({ at }) {
  const items = [t('White keys', '흰건반'), t('Black keys', '검은건반'), t('All twelve', '열두 조')];
  return (
    <div role="img" aria-label={items.map((l, i) => i === at ? '[' + l + ']' : l).join(' → ')} style={{display:'flex',flexWrap:'nowrap',justifyContent:'center',alignItems:'center',gap:3,marginBottom:8}}>
      {items.map((l, i) => <React.Fragment key={i}>{i > 0 && <span style={{color:'#a3a5c2',fontWeight:800,fontSize:12}}>→</span>}<span style={{flex:'1 1 0',minWidth:0,textAlign:'center',lineHeight:1.2,padding:'5px 4px',borderRadius:14,fontSize:11.5,fontWeight:800,background:i === at ? '#e4572e' : '#efe8d6',color:i === at ? '#fff' : '#26296b'}}>{l}</span></React.Fragment>)}
    </div>
  );
}
function SfStage({ keys, k, setK, hand, setHand, titleFor, grid, go }) {
  const tiny = useCbNarrow(380);
  const info = scaleData(k, 'major') || SCALES.C, e = info.octaves[1];
  const play = () => playScaleNotes(info.rootPc, e.offsets, null);
  const hands = [['RH', t('Right hand', '오른손')], ['LH', t('Left hand', '왼손')], ['both', t('Both hands', '양손')]];
  const nm = prettyNote(k);
  return (<>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',minHeight:27,textWrap:'balance'}}>{titleFor(nm)}</div>
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + grid + ', minmax(0, 1fr))',gap:4,marginBottom:8}}>
      {keys.map(x => <button key={x} className={'chip' + (x === k ? ' active' : '')} aria-pressed={x === k} style={{...KF_BTN,minWidth:0,padding:'0 2px',fontSize:15}} onClick={() => setK(x)}>{prettyNote(x)}</button>)}
    </div>
    <div style={{display:'flex',gap:4,marginBottom:8}}>
      {hands.map(([h, l]) => <button key={h} className={'chip' + (hand === h ? ' active' : '')} aria-pressed={hand === h} style={{...KF_BTN,flex:'1 1 0',minWidth:0,padding:'0 2px',fontSize:tiny ? 12 : 13}} onClick={() => setHand(h)}>{l}</button>)}
    </div>
    {(hand === 'RH' || hand === 'both') && <div>{hand === 'both' && <div style={{fontSize:12,fontWeight:900,color:'#5a5d8f',letterSpacing:'0.05em',marginBottom:2}}>{t('RIGHT', '오른손')}</div>}<ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.RH} hand="RH"/></div>}
    {(hand === 'LH' || hand === 'both') && <div style={{marginTop:hand === 'both' ? 8 : 0}}>{hand === 'both' && <div style={{fontSize:12,fontWeight:900,color:'#5a5d8f',letterSpacing:'0.05em',marginBottom:2}}>{t('LEFT', '왼손')}</div>}<ScaleKeyboard rootPc={info.rootPc} offsets={e.offsets} fingers={e.LH} hand="LH"/></div>}
    <div style={{display:'flex',gap:14,flexWrap:'wrap',alignItems:'center',justifyContent:'center',marginTop:8,fontSize:13,fontWeight:800,color:'#26296b'}}>
      <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:16,height:16,borderRadius:4,background:SEGMENT_COLORS.three.fill,border:'1.5px solid ' + SEGMENT_COLORS.three.stroke}}/>1-2-3</span>
      <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:16,height:16,borderRadius:4,background:SEGMENT_COLORS.four.fill,border:'1.5px solid ' + SEGMENT_COLORS.four.stroke}}/>1-2-3-4</span>
    </div>
    <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:12}}>
      <button className="ghost-btn" style={{...KF_BTN,minWidth:120}} onClick={play}>{t('▶ Hear it', '▶ 듣기')}</button>
      {go && <button className="ghost-btn" style={{...KF_BTN,minWidth:120,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={go}>{t('Next →', '다음 →')}</button>}
    </div>
  </>);
}
function ScaleFinder(props = {}) {
  const hub = !props.onKey && !props.ext;
  const fromLink = (() => { if (PENDING_SCALE) return true; try { const p = new URLSearchParams(location.search); return !!p.get('key'); } catch (e) { return false; } })();
  const [step, setStep] = useState(!hub || fromLink ? 0 : 1);
  const [hand, setHand] = useState('RH');
  const [k1, setK1] = useState('C'), [k2, setK2] = useState('Db'), [k3, setK3] = useState('C');
  const tiny = useCbNarrow(380);
  if (!hub) return <ScaleFinderFree {...props}/>;
  const names = [null, t('White keys', '흰건반'), t('Black keys', '검은건반'), t('All twelve', '열두 조')];
  const go = () => setStep(x => Math.min(3, x + 1));
  const box = { background:'#fff', border:'1px solid var(--border)', borderRadius:10, padding:'10px 10px 12px', margin:'4px 0 16px' };
  if (step === 0) return (
    <div>
      <button className="ghost-btn" style={{...KF_BTN,marginBottom:6}} onClick={() => setStep(1)}>{t('← The three steps', '← 세 단계')}</button>
      <ScaleFinderFree {...props}/>
    </div>);
  return (
    <div className="try-box" data-sf-steps style={box}>
      <div role="tablist" aria-label={t('Three steps', '세 단계')} style={{display:'flex',gap:4,marginBottom:6}} onKeyDown={(e) => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!d) return; e.preventDefault(); const nv = ((step - 1 + d + 3) % 3) + 1; setStep(nv); const el = document.getElementById('sf-tab-' + nv); if (el) el.focus(); }}>
        {[1, 2, 3].map(i => <button key={i} id={'sf-tab-' + i} role="tab" tabIndex={step === i ? 0 : -1} aria-selected={step === i} aria-label={names[i]} className={'chip' + (step === i ? ' active' : '')} style={{...KF_BTN,flex:'1 1 0',minWidth:0,padding:'0 2px',fontSize:14}} onClick={() => setStep(i)}>{i}</button>)}
      </div>
      <SfChain at={step - 1}/>
      {step === 1 && <SfStage key="s1" keys={['C', 'D', 'E', 'F', 'G', 'A', 'B']} k={k1} setK={setK1} hand={hand} setHand={setHand} grid={tiny ? 4 : 7} titleFor={(n) => t('How do you play ' + n + ' major?', n + '장조는 어떻게 쳐요?')} go={go}/>}
      {step === 2 && <SfStage key="s2" keys={['Db', 'Eb', 'F#', 'Ab', 'Bb']} k={k2} setK={setK2} hand={hand} setHand={setHand} grid={tiny ? 5 : 5} titleFor={(n) => t('How do you play ' + n + ' major?', n + '장조는 어떻게 쳐요?')} go={go}/>}
      {step === 3 && <SfStage key="s3" keys={SF12} k={k3} setK={setK3} hand={hand} setHand={setHand} grid={tiny ? 4 : 6} titleFor={() => t('Twelve keys, a half step apart', '열두 조, 반음씩 올라가요')}/>}
      <div style={{textAlign:'center',marginTop:12}}><button className="ghost-btn" style={{minHeight:44,fontSize:13,fontWeight:700,color:'#5a5d8f'}} onClick={() => setStep(0)}>{t('Free play', '자유롭게')}</button></div>
    </div>
  );
}

'''
rep("// ─── Scale finder (Phase 135): any major or harmonic minor scale, straight away ───", "// ─── Scale finder (Phase 135): any major or harmonic minor scale, straight away ───")  # anchor check
# put the new wrapper after ScaleFinderFree (before ScalePath)
rep("function ScalePath({ sel, onPick, keys = SCALE_PATH, prefix = '', mode = 'major', cols = 3 }) {", NEW + "function ScalePath({ sel, onPick, keys = SCALE_PATH, prefix = '', mode = 'major', cols = 3 }) {")
rep("blurb: 'Type or tap any scale, major or minor (natural, harmonic, melodic): the steps and degrees, key signature, notes, fingering for both hands. Build one, stamp it, modes.'",
    "blurb: 'Three short steps: scales that start on a white key, on a black key, then all twelve a half step apart. Right hand, left hand, both. Free play for any scale, major or minor.'")
rep("'아무 스케일이나 입력하거나 눌러요. 장조와 단조(자연·화성·가락): 스텝과 음 번호, 조표, 음, 양손 손가락 번호. 직접 만들기, 도장, 선법까지.'", "'세 단계: 흰건반으로 시작하는 스케일, 검은건반으로 시작하는 스케일, 반음씩 올라가는 열두 조. 오른손, 왼손, 양손 순서예요. 맨 아래 “자유롭게”에서는 장조·단조 어떤 스케일이든 찾아요.'")
rep("'scale-finder': ['Type or tap any scale: its notes, steps and fingers.', '스케일을 입력하거나 눌러 보세요: 음, 온음과 반음, 손가락 번호.'],", "'scale-finder': ['Three short steps: white keys, black keys, all twelve.', '세 단계: 흰건반, 검은건반, 열두 조.'],")
rep('params="tool=scale-finder" label="Scale finder"', 'params="tool=scale-finder&key=C" label="Scale finder"')
rep("href={cbHref('tool=scale-finder')}", "href={cbHref('tool=scale-finder&key=C')}")
open(dst, 'w', encoding='utf-8').write(s)
print('patched 493', len(s))
