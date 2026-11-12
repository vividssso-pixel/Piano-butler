# The Piano Butler Handbook, Part IX: Going further (her 11 Nov: the topics the Library had as Extra get Handbook chapters).
# 1 Notes outside the chord (non-chord notes). Modes and other scales, and Transposition, follow.
exec(open('/tmp/claude-0/pk/harmony.py').read())   # helpers, css, cakes (rebuilds the harmony drafts, harmless)
import json as _gj
PP.update({k: _ledger(v) for k, v in _gj.load(open('/tmp/claude-0/further/gout_c.json')).items()})
def gpage(inner, n): return page(inner, n, 'PART IX · GOING FURTHER')
SECRETS['G1'] = 'A note outside the chord moves by step: into the chord, out of it, or both.'
def nfig(k, red, h=80): return ykfig(k, red, h)
NCT = [('Passing note', 'g1_pass', ('n2',), 'over C', 'steps <b>between</b> two chord notes'),
       ('Auxiliary note', 'g1_aux', ('n2',), 'over C', 'steps <b>out and back</b> to the same note'),
       ('Appoggiatura', 'g1_app', ('n1',), 'over C', '<b>leans</b> on the beat, then steps into the chord'),
       ('Suspension', 'g1_sus', ('n3',), 'F chord, then C', 'is <b>held over</b> from the last chord, then falls'),
       ('Anticipation', 'g1_ant', ('n3',), 'G chord, then C', 'arrives <b>early</b>, before its chord')]
CARDS = '<div class="nct5">' + ''.join(f'<div class="nc"><b>{n}</b>{nfig(k, r)}<i>{c}</i><span>{t}</span></div>' for n, k, r, c, t in NCT) + '</div>'
G1 = gpage(f"""{head('Part IX · Going further · 1', 'Notes outside the chord', 'Under a tune, the chord holds the main notes. The other notes of the tune are <b>non-chord notes</b>: they lean on the chord for a moment, then step back into it. Name them, and you know which notes to shape and which to rest on.')}
{hero(CARDS, 'Five ways out of the chord and back. Red: outside the chord.')}
<div class="big3 h3x"><div><span>1</span><p>Name the <b>chord</b> under the bar: its three notes.</p></div><div><span>2</span><p>Mark every tune note that is <b>not</b> one of them.</p></div><div><span>3</span><p>Look how it <b>moves in and out</b>: that gives its name.</p></div></div>
{h3('The five at a glance')}
{tbl(['Name', 'How it moves', 'Beat', 'Also called'], [['<b>Passing note</b>', 'steps between two chord notes, going the same way', 'usually weak', '—'], ['<b>Auxiliary note</b>', 'steps away from a chord note and back to it', 'usually weak', 'neighbour note'], ['<b>Appoggiatura</b>', 'lands on the strong beat and leans, then steps into the chord', 'strong', 'from Italian <i>appoggiare</i>, to lean'], ['<b>Suspension</b>', 'held over from the last chord, then falls by step', 'strong', 'prepared, held, resolved'], ['<b>Anticipation</b>', 'a note of the next chord, sounded early', 'weak', '—']], ['24%', '42%', '14%', '20%'])}
<!--SPLIT-->
{youknow('Ode to Joy (Beethoven)', ykfig('g1_ode', ('n3',), 70), 'Bar 1 sits on C (C E G). The <b class="co">F</b> steps from E up to G: a <b>passing note</b>.', 'Play bar 1 with a C chord in the left hand and hear the F slip between E and G.')}
{inaction('Which notes are outside the chord? The chord is C', qtag(nfig('g1_ex1', (), 66)), ['<b>The chord is C</b>: C, E and G.', '<b>Mark every note</b> that is not C, E or G.', '<b>How does each one move?</b>'], 'A and B: two passing notes from G up to C (B falls on beat 3, and still passes). In bar 2, D passes from E down to C.')}
{game('Name it', '<div class="gm4" style="grid-template-columns:repeat(4,1fr)">' + ''.join(f'<div>{nfig(k, r, 46)}<b>{q}</b></div>' for k, r, q in (('g1_pass_q', ('n2',), '1'), ('g1_aux_q', ('n2',), '2'), ('g1_app_q', ('n1',), '3'), ('g1_sus_q', ('n3',), '4'))) + '</div>', 'Passing, auxiliary, appoggiatura or suspension? The chord is C (in 4: F, then C).', '1 passing · 2 auxiliary · 3 appoggiatura · 4 suspension')}
{try10(nfig('g1_aux', ('n2',), 46), 'Play C D C, then C B C, over a C chord.', 'Out and straight back: two auxiliary notes.')}
{thinkt('Stepping stones in a stream: the chord is the bank. Step onto a stone for a moment, then land on the bank again.')}
{watch(['Calling a note outside the chord a mistake: it is the tune’s colour. It almost always moves by step.', 'Choosing a chord for a passing note: choose for the main notes.'])}
{foot('Chords under a melody p. {{M3}} · Chords in a key p. {{H3}} · Ornaments p. {{E5}}', 'Workbook Going further 1 · Online: Library › Non-chord notes')}""", 175)
GTOC = [('Notes outside the chord', 'G1'), ('Modes and other scales (coming)', 'G2'), ('Transposition (coming)', 'G3')]
GOPEN = f"""<section class="pg part2"><div class="pframe"><div class="pk">Part IX · Beyond the levels</div><div class="pt">Going further</div><div class="pdv"></div>
<p class="pl">The notes that decorate a tune, the scales older and newer than major and minor, and moving a whole piece into another key. Read them when your pieces ask for them.</p>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{"" if "coming" in x else PM.PAGE[k]}</span></div>' for x, k in GTOC)}</div></div></section>"""
css += """
.nct5{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;width:100%} .nct5>.nc{grid-column:span 2} .nct5>.nc:nth-child(4){grid-column:2 / span 2} .nct5>.nc:nth-child(5){grid-column:4 / span 2} .nc{border:1.5px solid #e3e1ee;border-radius:8px;padding:8px 6px 9px;display:flex;flex-direction:column;align-items:center;gap:3px;text-align:center;background:#fff}
.nc>b{font-size:14px;color:#26296b} .nc i{font-size:11.5px;color:#6d6f9c;font-style:normal} .nc span{font-size:12.5px;line-height:1.3;color:#26296b} .nc figure{margin:2px 0} .gm4>div{justify-content:flex-end}
"""
_secsG = [assemble('G1', G1)]
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{GOPEN}{"".join(_secsG)}{_flowjs}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-further.html', 'w').write(html)
print('ok further')
