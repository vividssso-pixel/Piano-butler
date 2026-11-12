# The Piano Butler Workbook: Going further (her 11 Nov). Two pages per chapter: Learn and Use.
exec(open('/tmp/claude-0/pk/wbmore.py').read())   # helpers, css, firstdone (rewrites the other workbooks, harmless)
import json as _wj
_GV = _wj.load(open('/tmp/claude-0/further/gout_c.json'))
def gsn(k, red=(), h=64):
    s = _GV[k].replace('<svg ', f'<svg style="width:100%;height:auto;max-height:{h}px" ', 1)
    for n in red: s = s.replace(f'<g id="{n}" class="note">', f'<g id="{n}" class="note" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx px" style="border:0;background:none;box-shadow:none;margin:0"><div class="vs">' + s + '</div></figure>'
GT = mk('Going further', 'GOING FURTHER')
G1A = GT('Learn', 'Notes outside the chord', 'Notes outside the chord', 'A note outside the chord moves by step: into the chord, out of it, or both.', f'''
{ex(1, 'In or out?', 1, 'The chord is C: C, E and G. Write <b>in</b> or <b>out</b> under each note. The first is done.', tbl(['Note', 'C', 'D', 'E', 'F', 'G', 'A', 'B'], [['In or out?', D('in'), BOX, BOX, BOX, BOX, BOX, BOX]], ['23%'] + ['11%'] * 7))}
{ex(2, 'Match the name', 1, 'Write the name: passing note, auxiliary note, appoggiatura, suspension or anticipation. The first is done.', tbl(['How it moves', 'Its name'], [['steps between two chord notes', D('passing note')], ['steps out and straight back to the same note', LINE], ['lands on the strong beat and leans, then steps into the chord', LINE], ['is held over from the last chord, then falls by step', LINE], ['is a note of the next chord, sounded early', LINE]], ['62%', '38%']))}
{ex(3, 'Name the red note', 2, 'The chord is C each time. Name the red note.', '<div class="ts6" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div style="flex-direction:column;border:0">{gsn(k, r)}<b>{n}</b>{LINE}</div>' for n, k, r in (('A', 'w_1', ('n2',)), ('B', 'w_2', ('n2',)), ('C', 'w_3', ('n1',)))) + '</div>')}
{ex(4, 'True or false?', 1, 'Circle T or F.', tfrows(('A note outside the chord is a wrong note.', 'A passing note moves by step.', 'An auxiliary note comes back to the note it started on.', 'A suspension arrives before its chord.')))}
<p class="sm" style="margin-top:12px"><b>Answers:</b> 1 in, out, in, out, in, out, out · 2 passing note, auxiliary note, appoggiatura, suspension, anticipation · 3 A passing (F), B auxiliary (D), C appoggiatura (B, on the beat, up to C) · 4 F, T, T, F.</p>''', 1, 'G1')
G1B = GT('Use', 'Notes outside the chord', 'Find them, write them', 'Find the chord first. Every tune note that is not in it is a note outside the chord.', f'''
{ex(1, 'Find them in a tune', 2, 'The chord is C for both bars. Circle each note outside the chord, then name it below.', gsn('w_4', (), 62) + tbl(['Note', 'Its name'], [[D('D'), D('passing note')], [LINE, LINE]], ['30%', '70%']))}
{ex(2, 'Write the missing note', 2, 'Write the note that fits. The chord is C. The first is done.', tbl(['Tune', 'The missing note is…', 'Letter'], [['E · ? · C', 'a passing note', D('D')], ['G · ? · G', 'an auxiliary note, above', BOX], ['C · ? · C', 'an auxiliary note, below', BOX]], ['30%', '48%', '22%']))}
{ex(3, 'In your own piece', 2, 'Find two notes outside the chord in a piece you play.', tbl(['Bar', 'Chord', 'Note', 'Its name'], [[LINE, LINE, LINE, LINE] for _ in range(2)], ['16%', '22%', '18%', '44%']))}
{ex(4, 'Late or early?', 2, 'Late (a suspension) or early (an anticipation)? The first is done.', tbl(['What happens', 'Late or early?', 'Its name'], [['The chords go F, then C. The tune holds F into the C chord, then falls to E.', D('late'), D('suspension')], ['The chords go G, then C. The tune plays C just before the C chord.', BOX, LINE], ['The chords go C, then G. The tune holds C into the G chord, then falls to B.', BOX, LINE]], ['58%', '18%', '24%']))}
<p class="sm" style="margin-top:12px"><b>Answers:</b> 1 D and F: passing notes · 2 D, A, B · 3 check with your teacher · 4 late, suspension; early, anticipation; late, suspension.</p>''', 2, 'G1')
_write('workbook-further', [G1A, G1B], {})
print('ok wbfurther')
