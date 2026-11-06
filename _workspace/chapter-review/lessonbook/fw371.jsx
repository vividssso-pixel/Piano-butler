// ─── Phase 371: Play: finger walks (chapter 1, the Lesson Book's page 6 as the app's moving version) ───
// Start small: one note, then two, three, four, five. One circle is one steady beat; an empty dashed circle holds the
// note for one more beat. "Play along" lights the circles at a steady 72 and sounds each finger (right hand C-G,
// left hand C-G an octave lower, finger 5 on C). The hand pictures are the Lesson Book's (art369.jsx).
const FW_TUNES = [
  { icon: 'tune-hop', en: 'Hop on 3', ko: '3번으로 깡충', howEn: 'one note: an arm drop on every 3', howKo: '한 음: 3번을 칠 때마다 팔 떨어뜨리기', seq: ['3', '-', '3', '-', '|', '3', '3', '3', '-'] },
  { icon: 'tune-neighbours', en: 'Neighbours', ko: '이웃사촌', howEn: 'two notes, next door, taking turns', howKo: '두 음: 옆집 손가락끼리 번갈아', seq: ['2', '3', '2', '3', '|', '3', '2', '3', '-'] },
  { icon: 'tune-hill3', en: 'Up and back', ko: '올라갔다 내려오기', howEn: 'three notes: up, then back down', howKo: '세 음: 올라갔다가 다시 내려와요', seq: ['1', '2', '3', '-', '|', '3', '2', '1', '-'] },
  { icon: 'tune-hill4', en: 'Little hill', ko: '작은 언덕', howEn: 'four notes: up the hill and down', howKo: '네 음: 언덕을 올라갔다 내려와요', seq: ['1', '2', '3', '4', '|', '3', '2', '1', '-'] },
  { icon: 'tune-stairs', en: 'Stairs and slide', ko: '계단과 미끄럼틀', howEn: 'all five: up the stairs, then down the slide', howKo: '다섯 음: 계단을 올라가서 미끄럼틀로 내려와요', seq: ['1', '2', '3', '4', '5', '-', '|', '5', '4', '3', '2', '1', '-'] },
];
function FingerWalks() {
  const [tune, setTune] = useState(0);
  const [hand, setHand] = useState('R');
  const [pos, setPos] = useState(-1);
  const timer = useRef(null);
  const T = FW_TUNES[tune];
  const stop = () => { clearInterval(timer.current); timer.current = null; setPos(-1); };
  function play() {
    stop();
    const beats = T.seq.map((x, i) => [x, i]).filter(([x]) => x !== '|');
    let k = 0;
    const tick = () => {
      if (k >= beats.length) { stop(); return; }
      const [x, i] = beats[k]; setPos(i);
      const ctx = getAudio();
      if (ctx && x !== '-') {
        const semis = [0, 2, 4, 5, 7], f = +x, st = hand === 'R' ? semis[f - 1] : semis[5 - f];
        blip(ctx, ctx.currentTime + 0.01, 262 * Math.pow(2, st / 12) * (hand === 'L' ? 0.5 : 1), 0.32, 0.16, 'triangle');
      }
      k++;
    };
    tick(); timer.current = setInterval(tick, 60000 / 72);
  }
  useEffect(() => () => clearInterval(timer.current), []);
  useEffect(() => { stop(); }, [tune, hand]);
  const navy = '#26296b', coral = '#e4572e';
  return (
    <div className="try-box" style={actBox}>
      <div style={actTitle}>{t('Play: finger walks', '연주: 손가락 걷기')}</div>
      <div style={actNote}>{LANG === 'ko'
        ? <>앉은 자세, 둥근 손으로 쳐 봐요. <b>작게 시작해요:</b> 한 음, 그다음 두 음, 세 음, 네 음, 다섯 음. 건반에서 건반으로 손이 작은 <b>무지개</b>를 그려요: 꽉 쥐지 않고 편하게, 손 전체가 도와줘요. <b>동그라미 하나가 일정한 박 하나</b>예요.</>
        : <>Sit well, make a round hand, and play. <b>Start small:</b> one note, then two, three, four, and all five. From key to key, the hand draws a little <b>rainbow</b>: relaxed, never squeezed tight, the whole hand helping. <b>One circle is one steady beat.</b></>}</div>
      <div style={{display:'flex',justifyContent:'center',gap:18,margin:'2px 0 8px'}}>
        {['L', 'R'].map(h => (
          <button key={h} onClick={() => setHand(h)} aria-pressed={hand === h} style={{border:'2px solid ' + (hand === h ? navy : 'transparent'),borderRadius:12,background:'#fff',padding:'4px 6px',cursor:'pointer',opacity:hand === h ? 1 : 0.5}}>
            <PbArt name={'keys-hand-' + h} h={112}/>
          </button>))}
      </div>
      <div style={{display:'flex',flexWrap:'wrap',gap:4,marginBottom:8}}>
        {FW_TUNES.map((x, i) => <button key={i} className={'chip' + (i === tune ? ' active' : '')} style={{padding:'3px 9px',fontSize:12.5}} onClick={() => setTune(i)}>{i + 1}. {t(x.en, x.ko)}</button>)}
      </div>
      <div style={{background:'#fff',borderRadius:12,padding:'8px 10px',display:'flex',alignItems:'center',gap:12}}>
        <PbArt name={T.icon} h={58}/>
        <div style={{flex:1,minWidth:0}}>
          <div style={{fontSize:13,color:'var(--muted)',marginBottom:6}}>{t(T.howEn, T.howKo)} · {hand === 'R' ? t('right hand', '오른손') : t('left hand', '왼손')}</div>
          <div style={{display:'flex',flexWrap:'wrap',alignItems:'center',gap:6}}>
            {T.seq.map((x, i) => x === '|' ? <span key={i} style={{width:1.6,height:28,background:navy,opacity:0.5,margin:'0 4px'}}/>
              : x === '-' ? <span key={i} style={{width:28,height:28,borderRadius:14,border:'1.6px dashed ' + (pos === i ? coral : '#cfc6b2'),background:pos === i ? '#fde9e1' : 'transparent',transition:'background 0.15s'}}/>
              : <span key={i} style={{width:28,height:28,borderRadius:14,background:pos === i ? coral : '#fff',border:'2px solid ' + (pos === i ? coral : navy),display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14.5,fontWeight:900,color:pos === i ? '#fff' : navy,transition:'background 0.15s'}}>{x}</span>)}
          </div>
        </div>
      </div>
      <div style={{display:'flex',justifyContent:'center',gap:8,marginTop:8}}>
        {pos < 0 ? <button className="ghost-btn" style={{padding:'6px 16px',fontWeight:800}} onClick={play}>{t('▶ Play along', '▶ 따라 치기')}</button>
          : <button className="ghost-btn" style={{padding:'6px 16px',fontWeight:800}} onClick={stop}>{t('■ Stop', '■ 멈추기')}</button>}
      </div>
      <div style={{fontSize:12.5,color:'var(--muted)',marginTop:8,lineHeight:1.45}}>{t('An empty dashed circle means: hold the note for one more beat. Move on to the next tune only when the hand stays round.', '빈 점선 동그라미는 그 음을 한 박 더 누르고 있으라는 뜻이에요. 손이 둥글게 유지될 때 다음 곡으로 넘어가요.')}</div>
    </div>
  );
}
