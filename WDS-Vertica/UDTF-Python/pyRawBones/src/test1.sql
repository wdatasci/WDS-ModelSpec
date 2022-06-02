drop table if exists x cascade;

create local temporary table x
on commit preserve rows as
select 1 as a, 10 as b, 200 as m
order by a,b
;
insert into x values(-1,5,140); commit;
insert into x values(17,8,300); commit;

select * from x order by a,b,m;


select public.pyRawBones(a,b, 0 using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.pyRawBones(a,b, 0 using parameters BlockMaxLength=10, EndPointInclusive=true) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.pyRawBones(a,b,m using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;


insert into x values(1,5,233); commit;

\echo Supposed to fail with more than one row with a=1

select * from x order by a,b;

select public.pyRawBones(a,b, 0 using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;

