import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CJ (call 25, batch 8; her 09:56: fun first): the Grade 5 rooms' things to make.
#   Ear Training, Grade 5: Triad tower (any white-key root, major or minor, root position or an inversion; sing it up and
#     down; collect all six shapes)
#   Scales and arpeggios, Grade 5: Scale DJ (a set of four tracks, D♭ major or B♭ melodic minor, each one of the four ways;
#     then hide the ways and see if a listener can name them)
#   Keys and intervals, Grade 5: Flip it (build any interval on a lower note, then flip it: the numbers add to 9, major and
#     minor swap, augmented and diminished swap, perfect stays)
#   Chords and cadences, Grade 5: Decorate the tune (a plain tune of chord notes; add passing notes in the 3rds and
#     auxiliary notes between repeated notes; hear it plain, then decorated)

CODE = r'''
// ══ Build CJ: batch 8, the Grade 5 rooms' things to make (call 25; her 09:56: fun first) ══
// ── Ear Training, Grade 5: Triad tower. Root position: the root at the bottom; first inversion: the 3rd; second: the 5th ──
const TT_ROOTS = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], TT_NAT = [0, 2, 4, 5, 7, 9, 11];
const ttNotes = (r, q, inv) => { const L = TT_ROOTS.indexOf(r), base = TT_NAT[L], want = [0, q === 'maj' ? 4 : 3, 7];
  let ns = [0, 2, 4].map((x, i) => { const l = (L + x) % 7, nat = TT_NAT[l] + 12 * Math.floor((L + x) / 7); return { d: 28 + L + x, acc: base + want[i] - nat, s: base + want[i], role: i }; });
  for (let j = 0; j < inv; j++) { const f = ns.shift(); ns.push({ ...f, d: f.d + 7, s: f.s + 12 }); }
  if (ns[0].s > 7) ns = ns.map(n => ({ ...n, d: n.d - 7, s: n.s - 12 }));
  return ns; };
const TT_ROLE = [['root', '근음'], ['3rd', '3음'], ['5th', '5음']];
function TriadTower() {
  const T = useSpTimers();
  const [r, setR] = useState('C'), [q, setQ] = useState('maj'), [inv, setInv] = useState(0), [on, setOn] = useState(-1);
  const [got, setGot] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_triad')) || {}; } catch (e) { return {}; } });
  const ns = ttNotes(r, q, inv), name = h3Let(ns.find(n => n.role === 0)) + (q === 'maj' ? t(' major', ' 장3화음') : t(' minor', ' 단3화음'));
  const play = (how) => { T.clear(); const ss = ns.map(n => n.s), seq = how === 'down' ? ss.slice().reverse() : ss, ev = [{ at: 0, keys: ss, len: 1.6, vol: 0.1 }].concat(seq.map((x, j) => ({ at: 2.2 + j * 1.1, keys: [x], len: 1, vol: 0.14 })));
    const rr = spPlay(ev, 72); if (!rr) return; seq.forEach((x, j) => T.at(rr.ms(2.2 + j * 1.1), () => setOn(ss.indexOf(x)))); T.at(rr.ms(2.2 + seq.length * 1.1 + 0.3), () => setOn(-1));
    const key = q + inv; if (!got[key]) { const n = { ...got, [key]: 1 }; setGot(n); try { localStorage.setItem('pb_mk_triad', JSON.stringify(n)); } catch (e) {} } };
  const ch = (fn) => { T.clear(); setOn(-1); fn(); };
  return (
    <div className="try-box" style={actBox} data-mk="triad">
      <div style={actTitle}>{t('Triad tower', '3화음 탑')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>3화음 탑을 쌓아요: 근음, 장조나 단조, 그리고 어떤 음을 맨 아래에 둘지. 들어 보고 <b>세 음을 모두</b> 위로, 아래로 불러요. 여섯 가지 모양을 다 모아 봐요!</> : <>Build a triad tower: a root, major or minor, and which note goes at the bottom. Hear it, then sing <b>all three notes</b>, up and down. Collect all six shapes!</>}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:4,maxWidth:330,margin:'0 auto 6px'}}>{['maj', 'min'].map(qq => [0, 1, 2].map(ii => <span key={qq + ii} style={{fontSize:11,fontWeight:800,textAlign:'center',padding:'3px 2px',borderRadius:8,border:'1.5px solid ' + (got[qq + ii] ? BK.coral : BK.line),color:got[qq + ii] ? BK.coral : BK.muted,background:qq === q && ii === inv ? '#fbe3da' : '#fff'}}>{got[qq + ii] ? '★ ' : '☆ '}{qq === 'maj' ? t('major', '장') : t('minor', '단')} · {t(['root', '1st inv.', '2nd inv.'][ii], ['기본형', '첫째', '둘째'][ii])}</span>))}</div>
      {spChips(TT_ROOTS.map(x => [x, x]), r, (x) => ch(() => setR(x)))}
      {spChips([['maj', t('Major', '장3화음')], ['min', t('Minor', '단3화음')]], q, (x) => ch(() => setQ(x)))}
      {spChips([0, 1, 2].map(i => [i, t(L4_INVW[i][0], L4_INVW[i][1])]), inv, (x) => ch(() => setInv(x)))}
      <div style={{display:'flex',flexDirection:'column-reverse',alignItems:'center',gap:4,margin:'6px 0'}}>{ns.map((n, j) => <div key={j} style={{display:'flex',alignItems:'center',gap:8}}>
        <span style={{width:58,height:32,borderRadius:10,display:'inline-flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:16,border:'2px solid ' + (n.role === 0 ? BK.coral : BK.ink),background:j === on ? (n.role === 0 ? BK.coral : BK.ink) : n.role === 0 ? '#fbe3da' : '#fff',color:j === on ? '#fff' : n.role === 0 ? BK.coral : BK.ink}}>{h3Let(n)}</span>
        <span style={{width:46,fontSize:12,fontWeight:900,color:BK.muted}}>{t(TT_ROLE[n.role][0], TT_ROLE[n.role][1])}</span></div>)}</div>
      <SpKb lo={Math.min(...ns.map(n => n.s)) - 2} hi={Math.max(...ns.map(n => n.s)) + 2} W={26} H={66} lit={Object.fromEntries(ns.map((n, j) => [n.s, j === on ? 'cor' : 'pale']))} names={Object.fromEntries(ns.map(n => [n.s, h3Let(n)]))} onTap={(k) => playKey(k, 0.5)} label={name}/>
      {spMsg(t(name + ', ' + L4_INVW[inv][0] + ': the ' + ['root', '3rd', '5th'][inv] + ' is at the bottom.', name + ', ' + L4_INVW[inv][1] + ': 맨 아래에 ' + ['근음', '3음', '5음'][inv] + '.'))}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} onClick={() => play('up')}>{t('▶ Hear it, sing up', '▶ 듣고, 위로 불러요')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => play('down')}>{t('▶ Sing down', '▶ 아래로 불러요')}</button>
      </div>
    </div>
  );
}

// ── Scales and arpeggios, Grade 5: Scale DJ. Four tracks, each D♭ major or B♭ melodic minor played one of the room's four
// ways (s5PlayWay: four clicks, then two octaves up and down); then hide the ways and see if someone can name them ──
const DJ_KEYS = ['Db', 'Bbmel'];
const djMs = (k, m) => (0.15 + (4 + s4Two(k).length / 4 + 1.5) * 60 / s5Bpm(m)) * 1000 + 700;
const DJ_STARS = [['set', 'A set with all four ways', '네 가지가 다 든 세트'], ['four', 'A listener named all four', '듣는 사람이 넷 다 맞힘']];
function ScaleDJ() {
  const T = useSpTimers();
  const [tr, setTr] = useState([['Db', 'p'], ['Bbmel', 'cd'], ['Db', 'st'], ['Bbmel', 'f']]), [on, setOn] = useState(-1), [cur, setCur] = useState(-1), [hide, setHide] = useState(false), [guess, setGuess] = useState([null, null, null, null]), [shown, setShown] = useState(false);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_dj')) || {}; } catch (e) { return {}; } });
  const give = (x) => { if (stars[x]) return; const n = { ...stars, [x]: 1 }; setStars(n); try { localStorage.setItem('pb_mk_dj', JSON.stringify(n)); } catch (e) {} };
  const playSet = () => { T.clear(); setCur(-1); let off = 0;
    tr.forEach(([k, m], j) => { T.at(off, () => { setOn(j); setCur(-1); const r = s5PlayWay(k, m); if (!r) return; for (let x = 0; x < r.n; x++) T.at(r.ms(x / 4), () => setCur(x)); }); off += djMs(k, m); });
    T.at(off, () => { setOn(-1); setCur(-1); }); if (S5_WAYS.every(w => tr.some(x => x[1] === w))) give('set'); };
  const setT = (j, f) => { T.clear(); setOn(-1); setCur(-1); setShown(false); setTr(tr.map((x, i) => (i === j ? f(x) : x))); };
  const right = tr.filter((x, j) => guess[j] === x[1]).length;
  const check = () => { setShown(true); if (right === 4) give('four'); };
  const WAY_S = { p: 'p', f: 'f', cd: t('cresc.', '크레센도'), st: t('stacc.', '스타카토') };
  return (
    <div className="try-box" style={actBox} data-mk="dj">
      <div style={actTitle}>{t('Scale DJ', '스케일 DJ')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>나는 DJ! 트랙 네 개로 세트를 짜요: 트랙마다 조와 <b>치는 방법</b>(p, f, 세게 갔다 여리게, 스타카토)을 골라요. 그다음 방법을 숨기고 누가 다 맞히는지 도전!</> : <>You are the DJ! Build a set of four tracks: for each, a key and a <b>way to play it</b> (p, f, louder then softer, staccato). Then hide the ways and challenge someone to name them all!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{DJ_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips([[false, t('Show the ways', '방법 보이기')], [true, t('Hide the ways', '방법 숨기기')]], hide, (x) => { T.clear(); setOn(-1); setHide(x); setGuess([null, null, null, null]); setShown(false); })}
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,margin:'6px 0'}}>{tr.map(([k, m], j) => { const sh = !hide || shown, ok = shown && guess[j] === m;
        return <div key={j} style={{border:'2px solid ' + (j === on ? BK.coral : shown ? (ok ? BK.green : BK.coral) : BK.ink),borderRadius:12,padding:'6px 6px 8px',background:j === on ? '#fbe3da' : '#fff',minWidth:0}}>
          <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',gap:4}}><span style={{fontFamily:LB_SERIF,fontSize:16,fontWeight:900,color:BK.coral,fontVariantNumeric:'lining-nums'}}>{j + 1}</span>
            <button className="chip" onClick={() => setT(j, x => [x[0] === 'Db' ? 'Bbmel' : 'Db', x[1]])} style={{minHeight:30,padding:'2px 8px',fontSize:12}}>{k === 'Db' ? 'D♭' : t('B♭ mel. m', 'B♭ 가락 단')}</button></div>
          <button onClick={() => !hide && setT(j, x => [x[0], S5_WAYS[(S5_WAYS.indexOf(x[1]) + 1) % 4]])} style={{display:'block',width:'100%',border:'none',background:'none',padding:'4px 0 0',cursor:hide ? 'default' : 'pointer',fontFamily:'inherit'}}>
            <S5Ribbon m={sh ? m : null} cur={j === on ? cur : -1} w={150} marks={false}/><div style={{fontSize:11.5,fontWeight:900,color:BK.ink,marginTop:2}}>{sh ? s5WayName(m) : '?'}</div></button>
          {hide && !shown && <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:3,marginTop:4}}>{S5_WAYS.map(w => <button key={w} className={'chip' + (guess[j] === w ? ' active' : '')} onClick={() => setGuess(guess.map((g, i) => (i === j ? w : g)))} style={{minHeight:30,padding:0,fontSize:10.5,minWidth:0}}>{WAY_S[w]}</button>)}</div>}
        </div>; })}</div>
      {spMsg(shown ? t(right + ' of 4 right.' + (right === 4 ? ' A perfect ear!' : ''), '4개 중 ' + right + '개 맞았어요.' + (right === 4 ? ' 완벽한 귀!' : '')) : hide ? t('Play the set, then pick a way under each track.', '세트를 듣고, 트랙마다 방법을 골라요.') : t('Tap a track to change its way, the key chip to change its key.', '트랙을 누르면 방법이, 조 칩을 누르면 조가 바뀌어요.'), shown ? (right === 4 ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} onClick={playSet}>{t('▶ Play my set', '▶ 내 세트 틀기')}</button>
        {on >= 0 && <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setOn(-1); setCur(-1); }}>{t('■ Stop', '■ 멈추기')}</button>}
        {hide && !shown && guess.every(g => g) && <button className="ghost-btn" style={spBtn} onClick={check}>{t('✓ Check', '✓ 확인')}</button>}
      </div>
    </div>
  );
}

// ── Keys and intervals, Grade 5: Flip it. The number from the letters, the quality from the semitones (k5Iv); turned upside
// down the numbers add to 9, major and minor swap, augmented and diminished swap, perfect stays (k5Inv, the room's step 4) ──
const FL_Q = { 2: ['d', 'm', 'M', 'A'], 3: ['d', 'm', 'M', 'A'], 4: ['d', 'P', 'A'], 5: ['d', 'P', 'A'], 6: ['d', 'm', 'M', 'A'], 7: ['d', 'm', 'M', 'A'], 8: ['d', 'P', 'A'] };
const flUpper = (lo, q, n) => { const d = lo.d + n - 1, want = ivMidi(lo) + K5_BASE[n] + ({ d: [4, 5, 8].includes(n) ? -1 : -2, m: -1, M: 0, P: 0, A: 1 })[q]; return { d, acc: want - ivMidi({ d, acc: 0 }) }; };
const FL_ACC = [[-1, '♭'], [0, '♮'], [1, '♯']];
const FL_STARS = [['P', 'Flip a perfect', '완전음정 뒤집기'], ['Mm', 'Flip a major or minor', '장·단음정 뒤집기'], ['Ad', 'Flip an augmented or diminished', '증·감음정 뒤집기']];
function FlipIt() {
  const [L, setL] = useState(0), [acc, setAcc] = useState(0), [n, setN] = useState(3), [q, setQ] = useState('M'), [flip, setFlip] = useState(false);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_flip')) || {}; } catch (e) { return {}; } });
  const qs0 = FL_Q[n], qv = qs0.includes(q) ? q : qs0[1], lo = { d: 28 + L, acc }, hi = flUpper(lo, qv, n), okAcc = Math.abs(hi.acc) <= 2, top8 = { d: lo.d + 7, acc: lo.acc };
  const id = okAcc ? k5Iv(lo, hi) : null, inv = id ? k5Iv(hi, top8) : null;
  const ns = flip ? [hi, top8] : [lo, hi];
  const hear = () => { const a = h3Semi(ns[0]), b = h3Semi(ns[1]); spPlay([{ at: 0, keys: [a], len: 0.9 }, { at: 1, keys: [b], len: 0.9 }, { at: 2.2, keys: [a, b], len: 1.6, vol: 0.12 }], 72); };
  const doFlip = () => { if (!id) return; const f = !flip; setFlip(f); if (f) { const k = id[0] === 'P' ? 'P' : 'Mm'.includes(id[0]) ? 'Mm' : 'Ad'; if (!stars[k]) { const s2 = { ...stars, [k]: 1 }; setStars(s2); try { localStorage.setItem('pb_mk_flip', JSON.stringify(s2)); } catch (e) {} } } };
  const ch = (fn) => { setFlip(false); fn(); };
  const qs = FL_Q[n], qq = qs.includes(q) ? q : qs[1];
  const QW = { d: t('dim.', '감'), m: t('minor', '단'), M: t('major', '장'), P: t('perfect', '완전'), A: t('aug.', '증') };
  return (
    <div className="try-box" style={actBox} data-mk="flip">
      <div style={actTitle}>{t('Flip it!', '뒤집어!')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>아래 음과 음정을 골라 만들고, <b>뒤집어!</b> 아래 음이 한 옥타브 위로 올라가요. 숫자를 더하면 언제나 <b>9</b>, 장↔단, 증↔감이 바뀌고, 완전은 그대로.</> : <>Build an interval on a lower note, then <b>flip it!</b> The bottom note jumps up an octave. The two numbers always add to <b>9</b>; major and minor swap, augmented and diminished swap, perfect stays perfect.</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{FL_STARS.map(([sid, en, ko]) => <span key={sid} style={{fontSize:12.5,fontWeight:800,color:stars[sid] ? BK.coral : BK.muted}}>{stars[sid] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips('CDEFGAB'.split('').map((x, i) => [i, x]), L, (x) => ch(() => setL(x)))}
      {spChips(FL_ACC, acc, (x) => ch(() => setAcc(x)))}
      {spChips([2, 3, 4, 5, 6, 7, 8].map(x => [x, x === 8 ? t('8ve', '8도') : t(H3_ORD[x], H3_ORDK[x])]), n, (x) => ch(() => { setN(x); if (!FL_Q[x].includes(q)) setQ(FL_Q[x][1]); }))}
      {spChips(qs.map(x => [x, QW[x]]), qq, (x) => ch(() => setQ(x)))}
      {okAcc ? <>
        <div style={{maxWidth:260,margin:'0 auto'}}><K4Melody notes={ns} width={220} hi={flip ? [1] : []} labels={ns.map(h3Let)}/></div>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:10,margin:'4px 0',flexWrap:'wrap'}}>
          <span style={{fontWeight:900,fontSize:15,color:flip ? BK.muted : BK.ink}}>{k5IvName(id)}</span><span style={{fontSize:18,color:BK.coral,fontWeight:900}}>⇄</span><span style={{fontWeight:900,fontSize:15,color:flip ? BK.coral : BK.muted}}>{k5IvName(inv)}</span></div>
        <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:26,fontWeight:900,color:BK.ink,fontVariantNumeric:'lining-nums'}}>{id.slice(1)} + {inv.slice(1)} = <span style={{color:BK.coral}}>9</span></div>
        {spMsg(flip ? t(id[0] === 'P' ? 'Perfect stays perfect.' : 'MmAd'.includes(id[0]) ? ({ M: 'Major became minor.', m: 'Minor became major.', A: 'Augmented became diminished.', d: 'Diminished became augmented.' })[id[0]] : '', id[0] === 'P' ? '완전은 그대로 완전.' : ({ M: '장이 단이 되었어요.', m: '단이 장이 되었어요.', A: '증이 감이 되었어요.', d: '감이 증이 되었어요.' })[id[0]]) : t('Now flip it!', '이제 뒤집어요!'), flip ? BK.green : undefined)}
      </> : spMsg(t('That one would need a triple sharp or flat: pick another.', '그건 세 겹 샵이나 플랫이 필요해요: 다른 걸 골라요.'), BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="primary-btn" style={spBtn} disabled={!okAcc} onClick={doFlip}>{flip ? t('↺ Flip back', '↺ 되돌리기') : t('⇅ Flip it!', '⇅ 뒤집어!')}</button>
        <button className="ghost-btn" style={spBtn} disabled={!okAcc} onClick={hear}>{t('▶ Hear it', '▶ 들어 보기')}</button>
      </div>
    </div>
  );
}

// ── Chords and cadences, Grade 5: Decorate the tune. A plain tune of chord notes, one a beat; between two notes a 3rd apart a
// passing note (a step through), between two of the same an auxiliary note (a step away and back), as the room's step 3 ──
const DT_TUNES = [
  { k: 'C', m: [['G4', 1], ['E4', 1], ['F4', 4], ['A4', 4], ['G4', 5], ['G4', 5], ['E4', 1], ['C4', 1]] },
  { k: 'G', m: [['B4', 1], ['D5', 1], ['C5', 4], ['E5', 4], ['D5', 5], ['D5', 5], ['B4', 1], ['G4', 1]] },
  { k: 'F', m: [['C5', 1], ['C5', 1], ['Bb4', 4], ['D5', 4], ['C5', 5], ['E5', 5], ['C5', 1], ['A4', 1]] },
];
const dtNote = (k, d) => ({ d, acc: h4Sig(k)[H3_L[((d % 7) + 7) % 7]] || 0 });
const dtGap = (a, b) => (a.d === b.d && a.acc === b.acc ? 'aux' : Math.abs(a.d - b.d) === 2 ? 'pass' : null);
const DT_STARS = [['pass', 'Add a passing note', '경과음 넣기'], ['aux', 'Add an auxiliary note', '보조음 넣기'], ['all', 'Decorate every gap you can', '넣을 수 있는 곳 모두']];
function DecorateTune() {
  const T = useSpTimers();
  const [ti, setTi] = useState(0), [dec, setDec] = useState([0, 0, 0, 0, 0, 0, 0]), [on, setOn] = useState(-1);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_decor')) || {}; } catch (e) { return {}; } });
  const M = DT_TUNES[ti], sk = M.m.map(([x]) => h3N(x)), gaps = sk.slice(0, -1).map((a, j) => dtGap(a, sk[j + 1]));
  const extra = (j) => { const a = sk[j], b = sk[j + 1], v = dec[j]; if (!v) return null; return v === 'p' ? dtNote(M.k, (a.d + b.d) / 2) : dtNote(M.k, a.d + (v === 'u' ? 1 : -1)); };
  const seq = []; sk.forEach((n, j) => { seq.push({ n, j, dec: false }); const x = j < sk.length - 1 ? extra(j) : null; if (x) seq.push({ n: x, j, dec: true }); });
  const cycle = (j) => { const g = gaps[j]; if (!g) return; T.clear(); setOn(-1); const opts = g === 'pass' ? [0, 'p'] : [0, 'u', 'l'], v = opts[(opts.indexOf(dec[j]) + 1) % opts.length], d2 = dec.map((x, i) => (i === j ? v : x)); setDec(d2);
    const n2 = { ...stars }; if (d2.includes('p')) n2.pass = 1; if (d2.includes('u') || d2.includes('l')) n2.aux = 1; if (gaps.every((g2, i) => !g2 || d2[i])) n2.all = 1;
    if (Object.keys(n2).length !== Object.keys(stars).length) { setStars(n2); try { localStorage.setItem('pb_mk_decor', JSON.stringify(n2)); } catch (e) {} } };
  const play = (plain) => { T.clear(); const ev = []; const marks = [];
    sk.forEach((n, j) => { const x = !plain && j < sk.length - 1 ? extra(j) : null, deg = M.m[j][1], root = h4Note(M.k, h4Td(M.k, 2), deg - 1), mid = [2, 4].map(y => h4Note(M.k, h4Td(M.k, 3), deg - 1 + y));
      ev.push({ at: j, keys: [h3Semi(root), ...mid.map(h3Semi)], len: 0.95, vol: 0.06 }); ev.push({ at: j, keys: [h3Semi(n)], len: x ? 0.45 : j === sk.length - 1 ? 1.4 : 0.92, vol: 0.15 }); marks.push([j, seq.findIndex(s2 => s2.j === j && !s2.dec)]);
      if (x) { ev.push({ at: j + 0.5, keys: [h3Semi(x)], len: 0.45, vol: 0.15 }); marks.push([j + 0.5, seq.findIndex(s2 => s2.j === j && s2.dec)]); } });
    const r = spPlay(ev, 76); if (!r) return; if (!plain) marks.forEach(([b, i]) => T.at(r.ms(b), () => setOn(i))); T.at(r.ms(sk.length + 0.6), () => setOn(-1)); };
  const nP = dec.filter(x => x === 'p').length, nA = dec.filter(x => x === 'u' || x === 'l').length;
  return (
    <div className="try-box" style={actBox} data-mk="decor">
      <div style={actTitle}>{t('Decorate the tune', '선율 꾸미기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>화음 음으로만 된 밋밋한 선율이에요. 두 음 사이 칸을 눌러 꾸며요: 3도 떨어진 곳엔 <b>경과음</b>(한 음 지나가기), 같은 음 사이엔 <b>보조음</b>(한 음 떠났다 돌아오기). 밋밋하게, 꾸며서, 둘 다 들어 봐요!</> : <>A plain tune made only of chord notes. Tap a gap to decorate it: between notes a 3rd apart, a <b>passing note</b> (a step through); between two of the same, an <b>auxiliary note</b> (a step away and back). Hear it plain, then decorated!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{DT_STARS.map(([id, en, ko]) => <span key={id} style={{fontSize:12.5,fontWeight:800,color:stars[id] ? BK.coral : BK.muted}}>{stars[id] ? '★' : '☆'} {t(en, ko)}</span>)}</div>
      {spChips(DT_TUNES.map((x, i) => [i, h4Name(x.k)]), ti, (x) => { T.clear(); setOn(-1); setTi(x); setDec([0, 0, 0, 0, 0, 0, 0]); })}
      <div style={{maxWidth:380,margin:'0 auto'}}><K4Melody notes={seq.map(x => x.n)} ks={H4_KEYS[M.k][2]} width={360} hi={on >= 0 ? [on] : seq.map((x, i) => (x.dec ? i : -1)).filter(i => i >= 0)} labels={seq.map(x => (x.dec ? '' : h4Rom(M.k, M.m[x.j][1], 0)))}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:3,margin:'6px 0'}}>{gaps.map((g, j) => <button key={j} className="chip" disabled={!g} onClick={() => cycle(j)} style={{minHeight:46,padding:'2px 0',minWidth:0,display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',lineHeight:1.1,opacity:g ? 1 : 0.35,border:dec[j] ? '2px solid ' + BK.coral : undefined}}>
        <span style={{fontSize:10,fontWeight:800,color:BK.muted}}>{h3Let(sk[j])}–{h3Let(sk[j + 1])}</span><span style={{fontSize:12,fontWeight:900,color:dec[j] ? BK.coral : BK.ink}}>{!g ? '–' : dec[j] === 'p' ? t('pass', '경과') : dec[j] === 'u' ? t('aux ↑', '보조 ↑') : dec[j] === 'l' ? t('aux ↓', '보조 ↓') : '+'}</span></button>)}</div>
      {spMsg(nP || nA ? t((nP ? nP + ' passing note' + (nP > 1 ? 's' : '') : '') + (nP && nA ? ' and ' : '') + (nA ? nA + ' auxiliary note' + (nA > 1 ? 's' : '') : '') + ', each on the half beat, between two chord notes.', (nP ? '경과음 ' + nP + '개' : '') + (nP && nA ? ', ' : '') + (nA ? '보조음 ' + nA + '개' : '') + ': 모두 반 박에, 화음 음 사이에.')
        : t('Tap + between two notes. A dash means no room: a step apart, or too far.', '두 음 사이의 +를 눌러요. –는 넣을 자리가 없는 곳: 한 걸음 차이거나, 너무 멀어요.'), nP || nA ? BK.green : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play(true)}>{t('▶ Plain', '▶ 밋밋하게')}</button>
        <button className="primary-btn" style={spBtn} onClick={() => play(false)}>{t('▶ Decorated', '▶ 꾸며서')}</button>
      </div>
    </div>
  );
}
'''
rep("// ══ Build BH: Blues jam ══", CODE + "\n// ══ Build BH: Blues jam ══")
rep("""  { id: 'mk-bingo', ch: 'listen-4',""", """  { id: 'mk-triad', ch: 'listen-5', title: 'Triad tower', blurb: 'Build a triad, major or minor, with the root, 3rd or 5th at the bottom. Sing it up and down; collect all six.', C: () => <TriadTower/> },   // Build CJ
  { id: 'mk-dj', ch: 'scales-5', title: 'Scale DJ', blurb: 'A set of four scale tracks, each played one of the four ways. Then hide the ways: can someone name them?', C: () => <ScaleDJ/> },
  { id: 'mk-flip', ch: 'keys-5', title: 'Flip it!', blurb: 'Build an interval, then flip it: the numbers add to 9, major and minor swap, perfect stays.', C: () => <FlipIt/> },
  { id: 'mk-decor', ch: 'harmony-5', title: 'Decorate the tune', blurb: 'Add passing and auxiliary notes to a plain tune of chord notes. Hear it plain, then decorated.', C: () => <DecorateTune/> },
  { id: 'mk-bingo', ch: 'listen-4',""")
