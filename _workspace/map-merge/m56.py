p='drills.src.html'; s=open(p).read()
assert 'VIS_OPEN' not in s
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)

# ── A. visitors (no teacher, no student link) see a few finished rooms per floor; the rest are locked ──
rep("function thRoomClean(view, state, id, x, y, w, h, fs, out, dimNew, lay, cmp) {", r'''// m56 (her 2 Nov): a visitor sees a few well-made rooms on each floor; every room opens with a teacher's student link.
const VIS_OPEN = new Set(['first-steps', 'note-values', 'staff', 'rhythm', 'scales', 'intervals', 'key-signatures', 'melody', 'harmony-2', 'harmony-3', 'melody-3', 'keys-4', 'harmony-5', 'arps-6', 'pieces-78', 'composers', 'styles']);
const isVisitor = () => !UI_TEACHER && !(linkTokenFromHash() || loadStoredLink());
const visLocked = (id) => isVisitor() && !!id && !VIS_OPEN.has(id);
function VisitorLock({ onBack }) {
  return <div data-testid="visitor-lock" className="fade-up" style={{textAlign:'center',background:'var(--surface)',border:'1.5px solid var(--navy-line)',borderRadius:16,padding:'26px 18px',margin:'10px 0'}}>
    <svg width="40" height="44" viewBox="0 0 40 44" aria-hidden="true"><rect x="5" y="19" width="30" height="22" rx="4" fill="var(--navy)"/><path d="M12 19v-6a8 8 0 0 1 16 0v6" fill="none" stroke="var(--navy)" strokeWidth="4"/><circle cx="20" cy="30" r="3" fill="#c9a24f"/></svg>
    <div style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:800,color:'var(--navy)',margin:'8px 0 4px'}}>{t('This room is locked', '잠긴 방이에요')}</div>
    <div style={{fontSize:14.5,color:'var(--muted)',lineHeight:1.5,maxWidth:340,margin:'0 auto 14px'}}>{t('Every room opens with a student link from your teacher. The open rooms on each floor are yours to try now.', '모든 방은 선생님이 주는 학생 링크로 열려요. 층마다 열린 방은 지금 바로 해 볼 수 있어요.')}</div>
    <button className="primary-btn" style={{width:'auto',padding:'10px 20px'}} onClick={onBack}>{t('Back to the house', '집으로 돌아가기')}</button>
  </div>;
}
function thRoomClean(view, state, id, x, y, w, h, fs, out, dimNew, lay, cmp) {''')
rep("  if (view.focus && thArea(id) !== view.focus) s += '<rect x=\"' + pFix(x + 1) + '\" y=\"' + pFix(y + 1) + '\" width=\"' + pFix(w - 2) + '\" height=\"' + pFix(h - 2) + '\" fill=\"#fff\" opacity=\"0.78\" stroke=\"none\"/>';\n  const nm = CH_SHORT[id] || [id, ''], sb = CH_SUB[id];",
    "  if (view.focus && thArea(id) !== view.focus) s += '<rect x=\"' + pFix(x + 1) + '\" y=\"' + pFix(y + 1) + '\" width=\"' + pFix(w - 2) + '\" height=\"' + pFix(h - 2) + '\" fill=\"#fff\" opacity=\"0.78\" stroke=\"none\"/>';\n"
    "  if (view.lock && view.lock(id)) { const lx = x + w - (cmp ? 13 : 16), ly = y + (cmp ? 5 : 7);   /* m56: a visitor's locked room, greyed, a small padlock */\n"
    "    s += '<rect x=\"' + pFix(x + 1) + '\" y=\"' + pFix(y + 1) + '\" width=\"' + pFix(w - 2) + '\" height=\"' + pFix(h - 2) + '\" fill=\"#f4f1ea\" opacity=\"0.72\" stroke=\"none\"/>'\n"
    "      + '<rect x=\"' + pFix(lx) + '\" y=\"' + pFix(ly + 4) + '\" width=\"9\" height=\"7\" rx=\"1.5\" fill=\"' + ST.N + '\"/><path d=\"M' + pFix(lx + 2) + ' ' + pFix(ly + 4) + 'v-1.6a2.5 2.5 0 0 1 5 0v1.6\" fill=\"none\" stroke=\"' + ST.N + '\" stroke-width=\"1.4\"/>'; }\n"
    "  const nm = CH_SHORT[id] || [id, ''], sb = CH_SUB[id];")
