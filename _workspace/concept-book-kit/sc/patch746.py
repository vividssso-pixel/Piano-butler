import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CA (her 07:02, 'where are the make-toys?'): every room shows its own thing to make at the end of the room, under
# MAKE YOUR OWN, before the drill button. Until now a room's toy lived only in the Toolbox tab and at the end of the room's
# Home group (and, for five rooms, among the 'More in the toolbox' chips), so a child in a room never met it. The card finds
# the toys by their room (TOOLS ch), so the twenty toys there are now, and any made later, show up without a list to keep.
# Navy and coral only, no icon (the toolbox icons keep the illustration palette; this is a new student screen).

rep("""function LessonMore({ id }) {
  const own = { 'posture-hands': ['sit-check', 'arm-moves', 'hand-shape'], 'whole-staff': ['rhymes'] }[id] || [];
  const list = (CHAPTER_TOOL_ORDER[id] || []).filter(x => !/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv)-/.test(x) && !own.includes(x)).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean);
  if (!list.length) return null;
  return <div style={{margin:'14px 0 0',padding:'10px 12px',border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,background:'#fff'}}>""",
"""function LessonMake({ id }) {   // Build CA: the room's own thing to make, at the end of the room
  const toys = TOOLS.filter(tl => tl.ch === id && /^mk-/.test(tl.id) && !tl.hidden);
  if (!toys.length) return null;
  return <div data-make={id} style={{margin:'14px 0 0',padding:'10px 12px 6px',border:'1.5px solid rgba(38,41,107,0.28)',borderRadius:10,background:'#fff'}}>
    <div style={{fontSize:11.5,fontWeight:900,color:'#e4572e',letterSpacing:'0.1em',textTransform:'uppercase',margin:'0 0 2px'}}>{t('Make your own', '만들어 보기')}</div>
    {toys.map(tl => <a key={tl.id} href={'?tool=' + tl.id + (LANG === 'ko' ? '&lang=ko' : '')} style={{display:'flex',alignItems:'center',gap:10,textDecoration:'none',color:'var(--text)',minHeight:44,padding:'4px 0'}}>
      <span style={{flex:1,minWidth:0}}><span style={{display:'block',fontSize:16,fontWeight:900,color:'#26296b'}}>{sscSx(LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][0] : tl.title)}</span>
        <span style={{display:'block',fontSize:13,color:'#4a4d86',lineHeight:1.4}}>{LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][1] : tl.blurb}</span></span>
      <span aria-hidden="true" style={{flex:'0 0 auto',color:'#e4572e',fontSize:22,fontWeight:900}}>›</span></a>)}
  </div>;
}
function LessonMore({ id }) {
  const own = { 'posture-hands': ['sit-check', 'arm-moves', 'hand-shape'], 'whole-staff': ['rhymes'] }[id] || [];
  const list = (CHAPTER_TOOL_ORDER[id] || []).filter(x => !/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv|mk)-/.test(x) && !own.includes(x)).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean);
  if (!list.length) return <LessonMake id={id}/>;
  return <><LessonMake id={id}/><div style={{margin:'14px 0 0',padding:'10px 12px',border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,background:'#fff'}}>""")
rep("""{sscSx(LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][0] : tl.title)}</a>)}</div>
  </div>;
}""", """{sscSx(LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][0] : tl.title)}</a>)}</div>
  </div></>;
}""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
