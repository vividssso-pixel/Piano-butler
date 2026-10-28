import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CR (board call 29; her 19:58: 'some children's practical and theory don't match; a diagnostic like this is also the
# hook that starts people on the drills'): Where should you start? Two ladders, apart: Piano (the practical rooms of each
# floor: ears, keys, scales, reading) and Theory (the theory rooms by Theory of Music grade, no sound). Each starts at the
# grade the child says they have passed (or the bottom), six quick questions a rung, five to climb; the first rung missed is
# the start (if the very first rung is missed, one rung lower is tried). The result: the piano floor and the theory grade,
# each with one room to start; the rooms missed on the floors passed are listed to look at. It is saved on the device, and the
# house's next room and 'you are here' start from that floor, with theory rooms above the placed theory grade left for later (call 24).
# Opened from the map's head ('Where should I start?') or by the link ?start=1.
CODE = r"""
// ══ Build CR: Where should you start? (board call 29) ══
const PLACE_KEY = 'pb_place_v1', PLACE_N = 6, PLACE_PASS = 5;
function loadPlace() { try { const v = JSON.parse(localStorage.getItem(PLACE_KEY)); return v && typeof v === 'object' ? v : null; } catch (e) { return null; } }
const placeFloor = () => { const p = loadPlace(); return p && p.piano > 0 ? p.piano : 0; };
function placeNext(ids, notDone) {   // the next room: from the placed floor up (theory rooms above the placed theory grade wait), then from the bottom
  const p = loadPlace(), k = placeFloor(), th = p && p.theory ? p.theory : 7;
  if (k > 0 && PATH_STAGES[k]) { const first = pathStageIds(PATH_STAGES[k])[0], i = ids.indexOf(first); if (i > 0) { const nx = ids.slice(i).find(id => notDone(id) && !(THEORY_ROOM[id] > th)); if (nx) return nx; } }
  return ids.find(notDone);
}
function placeLadders() {
  const piano = [], theory = [];
  PATH_STAGES.forEach((st, k) => { if (stageExtra(st)) return; const ids = pathStageIds(st).filter(id => CHECK_LV[id] && !THEORY_ROOM[id]); if (ids.length) piano.push({ k, ids }); });
  for (let n = 1; n <= 6; n++) { const ids = pathIds().filter(id => THEORY_ROOM[id] === n && CHECK_LV[id]); if (ids.length) theory.push({ n, ids }); }
  return { piano, theory };
}
function placeItems(ids, n, noSound) {   // n questions from as many rooms as possible; the theory ladder asks without sound or tapping
  const lv = (id) => chkLevels(id).filter(l => !(noSound && l.noPrint));
  const rooms = chkShuffle(ids.filter(id => lv(id).length)), out = [];
  let r = 0; while (out.length < n && rooms.length) { const id = rooms[r % rooms.length], L = lv(id); out.push({ id, lv: L[Math.floor(Math.random() * L.length)] }); r++; }
  return chkShuffle(out);
}
const PLACE_PIANO = [['0', 'Not yet', '아직'], ['P', 'Prelim', 'Prelim'], ['1', 'Grade 1', 'Grade 1'], ['2', '2', '2'], ['3', '3', '3'], ['4', '4', '4'], ['5', '5', '5'], ['6', '6', '6'], ['7', '7', '7'], ['8', '8', '8']];
const PLACE_THEORY = [['0', 'Not yet', '아직'], ['1', 'Grade 1', 'Grade 1'], ['2', '2', '2'], ['3', '3', '3'], ['4', '4', '4'], ['5', '5', '5'], ['6', '6', '6']];
const placeChips = (opts, val, set) => <div style={{display:'flex',gap:6,flexWrap:'wrap',marginBottom:10}}>{opts.map(([id, en, ko]) => <button key={id} className={'chip' + (id === val ? ' active' : '')} aria-pressed={id === val} style={{minHeight:40,padding:'6px 12px'}} onClick={() => set(id)}>{t(en, ko)}</button>)}</div>;
function placeStartRung(lad, said) {   // the rung of the grade the child says they have passed
  if (said === '0') return 0;
  const name = said === 'P' ? 'Prelim' : 'Grade ' + said, i = lad.findIndex(x => PATH_STAGES[x.k].en[0] === name);
  return Math.max(0, i);
}
function Placement({ onOpen, onClose }) {
  const lads = useMemo(() => placeLadders(), []);
  const [phase, setPhase] = useState('ask'), [pg, setPg] = useState('0'), [tg, setTg] = useState('0');
  const [track, setTrack] = useState('piano'), [rung, setRung] = useState(0), [items, setItems] = useState(null), [runKey, setRunKey] = useState(0);
  const [down, setDown] = useState(false), [last, setLast] = useState(null), [res, setRes] = useState({}), [miss, setMiss] = useState([]);
  const box = useRef(null);
  const lad = track === 'piano' ? lads.piano : lads.theory;
  const theoryStart = () => Math.max(0, Math.min(lads.theory.length - 1, (+tg || 1) - 1));
  const rungName = (tr, i) => tr === 'piano' ? floorName(lads.piano[i].k) : theoryName(lads.theory[i].n);
  const ask = (tr, i) => { const L = tr === 'piano' ? lads.piano : lads.theory; setTrack(tr); setRung(i); setItems(placeItems(L[i].ids, PLACE_N, tr === 'theory')); setRunKey(x => x + 1); setPhase('run'); try { box.current.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {} };
  const begin = () => { setRes({}); setMiss([]); setDown(false); ask('piano', placeStartRung(lads.piano, pg)); };
  const finish = (tr, startIdx) => {
    const out = { ...res, [tr]: startIdx };
    setRes(out);
    if (tr === 'piano') { setDown(false); setLast(null); setPhase('turn'); return; }
    const piano = lads.piano[out.piano] || lads.piano[lads.piano.length - 1], th = out.theory >= lads.theory.length ? null : lads.theory[out.theory];
    try { localStorage.setItem(PLACE_KEY, JSON.stringify({ piano: piano.k, theory: th ? th.n : 7, at: Date.now() })); } catch (e) {}
    setPhase('done');
  };
  const done = (r) => {
    const right = r.filter(x => x.ok).length, pass = right >= PLACE_PASS, missed = r.filter(x => !x.ok).map(x => x.id);
    setLast({ right, total: r.length, pass, name: rungName(track, rung) });
    if (pass) { setMiss(m => m.concat(missed)); if (rung + 1 < lad.length && !down) { setPhase('climb'); return; } finish(track, down ? rung + 1 : lad.length); return; }
    if (rung > 0 && !down && rung === (track === 'piano' ? placeStartRung(lads.piano, pg) : theoryStart())) { setDown(true); setPhase('lower'); return; }
    finish(track, rung);
  };
  const shell = (body) => <div ref={box} data-testid="placement" data-phase={phase} style={{...chkBox(false),margin:'12px 0 0',textAlign:'left'}}>
    <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',gap:8}}><div style={chkKicker}>{t('Where should you start?', '어디서 시작할까?')}</div><button className="chip" style={{padding:'2px 10px',fontSize:12}} onClick={onClose}>{t('Close', '닫기')}</button></div>{body}</div>;
  if (phase === 'ask') return shell(<>
    <div style={{fontSize:15,color:'#26296b',lineHeight:1.45,margin:'2px 0 8px'}}>{t('About ten minutes of quick questions, in two parts: piano (ears, keys, scales; sound on) and theory. They can be at different grades, and that is fine.', '빠른 문제로 10분쯤, 두 부분: 피아노(귀, 건반, 스케일; 소리 켜기)와 이론. 둘의 급이 달라도 괜찮아요.')}</div>
    <div style={{fontSize:13,fontWeight:800,color:'#4a4d86',margin:'4px 0 4px'}}>{t('Piano exam passed', '통과한 피아노 시험')}</div>
    {placeChips(PLACE_PIANO, pg, setPg)}
    <div style={{fontSize:13,fontWeight:800,color:'#4a4d86',margin:'2px 0 4px'}}>{t('Theory exam passed', '통과한 이론 시험')}</div>
    {placeChips(PLACE_THEORY, tg, setTg)}
    <div style={{fontSize:12.5,color:'#6d6f9c',margin:'0 0 8px'}}>{t('Not sure? Choose Not yet: the questions will find your level.', '잘 모르겠으면 ‘아직’을 골라요: 문제가 알아서 찾아 줘요.')}</div>
    <button className="primary-btn" data-testid="place-start" onClick={begin}>{t('Start →', '시작 →')}</button>
  </>);
  if (phase === 'run' && items) return shell(<>
    <div style={{fontSize:15,fontWeight:900,color:'#26296b',margin:'0 0 2px'}}>{(track === 'piano' ? t('Piano · ', '피아노 · ') : t('Theory · ', '이론 · ')) + rungName(track, rung)}</div>
    <div style={{display:'flex',gap:3,margin:'2px 0 0'}} aria-hidden="true">{lad.map((x, i) => <span key={i} style={{flex:1,height:5,borderRadius:3,background:i < rung ? '#26296b' : i === rung ? '#e4572e' : 'rgba(38,41,107,0.12)'}}/>)}</div>
    <CheckRun key={'p' + runKey} items={items} floor onDone={done} onQuit={onClose}/>
  </>);
  if (phase === 'climb' || phase === 'lower' || phase === 'turn') return shell(<div data-testid="place-step" style={{textAlign:'center',padding:'6px 0'}}>
    {last && <div style={{fontSize:34,fontWeight:900,color:'#26296b'}}>{last.right}<span style={{fontSize:17,color:'var(--muted)'}}> / {last.total}</span></div>}
    <div style={{fontSize:16,fontWeight:900,color:phase === 'climb' ? '#2e8a6e' : '#26296b',margin:'4px 0 10px'}}>{phase === 'climb' ? t(last.name + ': easy for you! Up a floor.', last.name + ': 쉽네요! 한 층 위로.') : phase === 'lower' ? t('That one was hard. Let’s try a floor lower.', '조금 어려웠어요. 한 층 아래로 가 봐요.') : t('Piano done! Now theory: no sound, just looking and thinking.', '피아노 끝! 이제 이론: 소리 없이, 보고 생각하기.')}</div>
    {phase === 'turn' && <div style={{fontSize:14,color:'#4a4d86',margin:'-4px 0 10px'}}>{t('Piano: ', '피아노: ') + floorName(lads.piano[Math.min(res.piano, lads.piano.length - 1)].k)}</div>}
    <button className="primary-btn" data-testid="place-next" onClick={() => phase === 'turn' ? ask('theory', theoryStart()) : ask(track, phase === 'climb' ? rung + 1 : rung - 1)}>{phase === 'climb' ? t('Next floor →', '다음 층 →') : phase === 'lower' ? t('One floor lower →', '한 층 아래 →') : t('Theory →', '이론 →')}</button>
  </div>);
  if (phase === 'done') {
    const p = lads.piano[Math.min(res.piano, lads.piano.length - 1)], allPiano = res.piano >= lads.piano.length, th = res.theory >= lads.theory.length ? null : lads.theory[res.theory];
    const firstRoom = pathStageIds(PATH_STAGES[p.k])[0], thFirst = th ? th.ids[0] : null;
    const room = (id) => <button key={id} className="chip" style={{fontSize:13,minHeight:36}} onClick={() => onOpen(id)}>{bkChapterNo(id) + ' · ' + bkChapterName(id)} ›</button>;
    const visit = [...new Set(miss)].filter(id => pathIds().indexOf(id) >= 0);
    return shell(<div data-testid="place-result" data-floor={p.k} data-theory={th ? th.n : 7} style={{textAlign:'center'}}>
      <CheckStamp text={t('START!', '출발!')} color="#26296b"/>
      <div style={{display:'grid',gap:10,textAlign:'left',margin:'6px 0 0'}}>
        <div style={{borderTop:'1px solid rgba(38,41,107,0.12)',paddingTop:8}}>
          <div style={{...chkKicker,margin:0}}>{t('Piano', '피아노')}</div>
          <div style={{fontSize:17,fontWeight:900,color:'#26296b'}}>{allPiano ? t('Every floor was easy. Start at the top: ', '모든 층이 쉬웠어요. 맨 위에서: ') + floorName(p.k) : floorName(p.k)}</div>
          <div style={{display:'flex',flexWrap:'wrap',gap:6,marginTop:6}}><button className="primary-btn" data-testid="place-go" style={{width:'auto',padding:'9px 14px',fontSize:14}} onClick={() => onOpen(firstRoom)}>{t('Start here: ', '여기서 시작: ') + bkChapterName(firstRoom) + ' →'}</button></div>
        </div>
        <div style={{borderTop:'1px solid rgba(38,41,107,0.12)',paddingTop:8}}>
          <div style={{...chkKicker,margin:0}}>{t('Theory', '이론')}</div>
          <div style={{fontSize:17,fontWeight:900,color:'#26296b'}}>{th ? theoryName(th.n) : t('Every theory grade was easy!', '모든 이론 급이 쉬웠어요!')}</div>
          {th && <div style={{display:'flex',flexWrap:'wrap',gap:6,marginTop:6}}><button className="primary-btn" data-testid="place-go-theory" style={{width:'auto',padding:'9px 14px',fontSize:14}} onClick={() => onOpen(thFirst)}>{t('Start here: ', '여기서 시작: ') + bkChapterName(thFirst) + ' →'}</button></div>}
        </div>
        {visit.length > 0 && <div style={{borderTop:'1px solid rgba(38,41,107,0.12)',paddingTop:8}}>
          <div style={{fontSize:13,fontWeight:800,color:'#4a4d86',margin:'0 0 4px'}}>{t('Missed on the way up: worth a quick look', '올라오다 틀린 방: 잠깐 들러 봐요')}</div>
          <div style={{display:'flex',flexWrap:'wrap',gap:6}}>{visit.slice(0, 6).map(room)}</div></div>}
      </div>
      <div style={{fontSize:12.5,color:'#6d6f9c',margin:'10px 0 0'}}>{t('Saved: the house now starts you on this floor. Do it again any time.', '저장했어요: 이제 집이 이 층부터 안내해요. 언제든 다시 해도 돼요.')}</div>
    </div>);
  }
  return null;
}
"""
rep("""// The top of the map page: the one chapter to open next, and "How it works" folded away until asked for.""", CODE + """// The top of the map page: the one chapter to open next, and "How it works" folded away until asked for.""")
# the map's head: a way in to the placement (and ?start=1)
rep("""function MapHead({ onOpen }) {
  const [help, setHelp] = useState(false);""", """function MapHead({ onOpen }) {
  const [help, setHelp] = useState(false);
  const [place, setPlace] = useState(() => BOOT_PARAMS.get('start') === '1'), [, setPt] = useState(0);   // Build CR""")
rep("""      <div style={{display:'flex',justifyContent:'flex-end',marginTop:8}}>
        <button className={'chip' + (help ? ' active' : '')} data-testid="map-help\"""", """      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',gap:8,flexWrap:'wrap',marginTop:8}}>
        <button className={'chip' + (place ? ' active' : '')} data-testid="map-place" aria-expanded={place} style={{padding:'3px 11px',fontSize:12.5,fontWeight:800}} onClick={() => setPlace(v => !v)}>{loadPlace() ? t('Find my start again ▸', '시작점 다시 찾기 ▸') : focus && focus.kind === 'start' ? t('Already playing? Find your start ▸', '이미 치고 있나요? 시작점 찾기 ▸') : t('Where should I start? ▸', '어디서 시작할까? ▸')}</button>
        <button className={'chip' + (help ? ' active' : '')} data-testid="map-help\"""")
rep("""      {help && <div data-testid="map-help-panel\"""", """      {place && <Placement onOpen={onOpen} onClose={() => { setPlace(false); setPt(x => x + 1); }}/>}
      {help && <div data-testid="map-help-panel\"""")
# the next room and 'you are here' start from the placed floor
rep("""  const nx = ids.find(id => status[id] !== 'done');
  return nx ? { id: nx, kind: ids.some(id => status[id] !== 'new') ? 'next' : 'start' } : null;""", """  const nx = placeNext(ids, id => status[id] !== 'done');   // Build CR: from the placed floor
  return nx ? { id: nx, kind: ids.some(id => status[id] !== 'new') ? 'next' : placeFloor() > 0 ? 'placed' : 'start' } : null;""")
rep("""focus.kind === 'next' ? t('Next on your path', '나의 경로에서 다음') : t('Start at the beginning', '처음부터 시작하기')""", """focus.kind === 'next' ? t('Next on your path', '나의 경로에서 다음') : focus.kind === 'placed' ? t('Your start', '나의 시작') : t('Start at the beginning', '처음부터 시작하기')""", 2)
rep("""  const here = last && all.includes(last) && chapterState(last).status !== 'done' ? last : all.find(id => chapterState(id).status !== 'done');""", """  const here = last && all.includes(last) && chapterState(last).status !== 'done' ? last : placeNext(all, id => chapterState(id).status !== 'done');""", 2)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
