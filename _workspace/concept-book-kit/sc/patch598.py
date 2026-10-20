import sys
s=open(sys.argv[1],encoding='utf-8').read()
a="      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + fm} onTap={tap}/>\n      <ScPillRow st={QS} upTo={at} cur={at - 1}/>\n"
assert s.count(a)==1
b="""      <ScKeys ks={K} marks={at === 0 ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={arcs} nonce={nonce + fm} onTap={tap}/>
      {(() => {   // the staff with its key signature (B♭); each note appears as she taps it: key-signature notes green, accidentals coral
        const dn = at >= 7, cnt = dn ? at - 6 : at + 1, all = scMinItems(fm, dn ? 'down' : 'up'), items = all.slice(0, cnt).concat([['||']]);
        const acc = dn ? (fm === 'harmonic' ? [1] : []) : (fm === 'harmonic' ? [6] : fm === 'melodic' ? [5, 6] : []), ks = dn ? [2] : (fm === 'melodic' ? [] : [5]);
        const on = (l) => l.filter(j => j < cnt);
        return <SkgStaff key={'tr' + fm + (dn ? 'd' : 'u') + cnt} items={items} k="F" width={330} o={{ boxS: 26, D: 30, hl: on(acc), hl2: on(ks), signHl: on(acc), underAlt: on(ks), ksCol: '#2e8a6e', ...skgUnder(items, 'F', null, on(acc)) }}/>;
      })()}
      <ScPillRow st={QS} upTo={at} cur={at - 1}/>
"""
s=s.replace(a,b)
open(sys.argv[2],'w',encoding='utf-8').write(s)
