drop table if exists x cascade;

create local temporary table x
on commit preserve rows as
select 80003 as a, 10 as b, 200 as m
order by a,b
;
insert into x values(81000,5,140); commit;
insert into x values(84000,8,300); commit;

\echo Test input data
select * from x order by a,b,m;


select public.Bones(a,b,0) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.Bones(a,b,0 using parameters BlockMaxLength=3) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.Bones(a,b,0 using parameters BlockMaxLength=10, EndPointInclusive=true) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.Bones(a,b,m using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;


insert into x values(81000,5,233); commit;

select * from x order by a,b;

select public.Bones(a,b,0) over (partition by a order by b)
from (select * from x order by a,b) a
;
select public.Bones(a,b,0 using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;

