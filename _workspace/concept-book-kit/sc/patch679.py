import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build Q (her 2026-10-25 15:02, 'before Prelim, one floor is better, right?'): the two Beginner storeys become one floor of
# twelve rooms, in the same order (the first-tutor rooms, then the bridge to Prelim). The house has four floors; a floor of more
# than six rooms takes two rows on big screens and in the books' small house. The words that said 'five floors' count them.
rep("""const PATH_STAGES = [   // Phase 436: five floors of the house, in the plan's order; inside a floor any room first.""",
    """const PATH_STAGES = [   // Phase 436: the floors of the house, in the plan's order; inside a floor any room first. Build Q: Beginner is one floor.""")
rep("""  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff'], en: ['Beginner', 'Sitting well, the keys and their letters, a steady beat, the first note values and the staff.'], ko: ['Beginner', '바른 자세, 건반과 글자, 일정한 박, 처음 음표 길이, 그리고 오선.'] },
  { ids: ['whole-staff', 'time-signatures', 'reading-steps', 'dynamics', 'tones', 'pitch-range'], en: ['Beginner', 'Both staves, bar lines and time signatures, the first tunes, loud and soft, half and whole steps, high and low.'], ko: ['Beginner', '두 오선, 세로줄과 박자표, 첫 선율, 셈여림, 반음과 온음, 높고 낮은 소리.'] },""",
    """  { ids: ['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff', 'whole-staff', 'time-signatures', 'reading-steps', 'dynamics', 'tones', 'pitch-range'], en: ['Beginner', 'Sitting well, the keys and their letters, a steady beat, note values, the staff and time signatures, the first tunes, loud and soft, half and whole steps, high and low.'], ko: ['Beginner', '바른 자세, 건반과 글자, 일정한 박, 음표 길이, 오선과 박자표, 첫 선율, 셈여림, 반음과 온음, 높고 낮은 소리.'] },""")
rep("""const floorName = (k, caps) =>""", """const houseFloors = (ko) => (ko ? ['', '한 층', '두 층', '세 층', '네 층', '다섯 층', '여섯 층', '일곱 층', '여덟 층', '아홉 층', '열 층'] : ['', 'one floor', 'two floors', 'three floors', 'four floors', 'five floors', 'six floors', 'seven floors', 'eight floors', 'nine floors', 'ten floors'])[PATH_STAGES.length] || PATH_STAGES.length + (ko ? '층' : ' floors');   // Build Q
const floorName = (k, caps) =>""")
rep("""'Everything here is one house: five floors,""", """'Everything here is one house: ' + houseFloors() + ',""")
rep("""'여기 있는 모든 것은 집 한 채예요: 다섯 층,""", """'여기 있는 모든 것은 집 한 채예요: ' + houseFloors(true) + ',""")
rep("""'The Piano Butler’s house: five floors, a room for each chapter.""", """'The Piano Butler’s house: ' + houseFloors() + ', a room for each chapter.""", 2)
rep("""'피아노 버틀러의 집: 다섯 층, 챕터마다""", """'피아노 버틀러의 집: ' + houseFloors(true) + ', 챕터마다""", 3)
rep("""'The Piano Butler’s house: five floors, one room for each chapter'""", """'The Piano Butler’s house: ' + houseFloors() + ', one room for each chapter'""")
rep(""">five floors, a room for each chapter, the same order as the app<""", """>{houseFloors()}, a room for each chapter, the same order as the app<""")

# the house: on big screens and paper a floor of more than six rooms takes two rows
rep("""  const cols = (n) => o.wide ? n : n <= 3 ? n : n === 4 ? 2 : 3;""",
    """  const cols = (n) => o.wide ? (n <= 6 ? n : Math.ceil(n / 2)) : n <= 3 ? n : n === 4 ? 2 : 3;   // Build Q: twelve rooms, two rows of six""")
# the books' small house: rows of six; the floor's name on its first row, a faint line between its rows
rep("""  let y = TOP, svg = '';
  stages.forEach(x => {
    const has = x.ids.includes(current), rw = (HW - SC) / 6,""",
    """  let y = TOP, svg = '';
  const rows = []; stages.forEach(x => { for (let k = 0; k < x.ids.length; k += 6) rows.push({ st: x.st, i: x.i, ids: x.ids.slice(k, k + 6), all: x.ids, first: k === 0, last: k + 6 >= x.ids.length }); });   // Build Q
  rows.forEach(x => {
    const has = x.all.includes(current), rw = (HW - SC) / 6,""")
rep("""    const fh = Math.max(FH + (x.ids.some(id => lines[id].length > 1) ? 11 : 0), ll.length > 1 ? 24 : 0);
    svg += stL(X0, y + fh, X0 + HW, y + fh, 0.6);
    ll.forEach((p, i) => {""", """    const fh = Math.max(FH + (x.ids.some(id => lines[id].length > 1) ? 11 : 0), x.first && ll.length > 1 ? 24 : 0);
    svg += x.last ? stL(X0, y + fh, X0 + HW, y + fh, 0.6) : '<g opacity="0.35">' + stL(X0 + SC, y + fh, X0 + HW, y + fh, 0.5) + '</g>';
    if (x.first) ll.forEach((p, i) => {""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
