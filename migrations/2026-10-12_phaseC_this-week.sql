-- Phase C: "This week" -- the student's own ticks on their homework are saved, so the teacher sees them
-- Run ONCE in Supabase > SQL Editor > New query > paste all > Run. Safe to run again.
-- Run phaseA1, phaseB1, phaseB2 and phaseB3 first -- you already did.
--
-- Adds:
--   table homework_ticks        one row per homework line the student ticked, for one lesson
--                               (the lesson's date + the line exactly as written under Log lesson > "For the student")
--   pb_hw_tick(token, lesson_date, item, on)   the student ticks / unticks a line on their Today page
-- Changes:
--   pb_student_today(token)     same as before (phaseB2), plus  ticks: ["Ledger Lines [chapter:ledger-lines]", ...]
--                               = the lines ticked for the lesson that is shown
-- Chapters played in the app tick themselves without this table (the dashboard reads practice_log for that).
-- The teacher dashboard reads homework_ticks with the teacher's own login (row level security, own students only).
-- Students never read tables: they only call these functions with the secret token from their link.

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
    create table if not exists public.homework_ticks (
      student_id   %s not null references public.students(id) on delete cascade,
      lesson_date  date not null,
      item         text not null check (char_length(item) between 1 and 220),
      at           timestamptz not null default now(),
      primary key (student_id, lesson_date, item)
    )$f$, idtype);
end $$;

alter table public.homework_ticks enable row level security;
revoke all on public.homework_ticks from anon;

drop policy if exists homework_ticks_select on public.homework_ticks;
drop policy if exists homework_ticks_delete on public.homework_ticks;

-- the teacher can read (and clear) the ticks of their own students; nobody inserts directly
create policy homework_ticks_select on public.homework_ticks
  for select to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));

create policy homework_ticks_delete on public.homework_ticks
  for delete to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));

-- the ticked lines for one student and one lesson, as json (internal helper)
create or replace function public.pb_ticks_json(p_sid text, p_date date)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  select coalesce(jsonb_agg(t.item order by t.at), '[]'::jsonb)
  from public.homework_ticks t
  where t.student_id::text = p_sid and t.lesson_date = p_date;
$$;
revoke all on function public.pb_ticks_json(text, date) from public;

create or replace function public.pb_hw_tick(p_token text, p_lesson_date date, p_item text, p_on boolean)
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
  if p_lesson_date is null or p_lesson_date < current_date - 120 or p_lesson_date > current_date + 2 then
    return jsonb_build_object('ok', false, 'reason', 'day');
  end if;
  if p_item is null or char_length(p_item) < 1 or char_length(p_item) > 220 then
    return jsonb_build_object('ok', false, 'reason', 'item');
  end if;
  if coalesce(p_on, false) then
    -- a homework list has at most 12 lines; 30 leaves room for a teacher who edits the lines during the week
    if (select count(*) from public.homework_ticks where student_id = v_sid and lesson_date = p_lesson_date) >= 30 then
      return jsonb_build_object('ok', false, 'reason', 'full');
    end if;
    insert into public.homework_ticks (student_id, lesson_date, item)
    values (v_sid, p_lesson_date, p_item)
    on conflict (student_id, lesson_date, item) do nothing;
  else
    delete from public.homework_ticks t
    where t.student_id = v_sid and t.lesson_date = p_lesson_date and t.item = p_item;
  end if;
  -- old weeks are not needed for long
  delete from public.homework_ticks t where t.student_id = v_sid and t.lesson_date < current_date - 120;
  return jsonb_build_object('ok', true, 'ticks', public.pb_ticks_json(v_sid::text, p_lesson_date));
end;
$$;

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
  v_day  date;
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

  if v_hw is not null then
    begin
      v_day := left(v_date, 10)::date;
    exception when others then
      v_day := null;
    end;
  end if;

  return jsonb_build_object(
    'name',       v_link.display_name,
    'lesson',     case when v_hw is null then null else jsonb_build_object('date', v_date, 'homework', v_hw) end,
    'ticks',      case when v_day is null then '[]'::jsonb else public.pb_ticks_json(v_link.student_id::text, v_day) end,
    'pieces',     public.pb_pieces_json(v_link.student_id::text),
    'checkins',   public.pb_checkins_json(v_link.student_id::text),
    'server_day', current_date
  );
end;
$$;

revoke all on function public.pb_student_today(text) from public;
revoke all on function public.pb_hw_tick(text, date, text, boolean) from public;
grant execute on function public.pb_student_today(text) to anon, authenticated;
grant execute on function public.pb_hw_tick(text, date, text, boolean) to anon, authenticated;

notify pgrst, 'reload schema';
