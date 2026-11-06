#!/usr/bin/env python3
"""Phase 453 (This week): patch drills.src.html. Usage: patch_drills.py <drills.src.html>
Each replacement must match exactly once, or the script stops without writing."""
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()

def rep(old, new):
    global s
    n = s.count(old)
    if n != 1:
        sys.exit('anchor found %d times: %r' % (n, old[:80]))
    s = s.replace(old, new)

# 1. header comment + keys
rep("""// Ticks on homework lines are this device's own memory (the teacher does not see them).
""", """// Phase 451 ("This week"): ticks on homework lines are saved through the link (pb_hw_tick, table homework_ticks) so the
// teacher sees them; this device keeps a copy and a list of ticks not saved yet (sent again on the next visit). A chapter
// line ticks itself once that chapter has been played in the app since the lesson day (the dashboard does the same from practice_log).
// An older database without pb_hw_tick: ticks simply stay on this device, as before.
""")
rep("""const TODAY_CACHE_KEY = 'pb_today_cache_v1', TODAY_TICKS_KEY = 'pb_today_ticks_v1';
""", """const TODAY_CACHE_KEY = 'pb_today_cache_v1', TODAY_TICKS_KEY = 'pb_today_ticks_v1';
const TODAY_DIRTY_KEY = 'pb_today_ticks_dirty_v1', TODAY_SYNCED_KEY = 'pb_today_ticks_synced_v1';
""")

# 2. helpers
rep("""function loadTicks() { try { const o = JSON.parse(localStorage.getItem(TODAY_TICKS_KEY)); return o && typeof o === 'object' ? o : {}; } catch (e) { return {}; } }
""", """function loadTicks() { try { const o = JSON.parse(localStorage.getItem(TODAY_TICKS_KEY)); return o && typeof o === 'object' ? o : {}; } catch (e) { return {}; } }
function loadObj(key) { try { const o = JSON.parse(localStorage.getItem(key)); return o && typeof o === 'object' && !Array.isArray(o) ? o : {}; } catch (e) { return {}; } }
function saveObj(key, o) { try { localStorage.setItem(key, JSON.stringify(o)); } catch (e) {} }
// the first time (ms) a drill of this chapter was played on or after the lesson day, or 0 (drill records are synced between devices)
function playedSince(drillId, lessonDate) {
  const d = dayDate(lessonDate); if (!d) return 0;
  const from = new Date(d.getFullYear(), d.getMonth(), d.getDate(), 0, 0, 0).getTime();
  let first = 0;
  const all = loadRecords();
  Object.keys(all).forEach(k => {
    if (k.split('|')[0] !== drillId) return;
    const r = all[k] || {};
    const times = (Array.isArray(r.history) ? r.history.map(h => h && +h.at) : []).concat([+r.lastAt]);
    times.forEach(at => { if (at && at >= from && (!first || at < first)) first = at; });
  });
  return first;
}
""")

# 3. merge the server's ticks after a load
rep("""        setData(r.data); setStatus('ok'); keep(r.data);
      });
    }
    load();""", """        setData(r.data); setStatus('ok'); keep(r.data);
        mergeServerTicks(r.data);
      });
    }
    load();""")

