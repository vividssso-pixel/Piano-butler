import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# Build D (her calls 2026-10-24 00:56: every old Pitch topic moves onto the Home; order: Pitch gaps, Rhythm, Technique,
# Touch and tempo, Pieces, Beside; students see the Home once every area is moved). This build: Keys and staff gaps.

# ── re-splice the three lesson files (kq, iv, ch) at their markers
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'iv.jsx', encoding='utf-8').read() + "\n" + open(SC + 'ch.jsx', encoding='utf-8').read() + "\n" + open(SC + 'pg.jsx', encoding='utf-8').read() + s[j:]

# ── Keys and staff on the Home: octaves, the alto clef, writing notes
rep("lessons: ['kq-black', 'kq-houses', 'kq-names'], check: 'first-steps' },", "lessons: ['kq-black', 'kq-houses', 'kq-names', 'kq-octave'], check: 'first-steps' },")
rep("lessons: ['kq-lines', 'kq-climb', 'kq-clefs'], check: 'staff' },", "lessons: ['kq-lines', 'kq-climb', 'kq-clefs', 'kq-alto'], check: 'staff' },")
rep("lessons: ['kq-letters', 'kq-landmarks', 'kq-read'], check: 'whole-staff' },", "lessons: ['kq-letters', 'kq-landmarks', 'kq-read', 'kq-write'], check: 'whole-staff' },")

# ── Chords on the Home: the seven chords and cadences in 'Chords in a key'; 9th/11th/13th and the 12-bar blues in a new group (no Questions drill yet)
rep("    { id: 'ch-key', en: 'Chords in a key', ko: '조 안의 화음', lessons: ['ch-tonic', 'ch-145', 'ch-inv'], check: 'chords', level: 7 },",
    "    { id: 'ch-key', en: 'Chords in a key', ko: '조 안의 화음', lessons: ['ch-tonic', 'ch-145', 'ch-seven', 'ch-inv', 'ch-cad'], check: 'chords', level: 7 },\n    { id: 'ch-more', en: 'More chords', ko: '더 많은 화음', lessons: ['ch-ext', 'ch-blues'] },")
# ── Key signatures and Scales: writing a key signature, transposing, the pentatonic scale
rep("lessons: ['kf-what', 'kf-sharps', 'kf-flats', 'kf-msharp', 'kf-mflat', 'kf-minor', 'kf-piece'], check: 'key-signatures',", "lessons: ['kf-what', 'kf-sharps', 'kf-flats', 'kf-msharp', 'kf-mflat', 'kf-minor', 'kf-piece', 'kf-write', 'kf-trans'], check: 'key-signatures',")
rep("lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'sc-all', 'sc-chrom', 'sc-min'], check: 'scales',", "lessons: ['sc-shape', 'sc-same', 'sc-deg', 'sc-wr', 'sc-wl', 'sc-br', 'sc-bl', 'sc-both', 'sc-all', 'sc-chrom', 'sc-min', 'sc-penta'], check: 'scales',")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
