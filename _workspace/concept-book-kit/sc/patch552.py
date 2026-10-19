import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# no sentence starts with the article 'A': it reads like the note name A (her 15:25 note)
rep("all: ['A half step (semitone) is the very next key.', '반음(semitone)은 바로 옆 건반이에요.'],", "all: ['Half step (semitone) = the very next key.', '반음(semitone)은 바로 옆 건반이에요.'],")
rep("all: ['A whole step (tone) is two half steps: skip one key.', '온음(tone)은 반음 두 개예요: 건반 하나를 건너뛰어요.'],", "all: ['Whole step (tone) = two half steps: skip one key.', '온음(tone)은 반음 두 개예요: 건반 하나를 건너뛰어요.'],")
rep("en: 'From C, skip the black key: D. A whole step.',", "en: 'From C, skip the black key to D: a whole step.',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
