p='drills.src.html'; s=open(p).read()
if 'const lvlName' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)
# the mapper, before floorName
rep("const floorName = (k, caps) => {",
    "// m36 (her 1 Nov: 'not AMEB's names: Level 1 is a floor and a level-up'): Beginner -> Level 0, Prelim -> Level ½, Grade n -> Level n.\n"
    "// The exam's own name stays for the teacher as '≈ Grade 3' (lvlExam).\n"
    "const lvlName = (x) => { const v = String(x || ''); return v === 'Beginner' ? 'Level 0' : v === 'Prelim' ? 'Level ½' : v.replace(/^Grade (\\d)$/, 'Level $1'); };\n"
    "const lvlExam = (x) => '≈ ' + String(x || '');\n"
    "const floorName = (k, caps) => {")
rep("return caps ? s.en[0].toUpperCase() : t(s.en[0], s.ko[0]); };", "return caps ? lvlName(s.en[0]).toUpperCase() : lvlName(t(s.en[0], s.ko[0])); };")
rep("const refFloor = (room) => { const s = STAGES.find(x => x.ids.includes(room)); return s && s.en ? s.en[0] : ''; };",
    "const refFloor = (room) => { const s = STAGES.find(x => x.ids.includes(room)); return s && s.en ? lvlName(s.en[0]) : ''; };")
rep("  const lab = g || (REF_STORY[room] ? t(REF_STORY[room][0], REF_STORY[room][1]) : refFloor(room));",
    "  const lab = lvlName(g) || (REF_STORY[room] ? t(REF_STORY[room][0], REF_STORY[room][1]) : refFloor(room));")
rep("<b style={{fontSize:15.5,color:'var(--navy)'}}>{t(s.en[0], s.ko[0])}</b>", "<b style={{fontSize:15.5,color:'var(--navy)'}}>{lvlName(t(s.en[0], s.ko[0]))}</b>")
rep("const num = String(i + 1).padStart(2, '0'), name = t(x.s.en[0], x.s.ko[0]);", "const num = String(i + 1).padStart(2, '0'), name = lvlName(t(x.s.en[0], x.s.ko[0]));")
rep("const floors = STAGES.map(s => ({ name: s.en ? s.en[0] : '',", "const floors = STAGES.map(s => ({ name: s.en ? lvlName(s.en[0]) : '',")
# the house plaque (screen and paper alike: the floor's name is ours)
i = s.index("    const name = st.s && st.s.attic ?")
j = s.index("\n", i)
line = s[i:j]
assert "st.s.en[0].toUpperCase()" in line
line = line.replace("st.s.en[0].toUpperCase()", "lvlName(st.s.en[0]).toUpperCase()", 1)
s = s[:i] + line + s[j:]
# the teacher's '≈ Grade 3' on each floor band
rep("    if (shut) {   // a closed floor: its plaque, how many rooms are done, and a tap opens it",
    "    if (!o.print && UI_TEACHER && st.s && !st.s.stories && !st.s.attic) body += stT(L1 - (shut ? (cmp ? 46 : 56) : 8), yy + (cmp ? 15 : 18), lvlExam(st.s.en[0]), { size: cmp ? 8 : 9.5, weight: 700, font: TH_SANS, fill: '#9a9cc0', anchor: 'end' });   // m36\n"
    "    if (shut) {   // a closed floor: its plaque, how many rooms are done, and a tap opens it")
open(p,'w').write(s); print('ok')
