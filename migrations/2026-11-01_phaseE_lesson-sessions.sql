-- Phase E: the open lesson, shared between the teacher's devices (lesson mode, 2026-11-01)
-- Run ONCE in Supabase > SQL Editor > New query (name it "E lesson sessions") > paste all > Run. Safe to run again.
-- Run phaseA1, B1, B2, B3, C and D first (already done).
--
-- Adds: table lesson_sessions -- at most one row per teacher: the lesson that is open right now
--   (started on a student's page with "Start lesson", ended with "Save lesson", "Absent" or "Discard").
--   user_id    = the teacher (auth.uid())
--   student_id = the student's id, as text
--   name       = the student's first name, for the coral bar
--   shown      = what the materials noted: [{ "kind": "room"|"tool", "id": "...", "label": "...", "at": <ms> }]
-- The teacher reads and writes only their own row (dashboard and drills, with the teacher's login).
-- Students and visitors never see it. No email, age or lesson content beyond room and tool names.

create table if not exists public.lesson_sessions (
  user_id     uuid primary key default auth.uid() references auth.users(id) on delete cascade,
  student_id  text not null check (char_length(student_id) between 1 and 64),
  name        text not null default '' check (char_length(name) <= 40),
  started_at  timestamptz not null default now(),
  shown       jsonb not null default '[]'::jsonb check (jsonb_typeof(shown) = 'array' and jsonb_array_length(shown) <= 60),
  updated_at  timestamptz not null default now()
);

alter table public.lesson_sessions enable row level security;
revoke all on public.lesson_sessions from anon;
grant select, insert, update, delete on public.lesson_sessions to authenticated;

drop policy if exists lesson_sessions_own on public.lesson_sessions;
create policy lesson_sessions_own on public.lesson_sessions
  for all to authenticated
  using (user_id = auth.uid())
  with check (user_id = auth.uid());
