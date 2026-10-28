import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:100])
    s = s.replace(old, new)
# Build CS, part 2 (board call 8, the dashboard; call 2, her 21:18 'agree'):
#  - the checks and the placement follow a linked student: two more synced stores, 'checks' (pb_checks_v1) and 'place'
#    (pb_place_v1), merged without loss (a room keeps its first pass, best score and furthest review; a floor checkpoint
#    keeps its latest round; the later placement wins). Until the database step phaseD is run the server refuses the two
#    stores: that is remembered for the session and nothing else changes; once it is run, what is already on the device is sent.
#  - the teacher's plan for a student (start floor, theory grade, the Home for an adult) comes with pb_get as 'plan' and is
#    kept on the device (pb_plan_v1). The plan wins over the student's own placement. The house's next room and 'you are
#    here' start from that floor; theory rooms above the theory grade wait; a floor checkpoint asks only theory up to that
#    grade (call 24). A child sees the dollhouse and Practice, as now; the Home opens for a linked student only when the
#    teacher has switched it on (an adult): a button on the Today page, and the Home with a way back to Today.
rep("""const placeFloor = () => { const p = loadPlace(); return p && p.piano > 0 ? p.piano : 0; };""",
"""const PLAN_KEY = 'pb_plan_v1';   // Build CS: the teacher's plan for a linked student (from pb_get): { piano: floor index, theory: 1..7, home: bool }
function loadPlan() { try { const v = JSON.parse(localStorage.getItem(PLAN_KEY)); return v && typeof v === 'object' && !Array.isArray(v) ? v : null; } catch (e) { return null; } }
const placeFloor = () => { const pl = loadPlan(); if (pl && Number.isInteger(pl.piano) && pl.piano >= 0 && PATH_STAGES[pl.piano]) return pl.piano; const p = loadPlace(); return p && p.piano > 0 ? p.piano : 0; };
const myTheory = () => { const pl = loadPlan(); if (pl && pl.theory >= 1 && pl.theory <= 7) return Math.round(pl.theory); const p = loadPlace(); return p && p.theory >= 1 && p.theory <= 7 ? p.theory : 7; };   // 7 = no limit
const planHome = () => { const pl = loadPlan(); return !!(pl && pl.home === true); };""")
rep("""  const p = loadPlace(), k = placeFloor(), th = p && p.theory ? p.theory : 7;""", """  const k = placeFloor(), th = myTheory();""")
# the floor checkpoint: theory only up to the student's theory grade
rep("""  const N = f.part ? FLOOR_HALF_N : FLOOR_N, c = loadChecks(), rec = c.floors[f.key];""",
"""  const N = f.part ? FLOOR_HALF_N : FLOOR_N, c = loadChecks(), rec = c.floors[f.key];
  const thG = myTheory(), fIds0 = thG < 7 ? f.ids.filter(id => !(THEORY_ROOM[id] > thG)) : f.ids, fIds = fIds0.length ? fIds0 : f.ids, thCut = fIds.length < f.ids.length;   // Build CS (call 24)""")
rep("""  const start = () => { setItems(chkFloorItems(f.ids, N)); setOut(null); setMode('run');""", """  const start = () => { setItems(chkFloorItems(fIds, N)); setOut(null); setMode('run');""")
rep("""    const right = r.filter(x => x.ok).length, review = f.ids.filter(id => per[id] && per[id].miss.length);""", """    const right = r.filter(x => x.ok).length, review = fIds.filter(id => per[id] && per[id].miss.length);""")
rep("""      <div style={{fontSize:16,fontWeight:900,color:'#26296b',lineHeight:1.3}}>{chkFloorName(f)}</div>""",
"""      <div style={{fontSize:16,fontWeight:900,color:'#26296b',lineHeight:1.3}}>{chkFloorName(f)}</div>
      {thCut && <div data-testid="floor-theory-cut" style={{fontSize:12.5,color:'#6d6f9c',fontWeight:700,margin:'2px 0 0'}}>{t('Theory up to ' + theoryName(thG) + ' only: ' + fIds.length + ' of the ' + f.ids.length + ' rooms.', theoryName(thG) + '까지의 이론만: 방 ' + f.ids.length + '개 중 ' + fIds.length + '개.')}</div>}""")
# sync: two more stores
rep("""  posture: 'pb_posture_v1', arm_ex: 'pb_arm_ex_v1', last_chapter: 'pb_last_chapter_v1',
};""", """  posture: 'pb_posture_v1', arm_ex: 'pb_arm_ex_v1', last_chapter: 'pb_last_chapter_v1',
  checks: 'pb_checks_v1', place: 'pb_place_v1',   // Build CS (needs the database step phaseD; refused quietly before it)
};
const SYNC_LATE = ['checks', 'place'];   // stores added after devices already held them: sent once even if unchanged""")
rep("""const SY = { token: null, watch: false,""", """const SY = { noStore: {}, token: null, watch: false,""")
rep("""  const ar = syReadStore('arm_ex'); if (ar && Object.keys(ar).some(k => syNum(ar[k]) > 0)) return true;
  return false;""", """  const ar = syReadStore('arm_ex'); if (ar && Object.keys(ar).some(k => syNum(ar[k]) > 0)) return true;
  const ck = syReadStore('checks'); if (ck && syIsObj(ck.rooms) && Object.keys(ck.rooms).length) return true;
  return false;""")
