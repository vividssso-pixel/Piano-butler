#!/usr/bin/env python3
# Phase 491: the dice board game under every quiz is gone (her 2026-10-19 01:07: 'remove this; ten questions at a time like chess, seeing the movement is good').
# In its place: ten small steps, one per question, and one token that moves a step after each answer (navy = right, coral = wrong).
# Same hook name and component name so all ~25 quiz types keep working.   python3 patch491.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
a = s.index("// Board game for this chapter: a correct answer rolls a die")
b = s.index("function NoteValQuestion({ q, level, given, locked, onAnswer, pixel }) {")
NEW = r'''// Ten steps, one per question (Phase 491; it replaced the dice board). The token moves one step after every answer:
// a navy step for a right answer, a coral one for a wrong answer. After the tenth step it starts again.
function useBoard(q, given) {
  const [b, setB] = useState({ marks: [] });
  const seen = useRef(null);
  useEffect(() => {
    if (!given || seen.current === q.uid) return;
    seen.current = q.uid;
    setB(prev => ({ marks: (prev.marks.length >= LESSON_TOTAL ? [] : prev.marks).concat(!!given.ok) }));
  }, [given, q.uid]);
  return b;
}
function BoardTrack({ b, pixel }) {
  try { if (new URLSearchParams(location.search).get('print') === '1') return null; } catch (e) {}
  const n = LESSON_TOTAL, gap = 4, gaps = (n - 1) * gap, pos = b.marks.length;
  const ink = pixel ? '#faf6ec' : '#26296b', cell = 'calc((100% - ' + gaps + 'px) / ' + n + ')';
  const label = t('Question ' + Math.min(pos + 1, n) + ' of ' + n + ', ' + b.marks.filter(Boolean).length + ' right so far', '문제 ' + Math.min(pos + 1, n) + ' / ' + n + ' · 지금까지 ' + b.marks.filter(Boolean).length + '개 맞음');
  return (
    <div role="img" aria-label={label} style={{position:'relative',display:'flex',gap,margin:'2px 0 14px',paddingBottom:2}}>
      {Array.from({ length: n }, (_, i) => {
        const done = i < pos, ok = b.marks[i];
        return <div key={i} style={{flex:'1 1 0',minWidth:0,height:12,borderRadius:pixel ? 0 : 6,boxSizing:'border-box',
          background:done ? (ok ? ink : (pixel ? 'rgba(228,87,46,0.55)' : '#fbe3da')) : (pixel ? 'rgba(250,246,236,0.08)' : '#fff'),
          border:'1.5px solid ' + (done && !ok ? '#e4572e' : (pixel ? 'rgba(250,246,236,0.35)' : '#e4dccb')),transition:'background 0.3s'}}/>;
      })}
      {pos < n && <div style={{position:'absolute',top:-4,left:'calc(' + pos + ' * (' + cell + ' + ' + gap + 'px) + ' + cell + ' / 2 - 10px)',width:20,height:20,borderRadius:10,background:'#e4572e',border:'2px solid ' + ink,boxSizing:'border-box',transition:'left 0.35s ease',pointerEvents:'none'}}/>}
    </div>
  );
}

'''
s = s[:a] + NEW + s[b:]
# the rule paragraph about the old board
x = s.index("      <p style={{fontSize:12,color:'var(--muted)',margin:'10px 0 0',lineHeight:1.5}}>\n        {t('Game board rule:")
y = s.index("</p>\n", x) + len("</p>\n")
s = s[:x] + s[y:]
open(dst, 'w', encoding='utf-8').write(s)
print('patched 491', len(s))
