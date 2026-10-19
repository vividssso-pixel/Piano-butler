import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# her 22:07: lesson 6 is named after what it teaches
rep("const title = t('Signs in a bar', '마디 안의 임시표');", "const title = t('Rules for sharps, flats and naturals', '샵, 플랫, 내추럴의 규칙');")
rep("[['ac-bar', 'Signs in a bar', '마디 안의 임시표',", "[['ac-bar', 'Rules for sharps, flats and naturals', '샵, 플랫, 내추럴의 규칙',")
rep("'How ♯, ♭ and ♮ work inside a bar.', '마디 안에서 ♯, ♭, ♮가 어떻게 적용되는지.'", "'How long each sign lasts, and which notes it reaches.', '각 임시표가 어디까지, 어떤 음에 적용되는지.'")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
