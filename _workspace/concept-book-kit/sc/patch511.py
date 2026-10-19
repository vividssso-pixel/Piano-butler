import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
rep("        {step(1, t('Learn', '배우기'), LANG === 'ko' ? live.learnLine[1] : live.learnLine[0], false, () => go(live.lessons ? { hs: 'learn' } : { view: 'tools', tool: live.learn, ret: 'home' }))}\n        {step(2, t('Try', '해 보기'), LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ hs: 'try' }))}\n        {step(3, t('Check', '확인하기'),",
"""        {live.lessons ? live.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })
          : step(1, t('Learn', '배우기'), LANG === 'ko' ? live.learnLine[1] : live.learnLine[0], false, () => go({ view: 'tools', tool: live.learn, ret: 'home' }))}
        {step(live.lessons ? live.lessons.length + 1 : 2, t('Try', '해 보기'), LANG === 'ko' ? live.tryLine[1] : live.tryLine[0], true, () => go({ hs: 'try' }))}
        {step(live.lessons ? live.lessons.length + 2 : 3, t('Check', '확인하기'),""")
rep("const homeBack = '← ' + (st.hs === 'try' ? t('Try', '해 보기') : st.hs === 'learn' ? t('Learn', '배우기') :","const homeBack = '← ' + (st.hs === 'try' ? t('Try', '해 보기') :")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