rep("""  'mk-bingo': ['음정 빙고',""", """  'mk-triad': ['3화음 탑', '장3화음이나 단3화음을 쌓고, 맨 아래에 근음, 3음, 5음 중 하나를. 위로 아래로 불러요. 여섯 가지 모두 모아요.'],
  'mk-dj': ['스케일 DJ', '스케일 트랙 네 개, 트랙마다 네 가지 방법 중 하나로. 방법을 숨기면 누가 맞힐까요?'],
  'mk-flip': ['뒤집어!', '음정을 만들고 뒤집어요: 숫자를 더하면 9, 장과 단이 바뀌고, 완전은 그대로.'],
  'mk-decor': ['선율 꾸미기', '화음 음만 있는 밋밋한 선율에 경과음과 보조음을. 밋밋하게, 꾸며서 들어요.'],
  'mk-bingo': ['음정 빙고',""")
rep("""'mk-bingo': ['intervals', 2, 2, 'game ear'],""", """'mk-bingo': ['intervals', 2, 2, 'game ear'], 'mk-triad': ['chords', 2, 3, 'game ear'], 'mk-dj': ['scales', 2, 3, 'game ear'], 'mk-flip': ['intervals', 2, 3, 'game'], 'mk-decor': ['melody', 2, 3, 'game ear'],""")
rep("""'mk-bingo': 'aural',""", """'mk-bingo': 'aural', 'mk-triad': 'aural', 'mk-dj': 'k-play', 'mk-flip': 'p-scales', 'mk-decor': 'p-chords',""")
rep("""  'mk-bingo': () => (\n""", """  'mk-triad': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#2e8a6e"/>{[0, 1, 2].map(i => <rect key={i} x="6" y={15 - i * 5} width="12" height="4" rx="1.2" fill={i === 0 ? '#e9a83a' : '#fefbf3'}/>)}</svg>
  ),
  'mk-dj': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#7a4f96"/><circle cx="8" cy="12" r="5" fill="none" stroke="#fefbf3" strokeWidth="1.4"/><circle cx="8" cy="12" r="1.2" fill="#e9a83a"/><path d="M15 16 L21 8 L21 16 Z" fill="#fefbf3"/></svg>
  ),
  'mk-flip': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#e4572e"/><text x="7.5" y="15.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="10" fontWeight="900" fill="#fefbf3">3</text><path d="M11 9 L13 7 L15 9 M13 7 V17 M11 15 L13 17 L15 15" stroke="#e9a83a" strokeWidth="1.2" fill="none"/><text x="18.5" y="15.5" textAnchor="middle" fontFamily="Georgia, serif" fontSize="10" fontWeight="900" fill="#fefbf3">6</text></svg>
  ),
  'mk-decor': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[[5, 15], [12, 11], [19, 7]].map(([x, y]) => <circle key={x} cx={x} cy={y} r="2" fill="#fefbf3"/>)}{[[8.5, 13], [15.5, 9]].map(([x, y]) => <circle key={x} cx={x} cy={y} r="1.3" fill="#e9a83a"/>)}</svg>
  ),
  'mk-bingo': () => (\n""")
