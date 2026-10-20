import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
# second colour for accidentals: o.hl2 (notes), o.signHl2 (signs), o.underAlt (names)
rep("const coral = (j) => o.lit === j || (o.hl || []).includes(j);\n  const stem", "const coral = (j) => o.lit === j || (o.hl || []).includes(j), alt = (j) => (o.hl2 || []).includes(j), ALT = '#2e8a6e';\n  const stem")
rep("kind = k === 'hd' ? 'h' : k, c = coral(notes.length) ? cor : col;", "kind = k === 'hd' ? 'h' : k, c = coral(notes.length) ? cor : alt(notes.length) ? ALT : col;")
rep("fill=\"' + (cr ? cor : col) + '\"' + (cr ? ' font-style=\"italic\"' : '') + '>' + v", "fill=\"' + (cr ? cor : (o.underAlt || []).includes(j) ? ALT : col) + '\"' + (cr || (o.underAlt || []).includes(j) ? ' font-style=\"italic\"' : '') + '>' + v")
rep("tnAcc(P.signs[j], n.x - 21, n.y, (o.signHl || []).includes(j) ? PEN_C : (o.ink || PEN_N))", "tnAcc(P.signs[j], n.x - 21, n.y, (o.signHl || []).includes(j) ? PEN_C : (o.signHl2 || []).includes(j) ? '#2e8a6e' : (o.ink || PEN_N))", s.count("tnAcc(P.signs[j], n.x - 21, n.y, (o.signHl || []).includes(j) ? PEN_C : (o.ink || PEN_N))"))
# ScMinor: key-signature notes coral, accidentals blue
rep("const cUp = f === 'harmonic' ? [6] : f === 'melodic' ? [5, 6] : [], cDn = f === 'harmonic' ? [1] : [];",
    "const cUp = f === 'harmonic' ? [6] : f === 'melodic' ? [5, 6] : [], cDn = f === 'harmonic' ? [1] : [], aUp = f === 'melodic' ? [] : [5], aDn = [2];")
rep("const stf = (items, coral, only, ring, key) => <SkgStaff key={key} items={items} k=\"F\" width={330} o={{ boxS: 26, D: 30, hl: coral, signHl: coral, ring: ring == null ? [] : [ring], ...skgUnder(items, 'F', only, coral) }}/>;",
    "const stf = (items, coral, alt, only, ring, key) => <SkgStaff key={key} items={items} k=\"F\" width={330} o={{ boxS: 26, D: 30, hl: coral, hl2: alt, signHl: coral, underAlt: alt, ksCol: '#2e8a6e', ring: ring == null ? [] : [ring], ...skgUnder(items, 'F', only, coral) }}/>;")
rep("{stf(upI, cUp, onlyUp,", "{stf(upI, cUp, aUp, onlyUp,")
rep("{stf(dnI, cDn, onlyDn,", "{stf(dnI, cDn, aDn, onlyDn,")
rep("      {an >= 0 ? <ScPillRow st={QS} upTo={an} cur={an - 1}/> : <ScPillRow st={M.ST} upTo={7}/>}\n",
    "      <div style={{display:'flex',justifyContent:'center',gap:14,flexWrap:'wrap',fontSize:12,fontWeight:800,margin:'2px 0 4px'}}><span style={{color:'#2e8a6e'}}>{t('● from the key signature', '● 조표에서 온 음')}</span>{f !== 'natural' && <span style={{color:'#c0431f'}}>{t('● accidental, beside the note', '● 임시표, 음표 옆에 붙은 음')}</span>}</div>\n      {an >= 0 ? <ScPillRow st={QS} upTo={an} cur={an - 1}/> : <ScPillRow st={M.ST} upTo={7}/>}\n")
# lesson 9 and 2: key-signature notes green too
a="const d0 = SC_D0[k], items = Array.from({ length: 8 }, (_, j) => ['q', 1, d0 + j]).concat([['||']]), hl = skgOf(items, k, n => n.byKey);\n  return <SkgStaff items={items} k={k} width={width} o={{ boxS: 26, D: 30, hl, ...skgUnder(items, k, only, hl), ring: ring == null ? [] : [ring] }}/>;"
assert s.count(a)==1
s=s.replace(a,"const d0 = SC_D0[k], items = Array.from({ length: 8 }, (_, j) => ['q', 1, d0 + j]).concat([['||']]), hl = skgOf(items, k, n => n.byKey);\n  return <SkgStaff items={items} k={k} width={width} o={{ boxS: 26, D: 30, hl2: hl, underAlt: hl, ksCol: '#2e8a6e', ...skgUnder(items, k, only, []), ring: ring == null ? [] : [ring] }}/>;")
open(sys.argv[2],'w',encoding='utf-8').write(s)
