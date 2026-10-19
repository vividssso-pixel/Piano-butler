import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
# --- KSStaff: the key note on the staff
rep("numbers, onPick, ghostPos, ring }) {","numbers, onPick, ghostPos, ring, tonicPos, tonicFrom, tallBox }) {   // Phase 516: tonicPos = draw the key note at this staff step; tonicFrom = step of the sign it comes from (draws the half-step arrow)")
rep("      {ring != null && ring >= 0 && ring < accs.length &&",
"""      {tonicPos != null && (() => {
        const nx = (accs.length ? xs[accs.length - 1] : 56) + 26, ny = yPos(tonicPos), ledgers = [];
        for (let p = 10; p <= tonicPos; p += 2) ledgers.push(p);
        for (let p = -2; p >= tonicPos; p -= 2) ledgers.push(p);
        const fx = accs.length ? xs[accs.length - 1] : 56, fy = tonicFrom != null ? yPos(tonicFrom) : null;
        return <g style={{animation:'fadeUp 0.35s both'}}>
          {ledgers.map(p => <line key={p} x1={nx - 10} x2={nx + 10} y1={yPos(p)} y2={yPos(p)} stroke={ink} strokeOpacity="0.5" strokeWidth="1.1"/>)}
          {fy != null && <><path d={`M${fx + 9},${fy} Q${fx + 20},${(fy + ny) / 2 - 7} ${nx - 8},${ny + 1}`} fill="none" stroke="#c8361b" strokeWidth="1.7" strokeLinecap="round"/><text x={fx + 20} y={Math.min(fy, ny) - 8} fontSize="9" fontWeight="900" fill="#c8361b">½↑</text></>}
          <ellipse cx={nx} cy={ny} rx="6.2" ry="4.5" fill="#c0431f" transform={`rotate(-18 ${nx} ${ny})`}/>
        </g>;
      })()}
      {ring != null && ring >= 0 && ring < accs.length &&""")
