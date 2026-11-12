# Part II Time, chapter 8 (her 8 Nov: put in everything Time should have, in order): repeats and road signs.
_RN, _RR = '#26296b', '#e4572e'
def rule(x): return f'<div class="secret1" style="margin:8px 0"><span class="sl">The rule</span><span>{x}</span></div>'
def _segno(x, y, s=1):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M6,-14 C-6,-14 -6,-4 0,0 C6,4 6,14 -6,14" fill="none" stroke="{_RN}" stroke-width="2.6"/>'
            f'<line x1="-9" y1="12" x2="9" y2="-12" stroke="{_RN}" stroke-width="2"/><circle cx="-8" cy="-4" r="2" fill="{_RN}"/><circle cx="8" cy="4" r="2" fill="{_RN}"/></g>')
def _coda(x, y, s=1):
    return (f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="8" ry="10" fill="none" stroke="{_RN}" stroke-width="2.4"/>'
            f'<line x1="-14" y1="0" x2="14" y2="0" stroke="{_RN}" stroke-width="2"/><line x1="0" y1="-15" x2="0" y2="15" stroke="{_RN}" stroke-width="2"/></g>')
def road(blocks, order=None, q=False, W=74, H=52):
    """blocks: list of dicts {l: letter, start_rep, end_rep, ending: '1.'|'2.', above: text, segno, coda, fine}.
    order: list of block indices in playing order (drawn as a numbered path under the blocks); q: show '?' instead of the order."""
    n = len(blocks); x0 = 16; top = 46; Wt = x0 * 2 + n * W
    if order and q: Wt = max(Wt, x0 + 96 + len(order) * 34 + 6)
    o = f'<svg viewBox="0 0 {Wt} {top + H + (64 if order else 14)}" style="width:100%;max-width:{Wt}px;height:auto;display:block;margin:0 auto">'
    for i, b in enumerate(blocks):
        x = x0 + i * W
        o += f'<rect x="{x}" y="{top}" width="{W}" height="{H}" fill="#fff" stroke="{_RN}" stroke-width="1.6"/>'
        o += f'<text x="{x + W / 2}" y="{top + H / 2 + 9}" text-anchor="middle" font-family="PF,serif" font-size="26" font-weight="700" fill="{_RN}">{b["l"]}</text>'
        if b.get('start_rep'): o += f'<line x1="{x + 3}" y1="{top}" x2="{x + 3}" y2="{top + H}" stroke="{_RN}" stroke-width="5"/><line x1="{x + 10}" y1="{top}" x2="{x + 10}" y2="{top + H}" stroke="{_RN}" stroke-width="1.6"/><circle cx="{x + 16}" cy="{top + H * .36}" r="3" fill="{_RN}"/><circle cx="{x + 16}" cy="{top + H * .64}" r="3" fill="{_RN}"/>'
        if b.get('end_rep'): o += f'<line x1="{x + W - 3}" y1="{top}" x2="{x + W - 3}" y2="{top + H}" stroke="{_RN}" stroke-width="5"/><line x1="{x + W - 10}" y1="{top}" x2="{x + W - 10}" y2="{top + H}" stroke="{_RN}" stroke-width="1.6"/><circle cx="{x + W - 16}" cy="{top + H * .36}" r="3" fill="{_RN}"/><circle cx="{x + W - 16}" cy="{top + H * .64}" r="3" fill="{_RN}"/>'
        if b.get('ending'): o += f'<path d="M{x + 2},{top - 4} V{top - 18} H{x + W - 6}" fill="none" stroke="{_RR}" stroke-width="2"/><text x="{x + 8}" y="{top - 6}" font-family="AH,Arial" font-size="13" font-weight="700" fill="{_RR}">{b["ending"]}</text>'
        if b.get('segno'): o += _segno(x + 14, top - 20, .9)
        if b.get('coda'): o += _coda(x + 14, top - 20, .9)
        if b.get('above'): o += f'<text x="{x + W / 2 + (10 if b.get('segno') or b.get('coda') else 0)}" y="{top - 8}" text-anchor="middle" font-family="AH,Arial" font-size="12.5" font-weight="700" font-style="italic" fill="{_RR}">{b["above"]}</text>'
    if order:
        y = top + H + 30
        if q:
            o += f'<text x="{x0}" y="{y + 6}" font-family="AH,Arial" font-size="15" font-weight="700" fill="{_RN}">You play:</text>'
            for k in range(len(order)):
                cx = x0 + 96 + k * 34
                o += f'<circle cx="{cx}" cy="{y}" r="13" fill="#fff3ee" stroke="{_RR}" stroke-width="2"/><text x="{cx}" y="{y + 5}" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{_RR}">?</text>'
        else:
            pts = ' → '.join(blocks[k]['l'] for k in order)
            o += f'<text x="{Wt / 2}" y="{y + 6}" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="{_RR}">You play: {pts}</text>'
    return o + '</svg>'
