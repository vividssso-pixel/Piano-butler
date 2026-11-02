p='drills.src.html'; s=open(p).read()
assert 'learnerWho' not in s
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)

# ── 1. a learner (signed up on join.html, role 'learner') is never the teacher ──
rep("function initialMode() {", r'''// m57: a learner who joined on join.html (Supabase user_metadata.role 'learner'); null for teachers and visitors
function learnerWho() {
  try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i) || ''; if (!/^sb-.*-auth-token$/.test(k)) continue;
    const v = JSON.parse(localStorage.getItem(k) || 'null'); const u = v && (v.user || (v.currentSession && v.currentSession.user));
    if (u && u.user_metadata && u.user_metadata.role === 'learner') return { email: u.email || '', name: String(u.user_metadata.name || (u.email || '').split('@')[0] || '').slice(0, 40) }; } } catch (e) {}
  return null;
}
function learnerSignOut() { try { Object.keys(localStorage).filter(k => /^sb-.*-auth-token$/.test(k)).forEach(k => localStorage.removeItem(k)); localStorage.setItem(MODE_KEY, 'student'); } catch (e) {} location.href = 'drills.html'; }
function initialMode() {''')
rep("    for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i) || ''; if (/^sb-.*-auth-token$/.test(k)) { localStorage.setItem(MODE_KEY, 'teacher'); return true; } }",
    "    if (learnerWho()) { localStorage.setItem(MODE_KEY, 'student'); return false; }   // m57\n    for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i) || ''; if (/^sb-.*-auth-token$/.test(k)) { localStorage.setItem(MODE_KEY, 'teacher'); return true; } }")
rep("    const saved = localStorage.getItem(MODE_KEY);\n    if (saved === 'student') return false;",
    "    if (learnerWho()) { localStorage.setItem(MODE_KEY, 'student'); return false; }   // m57: before a remembered 'teacher'\n    const saved = localStorage.getItem(MODE_KEY);\n    if (saved === 'student') return false;")
# the teacher-login helpers ignore a learner's session
rep("    const v = JSON.parse(localStorage.getItem(k) || 'null'); const u = v && (v.user || (v.currentSession && v.currentSession.user)); if (u && (v.refresh_token || v.access_token)) return { email: u.email || '' }; } } catch (e) {}",
    "    const v = JSON.parse(localStorage.getItem(k) || 'null'); const u = v && (v.user || (v.currentSession && v.currentSession.user)); if (u && !(u.user_metadata && u.user_metadata.role === 'learner') && (v.refresh_token || v.access_token)) return { email: u.email || '' }; } } catch (e) {}")

# ── 2. a learner's free floors: Level 0 and Level ½ in full ──
rep("const visLocked = (id) => isVisitor() && !!id && !VIS_OPEN.has(id);",
    "const LEARNER_FREE = () => [0, 1].flatMap(k => PATH_STAGES[k] ? pathStageIds(PATH_STAGES[k]) : []);   // m57: free with an account\nconst visLocked = (id) => isVisitor() && !!id && !VIS_OPEN.has(id) && !(learnerWho() && LEARNER_FREE().includes(id));")
rep("    <div style={{fontSize:14.5,color:'var(--muted)',lineHeight:1.5,maxWidth:340,margin:'0 auto 14px'}}>{t('Every room opens with a student link from your teacher. The open rooms on each floor are yours to try now.', '모든 방은 선생님이 주는 학생 링크로 열려요. 층마다 열린 방은 지금 바로 해 볼 수 있어요.')}</div>",
    "    <div style={{fontSize:14.5,color:'var(--muted)',lineHeight:1.5,maxWidth:340,margin:'0 auto 14px'}}>{learnerWho() ? t('Levels 0 and ½ are yours, every room. The higher floors open floor by floor (coming soon); their open rooms are yours to try now.', '레벨 0과 ½은 모든 방이 열려 있어요. 위층은 층마다 열려요(곧). 열린 방은 지금 바로 해 볼 수 있어요.') : t('Every room opens with a student link from your teacher. The open rooms on each floor are yours to try now.', '모든 방은 선생님이 주는 학생 링크로 열려요. 층마다 열린 방은 지금 바로 해 볼 수 있어요.')}</div>\n    {!learnerWho() && <div style={{fontSize:13.5,color:'var(--navy)',margin:'-4px 0 14px'}}>{t('Learning on your own? ', '혼자 배우나요? ')}<a href=\"join.html\" style={{color:'var(--coral)',fontWeight:800}}>{t('Join free: Levels 0 and ½ open', '무료 가입: 레벨 0과 ½ 열림')}</a></div>}")

