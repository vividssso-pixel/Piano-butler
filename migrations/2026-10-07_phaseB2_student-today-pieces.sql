-- Phase B2: the student's Today page also shows "pieces you're working on"
-- Run ONCE in Supabase > SQL Editor > New query > paste all > Run. Safe to run again.
-- Run phaseA1 and phaseB1 first -- you already did.
--
-- Changes one function and adds one internal helper:
--   pb_pieces_json(student)   the piece names from the latest lesson log (not an absence) whose Repertoire is not empty.
--                             Each line is one piece. The red / yellow / green rating mark at the start of a line is REMOVED,
--                             so ratings never leave the database. At most 12 pieces, 120 characters each.
--   pb_student_today(token)   same as before, plus  pieces: ["Minuet in G", ...]
-- Still never returned: the private notes, mood, ratings, technical work or anything else from the lesson log.
-- NOTE: whatever is typed in a Repertoire row (apart from the rating circle) is shown to the student.
-- If a lesson log has no Repertoire, the pieces from the previous lesson stay on the student's page.

create or replace function public.pb_pieces_json(p_sid text)
returns jsonb
language sql
stable
security definer
set search_path = public
as $$
  with latest as (
    select l.repertoire as rep
    from public.lesson_logs l
    cross join lateral (select coalesce(public.pb_safe_jsonb(l.extra::text) ->> 'type', 'regular') as ty) e
    where l.student_id::text = p_sid
      and e.ty <> 'absent'
      and btrim(regexp_replace(coalesce(l.repertoire, ''), '[🔴🟡🟢[:space:]]', '', 'g')) <> ''
    order by l.date desc, l.id desc
    limit 1
  ),
  lines as (
    select x.n,
           left(btrim(regexp_replace(x.line, '^([[:space:]]|🔴|🟡|🟢)+', '')), 120) as t
    from latest
    cross join lateral regexp_split_to_table(latest.rep, E'\r?\n') with ordinality as x(line, n)
  ),
  kept as (
    select t, n from lines where t <> '' order by n limit 12
  )
  select coalesce(jsonb_agg(t order by n), '[]'::jsonb) from kept;
$$;
revoke all on function public.pb_pieces_json(text) from public;

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
    'pieces',     public.pb_pieces_json(v_link.student_id::text),
    'checkins',   public.pb_checkins_json(v_link.student_id::text),
    'server_day', current_date
  );
end;
$$;

revoke all on function public.pb_student_today(text) from public;
grant execute on function public.pb_student_today(text) to anon, authenticated;

notify pgrst, 'reload schema';
