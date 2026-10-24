import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build O (her 2026-10-25 00:36, '응 그렇게 해보자': step 1 of the curriculum plan, built on the recommendations):
# 1. The dollhouse floors are named by grade (decision 1): today's floors 1-2 are Ground (two storeys), 3-4 are P-1
#    (Preliminary and Grade 1, two storeys), 5 is 2-3. A band with two storeys tells them apart with I and II on the
#    plaque (the house's classical capitals). The rooms stay where they are.
rep("""const PATH_STAGES = [   // Phase 436: five levels, the floors of the house, in the plan's order; inside a floor any room first
  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff'], en: ['Level 1',""",
    """const PATH_STAGES = [   // Phase 436: five floors of the house, in the plan's order; inside a floor any room first.
  // Build O (2026-10-25): named by grade, as the curriculum plan's floors -- Ground (before Preliminary), P–1 (Preliminary and
  // Grade 1), 2–3; a band with two storeys is told apart by I and II. The Home's floor marks use the same names (HOME_FLOOR).
  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff'], en: ['Ground · I',""")
rep("""ko: ['1층', '바른 자세, 건반과 글자, 일정한 박, 처음 음표 길이, 그리고 오선.'] },""",
    """ko: ['Ground · I', '바른 자세, 건반과 글자, 일정한 박, 처음 음표 길이, 그리고 오선.'] },""")
rep("""en: ['Level 2', 'Both staves,""", """en: ['Ground · II', 'Both staves,""")
rep("""ko: ['2층', '두 오선,""", """ko: ['Ground · II', '두 오선,""")
rep("""en: ['Level 3', 'Speed,""", """en: ['P–1 · I', 'Speed,""")
rep("""ko: ['3층', '빠르기,""", """ko: ['P–1 · I', '빠르기,""")
rep("""en: ['Level 4', 'Key signatures,""", """en: ['P–1 · II', 'Key signatures,""")
rep("""ko: ['4층', '조표,""", """ko: ['P–1 · II', '조표,""")
rep("""en: ['Level 5', 'How a tune""", """en: ['2–3', 'How a tune""")
rep("""ko: ['5층', '선율의 모양""", """ko: ['2–3', '선율의 모양""")

# the words that named "Level 1"
rep("""Start on Level 1 and go up floor by floor. On each floor, any room first. Three things to know:', '여기 있는 모든 것은 집 한 채예요: 다섯 층, 챕터마다 방 하나. 1층에서 시작해 한 층씩 올라가요.""",
    """Start on Ground · I and go up floor by floor. On each floor, any room first. Three things to know:', '여기 있는 모든 것은 집 한 채예요: 다섯 층, 챕터마다 방 하나. Ground · I에서 시작해 한 층씩 올라가요.""")
rep("""New to the piano? Start on Level 1. Already playing? Go straight to any room, or carry on with the button.', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요. 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 1층부터,""",
    """New to the piano? Start on Ground · I. Already playing? Go straight to any room, or carry on with the button.', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요. 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 Ground · I부터,""")
rep("""New to the piano? Start on Level 1. Already playing? Go straight to any room.', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요. 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 1층부터,""",
    """New to the piano? Start on Ground · I. Already playing? Go straight to any room.', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요. 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 Ground · I부터,""")
rep("""t(s.en[0] + ' of ' + PATH_STAGES.length, PATH_STAGES.length + '층 중 ' + s.ko[0])""",
    """t('Floor ' + (k + 1) + ' of ' + PATH_STAGES.length + ': ' + s.en[0], PATH_STAGES.length + '층 중 ' + (k + 1) + '층: ' + s.ko[0])""")
rep("""Every floor is a level and every room is a chapter, numbered 1 to""", """Every floor is a stage, from Ground up, and every room is a chapter, numbered 1 to""")

