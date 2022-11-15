-- call via command line:
-- vsql <this_file> [OPTIONS] -v lSchema=name -v lTable=othername

\set llSchema '''':lSchema''''
\set llTable '''':lTable''''

select ', '||column_name||' as _'||column_name, '--', column_name,data_type,data_type_length,ordinal_position
from v_catalog.columns where table_schema=:llSchema and table_name=:llTable order by ordinal_position;

