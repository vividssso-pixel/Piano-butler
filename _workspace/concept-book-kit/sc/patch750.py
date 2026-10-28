import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CE (call 25, batch 4; her 09:56: everything must be fun, the How to Blitz way): the Beginner floor's things to make.
# Five rooms that had none get one each, each a game with a goal to chase:
#   Music alphabet: My word tune (spell real words with A to G on the keys, hear them, collect them; riddles; secret words)
#   Line and space names: Words on the staff (the same game on the treble or the bass staff; FACE up the treble spaces)
#   Hand positions: My tune moves (write a tune with finger numbers, play it in C position, then in G: the same tune, higher)
#   Ear prep: Trick your teacher (make two rhythms or two tunes, the same or with one change; the teacher guesses; a score)
#   Tones and semitones: Build a scale (seven steps, each a best friend or a friend of a friend; land on C; find the major
#     and minor patterns; three stars to earn)
# Her metaphors only (best friend and friend of a friend; walk and run-ning; turtle and bird), no new ones.

CODE = r'''
// ══ Build CE: batch 4, the Beginner floor's things to make (call 25; her 09:56: fun first) ══
// ── words from the music alphabet (Music alphabet, Line and space names) ──
const WG_WORDS = ['ACE', 'ADD', 'AGE', 'BAD', 'BAG', 'BED', 'BEE', 'BEG', 'CAB', 'DAD', 'EGG', 'FED', 'FEE', 'BEAD', 'CAFE', 'CAGE', 'DEAF', 'FACE', 'FADE', 'BADGE', 'CABBAGE', 'BAGGAGE', 'DECADE'];
const WG_HINT = { CABBAGE: ['A round green vegetable, seven letters long.', '양배추를 영어로. 일곱 글자!'], FACE: ['Your eyes, nose and mouth live here.', '얼굴을 영어로.'], BEE: ['It buzzes and makes honey.', '꿀벌을 영어로.'],
  CAGE: ['A bird might live in one.', '새장을 영어로.'], BAG: ['You carry your books in it.', '가방을 영어로.'], EGG: ['A chicken lays one.', '달걀을 영어로.'], BED: ['You sleep in it.', '침대를 영어로.'],
  CAFE: ['A place for a hot chocolate.', '카페를 영어로.'], DAD: ['Mum and …', '아빠를 영어로.'], BADGE: ['A pin to wear on your jumper.', '배지를 영어로.'], BAGGAGE: ['All the bags you take on a trip.', '여행 짐을 영어로.'], DECADE: ['Ten years.', '10년을 영어로.'] };
const WG_PC = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const wgLetter = (k) => ({ 0: 'C', 2: 'D', 4: 'E', 5: 'F', 7: 'G', 9: 'A', 11: 'B' })[spPc(k)] || null;
// on the staff: the treble from F up to E (so F A C E climbs the spaces), the bass from A up to G (A C E G, its spaces)
const wgD = (L, clef) => clef === 'bass' ? 19 + 'ABCDEFG'.indexOf(L) : 31 + 'FGABCDE'.indexOf(L);
const wgLoad = (k) => { try { return JSON.parse(localStorage.getItem(k)) || []; } catch (e) { return []; } };
function WordGame({ view = 'keys', store }) {
  const T = useSpTimers();
  const [mode, setMode] = useState('make'), [clef, setClef] = useState('treble'), [word, setWord] = useState([]), [hide, setHide] = useState(false), [on, setOn] = useState(-1), [msg, setMsg] = useState(null);
  const [found, setFound] = useState(() => wgLoad(store)), [secret, setSecret] = useState(null), [guess, setGuess] = useState([]), [res, setRes] = useState(null), [streak, setStreak] = useState(0);
  const item = (L) => (view === 'keys' ? { L, k: WG_PC[L] } : { L, d: wgD(L, clef) });
  const semi = (x) => (x.k != null ? x.k : hpSemi(x.d));
  const play = (xs) => { T.clear(); const r = spPlay(xs.map((x, j) => ({ at: j * 0.6, keys: [semi(x)], len: 0.5, vol: 0.14 })), 60); if (!r) return; xs.forEach((_, j) => T.at(r.ms(j * 0.6), () => setOn(j))); T.at(r.ms(xs.length * 0.6), () => setOn(-1)); };
  const keep = (w) => { if (found.includes(w)) return false; const nf = found.concat([w]); setFound(nf); try { localStorage.setItem(store, JSON.stringify(nf)); } catch (e) {} return true; };
  const add = (x) => { if (mode !== 'make' || word.length >= 7) return; const nw = word.concat([x]), w = nw.map(y => y.L).join(''); setWord(nw); playKey(semi(x), 0.5);
    if (WG_WORDS.includes(w)) { const fresh = keep(w); setMsg({ ok: true, w, fresh }); setTimeout(() => play(nw), 500); } else setMsg(null); };
  const newSecret = () => { const pool = WG_WORDS.filter(w => !found.includes(w) && w.length <= 5), list = pool.length ? pool : WG_WORDS; let w, g = 0; do { w = pick(list); } while (secret && w === secret && g++ < 10);
    const xs = w.split('').map(item); setSecret(w); setGuess([]); setRes(null); setTimeout(() => play(xs), 300); };
  const tapLetter = (L) => { if (mode === 'make') { add(item(L)); return; } if (!secret || res) return; const g = guess.concat([L]); setGuess(g); playKey(semi(item(L)), 0.4);
    if (g.length >= secret.length) { const ok = g.join('') === secret; setRes(ok ? 'ok' : 'no'); setStreak(n => (ok ? n + 1 : 0)); if (ok) keep(secret); } };
  const shown = mode === 'make' ? word : secret ? secret.split('').map(item) : [];
  const tiles = mode === 'make' ? word.map(x => x.L) : secret ? secret.split('').map((L, j) => (res ? L : guess[j] || '?')) : [];
  const miss = (j) => res === 'no' && guess[j] !== secret[j];
  const hint = WG_WORDS.find(w => !found.includes(w) && WG_HINT[w]);
  const keysLit = {}, keysNames = {};
  if (view === 'keys') { shown.forEach((x, j) => { if (mode === 'make' || res || j === on) keysLit[x.k] = j === on ? 'cor' : 'pale'; });
    if ((!hide && mode === 'make') || res) [-12, -10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11].forEach(k => { keysNames[k] = wgLetter(k); }); }
  return (
    <div className="try-box" style={actBox} data-mk={view === 'keys' ? 'word' : 'staffword'}>
      <div style={actTitle}>{view === 'keys' ? t('My word tune', '나의 낱말 선율') : t('Words on the staff', '오선 위의 낱말')}</div>
      <div style={actNote}>{view === 'keys' ? (LANG === 'ko' ? <>음악 알파벳은 A부터 G까지 일곱 글자뿐이에요. 그런데 이 글자로 <b>진짜 영어 낱말</b>을 만들 수 있어요: CAFE, FACE, CABBAGE! 건반을 눌러 낱말을 만들면 선율이 돼요. 몇 개나 모을까요?</> : <>The music alphabet has only seven letters, A to G. But they spell <b>real words</b>: CAFE, FACE, even CABBAGE! Spell a word on the keys and it becomes a tune. How many can you collect?</>)
        : (LANG === 'ko' ? <>글자를 누르면 오선에 음이 생겨요. 높은음자리표의 칸은 아래부터 <b>F A C E</b>, 낱말 FACE예요! 낮은음자리표의 칸은 <b>A C E G</b>. 낱말을 만들어 보고, 비밀 낱말도 읽어 봐요.</> : <>Tap the letters and the notes land on the staff. The treble staff's spaces, from the bottom, spell <b>F A C E</b>: FACE! The bass staff's spaces are <b>A C E G</b>. Write words, then read secret ones.</>)}</div>
      {spChips([['make', t('Spell a word', '낱말 만들기')], ['secret', t('Secret word', '비밀 낱말')]], mode, (m) => { T.clear(); setMode(m); setWord([]); setMsg(null); setSecret(null); setGuess([]); setRes(null); setOn(-1); if (m === 'secret') setTimeout(newSecret, 50); })}
      {view === 'staff' && spChips([['treble', t('Treble clef', '높은음자리표')], ['bass', t('Bass clef', '낮은음자리표')]], clef, (c) => { T.clear(); setClef(c); setWord([]); setMsg(null); setSecret(null); setGuess([]); setRes(null); if (mode === 'secret') setTimeout(newSecret, 50); })}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',minHeight:46,margin:'4px 0 8px'}}>{tiles.length ? tiles.map((L, j) => <span key={j} style={{width:38,height:44,borderRadius:8,display:'inline-flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:24,fontWeight:900,
        border:'2px solid ' + (j === on || miss(j) ? BK.coral : res === 'ok' || (mode === 'make' && msg && msg.ok) ? BK.green : BK.ink),background:j === on || miss(j) ? '#fbe3da' : '#fff',color:L === '?' ? BK.muted : BK.ink}}>{L}</span>)
        : <span style={{alignSelf:'center',fontSize:14,color:BK.muted}}>{mode === 'make' ? t('Tap a letter to start.', '글자를 눌러 시작해요.') : ''}</span>}</div>
      {view === 'keys'
        ? <SpKb lo={-12} hi={11} W={24} H={80} lit={keysLit} names={keysNames} onTap={(k) => { const L = wgLetter(k); if (!L) { playKey(k, 0.4); setMsg({ black: true }); return; } if (mode === 'make') add({ L, k }); else tapLetter(L); }} label={t('Spell on the keys', '건반으로 글자 쓰기')}/>
        : <div style={{background:'#fff',borderRadius:8,padding:'2px 0',maxWidth:360,margin:'0 auto'}}><MelodyStaff notes={shown.map(x => ({ d: x.d, dur: 1 }))} beats={Math.max(4, shown.length)} clef={clef} width={330} on={on} names={mode === 'make' || !!res} showTime={false}/></div>}
      {(view === 'staff' || mode === 'secret') && <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:5,marginTop:8}}>{'ABCDEFG'.split('').map(L => <button key={L} className="choice-btn" onClick={() => tapLetter(L)} style={{padding:'10px 0',fontSize:18,fontWeight:900,fontFamily:LB_SERIF}}>{L}</button>)}</div>}
      {spMsg(msg && msg.black ? t('A black key has no plain letter of its own: pick a white one.', '검은건반은 자기만의 글자가 없어요: 흰건반을 골라요.')
        : msg && msg.ok ? t('★ A real word: ' + msg.w + '!' + (msg.fresh ? ' New for your collection.' : ''), '★ 진짜 낱말: ' + msg.w + '!' + (msg.fresh ? ' 새로 모았어요.' : ''))
        : res === 'ok' ? t('You read it: ' + secret + '!' + (streak > 1 ? ' ' + streak + ' in a row!' : ''), '읽었어요: ' + secret + '!' + (streak > 1 ? ' ' + streak + '개 연속!' : ''))
        : res === 'no' ? t('Nearly! It was ' + secret + '. Listen again and read it from the ' + (view === 'keys' ? 'keys' : 'staff') + '.', '거의! 정답은 ' + secret + '. 다시 듣고 ' + (view === 'keys' ? '건반' : '오선') + '에서 읽어 봐요.')
        : mode === 'secret' && secret ? t('Read the ' + (view === 'keys' ? 'keys as they light up' : 'notes') + ', then tap the letters.', (view === 'keys' ? '불이 켜지는 건반' : '음표') + '를 읽고, 글자를 눌러요.') : '', res === 'no' ? BK.coral : (msg && msg.ok) || res === 'ok' ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {shown.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => play(shown)}>{t('▶ Play it', '▶ 들어 보기')}</button>}
        {mode === 'make' && word.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setWord(word.slice(0, -1)); setMsg(null); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
        {mode === 'make' && word.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setWord([]); setMsg(null); }}>{t('Clear', '처음부터')}</button>}
        {mode === 'secret' && (res || !secret) && <button className="ghost-btn" style={spBtn} onClick={newSecret}>{t('▶ Another secret word', '▶ 다른 비밀 낱말')}</button>}
        {mode === 'secret' && secret && !res && guess.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => setGuess(guess.slice(0, -1))}>{t('⌫ Back', '⌫ 지우기')}</button>}
        {view === 'keys' && mode === 'make' && <button className={'chip' + (hide ? ' active' : '')} aria-pressed={hide} style={{minHeight:44,padding:'4px 12px'}} onClick={() => setHide(!hide)}>{t('Hide the letters', '글자 숨기기')}</button>}
      </div>
      <div style={{marginTop:10,borderTop:'1px solid ' + BK.line,paddingTop:8}}>
        <div style={{fontSize:13,fontWeight:900,color:BK.ink}}>{t('My words: ' + found.length + ' of ' + WG_WORDS.length, '모은 낱말: ' + WG_WORDS.length + '개 중 ' + found.length + '개')}</div>
        {found.length > 0 && <div style={{display:'flex',gap:4,flexWrap:'wrap',marginTop:4}}>{found.map(w => <span key={w} style={{fontSize:12,fontWeight:800,padding:'2px 8px',borderRadius:10,border:'1px solid ' + BK.green,color:BK.green}}>{w}</span>)}</div>}
        {hint && mode === 'make' && <div style={{fontSize:13,color:BK.muted,marginTop:6}}>{t('Riddle: ' + WG_HINT[hint][0] + ' (' + hint.length + ' letters)', '수수께끼: ' + WG_HINT[hint][1] + ' (' + hint.length + '글자)')}</div>}
      </div>
    </div>
  );
}
function WordTune() { return <WordGame view="keys" store="pb_mk_word"/>; }
function StaffWords() { return <WordGame view="staff" store="pb_mk_staffword"/>; }

// ── Hand positions: My tune moves ──
const MT_SONGS = [['Hot cross buns', '핫 크로스 번', [3, 2, 1, 3, 2, 1]], ['Mary had a little lamb', '메리의 어린 양', [3, 2, 1, 2, 3, 3, 3]]];
function MoveTune() {
  const T = useSpTimers();
  const [tune, setTune] = useState([1, 2, 3, 1]), [pos, setPos] = useState('C'), [on, setOn] = useState(-1), [heard, setHeard] = useState({});
  const ds = (p) => tune.map(f => hpFingerD(p, 'R', f));
  const play = (ps) => { T.clear(); let at = 0; const ev = []; ps.forEach((p, i) => { ds(p).forEach(d => { ev.push({ at, keys: [hpSemi(d)], len: 0.45, vol: 0.14, p, d }); at += 0.5; }); at += 1; });
    const r = spPlay(ev, 60); if (!r) return; ev.forEach((e, j) => T.at(r.ms(e.at), () => { setPos(e.p); setOn(e.d); })); T.at(r.ms(at), () => setOn(-1)); setHeard(h => { const n = { ...h }; ps.forEach(p => { n[p] = 1; }); return n; }); };
  const add = (f) => { if (tune.length >= 8) return; setTune(tune.concat([f])); playKey(hpSemi(hpFingerD(pos, 'R', f)), 0.4); setHeard({}); };
  const lets = (p) => ds(p).map(d => 'CDEFGAB'[(d - 28 + 70) % 7]).join(' ');
  return (
    <div className="try-box" style={actBox} data-mk="move">
      <div style={actTitle}>{t('My tune moves', '나의 선율 이사 가기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>손가락 번호로 선율을 써요(1부터 5). 먼저 <b>C 자리</b>에서, 그다음 똑같은 손가락으로 <b>G 자리</b>에서 쳐요. 음이름은 다 바뀌는데... 같은 노래일까요?</> : <>Write a tune with finger numbers (1 to 5). Play it in <b>C position</b>, then with the very same fingers in <b>G position</b>. Every letter changes... is it still the same song?</>}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'2px 0 8px'}}>{tune.map((f, j) => <span key={j} style={{width:34,height:34,borderRadius:17,display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:16,fontWeight:900,border:'2px solid ' + BK.ink,background:'#fff',color:BK.ink}}>{f}</span>)}</div>
      <HpKeys pos={pos} hands="R" fingers names lit={on != null && on >= 0 ? { [on]: 'cor' } : {}} k={1.6}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,marginTop:8}}>{[1, 2, 3, 4, 5].map(f => <button key={f} className="choice-btn" onClick={() => add(f)} style={{padding:'10px 0',fontSize:18,fontWeight:900}}>{f}</button>)}</div>
      <div style={{fontSize:13.5,color:BK.ink,textAlign:'center',margin:'8px 0 2px',lineHeight:1.5}}>{t('In C position: ', 'C 자리: ')}<b>{lets('C')}</b><br/>{t('In G position: ', 'G 자리: ')}<b>{lets('G')}</b></div>
      {spMsg(heard.C && heard.G ? t('Every letter changed, but it is the same tune, just higher: your fingers carried it.', '글자는 다 바뀌었지만 같은 선율, 더 높을 뿐: 손가락이 옮겨 왔어요.') : t('Play it in C, then in G.', 'C에서, 그다음 G에서 쳐 봐요.'), heard.C && heard.G ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play(['C'])}>{t('▶ In C', '▶ C에서')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => play(['G'])}>{t('▶ In G', '▶ G에서')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => play(['C', 'G'])}>{t('▶ C, then G', '▶ C, 그다음 G')}</button>
        {tune.length > 0 && <button className="ghost-btn" style={spBtn} onClick={() => { setTune(tune.slice(0, -1)); setHeard({}); }}>{t('⌫ Back', '⌫ 지우기')}</button>}
      </div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>{MT_SONGS.map(([en, ko, fs]) => <button key={en} className="chip" style={{minHeight:40,padding:'4px 12px'}} onClick={() => { setTune(fs.slice()); setHeard({}); }}>{t('Try: ' + en, '해 보기: ' + ko)}</button>)}</div>
    </div>
  );
}

// ── Ear prep: Trick your teacher ──
const TK_CYCLE = { w: 'r', r: '.', '.': 'w' };
const tkWord = (c) => (c === '.' ? t('(rest)', '(쉼)') : lsBeatWord(c));
function TrickPad() {
  const ts = useRef([]), clear = () => { ts.current.forEach(clearTimeout); ts.current = []; };
  useEffect(() => () => clear(), []);
  const [kind, setKind] = useState('rhythm'), [a, setA] = useState(['w', 'w', 'r', 'w']), [b, setB] = useState(['w', 'w', 'r', 'w']), [ta, setTa] = useState([1, 2, 3, 1]), [tb, setTb] = useState([1, 2, 3, 1]);
  const [phase, setPhase] = useState('make'), [said, setSaid] = useState(null), [lit, setLit] = useState(-1);
  const [score, setScore] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_trick')) || { me: 0, them: 0 }; } catch (e) { return { me: 0, them: 0 }; } });
  const same = kind === 'rhythm' ? a.join() === b.join() : ta.join() === tb.join();
  const play = () => { clear(); if (kind === 'rhythm') { const spb = 60 / 96; setLit(0); lsBar(a, 0, spb, ts.current); ts.current.push(setTimeout(() => setLit(1), 5 * spb * 1000)); lsBar(b, 5 * spb * 1000, spb, ts.current); ts.current.push(setTimeout(() => setLit(-1), 9 * spb * 1000)); }
    else { setLit(0); lsSeq(ta.map(f => hpFingerD('C', 'R', f)), 480); ts.current.push(setTimeout(() => { setLit(1); lsSeq(tb.map(f => hpFingerD('C', 'R', f)), 480); }, 4 * 480 + 700)); ts.current.push(setTimeout(() => setLit(-1), 8 * 480 + 900)); } };
  const guess = (g) => { if (said) return; setSaid(g); const right = (g === 'same') === same, ns = { me: score.me + (right ? 0 : 1), them: score.them + (right ? 1 : 0) }; setScore(ns); try { localStorage.setItem('pb_mk_trick', JSON.stringify(ns)); } catch (e) {} };
  const fresh = () => { clear(); setPhase('make'); setSaid(null); setLit(-1); };
  const cell = (row, j, v, set, arr) => <button key={j} disabled={phase !== 'make'} onClick={() => { const n = arr.slice(); n[j] = kind === 'rhythm' ? TK_CYCLE[v] : v % 5 + 1; set(n); if (kind === 'tune') lsPlay(hpFingerD('C', 'R', n[j]), 0.4); }}
    style={{width:52,minHeight:52,borderRadius:26,border:'2px solid ' + (lit === row ? BK.coral : BK.ink),background:lit === row ? '#fbe3da' : '#fff',display:'inline-flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:2,cursor:phase === 'make' ? 'pointer' : 'default',fontFamily:'inherit',padding:0}}>
    {kind === 'rhythm' ? <><span style={{display:'flex',gap:3}}>{v === '.' ? <span style={{width:9,height:9,borderRadius:5,border:'1.5px solid ' + BK.line}}/> : (v === 'r' ? [0, 1] : [0]).map(k => <span key={k} style={{width:v === 'r' ? 8 : 11,height:v === 'r' ? 8 : 11,borderRadius:6,background:BK.coral}}/>)}</span><span style={{fontSize:10,fontWeight:800,color:BK.muted}}>{tkWord(v)}</span></>
      : <span style={{fontSize:18,fontWeight:900,color:BK.ink}}>{'CDEFG'[v - 1]}</span>}</button>;
  const rows = kind === 'rhythm' ? [[a, setA], [b, setB]] : [[ta, setTa], [tb, setTb]];
  return (
    <div className="try-box" style={actBox} data-mk="trick">
      <div style={actTitle}>{t('Trick your teacher', '선생님 속이기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>이번엔 내가 문제를 내요! 첫째와 둘째를 <b>똑같이</b> 두거나, 둘째에서 <b>하나만 살짝</b> 바꿔요. 동그라미를 누를 때마다 바뀌어요. 그다음 선생님께 들려주고 맞혀 보라고 해요.</> : <>Now you set the question! Make the second one <b>the same</b> as the first, or change <b>just one</b> circle, sneakily. Tap a circle to change it. Then play both to your teacher: can they tell?</>}</div>
      {spChips([['rhythm', t('Rhythm', '리듬')], ['tune', t('Tune', '선율')]], kind, (k) => { fresh(); setKind(k); })}
      {rows.map(([arr, set], row) => <div key={row} style={{display:'flex',alignItems:'center',gap:8,justifyContent:'center',margin:'6px 0'}}><span style={{width:78,fontSize:12.5,fontWeight:900,whiteSpace:'nowrap',color:row ? BK.coral : BK.muted}}>{kind === 'rhythm' ? t('Rhythm ' + (row + 1), '리듬 ' + (row + 1)) : t('Tune ' + (row + 1), '선율 ' + (row + 1))}</span>
        <div style={{display:'flex',gap:6}}>{phase === 'make' || row === 0 || said ? arr.map((v, j) => cell(row, j, v, set, arr)) : arr.map((_, j) => <span key={j} style={{width:52,height:52,borderRadius:26,border:'2px dashed ' + BK.line,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,color:BK.muted}}>?</span>)}</div></div>)}
      {phase === 'make' && <div style={{textAlign:'center',marginTop:6}}><button className="ghost-btn" style={spBtn} onClick={() => (kind === 'rhythm' ? setB(a.slice()) : setTb(ta.slice()))}>{t('Copy the first into the second', '첫째를 둘째로 복사')}</button></div>}
      {phase === 'ask' && !said && <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginTop:8}}>{[['same', t('Teacher says: the same', '선생님: 같아요')], ['different', t('Teacher says: different', '선생님: 달라요')]].map(([g, lab]) => <button key={g} className="choice-btn" onClick={() => guess(g)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}}>{lab}</button>)}</div>}
      {spMsg(said ? ((said === 'same') === same ? t('They got it! It was ' + (same ? 'the same.' : 'different.'), '맞혔어요! ' + (same ? '같았어요.' : '달랐어요.')) : t('You tricked them! It was ' + (same ? 'the same.' : 'different.'), '속였어요! ' + (same ? '같았어요.' : '달랐어요.'))) : phase === 'ask' ? t('Play it to your teacher. Same or different?', '선생님께 들려줘요. 같을까, 다를까?') : '', said ? ((said === 'same') === same ? BK.ink : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play both', '▶ 둘 다 듣기')}</button>
        {phase === 'make' && <button className="primary-btn" style={spBtn} onClick={() => { setPhase('ask'); setSaid(null); setTimeout(play, 200); }}>{t('Hide it and ask', '숨기고 물어보기')}</button>}
        {phase === 'ask' && said && <button className="ghost-btn" style={spBtn} onClick={fresh}>{t('▶ New trick', '▶ 새 문제')}</button>}
      </div>
      <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink,marginTop:8}}>{t('Me ' + score.me + ' : ' + score.them + ' Teacher', '나 ' + score.me + ' : ' + score.them + ' 선생님')}</div>
    </div>
  );
}

// ── Tones and semitones: Build a scale ──
const SS_GOALS = [['oct', 'Land on C again (an octave)', 'C에 다시 도착하기(옥타브)'], ['maj', 'Make the major scale', '장음계 만들기'], ['min', 'Make the natural minor scale', '자연 단음계 만들기']];
const SS_NAME = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'];
function StepScale() {
  const T = useSpTimers();
  const [st, setSt] = useState(['H', 'H', 'H', 'H', 'H', 'H', 'H']), [on, setOn] = useState(-1);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_steps')) || {}; } catch (e) { return {}; } });
  const ks = st.reduce((a, x) => a.concat(a[a.length - 1] + (x === 'W' ? 2 : 1)), [0]), end = ks[7], pat = st.join('');
  const hit = end === 12 ? (pat === 'WWHWWWH' ? 'maj' : pat === 'WHWWHWW' ? 'min' : 'oct') : null;
  useEffect(() => { if (!hit) return; const n = { ...stars, oct: 1 }; if (hit !== 'oct') n[hit] = 1; if (JSON.stringify(n) !== JSON.stringify(stars)) { setStars(n); try { localStorage.setItem('pb_mk_steps', JSON.stringify(n)); } catch (e) {} } }, [pat]);
  const play = () => { T.clear(); const r = spPlay(ks.map((k, j) => ({ at: j * 0.5, keys: [k], len: 0.45, vol: 0.14 })), 60); if (!r) return; ks.forEach((k, j) => T.at(r.ms(j * 0.5), () => setOn(j))); T.at(r.ms(4), () => setOn(-1)); };
  const lit = {}, names = {}; ks.forEach((k, j) => { lit[k] = j === on ? 'cor' : j === 0 || k === 12 ? 'good' : 'pale'; names[k] = String(j + 1); });
  return (
    <div className="try-box" style={actBox} data-mk="steps">
      <div style={actTitle}>{t('Build a scale', '음계 만들기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>C에서 일곱 걸음을 가요. 걸음마다 골라요: <b>반음</b>(베프, 바로 옆 건반)이나 <b>온음</b>(친구의 친구, 사이에 하나). 별 세 개를 모아 봐요!</> : <>Seven steps up from C. For each one choose: a <b>half step</b> (your best friend, the very next key) or a <b>whole step</b> (a friend of a friend, one key in between). Can you earn all three stars?</>}</div>
      <div style={{display:'flex',gap:10,justifyContent:'center',flexWrap:'wrap',margin:'0 0 8px'}}>{SS_GOALS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      <SpKb lo={0} hi={14} W={26} H={80} lit={lit} names={names} label={t('Your scale', '나의 음계')}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:4,marginTop:8}}>{st.map((x, j) => <button key={j} className="choice-btn" aria-pressed={x === 'W'} onClick={() => { const n = st.slice(); n[j] = x === 'W' ? 'H' : 'W'; setSt(n); }} style={{padding:'8px 0',fontSize:11.5,fontWeight:900,lineHeight:1.2,minWidth:0,overflow:'hidden',...(x === 'W' ? { background:'#26296b', color:'#fff', borderColor:'#26296b' } : {})}}>{x === 'W' ? t('whole', '온') : t('half', '반')}</button>)}</div>
      {spMsg(hit === 'maj' ? t('★ The major scale! Whole, whole, half, whole, whole, whole, half: every major scale has these steps.', '★ 장음계! 온 온 반 온 온 온 반: 모든 장음계가 이 걸음이에요.')
        : hit === 'min' ? t('★ The natural minor scale: whole, half, whole, whole, half, whole, whole. Hear how it sounds sadder?', '★ 자연 단음계: 온 반 온 온 반 온 온. 더 슬프게 들리나요?')
        : hit === 'oct' ? t('★ You landed on C again: an octave! Now can you find the major scale?', '★ C에 다시 도착: 옥타브! 이제 장음계를 찾아볼까요?')
        : end < 12 ? t('You stopped on ' + SS_NAME[end] + ', short of the next C. Make some steps whole.', SS_NAME[end] + '에서 멈췄어요. 다음 C까지 모자라요. 온음을 늘려 봐요.')
        : t('You went past C, up to ' + SS_NAME[end % 12] + '. Make some steps half.', 'C를 지나 ' + SS_NAME[end % 12] + '까지 갔어요. 반음을 늘려 봐요.'), hit ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play my scale', '▶ 나의 음계 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => setSt(['H', 'H', 'H', 'H', 'H', 'H', 'H'])}>{t('All half', '모두 반음')}</button>
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-band', ch: 'pulse',""", """  { id: 'mk-word', ch: 'note-names', title: 'My word tune', blurb: 'Spell real words with A to G on the keys, hear them as tunes, collect them all.', C: () => <WordTune/> },   // Build CE
  { id: 'mk-staffword', ch: 'whole-staff', title: 'Words on the staff', blurb: 'Write words on the treble or bass staff; FACE climbs the treble spaces. Then read secret ones.', C: () => <StaffWords/> },
  { id: 'mk-move', ch: 'hand-positions', title: 'My tune moves', blurb: 'Write a tune with finger numbers; play it in C position, then in G: the same tune, higher.', C: () => <MoveTune/> },
  { id: 'mk-trick', ch: 'ear-prep', title: 'Trick your teacher', blurb: 'Make two rhythms or two tunes, the same or with one sneaky change. Can your teacher tell?', C: () => <TrickPad/> },
  { id: 'mk-steps', ch: 'tones', title: 'Build a scale', blurb: 'Seven steps from C, each a best friend or a friend of a friend. Find the major scale.', C: () => <StepScale/> },
  { id: 'mk-band', ch: 'pulse',""")
rep("""  'mk-band': ['나의 박 밴드',""", """  'mk-word': ['나의 낱말 선율', 'A부터 G로 진짜 낱말을 만들어 선율로 듣고, 모두 모아요.'],
  'mk-staffword': ['오선 위의 낱말', '높은음자리표나 낮은음자리표에 낱말을 써요. FACE는 높은음자리표의 칸을 올라가요. 비밀 낱말도 읽어요.'],
  'mk-move': ['나의 선율 이사 가기', '손가락 번호로 선율을 써서 C 자리에서, 그다음 G 자리에서: 같은 선율, 더 높게.'],
  'mk-trick': ['선생님 속이기', '리듬이나 선율 두 개를 똑같이, 또는 하나만 살짝 바꿔요. 선생님이 알아챌까요?'],
  'mk-steps': ['음계 만들기', 'C에서 일곱 걸음, 걸음마다 베프나 친구의 친구. 장음계를 찾아요.'],
  'mk-band': ['나의 박 밴드',""")
rep("""'mk-band': ['rpulse', 0, 1, 'game home'],""", """'mk-band': ['rpulse', 0, 1, 'game home'], 'mk-word': ['keys', 0, 0, 'game'], 'mk-staffword': ['pitch', 0, 1, 'game'], 'mk-move': ['steps', 0, 1, 'game ear'], 'mk-trick': ['rpulse', 0, 0, 'game ear'], 'mk-steps': ['tones', 0, 1, 'game ear'],""")
rep("""'mk-band': 'r-beat',""", """'mk-band': 'r-beat', 'mk-word': 'p-staff', 'mk-staffword': 'p-staff', 'mk-move': 'k-positions', 'mk-trick': 'aural', 'mk-steps': 'p-clock',""")
rep("""  'mk-band': () => (\n""", """  'mk-word': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><text x="12" y="15.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="8.5" fontWeight="900" fill="#fefbf3">CAFE</text><rect x="4" y="18" width="16" height="2" rx="1" fill="#e9a83a"/></svg>
  ),
  'mk-staffword': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/>{[6, 9, 12, 15, 18].map(y => <path key={y} d={'M3 ' + y + 'H21'} stroke="#fefbf3" strokeWidth="0.8"/>)}{[[6, 16.5], [10, 13.5], [14, 10.5], [18, 7.5]].map(([x, y]) => <ellipse key={x} cx={x} cy={y} rx="1.9" ry="1.4" fill="#e9a83a"/>)}</svg>
  ),
  'mk-move': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/>{[0, 1, 2].map(i => <circle key={i} cx={5 + i * 3.5} cy={15 - i * 2} r="1.6" fill="#fefbf3"/>)}{[0, 1, 2].map(i => <circle key={i} cx={13 + i * 3.5} cy={11 - i * 2} r="1.6" fill="#e9a83a"/>)}<path d="M8 6 Q12 3 16 6" fill="none" stroke="#fefbf3" strokeWidth="1.3"/></svg>
  ),
  'mk-trick': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/>{[0, 1, 2, 3].map(i => <circle key={i} cx={5 + i * 4.7} cy="8.5" r="1.8" fill="#fefbf3"/>)}{[0, 1, 2, 3].map(i => <circle key={i} cx={5 + i * 4.7} cy="15.5" r="1.8" fill={i === 2 ? '#e9a83a' : '#fefbf3'}/>)}</svg>
  ),
  'mk-steps': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><path d="M3 19H6V16H9V13H11V10H14V7H17V5H20" fill="none" stroke="#fefbf3" strokeWidth="1.8" strokeLinejoin="round"/><circle cx="20" cy="5" r="1.8" fill="#e9a83a"/></svg>
  ),
  'mk-band': () => (\n""")
rep("""  'note-names': ['find-every', 'name-reveal', 'step-updown', 'letter-chain'],""", """  'note-names': ['find-every', 'name-reveal', 'step-updown', 'letter-chain', 'mk-word'],""")
rep("""  'tones': ['tone-semitone', 'accidental-cards', 'sharp-flat', 'accidental-bar', 'chromatic'],""", """  'tones': ['tone-semitone', 'accidental-cards', 'sharp-flat', 'accidental-bar', 'chromatic', 'mk-steps'],""")
rep("""  'whole-staff': ['rhymes', 'landmarks', 'landmark-hop', 'fold', 'flash-cards', 'write-note'],""", """  'whole-staff': ['rhymes', 'landmarks', 'landmark-hop', 'fold', 'flash-cards', 'write-note', 'mk-staffword'],""")
rep("""lessons: ['name-reveal', 'step-updown', 'letter-chain', 'find-every'], check: 'note-names' }""", """lessons: ['name-reveal', 'step-updown', 'letter-chain', 'find-every', 'mk-word'], check: 'note-names' }""")
rep("""lessons: ['kq-letters', 'kq-fold', 'kq-landmarks', 'kq-read', 'kq-write'], check: 'whole-staff' }""", """lessons: ['kq-letters', 'kq-fold', 'kq-landmarks', 'kq-read', 'kq-write', 'mk-staffword'], check: 'whole-staff' }""")
rep("""lessons: ['ac-half', 'ac-whole', 'ac-sharp', 'ac-flat', 'ac-two'], check: 'tones' }""", """lessons: ['ac-half', 'ac-whole', 'ac-sharp', 'ac-flat', 'ac-two', 'mk-steps'], check: 'tones' }""")
rep("""  'k-positions': { lessons: ['kp-fingers', 'kp-cpos', 'kp-gpos', 'kp-five'], check: 'hand-positions' },""", """  'k-positions': { lessons: ['kp-fingers', 'kp-cpos', 'kp-gpos', 'kp-five', 'mk-move'], check: 'hand-positions' },""")
rep("""lessons: ['ep-hml', 'ep-rhythm', 'ep-tune', 'ep-shape', 'ls-find'], check: 'ear-prep' }""", """lessons: ['ep-hml', 'ep-rhythm', 'ep-tune', 'ep-shape', 'ls-find', 'mk-trick'], check: 'ear-prep' }""")
rep("""  set('23', 'l2-clap2 lw-metre l3-sing');   // Build CC: Ear training, Grades 2 and 3""", """  set('23', 'l2-clap2 lw-metre l3-sing');   // Build CC: Ear training, Grades 2 and 3
  set('G', 'mk-word mk-staffword mk-move mk-trick mk-steps');   // Build CE: the Beginner floor's things to make""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