# ── 3. the practice dial: set the minutes on a ring, or run the timer and the ring fills (her 2 Nov) ──
rep("function TodayView({ link, onOpenChapter,", r'''function PracticeDial({ value, onCommit, disabled }) {   // m57: 0 to 120 minutes on a ring; drag or tap to set, or run the timer
  const [v, setV] = useState(value || 0), [run, setRun] = useState(null), [, tick] = useState(0), drag = useRef(false), box = useRef(null);
  useEffect(() => { if (!run) setV(value || 0); }, [value]);
  useEffect(() => { if (!run) return; const id = setInterval(() => tick(x => x + 1), 1000); return () => clearInterval(id); }, [run]);
  const live = run ? Math.min(120, (v || 0) + (Date.now() - run) / 60000) : v, R = 54, C = 2 * Math.PI * R, frac = Math.min(1, live / 60), laps = live > 60;
  const at = (e) => { const r = box.current.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 140 - 70, y = (e.clientY - r.top) / r.height * 140 - 70; let a = Math.atan2(x, -y); if (a < 0) a += 2 * Math.PI; const m = Math.round(a / (2 * Math.PI) * 60 / 5) * 5; return v >= 55 && m <= 10 ? 60 + m : v > 60 ? Math.max(60, 60 + m) : m; };
  const mm = Math.floor(live), ss = run ? Math.floor((live - mm) * 60) : 0;
  return <div data-testid="practice-dial" style={{display:'flex',alignItems:'center',gap:14,margin:'12px 0 4px'}}>
    <svg ref={box} viewBox="0 0 140 140" width="132" height="132" style={{flex:'none',touchAction:'none',cursor:disabled || run ? 'default' : 'pointer'}}
      onPointerDown={e => { if (disabled || run) return; drag.current = true; try { e.currentTarget.setPointerCapture(e.pointerId); } catch (x) {} setV(at(e)); }}
      onPointerMove={e => { if (drag.current) setV(at(e)); }} onPointerUp={() => { if (!drag.current) return; drag.current = false; onCommit(v || null); }}>
      <circle cx="70" cy="70" r={R} fill="none" stroke="var(--navy-line)" strokeWidth="12"/>
      {laps && <circle cx="70" cy="70" r={R} fill="none" stroke="#bfe0d3" strokeWidth="12"/>}
      <circle cx="70" cy="70" r={R} fill="none" stroke={run ? 'var(--coral)' : '#2e8a6e'} strokeWidth="12" strokeLinecap="round" strokeDasharray={(laps ? Math.min(1, (live - 60) / 60) : frac) * C + ' ' + C} transform="rotate(-90 70 70)"/>
      {[0, 15, 30, 45].map(m => <text key={m} x={70 + 38 * Math.sin(m / 60 * 2 * Math.PI)} y={70 - 38 * Math.cos(m / 60 * 2 * Math.PI) + 3.5} textAnchor="middle" fontSize="9" fontWeight="800" fill="#9a9cc0">{m === 0 ? (laps ? '60' : '0') : laps ? 60 + m : m}</text>)}
      <text x="70" y={run ? 72 : 76} textAnchor="middle" fontSize={run ? 22 : 30} fontWeight="900" fill="var(--navy)" fontFamily="'Playfair Display', Georgia, serif">{run ? mm + ':' + String(ss).padStart(2, '0') : (v || 0)}</text>
      <text x="70" y={run ? 90 : 92} textAnchor="middle" fontSize="10" fontWeight="800" fill="#9a9cc0">{t('minutes', '분')}</text>
    </svg>
    <div style={{flex:1,minWidth:0}}>
      <div style={{fontSize:13,color:'var(--muted)',lineHeight:1.4,marginBottom:8}}>{t('Turn the ring to the minutes you played, or time it now.', '친 시간만큼 원을 돌리거나, 지금 타이머로 재요.')}</div>
      <button type="button" data-testid="dial-timer" disabled={disabled} className="chip" onClick={() => { if (run) { const m = Math.max(1, Math.round(live)); setRun(null); setV(m); onCommit(m); } else setRun(Date.now()); }}
        style={{padding:'7px 14px',fontSize:14,fontWeight:800,color:run ? '#fff' : 'var(--navy)',background:run ? 'var(--coral)' : '#fff',borderColor:run ? 'var(--coral)' : 'var(--navy-line)'}}>{run ? t('■ Stop', '■ 멈추기') : t('▶ Start the timer', '▶ 타이머 시작')}</button>
    </div>
  </div>;
}
function TodayView({ link, onOpenChapter,''')
a = s.index("          <div style={{ display: 'flex', gap: 8, margin: '14px 0 4px' }}>\n            {[5, 10, 20, 30].map(m => (")
b = s.index("            <span>{t('minutes (optional)', '분 (선택)')}</span>", a)
s = s[:a] + "          <PracticeDial value={selMins} disabled={busy} onCommit={(m) => { if (checked) save(m); else setMins(m); }}/>   {/* m57 */}\n          <div style={{ fontSize: 12, color: 'var(--muted)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 8 }}>\n" + s[b:]

