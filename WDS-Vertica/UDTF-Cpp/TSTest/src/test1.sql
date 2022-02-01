

/* example of calling a Vertica UDTF function */


/* create a temporary table with an ID and something to create a "Bones" table for time series work */


drop table if exists x cascade;

create local temporary table x
on commit preserve rows as
select -10 as ID,'hey1'::char(20) as JunkStr, 0 as LengthIndex, 10 as StartingIndex
order by ID, StartingIndex
; commit;
insert into x values(20,'huh',5,20); commit;
insert into x values(30,'what',8,30); commit;

\echo /// Test input data
select * from x order by ID, StartingIndex, LengthIndex;

\echo /// Bones output

create local temporary table xx
on commit preserve rows as 
select public.Bones(ID, LengthIndex, StartingIndex using parameters EndPointInclusive=true ) over (partition by ID order by StartingIndex)
from (
	select *
	from x
	order by ID, StartingIndex
) a
;

select * from xx;

\echo /// Embedded in a series of queries
\echo /// Note: Row with -10 as ID has 0 for LengthIndex and so will not return a row.

create local temporary table xxx
on commit preserve rows as 
select 
	ID
	, ID::char(10) as IDStr
	, RowIndex
	, RowIndex+10 as MonthID
	, MonthID2Date(RowIndex+10) as TestDate
from (
		select public.Bones(ID, LengthIndex, StartingIndex) over (partition by ID order by StartingIndex)
		from (
			select *
			from x
			order by ID, StartingIndex
		) a
     ) a
;

select * from xxx;

\echo /// Another call.  The guts of TSTest can be general and hit external resources.

select public.TSTest(ID,IDStr,RowIndex,TestDate) over (partition by ID order by RowIndex)
from xxx
order by ID, RowIndex;


