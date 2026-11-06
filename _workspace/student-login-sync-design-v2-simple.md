# Piano Butler: student links + progress tracking — design v2 (simple first)
Supersedes student-login-sync-design.md (v1). Decisions made with Sohyun on 2026-10-07.

## Scope (v1 = simple)
IN
- Personal student link (secret token in the URL fragment). No username/passphrase, no synthetic email accounts, no Edge Function.
- Opening the link on any device loads that student's progress; progress is saved back automatically.
- Student sees ALL chapters (no lock). Teacher posts "This week" items per student; shown pinned at the top. Auto-marked done from tracked plays.
- Teacher sees per-student progress (Progress Passport in teacher-dashboard.html).
- Pause / regenerate link / delete data per student.
OUT (later, only if needed)
- Chapter lock/unlock; per-question "most missed" tracking; syncing the Students-tab kits (stay on teacher's device);
  syncing voice recordings (pb_myvoice_v2 stays local); parent read-only link; multi-teacher sign-up.

## Phases (each ships alone)
0. Restore teacher login: auth.js + minimal login.html (Magic Link) from commit 1bccbd5^, so teacher-dashboard.html works again.
   (login.html/auth.js were deleted in Phase 54; the dashboard still requires them.)
A. SQL + dashboard "Create student link" (copy/pause/regenerate) + drills opens a student link and shows the student's name.
B. Sync: progress stores + practice log, merge rules, shared-device rule.
C. Passport view + "This week" items with auto-done.

## Data model (SQL goes in _workspace/ as a file; Sohyun runs it in the Supabase SQL editor)
student_links(student_id pk -> students, teacher_id, token text unique, active bool, created_at, revoked_at)
  - token stored in plain text, readable only by the owning teacher (RLS), so the link can be re-copied. Regenerate = new token, old dies.
progress_store(student_id, store, value jsonb, rev int, updated_at)  pk(student_id, store)
  stores: records | stamps | lesson_steps | steps_total | posture | arm_ex | last_chapter
practice_log(id, student_id, at, drill, level, mode, score, correct, total, secs)   append-only, one row per drill play
assignments(id, student_id, week_start date, kind (chapter|drill|tool), ref text, level int null, target_plays int, target_score int null, created_at)
Access:
- Students (anon key + token) never touch tables. They call SECURITY DEFINER functions that check the token is active:
  pb_get(token) -> name, stores, this week's assignments;  pb_save(token, store, value, rev);  pb_log(token, rows).
  Size limits on every write. No table policy exists for anon.
- Teacher (logged in): RLS, owner only (students.user_id = auth.uid()): read all of the above for own students, write student_links and assignments.
- Students cannot read students, lesson_logs, lesson_overrides or other students' rows.

## Client (drills)
- No supabase-js for students: plain fetch to the Supabase REST rpc endpoints with the anon key (zero library weight).
- Active only if the URL has #k=<token> or localStorage pb_link_token_v1 exists. Logged-out page unchanged; print routes (?book=) never run this code.
- Pull in the background after first paint; push debounced ~3 s after a change and on page hide; failures stay queued (dirty flag).
- Because some components read localStorage only at mount, after a pull that changes data the chapter view is remounted (no reload).
- Header shows the student's first name + "Not me" (switch/leave link). All UI strings en + ko via t().

## Merge rules (no data loss)
- First link open on a device with local progress and no owner tag: ask once "Add this device's practice to <name>?"; Yes -> import:
  plays summed, best = max, history union, stamps/steps/posture marks union. Then tag local data with pb_sync_owner_v1 = student id.
- Ongoing: plays = max(local, remote), best = max, history union by timestamp, stamps union, arm_ex/last_chapter latest wins.
- Different child's link on the same device: never merge. Switching pushes first, then clears synced keys; if the push fails, warn first.
- Practice log: append-only, de-duplicated by (at, drill, level, mode).

## "This week" auto-done
Teacher adds items (chapter/drill/tool, optional level, target N plays, optional min score) in the Passport. Done = count of practice_log rows
since week_start matching the item reaches target (and score if set). No manual ticking. Chapters/tools without a score count opens as 1 play.

## Teacher Passport (read-only + controls)
Streak, days practised (last 4 weeks), avg session, last practised; sessions per week; best score per drill/level/mode; scale stamps;
lesson steps done/total; recent sessions; This week items with progress; controls: copy link, pause, regenerate, delete data.

## Not changing
Preferences (language, sound, guide, solfa, find-all, books), teacher mode (pb_mode_v1), kits (pb_kits_v1, pb_who_v1) stay local.

## Flags for Sohyun (not blocking local build; decide before pushing real student data)
- Children's data: privacy.html wording, parent consent, Supabase region. No legal claims made here.
- Supabase free tier has no point-in-time backups; Pro ($25/mo) worth considering once students depend on it.
- Link = secret: anyone holding it can read/write that student's record. Low-sensitivity data only (no voice, no email). Revoke by regenerating.
- Build starts only after Sohyun confirms Phase 0 (restore teacher login) and this scope.
