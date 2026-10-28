\set QUIET on
insert into public.student_links (student_id, teacher_id, display_name, token) values ('aaaaaaaa-0000-0000-0000-000000000001', '11111111-1111-1111-1111-111111111111', 'Mia', 'tok_mia_0123456789abcdefghijklmnopqrstuv');
\echo == before phaseD
select public.pb_save('tok_mia_0123456789abcdefghijklmnopqrstuv', 'checks', '{"rooms":{}}'::jsonb, 0) as save_checks;
select public.pb_get('tok_mia_0123456789abcdefghijklmnopqrstuv') ? 'plan' as get_has_plan;
