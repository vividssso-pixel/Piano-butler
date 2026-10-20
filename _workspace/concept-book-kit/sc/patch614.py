import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:80])
    s = s.replace(x, y)
rep("overlay = null, top = 0, vx = null }) {   // Phase 512", "overlay = null, top = 0, vx = null, clean = false }) {   // clean: thin quiet outlines, the colour is in the fill only   // Phase 512")
rep("stroke={m ? m.stroke : (pixel ? '#26296b' : '#dbd2bd')} strokeWidth={m ? (m.sw || 2.5) : (pixel ? 2 : 1)}", "stroke={clean ? '#d3cab4' : m ? m.stroke : (pixel ? '#26296b' : '#dbd2bd')} strokeWidth={clean ? 1 : m ? (m.sw || 2.5) : (pixel ? 2 : 1)}")
rep("stroke={m ? m.stroke : '#26296b'} strokeWidth={m ? (m.sw ? Math.min(m.sw, 2) : 2) : 1} rx={pixel ? 0 : 2}/>", "stroke={clean ? (m ? m.black : '#1d1c22') : m ? m.stroke : '#26296b'} strokeWidth={clean ? 1 : m ? (m.sw ? Math.min(m.sw, 2) : 2) : 1} rx={pixel ? 0 : 2}/>")
rep("ncol, nums, ring, mw, oct }) {", "ncol, nums, ring, mw, oct, clean }) {")
rep("<TapKeyboard octaves={oct || 2} extraC labels=", "<TapKeyboard octaves={oct || 2} extraC clean={clean} labels=")
rep("<ScKeys nums ks={KK} marks={P.mk}", "<ScKeys nums clean ks={KK} marks={P.mk}")
rep("<ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={mode + key + form} mw={520}/>", "<ScKeys clean ks={K} marks={marks} names={names} arcs={[]} nonce={mode + key + form} mw={520}/>")
rep("<div style={{ overflowX: 'auto' }}><div style={{ minWidth: oct === 2 ? 640 : 0 }}><ScKeys nums clean", "<div><div><ScKeys nums clean")
# the staff: both hands together (treble over bass), one octave
rep("function sfdMinItems(key, form) {\n  const L = 'CDEFGAB', d0 = key[0] === 'B' ? 27 : 28 + L.indexOf(key[0]), nat", "function sfdMinItems(key, form, dOver) {\n  const L = 'CDEFGAB', d0 = dOver != null ? dOver : key[0] === 'B' ? 27 : 28 + L.indexOf(key[0]), nat")
rep("const sfdScaleItems = (k) => { const d0 = SC_D0[k]; return", "const sfdLD0 = (k) => { const L = 'CDEFGAB'.indexOf(k[0]); return 21 + L - (L >= 3 ? 7 : 0); };   // the left hand's octave, on the bass staff\nconst sfdScaleItems = (k, d0 = SC_D0[k]) => { return")
rep("    const hl = skgOf(sfdScaleItems(key), key, n => n.byKey);\n    staff = { items: sfdScaleItems(key), k: key, coral: [], alt: hl };", "    const mkS = (d0) => { const it = sfdScaleItems(key, d0); return { items: it, coral: [], alt: skgOf(it, key, n => n.byKey) }; };\n    staff = { k: key, R: mkS(SC_D0[key]), L: mkS(sfdLD0(key)) };")
rep("    const mi = sfdMinItems(key, form); if (mi) { const hl = skgOf(mi.items, sigK, n => n.byKey).filter(j => !mi.coral.includes(j)); staff = { items: mi.items, k: sigK, coral: mi.coral, alt: hl }; }", "    const mkM = (d0) => { const mi = sfdMinItems(key, form, d0); return mi && { items: mi.items, coral: mi.coral, alt: skgOf(mi.items, sigK, n => n.byKey).filter(j => !mi.coral.includes(j)) }; };\n    const mR = mkM(null), mL = mkM(sfdLD0(key)); if (mR && mL) staff = { k: sigK, R: mR, L: mL };")
rep("        <SkgStaff items={staff.items} k={staff.k} width={330} o={{ boxS: 26, D: 30, hl: staff.coral, hl2: staff.alt, signHl: staff.coral, underAlt: staff.alt, ksCol: '#2e8a6e', ...skgUnder(staff.items, staff.k, null, staff.coral) }}/>",
"        {[['R', 'treble', t('RIGHT HAND', '오른손')], ['L', 'bass', t('LEFT HAND', '왼손')]].map(([h, cf, lb]) => <div key={h} style={{ marginTop: 6 }}><div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em' }}>{lb}</div><SkgStaff items={staff[h].items} k={staff.k} clef={cf} width={330} o={{ boxS: 26, D: 30, hl: staff[h].coral, hl2: staff[h].alt, signHl: staff[h].coral, underAlt: staff[h].alt, ksCol: '#2e8a6e', ...skgUnder(staff[h].items, staff.k, null, staff[h].coral) }}/></div>)}")
open(b, 'w', encoding='utf-8').write(s); print('ok')
