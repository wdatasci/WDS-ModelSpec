<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text"/>
    <xsl:strip-space elements="Enum EnumFields EnumField EnumValue Column"/>
    <xsl:decimal-format 
        decimal-separator="."
        grouping-separator=","
        infinity=" NaN "
        NaN=" NaN "
        />
    <!--Pull global parameters BEGIN-->
    <!--Pull global parameters END-->

<xsl:template name="UDTF_Cpp">
        <!--Pull local parameters BEGIN-->
        <xsl:variable name="ProjectName" select="@Name"/>
        <xsl:variable name="BlockID" select=".//Column[count(@BlockID)>0]/@Name"/>
        <xsl:variable name="BlockIDDTyp" select=".//Column[count(@BlockID)>0]/@DTyp"/>
        <xsl:variable name="RowID" select=".//Column[count(@RowID)>0]/@Name"/>
        <!--Pull local parameters BEGIN-->

#include "Vertica.h"
#include &lt;string&gt;
#include &lt;cstdarg&gt;
#include &lt;climits&gt;

using namespace Vertica;
using namespace std;

#include "WDS/Vertica/vutilities.h"

//handle any enums
//extended enums are expected to have an 'Index' named attribute/field for simple ordering

<xsl:for-each select="//Enums/Enum">
class <xsl:value-of select="@Name"/> {
public:
enum <xsl:value-of select="@Name"/>_EnumBase {
<xsl:for-each select="EnumValue">
<xsl:text>            </xsl:text><xsl:value-of select="@Name"/>,
</xsl:for-each>        };


    private:
        <xsl:value-of select="@Name"/>_EnumBase data;

    public:


        <xsl:value-of select="@Name"/>()=default;
        constexpr <xsl:value-of select="@Name"/>(<xsl:value-of select="@Name"/>_EnumBase arg) : data(arg) {}
        operator <xsl:value-of select="@Name"/>() const {return data;}
        constexpr bool operator == (<xsl:value-of select="@Name"/>_EnumBase arg) const { return (data==arg); }
        constexpr bool operator != (<xsl:value-of select="@Name"/>_EnumBase arg) const { return (data!=arg); }
        constexpr bool operator == (<xsl:value-of select="@Name"/> arg) const { return (data==arg.data); }
        constexpr bool operator != (<xsl:value-of select="@Name"/> arg) const { return (data!=arg.data); }
        bool bIn(int nArgs, ...) {
            va_list lArgs;
            va_start(lArgs, nArgs);
            bool rc=false;
            for ( int i=0; i&lt; nArgs &amp;&amp; !rc; i++ ) {
                //if ( data == (va_arg(lArgs,<xsl:value-of select="@Name"/>_EnumBase)) ) rc=true;
                if ( data == (va_arg(lArgs,int)) ) rc=true;
            }
            va_end(lArgs);
            return rc;
        }


        <xsl:if test="count(EnumFields/EnumField[@Name='Index'])=0">
        <xsl:variable name="tmpName" select="Index"/>
        static int mGet_Index(<xsl:value-of select="@Name"/>_EnumBase arg) {
            switch (arg) {<xsl:for-each select="EnumValue">
                case <xsl:value-of select="@Name"/>: return <xsl:value-of select="position()"/>;</xsl:for-each>
                //default: throw("Error in <xsl:value-of select="@Name"/> for mGet_Index"); 
                default: vt_report_error(0,"Error in <xsl:value-of select="@Name"/> for mGet_Index"); 
            }
            return 0;
            }
        int Index() { return mGet_Index(data); }

        static <xsl:value-of select="@Name"/>_EnumBase mFrom_Index(int arg) {
            <xsl:for-each select="EnumValue">
                if (arg==<xsl:value-of select="position()"/>) return <xsl:value-of select="@Name"/>;</xsl:for-each>
                //throw("Error in <xsl:value-of select="@Name"/> for mFrom_Index"); 
                vt_report_error(0,"Error in <xsl:value-of select="@Name"/> for mFrom_Name"); 
                return <xsl:value-of select="EnumValue[1]/@Name"/>;
            }