# the house's plaques and the books' small house. Cinzel's 1 reads as a capital I, so the digits are set in Playfair Display.
rep("""  return '<text x="' + pFix(x) + '" y="' + pFix(y) + '" font-size="' + (o.size || 11) + '" font-weight="' + (o.weight || 600) + '" fill="' + (o.fill || ST.N) + '" stroke="none" text-anchor="' + (o.anchor || 'start') + '" font-family="' + (o.font || ST_SANS) + '"' + (st ? ' style="' + st + '"' : '') + (o.op ? ' opacity="' + o.op + '"' : '') + '>' + penEsc(s) + '</text>';""",
    """  const body = o.digits ? String(s).split(/(\\d+)/).map((p, i) => i % 2 ? '<tspan style="font-family:' + o.digits + ';font-variant-numeric:lining-nums;letter-spacing:0.02em">' + penEsc(p) + '</tspan>' : penEsc(p)).join('') : penEsc(s);   // Build O: o.digits, a face for the digits
  return '<text x="' + pFix(x) + '" y="' + pFix(y) + '" font-size="' + (o.size || 11) + '" font-weight="' + (o.weight || 600) + '" fill="' + (o.fill || ST.N) + '" stroke="none" text-anchor="' + (o.anchor || 'start') + '" font-family="' + (o.font || ST_SANS) + '"' + (st ? ' style="' + st + '"' : '') + (o.op ? ' opacity="' + o.op + '"' : '') + '>' + body + '</text>';""")
rep("""    // the floor's plaque, centred in a moulded frame: just the floor -- "LEVEL 2", "2층" (her 2026-10-12: no floor names);
    // coral on your floor, green once every room on it is done
    const name = o.print || LANG !== 'ko' ? 'LEVEL ' + (k + 1) : (k + 1) + '층',""",
    """    // the floor's plaque, centred in a moulded frame: just the floor -- "GROUND · II", "P–1 · I" (her 2026-10-12: no floor names;
    // Build O: named by grade, in both languages); coral on your floor, green once every room on it is done
    const name = String((st.s && st.s.en[0]) || 'Level ' + (k + 1)).toUpperCase(),""")
rep("""      + stT((X0 + X1) / 2, yy + 18.4, name, { size: 11.5, weight: 700, font: TH_CAPS, ls: '0.09em', fill: here ? ST.C : st.st.every(v => v === 'done') ? ST.G : ST.N, anchor: 'middle' });""",
    """      + stT((X0 + X1) / 2, yy + 18.4, name, { size: 11.5, weight: 700, font: TH_CAPS, digits: "'Playfair Display',Georgia,serif", ls: '0.09em', fill: here ? ST.C : st.st.every(v => v === 'done') ? ST.G : ST.N, anchor: 'middle' });""")
rep("""    svg += stT(X0 + 2, y + 13, 'LEVEL ' + (x.i + 1), { size: 8.6, weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, ls: '0.06em' });""",
    """    const lbl = x.st.en[0].toUpperCase(); let lz = 8.6; while (lz > 6.6 && rdWidth(lbl, 700, lz, TH_CAPS) + lbl.length * lz * 0.06 > SC - 6) lz -= 0.2;   // Build O: the floor's name, as small as it must be to fit
    svg += stT(X0 + 2, y + 13, lbl, { size: +lz.toFixed(1), weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, digits: "'Playfair Display',Georgia,serif", ls: '0.06em' });""")

