drop table if exists x cascade;

create local temporary table x
on commit preserve rows as
select 80003 as A, 10 as B, 200 as m
order by a,b
;
insert into x values(81000,5,140); commit;
insert into x values(84000,8,300); commit;

select * from x;


select public.pyTestScalar(A,B) from x;

