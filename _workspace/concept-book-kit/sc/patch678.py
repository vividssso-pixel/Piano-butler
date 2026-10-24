import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build P (her 2026-10-25 08:17, 'the names are hard: just show the grade plainly', then option 3: one floor per grade, and
# 'Ground or Beginner? recommend'): plain names everywhere -- Beginner, Prelim, Grade 1, Grade 2 ... Until a floor is
# rebuilt one grade per floor (the plan's floor-by-floor work), a storey that still mixes two grades says both, and the
# storeys carry their number so two storeys with the same name are told apart ('Floor 3 · Prelim – Grade 1').
rep("""  // Build O (2026-10-25): named by grade, as the curriculum plan's floors -- Ground (before Preliminary), P–1 (Preliminary and
  // Grade 1), 2–3; a band with two storeys is told apart by I and II. The Home's floor marks use the same names (HOME_FLOOR).""",
    """  // Build P (2026-10-25): named by grade in plain words -- Beginner (before Prelim), Prelim – Grade 1, Grades 2–3; storeys with
  // one name are told apart by their number (floorName). One grade per floor as each floor is rebuilt. The Home's marks: HOME_FLOOR.""")
rep("""en: ['Ground · I', 'Sitting""", """en: ['Beginner', 'Sitting""")
rep("""ko: ['Ground · I', '바른""", """ko: ['Beginner', '바른""")
rep("""en: ['Ground · II', 'Both""", """en: ['Beginner', 'Both""")
rep("""ko: ['Ground · II', '두 오선""", """ko: ['Beginner', '두 오선""")
rep("""en: ['P–1 · I', 'Speed""", """en: ['Prelim – Grade 1', 'Speed""")
rep("""ko: ['P–1 · I', '빠르기""", """ko: ['Prelim – Grade 1', '빠르기""")
rep("""en: ['P–1 · II', 'Key""", """en: ['Prelim – Grade 1', 'Key""")
rep("""ko: ['P–1 · II', '조표""", """ko: ['Prelim – Grade 1', '조표""")
rep("""en: ['2–3', 'How a tune""", """en: ['Grades 2–3', 'How a tune""")
rep("""ko: ['2–3', '선율의""", """ko: ['Grade 2–3', '선율의""")
rep("""const pathIds = () => PATH_STAGES.flatMap(pathStageIds);""",
    """const pathIds = () => PATH_STAGES.flatMap(pathStageIds);
const floorName = (k, caps) => { const s = PATH_STAGES[k], nm = caps ? s.en[0].toUpperCase() : t(s.en[0], s.ko[0]); return LANG === 'ko' && !caps ? (k + 1) + '층 · ' + nm : (caps ? 'FLOOR ' : 'Floor ') + (k + 1) + ' · ' + nm; };   // Build P""")

# the words
rep("""Start on Ground · I and go up floor by floor.""", """Start on floor 1, Beginner, and go up floor by floor.""")
rep("""Ground · I에서 시작해 한 층씩 올라가요.""", """1층 Beginner에서 시작해 한 층씩 올라가요.""")
rep("""New to the piano? Start on Ground · I.""", """New to the piano? Start on floor 1, Beginner.""", 2)
rep("""처음이라면 Ground · I부터,""", """처음이라면 1층 Beginner부터,""", 2)
rep("""t('That was the last room on ' + s.en[0] + '. Next floor: ' + PATH_STAGES[nk].en[0] + '.', s.ko[0] + '의 마지막 방이에요. 다음 층: ' + PATH_STAGES[nk].ko[0] + '.')""",
    """t('That was the last room on floor ' + (k + 1) + '. Next: ' + floorName(nk) + '.', (k + 1) + '층의 마지막 방이에요. 다음: ' + floorName(nk) + '.')""")
rep("""{t(st.en[0].toUpperCase(), st.ko[0])}</div>""", """{LANG === 'ko' ? floorName(st.n) : floorName(st.n, true)}</div>""")
rep("""Every floor is a stage, from Ground up, and every room""", """Every floor is a stage, from Beginner up through the grades, and every room""")

# the house's plaques: 'FLOOR 3 · PRELIM – GRADE 1' (Korean '3층 · PRELIM – GRADE 1')
rep("""    const name = String((st.s && st.s.en[0]) || 'Level ' + (k + 1)).toUpperCase(),""",
    """    const name = st.s ? (o.print || LANG !== 'ko' ? 'FLOOR ' : '') + (k + 1) + (o.print || LANG !== 'ko' ? '' : '층') + ' · ' + st.s.en[0].toUpperCase() : 'LEVEL ' + (k + 1),""")
# the books' small house: the name on one line if it fits, else two ('PRELIM –' / 'GRADE 1')
rep("""    const fh = FH + (x.ids.some(id => lines[id].length > 1) ? 11 : 0);
    svg += stL(X0, y + fh, X0 + HW, y + fh, 0.6);
    const lbl = x.st.en[0].toUpperCase(); let lz = 8.6; while (lz > 6.6 && rdWidth(lbl, 700, lz, TH_CAPS) + lbl.length * lz * 0.06 > SC - 6) lz -= 0.2;   // Build O: the floor's name, as small as it must be to fit
    svg += stT(X0 + 2, y + 13, lbl, { size: +lz.toFixed(1), weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, digits: "'Playfair Display',Georgia,serif", ls: '0.06em' });""",
    """    const lbl = x.st.en[0].toUpperCase(), fits = (txt, z) => rdWidth(txt, 700, z, TH_CAPS) + txt.length * z * 0.06 <= SC - 6;   // Build P: the floor's name
    let lz = 8.6; while (lz > 7.2 && !fits(lbl, lz)) lz -= 0.2;
    const ll = fits(lbl, lz) ? [lbl] : lbl.replace(' – ', ' –\\n').split('\\n');
    if (ll.length > 1) { lz = 8.2; while (lz > 6.6 && !ll.every(p => fits(p, lz))) lz -= 0.2; }
    const fh = Math.max(FH + (x.ids.some(id => lines[id].length > 1) ? 11 : 0), ll.length > 1 ? 24 : 0);
    svg += stL(X0, y + fh, X0 + HW, y + fh, 0.6);
    ll.forEach((p, i) => { svg += stT(X0 + 2, y + 12.6 + i * 9, p, { size: +lz.toFixed(1), weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, digits: "'Playfair Display',Georgia,serif", ls: '0.06em' }); });""")

# the Home's marks in the same plain words
rep("""const HOME_FLOOR_NAME = { G: 'Ground', P1: 'P–1', '23': '2–3', '4': '4', '5': '5' };""",
    """const HOME_FLOOR_NAME = { G: 'Beginner', P1: 'Prelim – Grade 1', '23': 'Grades 2–3', '4': 'Grade 4', '5': 'Grade 5' };   // Build P: plain words""")
rep("""title={t('Floor', '층') + ' ' + HOME_FLOOR_NAME[fl]}""", """title={HOME_FLOOR_NAME[fl]}""")
rep("""// Build O (the curriculum plan, 2026-10-25): the floor of every Home lesson. 'G' Ground, 'P1' Preliminary and Grade 1,
// '23' Grades 2-3, '4', '5', 'home' the Home only.""", """// Build O (the curriculum plan, 2026-10-25): the floor of every Home lesson. 'G' Beginner (before Prelim), 'P1' Prelim and
// Grade 1, '23' Grades 2-3, '4', '5', 'home' the Home only (Build P: shown in plain words, HOME_FLOOR_NAME).""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
