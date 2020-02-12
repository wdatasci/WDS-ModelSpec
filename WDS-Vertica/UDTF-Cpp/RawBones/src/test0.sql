drop table if exists x cascade;

create local temporary table x
on commit preserve rows as
select 'hey1'::varchar(20) as a, 10 as b, 200 as m
order by a,b
;
insert into x values('huh',5,140); commit;
insert into x values('what',8,300); commit;

select * from x order by a,b,m;


select public.RawBones(a,b using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.RawBones(a,b using parameters BlockMaxLength=10, EndPointInclusive=true) over (partition by a order by b)
from (select * from x order by a,b) a
;

select public.RawBones(a,b,m using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;


insert into x values('huh',5,233); commit;

select * from x order by a,b;

select public.RawBones(a,b using parameters BlockMaxLength=10) over (partition by a order by b)
from (select * from x order by a,b) a
;

