import sys, io, re
md, hist = sys.argv[1], sys.argv[2]   # CLAUDE.md, CLAUDE-history.md
s = io.open(md, encoding='utf-8').read()
def R(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)
R("DS to DX and DZ to EB committed, waiting for her push.", "DS to DX, DZ to EB and EC committed, waiting for her push.")
R("DS to DX and DZ to EB (four commits).", "DS to DX, DZ to EB and EC (five commits).")
R("The dashboard's house has 67 rooms (td796). |", "The Reference (EC, call 41, her 14:32 and 14:36 'all at once'): the theory on seven tables, Beginner to Grade 8 (notes and rests, time signatures, keys and key signatures, scales, intervals, chords and cadences, signs and terms), every row a door into the room that teaches it; the patterns and semitones counted by the code, the words the rooms' own; ?tool=reference on the Home's Quick line in place of the Scales map (now inside it, under Scales), ?book=reference five A4 pages on the Books tab (sc/ref41.code.js). The dashboard's house has 67 rooms (td796). |")
i = s.index("1. Call 41, the Reference (her 14:32"); j = s.index("\n", i)
s = s[:i] + "1. The rest of call 39: the staff under the Grade 4 to 8 rooms' other keyboards (groups, chromatic). Then the Workbooks, fun first, floor by floor. Then a Pieces shelf (her 22:31) once she says which grade and what for." + s[j:]
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(h) if l.startswith('| 772 |')]
assert len(idx) == 1 and not any(l.startswith('| 773 |') for l in h)
h[idx[0] + 1:idx[0] + 1] = [
 "| 773 | 2026-10-31 | **The Reference (Build EC, call 41; her 14:32 with a theory book's reference pages, 'a space that takes in the whole: it becomes the map, easier to see', 14:36 'all at once').** Seven tables, Beginner to Grade 8, one line of words at most under each: (1) notes and rests: eight values with their beats (crotchet = 1) and the rests the rooms teach, the triplet and the duplet; (2) time signatures: the bottom number (2 minim, 4 crotchet, 8 quaver), six simple (2/4, 3/4, 4/4 with C, 2/2 with cut C, 3/2, 3/8) and four compound (6/8, 9/8, 12/8, 6/4); (3) keys: the order of sharps and flats with their letters under each sign, the two rules, fifteen majors with their relative minors and signatures, the enharmonic pairs; (4) scales: seven forms with their tones and semitones counted from their notes, then the Scales map, floor by floor (closed until tapped); (5) intervals: each number with its qualities' semitones, six rules; (6) chords: the triad on every degree of C major on the staff, the degree names, eight chord facts, the four cadences in Chords and Cadences, Grade 4's own words; (7) signs and terms: the dictionary's 79 words, floor by floor, each opening its card. Every row's chip names the floor where the house first teaches it and opens that room (from the rooms' steps and key lists: SCF, SCF_CM, S4_KEYS..., K4_IDS, MM_KEYS, H3_MIN). A separate check of every fact found no errors; its points taken: the bottom number's Korean head is 세는 단위 (8 is not the beat in 6/8), 마침표(.) and 쉼표(,) so a comma is not read as a rest, 'from two flats' (one flat: F major), '(the harmonic minor)' on the minor key's intervals, 기본 위치 as the rooms say, the diminished 7th 'of a key', and the Korean particles after a sharp. On the Home's Quick line in place of the Scales map; on paper ?book=reference, five A4 pages (page 1 in two columns), a button on the Books tab. Tests sc/ec805.js; sc/dr794.js opens the Scales map from the Reference now. |",
]
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h))
print('CLAUDE.md and CLAUDE-history.md updated (row 773)')
