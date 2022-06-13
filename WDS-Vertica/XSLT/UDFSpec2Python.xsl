<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="NumpyOrObject" select="Object"/>
    <xsl:param name="ProcessEnums" select="No"/>
    <xsl:param name="ProcessUtils" select="No"/>
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

<xsl:template name="UDF_Python">
        <!--Pull local parameters BEGIN-->
        <xsl:variable name="ProjectName" select="@Name"/>
        <xsl:variable name="BlockID" select=".//Column[count(@BlockID)>0]/@Name"/>
        <xsl:variable name="BlockIDDTyp" select=".//Column[count(@BlockID)>0]/@DTyp"/>
        <xsl:variable name="RowID" select=".//Column[count(@RowID)>0]/@Name"/>
        <!--Pull local parameters BEGIN-->

bUsingVerticaSDK=True
try:
    import vertica_sdk
except:
    print("not using vertica_sdk")
    bUsingVerticaSDK=False

if not bUsingVerticaSDK:
    class vertica_sdk:
        class ScalarFunction:
            pass
        class ScalarFunctionFactory:
            pass


<xsl:if test="$ProcessEnums != 'Only' and $ProcessUtils != 'Only'">
try:
    from depends.<xsl:value-of select="@Name"/>_Utils import *
    from depends.<xsl:value-of select="@Name"/>_guts import *
    #from depends.<xsl:value-of select="@Name"/>_Enums import *
except:
    from build.depends.<xsl:value-of select="@Name"/>_Utils import *
    from build.depends.<xsl:value-of select="@Name"/>_guts import *
    #from build.depends.<xsl:value-of select="@Name"/>_Enums import *

import numpy as np

import datetime
import dateutil.parser

_isoparser=dateutil.parser.isoparser()

</xsl:if>

<xsl:if test="$ProcessUtils='Yes' or $ProcessUtils='Only'">

import numpy as np

import sys
import datetime
import math

vint_null=-sys.maxsize
Int_null=vint_null

vfloat_null=math.nan
Dbl_null=vfloat_null

vbool_null=None
Bln_null=False
vbool_false=False
vbool_true=True

#Dte_null=np.datetime64('NaT','s')
Dte_null=datetime.datetime(1970,1,1,0,0,0) # UnixEpoch

#DTm_null=np.datetime64('NaT','s')
DTm_null=datetime.datetime(1970,1,1,0,0,0) # UnixEpoch

Str_null=""
VLS_null=""

def vt_report_error(code, arg1, arg2):
    raise Exception("{} {} {}".format(code, arg1, arg2))

def df_row_ref(df, row):
    class __df_row(object):
        def __getattribute__(self, field):
            if field is None:
                return df[row]
            if field == 'parent':
                return df
            if field == 'copy':
                return lambda : df_row_ref(df[row].copy(),0)
            return df[row][field]
        def __setattr__(self, field, value):
            try:
                if type(field) is tuple:
                    df.__setattr__(df, field, value)
                elif (value is None) or (type(value) is type(None)):
                    if df.dtype[field] == 'O':
                        df[row][field]=Str_null
                    elif df.dtype[field] == np.float64:
                        df[row][field]=Dbl_null
                    elif df.dtype[field] == np.int64:
                        df[row][field]=Int_null
                    elif df.dtype[field] == np.datetime64:
                        df[row][field]=DTm_null
                    else:
                        df[row][field]=None
                else:
                    if not np.can_cast(type(value),df.dtype[field]):
                        df[row][field]=value
                    elif df.dtype[field].base == np.dtype('O'):
                        if type(value) is str:
                            df[row][field]=value
                        else:
                            df[row][field]=str(value)
                    elif df.dtype[field] == np.dtype(np.float64):
                        if type(value) is np.float64:
                            df[row][field]=value
                        else:
                            df[row][field]=np.float64(value)
                    elif df.dtype[field] == np.dtype(np.int64):
                        if type(value) is np.int64:
                            df[row][field]=value
                        else:
                            df[row][field]=np.int64(value)
                    elif df.dtype[field] == np.dtype(np.datetime64):
                        if type(value) is np.datetime64:
                            df[row][field]=value
                        else:
                            df[row][field]=np.datetime64(value,'s')
                    else:
                        df[row][field]=value
            except Exception as e:
                raise(Exception(str(e)+", field=",field,", value=",value,", dtype=",str(df.dtype[field])))

        def __getitem__(self, altrow):
            if type(altrow) is tuple:
                return df.__getitem__(df, altrow)
            return df_row_ref(df, altrow)
    return  __df_row()

