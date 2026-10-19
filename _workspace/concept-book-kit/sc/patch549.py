import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)

# Key signatures: a new first card, 'What a key signature does' (her 15:12 note: the sign applies to every note of that letter, in every octave)
rep("function KeyFinder({ only }) {\n  const [step, setStep] = useState(1);",
r"""const KF_WHAT_ROW = [['q', 1, 31], ['q', 1, 34], ['q', 1, 35], ['q', 1, 38], ['q', 1, 36], ['q', 1, 31], ['||']];   // F B C, the F an octave up, D, F
function KfWhat() {
  const [view, setView] = useState('all');   // 'all' (the whole picture, G major) -> 'try' (pick another key)
  const [k, setK] = useState('G'), [n, setN] = useState(0);
  const timers = useRef([]);
  const clear = () => { timers.current.forEach(clearTimeout); timers.current = []; };
  useEffect(() => clear, []);
  const map = skgMap(k), L = Object.keys(map), sign = SKG_KEY[k][0] === '#' ? 'sharp' : 'flat';
  const hits = KF_WHAT_ROW.map((it, j) => it.length === 3 && L.includes(dName(it[2])) ? j : -1).filter(j => j >= 0);
  useEffect(() => { clear(); setN(0); hits.forEach((j, i) => timers.current.push(setTimeout(() => setN(i + 1), 700 + i * 650))); return clear; }, [k, view]);
  const titleStyle = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const lineStyle = {textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:42,textWrap:'balance',wordBreak:'keep-all'};
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const letters = L.map(prettyNote === undefined ? (x => x) : (x => x)).join(t(' and every ', '와 모든 '));
  const word = sign === 'sharp' ? t('a sharp', '샵') : t('a flat', '플랫');
  const done = n >= hits.length;
  const line = view === 'all'
    ? (done ? t('The ♯ on the F line is in the key signature. Every F is sharp: the low ones and the high one.', '조표의 ♯이 F 줄에 있어요. 낮은 F도 높은 F도, 모든 F가 샵이에요.') : '')
    : (done ? t('Every ' + letters + ' gets ' + word + ', in every octave.', '모든 ' + letters + '에 ' + word + '이 붙어요, 어느 옥타브에서나.') : '');
  return (
    <div className="try-box" data-kf-lesson="what" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>
      <div style={titleStyle}>{view === 'all' ? t('What a key signature does', '조표가 하는 일') : t('Your turn', '내가 해보기')}</div>
      {view === 'try' && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>
        {['G', 'D', 'F', 'Bb'].map(x => <button key={x} className={'chip' + (k === x ? ' active' : '')} aria-pressed={k === x} style={{...KF_BTN,padding:'0 12px',fontSize:14}} onClick={() => setK(x)}>{skgKeyName(x)}</button>)}
      </div>}
      <div style={{background:'#fff',maxWidth:300,margin:'0 auto 6px'}}><SkgStaff items={KF_WHAT_ROW} k={k} width={340} full o={{ D: 22, hl: hits.slice(0, n), base: 54 }}/></div>
      <div style={lineStyle}>{line}</div>
      <div style={{textAlign:'center',marginTop:12,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
        {view === 'try' && <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setK('G'); setView('all'); }}>{t('← Back', '← 이전')}</button>}
        {view === 'all' && <button className="ghost-btn" style={prim} onClick={() => setView('try')}>{t('Your turn →', '내가 해보기 →')}</button>}
      </div>
    </div>);
}
function KeyFinder({ only }) {
  const [step, setStep] = useState(1);""")
rep("        {only === 'sharps' && <KfFind key=\"os\" type=\"sharp\" mode=\"order\" setKi={setKi}/>}", "        {only === 'what' && <KfWhat/>}\n        {only === 'sharps' && <KfFind key=\"os\" type=\"sharp\" mode=\"order\" setKi={setKi}/>}")
rep("[['kf-sharps', 'sharps', 'Sharp order',", "[['kf-what', 'what', 'What a key signature does', '조표가 하는 일', 'A sharp or flat in it counts for every note of that letter.', '조표의 샵과 플랫은 그 글자의 모든 음에 붙어요.'],\n ['kf-sharps', 'sharps', 'Sharp order',")
rep("lessons: ['kf-sharps', 'kf-flats',", "lessons: ['kf-what', 'kf-sharps', 'kf-flats',")
for a,b in [("num: '1', kind: 'kn-ordS'","num: '2', kind: 'kn-ordS'"),("num: '2', kind: 'kn-ordF'","num: '3', kind: 'kn-ordF'"),("num: '3', kind: 'kn-majS'","num: '4', kind: 'kn-majS'"),("num: '4', kind: 'kn-majF'","num: '5', kind: 'kn-majF'"),("num: '3+4', kind: 'kn-maj15'","num: '4+5', kind: 'kn-maj15'"),("num: '5', kind: 'kn-min'","num: '6', kind: 'kn-min'"),("num: '6', kind: 'kn-last'","num: '7', kind: 'kn-last'")]:
    rep(a,b)
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
