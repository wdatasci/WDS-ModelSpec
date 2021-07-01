


create or replace function public.if(hyp boolean, thn int, els int) return int
as begin
return cast(case when (hyp) then thn else els end as int);
end;

create or replace function public.if(hyp boolean, thn varchar, els varchar) return varchar
as begin
return cast(case when (hyp) then thn else els end as varchar);
end;

create or replace function public.if(hyp boolean, thn float, els float) return float
as begin
return cast(case when (hyp) then thn else els end as float);
end;

create or replace function public.if(hyp boolean, thn date, els date) return date
as begin
return cast(case when (hyp) then thn else els end as date);
end;

create or replace function public.ifNotNull(hyp float, thn float, els float) return float
as begin
return cast(case when (hyp is not null) then thn else els end as float);
end;

create or replace function public.if10(hyp boolean) return float
as begin
return cast(case when (hyp) then 1.0 else 0.0 end as float);
end;

create or replace function public.ifelsenull(hyp boolean, thn float) return float
as begin
return cast(case when (hyp) then thn else null end as float);
end;

create or replace function public.ifelsenull(hyp boolean, thn int) return int
as begin
return cast(case when (hyp) then thn else null end as int);
end;

create or replace function public.ifPosElseNull(thn float) return float
as begin
return cast(case when (thn is not null and thn > 0.0) then thn else null end as float);
end;

create or replace function public.ifPosElseNull(thn int) return int
as begin
return cast(case when (thn is not null and thn > 0) then thn else null end as int);
end;


create or replace function public.isPos(arg float) return boolean 
as begin return cast(case when arg is null then false else (arg>0.0) end as boolean); end;

create or replace function public.isPos(arg int) return boolean as begin return public.isPos(castfloat(arg)); end;

create or replace function public.isNeg(arg float) return boolean 
as begin return cast(case when arg is null then false else (arg<0.0) end as boolean); end;

create or replace function public.isNeg(arg int) return boolean as begin return public.isNeg(castfloat(arg)); end;

create or replace function public.isNonZero(arg float) return boolean 
as begin return cast(case when arg is null then false else (arg<0.0 or arg>0.0) end as boolean); end;

create or replace function public.isNonZero(arg int) return boolean as begin return public.isNonZero(castfloat(arg)); end;


select x
    , if(true,'Hey','What') as zt
    , if(false,'Hey','What') as zf
from (select cast('2019-03-31' as date) as x) a;

select ifnotnull(3,4.5,3.2);








