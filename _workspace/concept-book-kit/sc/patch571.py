import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# her 22:16: leftovers are not shown on the Accidentals Home at all (the tools stay in the code until she decides)
rep("'ac-cmp', 'chromatic', 'accidental-bar', 'sac-bar', 'sac-line', 'sac-tune', 'accidental-cards', 'sharp-flat'], check: 'clock'", "'ac-cmp'], check: 'clock'") if "'ac-cmp', 'chromatic', 'accidental-bar'" in s else rep("'ac-cmp', 'chromatic', 'sac-bar', 'sac-line', 'sac-tune', 'accidental-cards', 'sharp-flat'], check: 'clock'", "'ac-cmp'], check: 'clock'")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
