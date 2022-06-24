<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="runtemplate" select="'UDTF_SQLCall'"/>
    <xsl:param name="language" select="'C++'"/>
    <xsl:param name="pathtobuild" select="'./build'"/>
    <xsl:output method="text"/>
    <xsl:decimal-format 
        decimal-separator="."
        grouping-separator=","
        infinity=" NaN "
        NaN=" NaN "
        />
    <!--Pull global parameters BEGIN-->
    <!--Pull global parameters END-->

<xsl:template name="UDTF_SQLCall">
        <!--Pull local parameters BEGIN-->
        <xsl:variable name="Schema" select="Info/SQL/Vertica/@Schema"/>
        <xsl:variable name="ProjectName" select="@Name"/>
        <xsl:variable name="BlockID" select=".//Column[count(@BlockID)>0]/@Name"/>
        <xsl:variable name="RowID" select=".//Column[count(@RowID)>0]/@Name"/>
        <!--Pull local parameters BEGIN-->



-- Example call for <xsl:value-of select="$ProjectName"/>

-----CTAS or other target code-----
create local temporary table x
on commit preserve rows as

select <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>(<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:text>
        </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:value-of select="@Name"/>::<xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">integer</xsl:when>
                    <xsl:when test="@DTyp='Dbl'">float</xsl:when>
                    <xsl:when test="@DTyp='Dte'">date</xsl:when>
                    <xsl:when test="@DTyp='DTm'">datetime</xsl:when>
                    <xsl:when test="@DTyp='Bln'">boolean</xsl:when>
                    <xsl:when test="@DTyp='Str'">char(<xsl:value-of select="@Length"/>)</xsl:when>
                    <xsl:when test="@DTyp='VLS'">varchar</xsl:when>
            </xsl:choose></xsl:for-each>

<xsl:if test="count(./Parameters/Column)>0">
    using parameters <xsl:for-each select="./Parameters/Column"><xsl:text>
        </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:choose>
        <xsl:when test="@DTyp='Int' or @DTyp='Lng' or @DTyp='Dbl' or @DTyp='Bln'"><xsl:value-of select="@Name"/>=(<xsl:value-of select="@Default"/>)</xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'"><xsl:value-of select="@Name"/>="<xsl:value-of select="@Default"/>"</xsl:when></xsl:choose>
</xsl:for-each>
</xsl:if>
            ) over (partition by <xsl:value-of select="$BlockID"/> order by <xsl:value-of select="$RowID"/>)
from (

   --------------add source query here------------------
   --------------add source query here------------------
   --------------add source query here------------------

   <xsl:value-of select="Info/SQL/Vertica/TestSourceBody"/>

   ) a


-----other wrap up code-----
a order by <xsl:value-of select="$BlockID"/>, <xsl:value-of select="$RowID"/>
----- partitioned by <xsl:value-of select="$BlockID"/>
segmented by hash(<xsl:value-of select="$BlockID"/>) all nodes
;

create local temporary table xstatic
on commit preserve rows as

select <xsl:for-each select="./Columns/Column[(@Use='IO' or @Use='O') and ((count(@BlockID)>0) or (count(@Static)>0))]"><xsl:text>
    </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:value-of select="@Name"/></xsl:for-each>
from x 
--When creating a panel dataset table, the where-clause to pull static output columns
<xsl:value-of select="./Info/SQL/PanelDataSet/OutputStaticRowIndicator"/>
--this is simpler than adding a distinct statement, but <xsl:value-of select="$ProjectName"/>_guts must define the indictator
order by <xsl:value-of select="$BlockID"/>
unsegmented all nodes

;

create local temporary table xts
on commit preserve rows as

select <xsl:for-each select="./Columns/Column[(@Use='IO' or @Use='O') and ((count(@BlockID)>0) or (count(@Static)=0))]"><xsl:text>
    </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:value-of select="@Name"/></xsl:for-each>
a order by <xsl:value-of select="$BlockID"/>, <xsl:value-of select="$RowID"/>
----- partitioned by <xsl:value-of select="$BlockID"/>
segmented by hash(<xsl:value-of select="$BlockID"/>) all nodes

;

-- Example call for <xsl:value-of select="$ProjectName"/>

