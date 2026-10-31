"""Build EA (her 09:38 'stems hanging off the heads: check for any like this', the audit after call 40 opened the toys in
their steps): MelodyStaff's stems meet their heads (the filled 6.4 x 4.6 head's outer edge is 6.22 from its centre, the
hollow 6.8 x 4.6 one's 7.58 with its stroke: stems at 5.57 and 6.93, from the centre; flags and beams with them), and the
syncopation picture's second and third stems (Rhythm, Grade 4's checks) sit like its first."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
R("""            {stem && (up ? <line x1={n.x + 6} x2={n.x + 6} y1={y - 1} y2={G ? G.beamY : y - 30} stroke={col} strokeWidth="1.3"/> : <line x1={n.x - 6} x2={n.x - 6} y1={y + 1} y2={G ? G.beamY : y + 30} stroke={col} strokeWidth="1.3"/>)}""",
  """            {stem && (up ? <line x1={n.x + (hollow ? 6.93 : 5.57)} x2={n.x + (hollow ? 6.93 : 5.57)} y1={y} y2={G ? G.beamY : y - 30} stroke={col} strokeWidth="1.3"/> : <line x1={n.x - (hollow ? 6.93 : 5.57)} x2={n.x - (hollow ? 6.93 : 5.57)} y1={y} y2={G ? G.beamY : y + 30} stroke={col} strokeWidth="1.3"/>)}""")
R("""            {n.dur === 0.5 && !G && (up ? <path d={`M${n.x + 6},${y - 30} q 3 8 9 12 q -4 -3 -9 -5`} fill={col} stroke={col} strokeWidth="1"/> : <path d={`M${n.x - 6},${y + 30} q 3 -8 9 -12 q -4 3 -9 5`} fill={col} stroke={col} strokeWidth="1"/>)}""",
  """            {n.dur === 0.5 && !G && (up ? <path d={`M${n.x + 5.57},${y - 30} q 3 8 9 12 q -4 -3 -9 -5`} fill={col} stroke={col} strokeWidth="1"/> : <path d={`M${n.x - 5.57},${y + 30} q 3 -8 9 -12 q -4 3 -9 5`} fill={col} stroke={col} strokeWidth="1"/>)}""")
R("""        const xa = placed[g.first].x + (g.up ? 6 : -6) - 0.65, xb = placed[g.last].x + (g.up ? 6 : -6) + 0.65, y = g.up ? g.beamY : g.beamY - 4;""",
  """        const xa = placed[g.first].x + (g.up ? 5.57 : -5.57) - 0.65, xb = placed[g.last].x + (g.up ? 5.57 : -5.57) + 0.65, y = g.up ? g.beamY : g.beamY - 4;""")
R("""<line x1="43" x2="43" y1="33" y2="10" stroke="#e4572e" stroke-width="1.8"/>""", """<line x1="42.45" x2="42.45" y1="34" y2="10" stroke="#e4572e" stroke-width="1.8"/>""")
R("""<line x1="67" x2="67" y1="33" y2="10" stroke="#26296b" stroke-width="1.8"/><path d="M67 10 Q74 16 72 24" """, """<line x1="66.45" x2="66.45" y1="34" y2="10" stroke="#26296b" stroke-width="1.8"/><path d="M66.45 10 Q73.45 16 71.45 24" """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok stems', len(s))
