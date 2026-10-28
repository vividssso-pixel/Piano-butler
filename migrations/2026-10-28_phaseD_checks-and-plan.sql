-- Phase D: the chapter checks and the placement reach the teacher; the teacher sets a student's start in the drills
-- Run ONCE in Supabase > SQL Editor > New query (name it "D checks and plan") > paste all > Run. Safe to run again.
-- Run phaseA1, phaseB1, phaseB2, phaseB3 and phaseC first -- you already did.
--
-- Changes:
--   progress_store, pb_save   two more kinds of progress a student's link saves:
--                               'checks' = the chapter checks, the floor checkpoints and the reviews
--                               'place'  = the result of "Where should you start?" (piano floor, theory grade)
--   pb_get(token)             same as before (phaseB3), plus  plan: { piano, theory, home }  = what the teacher set (or null)
-- Adds:
--   table student_plan        one row per student: the teacher's setting for the drills
--                               piano  = the floor the house starts from (0 = Beginner ... 9 = Grade 8)
--                               theory = the student's theory grade (1 to 6; 7 = all done)
--                               home   = true: the student (an adult) also sees the Home
--                             The teacher reads and writes it with their own login (own students only).
--                             Students never read the table: their drills get it through pb_get with the secret token.
-- No name, email or age is stored here.

-- 1. two more stores in progress_store
do $$
declare c record;
begin
  for c in
    select conname from pg_constraint
    where conrelid = 'public.progress_store'::regclass and contype = 'c' and pg_get_constraintdef(oid) like '%last_chapter%'
  loop
    execute format('alter table public.progress_store drop constraint %I', c.conname);
  end loop;
end $$;
alter table public.progress_store add constraint progress_store_store_check
  check (store in ('records','stamps','lesson_steps','steps_total','posture','arm_ex','last_chapter','checks','place'));

-- 2. the teacher's setting for each student
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
    create table if not exists public.student_plan (
      student_id  %s primary key references public.students(id) on delete cascade,
      plan        jsonb not null default '{}'::jsonb check (jsonb_typeof(plan) = 'object' and octet_length(plan::text) <= 2000),
      updated_at  timestamptz not null default now()
    )$f$, idtype);
end $$;

alter table public.student_plan enable row level security;
revoke all on public.student_plan from anon;
grant select, insert, update, delete on public.student_plan to authenticated;

drop policy if exists student_plan_select on public.student_plan;
drop policy if exists student_plan_insert on public.student_plan;
drop policy if exists student_plan_update on public.student_plan;
drop policy if exists student_plan_delete on public.student_plan;

create policy student_plan_select on public.student_plan
  for select to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));
create policy student_plan_insert on public.student_plan
  for insert to authenticated
  with check (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));
create policy student_plan_update on public.student_plan
  for update to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()))
  with check (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));
create policy student_plan_delete on public.student_plan
  for delete to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));

-- 3. pb_get: as in phaseB3, plus the plan
create or replace function public.pb_get(p_token text)
returns jsonb
language plpgsql
stable
security definer
set search_path = public
as $$
declare
  v_link   public.student_links%rowtype;
  v_stores jsonb;
  v_plan   jsonb;
begin
  if p_token is null or char_length(p_token) < 32 then return null; end if;
  select * into v_link from public.student_links where token = p_token and active;
  if not found then return null; end if;
  select coalesce(jsonb_object_agg(s.store, jsonb_build_object('value', s.value, 'rev', s.rev)), '{}'::jsonb)
    into v_stores
  from public.progress_store s
  where s.student_id = v_link.student_id;
  select p.plan into v_plan from public.student_plan p where p.student_id = v_link.student_id;
  return jsonb_build_object(
    'ref',         left(md5('pb:' || v_link.student_id::text), 16),
    'name',        v_link.display_name,
    'stores',      v_stores,
    'plan',        v_plan,
    'server_time', now()
  );
end;
$$;

-- 4. pb_save: as in phaseB3, with the two new stores
create or replace function public.pb_save(p_token text, p_store text, p_value jsonb, p_base_rev integer)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_sid public.student_links.student_id%type;
  v_rev integer;
  v_cur jsonb;
  v_n   integer;
  v_max integer;
begin
  if p_token is null or char_length(p_token) < 32 then
    return jsonb_build_object('ok', false, 'reason', 'link');
  end if;
  select l.student_id into v_sid from public.student_links l where l.token = p_token and l.active;
  if not found then return jsonb_build_object('ok', false, 'reason', 'link'); end if;

  if p_store is null or p_store not in ('records','stamps','lesson_steps','steps_total','posture','arm_ex','last_chapter','checks','place') then
    return jsonb_build_object('ok', false, 'reason', 'store');
  end if;
  if p_value is null or p_base_rev is null or p_base_rev < 0 then
    return jsonb_build_object('ok', false, 'reason', 'value');
  end if;
  -- last_chapter is a short piece of text; every other store is a json object
  if p_store = 'last_chapter' then
    if jsonb_typeof(p_value) <> 'string' or char_length(p_value #>> '{}') > 60 then
      return jsonb_build_object('ok', false, 'reason', 'value');
    end if;
  elsif jsonb_typeof(p_value) <> 'object' then
    return jsonb_build_object('ok', false, 'reason', 'value');
  end if;
  v_max := case when p_store = 'records' then 300000 else 60000 end;
  if octet_length(p_value::text) > v_max then
    return jsonb_build_object('ok', false, 'reason', 'size');
  end if;

  if p_base_rev = 0 then
    insert into public.progress_store (student_id, store, value, rev)
    values (v_sid, p_store, p_value, 1)
    on conflict (student_id, store) do nothing;
    get diagnostics v_n = row_count;
    if v_n = 1 then return jsonb_build_object('ok', true, 'rev', 1); end if;
  end if;

  select s.rev, s.value into v_rev, v_cur
  from public.progress_store s
  where s.student_id = v_sid and s.store = p_store
  for update;
  if not found or v_rev <> p_base_rev then
    return jsonb_build_object('ok', false, 'reason', 'conflict', 'rev', coalesce(v_rev, 0), 'value', v_cur);
  end if;

  update public.progress_store
     set value = p_value, rev = v_rev + 1, updated_at = now()
   where student_id = v_sid and store = p_store;
  return jsonb_build_object('ok', true, 'rev', v_rev + 1);
end;
$$;

revoke all on function public.pb_get(text) from public;
revoke all on function public.pb_save(text, text, jsonb, integer) from public;
grant execute on function public.pb_get(text) to anon, authenticated;
grant execute on function public.pb_save(text, text, jsonb, integer) to anon, authenticated;

notify pgrst, 'reload schema';