        static bool bEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_Index(arg0)==arg1);}
        static bool bLt_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_Index(arg0)&lt;arg1);}
        static bool bLtEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_Index(arg0)&lt;=arg1);}
        static bool bGt_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_Index(arg0)&gt;arg1);}
        static bool bGtEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_Index(arg0)&gt;=arg1);}

        static bool bEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, <xsl:value-of select="@Name"/>_EnumBase arg1) { 
            return (mGet_Index(arg0)==mGet_Index(arg1));}
        static bool bLt_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, <xsl:value-of select="@Name"/>_EnumBase arg1) { 
            return (mGet_Index(arg0)&lt;mGet_Index(arg1));}
        static bool bLtEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, <xsl:value-of select="@Name"/>_EnumBase arg1) { 
            return (mGet_Index(arg0)&lt;=mGet_Index(arg1));}
        static bool bGt_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, <xsl:value-of select="@Name"/>_EnumBase arg1) { 
            return (mGet_Index(arg0)&gt;mGet_Index(arg1));}
        static bool bGtEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg0, <xsl:value-of select="@Name"/>_EnumBase arg1) { 
            return (mGet_Index(arg0)&gt;=mGet_Index(arg1));}

        bool bEq_Index(int arg) { return bEq_Index(data,arg);}
        bool bLt_Index(int arg) { return bLt_Index(data,arg);}
        bool bLtEq_Index(int arg) { return bLtEq_Index(data,arg);}
        bool bGt_Index(int arg) { return bGt_Index(data,arg);}
        bool bGtEq_Index(int arg) { return bGtEq_Index(data,arg);}

        bool bEq_Index(<xsl:value-of select="@Name"/> arg) { return bEq_Index(data,arg.data);}
        bool bLt_Index(<xsl:value-of select="@Name"/> arg) { return bLt_Index(data,arg.data);}
        bool bLtEq_Index(<xsl:value-of select="@Name"/> arg) { return bLtEq_Index(data,arg.data);}
        bool bGt_Index(<xsl:value-of select="@Name"/> arg) { return bGt_Index(data,arg.data);}
        bool bGtEq_Index(<xsl:value-of select="@Name"/> arg) { return bGtEq_Index(data,arg.data);}

        bool bEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { return bEq_Index(data,arg);}
        bool bLt_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { return bLt_Index(data,arg);}
        bool bLtEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { return bLtEq_Index(data,arg);}
        bool bGt_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { return bGt_Index(data,arg);}
        bool bGtEq_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { return bGtEq_Index(data,arg);}


        <xsl:value-of select="@Name"/>_EnumBase  eMaxWith_Index(<xsl:value-of select="@Name"/> arg) { 
            if ( bLt_Index(arg) ) return arg.data; else return data; }
        <xsl:value-of select="@Name"/>_EnumBase  eMaxWith_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { 
            if ( bLt_Index(arg) ) return arg; else return data; }

        <xsl:value-of select="@Name"/>_EnumBase  eMinWith_Index(<xsl:value-of select="@Name"/> arg) { 
            if ( bGt_Index(arg) ) return arg.data; else return data; }
        <xsl:value-of select="@Name"/>_EnumBase  eMinWith_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { 
            if ( bGt_Index(arg) ) return arg; else return data; }

        void mMaxWith_Index(<xsl:value-of select="@Name"/> arg) { 
            if ( bLt_Index(arg) ) data=arg.data; }
        void mMaxWith_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { 
            if ( bLt_Index(arg) ) data=arg; }

        void mMinWith_Index(<xsl:value-of select="@Name"/> arg) { 
            if ( bGt_Index(arg) ) data=arg.data; }
        void mMinWith_Index(<xsl:value-of select="@Name"/>_EnumBase arg) { 
            if ( bGt_Index(arg) ) data=arg; }


        </xsl:if>

        <xsl:for-each select="EnumFields/EnumField">
        <xsl:variable name="tmpName" select="@Name"/>
        <xsl:choose><xsl:when test="@DTyp='Int'">
        static int mGet_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) {
            switch (arg) {<xsl:for-each select="../../EnumValue">
                case <xsl:value-of select="@Name"/>: return <xsl:value-of select="@*[name(.)=$tmpName]"/>;</xsl:for-each>
                //default: throw("Error in <xsl:value-of select="$tmpName"/> for mGet_<xsl:value-of select="../../@Name"/>"); 
                default: vt_report_error(0,"Error in <xsl:value-of select="$tmpName"/> for mGet_<xsl:value-of select="../../@Name"/>"); 
            }
            return 0;
            }
        int <xsl:value-of select="@Name"/>() { return mGet_<xsl:value-of select="@Name"/>(data); }

        static <xsl:value-of select="../../@Name"/>_EnumBase mFrom_<xsl:value-of select="@Name"/>(int arg) {
            <xsl:for-each select="../../EnumValue">
                if (arg==<xsl:value-of select="@*[name(.)=$tmpName]"/>) return <xsl:value-of select="@Name"/>;</xsl:for-each>
                //throw("Error in <xsl:value-of select="$tmpName"/> for mFrom_<xsl:value-of select="../../@Name"/>"); 
                vt_report_error(0,"Error in <xsl:value-of select="$tmpName"/> for mFrom_<xsl:value-of select="../../@Name"/>"); 
                return <xsl:value-of select="../../EnumValue[1]/@Name"/>;
            }

        static bool bEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)==arg1);}
        static bool bLt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&lt;arg1);}
        static bool bLtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&lt;=arg1);}
        static bool bGt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&gt;arg1);}
        static bool bGtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, int arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&gt;=arg1);}

        static bool bEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, <xsl:value-of select="../../@Name"/>_EnumBase arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)==mGet_<xsl:value-of select="@Name"/>(arg1));}
        static bool bLt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, <xsl:value-of select="../../@Name"/>_EnumBase arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&lt;mGet_<xsl:value-of select="@Name"/>(arg1));}
        static bool bLtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, <xsl:value-of select="../../@Name"/>_EnumBase arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&lt;=mGet_<xsl:value-of select="@Name"/>(arg1));}
        static bool bGt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, <xsl:value-of select="../../@Name"/>_EnumBase arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&gt;mGet_<xsl:value-of select="@Name"/>(arg1));}
        static bool bGtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg0, <xsl:value-of select="../../@Name"/>_EnumBase arg1) { 
            return (mGet_<xsl:value-of select="@Name"/>(arg0)&gt;=mGet_<xsl:value-of select="@Name"/>(arg1));}

        bool bEq_<xsl:value-of select="@Name"/>(int arg) { return bEq_<xsl:value-of select="@Name"/>(data,arg);}
        bool bLt_<xsl:value-of select="@Name"/>(int arg) { return bLt_<xsl:value-of select="@Name"/>(data,arg);}
        bool bLtEq_<xsl:value-of select="@Name"/>(int arg) { return bLtEq_<xsl:value-of select="@Name"/>(data,arg);}
        bool bGt_<xsl:value-of select="@Name"/>(int arg) { return bGt_<xsl:value-of select="@Name"/>(data,arg);}
        bool bGtEq_<xsl:value-of select="@Name"/>(int arg) { return bGtEq_<xsl:value-of select="@Name"/>(data,arg);}

        bool bEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { return bEq_<xsl:value-of select="@Name"/>(data,arg.data);}
        bool bLt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { return bLt_<xsl:value-of select="@Name"/>(data,arg.data);}
        bool bLtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { return bLtEq_<xsl:value-of select="@Name"/>(data,arg.data);}
        bool bGt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { return bGt_<xsl:value-of select="@Name"/>(data,arg.data);}
        bool bGtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { return bGtEq_<xsl:value-of select="@Name"/>(data,arg.data);}

        bool bEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { return bEq_<xsl:value-of select="@Name"/>(data,arg);}
        bool bLt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { return bLt_<xsl:value-of select="@Name"/>(data,arg);}
        bool bLtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { return bLtEq_<xsl:value-of select="@Name"/>(data,arg);}
        bool bGt_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { return bGt_<xsl:value-of select="@Name"/>(data,arg);}
        bool bGtEq_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { return bGtEq_<xsl:value-of select="@Name"/>(data,arg);}


        <xsl:value-of select="../../@Name"/>_EnumBase  eMaxWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { 
            if ( bLt_<xsl:value-of select="@Name"/>(arg) ) return arg.data; else return data; }
        <xsl:value-of select="../../@Name"/>_EnumBase  eMaxWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { 
            if ( bLt_<xsl:value-of select="@Name"/>(arg) ) return arg; else return data; }

        <xsl:value-of select="../../@Name"/>_EnumBase  eMinWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { 
            if ( bGt_<xsl:value-of select="@Name"/>(arg) ) return arg.data; else return data; }
        <xsl:value-of select="../../@Name"/>_EnumBase  eMinWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { 
            if ( bGt_<xsl:value-of select="@Name"/>(arg) ) return arg; else return data; }

        void mMaxWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { 
            if ( bLt_<xsl:value-of select="@Name"/>(arg) ) data=arg.data; }
        void mMaxWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { 
            if ( bLt_<xsl:value-of select="@Name"/>(arg) ) data=arg; }

        void mMinWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/> arg) { 
            if ( bGt_<xsl:value-of select="@Name"/>(arg) ) data=arg.data; }
        void mMinWith_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) { 
            if ( bGt_<xsl:value-of select="@Name"/>(arg) ) data=arg; }



        </xsl:when><xsl:when test="@DTyp='Str'">
        static string mGet_<xsl:value-of select="@Name"/>(<xsl:value-of select="../../@Name"/>_EnumBase arg) {
            switch (arg) {<xsl:for-each select="../../EnumValue">
                case <xsl:value-of select="@Name"/>: return string("<xsl:value-of select="@*[name(.)=$tmpName]"/>");</xsl:for-each>
                //default: throw("Error in <xsl:value-of select="$tmpName"/> for <xsl:value-of select="../../@Name"/>"); 
                default: vt_report_error(0,"Error in <xsl:value-of select="$tmpName"/> for <xsl:value-of select="../../@Name"/>"); 
            }
                vt_report_error(0,"Error in <xsl:value-of select="$tmpName"/> for <xsl:value-of select="../../@Name"/>"); 
            }
        string <xsl:value-of select="@Name"/>() { return mGet_<xsl:value-of select="@Name"/>(data); }
        </xsl:when></xsl:choose> 
        </xsl:for-each> <!-- EnumFields -->

        static string mGet_Label(<xsl:value-of select="@Name"/>_EnumBase arg) {
            switch (arg) {<xsl:for-each select="EnumValue">
                case <xsl:value-of select="@Name"/>: return string("<xsl:value-of select="@Name"/>");</xsl:for-each>
                //default: throw("Error in Label() for <xsl:value-of select="../../@Name"/>"); 
                default: vt_report_error(0,"Error in Label() for <xsl:value-of select="../../@Name"/>"); 
            }
            return 0;
            }
        string Label() {return mGet_Label(data);}

        static string LabelFor(<xsl:value-of select="@Name"/>_EnumBase arg) {return mGet_Label(arg);}

        //these will fail if spec.xml for this Enum does not have EnumField Name='Index' DTyp='Int'
        bool operator &lt; (<xsl:value-of select="@Name"/>&amp; arg) { return bLt_Index(arg); }
        bool operator &lt;= (<xsl:value-of select="@Name"/>&amp; arg) { return bLtEq_Index(arg); }
        bool operator &gt; (<xsl:value-of select="@Name"/>&amp; arg) { return bGt_Index(arg); }
        bool operator &gt;= (<xsl:value-of select="@Name"/>&amp; arg) { return bGtEq_Index(arg); }

        bool operator &lt; (<xsl:value-of select="@Name"/>_EnumBase arg) { return bLt_Index(arg); }
        bool operator &lt;= (<xsl:value-of select="@Name"/>_EnumBase arg) { return bLtEq_Index(arg); }
        bool operator &gt; (<xsl:value-of select="@Name"/>_EnumBase arg) { return bGt_Index(arg); }
        bool operator &gt;= (<xsl:value-of select="@Name"/>_EnumBase arg) { return bGtEq_Index(arg); }

};
</xsl:for-each>


