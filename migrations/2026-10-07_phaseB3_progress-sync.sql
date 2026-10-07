-- Phase B3: a student's drill progress follows them from device to device
-- Run ONCE in Supabase > SQL Editor > New query (name it "B3 progress sync") > paste all > Run. Safe to run again.
-- Run phaseA1 and phaseB1 first -- you already did (B2 is not needed for this one, but you ran it too).
--
-- Adds:
--   table progress_store   one row per student per kind of progress (best scores, scale stamps, lesson steps ticked,
--                          steps per chapter, posture check, arm exercises, the chapter they were last in).
--                          Each row has a revision number so two devices can never overwrite each other silently.
--   table practice_log     one row per drill play (when, which drill and level, mode, score). Only added to, never changed.
--   pb_get(token)          the student's saved progress (called when the student opens their link)
--   pb_save(token, store, value, base_rev)   save one kind of progress; refused with "conflict" if another device saved first
--   pb_log(token, rows)    add drill plays to the practice log (up to 50 at a time, duplicates ignored)
-- Students never read or write the tables: they only call these three functions with the secret token from their link.
-- The teacher dashboard reads (and can delete) the rows of the teacher's own students with the teacher's own login.
-- Voice recordings and the teacher's kits are NOT stored here. No name, email or age is stored here (only drill results).

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
    create table if not exists public.progress_store (
      student_id  %s not null references public.students(id) on delete cascade,
      store       text not null check (store in ('records','stamps','lesson_steps','steps_total','posture','arm_ex','last_chapter')),
      value       jsonb not null,
      rev         integer not null default 1 check (rev >= 1),
      updated_at  timestamptz not null default now(),
      primary key (student_id, store)
    )$f$, idtype);
  execute format($f$
    create table if not exists public.practice_log (
      id          bigint generated always as identity primary key,
      student_id  %s not null references public.students(id) on delete cascade,
      at          timestamptz not null,
      drill       text not null check (char_length(drill) between 1 and 60),
      level       integer not null check (level between 0 and 99),
      mode        text not null check (mode in ('lesson','game')),
      score       integer not null check (score between 0 and 100000),
      correct     integer not null check (correct between 0 and 1000),
      total       integer not null check (total between 0 and 1000),
      created_at  timestamptz not null default now(),
      unique (student_id, at, drill, level, mode)
    )$f$, idtype);
end $$;

create index if not exists practice_log_student_at on public.practice_log (student_id, at desc);

alter table public.progress_store enable row level security;
alter table public.practice_log   enable row level security;
revoke all on public.progress_store from anon;
revoke all on public.practice_log   from anon;

drop policy if exists progress_store_select on public.progress_store;
drop policy if exists progress_store_delete on public.progress_store;
drop policy if exists practice_log_select   on public.practice_log;
drop policy if exists practice_log_delete   on public.practice_log;

-- the teacher can read (and clear, by deleting) the progress of their own students; nobody inserts or updates directly
create policy progress_store_select on public.progress_store
  for select to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));
create policy progress_store_delete on public.progress_store
  for delete to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));
create policy practice_log_select on public.practice_log
  for select to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));
create policy practice_log_delete on public.practice_log
  for delete to authenticated
  using (exists (select 1 from public.students s where s.id = student_id and s.user_id = auth.uid()));

-- ref = a short code for this student that stays the same when the link is regenerated; the drills use it to tell
-- "same child" from "another child" on a shared tablet. It does not reveal the student's id.
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
begin
  if p_token is null or char_length(p_token) < 32 then return null; end if;
  select * into v_link from public.student_links where token = p_token and active;
  if not found then return null; end if;
  select coalesce(jsonb_object_agg(s.store, jsonb_build_object('value', s.value, 'rev', s.rev)), '{}'::jsonb)
    into v_stores
  from public.progress_store s
  where s.student_id = v_link.student_id;
  return jsonb_build_object(
    'ref',         left(md5('pb:' || v_link.student_id::text), 16),
    'name',        v_link.display_name,
    'stores',      v_stores,
    'server_time', now()
  );
end;
$$;

-- p_base_rev = the revision this device last saw (0 = it has never saved this store).
-- ok:true -> saved, 'rev' is the new revision.  reason 'conflict' -> another device saved first: 'value' and 'rev' are what is stored now.
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

  if p_store is null or p_store not in ('records','stamps','lesson_steps','steps_total','posture','arm_ex','last_chapter') then
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

-- p_rows: [{ "at": <milliseconds since 1970>, "drill": "note-names", "level": 2, "mode": "game", "score": 80, "correct": 8, "total": 10 }, ...]
-- A row that is out of range is skipped (counted in 'skipped'); a row already logged is ignored.
create or replace function public.pb_log(p_token text, p_rows jsonb)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_sid   public.student_links.student_id%type;
  r       jsonb;
  v_at    timestamptz;
  v_added integer := 0;
  v_skip  integer := 0;
  v_n     integer;
begin
  if p_token is null or char_length(p_token) < 32 then
    return jsonb_build_object('ok', false, 'reason', 'link');
  end if;
  select l.student_id into v_sid from public.student_links l where l.token = p_token and l.active;
  if not found then return jsonb_build_object('ok', false, 'reason', 'link'); end if;
  if p_rows is null or jsonb_typeof(p_rows) <> 'array' or jsonb_array_length(p_rows) > 50 then
    return jsonb_build_object('ok', false, 'reason', 'rows');
  end if;
  if (select count(*) from public.practice_log where student_id = v_sid) >= 20000 then
    return jsonb_build_object('ok', false, 'reason', 'full');
  end if;

  for r in select e.value from jsonb_array_elements(p_rows) e loop
    begin
      v_at := to_timestamp((r ->> 'at')::numeric / 1000.0);
      if v_at < now() - interval '400 days' or v_at > now() + interval '2 days' then
        v_skip := v_skip + 1;
      else
        insert into public.practice_log (student_id, at, drill, level, mode, score, correct, total)
        values (v_sid, v_at, r ->> 'drill', (r ->> 'level')::integer, r ->> 'mode',
                (r ->> 'score')::integer, (r ->> 'correct')::integer, (r ->> 'total')::integer)
        on conflict do nothing;
        get diagnostics v_n = row_count;
        v_added := v_added + v_n;
      end if;
    exception when others then
      v_skip := v_skip + 1;
    end;
  end loop;
  return jsonb_build_object('ok', true, 'added', v_added, 'skipped', v_skip);
end;
$$;

revoke all on function public.pb_get(text) from public;
revoke all on function public.pb_save(text, text, jsonb, integer) from public;
revoke all on function public.pb_log(text, jsonb) from public;
grant execute on function public.pb_get(text) to anon, authenticated;
grant execute on function public.pb_save(text, text, jsonb, integer) to anon, authenticated;
grant execute on function public.pb_log(text, jsonb) to anon, authenticated;

notify pgrst, 'reload schema';
