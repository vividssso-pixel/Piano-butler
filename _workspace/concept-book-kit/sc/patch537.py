import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("['kf-piece', 'piece', 'Before a piece', '곡 치기 전에', 'Find the key, then play its scale.', '조를 찾고, 그 스케일을 쳐 봐요.']","['kf-piece', 'piece', 'Circle of fifths', '5도권', 'Every key in one circle, then the list.', '모든 조를 한 바퀴로, 그다음 목록으로.']")
rep("[t('Before a piece', '곡 치기 전에'), 6],","[t('Circle of fifths', '5도권'), 6],")
rep("<div style={head}>{t('Before you play the piece', '곡을 치기 전에')}</div>","<div style={head}>{t('Circle of fifths', '5도권')}</div>")
rep("const [view, setView] = useState('list');","const [view, setView] = useState('circle');")
rep("{[['list', t('List', '목록')], ['circle', t('Circle', '원')]].map(","{[['circle', t('Circle', '원')], ['list', t('List', '목록')]].map(")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
