import sys, re
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
# virtual home concepts (the Toolbox keeps its one 'Scales and keys' group)
rep("// an area's name over its concepts: a larger Playfair line",
"""// Phase 513: on the Home, Scales and keys is two concepts: Key signatures and Scales (the Toolbox keeps one group)
const HOME_VIRTUAL = [{ id: 'p-keysig', area: 'pitch', en: 'Key signatures', ko: '조표' }, { id: 'p-scale', area: 'pitch', en: 'Scales', ko: '스케일' }]
  .map(v => ({ id: v.id, area: v.area, get name() { return LANG === 'ko' ? v.ko : v.en; } }));
const homeCats = (areaId) => TOOL_CATS.filter(c => c.area === areaId).flatMap(c => c.id === 'p-scales' ? HOME_VIRTUAL : [c]);
const homeCatById = (id) => TOOL_CATS.find(c => c.id === id) || HOME_VIRTUAL.find(c => c.id === id);
// an area's name over its concepts: a larger Playfair line""")
rep("hc: TOOL_CATS.some(c => c.id === p.get('concept')) ? p.get('concept') : null","hc: homeCatById(p.get('concept')) ? p.get('concept') : null")
rep("  const cat = TOOL_CATS.find(c => c.id === st.hc && c.area !== 'beside');","  const cat0 = homeCatById(st.hc), cat = cat0 && cat0.area !== 'beside' ? cat0 : undefined;")
rep("((TOOL_CATS.find(c => c.id === st.hc) || {}).name || t('Home', '홈'))","((homeCatById(st.hc) || {}).name || t('Home', '홈'))",2)
rep("        {TOOL_CATS.filter(c => c.area === area.id).map(c => { const on = !!HOME_LIVE[c.id]","        {homeCats(area.id).map(c => { const on = !!HOME_LIVE[c.id]")
# lines
rep("  'p-scales': ['Every key from one pattern', '패턴 하나로 모든 조'],",
    "  'p-scales': ['Every key from one pattern', '패턴 하나로 모든 조'],\n  'p-keysig': ['Which sharps and flats a key has', '조마다 붙는 샵과 플랫'],\n  'p-scale': ['The same pattern from every note', '어느 음에서나 같은 패턴'],")
# live blocks
i=s.index("const HOME_LIVE = {\n  'p-scales': {"); j=s.index("};\nconst HOME_AREA_LINE")
s=s[:i]+"""const HOME_LIVE = {
  'p-keysig': {
    lessons: ['kf-sharps', 'kf-flats', 'kf-major', 'kf-minor', 'kf-piece'], check: 'key-signatures', tools: [], more: [],
    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },
  'p-scale': {
    check: 'scales', tools: ['scale-finder'], more: ['csx-penta'],
    tryLine: ['Three steps: white keys, black keys, all twelve', '세 단계: 흰건반, 검은건반, 열두 조'],
    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },
"""+s[j:]
# concept page: no T/S card, rows counted, Drill
i=s.index("      <div style={{marginTop:14}}><HomeScaleRule/></div>\n"); j=s.index("  // level 1: the concepts of one area")
s=s[:i]+"""      <div style={{display:'flex',flexDirection:'column',gap:10,marginTop:14}}>
        {(() => { let n = 0; return <>
          {(live.lessons || []).map(id => { const tl = TOOLS.find(x => x.id === id); return tl ? step(++n, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}
          {live.tools && live.tools.length > 0 && step(++n, t('Try', '해 보기'), LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ hs: 'try' }))}
          {step(++n, t('Drill', '드릴'), LANG === 'ko' ? live.checkLine[1] : live.checkLine[0], false, () => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' }))}
        </>; })()}
      </div>
    </div>
  );
"""+s[j:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
