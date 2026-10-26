import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AF-1 (decision board call 5, changed 26 Oct 10:23: theory follows Theory of Music, the exam Sohyun's students sit; Music
# Craft is reference only). Build AF-0 moved three Home lessons from Grade 4 to Grades 2-3 on Music Craft Grade 3. In Theory of Music
# the inversion of intervals is Grade 4 and chromatic intervals Grade 5, and diminished and augmented triads are not a topic of their
# own, so the three go back to the Grade 4 mark (the exact floor is set when floors 4 and 5 are built, board call 9).
# 'Question or answer phrase?' and 'Sequences' stay on Grades 2-3 (Theory of Music Grade 3: sequence, phrasing in melody writing).
rep("""  set('4', 'md-family md-ladder');
  set('23', 'iv-invert iv-tritone ch-da');   // Build AF-0: Music Craft Grade 3 (was '4')""",
    """  set('4', 'iv-invert iv-tritone ch-da md-family md-ladder');   // Build AF-1: back to '4' (Theory of Music: inversions Grade 4, chromatic intervals Grade 5)""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
