# The Piano Butler Workbook: Before you play (her 11 Nov). Two pages: Learn (finger numbers, hand shape, stool) and a week of posture checks.
exec(open('/tmp/claude-0/pk/wbmore.py').read())   # helpers, css, firstdone (rewrites the other workbooks, harmless)
NV, RD, SOFT, LINE_C = '#26296b', '#e4572e', '#5a5d8f', '#c9cbe0'
_src = open('/tmp/claude-0/pk/before.py').read()
exec(_src[_src.index('def hand_side('):_src.index('def hand_top(')])      # the same hand drawings as the Handbook page
import json as _js, re as _re
exec(_src[_src.index('APP = _js.load'):_src.index('def warmpic(')])   # and the app's own pen drawings
BT = mk('Before you play', 'BEFORE YOU PLAY')
CHK = ['<b>Stool:</b> forearms level with the keys', '<b>Body:</b> front half of the stool, feet flat', '<b>Shoulders:</b> lifted, then dropped', '<b>Hands:</b> round, knuckles up', '<b>Breathe out</b>, then play']
BA = BT('Learn', 'Posture and hand shape', 'Posture and hand shape', 'Sit tall, forearms level with the keys, a round hand on the fingertips.', f'''
{ex(1, 'Finger numbers', 1, 'Write the number of each finger. They are the same in both hands. The first is done.', tbl(['Finger', 'Number', 'Finger', 'Number'], [['thumb', D('1'), 'ring finger', BOX], ['index finger', BOX, 'little finger', BOX], ['middle finger', BOX, '', '']], ['30%', '20%', '30%', '20%']))}
{ex(2, 'Which hand is round?', 1, 'Circle the round hand.', '<div class="ts6" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div style="flex-direction:column;border:0">{app(k, 190, "w" + n)}<b>{n}</b></div>' for n, k in (('A', '2:flat fingers'), ('B', '2:The good shape'), ('C', '2:knuckles collapsed'))) + '</div>')}
{ex(3, 'Too low, too high, or right?', 2, 'Write too low, too high or right.', tbl(['What you see', 'The stool is'], [['The elbows are well below the keys; the forearms go uphill.', D('too low')], ['The forearms are level with the keys.', LINE], ['The elbows are above the keys; the wrists drop down to them.', LINE]], ['68%', '32%']))}
{ex(4, 'True or false?', 1, 'Circle T or F.', tfrows(('The thumb is finger 1 in both hands.', 'Play with the flat pads of your fingers.', 'Your wrists can rest on the wood in front of the keys.', 'Your feet stay flat on the floor.')))}
<p class="sm" style="margin-top:14px"><b>Answers:</b> 1 thumb 1, index 2, middle 3, ring 4, little 5 · 2 B · 3 too low, right, too high · 4 T, F, F, T.</p>''', 1, 'B1')
BB = BT('Use', 'Posture and hand shape', 'My posture week', 'The 30-second check, every time you sit down: stool, body, shoulders, hands, breathe.', f'''
{ex(1, 'The 30-second check', 1, 'Every time you sit down to practise, check each line and tick a circle. One circle per day.', tbl(['', 'Mon to Sun'], [[c, ticks(7)] for c in CHK], ['48%', '52%'], 'wk7'))}
{ex(2, 'Six warm-ups', 1, 'Do each warm-up before you play. Tick a circle each day.', tbl(['', 'Mon to Sun'], [[f'<b>{w}</b>', ticks(7)] for w in ('Rag doll', 'Elbow wings', 'Arm glide', 'Arm drop', 'Knuckle bridge', 'Wrist balloon')], ['48%', '52%'], 'wk7'))}
{ex(3, 'Teacher’s check', 2, 'Your teacher ticks what is already right and circles one thing to work on this week.', tbl(['', 'Right', 'Work on'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>'] for c in ('Stool height and distance', 'Back and shoulders', 'Round hand: knuckles up, fingertips, level wrist')], ['60%', '20%', '20%'], 'prog'))}
''', 2, 'B1')
BFIRST = {'Which hand is round?': [('ring', 'B')]}
css += ' .wk7 td{padding-top:5px!important;padding-bottom:5px!important} .wk7 .tk{white-space:nowrap}'
_write('workbook-before', [BA, BB], {})
print('ok wbbefore')