_SIGNS = [[road([{'l': 'A', 'start_rep': 1, 'end_rep': 1}], W=60, H=40), '<b>repeat signs</b>', 'play the bars between them twice (with only the end sign: go back to the start)'],
          [road([{'l': 'B', 'ending': '1.', 'end_rep': 1}, {'l': 'C', 'ending': '2.'}], W=60, H=40), '<b>1st and 2nd time bars</b>', 'first time play the 1. bar; after the repeat skip it and play the 2. bar'],
          ['<b class="co">D.C.</b>', '<b>da capo</b>', '“from the head”: go back to the very beginning'],
          [road([{'l': '', 'segno': 1}], W=40, H=20), '<b>D.S.</b> (dal segno)', '“from the sign”: go back to the segno'],
          ['<b class="co">Fine</b>', '<b>fine</b>', '“the end”: after a D.C. or D.S., stop here'],
          [road([{'l': '', 'coda': 1}], W=40, H=20), '<b>coda</b>', '“tail”: at “To Coda”, jump to the coda sign and play the ending']]
P43 = page(f'''{head('Part II · Time · 8', 'Repeats and road signs', 'Music often says “play that again”. Instead of writing the same bars twice, it uses <b>repeat signs</b> and <b>road signs</b>. Read them like a map: they tell you which bar comes next.')}
{hero(road([{'l': 'A', 'start_rep': 1}, {'l': 'B', 'end_rep': 1}, {'l': 'C'}], order=[0, 1, 0, 1, 2]), 'Two dots facing back mean: go back and play it again')}
{tbl(['Sign', 'Name', 'What you do'], _SIGNS, ['24%', '24%', '52%'])}
{rule('Follow the map in order. At a jump (D.C., D.S.) go back; then the first time you meet <b>Fine</b>, stop; or at <b>To Coda</b>, jump to the coda.')}
<!--SPLIT-->
{inact('In what order do you play these bars?', road([{'l': 'A'}, {'l': 'B', 'end_rep': 1}, {'l': 'C'}], order=[0, 1, 0, 1, 2], q=True), ['<b>Play A and B.</b>', '<b>B ends with a repeat sign</b> facing back. There is no start sign: where do you go back to?', '<b>Play it again,</b> then carry on.'], 'Back to the very start: <b>A B A B C</b>.')}
{inact('First and second time', road([{'l': 'A', 'start_rep': 1}, {'l': 'B', 'ending': '1.', 'end_rep': 1}, {'l': 'C', 'ending': '2.'}], order=[0, 1, 0, 2], q=True), ['<b>First time through:</b> play A, then the bar marked 1.', '<b>The repeat sign</b> sends you back to A.', '<b>Second time:</b> which bar do you skip, and which do you play?'], 'A B, A C: <b>A B A C</b>. The 1. bar is skipped the second time.')}
{inact('D.C. al Fine', road([{'l': 'A'}, {'l': 'B', 'above': 'Fine'}, {'l': 'C'}, {'l': 'D', 'above': 'D.C. al Fine'}], order=[0, 1, 2, 3, 0, 1], q=True, W=90), ['<b>Play straight through</b> to D.', '<b>D.C.</b> means go back: to where?', '<b>al Fine:</b> where do you stop the second time?'], 'A B C D, then from the head to Fine: <b>A B C D A B</b>.')}
<!--SPLIT-->
{inact('D.S. al Coda', road([{'l': 'A'}, {'l': 'B', 'segno': 1}, {'l': 'C', 'above': 'To Coda'}, {'l': 'D', 'above': 'D.S. al Coda'}, {'l': 'E', 'coda': 1}], order=[0, 1, 2, 3, 1, 2, 4], q=True, W=96), ['<b>Play through</b> to D. (Ignore “To Coda” the first time.)', '<b>D.S.</b> sends you back to the sign: which bar has it?', '<b>Play on to “To Coda”,</b> then jump. Where?'], 'A B C D, back to the sign, B C, jump to the coda: <b>A B C D B C E</b>.')}
{game('How many bars do you play?', qitems(['|: A B :|', 'A |: B C :| D', 'A B (Fine) C D.C.'], 3), 'Each letter is one bar. Follow the signs and count every bar you play.', '1 four (A B A B) · 2 six (A B C B C D) · 3 five (A B C A B).')}
{watch(['Taking the repeat again after a D.C.: on the way back, skip the repeats (unless the music says otherwise).', 'Jumping at “To Coda” the first time through: it only works after the D.S. or D.C.'])}
{foot('Pulse, tempo and the bar p. {{T1}} · Time signatures p. {{T4}}', 'Online: Library › Signs')}''', 68)