<xsl:if test="$NumpyOrObject = 'Object'">

class ParameterObject(object):
    def __init__(self):
<xsl:if test="count(./Parameters/Column)>0">
        <xsl:for-each select="./Parameters/Column"><xsl:text>
        </xsl:text><xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@DTyp='Int' or @DTyp='Lng'"><xsl:if test="@Default='NULL'">vint_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Dbl'"><xsl:if test="@Default='NULL'">vfloat_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Dte'"><xsl:if test="@Default='NULL'">Dte_null</xsl:if><xsl:if test="@Default != 'NULL'">_isoparser.parse_isodate("<xsl:value-of select="@Default"/>")</xsl:if></xsl:when>
        <xsl:when test="@DTyp='DTm'"><xsl:if test="@Default='NULL'">DTm_null</xsl:if><xsl:if test="@Default != 'NULL'">_isoparser.isoparse("<xsl:value-of select="@Default"/>")</xsl:if></xsl:when>
        <xsl:when test="@DTyp='Bln'"><xsl:if test="@Default='NULL'">vbool_null</xsl:if><xsl:if test="@Default != 'NULL'">vbool_<xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">"<xsl:value-of select="@Default"/>"</xsl:when></xsl:choose>
</xsl:for-each>
        vars(self).update(locals())
        vars(self).pop('self')

    def __repr__(self):
        return ('EnvObject'<xsl:for-each select="./Parameters/Column">
         +', <xsl:value-of select="@Name"/>:'+str(self.<xsl:value-of select="@Name"/>)</xsl:for-each>)
</xsl:if>



class StaticObject(object):
     def __init__(self):<xsl:for-each select="./Columns/Column[@Use='I' ]">
     <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:text>
         </xsl:text><xsl:value-of select="@Name"/> = <xsl:choose><xsl:when test="@InitValue!='NULL'">
             <xsl:choose><xsl:when test="@DTyp='Str' or @DTyp='VLS'">"<xsl:value-of select="@InitValue"/>"</xsl:when>
             <xsl:otherwise><xsl:value-of select="@InitValue"/></xsl:otherwise></xsl:choose></xsl:when>
             <xsl:otherwise><xsl:value-of select='@DTyp'/>_null
             </xsl:otherwise></xsl:choose>
             </xsl:if></xsl:for-each>
         vars(self).update(locals())
         vars(self).pop('self')

     def From(self<xsl:for-each select="./Columns/Column[@Use='I' ]">
     <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:text>
         ,</xsl:text><xsl:value-of select="@Name"/></xsl:if></xsl:for-each>
         ):
         vars(self).update(locals())
         vars(self).pop('self')
         return self
 
     def __repr__(self):
        return ('StaticObject'<xsl:for-each select="./Columns/Column[@Use='I' ]">
     <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'">
         +', '+str(self.<xsl:value-of select="@Name"/>)</xsl:if></xsl:for-each>)



</xsl:if>


 

class <xsl:value-of select="$ProjectName"/>(vertica_sdk.ScalarFunction):

    def __init__(self, srvInterface):
        #//Localized parameters
        self.local_parameters=ParameterObject()
<xsl:if test="count(./Parameters/Column)>0">
<xsl:choose>
<xsl:when test="$NumpyOrObject != 'Object'">
        self.local_parameters=df_row_ref(np.recarray((1,), dtype=[<xsl:for-each select="./Parameters/Column"><xsl:choose>
        <xsl:when test="@DTyp='Int' or @DTyp='Lng'">('<xsl:value-of select="@Name"/>', np.int64),</xsl:when>
        <xsl:when test="@DTyp='Dte' or @DTyp='Dte'">('<xsl:value-of select="@Name"/>', np.datetime64),</xsl:when>
        <xsl:when test="@DTyp='Dbl'">('<xsl:value-of select="@Name"/>', np.float64),</xsl:when>
        <xsl:when test="@DTyp='Bln'">('<xsl:value-of select="@Name"/>', np.bool),</xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">('<xsl:value-of select="@Name"/>', 'O'),</xsl:when></xsl:choose>
</xsl:for-each>]), 0)
</xsl:when>
<xsl:when test="$NumpyOrObject = 'Object'">
        self.local_parameters = ParameterObject()