# 4. toggle saves + flush
rep("""  function toggleTick(k, date) {
    const n = { ...ticks };
    if (n[k]) delete n[k]; else n[k] = 1;
    const keepPrefix = who + '|' + date + '|';
    Object.keys(n).forEach(x => { if (x.indexOf(who + '|') === 0 && x.indexOf(keepPrefix) !== 0) delete n[x]; });
    setTicks(n);
    try { localStorage.setItem(TODAY_TICKS_KEY, JSON.stringify(n)); } catch (e) {}
  }
""", """  // keep only this lesson's keys of this student (other students' keys on a shared device stay)
  function prune(o, prefix) { Object.keys(o).forEach(x => { if (x.indexOf(who + '|') === 0 && x.indexOf(prefix) !== 0) delete o[x]; }); return o; }
  function toggleTick(k, date) {
    const prefix = who + '|' + date + '|';
    const n = prune({ ...loadTicks() }, prefix);
    if (n[k]) delete n[k]; else n[k] = 1;
    setTicks(n); saveObj(TODAY_TICKS_KEY, n);
    const dirty = prune(loadObj(TODAY_DIRTY_KEY), prefix); dirty[k] = 1; saveObj(TODAY_DIRTY_KEY, dirty);
    flushTicks(date);
  }
  // the server's ticks for the lesson shown win, except for ticks not saved yet; the first time, this device's own ticks are sent up
  function mergeServerTicks(d) {
    if (!d || !d.lesson || !d.lesson.date || !Array.isArray(d.ticks)) return; // no homework, or an older database
    const date = d.lesson.date, prefix = who + '|' + date + '|';
    const n = prune({ ...loadTicks() }, prefix), dirty = prune(loadObj(TODAY_DIRTY_KEY), prefix), synced = loadObj(TODAY_SYNCED_KEY);
    if (!synced[who]) { Object.keys(n).forEach(k => { if (k.indexOf(prefix) === 0) dirty[k] = 1; }); synced[who] = 1; saveObj(TODAY_SYNCED_KEY, synced); }
    Object.keys(n).forEach(k => { if (k.indexOf(prefix) === 0 && !dirty[k]) delete n[k]; });
    d.ticks.forEach(item => { if (typeof item === 'string' && !dirty[prefix + item]) n[prefix + item] = 1; });
    setTicks(n); saveObj(TODAY_TICKS_KEY, n); saveObj(TODAY_DIRTY_KEY, dirty);
    flushTicks(date);
  }
  const flushing = useRef(false);
  async function flushTicks(date) {
    if (flushing.current) { flushing.current = 'again'; return; }
    flushing.current = true;
    const prefix = who + '|' + date + '|';
    for (;;) {
      const dirty = loadObj(TODAY_DIRTY_KEY), keys = Object.keys(dirty).filter(k => k.indexOf(prefix) === 0);
      if (!keys.length) break;
      const k = keys[0];
      const r = await pbRpc('pb_hw_tick', { p_token: token, p_lesson_date: String(date).slice(0, 10), p_item: k.slice(prefix.length), p_on: !!loadTicks()[k] });
      if (!r.ok || !r.data) break; // offline, or the database has no pb_hw_tick yet: try again next time
      const d2 = loadObj(TODAY_DIRTY_KEY);
      if (r.data.ok || r.data.reason === 'item' || r.data.reason === 'day' || r.data.reason === 'full') { delete d2[k]; saveObj(TODAY_DIRTY_KEY, d2); }
      else break; // the link is not active
    }
    const again = flushing.current === 'again';
    flushing.current = false;
    if (again) flushTicks(date);
  }
""")