# ── 4. on my own: Today for a learner ──
rep("function StudentHome({ link, onOpenChapter, onOpenTool, onAll }) {", r'''// m57 (her 2 Nov, mockup approved): Today for someone learning on their own -- the plan, the practice, their pieces, what comes next
const SOLO_DAYS_KEY = 'pb_solo_days_v1', SOLO_PIECES_KEY = 'pb_solo_pieces_v1';
const SOLO_STAGES = [['Right hand', '오른손'], ['Left hand', '왼손'], ['Together', '양손'], ['Speed', '속도'], ['Fluent', '유창하게']];
const soloLoad = (k, d) => { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } };
const soloSave = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} };
function SoloToday({ onOpenChapter, onOpenTool, onAll }) {
  const me = learnerWho() || { name: '' };
  const today = localDay();
  const [days, setDays] = useState(() => soloLoad(SOLO_DAYS_KEY, {}));
  const [pieces, setPieces] = useState(() => soloLoad(SOLO_PIECES_KEY, []));
  const [newP, setNewP] = useState('');
  const setD = (d) => { setDays(d); soloSave(SOLO_DAYS_KEY, d); }, setP = (p) => { setPieces(p); soloSave(SOLO_PIECES_KEY, p); };
  const totals = loadStepTotals(), ids = pathIds(), status = Object.fromEntries(ids.map(id => [id, chapterStatus(id, totals)]));
  const focus = guideFocus(status, ids), k0 = focus ? ids.indexOf(focus.id) : -1;
  const plan = k0 < 0 ? [] : ids.slice(k0).filter(id => status[id] !== 'done').slice(0, 2);
  const k = focus ? stageOfChapter(focus.id) : -1, floorIds = k >= 0 ? pathStageIds(PATH_STAGES[k]) : [], fDone = floorIds.filter(id => status[id] === 'done').length;
  const cards = myCards(), nextCard = cards.find(c => !c.on), learned = pieces.filter(x => x.f).length;
  const h = new Date().getHours(), hello = (h < 12 ? t('Good morning', '좋은 아침이에요') : h < 18 ? t('Good afternoon', '안녕하세요') : t('Good evening', '좋은 저녁이에요')) + (me.name ? ', ' + me.name : '') + '.';
  const dow = (dayDate(today).getDay() + 6) % 7, monday = dayPlus(today, -dow), week = [0, 1, 2, 3, 4, 5, 6].map(i => dayPlus(monday, i));
  const letters = LANG === 'ko' ? ['월', '화', '수', '목', '금', '토', '일'] : ['M', 'T', 'W', 'T', 'F', 'S', 'S'], checked = days[today] != null;
  const card = { background: 'var(--surface)', border: '1.5px solid var(--navy-line)', borderRadius: 16, padding: 16, marginBottom: 14, boxShadow: '0 4px 18px rgba(38,41,107,0.05)' };
  const lab = { fontSize: 11, fontWeight: 900, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'var(--coral)', marginBottom: 10 };
  const pill = (on, cur) => ({ fontSize: 11.5, fontWeight: 800, padding: '4px 9px', borderRadius: 99, cursor: 'pointer', border: '1.5px solid ' + (on ? '#2e8a6e' : 'var(--navy-line)'), background: cur ? '#2e8a6e' : on ? '#e8f3ee' : '#fff', color: cur ? '#fff' : on ? '#2e8a6e' : '#9a9cc0' });
  return (
    <div data-testid="solo-today">
      <div style={{ display: 'flex', gap: 12, alignItems: 'center', margin: '0 0 14px' }}>
        <img src={VIC_CAMEO} alt="" style={{ height: 58, flex: '0 0 auto' }}/>
        <div><div style={{ fontFamily: "'Playfair Display', Georgia, serif", fontStyle: 'italic', fontSize: 22, color: 'var(--navy)', lineHeight: 1.2 }}>{'“' + hello + '”'}</div>
          <div style={{ fontSize: 13.5, color: 'var(--muted)', marginTop: 2 }}>{k >= 0 ? floorName(k) + ' · ' : ''}<span style={{ fontSize: 10, fontWeight: 900, letterSpacing: '0.08em', color: '#fff', background: 'var(--navy)', borderRadius: 99, padding: '2px 8px' }}>{t('ON MY OWN', '혼자 배우기')}</span></div></div>
      </div>
      <div style={card} data-testid="solo-plan"><div style={lab}>{t('My plan this week', '이번 주 내 계획')}</div>
        {plan.map((id, i) => <div key={id} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '8px 0', borderTop: i ? '1px solid var(--navy-line)' : 'none' }}>
          <span style={{ width: 20, height: 20, borderRadius: 5, border: '1.5px solid var(--navy)', background: status[id] !== 'new' ? '#e8f3ee' : '#fff', flex: 'none' }}/>
          <span style={{ flex: 1, minWidth: 0, fontSize: 14.5, color: 'var(--navy)' }}>{bkChapterNo(id) + ' · ' + bkChapterName(id)}<small style={{ display: 'block', fontSize: 12, color: 'var(--muted)' }}>{i === 0 ? t('your next room', '다음 방') : t('after that', '그다음')}</small></span>
          <button className="chip" onClick={() => onOpenChapter(id)} style={{ padding: '4px 12px', fontSize: 13, fontWeight: 800, color: 'var(--coral)', borderColor: 'var(--coral)' }}>{t('Open ›', '열기 ›')}</button></div>)}
        {!plan.length && <div style={{ fontSize: 14, color: 'var(--good)', fontWeight: 800 }}>{t('Every room on your path is done. Wonderful!', '경로의 모든 방을 마쳤어요. 멋져요!')}</div>}
        <button type="button" onClick={onAll} style={{ border: 'none', background: 'none', padding: '8px 0 0', color: 'var(--coral)', fontWeight: 800, fontSize: 13, cursor: 'pointer' }}>{t('+ Choose a room myself', '+ 직접 방 고르기')}</button>
      </div>
      <div style={card}><div style={lab}>{t('Did you practise today?', '오늘 연습했어요?')}</div>
        <button onClick={() => { if (!checked) setD({ ...days, [today]: days[today] || 0 }); }} aria-pressed={checked} style={{ width: '100%', border: 'none', background: checked ? 'var(--good)' : 'var(--coral)', color: '#fff', fontWeight: 800, fontSize: 18, padding: 16, borderRadius: 14, boxShadow: '0 4px 0 ' + (checked ? '#236a53' : '#b9421f'), cursor: checked ? 'default' : 'pointer', fontFamily: 'Inter, sans-serif' }}>{checked ? t('Practised today ✓', '오늘 연습 완료 ✓') : t('I practised today', '오늘 연습했어요')}</button>
        <PracticeDial value={days[today] || null} onCommit={(m) => setD({ ...days, [today]: m || 0 })}/>
        {checked && <div style={{ textAlign: 'right' }}><button className="chip" style={{ padding: '2px 9px', fontSize: 12 }} onClick={() => { const n = { ...days }; delete n[today]; setD(n); }}>{t('Undo', '취소')}</button></div>}
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 12 }}>{week.map((d, i) => { const yes = days[d] != null; return <div key={d} style={{ textAlign: 'center', fontSize: 11, fontWeight: 800, color: 'var(--muted)', opacity: d > today ? 0.45 : 1 }}>{letters[i]}<i style={{ display: 'block', width: 30, height: 30, borderRadius: '50%', border: '2px ' + (d === today && !yes ? 'dashed' : 'solid') + ' ' + (yes ? 'var(--good)' : d === today ? 'var(--coral)' : 'var(--navy-line)'), background: yes ? 'var(--good)' : 'transparent', margin: '5px auto 0', color: '#fff', fontStyle: 'normal', fontSize: 15, lineHeight: '26px' }}>{yes ? '✓' : ''}</i></div>; })}</div>
      </div>
      <div style={card} data-testid="solo-pieces"><div style={lab}>{t('My pieces and scales', '내 곡과 스케일')}</div>
        {pieces.filter(x => !x.f).map((x) => { const j = pieces.indexOf(x); return <div key={j} style={{ marginBottom: 10 }}>
          <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}><div style={{ flex: 1, background: '#ecebf5', borderRadius: 10, padding: '7px 12px', fontWeight: 700, fontSize: 14, color: 'var(--navy)' }}>{x.t}</div>
            <button aria-label={t('Remove', '빼기')} onClick={() => setP(pieces.filter((_, q) => q !== j))} style={{ border: 'none', background: 'none', color: '#9b9cbd', fontSize: 18, cursor: 'pointer' }}>×</button></div>
          <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap', marginTop: 6 }}>{SOLO_STAGES.map((sg, q) => <button key={q} type="button" onClick={() => setP(pieces.map((y, r) => r === j ? { ...y, s: y.s === q + 1 ? q : q + 1 } : y))} style={pill(q + 1 <= (x.s || 0), q + 1 === x.s)}>{t(sg[0], sg[1])}</button>)}
            <button type="button" onClick={() => setP(pieces.map((y, r) => r === j ? { ...y, f: true, s: Math.max(y.s || 0, 5), at: Date.now() } : y))} style={{ ...pill(false, false), marginLeft: 'auto', borderColor: 'var(--coral)', color: 'var(--coral)' }}>{t('Finish', '마침')}</button></div></div>; })}
        <div style={{ display: 'flex', gap: 6 }}><input value={newP} onChange={e => setNewP(e.target.value)} onKeyDown={e => { if (e.key === 'Enter' && newP.trim()) { setP([...pieces, { t: newP.trim().slice(0, 80), s: 0 }]); setNewP(''); } }} placeholder={t('Add a piece or a scale', '곡이나 스케일 추가')} style={{ flex: 1, border: '1.5px solid var(--navy-line)', borderRadius: 10, padding: '8px 12px', font: 'inherit', fontSize: 14 }}/>
          <button className="chip" onClick={() => { if (newP.trim()) { setP([...pieces, { t: newP.trim().slice(0, 80), s: 0 }]); setNewP(''); } }} style={{ padding: '6px 12px', fontWeight: 800 }}>{t('Add', '추가')}</button></div>
        {learned > 0 && <div style={{ fontSize: 12.5, color: 'var(--good)', fontWeight: 800, marginTop: 10 }}>{t('Learned: ', '마친 곡: ') + pieces.filter(x => x.f).map(x => x.t).join(' · ')}</div>}
      </div>
      {k >= 0 && <div data-testid="solo-next" style={{ background: '#fff3ee', border: '1.5px solid var(--coral)', borderRadius: 12, padding: '10px 12px', fontSize: 13.5, color: 'var(--navy)', marginBottom: 14 }}>
        <b style={{ display: 'block', fontSize: 14.5 }}>{floorName(k) + ': ' + t(fDone + ' of ' + floorIds.length + ' rooms done', floorIds.length + '개 중 ' + fDone + '개 완료')}</b>
        {fDone < floorIds.length ? t('Finish the rest and the ' + floorName(k) + ' checkpoint is ready.', '나머지를 마치면 ' + floorName(k) + ' 중간점검을 볼 수 있어요.') : t('The ' + floorName(k) + ' checkpoint is ready: tap ✓ Check on your floor.', floorName(k) + ' 중간점검을 볼 차례예요: 층의 ✓ 점검을 눌러요.')}
        {nextCard ? t(' Pass it for the ' + nextCard.rank + ' ' + nextCard.suit + ' card.', ' 통과하면 ' + nextCard.suit + nextCard.rank + ' 카드.') : ''}</div>}
      <div style={card}><div style={lab}>{t('My progress', '나의 진도')}</div>
        <div style={{ display: 'flex', gap: 8 }}>{[[ids.filter(id => status[id] === 'done').length, t('rooms done', '끝낸 방')], [learned, t('pieces learned', '마친 곡')], [cards.filter(c => c.on).length + '/' + cards.length, t('cards', '카드')]].map(([n, w], i) =>
          <div key={i} style={{ flex: 1, border: '1.5px solid var(--navy-line)', borderRadius: 12, padding: 10 }}><b style={{ display: 'block', fontSize: 22, color: 'var(--navy)' }}>{n}</b><span style={{ fontSize: 12, color: 'var(--muted)' }}>{w}</span></div>)}</div></div>
      <div style={{ ...lab, margin: '4px 0 8px' }}>{t('Quick tools', '바로 쓰는 도구')}</div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0,1fr))', gap: 8, marginBottom: 14 }}>{[['scale-finder', '♯'], ['metronome', '♩'], ['practice-timer', '◷']].map(([id, g]) => { const tl = TOOLS.find(x => x.id === id); return tl ? <button key={id} onClick={() => onOpenTool(id)} style={{ background: 'var(--surface)', border: '1.5px solid var(--navy-line)', borderRadius: 12, padding: '10px 4px', cursor: 'pointer', font: 'inherit', textAlign: 'center' }}><span style={{ display: 'block', fontSize: 20, color: 'var(--coral)' }}>{g}</span><b style={{ display: 'block', fontSize: 13, color: 'var(--navy)', marginTop: 3 }}>{LANG === 'ko' && TOOL_KO[id] ? TOOL_KO[id][0] : tl.title}</b></button> : null; })}</div>
      <div style={{ textAlign: 'center', fontSize: 12, color: 'var(--muted)' }}>{t('Signed in' + (me.email ? ' as ' + me.email : ''), (me.email ? me.email + '(으)로 ' : '') + '로그인됨')} · <button onClick={learnerSignOut} style={{ border: 'none', background: 'none', color: 'var(--coral)', fontWeight: 800, cursor: 'pointer', fontSize: 12 }}>{t('Sign out', '로그아웃')}</button></div>
    </div>
  );
}
function StudentHome({ link, onOpenChapter, onOpenTool, onAll }) {''')

