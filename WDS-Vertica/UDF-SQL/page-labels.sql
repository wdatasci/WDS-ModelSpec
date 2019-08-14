

create or replace function public.IntBucket(arg int, c1 int) return int
as begin return cast(case when arg is null then 0 when arg <= c1 then 1 else 2 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int) return int
as begin return cast(case when arg is null or arg <= c1 then public.IntBucket(arg,c1) when arg <= c2 then 2 else 3 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int) return int
as begin return cast(case when arg is null or arg <= c2 then public.IntBucket(arg,c1,c2) when arg <= c3 then 3 else 4 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int) return int
as begin return cast(case when arg is null or arg <= c3 then public.IntBucket(arg,c1,c2,c3) when arg <= c4 then 4 else 5 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int) return int
as begin return cast(case when arg is null or arg <= c4 then public.IntBucket(arg,c1,c2,c3,c4) when arg <= c5 then 5 else 6 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int) return int
as begin return cast(case when arg is null or arg <= c5 then public.IntBucket(arg,c1,c2,c3,c4,c5) when arg <= c6 then 6 else 7 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int) return int
as begin return cast(case when arg is null or arg <= c6 then public.IntBucket(arg,c1,c2,c3,c4,c5,c6) when arg <= c7 then 7 else 8 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int) return int
as begin return cast(case when arg is null or arg <= c7 then public.IntBucket(arg,c1,c2,c3,c4,c5,c6,c7) when arg <= c8 then 8 else 9 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int) return int
as begin return cast(case when arg is null or arg <= c8 then public.IntBucket(arg,c1,c2,c3,c4,c5,c6,c7,c8) when arg <= c9 then 9 else 10 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int, c10 int) return int
as begin return cast(case when arg is null or arg <= c9 then public.IntBucket(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9) when arg <= c10 then 10 else 11 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int, c10 int, c11 int) return int
as begin return cast(case when arg is null or arg <= c10 then public.IntBucket(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10) when arg <= c11 then 11 else 12 end as int); end;
            
create or replace function public.IntBucket(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int, c10 int, c11 int, c12 int) return int
as begin return cast(case when arg is null or arg <= c11 then public.IntBucket(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11) when arg <= c12 then 12 else 13 end as int); end;
            


