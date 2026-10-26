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

create or replace function public.Date2MonthID(arg date) return int as begin return cast(  (year(arg)-2000)*12+month(arg) as int); end;

create or replace function public.Timestamp2MonthID(arg timestamp) return int as begin return cast(  (year(arg)-2000)*12+month(arg) as int); end;


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
    ,timestamp2MonthID(y)
    ,if(true,'Hey','What') as zt
    , if(false,'Hey','What') as zf
    , MonthID2Date(183)
    , MonthID2EOMDate(183)
    , Date2YYYYMM(MonthID2Date(183))
from (select cast('2019-03-31' as date) as x, cast('2019-03-31' as timestamp) as y) a;

select x
    ,date2MonthID(x)
    ,if(true,'Hey','What') as zt
    , if(false,'Hey','What') as zf
    , MonthID2Date(date2MonthID(x))
    , MonthID2EOMDate(date2MonthID(x))
    , Date2YYYYMM(MonthID2Date(date2MonthID(x)))
from (select cast('2019-02-11' as date) as x) a;







