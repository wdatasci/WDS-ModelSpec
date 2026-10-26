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