# 2. Every lesson on the Home carries its floor (decision 4): Ground, P–1, 2–3, 4, 5 or Home only, from the curriculum plan's
#    by-topic tables. The order stays; nothing locks. The mark is a little plaque in the house's capitals.
rep("""const HOME_AREA_LINE = {""", """// Build O (the curriculum plan, 2026-10-25): the floor of every Home lesson. 'G' Ground, 'P1' Preliminary and Grade 1,
// '23' Grades 2-3, '4', '5', 'home' the Home only. A lesson that runs across floors carries the first one it is taught on.
const HOME_FLOOR = (() => {
  const m = {}, set = (fl, ids) => ids.split(' ').forEach(id => { m[id] = fl; });
  set('G', 'kq-black kq-houses kq-names kq-octave kq-lines kq-climb kq-clefs kq-letters kq-fold kq-landmarks kq-read kq-write kq-size kq-range'
    + ' ac-half ac-whole ac-sharp ac-flat rb-beat rb-count rb-silent rb-words rb-finger rn-q rn-h rn-long rn-p rn-rest'
    + ' rt-bars rt-ts rt-strong rt-fill rt-tie kp-sit kp-arm kp-hand kp-fingers kp-walks kp-check kp-cpos kp-gpos kp-five');
  set('P1', 'kq-ledger kq-middlec ac-natural ac-bar ac-play ac-two ac-cmp iv-count iv-staff sc-shape sc-same sc-deg sc-wr sc-wl sc-both'
    + ' sc-chrom sc-min kf-what kf-minor kf-write ch-stack ch-staff ch-hands ch-mm ch-ear ch-tonic rp-beams rp-alone rp-dot rp-up rp-read rm-68 rm-sync');
  set('23', 'kq-alto kq-8va iv-half iv-tonic iv-minor iv-mh iv-ear sc-br sc-bl sc-penta kf-sharps kf-flats kf-msharp kf-mflat kf-trans'
    + ' ch-145 ch-seven ch-inv ch-cad md-home md-start sc-modes rm-semi rm-trip rm-cut rm-swing');
  set('4', 'iv-invert iv-tritone ch-da md-family md-ladder');
  set('5', 'ac-double sc-all kf-piece ch-7th md-parent md-keys');
  set('home', 'ch-ext ch-blues');
  return m;
})();
const HOME_FLOOR_NAME = { G: 'Ground', P1: 'P–1', '23': '2–3', '4': '4', '5': '5' };
function FloorMark({ id }) {   // sits at the start of the lesson's line, so the title keeps its width; Inter, whose 1 is never an I
  const fl = HOME_FLOOR[id]; if (!fl) return null;
  const box = { display:'inline-block', verticalAlign:'1px', marginRight:7, fontSize:10.5, fontWeight:800, lineHeight:1.25, whiteSpace:'nowrap', fontVariantNumeric:'lining-nums' };
  if (fl === 'home') return <span data-floor="home" style={{...box,color:'var(--navy-soft)',border:'1px dashed var(--navy-line)',borderRadius:3,padding:'1px 6px'}}>{t('Home only', '홈에만')}</span>;
  return <span data-floor={fl} title={t('Floor', '층') + ' ' + HOME_FLOOR_NAME[fl]} style={{...box,letterSpacing:'0.07em',color:'var(--navy)',border:'1px solid var(--navy)',boxShadow:'inset 0 0 0 1.5px var(--surface), inset 0 0 0 2.1px rgba(38,41,107,0.4)',borderRadius:2,padding:'2px 7px 1px'}}>{HOME_FLOOR_NAME[fl].toUpperCase()}</span>;
}
const HOME_AREA_LINE = {""")
rep("""  const step = (n, title, line, on, onClick) => (
    <button key={n} onClick={onClick} style={{...homeRow(on),minHeight:92}}>
      <span style={{flex:'none',width:40,height:40,borderRadius:20,background:'var(--navy)',color:'#fffefa',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:18}}>{n}</span>
      <span style={{flex:1,minWidth:0,display:'block'}}><span style={homeTitle}>{title}</span><span style={homeSub}>{line}</span></span>
      <HomeChev on/>""", """  const step = (n, title, line, on, onClick, fid) => (
    <button key={n} onClick={onClick} data-lesson={fid || undefined} style={{...homeRow(on),minHeight:92}}>
      <span style={{flex:'none',width:40,height:40,borderRadius:20,background:'var(--navy)',color:'#fffefa',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:18}}>{n}</span>
      <span style={{flex:1,minWidth:0,display:'block'}}><span style={homeTitle}>{title}</span><span style={homeSub}>{fid && <FloorMark id={fid}/>}{line}</span></span>
      <HomeChev on/>""")
rep("""{live.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}""",
    """{live.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' }), id) : null; })}""")
rep("""{(live.groups ? [] : (live.lessons || [])).map(id => { const tl = TOOLS.find(x => x.id === id); return tl ? step(++n, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}""",
    """{(live.groups ? [] : (live.lessons || [])).map(id => { const tl = TOOLS.find(x => x.id === id); return tl ? step(++n, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' }), id) : null; })}""")
rep("""{g.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(off + i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}""",
    """{g.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(off + i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' }), id) : null; })}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