</xsl:when>
</xsl:choose>
        <xsl:for-each select="./Parameters/Column">
        self.local_parameters.<xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@DTyp='Int' or @DTyp='Lng'"><xsl:if test="@Default='NULL'">vint_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Dbl'"><xsl:if test="@Default='NULL'">vfloat_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Dte'"><xsl:if test="@Default='NULL'">Dte_null</xsl:if><xsl:if test="@Default != 'NULL'">_isoparser.parse_isodate("<xsl:value-of select="@Default"/>")</xsl:if></xsl:when>
        <xsl:when test="@DTyp='DTm'"><xsl:if test="@Default='NULL'">DTm_null</xsl:if><xsl:if test="@Default != 'NULL'">_isoparser.isoparse("<xsl:value-of select="@Default"/>")</xsl:if></xsl:when>
        <xsl:when test="@DTyp='Bln'"><xsl:if test="@Default='NULL'">vbool_null</xsl:if><xsl:if test="@Default != 'NULL'">vbool_<xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">"<xsl:value-of select="@Default"/>"</xsl:when></xsl:choose>
</xsl:for-each>

        paramReader = srvInterface.getParamReader()           
            <xsl:for-each select="./Parameters/Column">
        if paramReader.containsParameter("<xsl:value-of select="@Name"/>"):<xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getInt("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getFloat("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getDate("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getTimestamp("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getBool("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getString("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
            </xsl:choose></xsl:for-each>
        </xsl:if>

    def processBlock(self, srvInterface, inputReader, outputWriter):
    
               

        try:# {


            try:# {
                while True:

                    static=StaticObject()
                    

            <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
            <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                    static.<xsl:value-of select="@Name"/> = inputReader.getInt(<xsl:value-of select="position()-1"/>)
                </xsl:when>
                <xsl:when test="@DTyp='Dbl'">
                    static.<xsl:value-of select="@Name"/> = inputReader.getFloat(<xsl:value-of select="position()-1"/>)
                </xsl:when>
                <xsl:when test="@DTyp='Dte'">
                    if inputReader.isNull(<xsl:value-of select="position()-1"/>):
                            static.<xsl:value-of select="@Name"/> = Dte_null
                    else:
                            static.<xsl:value-of select="@Name"/> = inputReader.getDate(<xsl:value-of select="position()-1"/>)
                </xsl:when>
                <xsl:when test="@DTyp='DTm'">
                    if inputReader.isNull(<xsl:value-of select="position()-1"/>):
                            static.<xsl:value-of select="@Name"/> = DTm_null
                    else:
                            static.<xsl:value-of select="@Name"/> = inputReader.getTimestamp(<xsl:value-of select="position()-1"/>)
                </xsl:when>
                <xsl:when test="@DTyp='Bln'">
                    static.<xsl:value-of select="@Name"/> = inputReader.getBool(<xsl:value-of select="position()-1"/>)
                </xsl:when>
                <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                    static.<xsl:value-of select="@Name"/> = inputReader.getString(<xsl:value-of select="position()-1"/>)
                </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>

                    rv=<xsl:value-of select="$ProjectName"/>_guts(static)


                    
                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']">
                <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                    try:
                        rv=int(rv)
                        if rv is None::
                            outputWriter.setNull()
                        else:
                            outputWriter.setInt(rv)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                    try:
                        rv=float(rv)
                        if <xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull()
                        else:
                            outputWriter.setFloat(rv)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                    try:
                        if rv is None or type(rv) is not datetime.datetime or rv &lt;=Dte_null:
                            outputWriter.setNull()
                        else:
                            if (tmp_str == 'None') or (tmp_str == 'NaT'):
                                outputWriter.setNull()
                            else:
                                outputWriter.setDate(rv.date())
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                    try:
                        if rv is None or type(rv) is not datetime.datetime or rv&lt;=Dte_null:
                            outputWriter.setNull()
                        else:
                            tmp_str=str(rv)
                            if (tmp_str == 'None') or (tmp_str == 'NaT'):
                                outputWriter.setNull()
                            else:
                                outputWriter.setTimestamp(rv)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                    try:
                        if rv is None:
                            outputWriter.setNull()
                        else:
                            outputWriter.setBool(rv)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                    try:
                        if <xsl:value-of select="@Name"/> is None or len(str(<xsl:value-of select="@Name"/>))==0:
                            outputWriter.setNull()
                        else:
                            outputWriter.setString(str(rv))
                    except Exception as e:
                        raise e
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>
                
                    outputWriter.next()
                    if not inputReader.next():
                        break

            except Exception as e:
                raise e

        except Exception as e:
                    raise Exception("Exception in <xsl:value-of select="$ProjectName"/>")

        #} 


class <xsl:value-of select="$ProjectName"/>_Factory(vertica_sdk.ScalarFunctionFactory):
    def getPrototype(self, srvInterface, argTypes, returnType):
        <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        argTypes.addInt() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        argTypes.addFloat() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        argTypes.addDate() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        argTypes.addTimestamp() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        argTypes.addBool() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Str'">
                        argTypes.addChar() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='VLS'">
                        argTypes.addVarchar() # <xsl:value-of select="@Name"/>
                    </xsl:when>
        </xsl:choose></xsl:for-each>

        <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        returnType.addInt() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        returnType.addFloat() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        returnType.addDate() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        returnType.addTimestamp() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        returnType.addBool() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='Str'">
                        returnType.addChar() # <xsl:value-of select="@Name"/>
                    </xsl:when>
                    <xsl:when test="@DTyp='VLS'">
                        returnType.addVarchar() # <xsl:value-of select="@Name"/>
                    </xsl:when>
        </xsl:choose></xsl:for-each>


    def getReturnType(self, srvInterface, inputTypes, outputTypes):
        <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        outputTypes.addInt("<xsl:value-of select="@Name"/>")
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        outputTypes.addFloat("<xsl:value-of select="@Name"/>")
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        outputTypes.addDate("<xsl:value-of select="@Name"/>")
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        outputTypes.addTimestamp(6,"<xsl:value-of select="@Name"/>")
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        outputTypes.addBool("<xsl:value-of select="@Name"/>")
                    </xsl:when>
                    <xsl:when test="@DTyp='Str'">
                        outputTypes.addChar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>")
                    </xsl:when>
                    <xsl:when test="@DTyp='VLS'">
                        outputTypes.addVarchar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>")
                    </xsl:when>
        </xsl:choose></xsl:for-each>

    #////// a generalizable SQL parameter signature
    def getParameterType(self, srvInterface, parameterTypes): <xsl:for-each select="./Parameters/Column"><xsl:choose>
<xsl:when test="@DTyp='Int' or @DTyp='Lng'">
            parameterTypes.addInt("<xsl:value-of select="@Name"/>")</xsl:when>
<xsl:when test="@DTyp='Dbl'">
            parameterTypes.addFloat("<xsl:value-of select="@Name"/>")</xsl:when>
<xsl:when test="@DTyp='Dte'">
            parameterTypes.addDate("<xsl:value-of select="@Name"/>")</xsl:when>
<xsl:when test="@DTyp='DTm'">
            parameterTypes.addTimestamp("<xsl:value-of select="@Name"/>")</xsl:when>
<xsl:when test="@DTyp='Bln'">
            parameterTypes.addBool("<xsl:value-of select="@Name"/>")</xsl:when>
<xsl:when test="@DTyp='Str'">
            parameterTypes.addChar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>")</xsl:when>
<xsl:when test="@DTyp='VLS'">
            parameterTypes.addVarchar(<xsl:value-of select="@Length"/>,"<xsl:value-of select="@Name"/>")</xsl:when>
</xsl:choose></xsl:for-each>

    #////// required part, but of a constant form
    def createScalarFunction(cls, srvInterface):
        return <xsl:value-of select="$ProjectName"/>(srvInterface) 




</xsl:if>

    </xsl:template>

    <xsl:template match="/">
        <xsl:for-each select="/UDxs/UDF">
            <xsl:call-template name="UDF_Python"/>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>
