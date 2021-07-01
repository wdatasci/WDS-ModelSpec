drop table if exists x cascade;

create local temporary table x
on commit preserve rows as
select -10 as a,'hey1'::varchar(20) as aa, 0 as b, 10 as c
order by a,b
;
insert into x values(20,'huh',5,20); commit;
insert into x values(30,'what',8,30); commit;

\echo Test input data
select * from x order by a,b,c;


select public.TSTest(ID,IDStr,RowIndex,TestDate) over (partition by ID order by RowIndex)
from (
select 
	ID
    , ID::char(10) as IDStr
	, RowIndex
	, RowIndex+10 as MonthID
	, MonthID2Date(RowIndex+10) as TestDate
from (
	select public.Bones(a,b,0) over (partition by a order by b)
	from (select * from x order by a,b) a
) aa
order by ID, RowIndex
) aaa
;


