// ---------------------------------------------------------------------------
// A tiny fairness gate for Render's single 0.1-vCPU instance (2026-09-16).
//
// Found via a live test right after Phase 80 shipped: the excerpt pool's
// background refill loop and a real visitor's live request could run their
// LilyPond compiles genuinely concurrently (two separate child processes
// racing for the same tenth-of-a-core), which made a slow request even
// slower than before the pool existed -- the opposite of the intent.
//
// This gate makes sure only ONE compile "unit of work" (a full excerpt
// build, a lazy hands-view render, or the boot-time font-cache warm-up)
// runs at a time system-wide, and a live visitor's own request always
// jumps the queue ahead of any background excerptPool refill work still
// waiting its turn.
//
// Limits, stated plainly: this cannot preempt a job that has ALREADY
// started -- a visitor whose click lands the instant a background compile
// begins still has to wait for that one to finish first. It also doesn't
// reach into compileExcerpt's own fire-and-forget follow-up work (the
// deferred full-page PDF compile and audio render kicked off after the
// gated call already returned) -- those were deliberately made
// non-blocking in Phases 77/78 and can still overlap with a next gated
// job. What this DOES fix is the compounding case: multiple background
// refills, or a background refill AND a live request, both actively
// compiling the primary preview at once.
// ---------------------------------------------------------------------------

let busy = false;
const liveQueue = [];
const backgroundQueue = [];

function pump() {
  if (busy) return;
  const job = liveQueue.shift() || backgroundQueue.shift();
  if (!job) return;
  busy = true;
  Promise.resolve()
    .then(job.task)
    .then(job.resolve, job.reject)
    .finally(() => {
      busy = false;
      pump();
    });
}

// priority: 'live' (jumps ahead of any queued background work) or
// 'background' (default) -- never preempts a job already running.
function runGated(task, priority = 'background') {
  return new Promise((resolve, reject) => {
    (priority === 'live' ? liveQueue : backgroundQueue).push({ task, resolve, reject });
    pump();
  });
}

module.exports = { runGated };
