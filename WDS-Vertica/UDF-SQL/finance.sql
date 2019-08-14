
create or replace function public.PMT(i float, nper integer, pv float, fv float, ptyp integer) return float
as begin return cast(
    case 
    when i is null or nper is null or pv is null or fv is null or ptyp is null then 
        null
    when abs(i)<0.000001 then 
        --   pv=-pmt*npr-fv
        -(pv+fv)/nper
    when ptyp=0 then 
        case 
        when fv=0 then
            -pv*i*power(1.0+i,nper)/(power(1.0+i,nper)-1.0) 
        else
            -- -(pv+fv/power(1.0+i,nper))*i*power(1.0+i,nper)/(power(1.0+i,nper)-1.0) 
            -(pv*power(1.0+i,nper)+fv)*i/(power(1.0+i,nper)-1.0) 
        end
    else 
        case
        when fv=0 then
            -pv*i*power(1.0+i,nper)/(1.0+i)/(power(1.0+i,nper)-1.0) 
        else
            -- -(pv+fv/power(1.0+i,nper))*i*power(1.0+i,nper)/(1.0+i)/(power(1.0+i,nper)-1.0) 
            -(pv*power(1.0+i,nper)+fv)*i/(1.0+i)/(power(1.0+i,nper)-1.0) 
        end
    end as float); end;

create or replace function public.PV(i float, nper integer, pmt float, fv float, ptyp integer) return float
as begin return cast(
    case 
    when i is null or nper is null or pmt is null or fv is null or ptyp is null then 
        null
    when abs(i)<0.000001 then 
        -pmt*nper-fv
    when ptyp=0 then 
        case 
        when fv=0 then
            -pmt/i/power(1.0+i,nper)*(power(1.0+i,nper)-1.0)
        else
            -pmt*(power(1.0+i,nper)-1.0)/i/power(1.0+i,nper)-fv/power(1.0+i,nper)
        end
    else 
        case
        when fv=0 then
            -pmt*(1.0+i)*(power(1.0+i,nper)-1.0)/i/power(1.0+i,nper)
        else
            -pmt/power(1.0+i,nper)/i*(1.0+i)*(power(1.0+i,nper)-1.0)-fv/power(1.0+i,nper)
        end
    end as float); end;

create or replace function public.FV(i float, nper integer, pmt float, pv float, ptyp integer) return float
as begin return cast(
    case 
    when i is null or nper is null or pmt is null or pv is null or ptyp is null then 
        null
    when abs(i)<0.000001 then 
        -pmt*nper-pv
    when ptyp=0 then 
            -pmt/(i/(power(1.0+i,nper)-1.0))-pv*power(1.0+i,nper)
    else 
            -pmt/(i/(1.0+i)/(power(1.0+i,nper)-1.0))-pv*power(1.0+i,nper)
    end as float); end;

create local temporary table x
on commit preserve rows 
as select 12.0::float as irpct, 120::integer as term, 1000.0::float as pv, 0.0::float as fv, 0::integer as ptyp;
insert into x values(12.0,120,1000.0,0.0,1); commit;
insert into x values(12.0,120,1000.0,-230.0,0); commit;
insert into x values(12.0,120,1000.0,-230.0,1); commit;
insert into x values(0.0,120,1000.0,0.0,1); commit;
insert into x values(0.0,120,1000.0,-100.0,1); commit;
insert into x values(0.0,120,1000.0,-230.0,1); commit;

\pset fieldsep ','
\pset format u
select *,public.PV(irpct/1200.0,term,_pmt,fv,ptyp) as _pv
        ,public.FV(irpct/1200.0,term,_pmt,pv,ptyp) as _fv
from (
    select *, public.PMT(irpct/1200.0,term,pv,fv,ptyp)::float as _pmt
    from x
) a;

