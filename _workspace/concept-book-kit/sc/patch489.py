#!/usr/bin/env python3
# Phase 489: the concept home (rule 16; her 2026-10-19 00:13 '구조화만 시키는거지 ... 최대한 단순하게 해서 보이게 ... 너 제안대로 해보자').
# A new Home view: five areas -> the concepts of one area -> one concept with three buttons (Learn, Try, Check) -> the tools.
# Only Scales and keys is rebuilt so far; the other concepts open their group in the Toolbox. Nothing is deleted.
# Runs on the output of patch487.  python3 patch489.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

HOME = r'''// ─── Phase 489: the concept home. Five areas, then the concepts of one area, then one concept with three buttons (Learn, Try, Check). ───
// Sohyun 2026-10-19: 'a 12-year-old should see it at once', 'the structure only; inside it we decide what to keep, merge or delete'.
// Only Scales and keys is rebuilt in this frame so far; the other concepts open their group in the Toolbox.
const HOME_LINE = {
  'p-staff': ['Where every note lives', '모든 음의 자리'],
  'p-clock': ['The smallest step, sharps and flats', '가장 작은 걸음, 샤프와 플랫'],
  'p-intervals': ['The gap between two notes', '두 음 사이의 거리'],
  'p-scales': ['Every key from one pattern', '패턴 하나로 모든 조'],
  'p-chords': ['Notes stacked together', '쌓아 올린 음들'],
  'r-beat': ['The steady beat and how long notes last', '일정한 박과 음의 길이'],
  't-touch': ['Smooth, short, soft and loud', '이어서, 짧게, 여리게, 세게'],
  't-tempo': ['Slow to fast, and the words for it', '느리게에서 빠르게까지, 그 말들'],
  'k-posture': ['How to sit and hold your hands', '앉는 법과 손 모양'],
  'k-positions': ['Fingers on the keys', '건반 위의 손가락'],
  'k-play': ['Scales and chords with both hands', '두 손으로 치는 스케일과 화음'],
  'c-reading': ['Reading a tune', '곡 읽기'],
  'c-map': ['How a tune is built', '곡의 짜임'],
};
const HOME_LIVE = {
  'p-scales': {
    learn: 'cb-p-scales', check: 'scales', tools: ['scale-finder', 'key-finder'],
    more: ['skg-every', 'skg-acc', 'skg-five', 'transpose', 'csx-penta'],
    learnLine: ['One page: the rule, and all 12 keys at once', '한 장: 규칙, 그리고 12개 조를 한꺼번에'],
    tryLine: ['Two tools: Scale finder, Key finder', '도구 둘: 스케일 찾기, 조 찾기'],
    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },
};
const HOME_AREA_LINE = {
  pitch: ['What the notes are', '음의 높이와 이름'], rhythm: ['How long they last', '음의 길이와 박'], touch: ['How they are played', '소리를 만드는 방법'],
  tech: ['The body and the hands', '몸과 손'], piece: ['Reading a tune and how it is built', '곡을 읽고 짜임 보기'],
};
const HOME_TOOL_LINE = {
  'scale-finder': ['Type or tap any scale: its notes, steps and fingers.', '스케일을 입력하거나 눌러 보세요: 음, 온음과 반음, 손가락 번호.'],
  'key-finder': ['Add the sharps or flats one at a time. Tap any key on the circle.', '샤프나 플랫을 하나씩 더해 봐요. 5도권에서 조를 눌러 봐요.'],
};
function HomeAreaIcon({ id }) {
  const p = { width: 44, height: 44, viewBox: '0 0 48 48', fill: 'none', stroke: '#26296b', strokeWidth: 2.4, strokeLinecap: 'round', strokeLinejoin: 'round', 'aria-hidden': true, style: { flex: 'none' } };
  if (id === 'pitch') return <svg {...p}><path d="M4 14H44M4 21H44M4 28H44M4 35H44M4 42H44" strokeWidth="1.3"/><ellipse cx="22" cy="28" rx="6" ry="4.5" fill="#e4572e" stroke="#e4572e" transform="rotate(-20 22 28)"/><path d="M27.5 26.5V6" stroke="#e4572e"/></svg>;
  if (id === 'rhythm') return <svg {...p}><path d="M8 38V20M18 38V10M28 38V24M38 38V14"/></svg>;
  if (id === 'touch') return <svg {...p}><path d="M6 24L42 12M6 24L42 36"/></svg>;
  if (id === 'tech') return <svg {...p} strokeWidth="3"><path d="M8 34V24M16 34V14M24 34V8M32 34V14M40 34V26"/><path d="M6 40H42" strokeWidth="2"/></svg>;
  return <svg {...p}><path d="M4 32C12 10 20 10 24 28C28 44 36 40 44 16"/></svg>;
}
function HomeChev({ on }) { return <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke={on ? '#e4572e' : '#26296b'} strokeOpacity={on ? 1 : 0.4} strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" style={{flex:'none'}}><path d="M9 5l7 7-7 7"/></svg>; }
const homeRow = (on) => ({ display: 'flex', alignItems: 'center', gap: 14, width: '100%', minHeight: 84, boxSizing: 'border-box', padding: '12px 16px', background: 'var(--surface)', border: '1.5px solid var(--navy-line)', borderRadius: 16, textAlign: 'left', cursor: 'pointer', fontFamily: 'inherit', color: 'var(--navy)' });
const homeTitle = { display: 'block', fontFamily: "'Playfair Display', Georgia, serif", fontWeight: 900, fontSize: 22, lineHeight: 1.15 };
const homeSub = { display: 'block', fontSize: 14, fontWeight: 500, color: 'var(--navy-soft)', marginTop: 3, lineHeight: 1.35 };
function HomeScaleRule() {
  const pat = ['T', 'T', 'S', 'T', 'T', 'T', 'S'];
  return (
    <div style={{background:'var(--surface)',border:'1.5px solid var(--navy-line)',borderRadius:16,padding:'16px 14px 14px',marginBottom:14}}>
      <div style={{fontSize:15,fontWeight:700,lineHeight:1.4,color:'var(--navy)',marginBottom:12}}>{t('Every major scale is the same pattern, starting on a different note.', '장음계는 모두 같은 패턴이에요. 시작하는 음만 달라요.')}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(7,minmax(0,1fr))',gap:5}}>
        {pat.map((p, i) => <div key={i} style={{height:40,borderRadius:10,background:p === 'S' ? '#fbe3da' : '#efe8d6',border:'1.5px solid ' + (p === 'S' ? '#e4572e' : '#dbd2bd'),color:p === 'S' ? '#c0431f' : 'var(--navy)',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:16}}>{p}</div>)}
      </div>
      <div style={{fontSize:13,fontWeight:600,color:'var(--navy-soft)',marginTop:10}}>{t('T = tone (whole step). S = semitone (half step).', 'T = 온음(tone, 한 걸음). S = 반음(semitone, 반 걸음).')}</div>
    </div>
  );
}
function HomeToolPreview({ id }) {
  if (id === 'scale-finder') return <span style={{display:'flex',gap:5,flexWrap:'wrap'}}>{['C', 'D', 'E', 'F', 'G', 'A', 'B'].map((n, i) => <span key={n} style={{display:'inline-flex',alignItems:'center',justifyContent:'center',minWidth:34,height:34,borderRadius:17,background:i === 0 ? '#26296b' : '#fffefa',color:i === 0 ? '#fffefa' : '#26296b',border:'1.5px solid #26296b',fontWeight:800,fontSize:15}}>{n}</span>)}</span>;
  return <span style={{display:'block'}}>
    <span style={{display:'flex',gap:10,fontWeight:800,fontSize:16}}>{['F♯', 'C♯', 'G♯', 'D♯', 'A♯', 'E♯', 'B♯'].map((n, i) => <span key={n} style={{color:i < 3 ? '#c8361b' : '#26296b',opacity:i < 3 ? 1 : 0.2}}>{n}</span>)}</span>
    <span style={{display:'block',fontSize:14,fontWeight:700,marginTop:6}}>Father Charles <span style={{color:'#c8361b',fontWeight:800}}>Goes</span> <span style={{opacity:0.25}}>Down And Ends Battle</span></span>
  </span>;
}
function ConceptHome({ st, update }) {
  const go = (patch) => { update(patch); try { window.scrollTo(0, 0); } catch (e) {} };
  const cat = TOOL_CATS.find(c => c.id === st.hc && c.area !== 'beside');
  const area = TOOL_AREAS.find(a => a.id === (st.ha || (cat && cat.area)) && a.id !== 'beside');
  const live = cat && HOME_LIVE[cat.id];
  const ghost = { fontSize: 14, padding: '10px 16px', minHeight: 44, marginBottom: 10 };
  const [moreOpen, setMoreOpen] = useState(false);
  const step = (n, title, line, on, onClick) => (
    <button key={n} onClick={onClick} style={{...homeRow(on),minHeight:92}}>
      <span style={{flex:'none',width:40,height:40,borderRadius:20,background:'var(--navy)',color:'#fffefa',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:18}}>{n}</span>
      <span style={{flex:1,minWidth:0,display:'block'}}><span style={homeTitle}>{title}</span><span style={homeSub}>{line}</span></span>
      <HomeChev on/>
    </button>
  );
  // level 3: the tools of one concept
  if (cat && live && st.hs === 'try') return (
    <div className="fade-up">
      <button className="ghost-btn" style={ghost} onClick={() => go({ hs: null })}>← {cat.name}</button>
      <StaffHead title={t('Try', '해 보기')}/>
      <div style={{display:'flex',flexDirection:'column',gap:12,marginTop:12}}>
        {live.tools.map(id => { const tl = TOOLS.find(x => x.id === id); if (!tl) return null; return (
          <button key={id} onClick={() => go({ view: 'tools', tool: id, ret: 'home' })} style={{...homeRow(true),flexDirection:'column',alignItems:'flex-start',gap:12,padding:16}}>
            <span style={{...homeTitle,fontSize:26}}>{tl.title}</span>
            <span style={{...homeSub,marginTop:0}}>{LANG === 'ko' ? HOME_TOOL_LINE[id][1] : HOME_TOOL_LINE[id][0]}</span>
            <HomeToolPreview id={id}/>
          </button>
        ); })}
      </div>
      <div style={{borderTop:'1.5px solid var(--navy-line)',marginTop:18,paddingTop:14}}>
        <button className="chip" aria-expanded={moreOpen} style={{padding:'10px 16px',fontSize:14,minHeight:44}} onClick={() => setMoreOpen(!moreOpen)}>{t('More practice', '더 연습하기')} {moreOpen ? '▴' : '▾'}</button>
        {moreOpen && <div style={{display:'flex',gap:6,flexWrap:'wrap',marginTop:10}}>
          {live.more.map(id => { const tl = TOOLS.find(x => x.id === id); return tl ? <button key={id} className="chip" style={{padding:'10px 14px',fontSize:13,minHeight:44}} onClick={() => go({ view: 'tools', tool: id, ret: 'home' })}>{tl.title}</button> : null; })}
        </div>}
      </div>
    </div>
  );
  // level 2: one concept, three buttons
  if (cat && live) return (
    <div className="fade-up">
      <button className="ghost-btn" style={ghost} onClick={() => go({ hc: null, hs: null })}>← {area ? area.name : t('Home', '홈')}</button>
      <StaffHead title={cat.name}/>
      <div style={{marginTop:14}}><HomeScaleRule/></div>
      <div style={{display:'flex',flexDirection:'column',gap:10}}>
        {step(1, t('Learn', '배우기'), LANG === 'ko' ? live.learnLine[1] : live.learnLine[0], false, () => go({ view: 'tools', tool: live.learn, ret: 'home' }))}
        {step(2, t('Try', '해 보기'), LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ hs: 'try' }))}
        {step(3, t('Check', '확인하기'), LANG === 'ko' ? live.checkLine[1] : live.checkLine[0], false, () => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' }))}
      </div>
    </div>
  );
  // level 1: the concepts of one area
  if (area) return (
    <div className="fade-up">
      <button className="ghost-btn" style={ghost} onClick={() => go({ ha: null, hc: null, hs: null })}>← {t('Home', '홈')}</button>
      <StaffHead title={area.name}/>
      <div style={{fontSize:15,fontWeight:500,color:'var(--navy-soft)',margin:'10px 0 12px'}}>{LANG === 'ko' ? HOME_AREA_LINE[area.id][1] : HOME_AREA_LINE[area.id][0]}</div>
      <div style={{display:'flex',flexDirection:'column',gap:10}}>
        {TOOL_CATS.filter(c => c.area === area.id).map(c => { const on = !!HOME_LIVE[c.id], ln = HOME_LINE[c.id] || ['', '']; return (
          <button key={c.id} style={{...homeRow(on),minHeight:76}} onClick={() => {
            if (on) go({ ha: area.id, hc: c.id, hs: null });
            else { go({ view: 'toolbox' }); setTimeout(() => { try { const el = document.getElementById('cat-' + c.id); if (el) el.scrollIntoView(); } catch (e) {} }, 300); }
          }}>
            <span style={{flex:1,minWidth:0,display:'block'}}><span style={{...homeTitle,fontSize:20}}>{c.name}</span><span style={{...homeSub,fontSize:13,marginTop:2}}>{LANG === 'ko' ? ln[1] : ln[0]}</span></span>
            {on ? <HomeChev on/> : <span style={{flex:'none',fontSize:11,fontWeight:800,color:'var(--navy-soft)',border:'1px solid var(--navy-line)',borderRadius:10,padding:'2px 8px'}}>{t('Toolbox', '도구함')}</span>}
          </button>
        ); })}
      </div>
    </div>
  );
  // level 0: the five areas
  return (
    <div className="fade-up">
      <h2 style={{fontFamily:"'Playfair Display', Georgia, serif",fontWeight:900,fontSize:32,lineHeight:1.1,margin:'4px 0 16px',color:'var(--navy)',textWrap:'balance'}}>{t('Where do you want to go?', '어디로 갈까요?')}</h2>
      <div style={{display:'flex',flexDirection:'column',gap:10}}>
        {TOOL_AREAS.filter(a => a.id !== 'beside').map(a => (
          <button key={a.id} style={homeRow(false)} onClick={() => go({ ha: a.id, hc: null, hs: null })}>
            <HomeAreaIcon id={a.id}/>
            <span style={{flex:1,minWidth:0,display:'block'}}><span style={{...homeTitle,fontSize:24}}>{a.name}</span><span style={homeSub}>{LANG === 'ko' ? HOME_AREA_LINE[a.id][1] : HOME_AREA_LINE[a.id][0]}</span></span>
            <HomeChev on/>
          </button>
        ))}
      </div>
    </div>
  );
}

'''
rep("function App() {\n  const [teacher, setTeacher] = useState(initialMode);", HOME + "function App() {\n  const [teacher, setTeacher] = useState(initialMode);")

