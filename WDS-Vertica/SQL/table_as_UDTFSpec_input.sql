-- call via command line:
-- vsql -f <this_file> [OPTIONS] -v lSchema=name -v lTable=othername

\set llSchema '''':lSchema''''
\set llTable '''':lTable''''

-- select * from v_catalog.columns where table_schema=:llSchema and table_name=:llTable limit 2;
\pset fieldsep ' '
\pset format unaligned
\pset tuples_only true
select concat(concat('<Column Use="I" Name="',column_name),'"'),concat(concat(' DTyp="',
        if(data_type='int','Int'
            ,if(data_type='float','Dbl'
            ,if(data_type='bool','Bln'
            ,if(data_type='date','Dte'
            ,if(data_type='datetime','Dtm'
            ,if(left(data_type,4)='char',concat('Str" Length="',data_type_length)
            ,if(left(data_type,7)='varchar',concat('VLS" Length="',data_type_length)
            ,data_type
        ))))))))
            , '" />')
        from v_catalog.columns where table_schema=:llSchema and table_name=:llTable order by ordinal_position;

