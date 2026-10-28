\echo == after phaseD
select public.pb_save('tok_mia_0123456789abcdefghijklmnopqrstuv', 'checks', '{"rooms":{"staff":{"pass":1}}}'::jsonb, 0) as save_checks;
select public.pb_save('tok_mia_0123456789abcdefghijklmnopqrstuv', 'place', '{"piano":4,"theory":3,"at":1}'::jsonb, 0) as save_place;
select public.pb_save('tok_mia_0123456789abcdefghijklmnopqrstuv', 'records', '{}'::jsonb, 0) as save_records_still;
select public.pb_save('tok_mia_0123456789abcdefghijklmnopqrstuv', 'bogus', '{}'::jsonb, 0) as save_bogus;
select public.pb_get('tok_mia_0123456789abcdefghijklmnopqrstuv') -> 'plan' as plan_before;
-- the teacher (RLS as authenticated)
set role authenticated; select set_config('request.uid', '11111111-1111-1111-1111-111111111111', false);
insert into public.student_plan (student_id, plan) values ('aaaaaaaa-0000-0000-0000-000000000001', '{"piano":5,"theory":1,"home":true}') on conflict (student_id) do update set plan = excluded.plan, updated_at = now();
select count(*) as teacher_sees_own_plan from public.student_plan;
select count(*) as teacher_reads_checks from public.progress_store where store in ('checks','place');
\echo -- another teacher's student: must be refused
do $$ begin
  begin insert into public.student_plan (student_id, plan) values ('bbbbbbbb-0000-0000-0000-000000000002', '{"piano":1}'); raise notice 'BAD: inserted for another teacher';
  exception when others then raise notice 'ok: refused (%)', sqlerrm; end;
end $$;
select set_config('request.uid', '22222222-2222-2222-2222-222222222222', false);
select count(*) as other_teacher_sees from public.student_plan;
reset role;
select public.pb_get('tok_mia_0123456789abcdefghijklmnopqrstuv') -> 'plan' as plan_via_get;
set role anon;
do $$ begin begin perform * from public.student_plan; raise notice 'BAD: anon read the table'; exception when others then raise notice 'ok: anon cannot read student_plan (%)', sqlerrm; end; end $$;
select (public.pb_get('tok_mia_0123456789abcdefghijklmnopqrstuv') -> 'plan') is not null as anon_gets_plan_via_rpc;
reset role;
