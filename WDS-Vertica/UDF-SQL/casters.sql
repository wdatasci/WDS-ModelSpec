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


create or replace function public.castfloat(arg int) return float as begin return cast(arg as float); end;
create or replace function public.castint(arg int) return int as begin return cast(arg as int); end;


-- vertica integers are all 64 bit signed longs and the min value is the null value

create or replace function public.CleanLimits(arg Integer, c1 Integer, c2 Integer) return Integer
as begin return cast(
    case
    when arg is null then null              --null
    --when arg <> arg then null               --Nan
    --when arg = (0.0::float)/0 then null     --Infinity
    --when arg = -(0.0::float)/0 then null    -- -Infinity
    when arg < c1 or arg > c2 then null
    else arg
    end as Integer); end;


create or replace function public.CleanLimitLeft(arg int, c1 int) return int
as begin return cast(
    case
    when arg is null then null              --null
    --when arg <> arg then null               --Nan
    --when arg = (0.0::float)/0 then null     --Infinity
    --when arg = -(0.0::float)/0 then null    -- -Infinity
    when arg < c1  then null
    else arg
    end as int); end;


create or replace function public.CleanLimitRight(arg int, c1 int) return int
as begin return cast(
    case
    when arg is null then null              --null
    --when arg <> arg then null               --Nan
    --when arg = (0.0::float)/0 then null     --Infinity
    --when arg = -(0.0::float)/0 then null    -- -Infinity
    when arg > c1  then null
    else arg
    end as int); end;

            
create or replace function public.CleanLimits(arg float, c1 float, c2 float) return float
as begin return cast(
    case
    when arg is null then null              --null
    when arg <> arg then null               --Nan
    when arg = (0.0::float)/0 then null     --Infinity
    when arg = -(0.0::float)/0 then null    -- -Infinity
    when arg < c1 or arg > c2 then null
    else arg
    end as float); end;


create or replace function public.CleanLimitLeft(arg float, c1 float) return float
as begin return cast(
    case
    when arg is null then null              --null
    when arg <> arg then null               --Nan
    when arg = (0.0::float)/0 then null     --Infinity
    when arg = -(0.0::float)/0 then null    -- -Infinity
    when arg < c1  then null
    else arg
    end as float); end;


create or replace function public.CleanLimitRight(arg float, c1 float) return float
as begin return cast(
    case
    when arg is null then null              --null
    when arg <> arg then null               --Nan
    when arg = (0.0::float)/0 then null     --Infinity
    when arg = -(0.0::float)/0 then null    -- -Infinity
    when arg > c1  then null
    else arg
    end as float); end;


create local temporary table x
on commit preserve rows as
select 1::float as x, 3::integer as y;

insert into x values( -3.4 , -3); commit;
insert into x values( 7.8 , 7); commit;
insert into x values( 17.8 , 17); commit;
insert into x values( (0.0::float)/0 , null::integer); commit;
insert into x values( (1.0::float)/0 , null::integer); commit;
insert into x values( -(1.0::float)/0 , null::integer); commit;
insert into x values( null , null::integer); commit;

select * from x;
select *, CleanLimits(x,1.2,10.0), CleanLimits(y,1.2,10.0) from x;
select *, CleanLimits(x,1,10), CleanLimits(y,1,10) from x;