# the address: view=home&area=..&concept=..&sec=..
rep("    kn: p.get('kn') || '',\n", "    kn: p.get('kn') || '',\n    ha: TOOL_AREAS.some(a => a.id === p.get('area')) ? p.get('area') : null, hc: TOOL_CATS.some(c => c.id === p.get('concept')) ? p.get('concept') : null, hs: p.get('room') === 'try' ? 'try' : null, ret: p.get('ret') === 'home' ? 'home' : null,\n")
rep("view: p.get('kit') ? 'kit' :", "view: p.get('kit') ? 'kit' : p.get('ret') === 'home' && p.get('drill') ? 'home' :")
rep("p.get('view') === 'students' ? 'students' :", "p.get('view') === 'students' ? 'students' : p.get('view') === 'home' ? 'home' :")
rep("      else if (st.view === 'today') p.set('view', 'today');\n",
    "      else if (st.view === 'today') p.set('view', 'today');\n      else if (st.view === 'home' && !st.drill) { p.set('view', 'home'); if (st.ha) p.set('area', st.ha); if (st.hc) p.set('concept', st.hc); if (st.hs) p.set('room', st.hs); }\n")
HOMEURL = "if (st.ret === 'home') { p.set('ret', 'home'); if (st.ha) p.set('area', st.ha); if (st.hc) p.set('concept', st.hc); if (st.hs) p.set('room', st.hs); }"
rep("      else if (st.view === 'tools' || st.view === 'practice') { if (st.tool) p.set('tool', st.tool); if (st.view === 'practice' || !st.tool) p.set('view', st.view); }", "      else if (st.view === 'tools' || st.view === 'practice') { if (st.tool) p.set('tool', st.tool); if (st.view === 'practice' || !st.tool) p.set('view', st.view); " + HOMEURL + " }")
rep("        p.set('drill', active.id);\n", "        p.set('drill', active.id);\n        if (st.view === 'home') { p.set('ret', 'home'); if (st.ha) p.set('area', st.ha); if (st.hc) p.set('concept', st.hc); }\n")
rep("}, [active.id, st.drill, st.tab, level, st.mode, st.lock, st.view, st.tool, st.kit, st.kn, lang]);", "}, [active.id, st.drill, st.tab, level, st.mode, st.lock, st.view, st.tool, st.kit, st.kn, st.ha, st.hc, st.hs, lang]);")