create or replace function public.PageLabels(arg int, c1 int) return varchar(32)
as begin return cast(
    case when arg is null then 'a NULL'
    when arg <= c1 then concat('b _ <= ',cast(c1 as char(40)))
    else concat('c _ > ',cast(c1 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c1 then public.PageLabels(arg,c1)
    when arg <= c2 then concat(concat(concat('c ',cast(c1 as char(40))),' < _ <= '),cast(c2 as char(40)))
    else concat('d _ > ',cast(c2 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c2 then public.PageLabels(arg,c1,c2)
    when arg <= c3 then concat(concat(concat('d ',cast(c2 as char(40))),' < _ <= '),cast(c3 as char(40)))
    else concat('e _ > ',cast(c3 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c3 then public.PageLabels(arg,c1,c2,c3)
    when arg <= c4 then concat(concat(concat('e ',cast(c3 as char(40))),' < _ <= '),cast(c4 as char(40)))
    else concat('f _ > ',cast(c4 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c4 then public.PageLabels(arg,c1,c2,c3,c4)
    when arg <= c5 then concat(concat(concat('f ',cast(c4 as char(40))),' < _ <= '),cast(c5 as char(40)))
    else concat('g _ > ',cast(c5 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c5 then public.PageLabels(arg,c1,c2,c3,c4,c5)
    when arg <= c6 then concat(concat(concat('g ',cast(c5 as char(40))),' < _ <= '),cast(c6 as char(40)))
    else concat('h _ > ',cast(c6 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c6 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6)
    when arg <= c7 then concat(concat(concat('h ',cast(c6 as char(40))),' < _ <= '),cast(c7 as char(40)))
    else concat('i _ > ',cast(c7 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c7 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7)
    when arg <= c8 then concat(concat(concat('i ',cast(c7 as char(40))),' < _ <= '),cast(c8 as char(40)))
    else concat('j _ > ',cast(c8 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c8 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8)
    when arg <= c9 then concat(concat(concat('j ',cast(c8 as char(40))),' < _ <= '),cast(c9 as char(40)))
    else concat('k _ > ',cast(c9 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int, c10 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c9 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9)
    when arg <= c10 then concat(concat(concat('k ',cast(c9 as char(40))),' < _ <= '),cast(c10 as char(40)))
    else concat('l _ > ',cast(c10 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int, c10 int, c11 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c10 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)
    when arg <= c11 then concat(concat(concat('l ',cast(c10 as char(40))),' < _ <= '),cast(c11 as char(40)))
    else concat('m _ > ',cast(c11 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg int, c1 int, c2 int, c3 int, c4 int, c5 int, c6 int, c7 int, c8 int, c9 int, c10 int, c11 int, c12 int) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c11 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
    when arg <= c12 then concat(concat(concat('m ',cast(c11 as char(40))),' < _ <= '),cast(c12 as char(40)))
    else concat('n _ > ',cast(c12 as char(40)))
    end as varchar(32)); end;
            





create or replace function public.PageLabels(arg float, c1 float) return varchar(32)
as begin return cast(
    case when arg is null then 'a NULL'
    when arg <= c1 then concat('b _ <= ',cast(c1 as char(40)))
    else concat('c _ > ',cast(c1 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c1 then public.PageLabels(arg,c1)
    when arg <= c2 then concat(concat(concat('c ',cast(c1 as char(40))),' < _ <= '),cast(c2 as char(40)))
    else concat('d _ > ',cast(c2 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c2 then public.PageLabels(arg,c1,c2)
    when arg <= c3 then concat(concat(concat('d ',cast(c2 as char(40))),' < _ <= '),cast(c3 as char(40)))
    else concat('e _ > ',cast(c3 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c3 then public.PageLabels(arg,c1,c2,c3)
    when arg <= c4 then concat(concat(concat('e ',cast(c3 as char(40))),' < _ <= '),cast(c4 as char(40)))
    else concat('f _ > ',cast(c4 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c4 then public.PageLabels(arg,c1,c2,c3,c4)
    when arg <= c5 then concat(concat(concat('f ',cast(c4 as char(40))),' < _ <= '),cast(c5 as char(40)))
    else concat('g _ > ',cast(c5 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c5 then public.PageLabels(arg,c1,c2,c3,c4,c5)
    when arg <= c6 then concat(concat(concat('g ',cast(c5 as char(40))),' < _ <= '),cast(c6 as char(40)))
    else concat('h _ > ',cast(c6 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float, c7 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c6 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6)
    when arg <= c7 then concat(concat(concat('h ',cast(c6 as char(40))),' < _ <= '),cast(c7 as char(40)))
    else concat('i _ > ',cast(c7 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float, c7 float, c8 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c7 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7)
    when arg <= c8 then concat(concat(concat('i ',cast(c7 as char(40))),' < _ <= '),cast(c8 as char(40)))
    else concat('j _ > ',cast(c8 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float, c7 float, c8 float, c9 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c8 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8)
    when arg <= c9 then concat(concat(concat('j ',cast(c8 as char(40))),' < _ <= '),cast(c9 as char(40)))
    else concat('k _ > ',cast(c9 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float, c7 float, c8 float, c9 float, c10 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c9 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9)
    when arg <= c10 then concat(concat(concat('k ',cast(c9 as char(40))),' < _ <= '),cast(c10 as char(40)))
    else concat('l _ > ',cast(c10 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float, c7 float, c8 float, c9 float, c10 float, c11 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c10 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)
    when arg <= c11 then concat(concat(concat('l ',cast(c10 as char(40))),' < _ <= '),cast(c11 as char(40)))
    else concat('m _ > ',cast(c11 as char(40)))
    end as varchar(32)); end;
            
create or replace function public.PageLabels(arg float, c1 float, c2 float, c3 float, c4 float, c5 float, c6 float, c7 float, c8 float, c9 float, c10 float, c11 float, c12 float) return varchar(32)
as begin return cast(
    case
    when arg is null or arg <= c11 then public.PageLabels(arg,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
    when arg <= c12 then concat(concat(concat('m ',cast(c11 as char(40))),' < _ <= '),cast(c12 as char(40)))
    else concat('n _ > ',cast(c12 as char(40)))
    end as varchar(32)); end;
            
select PageLabels(675,620,660,700,740);