/*
select 'this_EnvObject = EnvObject().From('<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:text>
        </xsl:text><xsl:if test="position()>1">|| ', ' </xsl:if>
        <xsl:choose><xsl:when test="count(@Static)>0">|| '<xsl:value-of select="@Name"/>=' || </xsl:when><xsl:otherwise>|| '<xsl:value-of select="@Name"/>=[' ||</xsl:otherwise></xsl:choose>
        <xsl:choose>
            <xsl:when test="@DTyp='Int' or @DTyp='Lng'">ifNotNullIntAsVarChar(<xsl:value-of select="@Name"/>, 'NULL'::varchar)</xsl:when>
            <xsl:when test="@DTyp='Dbl'">ifNotNullDblAsVarChar(<xsl:value-of select="@Name"/> , 'NaN'::varchar)</xsl:when>
            <xsl:when test="@DTyp='Dte'">'datetime.date.fromisoformat(' || ifNotNullDteAsVarChar(<xsl:value-of select="@Name"/>::date , '1900-01-01'::varchar) || ')'</xsl:when>
            <xsl:when test="@DTyp='DTm'">'datetime.datetime.fromisoformat(' || ifNotNullDTmAsVarChar(<xsl:value-of select="@Name"/>::timestamp , '1900-01-01 00:00:00'::varchar) || ')'</xsl:when>
            <xsl:when test="@DTyp='Bln'">ifNotNullBlnAsVarChar(<xsl:value-of select="@Name"/> , 'NaB'::varchar)</xsl:when>
            <xsl:when test="@DTyp='Str' or @DTyp='VLS'">'"' || ifNotNullVarCharAsVarChar(trim(<xsl:value-of select="@Name"/>)::varchar, ''::varchar) ||'"'</xsl:when>
            </xsl:choose>
            <xsl:choose><xsl:when test="count(@Static)>0"></xsl:when><xsl:otherwise>|| ']'</xsl:otherwise></xsl:choose>
            </xsl:for-each>|| ') '
from (
   <xsl:value-of select="Info/SQL/Vertica/TestSourceBody"/>

   ) a


-----other wrap up code-----
a order by <xsl:value-of select="$BlockID"/>, <xsl:value-of select="$RowID"/>
;

<xsl:value-of select="$ProjectName"/>_local_env = EnvObject.From(<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:text>
        </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:value-of select="@Name"/> = <xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">Int_null</xsl:when>
                    <xsl:when test="@DTyp='Dbl'">Dbl_null</xsl:when>
                    <xsl:when test="@DTyp='Dte'">Dte_null</xsl:when>
                    <xsl:when test="@DTyp='DTm'">DTm_null</xsl:when>
                    <xsl:when test="@DTyp='Bln'">Bln_null</xsl:when>
                    <xsl:when test="@DTyp='Str'">""</xsl:when>
                    <xsl:when test="@DTyp='VLS'">""</xsl:when>
            </xsl:choose></xsl:for-each>
<xsl:if test="count(./Parameters/Column)>0">
    using parameters <xsl:for-each select="./Parameters/Column"><xsl:text>
        </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:choose>
        <xsl:when test="@DTyp='Int' or @DTyp='Lng' or @DTyp='Dbl' or @DTyp='Bln'"><xsl:value-of select="@Name"/>=(<xsl:value-of select="@Default"/>)</xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'"><xsl:value-of select="@Name"/>="<xsl:value-of select="@Default"/>"</xsl:when></xsl:choose>
</xsl:for-each>
</xsl:if>
)
*/

</xsl:template>

<xsl:template name="UDTF_SQLInstall">
        <!--Pull local parameters BEGIN-->
        <xsl:variable name="Schema" select="Info/SQL/Vertica/@Schema"/>
        <xsl:variable name="ProjectName" select="@Name"/>
        <!--Pull local parameters BEGIN-->

drop library if exists <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/> cascade;
drop library if exists <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/> cascade;
drop library if exists <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>_lib cascade;