rep("""    return { marks: { ...(syIsObj(R.marks) ? R.marks : {}), ...(syIsObj(L.marks) ? L.marks : {}) }, history: Object.keys(byDay).sort().map(d => byDay[d]).slice(-8) };
  }
  return L;""", """    return { marks: { ...(syIsObj(R.marks) ? R.marks : {}), ...(syIsObj(L.marks) ? L.marks : {}) }, history: Object.keys(byDay).sort().map(d => byDay[d]).slice(-8) };
  }
  if (store === 'checks') {                                          // Build CS: first pass, best score, furthest review; the latest checkpoint round
    const a = syIsObj(R.rooms) ? R.rooms : {}, b = syIsObj(L.rooms) ? L.rooms : {}, rooms = {};
    new Set([...Object.keys(a), ...Object.keys(b)]).forEach(id => {
      const x = syIsObj(a[id]) ? a[id] : null, y = syIsObj(b[id]) ? b[id] : null;
      if (!x || !y) { rooms[id] = x || y; return; }
      const o = { ...x, ...y, best: Math.max(syNum(x.best), syNum(y.best)), tries: Math.max(syNum(x.tries), syNum(y.tries)) };
      const ps = [x.pass, y.pass].map(syNum).filter(v => v > 0); if (ps.length) o.pass = Math.min(...ps);
      const rx = syIsObj(x.review) ? x.review : null, ry = syIsObj(y.review) ? y.review : null;
      if (rx || ry) o.review = !rx ? ry : !ry ? rx : (syNum(ry.stage) > syNum(rx.stage) || (syNum(ry.stage) === syNum(rx.stage) && syNum(ry.due) >= syNum(rx.due))) ? ry : rx;
      rooms[id] = o;
    });
    const floors = { ...(syIsObj(R.floors) ? R.floors : {}) };
    Object.entries(syIsObj(L.floors) ? L.floors : {}).forEach(([k, v]) => { if (syIsObj(v) && (!syIsObj(floors[k]) || syNum(v.at) >= syNum(floors[k].at))) floors[k] = v; });
    return { ...R, ...L, rooms, floors };
  }
  if (store === 'place') return syNum(L.at) >= syNum(R.at) ? L : R;   // the later placement
  return L;""")
rep("""        else break;                                                                          // never synced and not changed: leave it""",
"""        else if (SYNC_LATE.includes(store) && !SY.noStore[store]) { toPush = L; pushBase = 0; }      // Build CS: held before it was synced: send it once
        else break;                                                                          // never synced and not changed: leave it""")
rep("""  for (const store of SYNC_STORE_NAMES) {
    let remote = d && d.stores && syIsObj(d.stores[store]) ? d.stores[store] : null;      // { value, rev }""", """  for (const store of SYNC_STORE_NAMES) {
    if (SY.noStore[store]) { syClearDirty(store); continue; }                              // Build CS: refused earlier in this session (phaseD not run)
    let remote = d && d.stores && syIsObj(d.stores[store]) ? d.stores[store] : null;      // { value, rev }""")
rep("""      syClearDirty(store); break;                                                            // refused for good (size / shape): do not retry forever""",
"""      if (a.reason === 'store') SY.noStore[store] = 1;                                         // Build CS: the database does not take this store yet (phaseD not run)
      syClearDirty(store); break;                                                            // refused for good (size / shape): do not retry forever""")
rep("""  [SYNC_OWNER_KEY, SYNC_REVS_KEY, SYNC_DIRTY_KEY, SYNC_LOGQ_KEY, TODAY_CACHE_KEY, TODAY_TICKS_KEY, 'pb_my_keys_v1'].forEach(syDel);
}""", """  [SYNC_OWNER_KEY, SYNC_REVS_KEY, SYNC_DIRTY_KEY, SYNC_LOGQ_KEY, TODAY_CACHE_KEY, TODAY_TICKS_KEY, 'pb_my_keys_v1', PLAN_KEY].forEach(syDel);
}
// Build CS: the teacher's plan from pb_get ('plan' is there once phaseD is run; without the key nothing is touched). -> true when it changed
function syApplyPlan(d) {
  if (!d || typeof d !== 'object' || !('plan' in d)) return false;
  const v = syIsObj(d.plan) ? JSON.stringify(d.plan) : null; let cur = null;
  try { cur = localStorage.getItem(PLAN_KEY); } catch (e) {}
  if (cur === v) return false;
  try { SY.applying = true; if (v == null) localStorage.removeItem(PLAN_KEY); else localStorage.setItem(PLAN_KEY, v); } catch (e) {} finally { SY.applying = false; }
  return true;
}""")
rep("""    sySetOwner(d.ref);
  }
  const res = await syReconcile(token, d, false, pushOnly);""", """    sySetOwner(d.ref);
  }
  if (!pushOnly && syApplyPlan(d)) sySet({ appliedN: SY.appliedN + 1 });   // Build CS
  const res = await syReconcile(token, d, false, pushOnly);""")
