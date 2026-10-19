import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("name: 'Semitones and accidentals', when:", "name: 'Accidentals', when:")
rep("'p-clock': ['반음과 임시표', '온음과 반음,", "'p-clock': ['임시표', '온음과 반음,")
rep("'p-clock': ['The smallest step, sharps and flats', '가장 작은 걸음, 샤프와 플랫'],", "'p-clock': ['Sharps, flats and naturals', '샵, 플랫, 내추럴'],")
rep("id: 'clock', label: 'Semitones and accidentals'", "id: 'clock', label: 'Accidentals'", 2)
rep("(LANG === 'ko' ? '반음과 임시표' : 'Semitones and accidentals')", "(LANG === 'ko' ? '임시표' : 'Accidentals')")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