rep("review: placeReview(), pawn: name ?", "review: placeReview(), lock: isVisitor() ? visLocked : null, pawn: name ?")
# a locked room opened any way (house, library, links) shows the lock card
rep("        ) : <>\n        {!st.lock && (() => {\n          const sg = catOfChapter(active.id)",
    "        ) : visLocked(st.drill) ? <VisitorLock onBack={() => { update({ view: 'path', drill: null, from: null }); try { window.scrollTo(0, 0); } catch (e) {} }}/> : <>\n        {!st.lock && (() => {\n          const sg = catOfChapter(active.id)")
# a visitor's placement chip asks the question plainly
rep("focus && focus.kind === 'start' ? t('Already playing? Find your start ▸', '이미 치고 있나요? 시작점 찾기 ▸'",
    "isVisitor() ? t('Which floor should I start on? ▸', '어느 층에서 시작할까? ▸') : focus && focus.kind === 'start' ? t('Already playing? Find your start ▸', '이미 치고 있나요? 시작점 찾기 ▸'")

# ── B. cards: pass a floor's checkpoint, the butler deals you its card ──
rep("const PRACTICE_GROUPS = [", r'''// m56 (her 2 Nov, mockup approved): one playing card per floor checkpoint passed (A, 2, 3 …; spades, hearts, diamonds, clubs in turn)
const CARD_SEEN_KEY = 'pb_cards_seen_v1';
const CARD_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'], CARD_SUITS = ['♠', '♥', '♦', '♣'];
function myCards() {
  const rec = loadChecks().floors;
  return checkFloors().map((f, i) => { const r = rec[f.key]; return { key: f.key, name: chkFloorName(f), rank: CARD_RANKS[i % 13], suit: CARD_SUITS[i % 4], on: !!(r && !(r.review || []).length), at: r && r.at }; });
}
function PlayingCard({ c, small }) {
  const col = c.suit === '♥' || c.suit === '♦' ? '#e4572e' : '#26296b';
  const box = { position: 'relative', aspectRatio: '5 / 7', borderRadius: 10, border: '1.5px solid #26296b', boxShadow: 'inset 0 0 0 4px #fff, inset 0 0 0 5px rgba(38,41,107,0.25)', background: '#fff', overflow: 'hidden' };
  if (!c.on) return <div style={{ ...box, background: 'repeating-linear-gradient(45deg,#26296b 0 6px,#2f3278 6px 12px)', boxShadow: 'inset 0 0 0 4px #fff' }}>
    <span style={{ position: 'absolute', left: 0, right: 0, top: '34%', textAlign: 'center', color: '#c9a24f', font: '700 26px Georgia, serif' }}>?</span>
    {!small && <span style={{ position: 'absolute', left: 4, right: 4, bottom: 6, textAlign: 'center', fontSize: 9.5, fontWeight: 700, color: '#c9cbe6' }}>{c.name}</span>}</div>;
  const corner = (rot) => <b style={{ position: 'absolute', [rot ? 'right' : 'left']: 7, [rot ? 'bottom' : 'top']: small ? 4 : 20, fontSize: small ? 10 : 13, lineHeight: 1, textAlign: 'center', color: col, transform: rot ? 'rotate(180deg)' : 'none' }}>{c.rank}<br/>{c.suit}</b>;
  return <div style={box}>{corner(false)}<span style={{ position: 'absolute', left: 0, right: 0, top: '26%', textAlign: 'center', fontSize: small ? 26 : 38, color: col }}>{c.suit}</span>{!small && corner(true)}
    {!small && <span style={{ position: 'absolute', left: 4, right: 4, bottom: 5, textAlign: 'center', fontSize: 9.5, fontWeight: 700, color: '#6d6f9c' }}>{c.name}</span>}</div>;
}
function MyCards() {
  const cards = myCards(), got = cards.filter(c => c.on);
  let seen = {}; try { seen = JSON.parse(localStorage.getItem(CARD_SEEN_KEY) || '{}') || {}; } catch (e) {}
  const fresh = got.filter(c => !seen[c.key]).sort((a, b) => (b.at || 0) - (a.at || 0))[0];
  useEffect(() => { if (!fresh) return; const n = { ...seen }; got.forEach(c => { n[c.key] = 1; }); try { localStorage.setItem(CARD_SEEN_KEY, JSON.stringify(n)); } catch (e) {} }, [fresh && fresh.key]);
  if (!cards.length) return null;
  return <div data-testid="my-cards" style={{ marginTop: 18 }}>
    <div style={{ fontSize: 11, fontWeight: 900, letterSpacing: '0.1em', textTransform: 'uppercase', color: 'var(--coral)', margin: '0 0 2px' }}>{t('My cards', '나의 카드')}</div>
    <div style={{ fontSize: 13, color: 'var(--muted)', margin: '0 0 10px' }}>{t('Pass a floor’s checkpoint and the butler deals you its card. ' + got.length + ' of ' + cards.length + '.', '층 중간점검을 통과하면 버틀러가 그 층의 카드를 줘요. ' + cards.length + '장 중 ' + got.length + '장.')}</div>
    {fresh && <div data-testid="new-card" style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--surface)', border: '1.5px solid var(--navy-line)', borderRadius: 14, padding: 12, marginBottom: 12 }}>
      <div style={{ width: 62, flex: 'none' }}><PlayingCard c={fresh} small/></div>
      <div><b style={{ color: 'var(--navy)' }}>{t('New card!', '새 카드!')}</b><div style={{ fontSize: 13, color: 'var(--muted)', lineHeight: 1.4 }}>{t('You passed the ' + fresh.name + ' checkpoint. The butler deals you the ' + fresh.rank + ' ' + fresh.suit + '.', fresh.name + ' 중간점검을 통과했어요. 버틀러가 ' + fresh.suit + fresh.rank + ' 카드를 줘요.')}</div></div></div>}
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0, 1fr))', gap: 10 }}>{cards.map(c => <PlayingCard key={c.key} c={c}/>)}</div>
  </div>;
}
const PRACTICE_GROUPS = [''')
rep('''          {ids.map((id, i) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null; return <SlimRow key={id} title={id === 'perfect-counter' ? t('5 in a row', '5번 연속') : LANG === 'ko' && TOOL_KO[id] ? TOOL_KO[id][0] : tl.title} sub={tl.blurb} onClick={() => onOpen(id)} last={i === ids.length - 1}/>; })}
        </div>)}
      </div>''', '''          {ids.map((id, i) => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null; return <SlimRow key={id} title={id === 'perfect-counter' ? t('5 in a row', '5번 연속') : LANG === 'ko' && TOOL_KO[id] ? TOOL_KO[id][0] : tl.title} sub={tl.blurb} onClick={() => onOpen(id)} last={i === ids.length - 1}/>; })}
        </div>)}
        {!isVisitor() && <MyCards/>}
      </div>''')