# ── 5. the learner gets Today · Practice and lands on Today ──
rep("  const todayView = hasLink && (p.get('view') === 'today'", "  const todayView = (hasLink || (!!studentMode && !!learnerWho())) && (p.get('view') === 'today'")
rep("  const showToday = !!sl.link && sl.state !== 'invalid';", "  const LEARNER = !teacher && !!learnerWho();   // m57\n  const showToday = (!!sl.link && sl.state !== 'invalid') || LEARNER;")
rep("        {st.view === 'today' && !T && !st.lock && sl.link ? (",
    "        {st.view === 'today' && !T && !st.lock && LEARNER && !sl.link ? (\n          <SoloToday onOpenChapter={(id) => { update({ view: 'path', tool: null, kit: null, drill: id, tab: 'learn', level: 1, from: { drill: id } }); try { window.scrollTo(0, 0); } catch (e) {} }} onOpenTool={(id) => { update({ view: PRACTICE_IDS.includes(id) ? 'practice' : 'tools', tool: id, kit: null, drill: null, from: { tool: id } }); try { window.scrollTo(0, 0); } catch (e) {} }} onAll={() => { update({ view: 'path', tool: null, kit: null, drill: null }); try { window.scrollTo(0, 0); } catch (e) {} }}/>\n        ) : st.view === 'today' && !T && !st.lock && sl.link ? (")
open(p,'w').write(s); print('ok')
