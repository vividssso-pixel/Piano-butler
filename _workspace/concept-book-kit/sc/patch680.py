import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build R (her 2026-10-25 15:45, 'balance it, fill it in'; the curriculum plan's step 3, decision 5 on its recommendation):
# Touch and expression and Pieces get their Home groups, in the plan's order (whole to detail), from the tools already there.
# Each group's questions are its chapter's. Duplicate pairs: one lesson each (sdy-tie over tie-slur, ssk-step over step-skip,
# stm-metro over the metronome dial, which stays as the area's tool to try). Every new lesson carries its floor.
rep("""  'p-modes': {
    lessons: ['md-home', 'md-start', 'sc-modes', 'md-family', 'md-ladder', 'md-parent', 'md-keys'], tools: [], more: [],
  },
};""", """  'p-modes': {
    lessons: ['md-home', 'md-start', 'sc-modes', 'md-family', 'md-ladder', 'md-parent', 'md-keys'], tools: [], more: [],
  },
  // Build R: Touch and expression, and Pieces
  't-touch': { lessons: [], groups: [
    { id: 't-dyn', en: 'Dynamics', ko: '셈여림', lessons: ['sdy-pf', 'sdy-ladder', 'sdy-hair', 'hairpin', 'tmx-vol', 'dyn-order'], check: 'dynamics' },
    { id: 't-art', en: 'Touch', ko: '터치', lessons: ['sdy-touch', 'sdy-tie', 'tmx-touch', 'touch-lengths', 'touch-ear'], check: 'dynamics', level: 4 },
    { id: 't-pedal', en: 'The pedals', ko: '페달', lessons: ['sps-pedals', 'pedal'] },
    { id: 't-orn', en: 'Ornaments', ko: '꾸밈음', lessons: ['ornaments', 'grace-write'] },
  ] },
  't-tempo': { lessons: [], groups: [
    { id: 't-speed', en: 'Tempo', ko: '빠르기', lessons: ['stm-sf', 'stm-words', 'stm-read', 'stm-metro', 'stm-steady', 'tmx-speed', 'tmx-change', 'speed-change'], check: 'tempo' },
    { id: 't-terms', en: 'Terms', ko: '용어', lessons: ['tmx-build', 'tmx-map', 'term-mixer', 'term-cards', 'term-match', 'term-sort'], check: 'terms' },
    { id: 't-feel', en: 'More about tempo', ko: '빠르기 더 알기', lessons: ['tempo-walk', 'tempo-race', 'tap-tempo', 'same-tune-tempo'] },
  ], tools: ['metronome'], tryLine: ['Any time signature, triplets and semiquavers, tap tempo.', '어떤 박자든, 셋잇단음표와 16분음표, 탭 템포까지.'] },
  'c-reading': { lessons: ['ssk-step', 'ssk-shape', 'ssk-read', 'mini-tune', 'tune-anatomy', 'hear-find', 'echo', 'sight-reading', 'draw-tune'], check: 'reading-steps', tools: [], more: [] },
  'c-map': { lessons: [], groups: [
    { id: 'c-signs', en: 'Signs and road maps', ko: '기호와 길찾기', lessons: ['sgn-rep', 'sgn-volta', 'sgn-dc', 'sgn-ds', 'sgn-pause', 'dc-ds-coda', 'road-map'], check: 'signs' },
    { id: 'c-form', en: 'Form', ko: '형식', lessons: ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'same-or-new', 'binary-ternary-spot', 'form-shapes', 'rondo-refrain', 'form-builder'], check: 'form' },
    { id: 'c-melody', en: 'Melody', ko: '선율', lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-build', 'phrase-marks', 'question-answer', 'melody-sequence', 'complete-melody'], check: 'melody' },
  ] },
};""")
# their floors, from the plan's by-topic tables
rep("""  set('home', 'ch-ext ch-blues');
  return m;""", """  set('home', 'ch-ext ch-blues');
  // Build R: Touch and expression, Pieces
  set('G', 'sdy-pf sdy-ladder sdy-hair hairpin sdy-touch sdy-tie ssk-step ssk-shape ssk-read mini-tune tune-anatomy');
  set('P1', 'tmx-vol dyn-order tmx-touch touch-lengths touch-ear sps-pedals stm-sf stm-words stm-read stm-metro stm-steady tmx-speed tmx-change speed-change'
    + ' tmx-build tmx-map hear-find echo sight-reading sgn-rep sgn-volta sgn-dc sgn-ds sgn-pause fmx-map fmx-phrase fmx-letters fmx-binary fmx-ternary fmx-find fmx-build');
  set('23', 'pedal term-mixer term-cards term-match term-sort dc-ds-coda road-map same-or-new binary-ternary-spot'
    + ' mlx-map mlx-line mlx-phrasing mlx-qa mlx-motif mlx-seq mlx-build phrase-marks');
  set('4', 'ornaments grace-write question-answer melody-sequence');
  set('5', 'form-shapes rondo-refrain');
  set('home', 'tempo-walk tempo-race tap-tempo same-tune-tempo draw-tune form-builder complete-melody');
  return m;""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
