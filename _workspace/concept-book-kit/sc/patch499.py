#!/usr/bin/env python3
# Phase 499: 'Say the order' draws the zigzag (her 2026-10-19 09:17): the sharps light on the keyboard as before, and a numbered
# dot for each sits above its key, joined by a line that falls step by step, so the left-right-left pattern shows.
# B♯ is drawn on an extra C to the right of B (E♯ on F), so the order keeps going 'up a 5th' instead of jumping back to the first C.
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)

rep("function TapKeyboard({ octaves, marks = {}, onTap, labels = null, tint = false, pixel = false, names = null, outline = null, bigLabels = false }) {",
    "function TapKeyboard({ octaves, marks = {}, onTap, labels = null, tint = false, pixel = false, names = null, outline = null, bigLabels = false, extraC = false, trail = null, trailLabels = null }) {   // Phase 499: extraC = one more C at the right end; trail = numbered dots above the keys, joined in order")
rep("  const width = w * whiteW;\n  const tap = onTap ?",
    "  if (extraC) { whites.push({ i: octaves * 12, x: w * whiteW, info: PC_INFO[0] }); w++; }\n  const width = w * whiteW;\n  const TR = trail && trail.length ? 58 : 0;\n  const tpos = (i) => { const wk = whites.find(k => k.i === i); if (wk) return wk.x + whiteW / 2; const bk = blacks.find(k => k.i === i); return bk ? bk.x + blackW / 2 : 0; };\n  const tap = onTap ?")
rep("    <svg viewBox={'-1 -1 ' + (width + 2) + ' ' + (whiteH + 2)} shapeRendering={edge}\n      style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>\n      {whites.map(k => {",
    "    <svg viewBox={'-1 ' + (-1 - TR) + ' ' + (width + 2) + ' ' + (whiteH + 2 + TR)} shapeRendering={edge}\n      style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>\n      {whites.map(k => {")
rep("            {labels && solfaOn() && (\n              <text x={k.x + whiteW / 2} y={whiteH - 27}",
    "            {trailLabels && trailLabels[k.i] && <text x={k.x + whiteW / 2} y={whiteH - 34} textAnchor=\"middle\" fontSize=\"13\" fontWeight=\"900\" fill={m ? (m.text || '#fff') : '#c0431f'} style={{pointerEvents:'none'}}>{trailLabels[k.i]}</text>}\n            {labels && solfaOn() && (\n              <text x={k.x + whiteW / 2} y={whiteH - 27}")
rep("      {outline && (() => { const a = whites.find",
    "      {TR > 0 && (() => { const P = trail.map((q, j) => [tpos(q.i), -50 + j * 7.5]); return <g aria-hidden=\"true\" style={{pointerEvents:'none'}}>\n        <polyline points={P.map(p => p.join(',')).join(' ')} fill=\"none\" stroke=\"#e4572e\" strokeWidth=\"2.2\" strokeLinejoin=\"round\" strokeLinecap=\"round\"/>\n        {P.map((p, j) => <g key={j}><circle cx={p[0]} cy={p[1]} r={j === P.length - 1 ? 9 : 7.5} fill={j === P.length - 1 ? '#c0431f' : '#e4572e'} stroke=\"#fffefa\" strokeWidth=\"1.5\"/><text x={p[0]} y={p[1] + 3.5} textAnchor=\"middle\" fontSize=\"10\" fontWeight=\"900\" fill=\"#fff\">{trail[j].n}</text></g>)}\n      </g>; })()}\n      {outline && (() => { const a = whites.find")

# KfFind: the trail
rep("  if (done) { if (sharp) marks[pcOfName(order[want])] = 'mate'; marks[tonic] = 'pick'; }\n  else if (ran) order.slice(0, lit).forEach((nm, i) => { marks[pcOfName(nm)] = i === lit - 1 ? 'pick' : 'mate'; });",
    "  const kidx = (nm) => (sharp && pcOfName(nm) === 0 ? 12 : pcOfName(nm));   // B♯ is the C above B\n  if (done) { if (sharp) marks[kidx(order[want])] = 'mate'; marks[tonic] = 'pick'; }\n  else if (ran) order.slice(0, lit).forEach((nm, i) => { marks[kidx(nm)] = i === lit - 1 ? 'pick' : 'mate'; });\n  const trail = ran && !done && lit > 0 ? order.slice(0, lit).map((nm, i) => ({ i: kidx(nm), n: i + 1 })) : null;\n  const trailLabels = trail ? (() => { const o = {}; order.slice(0, lit).forEach(nm => { if (sharp && (nm[0] === 'E' || nm[0] === 'B')) o[kidx(nm)] = prettyNote(nm); }); return o; })() : null;")
rep("<div style={{maxWidth:300,margin:'0 auto'}}><TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels/></div>\n    <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#5a5d8f',minHeight:20,marginTop:6}}>",
    "<div style={{maxWidth:300,margin:'0 auto'}}><TapKeyboard octaves={1} marks={marks} labels=\"all\" bigLabels extraC={sharp} trail={trail} trailLabels={trailLabels}/></div>\n    <div style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#5a5d8f',minHeight:20,marginTop:6}}>")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