rep("""lessons: ['l5-iv', 'l5-two', 'l5-tri', 'l5-clap'], check: 'listen-5' },""", """lessons: ['l5-iv', 'l5-two', 'l5-tri', 'l5-clap', 'mk-triad'], check: 'listen-5' },""")
rep("""lessons: ['s5-four', 's5-dyn', 's5-mirror', 's5-chrom', 's5-arp'], check: 'scales-5' },""", """lessons: ['s5-four', 's5-dyn', 's5-mirror', 's5-chrom', 's5-arp', 'mk-dj'], check: 'scales-5' },""")
rep("""lessons: ['k5-sig', 'k5-mel', 'k5-ad', 'k5-inv', 'k5-mod'], check: 'keys-5' },""", """lessons: ['k5-sig', 'k5-mel', 'k5-ad', 'k5-inv', 'k5-mod', 'mk-flip'], check: 'keys-5' },""")
rep("""lessons: ['h5-inv', 'h5-c64', 'h5-pass', 'h5-pre', 'h5-harm'], check: 'harmony-5' },""", """lessons: ['h5-inv', 'h5-c64', 'h5-pass', 'h5-pre', 'h5-harm', 'mk-decor'], check: 'harmony-5' },""")
rep("""  set('4', 'mk-bingo mk-four4 mk-anykey mk-tunechords mk-offbeat');   // Build CI""", """  set('4', 'mk-bingo mk-four4 mk-anykey mk-tunechords mk-offbeat');   // Build CI
  set('5', 'mk-triad mk-dj mk-flip mk-decor');   // Build CJ""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
