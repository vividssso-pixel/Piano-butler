# Piano Butler: student login + progress sync — design (Step 1, no code yet)

## Finding that changes the plan
login.html and auth.js do NOT exist. Both were deleted in the Phase 54 cleanup (commit 1bccbd5; recoverable from 1bccbd5^).
teacher-dashboard.html still loads auth.js and calls requireAuth()/signOut(), which are defined nowhere else, so by file
evidence the dashboard cannot start today (not yet opened live; I will confirm in a browser before Phase A).
Supabase itself is alive (keep-alive workflow; project icefqxaccclwasnfzgnp). The old login was Magic Link by email, which
is the wrong tool for children. drills.html loads no Supabase code at all today (good: nothing to slow down).

## 0. Restore teacher login first (prerequisite, ships alone)
Restore auth.js (+ a minimal login.html, Magic Link as before) from 1bccbd5^. No drills change. Needed because the
Edge Function that creates student accounts must verify "this caller is the teacher".
Rec: yes, do it as Phase 0.

## 1. Kid login = (a) teacher-created account
- Teacher taps "Create login" on a student (dashboard StudentDetail). Edge Function `create-student-login`
  (service key stays server-side): verifies caller JWT, checks the students row belongs to the caller and has no login yet,
  then auth.admin.createUser with a synthetic email `<username>@students.thepianobutler.invalid`, email_confirm:true,
  password = generated 3-word passphrase (e.g. blue-piano-frog). Username = first name/nickname + 4 digits (unique, e.g. mia-4827).
  Returns username + passphrase ONCE; teacher hands them over. Teacher can reset (new passphrase) or unlink.
- Student logs in on drills with username + passphrase; the client builds the synthetic email. No email is ever sent.
- Stored about the child: first name/nickname (user_metadata.display_name) + progress. Nothing else.
- Check vs login.html: old flow was email Magic Link, so it cannot serve a child on a shared tablet; (a) confirmed.
- (b) parent magic link: possible later as an add-on for adults/parents. (c) anonymous + claim code: needs the same Edge
  Function anyway and a code is a weaker credential. Rejected.
- Trade-off to accept: no self-service password reset; teacher resets.
Rec: (a).

## 2. Linking to the teacher's students row + RLS
Add `students.student_user_id uuid unique null references auth.users(id) on delete set null`.
Students get NO access to `students`, `lesson_logs`, `lesson_overrides` (their auth.uid never equals a teacher user_id).
New table (created by the Edge Function, never by the student):
  progress_store(
    student_user_id uuid references auth.users on delete cascade,
    store text,                 -- records|stamps|lesson_steps|steps_total|posture|arm_ex|last_chapter
    value jsonb not null default '{}',
    rev int not null default 0,
    updated_at timestamptz default now(),
    teacher_id uuid not null references auth.users,
    student_id uuid not null references students(id) on delete cascade,
    primary key (student_user_id, store))
RLS: student SELECT/UPDATE where student_user_id = auth.uid(); teacher SELECT where teacher_id = auth.uid().
Students get column-level UPDATE on (value, rev, updated_at) only, so they cannot repoint teacher_id/student_id.
INSERT/DELETE by service role only. SQL goes in _workspace/ as a file for you to run.
Rec: as above.

## 3. Storage shape + merge
One jsonb row per store (7 rows per student), not one blob (blob = two devices overwrite each other) and not per-drill rows
(hundreds of rows, more requests). Client merges with a store-specific pure function, then writes with `rev` check
(retry once on conflict).
Correction to the "sum plays" lean: summing is right ONLY for the one-time import of anonymous local data. If it ran on every
sync it would double-count. So:
- First login import (once, guarded by owner tag, see 6): plays = local + remote; best = max; history = union by `at`, last 20;
  stamps/steps/posture marks = union.
- Ongoing sync: plays = max(local, remote); best = max; history union by `at`; stamps union (earliest kept);
  lesson steps union; arm_ex / last_chapter latest-write-wins by a local updatedAt.
- Not synced: steps_total is a derived cache but the teacher view needs it, so it IS synced (max per lesson).
Pull on load in the background; push debounced ~3 s after a change and on page hide; failures stay queued (dirty flag).
Risk to handle in the build: some components read localStorage only at mount, so after a pull I remount the chapter view
rather than reload.
Rec: as above.

## 4. Teacher view
Progress Passport in teacher-dashboard.html (it owns the students rows, the teacher login and RLS). Read-only v1:
last practised, plays this week, drills tried, best score per drill/level/mode, scale stamp grid, lesson steps done / total,
posture + arm exercise latest. Account controls (create, reset passphrase, unlink) live there too.
The drills Students tab (pb_kits_v1/pb_who_v1) stays device-local: it holds children's names and notes, which is also the
privacy-friendlier place for them. Later: a link from a kit to its dashboard student.
Rec: Passport in dashboard.

## 5. Phasing (each ships alone)
0. Restore teacher login (dashboard works again).
A. SQL + Edge Function + "Create login" in dashboard + student Log in / Log out UI in drills (no sync yet).
B. Sync (import on first login, pull/push, shared-device rule).
C. Passport view.

## 6. Shared tablets (not in your brief; needed)
Local storage is per browser, not per child. Tag it with pb_sync_owner_v1 = account id.
- Login with no owner tag and existing local progress: ask once "Add this device's practice to <name>'s account?" (Yes/No).
- Login when the tag is another child: never merge. Log-out pushes, then clears the synced keys; if the push fails,
  log-out warns first.
- Preferences (language, sound...) stay on the device either way.
Rec: as above.

## 7. Voice recordings (pb_myvoice_v2): recommend NOT syncing
They are base64 audio of children's voices: large (blows the free-tier DB), and more sensitive than scores. Keep local;
revisit later with Supabase Storage and parent consent.

## 8. Flags for you (no legal claims made)
- Children's data: does privacy.html need a section, do you want parent consent at account creation, which Supabase region?
- Turn off "Allow new users to sign up" in Supabase Auth once your teacher account exists (admin creation still works).
- Free tier has no point-in-time backups; once real students depend on it, Pro ($25/mo) is worth considering. Your call.
- Lazy loading: supabase-js is injected only if the sb-<project>-auth-token key exists or a student taps Log in; never on ?book= print routes.