# ── C. the teacher sees whether this browser is signed in to the dashboard (her 2 Nov: 'I can't tell if I'm logged in') ──
rep("function tTeacherSession() {", """function tTeacherWho() {   // m56: the dashboard login kept in this browser -> { email } or null
  try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (!/^sb-.*-auth-token$/.test(k)) continue;
    const v = JSON.parse(localStorage.getItem(k) || 'null'); const u = v && (v.user || (v.currentSession && v.currentSession.user)); if (u && (v.refresh_token || v.access_token)) return { email: u.email || '' }; } } catch (e) {}
  return null;
}
function tTeacherSession() {""")
rep("""{T && <div data-testid="teacher-label" style={{fontSize:11,fontWeight:900,color:'#e4572e',letterSpacing:'0.06em',textTransform:'uppercase',marginTop:2}}>{t('Teacher view', '교사 화면')}</div>}""",
    """{T && <div data-testid="teacher-label" style={{fontSize:11,fontWeight:900,color:'#e4572e',letterSpacing:'0.06em',textTransform:'uppercase',marginTop:2}}>{t('Teacher view', '교사 화면')}</div>}
            {T && (() => { const w = tTeacherWho(); return <div data-testid="signin-state" style={{fontSize:12,fontWeight:700,marginTop:3,color:w ? '#2e8a6e' : '#9a9cc0',display:'flex',alignItems:'center',gap:5}}>
              <span aria-hidden="true" style={{width:7,height:7,borderRadius:4,background:w ? '#2e8a6e' : '#c9c6d9',display:'inline-block'}}/>
              {w ? t('Signed in' + (w.email ? ' as ' + w.email : ''), (w.email ? w.email + '(으)로 ' : '') + '로그인됨') : <span>{t('Not signed in · ', '로그인 안 됨 · ')}<a href="login.html" style={{color:'#e4572e'}}>{t('Sign in', '로그인')}</a></span>}</div>; })()}""")
open(p,'w').write(s); print('ok')
