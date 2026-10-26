import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AH (board call 15, her 2026-10-26 14:31: "작곡가 스타일 방, 피아노이야기 이런건 다 따로 음악이야기 별도 방에다가"):
# The piano's story (from floor 2), Composers and Styles (from the Grades 2-3 floor) leave the grade floors for their own
# storey, Stories of music, between the top floor and the attic: rooms to visit any time, like the attic. It has the theatre
# wallpaper. The Home's Stories of music door already holds the same three rooms. Chapter numbers follow the new order.
rep("""'scales', 'scale-play', 'accidentals', 'piano-story'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, 6/8, ledger lines, scales and how to play them, accidentals, and the piano’s own story.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 6/8박자, 덧줄, 스케일과 스케일 치기, 임시표, 그리고 피아노 이야기.'] },""",
    """'scales', 'scale-play', 'accidentals'], en: ['Prelim – Grade 1', 'Speed, quavers and dots, 6/8, ledger lines, scales and how to play them, and accidentals.'], ko: ['Prelim – Grade 1', '빠르기, 8분음표와 점, 6/8박자, 덧줄, 스케일과 스케일 치기, 그리고 임시표.'] },   // Build AH: the piano's story moves to Stories of music""")
rep("""  { ids: ['melody', 'composers', 'styles', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, music through time, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 시대별 음악, 그리고 더 많은 음계.'] },""",
    """  { ids: ['melody', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 그리고 더 많은 음계.'] },   // Build AH: Composers and Styles move to Stories of music
  { ids: ['piano-story', 'composers', 'styles'], stories: true, th: { wp: 'drape', fl: 'boards', lamp: 'candelabrum' }, en: ['Stories of music', 'Rooms to visit any time: the piano’s own story, composers through time, and styles.'], ko: ['음악 이야기', '언제든 들어가는 방: 피아노 이야기, 시대별 작곡가, 스타일.'] },   // Build AH: its own storey, not a grade floor""")
# the storeys that are not grade floors: the attic and Stories of music
rep("""const houseFloorsN = () => PATH_STAGES.filter(x => !x.attic).length;""",
    """const stageExtra = (s) => !!(s && (s.attic || s.stories));   // Build AH: not a grade floor (the attic, Stories of music)
const houseFloorsN = () => PATH_STAGES.filter(x => !stageExtra(x)).length;""")
rep("""  return PATH_STAGES.some(x => x.attic) ? w + (ko ? '과 다락방' : ' and an attic') : w; };""",
    """  const sm = PATH_STAGES.some(x => x.stories), at = PATH_STAGES.some(x => x.attic);   // Build AH: four floors, a Stories of music room and an attic
  return w + (sm ? (ko ? (at ? ', 음악 이야기 방' : '과 음악 이야기 방') : (at ? ', a Stories of music room' : ' and a Stories of music room')) : '') + (at ? (ko ? '과 다락방' : ' and an attic') : ''); };""")
rep("""const floorName = (k, caps) => { if (PATH_STAGES[k].attic) return caps ? 'ATTIC' : t('The attic', '다락방');""",
    """const floorName = (k, caps) => { if (PATH_STAGES[k].attic) return caps ? 'ATTIC' : t('The attic', '다락방'); if (PATH_STAGES[k].stories) return caps ? 'STORIES OF MUSIC' : t('Stories of music', '음악 이야기');""")
# Next on your path: the last room of a storey that is not a floor, and a room in Stories of music
rep("""{nk !== k ? t('That was the last room on floor ' + (k + 1) + '. Next: ' + floorName(nk) + '.', (k + 1) + '층의 마지막 방이에요. 다음: ' + floorName(nk) + '.') : s.attic ?""",
    """{nk !== k ? (stageExtra(s) ? t('That was the last room in ' + floorName(k) + '. Next: ' + floorName(nk) + '.', floorName(k) + '의 마지막 방이에요. 다음: ' + floorName(nk) + '.') : t('That was the last room on floor ' + (k + 1) + '. Next: ' + floorName(nk) + '.', (k + 1) + '층의 마지막 방이에요. 다음: ' + floorName(nk) + '.')) : s.stories ? t('Stories of music: rooms to visit any time', '음악 이야기: 언제든 들어가는 방') : s.attic ?""")
# the townhouse: the storey's plaque and its own wallpaper
rep("""const name = st.s && st.s.attic ? (o.print || LANG !== 'ko' ? 'ATTIC' : '다락방') : st.s ?""",
    """const name = st.s && st.s.attic ? (o.print || LANG !== 'ko' ? 'ATTIC' : '다락방') : st.s && st.s.stories ? (o.print || LANG !== 'ko' ? 'STORIES OF MUSIC' : '음악 이야기') : st.s ?""")
rep("""const st = view.stages[k], fs = TH_FLOOR[k],""", """const st = view.stages[k], fs = (st.s && st.s.th) || TH_FLOOR[k],""")
# the Lesson Book's small house: a long storey name without ' – ' ('STORIES OF MUSIC') breaks before its last word
rep("""const ll = fits(lbl, lz) ? [lbl] : lbl.replace(' – ', ' –\\n').split('\\n');""",
    """const ll = fits(lbl, lz) ? [lbl] : (lbl.includes(' – ') ? lbl.replace(' – ', ' –\\n') : lbl.replace(/ (\\S+)$/, '\\n$1')).split('\\n');""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