# call 2: the Home for an adult the teacher switched it on for
rep("""function StudentHome({ link, onOpenChapter, onOpenTool }) {
  const sec = { marginTop: 26 };
  return (
    <div data-testid="student-home">
      <TodayView link={link} onOpenChapter={onOpenChapter} onOpenTool={onOpenTool} onAll={() => {}} head={<HowItWorks/>} compact/>""",
"""function StudentHome({ link, onOpenChapter, onOpenTool, onHome }) {
  const sec = { marginTop: 26 };
  return (
    <div data-testid="student-home">
      <TodayView link={link} onOpenChapter={onOpenChapter} onOpenTool={onOpenTool} onAll={() => {}} head={<HowItWorks/>} compact/>
      {onHome && planHome() && <div style={sec}><button className="primary-btn" data-testid="today-home" onClick={onHome}>{t('The Home: every topic →', '홈: 모든 주제 →')}</button></div>}""")
rep("""  const T = teacher && !preview && !st.lock;
  UI_TEACHER = T;
  const active = DRILLS.find(d => d.id === st.drill) || DRILLS[0];
  const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || (T && st.view === 'home')) && !!st.drill;""",
"""  const T = teacher && !preview && !st.lock;
  UI_TEACHER = T;
  const HM = T || (showToday && !st.lock && planHome());   // Build CS (call 2): the Home is the teacher's, and an adult's when the teacher switched it on
  const active = DRILLS.find(d => d.id === st.drill) || DRILLS[0];
  const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || (HM && st.view === 'home')) && !!st.drill;""")
rep("""  useEffect(() => { if (st.view === 'home' && !T) setSt(prev => ({ ...prev, view: 'path', drill: null, ret: null })); }, [st.view, T]);""",
"""  useEffect(() => { if (st.view === 'home' && !HM) setSt(prev => ({ ...prev, view: 'path', drill: null, ret: null })); }, [st.view, HM]);""")
rep("""onOpenTool={(id) => { update({ view: PRACTICE_IDS.includes(id) ? 'practice' : 'tools', tool: id, kit: null, drill: null, from: { tool: id } }); try { window.scrollTo(0, 0); } catch (e) {} }}""",
"""onOpenTool={(id) => { update({ view: PRACTICE_IDS.includes(id) ? 'practice' : 'tools', tool: id, kit: null, drill: null, from: { tool: id } }); try { window.scrollTo(0, 0); } catch (e) {} }} onHome={() => { update({ view: 'home', ha: null, hc: null, hs: null, drill: null, tool: null, kit: null, from: null }); try { window.scrollTo(0, 0); } catch (e) {} }}""")
rep("""        ) : st.view === 'home' && T && !inChapter && !st.lock ? (
          <ConceptHome st={st} update={update}/>""", """        ) : st.view === 'home' && HM && !inChapter && !st.lock ? (
          <>{!st.ha && !st.hc && !st.hs && todayBack}<ConceptHome st={st} update={update}/></>""")
rep("""{T ? (st.view === 'home' ? '← ' + ((homeCatById(st.hc)""", """{(T || (HM && st.view === 'home')) ? (st.view === 'home' ? '← ' + ((homeCatById(st.hc)""")
rep("""{!(T && st.view === 'home') && <button className="ghost-btn" style={{fontSize:13,padding:'5px 9px'}} disabled={k <= 0}""", """{!(HM && st.view === 'home') && <button className="ghost-btn" style={{fontSize:13,padding:'5px 9px'}} disabled={k <= 0}""")
rep("""{!(T && st.view === 'home') && <button className="ghost-btn" style={{fontSize:13,padding:'5px 9px'}} disabled={k >= list.length - 1}""", """{!(HM && st.view === 'home') && <button className="ghost-btn" style={{fontSize:13,padding:'5px 9px'}} disabled={k >= list.length - 1}""")
rep("""{!st.lock && !(T && st.view === 'home') && <AfterNote""", """{!st.lock && !(HM && st.view === 'home') && <AfterNote""")
rep("""drillOnly={T && st.view === 'home'}""", """drillOnly={HM && st.view === 'home'}""")
rep("""{!st.lock && !(T && st.view === 'home') && <PathNext""", """{!st.lock && !(HM && st.view === 'home') && <PathNext""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