# 5. the card: kicker "This week", x of n, bar, auto-done lines
rep("""  const items = lesson ? homeworkItems(lesson.homework) : [];
""", """  const items = (lesson ? homeworkItems(lesson.homework) : []).map(it => {
    const k = who + '|' + lesson.date + '|' + it.key;
    const auto = it.kind === 'chapter' ? playedSince(it.id, lesson.date) : 0;
    return { ...it, k, auto, on: !!auto || !!ticks[k] };
  });
  const nDoneHw = items.filter(it => it.on).length;
""")
rep("""          <div style={kicker}>{lesson ? t('From your last lesson', '지난 레슨에서') + (lessonLabel ? ' · ' + lessonLabel : '') : t('From your teacher', '선생님이 올려준 것')}</div>
""", """          <div style={{ ...kicker, display: 'flex', justifyContent: 'space-between', gap: 8 }}>
            <span>{lesson ? t('This week', '이번 주') + (lessonLabel ? ' · ' + t('lesson on ', '') + lessonLabel + t('', ' 레슨') : '') : t('From your teacher', '선생님이 올려준 것')}</span>
            {items.length > 0 && <span data-testid="hw-count" style={{ color: nDoneHw === items.length ? 'var(--good)' : 'var(--coral)', whiteSpace: 'nowrap' }}>{t(nDoneHw + ' of ' + items.length + ' done', items.length + '개 중 ' + nDoneHw + '개')}</span>}
          </div>
          {items.length > 0 && <div aria-hidden="true" style={{ height: 6, borderRadius: 4, background: 'var(--navy-line)', margin: '-2px 0 12px', overflow: 'hidden' }}><i style={{ display: 'block', height: '100%', width: Math.round(100 * nDoneHw / items.length) + '%', background: nDoneHw === items.length ? 'var(--good)' : 'var(--coral)', transition: 'width .3s' }} /></div>}
""")
rep("""          {items.map((it, i) => {
            const k = who + '|' + lesson.date + '|' + it.key, on = !!ticks[k];
            return (
              <div key={i} style={{ display: 'flex', gap: 12, alignItems: 'flex-start', padding: '10px 0', borderTop: i ? '1px solid var(--navy-line)' : 'none', paddingTop: i ? 10 : 0 }}>
                <button role="checkbox" aria-checked={on} aria-label={it.text} onClick={() => toggleTick(k, lesson.date)} style={{ flex: '0 0 28px', width: 28, height: 28, borderRadius: 8, border: '2px solid ' + (on ? 'var(--good)' : 'var(--navy)'), background: on ? 'var(--good)' : 'transparent', color: '#fff', fontWeight: 900, fontSize: 16, lineHeight: 1, cursor: 'pointer', padding: 0, marginTop: 1 }}>{on ? '✓' : ''}</button>
                <span style={{ fontSize: 15.5, lineHeight: 1.35, color: on ? 'var(--muted)' : 'var(--navy)', fontWeight: 600, textDecoration: on ? 'line-through' : 'none', minWidth: 0, flex: 1, overflowWrap: 'anywhere' }}>{it.text}</span>
                {it.kind && <button""", """          {items.map((it, i) => {
            const k = it.k, on = it.on;
            return (
              <div key={i} data-testid="hw-item" style={{ display: 'flex', gap: 12, alignItems: 'flex-start', padding: '10px 0', borderTop: i ? '1px solid var(--navy-line)' : 'none', paddingTop: i ? 10 : 0 }}>
                <button role="checkbox" aria-checked={on} aria-label={it.text} disabled={!!it.auto} title={it.auto ? t('Done in the app', '앱에서 완료') : undefined} onClick={() => toggleTick(k, lesson.date)} style={{ flex: '0 0 28px', width: 28, height: 28, borderRadius: 8, border: '2px solid ' + (on ? 'var(--good)' : 'var(--navy)'), background: on ? 'var(--good)' : 'transparent', color: '#fff', fontWeight: 900, fontSize: 16, lineHeight: 1, cursor: it.auto ? 'default' : 'pointer', padding: 0, marginTop: 1, opacity: 1 }}>{on ? '✓' : ''}</button>
                <span style={{ minWidth: 0, flex: 1 }}><span style={{ display: 'block', fontSize: 15.5, lineHeight: 1.35, color: on ? 'var(--muted)' : 'var(--navy)', fontWeight: 600, textDecoration: on ? 'line-through' : 'none', overflowWrap: 'anywhere' }}>{it.text}</span>{it.auto ? <span data-testid="hw-auto" style={{ display: 'block', fontSize: 12, fontWeight: 800, color: 'var(--good)', marginTop: 2 }}>{t('Done in the app ✓', '앱에서 완료 ✓')}</span> : null}</span>
                {it.kind && <button""")
rep("""          {items.length === 0 && <div style={{ fontSize: 15, color: 'var(--muted)', lineHeight: 1.4 }}>{t('No homework yet. Your teacher will add it after your next lesson.', '아직 숙제가 없어요. 다음 레슨 후에 선생님이 올려줄 거예요.')}</div>}
""", """          {items.length === 0 && <div style={{ fontSize: 15, color: 'var(--muted)', lineHeight: 1.4 }}>{t('No homework yet. Your teacher will add it after your next lesson.', '아직 숙제가 없어요. 다음 레슨 후에 선생님이 올려줄 거예요.')}</div>}
          {items.length > 0 && <div style={{ fontSize: 12, color: 'var(--muted)', margin: '0 0 12px', lineHeight: 1.4 }}>{t('Tick what you finish. Your teacher sees it. Chapters tick themselves when you play them.', '끝낸 것을 체크해요. 선생님도 볼 수 있어요. 챕터는 앱에서 하면 저절로 체크돼요.')}</div>}
""")

open(p, 'w', encoding='utf-8').write(s)
print('patched', p)
