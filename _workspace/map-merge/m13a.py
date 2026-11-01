p='drills.src.html'; s=open(p).read()
a="""    if (up && d === 28) s += led(28);
"""
b="""    if (up && d === 28) { s += led(28);   // m13a: middle C written in the bass too, same key, same column
      const yb = yB(28); s += ln(yb, x - 8.5, x + 8.5).replace('stroke-opacity="0.55" stroke-width="1"', 'stroke-width="1.3"');
      s += '<ellipse data-ref-midc-bass cx="' + x + '" cy="' + yb + '" rx="5.4" ry="3.9" transform="rotate(-20 ' + x + ' ' + yb + ')" fill="' + col + '"/>'; }
"""
a2="middle C in coral, on its own ledger line between the staves.', '가운데 C 두 옥타브 아래 C부터 두 옥타브 위 C까지의 흰건반 모두. 코랄색이 가운데 C, 두 오선 사이의 덧줄 위.')"
b2="middle C in coral, written two ways: on a ledger line below the treble staff and on a ledger line above the bass staff. Same key, same sound.', '가운데 C 두 옥타브 아래 C부터 두 옥타브 위 C까지의 흰건반 모두. 코랄색이 가운데 C: 높은음자리표 아래 덧줄에도, 낮은음자리표 위 덧줄에도 써요. 같은 건반, 같은 소리.')"
if 'm13a' not in s:
    assert s.count(a)==1 and s.count(a2)==1
    s=s.replace(a,b).replace(a2,b2); open(p,'w').write(s); print('ok')
else: print('already')
