import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# lesson 4: the flat, the mirror of the sharp (C flat = B, F flat = E included)
rep("const AC_SIGN = {\n", """const AC_SIGN = {
  flat: { dir: -1, sym: '♭', title: ['The flat ♭', '플랫 ♭'],
    all: ['Flat (♭) = one half step down, to the very next key on the left: black or white.', '플랫(♭) = 반음 아래, 바로 왼쪽 건반으로: 검은건반일 수도 흰건반일 수도 있어요.'],
    order: [2, 0, 4, 5, 7, 9, 11], btn: ['♭ Flat →', '♭ 플랫 →'], word: ['flat', '플랫'], above: ['below', '아래'] },
""")
rep("'반음 위로: 바로 오른쪽 건반.']]", "'반음 위로: 바로 오른쪽 건반.'],\n ['ac-flat', 'flat', 'The flat ♭', '플랫 ♭', 'One half step down: the very next key to the left.', '반음 아래로: 바로 왼쪽 건반.']]")
rep("lessons: ['ac-half', 'ac-whole', 'ac-sharp', 'cl-flat',", "lessons: ['ac-half', 'ac-whole', 'ac-sharp', 'ac-flat',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
