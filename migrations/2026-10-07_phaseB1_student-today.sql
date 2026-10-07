-- Phase B1: the student's "Today" page and the daily practice check
-- Run ONCE in Supabase > SQL Editor > New query > paste all > Run. Safe to run again.
-- Run phaseA1 (student links) first -- you already did.
--
-- Adds:
--   table practice_checkins   one row per student per day ("I practised today", optional minutes)
--   pb_student_today(token)   what a student sees on Today: name, the homework from the latest lesson log,
--                             and the last 3 weeks of check-ins. Nothing else from the lesson log is returned
--                             (never the notes, mood or ratings).
--   pb_checkin(token, day, minutes) / pb_uncheck(token, day)   the student taps / undoes today
-- The teacher dashboard reads practice_checkins with the teacher's own login (row level security).
-- Students never read tables: they only call these functions with the secret token from their link.
-- The homework text is written in the dashboard (Log lesson > "For the student") and stored in
-- lesson_logs.extra (the existing text column), so lesson_logs itself is not changed.

-- turns text (or jsonb) into jsonb, or null when it is empty or not valid JSON
create or replace function public.pb_safe_jsonb(p text)
returns jsonb
language plpgsql
immutable
as $$
begin
  if p is null or btrim(p) = '' then return null; end if;
  return p::jsonb;
exception when others then
  return null;
end;
$$;
revoke all on function public.pb_safe_jsonb(text) from public;

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
    create table if not exists public.practice_checkins (
      student_id  %s not null references public.students(id) on delete cascade,
      day         date not null,
      minutes     integer check (minutes is null or minutes between 1 and 600),
      created_at  timestamptz not null default now(),
      primary key (student_id, day)
    )$f$, idtype);
end $$;

alter table public.practice_checkins enable row level security;
revoke all on public.practice_checkins from anon;

drop policy if exists practice_checkins_select on public.practice_checkins;
drop policy if exists practice_checkins_delete on public.practice_checkins;

-- the teacher can read (and correct, by deleting) the check-ins of their own students; nobody inserts directly
create policy practice_checkins_select on public.practice_checkins
  for select to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));

create policy practice_checkins_delete on public.practice_checkins
  for delete to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));

-- the last 3 weeks of check-ins for one student, as json (internal helper)
create or replace function public.pb_checkins_json(p_sid text)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select coalesce(
    jsonb_agg(jsonb_build_object('day', c.day, 'minutes', c.minutes) order by c.day),
    '[]'::jsonb)
  from public.practice_checkins c
  where c.student_id::text = p_sid and c.day >= current_date - 21;
$$;
revoke all on function public.pb_checkins_json(text) from public;

create or replace function public.pb_student_today(p_token text)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $$
declare
  v_link public.student_links%rowtype;
  v_date text;
  v_hw   text;
begin
  if p_token is null or char_length(p_token) < 32 then return null; end if;
  select * into v_link from public.student_links where token = p_token and active;
  if not found then return null; end if;

  -- the latest lesson (not an absence) that has homework written for the student
  select l.date::text, e.hw into v_date, v_hw
  from public.lesson_logs l
  cross join lateral (select public.pb_safe_jsonb(l.extra::text) as j) x
  cross join lateral (select left(btrim(x.j ->> 'homework'), 2000) as hw,
                             coalesce(x.j ->> 'type', 'regular') as ty) e
  where l.student_id::text = v_link.student_id::text
    and e.ty <> 'absent'
    and e.hw is not null and e.hw <> ''
  order by l.date desc, l.id desc
  limit 1;

  return jsonb_build_object(
    'name',       v_link.display_name,
    'lesson',     case when v_hw is null then null else jsonb_build_object('date', v_date, 'homework', v_hw) end,
    'checkins',   public.pb_checkins_json(v_link.student_id::text),
    'server_day', current_date
  );
end;
$$;

create or replace function public.pb_checkin(p_token text, p_day date, p_minutes integer default null)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_sid public.student_links.student_id%type;
begin
  if p_token is null or char_length(p_token) < 32 then
    return jsonb_build_object('ok', false, 'reason', 'link');
  end if;
  select l.student_id into v_sid from public.student_links l where l.token = p_token and l.active;
  if not found then return jsonb_build_object('ok', false, 'reason', 'link'); end if;
  -- the student's own date can differ from the server's by a day or so (time zones)
  if p_day is null or p_day < current_date - 2 or p_day > current_date + 2 then
    return jsonb_build_object('ok', false, 'reason', 'day');
  end if;
  if p_minutes is not null and (p_minutes < 1 or p_minutes > 600) then
    return jsonb_build_object('ok', false, 'reason', 'minutes');
  end if;
  insert into public.practice_checkins (student_id, day, minutes)
  values (v_sid, p_day, p_minutes)
  on conflict (student_id, day) do update set minutes = excluded.minutes;
  return jsonb_build_object('ok', true, 'checkins', public.pb_checkins_json(v_sid::text));
end;
$$;

create or replace function public.pb_uncheck(p_token text, p_day date)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_sid public.student_links.student_id%type;
begin
  if p_token is null or char_length(p_token) < 32 then
    return jsonb_build_object('ok', false, 'reason', 'link');
  end if;
  select l.student_id into v_sid from public.student_links l where l.token = p_token and l.active;
  if not found then return jsonb_build_object('ok', false, 'reason', 'link'); end if;
  if p_day is null or p_day < current_date - 2 or p_day > current_date + 2 then
    return jsonb_build_object('ok', false, 'reason', 'day');
  end if;
  delete from public.practice_checkins c where c.student_id = v_sid and c.day = p_day;
  return jsonb_build_object('ok', true, 'checkins', public.pb_checkins_json(v_sid::text));
end;
$$;

revoke all on function public.pb_student_today(text) from public;
revoke all on function public.pb_checkin(text, date, integer) from public;
revoke all on function public.pb_uncheck(text, date) from public;
grant execute on function public.pb_student_today(text) to anon, authenticated;
grant execute on function public.pb_checkin(text, date, integer) to anon, authenticated;
grant execute on function public.pb_uncheck(text, date) to anon, authenticated;

notify pgrst, 'reload schema';