# --- KfRule with three examples
i=s.index("function KfRule("); j=s.index("function KfMajor(")
new = r"""function KfRule({ type, go, back }) {
  const kc = React.useContext(KfCtx), sharp = type === 'sharp';
  const [r, setR] = useState(0);   // 0 = circle the sign, 1 = what the circle tells you
  const [e, setE] = useState(0);   // Phase 516: three examples with different counts
  const EX = sharp ? [3, 5, 2] : [3, 5, 2];
  const n = EX[e], k = KEY_BY_COUNT(type, n), marks = {};
  const want = sharp ? n - 1 : n - 2;
  const lastNm = (sharp ? SHARP_ORDER : FLAT_ORDER)[want];
  marks[pcOfName(lastNm)] = r === 0 ? 'pick' : 'mate';
  if (r === 1) marks[pcOfName(k.major)] = 'pick';
  const head = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const say = r === 0
    ? (sharp ? t('1. Find the last ♯ and circle it.', '1. 마지막 샤프를 찾아 동그라미 쳐요.') : t('1. Find the second-to-last ♭ and circle it.', '1. 뒤에서 두 번째 플랫을 찾아 동그라미 쳐요.'))
    : (sharp ? t('2. Go up one half step. That is the key.', '2. 반음 위로 올라가요. 그게 바로 그 조예요.') : t('2. That ♭ is the key.', '2. 그 플랫이 바로 그 조예요.'));
  const tonicPos = r === 1 ? (sharp ? SHARP_POS[lastNm] + 1 : FLAT_POS[lastNm]) : undefined;
  const more = e < EX.length - 1;
  return (<>
    <KfChain hi={[1]}/>
    <div style={head}>{sharp ? t('Sharps: find the key', '샤프로 조 찾기') : t('Flats: find the key', '플랫으로 조 찾기')}</div>
    <div key={r + '-' + e} style={{textAlign:'center',fontSize:16,fontWeight:800,color:'#26296b',margin:'0 0 8px',textWrap:'balance',minHeight:40,animation:'fadeUp 0.3s both'}}>{say}</div>
    <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={n} type={type} width={200} ring={want} tonicPos={tonicPos} tonicFrom={sharp && r === 1 ? SHARP_POS[lastNm] : undefined}/></div>
    <div style={{maxWidth:300,margin:'4px auto 0'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels/></div>
    <div style={{...head,margin:'6px 0 2px',minHeight:27,visibility:r === 1 ? 'visible' : 'hidden'}}>{n}{sharp ? '♯' : '♭'} → <span style={{color:'#c0431f'}}>{majName(k)}</span></div>
    <div style={{textAlign:'center',fontSize:12,color:'#5a5d8f',minHeight:16}}>{sharp ? '' : (r === 1 && n === 2 ? '' : '')}{!sharp && r === 0 ? t('One ♭ is the exception: it is F.', '플랫이 하나면 예외예요: F.') : ''}</div>
    <div style={{textAlign:'center',marginTop:10,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
      {r === 1 ? <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => setR(0)}>{t('← Back', '← 이전')}</button>
        : (back || (kc && kc.step > 1)) && <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={back || (() => kc && kc.setStep(1))}>{t('← Back', '← 이전')}</button>}
      <button className="ghost-btn" style={{...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={r === 0 ? () => { setR(1); playKey(pcOfName(k.major), 0.5); } : more ? () => { setE(e + 1); setR(0); } : go}>{r === 0 ? t('Next →', '다음 →') : more ? t('Another one →', '다른 예 →') : t('Try it →', '해 보기 →')}</button>
    </div>
  </>);
}
"""
s=s[:i]+new+s[j:]
# --- KfMajor: one side only
rep("function KfMajor({ go, setKi }) {\n  const [st, setSt] = useState('sharp-rule');","function KfMajor({ go, setKi, which }) {   // which: 'sharp' or 'flat' = that side on its own (Phase 516)\n  const [st, setSt] = useState(which === 'flat' ? 'flat-rule' : 'sharp-rule');")
rep("go={() => setSt('flat-rule')} goLabel={t('Now flats →', '이제 플랫 →')}","go={which === 'sharp' ? undefined : () => setSt('flat-rule')} goLabel={t('Now flats →', '이제 플랫 →')}")
rep("<KfRule type=\"flat\" go={() => setSt('flat')} back={() => setSt('sharp')}/>","<KfRule type=\"flat\" go={() => setSt('flat')} back={which === 'flat' ? undefined : () => setSt('sharp')}/>")
# --- KeyFinder only
rep("        {only === 'major' && <KfMajor setKi={setKi}/>}","        {only === 'major' && <KfMajor setKi={setKi}/>}\n        {only === 'msharp' && <KfMajor which=\"sharp\" setKi={setKi}/>}\n        {only === 'mflat' && <KfMajor which=\"flat\" setKi={setKi}/>}")
rep(" ['kf-major', 'major', 'Find the major key', '장조 찾기', 'The sharp way, then the flat way.', '샤프로 찾는 법, 그다음 플랫으로 찾는 법.'],",
    " ['kf-major', 'major', 'Find the major key', '장조 찾기', 'The sharp way, then the flat way.', '샤프로 찾는 법, 그다음 플랫으로 찾는 법.'],\n ['kf-msharp', 'msharp', 'Major key: sharps', '장조 찾기: 샤프', 'Circle the last sharp, go up a half step.', '마지막 샤프에 동그라미, 반음 위로.'],\n ['kf-mflat', 'mflat', 'Major key: flats', '장조 찾기: 플랫', 'Circle the second-to-last flat: that is the key.', '뒤에서 두 번째 플랫에 동그라미: 그게 그 조.'],")
rep("lessons: ['kf-sharps', 'kf-flats', 'kf-major', 'kf-minor', 'kf-piece'], check: 'key-signatures'","lessons: ['kf-sharps', 'kf-flats', 'kf-msharp', 'kf-mflat', 'kf-minor', 'kf-piece'], check: 'key-signatures'")
i0=s.index("function KSStaff("); i1=s.index("\nconst KEYSIG_LEVELS")
blk=s[i0:i1]
assert blk.count("numbers ? 72 : 60")==4 or True
blk=blk.replace("numbers ? 72 : 60","tall ? 72 : 60").replace("numbers ? 90 : 78","tall ? 90 : 78")
blk=blk.replace("  const order = type === 'sharp' ? SHARP_ORDER : FLAT_ORDER;\n  const posMap","  const tall = numbers || tallBox;\n  const order = type === 'sharp' ? SHARP_ORDER : FLAT_ORDER;\n  const posMap",1)
s=s[:i0]+blk+s[i1:]
rep("ring={want} tonicPos={tonicPos}","ring={want} tallBox={sharp} tonicPos={tonicPos}")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
