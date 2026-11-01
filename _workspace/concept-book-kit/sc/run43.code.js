// ── Build EE (the rest of call 39, her 02:09 'the pictures also show it on the staff'): any run of keys on the staff, spelt
// with the names the picture already shows, read against a key signature (accidentals only where the signature and the bar
// do not already give the note), placed in the octave nearest the staff's middle, the right hand's fingers over the treble
// and the left hand's under the bass. Her 20:30 ('it has to make sense: only the ones better changed'): only under the 7th
// chords (Arpeggios and Progressions, Grades 6 to 8), where the staff shows what the keys cannot: the four notes stacked in
// 3rds on lines or on spaces, and their spelling (E♯ not F, F♭ not E, C♭ not B). The chromatic scales (the same notes in
// both hands, a fingering task), the arpeggios (the names are on the keys already) and the scales a 3rd and a 6th apart
// keep their keyboards alone.
const SP_RUN_SIGN = { 1: '#', [-1]: 'b', 0: 'n' };
const spRunAlt = (nm) => (nm.includes('𝄪') ? 2 : nm.includes('𝄫') ? -2 : nm.includes('♯') ? 1 : nm.includes('♭') ? -1 : 0);
// keys (0 = middle C) with their names ('G♯') -> staff items in the key 'sig' (SKG_KEY's names); null for a double sharp or flat
function spRunItems(keys, names, sig = 'C', shift = 0) {
  const base = {}; skgSigns(sig).forEach(([s, l]) => { base[l] = s === '#' ? 1 : -1; });
  const cur = {}, items = [];
  for (let j = 0; j < keys.length; j++) {
    const nm = names[j], L = 'CDEFGAB'.indexOf(nm[0]), a = spRunAlt(nm); if (L < 0 || Math.abs(a) > 1) return null;
    const m = 60 + keys[j] + shift, oct = Math.round((m - a - [0, 2, 4, 5, 7, 9, 11][L]) / 12) - 1, d = 7 * oct + L;
    const now = cur[d] != null ? cur[d] : (base[nm[0]] || 0);
    if (a !== now) { items.push(['q', 1, d, SP_RUN_SIGN[a]]); cur[d] = a; } else items.push(['q', 1, d]);
  }
  return items.concat([['||']]);
}
// the octave that puts the run's middle nearest the staff's middle line (B4 on the treble, D3 on the bass)
const spRunShift = (keys, clef) => { const mid = (Math.min(...keys) + Math.max(...keys)) / 2, want = clef === 'bass' ? -10 : 11; return 12 * Math.round((want - mid) / 12); };
// rows: [{ hand: 'R' | 'L', keys, names, fingers, hl, sig }]; one staff each, the treble for the right hand, the bass for the left
function SpRunStaff({ rows, label, w = 380 }) {
  const out = rows.map((r, i) => { const clef = r.hand === 'L' ? 'bass' : 'treble', items = spRunItems(r.keys, r.names, r.sig || 'C', spRunShift(r.keys, clef));
    if (!items) return <div key={i} style={{textAlign:'center',fontSize:12,color:BK.muted,fontWeight:700,margin:'4px 0'}}>{t('This one needs a double sharp, so the staff is left out here.', '이건 겹샵이 필요해서 오선은 여기 없어요.')}</div>;
    return <div key={i} style={{display:'grid',gridTemplateColumns:rows.length > 1 ? '34px 1fr' : '1fr',alignItems:'center',gap:4,minWidth:0}}>{rows.length > 1 && <span style={{fontSize:10,fontWeight:900,color:BK.muted,textAlign:'right'}}>{r.hand === 'L' ? t('LH', '왼손') : t('RH', '오른손')}</span>}
      <SkgStaff items={items} k={r.sig || 'C'} clef={clef} width={w} full={r.keys.length > 9} o={{ boxS: 22, D: r.keys.length > 9 && r.fingers ? 22 : 26, hl: r.hl || [], ksCol: '#2e8a6e', fingers: r.fingers || undefined, fingerAt: clef === 'bass' ? 'below' : undefined }} label={label}/></div>; });
  return <div data-run-staff style={{display:'grid',gridTemplateColumns:rows.length > 1 ? 'repeat(auto-fit, minmax(250px, 1fr))' : '1fr',gap:'2px 10px',width:'100%',maxWidth:rows.length > 1 ? undefined : 460,margin:'6px auto 0'}}>{out}</div>;
}
