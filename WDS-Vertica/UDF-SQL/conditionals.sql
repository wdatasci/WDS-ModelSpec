/*Copyright (c) 2019-2027 Wypasek Data Science, Inc.
Released under the MIT open source license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

create or replace function public.if(hyp boolean, thn int, els int) return int 
as begin 
return cast(case when (hyp) then thn else els end as int); 
end;

create or replace function public.if(hyp boolean, thn int, els varchar) return varchar 
as begin 
return cast(case when (hyp) then thn::varchar else els end as varchar); 
end;

create or replace function public.ifNotNullIntAsVarChar(thn int, els varchar) return varchar
as begin
return public.if(thn is not null, thn, els);
end;

create or replace function public.if(hyp boolean, thn varchar, els varchar) return varchar
as begin
return cast(case when (hyp) then thn else els end as varchar);
end;

create or replace function public.if(hyp boolean, thn float, els float) return float
as begin
return cast(case when (hyp) then thn else els end as float);
end;

create or replace function public.if(hyp boolean, thn float, els varchar) return varchar
as begin
return cast(case when (hyp) then thn::varchar else els end as varchar);
end;

create or replace function public.ifNotNullDblAsVarChar(thn float, els varchar) return varchar
as begin
return public.if(thn is not null, thn, els);
end;

create or replace function public.if(hyp boolean, thn date, els date) return date
as begin
return cast(case when (hyp) then thn else els end as date);
end;

create or replace function public.if(hyp boolean, thn date, els varchar) return varchar
as begin
return cast(case when (hyp) then thn::varchar else els end as varchar);
end;

create or replace function public.ifNotNullDteAsVarChar(thn date, els varchar) return varchar
as begin
return public.if(thn is not null, '"' || thn::varchar || '"', '"' || els || '"');
end;

create or replace function public.if(hyp boolean, thn timestamp, els timestamp) return timestamp
as begin
return cast(case when (hyp) then thn else els end as timestamp);
end;

create or replace function public.if(hyp boolean, thn timestamp, els varchar) return varchar
as begin
return cast(case when (hyp) then thn::varchar else els end as varchar);
end;

create or replace function public.ifNotNullDTmAsVarChar(thn timestamp, els varchar) return varchar
as begin
return public.if(thn is not null, '"' || thn::varchar || '"', '"' || els || '"');
end;

create or replace function public.ifNotNull(hyp float, thn float, els float) return float
as begin
return cast(case when (hyp is not null) then thn else els end as float);
end;

create or replace function public.if(hyp boolean, thn boolean, els boolean) return boolean
as begin
return cast(case when (hyp) then thn else els end as boolean);
end;

create or replace function public.if(hyp boolean, thn boolean, els varchar) return varchar
as begin
return cast(case when (hyp) then thn::varchar else els end as varchar);
end;

create or replace function public.ifNotNullVarCharAsVarChar(thn varchar, els varchar) return varchar
as begin
return public.if(thn is not null, thn, els);
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