<xsl:choose>
<xsl:when test="$language='C++'">
\set libfile '\'<xsl:value-of select="$pathtobuild"/>/<xsl:value-of select="$ProjectName"/>.so\''
\set libdepends ''
</xsl:when>
<xsl:when test="$language='Java'">
\set libfile '\''`pwd`'/<xsl:value-of select="$pathtobuild"/>/<xsl:value-of select="$ProjectName"/>.jar\''
\set libdepends ''
</xsl:when>
<xsl:when test="$language='Python'">
\set libfile '\'<xsl:value-of select="$pathtobuild"/>/<xsl:value-of select="$ProjectName"/>.py\''
\set libdepends ' depends \'<xsl:value-of select="$pathtobuild"/>/depends<xsl:if test="count(Info/Python/Depends/Depend)>0" ><xsl:for-each select='Info/Python/Depends/Depend'>:<xsl:value-of select="."/></xsl:for-each></xsl:if>\''
</xsl:when>
</xsl:choose>
create library <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>_lib as :libfile 
:libdepends 
language '<xsl:value-of select="$language"/>' 
;
grant all extend on all functions in schema public to dbadmin;
grant all on library <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>_lib to dbadmin;
/*grant usage on schema <xsl:value-of select="$Schema"/> to public;*/
grant usage on library <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>_lib to public;
create transform function <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/> as name '<xsl:value-of select="$ProjectName"/>_Factory' library <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>_lib
<xsl:if test="$language='C++'"> fenced </xsl:if>;
grant all extend on all functions in schema public to dbadmin;
grant execute on all functions in schema public to public;

/*
comment on transform function <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>(<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:text>
        </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:value-of select="@Name"/><xsl:text>    </xsl:text><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">integer</xsl:when>
                    <xsl:when test="@DTyp='Dbl'">float</xsl:when>
                    <xsl:when test="@DTyp='Dte'">date</xsl:when>
                    <xsl:when test="@DTyp='DTm'">datetime</xsl:when>
                    <xsl:when test="@DTyp='Bln'">boolean</xsl:when>
                    <xsl:when test="@DTyp='Str'">char(<xsl:value-of select="@Length"/>)</xsl:when>
                    <xsl:when test="@DTyp='VLS'">varchar</xsl:when>
            </xsl:choose></xsl:for-each>
) is '<xsl:value-of select="./Info/SQL/Comment"/>';
*/

</xsl:template>

<xsl:template name="UDTF_SQLUnInstall">
        <!--Pull local parameters BEGIN-->
        <xsl:variable name="Schema" select="Info/SQL/Vertica/@Schema"/>
        <xsl:variable name="ProjectName" select="@Name"/>
        <!--Pull local parameters BEGIN-->

/*
\set ON_ERROR_STOP off
comment on transform function <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>() is null;
comment on transform function <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>(<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:text>
        </xsl:text><xsl:if test="position()>1">, </xsl:if><xsl:value-of select="@Name"/><xsl:text>    </xsl:text><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">integer</xsl:when>
                    <xsl:when test="@DTyp='Dbl'">float</xsl:when>
                    <xsl:when test="@DTyp='Dte'">date</xsl:when>
                    <xsl:when test="@DTyp='DTm'">datetime</xsl:when>
                    <xsl:when test="@DTyp='Bln'">boolean</xsl:when>
                    <xsl:when test="@DTyp='Str'">char(<xsl:value-of select="@Length"/>)</xsl:when>
                    <xsl:when test="@DTyp='VLS'">varchar</xsl:when>
            </xsl:choose></xsl:for-each>
) is null;
\set ON_ERROR_STOP on
*/

drop library if exists <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/> cascade;
drop library if exists <xsl:value-of select="$Schema"/>.<xsl:value-of select="$ProjectName"/>_lib cascade;


</xsl:template>



    <xsl:template match="/">
        <xsl:for-each select="/UDxs/UDTF">
            <xsl:choose>
                <xsl:when test="$runtemplate='UDTF_SQLCall'"><xsl:call-template name="UDTF_SQLCall"/></xsl:when>
                <xsl:when test="$runtemplate='UDTF_SQLInstall'"><xsl:call-template name="UDTF_SQLInstall"/></xsl:when>
                <xsl:when test="$runtemplate='UDTF_SQLUnInstall'"><xsl:call-template name="UDTF_SQLUnInstall"/></xsl:when>
                <xsl:otherwise><xsl:call-template name="UDTF_SQLCall"/></xsl:otherwise>
            </xsl:choose>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>
