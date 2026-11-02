p='drills.src.html'; s=open(p).read()
assert 'OPT_KINDS' not in s
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
i=s.index("Object.assign(SCALES_8_DRILL, {"); j=s.index("\n",i)+1
s=s[:j]+'''// m51 (her 2 Nov: 'the grand scale and the like are one exam board's; keep it general, make them optional'): those steps are marked Optional.
const OPT_KINDS = ['grand', 'ls', 'poly', 'held'];
[S6_LEVELS, S7_LEVELS, S8_LEVELS].forEach(L => L.forEach(l => { if (!OPT_KINDS.includes(l.kind) || l.opt) return; const ko = LEVEL_KO[l.label]; l.opt = true; l.label = 'Optional: ' + l.label.replace(/^Grade 8 /, '').replace(/^The /, 'the '); if (ko) LEVEL_KO[l.label] = '선택: ' + ko; }));
'''+s[j:]
rep("grand: t('Grand scale', '그랜드 스케일'), ls: t('Legato and staccato', '레가토와 스타카토'), poly: t('Three against two', '3 대 2'),",
    "grand: t('Grand scale (optional)', '그랜드 스케일 (선택)'), ls: t('Legato and staccato (optional)', '레가토와 스타카토 (선택)'), poly: t('Three against two (optional)', '3 대 2 (선택)'),")
rep("[t('Two against three', '2 대 3'), ['E major'], '']", "[t('Two against three (optional)', '2 대 3 (선택)'), ['E major'], '']")
rep("[t('Two voices, the Lydian mode', '두 성부, 리디아 선법'), [], '']", "[t('Two voices (optional); the Lydian mode', '두 성부 (선택); 리디아 선법'), [], '']")
open(p,'w').write(s); print('ok')
