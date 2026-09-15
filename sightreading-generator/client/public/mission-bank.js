// Mission Bank browsing page (2026-09-03) -- the single "saved excerpts"
// library, absorbing what used to be a separate "Explorer Bank" (a
// manually-curated famous-piece library that turned out to duplicate this
// page's job: being a place to keep pieces). Every card here is something
// the Generator actually produced and a teacher chose to keep, via
// POST /api/mission-bank (see app.js's saveToMissionBank).

const grid = document.getElementById('grid');
const search = document.getElementById('search');
const gradeFilter = document.getElementById('gradeFilter');

let allItems = []; // unfiltered, so the grade filter's option list never shrinks based on the current filter

async function loadList() {
  const res = await fetch('/api/mission-bank');
  const data = await res.json();
  allItems = data.items || [];
  updateGradeOptions(allItems);
  renderGrid(filterItems(allItems));
}

function filterItems(items) {
  let out = items;
  const q = search.value.trim().toLowerCase();
  if (q) {
    out = out.filter(
      (i) => (i.studentName || '').toLowerCase().includes(q) || (i.notes || '').toLowerCase().includes(q)
    );
  }
  if (gradeFilter.value) {
    out = out.filter((i) => i.meta && i.meta.gradeId === gradeFilter.value);
  }
  return out;
}

function updateGradeOptions(items) {
  const grades = [];
  const seen = new Set();
  items.forEach((i) => {
    if (i.meta && i.meta.gradeId && !seen.has(i.meta.gradeId)) {
      seen.add(i.meta.gradeId);
      grades.push({ id: i.meta.gradeId, label: i.meta.gradeLabel || i.meta.gradeId });
    }
  });
  const current = gradeFilter.value;
  gradeFilter.innerHTML =
    '<option value="">Any grade</option>' +
    grades.map((g) => `<option value="${g.id}">${escapeHtml(g.label)}</option>`).join('');
  gradeFilter.value = current;
}

function renderGrid(items) {
  if (!items.length) {
    grid.innerHTML = `<div style="color:var(--muted);font-size:14px;grid-column:1/-1;">Nothing saved yet — generate an excerpt and click "Save to Mission Bank".</div>`;
    return;
  }
  grid.innerHTML = items
    .map((i) => {
      const meta = i.meta || {};
      const savedDate = i.savedAt ? new Date(i.savedAt).toLocaleDateString() : '';
      return `
    <div class="mission-card">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px;">
        <h3 style="margin:0 0 4px;">${escapeHtml(i.studentName || 'Unassigned')}</h3>
        <button class="delete-card-btn" data-id="${i.id}" title="Remove from Mission Bank" style="border:none;background:none;color:var(--muted);cursor:pointer;font-size:15px;line-height:1;padding:2px 4px;">✕</button>
      </div>
      <div class="sub">${escapeHtml(meta.gradeLabel || '')}${savedDate ? ` · ${savedDate}` : ''}</div>
      ${meta.key ? `<span class="pill">${escapeHtml(meta.key)}</span>` : ''}
      ${meta.timeSig ? `<span class="pill">${escapeHtml(meta.timeSig)}</span>` : ''}
      ${meta.barCount ? `<span class="pill">${escapeHtml(String(meta.barCount))} bars</span>` : ''}
      ${meta.feelSource ? `<span class="pill">🎯 ${escapeHtml(meta.feelSource)}</span>` : ''}
      <div style="margin-top:8px"><a href="/api/mission-bank/${i.id}/pdf" target="_blank">View score (PDF)</a></div>
      ${i.notes ? `<div class="notes">📝 ${escapeHtml(i.notes)}</div>` : ''}
    </div>`;
    })
    .join('');

  grid.querySelectorAll('.delete-card-btn').forEach((btn) => {
    btn.addEventListener('click', async () => {
      if (!confirm('Remove this excerpt from the Mission Bank?')) return;
      try {
        const res = await fetch(`/api/mission-bank/${btn.dataset.id}`, { method: 'DELETE' });
        if (!res.ok) throw new Error((await res.json()).error || 'delete failed');
        loadList();
      } catch (err) {
        alert(`Couldn't delete: ${err.message}`);
      }
    });
  });
}

function debounce(fn, ms) {
  let t;
  return (...args) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...args), ms);
  };
}
function escapeHtml(s) { return String(s).replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }

search.addEventListener('input', debounce(() => renderGrid(filterItems(allItems)), 250));
gradeFilter.addEventListener('change', () => renderGrid(filterItems(allItems)));

loadList();