//////// read in any topmatter
//////// begin

#include "../../src/<xsl:value-of select="$ProjectName"/>_topmatter.cpp"

//////// end




class <xsl:value-of select="$ProjectName"/> : public TransformFunction
{

//Localized parameters
<xsl:for-each select="./Parameters/Column"><xsl:choose>
        <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
            vint <xsl:value-of select="@Name"/>=(<xsl:if test="@Default='NULL'">vint_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if>);
        </xsl:when>
        <xsl:when test="@DTyp='Dbl'">
            vfloat <xsl:value-of select="@Name"/>=(<xsl:if test="@Default='NULL'">vfloat_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if>);
        </xsl:when>
        <xsl:when test="@DTyp='Bln'">
            vbool <xsl:value-of select="@Name"/>=(<xsl:if test="@Default='NULL'">vbool_null</xsl:if><xsl:if test="@Default != 'NULL'">vbool_<xsl:value-of select="@Default"/></xsl:if>);
        </xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
            string <xsl:value-of select="@Name"/>="<xsl:value-of select="@Default"/>";
    </xsl:when></xsl:choose>
</xsl:for-each>

    virtual void setup(ServerInterface &amp;srvInterface, const SizedColumnTypes &amp;argTypes)
    {
        ParamReader paramReader = srvInterface.getParamReader();            
        if (paramReader.getNumCols()&gt;0) {

            //Localized parameters
            <xsl:for-each select="./Parameters/Column"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        try { <xsl:value-of select="@Name"/> = paramReader.getIntRef("<xsl:value-of select="@Name"/>");} 
                        catch(...) { <xsl:value-of select="@Name"/> = vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        try { <xsl:value-of select="@Name"/> = paramReader.getFloatRef("<xsl:value-of select="@Name"/>");} 
                        catch(...) { <xsl:value-of select="@Name"/> = vfloat_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        try { <xsl:value-of select="@Name"/> = paramReader.getBoolRef("<xsl:value-of select="@Name"/>");} 
                        catch(...) { <xsl:value-of select="@Name"/> = vbool_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        try { <xsl:value-of select="@Name"/> = paramReader.getStringRef("<xsl:value-of select="@Name"/>").str();} 
                        catch(...) { <xsl:value-of select="@Name"/> = NULL; }
                    </xsl:when>
            </xsl:choose></xsl:for-each>

        }
    }    

    virtual void processPartition(ServerInterface &amp;srvInterface, 
            PartitionReader &amp;inputReader, 
            PartitionWriter &amp;outputWriter)
    {
        try {



            vint row=0;
            vint first_row=0;
            vint last_row=-1;

            // hold initializing output non-statics until number of  rows is known

            <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
            <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        vint <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        vfloat <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vfloat_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        DateADT <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        TimeADT <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        vbool <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vbool_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        string <xsl:value-of select="@Name"/>="<xsl:if test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:if>";
                    </xsl:when>
            </xsl:choose></xsl:if>
            <xsl:if test="not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        vector&lt;vint&gt; <xsl:value-of select="@Name"/>; //(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        vector&lt;vfloat&gt; <xsl:value-of select="@Name"/>; //(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vfloat_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        vector&lt;DateADT&gt; <xsl:value-of select="@Name"/>; //(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        vector&lt;TimeADT&gt; <xsl:value-of select="@Name"/>; //(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        vector&lt;vbool&gt; <xsl:value-of select="@Name"/>; //(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vbool_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        vector&lt;string&gt; <xsl:value-of select="@Name"/>; //(last_row-first_row, "<xsl:if test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:if>");
                    </xsl:when>
            </xsl:choose></xsl:if>
            </xsl:for-each>

            //Vertica::log("WDS-Message: hey");
            //WDSThrow("Huh");

            try {
            do {

                <xsl:if test="count(./Parameters/Column[@Name='InputBlockMaxLength'])>0">
                    if (InputBlockMaxLength &gt; 0 &amp;&amp; row &gt;= InputBlockMaxLength) vt_report_error(0, "Partition by blocks are limited to InputBlockMaxLength rows", "");
                </xsl:if>

                if (row==0) {

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
                <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getIntRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getFloatRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vfloat_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getDateRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getTimeRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getBoolRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vbool_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getStringRef(<xsl:value-of select="position()-1"/>).str();}
                        catch(...) { <xsl:value-of select="@Name"/>=""; }
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>

                }

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
                <xsl:if test="not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        { 
                            vint tmp_vint;
                            try { tmp_vint  = inputReader.getIntRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_vint=vint_null; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_vint);
                        }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        { 
                            vfloat tmp_vfloat;
                            try { tmp_vfloat  = inputReader.getFloatRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_vfloat=vfloat_null; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_vfloat);
                        }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        { 
                            DateADT tmp_DateADT;
                            try { tmp_DateADT  = inputReader.getDateRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_DateADT=vint_null; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_DateADT);
                        }
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        { 
                            TimeADT tmp_TimeADT;
                            try { tmp_TimeADT  = inputReader.getTimeRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_TimeADT=vint_null; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_TimeADT);
                        }
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        { 
                            vbool tmp_vbool;
                            try { tmp_vbool  = inputReader.getBoolRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_vbool=vbool_null; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_vbool);
                        }
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        { 
                            string tmp_VString;
                            try { tmp_VString  = inputReader.getStringRef(<xsl:value-of select="position()-1"/>).str();} catch(...) { tmp_VString=""; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_VString);
                        }
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>

                row++;
            } while (inputReader.next());

            ////// catch inputReader erros
            } 
            catch(WDSException&amp; e) { WDSThrow("Exception reading input while processing partition: [%s]", e.what()); }
            catch(exception&amp; e) { WDSThrow("Exception reading input while processing partition: [%s]", e.what()); }

            last_row=row;

            //////// initialize output only or internal(temporary) fields now that row number is known


            <xsl:for-each select="./Columns/Column[@Use='O' or @Use='T']">
            <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        vint <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        vfloat <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vfloat_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        DateADT <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        TimeADT <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        vbool <xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vbool_null</xsl:otherwise></xsl:choose>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        string <xsl:value-of select="@Name"/>="<xsl:if test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:if>";
                    </xsl:when>
            </xsl:choose></xsl:if>
            <xsl:if test="not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        vector&lt;vint&gt; <xsl:value-of select="@Name"/>(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        vector&lt;vfloat&gt; <xsl:value-of select="@Name"/>(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vfloat_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        vector&lt;DateADT&gt; <xsl:value-of select="@Name"/>(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        vector&lt;TimeADT&gt; <xsl:value-of select="@Name"/>(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vint_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        vector&lt;vbool&gt; <xsl:value-of select="@Name"/>(last_row-first_row, <xsl:choose><xsl:when test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:when><xsl:otherwise>vbool_null</xsl:otherwise></xsl:choose>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        vector&lt;string&gt; <xsl:value-of select="@Name"/>(last_row-first_row, "<xsl:if test="@InitValue!='NULL'"><xsl:value-of select="@InitValue"/></xsl:if>");
                    </xsl:when>
            </xsl:choose></xsl:if>
            </xsl:for-each>

            //////// include customized guts
            //////// begin

            #include "../../src/<xsl:value-of select="$ProjectName"/>_guts.cpp"
            
            //////// end

            //////// in general, an output block
            for (row=first_row;row&lt;last_row;row++) {
            try {

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']">
                try {
                <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        outputWriter.setInt(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        outputWriter.setFloat(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        outputWriter.setDate(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputWriter.setTime(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        outputWriter.setBool(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        {
                            VString&amp; tmp_VString=outputWriter.getStringRef(<xsl:value-of select="position()-1"/>);
                            if ( <xsl:value-of select="@Name"/>=="" ) tmp_VString.setNull();
                            else if ( <xsl:value-of select="@Name"/>.length() &gt; <xsl:value-of select="@Length"/> ) 
                                 tmp_VString.copy(<xsl:value-of select="@Name"/>.c_str(),<xsl:value-of select="@Length"/>);
                            else tmp_VString.copy(<xsl:value-of select="@Name"/>);
                        }
                    </xsl:when>
                </xsl:choose></xsl:if>
                <xsl:if test="not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        outputWriter.setInt(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        outputWriter.setFloat(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        outputWriter.setDate(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputWriter.setTime(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        outputWriter.setBool(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        {
                            VString&amp; tmp_VString=outputWriter.getStringRef(<xsl:value-of select="position()-1"/>);
                            if ( <xsl:value-of select="@Name"/>[row]=="" ) tmp_VString.setNull();
                            else if ( <xsl:value-of select="@Name"/>[row].length() &gt; <xsl:value-of select="@Length"/> ) 
                                 tmp_VString.copy(<xsl:value-of select="@Name"/>[row].c_str(),<xsl:value-of select="@Length"/>);
                            else tmp_VString.copy(<xsl:value-of select="@Name"/>[row]);
                        }
                    </xsl:when>
                </xsl:choose></xsl:if>
                } catch(exception&amp; e) { WDSThrow("Exception writing output for <xsl:value-of select="@Name"/>, DTyp=<xsl:value-of select="@DTyp"/>: [%s]", e.what()); }
                </xsl:for-each>


                outputWriter.next();

            ////// catch outputWriter erros
            } 
            catch(WDSException&amp; e) { 
            <xsl:choose>
            <xsl:when test="$BlockIDDTyp='Str' or $BlockIDDTyp='VLS'">
                WDSThrow("Exception writing output while processing partition, BlockID:%Ls, RowIndex:%Ld: [%s]", <xsl:value-of select="$BlockID"/>.c_str(), row, e.what()); 
            </xsl:when>
            <xsl:otherwise>
                WDSThrow("Exception writing output while processing partition, BlockID:%Ld, RowIndex:%Ld: [%s]", <xsl:value-of select="$BlockID"/>, row, e.what()); 
            </xsl:otherwise>
            </xsl:choose>
            }
            catch(exception&amp; e) { 
            <xsl:choose>
            <xsl:when test="$BlockIDDTyp='Str' or $BlockIDDTyp='VLS'">
                WDSThrow("Exception writing output while processing partition, BlockID:%Ls, RowIndex:%Ld: [%s]", <xsl:value-of select="$BlockID"/>.c_str(), row, e.what()); 
            </xsl:when>
            <xsl:otherwise>
                WDSThrow("Exception writing output while processing partition, BlockID:%Ld, RowIndex:%Ld: [%s]", <xsl:value-of select="$BlockID"/>, row, e.what()); 
            </xsl:otherwise>
            </xsl:choose>
            }
            }

        ////// general wrapping up
        } 
        catch (WDSException&amp; e) { vt_report_error(0, "WDSException while processing partition: [%s]",e.what()); }
        catch(exception&amp; e) { vt_report_error(0, "Exception while processing partition: [%s]", e.what()); }
    }
};


class <xsl:value-of select="$ProjectName"/>_Factory : public TransformFunctionFactory
{
    ////// a generalizable SQL signature
    virtual void getPrototype(ServerInterface &amp;srvInterface,
        ColumnTypes &amp;argTypes,
        ColumnTypes &amp;returnType
    ) {

        <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        argTypes.addInt(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        argTypes.addFloat(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        argTypes.addDate(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        argTypes.addTime(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        argTypes.addBool(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Str'">
                        argTypes.addChar(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='VLS'">
                        argTypes.addVarchar(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
        </xsl:choose></xsl:for-each>

        <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        returnType.addInt(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        returnType.addFloat(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        returnType.addDate(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        returnType.addTime(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        returnType.addBool(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Str'">
                        returnType.addChar(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='VLS'">
                        returnType.addVarchar(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
        </xsl:choose></xsl:for-each>

    }

    ////// a generalizable SQL signature
    virtual void getReturnType(ServerInterface &amp;srvInterface, 
            const SizedColumnTypes &amp;inputTypes, 
            SizedColumnTypes &amp;outputTypes
    ) {


    //string NewName=__NewName;
    //ParamReader paramReader = srvInterface.getParamReader();            
    //if (paramReader.getNumCols()&gt;0) {
    //try { NewName = paramReader.getStringRef("NewName").str();} catch(...) { }
    //}

        <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        outputTypes.addInt("<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        outputTypes.addFloat("<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        outputTypes.addDate("<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputTypes.addTime("<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        outputTypes.addBool("<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='Str'">
                        outputTypes.addChar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='VLS'">
                        outputTypes.addVarchar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>");
                    </xsl:when>
        </xsl:choose></xsl:for-each>

    }

    ////// a generalizable SQL parameter signature
    virtual void getParameterType(ServerInterface &amp;srvInterface,
        SizedColumnTypes &amp;parameterTypes
    ) {

<xsl:for-each select="./Parameters/Column"><xsl:choose>
<xsl:when test="@DTyp='Int' or @DTyp='Lng'">
            parameterTypes.addInt("<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='Dbl'">
            parameterTypes.addFloat("<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='Dte'">
            parameterTypes.addDate("<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='DTm'">
            parameterTypes.addTime("<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='Bln'">
            parameterTypes.addBool("<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='Str'">
            parameterTypes.addChar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='VLS'">
            parameterTypes.addVarchar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>");
</xsl:when></xsl:choose></xsl:for-each>

    }

    ////// required part, but of a constant form
    virtual TransformFunction *createTransformFunction(ServerInterface &amp;srvInterface
    ) { 
    return vt_createFuncObject&lt;<xsl:value-of select="$ProjectName"/>&gt;(srvInterface.allocator); 
    }

};


////// register the factory
RegisterFactory(<xsl:value-of select="$ProjectName"/>_Factory);



    </xsl:template>

    <xsl:template match="/">
        <xsl:for-each select="/UDxs/UDTF">
            <xsl:call-template name="UDTF_Cpp"/>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>
