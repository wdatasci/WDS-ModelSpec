
create or replace function public.Date2MonthID(arg date) return int
as begin
return cast(  (year(arg)-2000)*12+month(arg) as int);
end;

create or replace function public.MonthID2Date(arg int) return date
as begin
return add_months('1999-12-01'::date,arg);
end;

create or replace function public.MonthID2EOMDate(arg int) return date
as begin
return (add_months('1999-12-01'::date,arg+1)-1)::date;
end;

create or replace function public.Date2YYYYMM(arg date) return int
as begin
return cast(case when arg is null then null else year(arg)*100+month(arg) end as int);
end;


select x
    ,date2MonthID(x)
    ,if(true,'Hey','What') as zt
    , if(false,'Hey','What') as zf
    , MonthID2Date(183)
    , MonthID2EOMDate(183)
    , Date2YYYYMM(MonthID2Date(183))
from (select cast('2019-03-31' as date) as x) a;

select x
    ,date2MonthID(x)
    ,if(true,'Hey','What') as zt
    , if(false,'Hey','What') as zf
    , MonthID2Date(date2MonthID(x))
    , MonthID2EOMDate(date2MonthID(x))
    , Date2YYYYMM(MonthID2Date(date2MonthID(x)))
from (select cast('2019-02-11' as date) as x) a;


