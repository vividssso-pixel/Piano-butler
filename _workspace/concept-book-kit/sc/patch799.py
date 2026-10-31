"""Build DW, call 40 (her 31 Oct 10:5x '40번 좋아'; asked 'what is MAKE YOUR OWN for? the whole thing has to be fun, and it
should all live in the lessons and drills'): each room's make-it toy moves out of the MAKE YOUR OWN card at the room's end
and into the step that teaches what it needs, open right there under the step's own activities ('Now make your own').
The end card goes. Where the toy was already in a step (Black-key jam, the Grade 6 to 8 pads, Viva cards, the map of my
piece) only the end card's copy goes. The drills stay the checks."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# 1. where each toy goes: room -> { step position: [tool ids] } (the position as the steps show, from 0)
R("""const MAKE_EXTRA = { 'first-steps': ['black-key-jam'], rhythm: ['make-card'], 'key-signatures': ['transpose'], form: ['form-builder'], melody: ['draw-tune'] };   // Build CB: made before the mk- toys""",
  """const MAKE_EXTRA = { 'first-steps': ['black-key-jam'], rhythm: ['make-card'], 'key-signatures': ['transpose'], form: ['form-builder'], melody: ['draw-tune'] };   // Build CB: made before the mk- toys
// Build DW (call 40): each toy in the step that teaches what it needs. Already in a step, so not here: black-key-jam (First
// steps 4), mk-two, mk-wave, mk-poly, mk-cad (their Grade 6 pages), mk-viva and mk-map (their own steps).
const MAKE_AT = {
  'posture-hands': { 2: ['mk-pianist'] }, pulse: { 2: ['mk-band'] }, 'note-names': { 5: ['mk-word'] }, 'hand-positions': { 2: ['mk-move'] },
  'ear-prep': { 2: ['mk-trick'] }, 'note-values': { 4: ['mk-ways'] }, dynamics: { 1: ['mk-dyn'] }, staff: { 1: ['mk-lines'] },
  'reading-steps': { 2: ['mk-qa'] }, 'whole-staff': { 2: ['mk-staffword'] }, 'time-signatures': { 2: ['mk-gtime'] }, tones: { 2: ['mk-steps'] },
  'listen-sing': { 3: ['mk-exam'] }, tempo: { 1: ['mk-tempo'] }, rhythm: { 4: ['make-card'] }, 'ledger-lines': { 4: ['mk-ladders'] },
  scales: { 4: ['mk-keytune'] }, 'scale-play': { 1: ['mk-remix'] }, 'minor-scales': { 0: ['mk-mm'] }, signs: { 3: ['mk-road'] },
  'listen-write': { 0: ['mk-hang'] }, accidentals: { 0: ['mk-acc'] }, 'key-signatures': { 4: ['transpose'] }, terms: { 3: ['mk-recipe'] },
  'six-eight': { 4: ['mk-e8'] }, intervals: { 2: ['mk-iv'] }, chords: { 3: ['mk-loop'] }, form: { 3: ['form-builder'] },
  'listen-23': { 0: ['mk-hidden'] }, melody: { 0: ['draw-tune'] }, 'scales-23': { 2: ['mk-melmin'] }, 'listen-3': { 4: ['mk-duel'] },
  'harmony-3': { 2: ['mk-choir'] }, 'rhythm-3': { 0: ['mk-split'] }, 'listen-4': { 0: ['mk-bingo'] }, 'scales-4': { 0: ['mk-four4'] },
  'keys-4': { 5: ['mk-anykey'] }, 'harmony-4': { 3: ['mk-tunechords'] }, 'rhythm-4': { 0: ['mk-offbeat'] }, 'listen-5': { 2: ['mk-triad'] },
  'scales-5': { 1: ['mk-dj'] }, 'keys-5': { 3: ['mk-flip'] }, 'harmony-5': { 2: ['mk-decor'] }, 'listen-7': { 2: ['mk-mem'] },
  'scales-7': { 6: ['mk-mode'] }, 'arps-7': { 0: ['mk-accomp'] }, 'listen-8': { 0: ['mk-colour'] }, 'scales-8': { 2: ['mk-thirds'] },
  'arps-8': { 3: ['mk-fourkeys'] }, 'piano-story': { 1: ['mk-surprise'] }, 'pitch-range': { 3: ['mk-who'] }, composers: { 4: ['mk-first'] },
  styles: { 4: ['mk-sty'] },
};
// in a step, the maker alone: the explanations before it are the step's own
const MAKE_BARE = { 'make-card': () => <RhythmComposer/>, transpose: () => <Transposer/> };
function StepMake({ ids }) {
  return <>{ids.map(x => { const tl = TOOLS.find(y => y.id === x); if (!tl) return null; const C = MAKE_BARE[x] || tl.C;
    return <div key={x} data-step-make={x} style={{margin:'14px 0 6px',paddingTop:10,borderTop:'1.5px dashed rgba(38,41,107,0.28)',minWidth:0}}>
      <div style={{fontSize:11.5,fontWeight:900,color:'#e4572e',letterSpacing:'0.1em',textTransform:'uppercase',margin:'0 0 6px'}}>{t('Now make your own', '이제 직접 만들어 봐요')}</div>
      <C/>
    </div>; })}</>;
}""")
# 2. the step draws them under its own activities, before Got it
R("""function Step({ n, total, title, color, open, done, onToggle, onDone, children, id, bookExtra }) {""",
  """function Step({ n, total, title, color, open, done, onToggle, onDone, children, id, bookExtra, make }) {""")
R("""          <StepCtx.Provider value={color}>{children}</StepCtx.Provider>
          <div style={{textAlign:'right',margin:'4px 0 2px'}}>""",
  """          <StepCtx.Provider value={color}>{children}{make && <StepMake ids={make}/>}</StepCtx.Provider>
          <div style={{textAlign:'right',margin:'4px 0 2px'}}>""")
R("""        open: !!open[i], done: !!done[sk(i)], onToggle: () => setOpen(o => (o[i] ? {} : { [i]: true })), onDone: () => markDone(i),
      }))}""",
  """        open: !!open[i], done: !!done[sk(i)], onToggle: () => setOpen(o => (o[i] ? {} : { [i]: true })), onDone: () => markDone(i),
        make: (MAKE_AT[id] || {})[i],
      }))}""")
# 3. the end card goes; the 'More to play with' chips stay (the toys are not among them)
R("""  if (!list.length) return <LessonMake id={id}/>;
  return <><LessonMake id={id}/><div style={{margin:'14px 0 0',padding:'10px 12px',border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,background:'#fff'}}>""",
  """  if (!list.length) return null;   // Build DW: the MAKE YOUR OWN card is gone; its toys live in their steps
  return <><div style={{margin:'14px 0 0',padding:'10px 12px',border:'1px solid rgba(38,41,107,0.16)',borderRadius:10,background:'#fff'}}>""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok call 40', len(s))
