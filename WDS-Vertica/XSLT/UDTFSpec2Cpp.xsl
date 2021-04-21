<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="text"/>
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
        <xsl:variable name="BlockID" select=".//Column[@Special='BlockID']/@Name"/>
        <!--Pull local parameters BEGIN-->

#include "Vertica.h"
#include &lt;string&gt;

using namespace Vertica;
using namespace std;

class <xsl:value-of select="$ProjectName"/>_Core : public TransformFunction
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
            const VString* <xsl:value-of select="@Name"/>=NULL; //"<xsl:value-of select="@Default"/>";
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
                        try { <xsl:value-of select="@Name"/> = paramReader.getStringPtr("<xsl:value-of select="@Name"/>").str();} 
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


            <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I' or @Use='O']">
            <xsl:if test="@Static='Y' or @Static='Yes' or @Static='YES' or @Static='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        vint <xsl:value-of select="@Name"/>=vint_null;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        vfloat <xsl:value-of select="@Name"/>=vfloat_null;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        DateADT <xsl:value-of select="@Name"/>=vint_null;
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        TimeADT <xsl:value-of select="@Name"/>=vint_null;
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        vbool <xsl:value-of select="@Name"/>=vbool_null;
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        const VString* <xsl:value-of select="@Name"/>=NULL;
                    </xsl:when>
            </xsl:choose></xsl:if>
            <xsl:if test="not(@Static='Y' or @Static='Yes' or @Static='YES' or @Static='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        vector&lt;vint&gt; <xsl:value-of select="@Name"/>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        vector&lt;vfloat&gt; <xsl:value-of select="@Name"/>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        vector&lt;DateADT&gt; <xsl:value-of select="@Name"/>;
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        vector&lt;TimeADT&gt; <xsl:value-of select="@Name"/>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        vector&lt;vbool&gt; <xsl:value-of select="@Name"/>;
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        vector&lt;VString*&gt; <xsl:value-of select="@Name"/>;
                    </xsl:when>
            </xsl:choose></xsl:if>
            </xsl:for-each>


            do {

                <xsl:if test="count(./Parameters/Column[@Name='InputBlockMaxLength'])>0">
                    if (InputBlockMaxLength &gt; 0 &amp;&amp; row &gt;= InputBlockMaxLength) vt_report_error(0, "Partition by blocks are limited to InputBlockMaxLength rows", "");
                </xsl:if>

                if (row==0) {

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
                <xsl:if test="@Static='Y' or @Static='Yes' or @Static='YES' or @Static='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getIntRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getFloatRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vfloat_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getDateADTRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getTimeADTRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vint_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getBoolRef(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=vbool_null; }
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        try { <xsl:value-of select="@Name"/> = inputReader.getStringPtr(<xsl:value-of select="position()-1"/>);}
                        catch(...) { <xsl:value-of select="@Name"/>=NULL; }
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>

                }

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
                <xsl:if test="not(@Static='Y' or @Static='Yes' or @Static='YES' or @Static='1')"><xsl:choose>
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
                            try { tmp_DateADT  = inputReader.getDateADTRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_DateADT=vint_null; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_DateADT);
                        }
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        { 
                            TimeADT tmp_TimeADT;
                            try { tmp_TimeADT  = inputReader.getTimeADTRef(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_TimeADT=vint_null; }
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
                            VString* tmp_VString;
                            try { tmp_VString  = inputReader.getStringPtr(<xsl:value-of select="position()-1"/>);} catch(...) { tmp_VString=NULL; }
                            <xsl:value-of select="@Name"/>.push_back(tmp_VString);
                        }
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>

                row++;
            } while (inputReader.next());

            last_row=row;

            //////// read in guts
            //////// begin

            #include "../../src/<xsl:value-of select="$ProjectName"/>_guts.cpp"
            
            //////// end


            //////// in general, an output block
            for (row=first_row;row&lt;last_row;row++) {

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']">
                <xsl:if test="@Static='Y' or @Static='Yes' or @Static='YES' or @Static='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        outputWriter.setInt(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        outputWriter.setFloat(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        outputWriter.setDateADT(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputWriter.setTimeADT(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        outputWriter.setBool(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>);
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        {
                            VString&amp; tmp_VString=outputWriter.getStringRef(<xsl:value-of select="position()-1"/>);
                            if ( <xsl:value-of select="@Name"/>==NULL ) tmp_VString.setNull();
                            else if ( (*<xsl:value-of select="@Name"/>).isNull() ) tmp_VString.setNull();
                            else tmp_VString.copy(*<xsl:value-of select="@Name"/>);
                        }
                    </xsl:when>
                </xsl:choose></xsl:if>
                <xsl:if test="not(@Static='Y' or @Static='Yes' or @Static='YES' or @Static='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        outputWriter.setInt(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        outputWriter.setFloat(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        outputWriter.setDateADT(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputWriter.setTimeADT(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        outputWriter.setBool(<xsl:value-of select="position()-1"/>, <xsl:value-of select="@Name"/>[row]);
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        {
                            VString&amp; tmp_VString=outputWriter.getStringRef(<xsl:value-of select="position()-1"/>);
                            if ( <xsl:value-of select="@Name"/>[row]==NULL ) tmp_VString.setNull();
                            else if ( (*<xsl:value-of select="@Name"/>[row]).isNull() ) tmp_VString.setNull();
                            else tmp_VString.copy(*<xsl:value-of select="@Name"/>[row]);
                        }
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>


                outputWriter.next();

            }

        ////// general wrapping up
        } catch(exception&amp; e) {
            // Standard exception. Quit.
            vt_report_error(0, "Exception while processing partition: [%s]", e.what());
        }
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
                        argTypes.addDateADT(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        argTypes.addTimeADT(); // <xsl:value-of select="@Name"/>
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
                        returnType.addDateADT(); // <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        returnType.addTimeADT(); // <xsl:value-of select="@Name"/>
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
                        outputTypes.addDateADT("<xsl:value-of select="@Name"/>");
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputTypes.addTimeADT("<xsl:value-of select="@Name"/>");
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
            parameterTypes.addDateADT("<xsl:value-of select="@Name"/>");
</xsl:when><xsl:when test="@DTyp='DTm'">
            parameterTypes.addTimeADT("<xsl:value-of select="@Name"/>");
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
    return vt_createFuncObject&lt;<xsl:value-of select="$ProjectName"/>_Core&gt;(srvInterface.allocator); 
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
