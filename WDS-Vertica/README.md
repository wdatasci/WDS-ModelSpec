# WDS-Vertica
Supporting Vertica utilities.

Vertica is a columnar-based database with several very helpful constructs.

# SQL
SQL general queries and snippets.

# UDF-SQL
SQL based UDFs. Each sql file contains supporting code, some examples include:
<ul>
<li>casters.sql</li> A few cast-ing wrappers used in other UDFs.
<li>conditionals.sql</li> Simple conditional functions missing in Vertica, such as an 
Excel-like if(condition,then,else). (Also used in other UDFs.)
<li>MonthID.sql</li> Date utilities and a simple month indenifier, 12(y-2000)+m.
<li>finance.sql</li> Base payment functions mirroring Excel's PMT, PV, FV.
<li>page-labels.sql</li> Basic grouping labels.
</ul>



# UDF-Cpp
C++ based UDFs, primarily UDTFs (User Defined Transformation Functions).
These UDTFs can take tables and produce tables with additional or different columns
and possibly a different number of rows.  As with analytic functions, UDTFs can be 
employed with partitioned-by and ordered-by groups.   For applications such as 
loan-level asset backed finance, where large datasets are panel based, i.e., the 
table is comprised of multiple time-series blocks, one for each loan.   The DBMS can 
deliver to the UDTF partitioned loan blocks ordered by reporting period or loan age.
This enables an extremely efficient processing of the entire loan history for purposes
including data scrubbing and new field creation.


Example projects include:
<ul>
<li>RawBones</li> A simple UDTF build directory for function which creates a contiguous 
sequence for each subject.  This is often used to create a <i>bones</i> structure for 
joining multiple month-based datasets that may have gaps.  RawBones is also an example of 
a polymorphic call.
<li>Bones</li> A generalizable version of RawBones that serves as a prototype for other 
custom functions.  In this example, a configuration XML is used to define the inputs, 
outputs, and other parameters.  XSL transformations provide the generized wrappers for 
the guts of the function.  Put simply, define the columns you want and the guts of the 
function and let the XSL take care of the pedantic ugly parts.
</ul>

# UNDER CONSTRUCTION
Supporting libraries are added periodically.

