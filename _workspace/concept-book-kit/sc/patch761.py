import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build CP (her 15:17, 'split Grades 2 and 3 into a floor each too'): as Prelim and Grade 1 in Build CC, the rooms stay
# whole and go to the grade whose exam first needs most of them. Grade 2: Ear Training 2, Melody & Phrasing (the accented
# syllables are Theory of Music Grade 2), Scales further (the melodic minor and the chromatic scale from any note start at
# Grade 2). Grade 3: Ear Training 3, Intervals and chords further (degree names, inversions, cadences, SATB: Theory
# Grade 3), Rhythm further (semiquaver groups, the dotted quaver, duplets, 2/2, 3/2, 3/8, 9/8: Theory Grade 3).
# The Home's 'Grades 2–3' marks split by the grade that asks for each lesson (the Syllabus check 2–3 tab); the lessons
# neither grade asks for (alto clef, 8va, modes, pentatonic, pedal, the term lists that span both, Stories) keep 2–3.
rep("""  { ids: ['listen-23', 'listen-3', 'melody', 'scales-23', 'harmony-23', 'rhythm-23'], en: ['Grades 2–3', 'Your ears for Grade 2 and for Grade 3; how a tune is shaped; scales, intervals and chords, and rhythm a step further.'], ko: ['Grade 2–3', '2급 청음과 3급 청음, 선율의 모양, 그리고 스케일, 음정과 화음, 리듬을 한 걸음 더.'] },""",
"""  { ids: ['listen-23', 'melody', 'scales-23'], en: ['Grade 2', 'Your ears for Grade 2, how a tune is shaped, and scales a step further: black-key starts, the melodic minor, the chromatic scale from any note.'], ko: ['Grade 2', '2급 청음, 선율의 모양, 그리고 스케일 한 걸음 더: 검은건반에서 시작하기, 가락 단음계, 어느 음에서든 반음계.'] },   // Build CP: Grades 2 and 3 a floor each
  { ids: ['listen-3', 'harmony-23', 'rhythm-23'], en: ['Grade 3', 'Your ears for Grade 3, intervals and chords a step further, and rhythm a step further.'], ko: ['Grade 3', '3급 청음, 음정과 화음 한 걸음 더, 그리고 리듬 한 걸음 더.'] },""")
rep("""  Object.keys(m).forEach(id => { if (m[id] === 'P1') m[id] = g1.has(id) ? '1' : 'P'; });
  return m;""", """  Object.keys(m).forEach(id => { if (m[id] === 'P1') m[id] = g1.has(id) ? '1' : 'P'; });
  // Build CP (her 15:17): Grades 2 and 3 a floor each; each lesson marked by the grade that asks for it (Syllabus check 2–3)
  const to2 = new Set(('l2-dyad l2-sing l2-clap2 mk-hidden scf-thumb scf-meet scf-mel scf-mirror scf-chrom mk-melmin h3-iv mlx-map mlx-line mlx-motif mlx-words mlx-build'
    + ' iv-half iv-tonic iv-minor sc-br sc-bl kf-sharps kf-msharp rm-semi rm-trip rm-swing dc-ds-coda road-map same-or-new binary-ternary-spot').split(' '));
  const to3 = new Set(('l2-any l2-deg l2-clap lw-metre l3-sing mk-duel h3-deg h3-inv h3-satb h3-cad mk-choir r2-semi r2-dot r2-trip r2-minim r2-98 mk-split'
    + ' mlx-qa mlx-phrasing mlx-seq mlx-write phrase-marks question-answer melody-sequence iv-ear kf-flats kf-mflat ch-145 ch-inv ch-cad rm-cut form-shapes rondo-refrain').split(' '));
  Object.keys(m).forEach(id => { if (m[id] === '23') m[id] = to2.has(id) ? '2' : to3.has(id) ? '3' : '23'; });
  return m;""")
rep("""const HOME_FLOOR_NAME = { G: 'Beginner', P: 'Prelim', '1': 'Grade 1', '23': 'Grades 2–3',""", """const HOME_FLOOR_NAME = { G: 'Beginner', P: 'Prelim', '1': 'Grade 1', '2': 'Grade 2', '3': 'Grade 3', '23': 'Grades 2–3',""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
