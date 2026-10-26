import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AF-2 (the Theory of Music check, after board call 5 changed to Theory of Music): two Home floor marks follow it.
# Theory of Music Grade 1 transposes a melody of up to four bars between the grade's keys, so 'Transposing' (kf-trans) moves from
# Grades 2-3 to Prelim - Grade 1 (its room, Key signatures, is already there). Theory of Music Grade 3 asks binary, ternary and
# rondo (AB, ABA, ABACA), so 'Binary, ternary, and rondo' and 'Rondo' move from Grade 5 to Grades 2-3.
rep("""kf-sharps kf-flats kf-msharp kf-mflat kf-trans""", """kf-sharps kf-flats kf-msharp kf-mflat""")
rep("""  set('5', 'form-shapes rondo-refrain');""", """  set('23', 'form-shapes rondo-refrain');   // Build AF-2: Theory of Music Grade 3 (was '5')
  set('P1', 'kf-trans');   // Build AF-2: Theory of Music Grade 1 transposition (was '23')""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
