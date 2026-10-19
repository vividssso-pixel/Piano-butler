import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("""{prompt(t('Which notes does this key signature change?', '이 조표가 바꾸는 음은?'))}""","""{prompt(skgKeySign(q.k) === '#' ? t('Which notes get a sharp (♯) in this key?', '이 조에서 샵(♯)이 붙는 음은?') : t('Which notes get a flat (♭) in this key?', '이 조에서 플랫(♭)이 붙는 음은?'))}""")
rep("{ n: 2, label: 'Which notes change?', short: ['Signs that change', '바뀌는 음'],","{ n: 2, label: 'Which notes get a sharp or a flat?', short: ['Which notes?', '어떤 음?'],")
rep("  'The order: which is the Nth sharp or flat?'","  'The order: which is the Nth sharp or flat?'",0) if False else None
rep("'Sharp order: which is the Nth sharp?': '샵 순서: N번째 샵은?',","'Which notes get a sharp or a flat?': '샵이나 플랫이 붙는 음은?', 'Sharp order: which is the Nth sharp?': '샵 순서: N번째 샵은?',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
