-- call via command line:
-- vsql -f <this_file> [OPTIONS] -v lSchema=name -v lTable=othername
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

\set llSchema '''':lSchema''''
\set llTable '''':lTable''''

-- select * from v_catalog.columns where table_schema=:llSchema and table_name=:llTable limit 2;
\pset fieldsep ' '
\pset format unaligned
\pset tuples_only true
\echo :llSchema
\echo :llTable
select concat(concat('<Column Use="I" Name="',column_name),'"'),concat(concat(' DTyp="',
        if(data_type='int','Int'
            ,if(data_type='float','Dbl'
            ,if(data_type='bool','Bln'
            ,if(data_type='date','Dte'
            ,if(data_type='datetime','DTm'
            ,if(data_type='timestamp','DTm'
            ,if(left(data_type,4)='char',concat('Str" Length="',data_type_length)
            ,if(left(data_type,7)='varchar',concat('VLS" Length="',data_type_length)
            ,data_type
        )))))))))
            , '" />')
        from v_catalog.columns where table_schema=:llSchema and table_name=:llTable order by ordinal_position;