# a chapter opened from Home (Check) goes back to Home
rep("const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox') && !!st.drill;", "const inChapter = (st.view === 'path' || st.view === 'chapters' || st.view === 'toolbox' || (T && st.view === 'home')) && !!st.drill;")

# the tab, the view, the way back from a tool
rep("(T ? [['path', t('Chapters', '챕터')],", "(T ? [['home', t('Home', '홈')], ['path', t('Chapters', '챕터')],")
rep("(T && v === 'toolbox' && st.view === 'tools' && st.ret === 'toolbox')", "(T && v === 'toolbox' && st.view === 'tools' && st.ret === 'toolbox') || (T && v === 'home' && st.view === 'tools' && st.ret === 'home')", s.count("(T && v === 'toolbox' && st.view === 'tools' && st.ret === 'toolbox')"))
rep("        ) : !inChapter && !st.lock ? (\n          T && st.view === 'toolbox'",
    "        ) : st.view === 'home' && T && !inChapter && !st.lock ? (\n          <ConceptHome st={st} update={update}/>\n        ) : !inChapter && !st.lock ? (\n          T && st.view === 'toolbox'")
rep("st.view === 'practice' ? '← Practice' : '← Toolbox'}", "st.view === 'practice' ? '← Practice' : st.ret === 'home' ? homeBack : '← Toolbox'}")
rep("update({ tool: null, view: st.ret || (T && st.view === 'tools' ? 'toolbox' : st.view), ret: null })", "update({ tool: null, view: (st.view === 'practice' ? null : st.ret) || (T && st.view === 'tools' ? 'toolbox' : st.view), ret: null })")
rep("  function jumpToChapter(id) {", "  const homeBack = '← ' + (st.hs === 'try' ? t('Try', '해 보기') : ((TOOL_CATS.find(c => c.id === st.hc) || {}).name || t('Home', '홈')));\n  useEffect(() => { if (st.view === 'home' && !T) setSt(prev => ({ ...prev, view: 'path', drill: null, ret: null })); }, [st.view, T]);\n  function jumpToChapter(id) {")
rep("{T ? t('← Back', '← 뒤로') :", "{T ? (st.view === 'home' ? '← ' + ((TOOL_CATS.find(c => c.id === st.hc) || {}).name || t('Home', '홈')) : t('← Back', '← 뒤로')) :")
rep("update({ view: v, tool: null, kit: null, from: null, drill: (v === 'practice' || v === 'students') ? st.drill : null })", "update({ view: v, tool: null, kit: null, from: null, ret: null, drill: (v === 'practice' || v === 'students') ? st.drill : null, ...(v === 'home' ? { ha: null, hc: null, hs: null } : {}) })")
rep("'← Toolbox': '← 도구 모음', '← Lesson plan'", "'← Toolbox': '← 도구 모음', '← Home': '← 홈', '← Lesson plan'")

open(dst, 'w', encoding='utf-8').write(s)
print('patched 489', len(s))
