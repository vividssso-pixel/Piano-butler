-- Phase A1: student links
-- Run ONCE in Supabase > SQL Editor > New query > paste all > Run. Safe to run again.
-- Creates: table student_links, its row level security, and the function pb_student_info(token).
-- Does not change any existing table. Students never read tables directly: the drills page
-- calls pb_student_info with the secret token from the student's link.

do $$
declare idtype text;
begin
  select format_type(a.atttypid, a.atttypmod) into idtype
  from pg_attribute a
  where a.attrelid = 'public.students'::regclass and a.attname = 'id' and not a.attisdropped;
  if idtype is null then
    raise exception 'public.students.id was not found';
  end if;
  execute format($f$
    create table if not exists public.student_links (
      student_id   %s primary key references public.students(id) on delete cascade,
      teacher_id   uuid not null default auth.uid() references auth.users(id) on delete cascade,
      display_name text not null check (char_length(display_name) between 1 and 40),
      token        text not null unique check (char_length(token) >= 32),
      active       boolean not null default true,
      created_at   timestamptz not null default now(),
      revoked_at   timestamptz
    )$f$, idtype);
end $$;

alter table public.student_links enable row level security;
revoke all on public.student_links from anon;

drop policy if exists student_links_select on public.student_links;
drop policy if exists student_links_insert on public.student_links;
drop policy if exists student_links_update on public.student_links;
drop policy if exists student_links_delete on public.student_links;

create policy student_links_select on public.student_links
  for select to authenticated
  using (teacher_id = auth.uid());

create policy student_links_insert on public.student_links
  for insert to authenticated
  with check (
    teacher_id = auth.uid()
    and exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid())
  );

create policy student_links_update on public.student_links
  for update to authenticated
  using (teacher_id = auth.uid())
  with check (
    teacher_id = auth.uid()
    and exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid())
  );

create policy student_links_delete on public.student_links
  for delete to authenticated
  using (teacher_id = auth.uid());

-- What the drills page asks when a student opens their link. Returns only the display name
-- (a first name or nickname), and only for an active link.
create or replace function public.pb_student_info(p_token text)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select jsonb_build_object('name', l.display_name)
  from public.student_links l
  where char_length(p_token) >= 32 and l.token = p_token and l.active
  limit 1;
$$;

revoke all on function public.pb_student_info(text) from public;
grant execute on function public.pb_student_info(text) to anon, authenticated;

notify pgrst, 'reload schema';
