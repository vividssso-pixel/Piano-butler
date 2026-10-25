import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: open(os.path.join(here, f), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
# Build AA (her 06:42 'match it to the syllabus'; the syllabus check, findings 3 and 4):
# 1. Listen and Sing to the letter of the Preliminary aural tests: the beat in two- or three-beat time at slow, moderate and quick
#    speeds (chord passages), carrying on when the music stops; higher or lower for two notes a third or more apart (no 'the same');
#    the sung phrase five or six one-beat notes, also played note by note. lsx.jsx / lsh.jsx replace the Build X versions.
rep(rd('lsx686.jsx'), rd('lsx.jsx'))
rep(rd('lsh686.jsx'), rd('lsh.jsx'))
# 2. no exam board's name where a student sees it: three Time signatures drill levels named them
for en, ko, en2, ko2 in [
    ('Whole-bar rests (ABRSM 1, AMEB 2)', '한 마디 쉼표 (ABRSM 1급, AMEB 2급)', 'Whole-bar rests', '한 마디 쉼표'),
    ('The bottom number: 2, 4 or 8 (ABRSM 2 to 4, AMEB 3)', '아래 숫자: 2, 4, 8 (ABRSM 2~4급, AMEB 3급)', 'The bottom number: 2, 4 or 8', '아래 숫자: 2, 4, 8'),
    ('Compound time: big beats (AMEB 2 to 4, ABRSM 3)', '겹박자: 큰 박 (AMEB 2~4급, ABRSM 3급)', 'Compound time: big beats', '겹박자: 큰 박'),
    ('Simple, compound or irregular? (ABRSM 3 to 5)', '홑박자, 겹박자, 혼합박자? (ABRSM 3~5급)', 'Simple, compound or irregular?', '홑박자, 겹박자, 혼합박자?')]:
    rep("label: '" + en + "'", "label: '" + en2 + "'")
    rep("'" + en + "': '" + ko + "'", "'" + en2 + "': '" + ko2 + "'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
