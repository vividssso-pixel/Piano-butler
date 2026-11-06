#!/usr/bin/env python3
# Phase 462 (her 2026-10-13 23:56 and 23:57):
#  1. 'Whose house is this?': the tapped key and its house were hard to see (green beside coral borders on coral tints).
#     Now the tapped key is solid coral, its housemates pale coral with thin borders, one navy outline round the house,
#     and the other keys plain white while a house is lit. Green stays the colour of 'correct' only.
#  2. The openers' lists ('In this chapter', 'By the end, you can') had tick boxes, which read as things to tick.
#     Now a coral diamond in a navy one (bkGoal), the chequered diamond of the openers in small.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)

# 1. the keyboard: two new marks (with their own stroke width) and an outline round a group of white keys
rep("""  fof:    { white: '#dfe9f8', black: '#3b4fa8', stroke: '#3b4fa8' },
};""", """  fof:    { white: '#dfe9f8', black: '#3b4fa8', stroke: '#3b4fa8' },
  pick:   { white: '#e4572e', black: '#e4572e', stroke: '#c0431f', sw: 1.5 },   // Phase 462: the key you tapped
  mate:   { white: '#fbe3da', black: '#e4572e', stroke: '#e9b9a6', sw: 1 },     // Phase 462: the keys that go with it
};""")
rep("function TapKeyboard({ octaves, marks = {}, onTap, labels = null, tint = false, pixel = false, names = null }) {",
    "function TapKeyboard({ octaves, marks = {}, onTap, labels = null, tint = false, pixel = false, names = null, outline = null }) {   // outline (Phase 462): [first, last] white key index, one navy frame round them")
rep("""              stroke={m ? m.stroke : (pixel ? '#26296b' : '#dbd2bd')} strokeWidth={m ? 2.5 : (pixel ? 2 : 1)}""",
    """              stroke={m ? m.stroke : (pixel ? '#26296b' : '#dbd2bd')} strokeWidth={m ? (m.sw || 2.5) : (pixel ? 2 : 1)}""")
rep("""              stroke={m ? m.stroke : '#26296b'} strokeWidth={m ? 2 : 1} rx={pixel ? 0 : 2}/>""",
    """              stroke={m ? m.stroke : '#26296b'} strokeWidth={m ? (m.sw ? Math.min(m.sw, 2) : 2) : 1} rx={pixel ? 0 : 2}/>""")
rep("""          </g>
        );
      })}
    </svg>
  );
}

const NOTE_NAME_LEVELS = [""", """          </g>
        );
      })}
      {outline && (() => { const a = whites.find(k => k.i === outline[0]), b = whites.find(k => k.i === outline[1]); return a && b ? <rect x={a.x + 1.2} y="1.2" width={b.x + whiteW - a.x - 2.4} height={whiteH - 2.4} rx="4" fill="none" stroke="#26296b" strokeWidth="3" style={{pointerEvents:'none'}}/> : null; })()}
    </svg>
  );
}

const NOTE_NAME_LEVELS = [""")
rep("""    (small ? [0, 2, 4] : [5, 7, 9, 11]).forEach(k => { marks[base + k] = 'target'; });
    marks[pick] = 'good';""", """    (small ? [0, 2, 4] : [5, 7, 9, 11]).forEach(k => { marks[base + k] = 'mate'; });
    marks[pick] = 'pick';""")
rep("""      <TapKeyboard octaves={2} tint marks={marks} onTap={(k) => { if (!PC_INFO[k % 12].white) { playKey(k); return; } setPick(k); playKey(k); }}/>""",
    """      <TapKeyboard octaves={2} tint={pick == null} marks={marks} outline={pick == null ? null : (() => { const b = Math.floor(pick / 12) * 12; return [0, 2, 4].includes(pick % 12) ? [b, b + 4] : [b + 5, b + 11]; })()} onTap={(k) => { if (!PC_INFO[k % 12].white) { playKey(k); return; } setPick(k); playKey(k); }}/>""")

# 2. the openers' lists: a coral diamond in a navy one, never a tick box
rep("const bkTick = (s = 18) =>", """const bkGoal = (s = 15) => <svg viewBox="0 0 16 16" width={s} height={s} aria-hidden="true" style={{flex:'0 0 auto',verticalAlign:'middle',display:'inline-block'}}><path d="M8 0.9 L15.1 8 L8 15.1 L0.9 8 Z" fill="#fff" stroke={BK.ink} strokeWidth="1.3" strokeLinejoin="round"/><path d="M8 4 L12 8 L8 12 L4 8 Z" fill={BK.coral}/></svg>;   // Phase 462: the openers' lists
const bkTick = (s = 18) =>""")
rep("bkTick(15)", "bkGoal(15)", 18)
open(dst, 'w', encoding='utf-8').write(s); print('ok')
