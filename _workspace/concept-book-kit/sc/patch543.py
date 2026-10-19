import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("{concept.levels.map(l => (\n                  <React.Fragment key={l.n}>","{concept.levels.map((l, li) => (\n                  <React.Fragment key={l.n}>")
rep("title={lvName(l.label)}>{l.short ? t(l.short[0], l.short[1]) : <>{t('Level ', '레벨 ')}{l.n}</>}</button>","title={lvName(l.label)}>{l.short ? <>{!l.extra && <span style={{opacity:0.55,marginRight:6,fontWeight:900}}>{concept.levels.slice(0, li + 1).filter(z => z.short && !z.extra).length}</span>}{t(l.short[0], l.short[1])}</> : <>{t('Level ', '레벨 ')}{l.n}</>}</button>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
