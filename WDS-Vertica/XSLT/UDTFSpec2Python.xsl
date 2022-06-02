<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
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

<xsl:template name="UDTF_Python">
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
        class TransformFunction:
            pass
        class TransformFunctionFactory:
            pass


<xsl:if test="$ProcessEnums != 'Only' and $ProcessUtils != 'Only'">
try:
    from <xsl:value-of select="@Name"/>_Utils import *
    from <xsl:value-of select="@Name"/>_guts import *
    from <xsl:value-of select="@Name"/>_Enums import *
except:
    from build.<xsl:value-of select="@Name"/>_Utils import *
    from build.<xsl:value-of select="@Name"/>_guts import *
    from build.<xsl:value-of select="@Name"/>_Enums import *

import numpy as np

import datetime

</xsl:if>

<xsl:if test="$ProcessUtils='Yes' or $ProcessUtils='Only'">

import numpy as np

vint_null=np.iinfo(np.int64).min
Int_null=vint_null
vfloat_null=np.nan
Dbl_null=vfloat_null
vbool_null=None
Bln_null=False
vbool_false=False
vbool_true=True
Dte_null=np.datetime64('NaT','s')
DTm_null=np.datetime64('NaT','s')
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


</xsl:if>


<xsl:if test="$ProcessEnums='Yes' or $ProcessEnums='Only'">

import enum

<xsl:for-each select="//Enums/Enum">
class <xsl:value-of select="@Name"/>_Base(object):
    def __new__(cls<xsl:for-each select="EnumFields/EnumField">, <xsl:value-of select="@Name"/>=None </xsl:for-each>):
        obj = object.__new__(cls)
        <xsl:for-each select="EnumFields/EnumField">
        obj._<xsl:value-of select="@Name"/>_ = <xsl:value-of select='@Name'/>
        </xsl:for-each>
        return obj

class <xsl:value-of select="@Name"/>(<xsl:value-of select="@Name"/>_Base, enum.Enum):
    <xsl:for-each select="EnumValue">
    <xsl:variable name="EV" select="@Name"/><xsl:text>
    
    </xsl:text><xsl:value-of select="$EV"/> = ( <xsl:for-each select="../EnumFields/EnumField"><xsl:variable name="EFN" select="@Name"/><xsl:variable name="EFT" select="@DTyp"/>
        <xsl:for-each select="../../EnumValue[@Name=$EV]/@*[name(.)=$EFN]">
            <xsl:choose><xsl:when test="$EFT='Str' or $EFT='VLS'">"<xsl:value-of select="."/>", </xsl:when>
            <xsl:otherwise><xsl:value-of select="."/>, </xsl:otherwise></xsl:choose>
        </xsl:for-each>
    </xsl:for-each>)
    </xsl:for-each>

    def bIn(self,*args):
        for a in args:
            if self.__class__ is a.__class__:
                if self is a:
                    return True
        return False

    is_in = bIn

    def __repr__(self):
        return self.name

    mGet_Label=__repr__

    Label=__repr__

    @classmethod
    def LabelFor(cls,arg):
        if arg.__class__ is cls:
            return arg.name
        raise(Exception(f"{cls} classmethod LabelFor not available for {arg}"))

    @classmethod
    def mFrom_Label(cls,arg):
        try:
            return cls.__members__[arg]
        except:
            raise(Exception(f"{cls} classmethod mFrom_Label not available for {arg}"))

    mFrom=mFrom_Label

    <xsl:if test="count(EnumFields/EnumField[@Name='Index'])>0">
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.name == other.name
        if other.__class__ is str:
            return self.name == other
        return NotImplemented
    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.value._Index_ &gt;= other.value._Index_
        return NotImplemented
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value._Index_ &gt; other.value._Index_
        return NotImplemented
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.value._Index_ &lt;= other.value._Index_
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value._Index_ &lt; other.value._Index_
        return NotImplemented
    </xsl:if>
    
    <xsl:for-each select="EnumFields/EnumField">
    def mGet_<xsl:value-of select="@Name"/>(self):
        return self.value._<xsl:value-of select="@Name"/>_

    <xsl:value-of select="@Name"/> = mGet_<xsl:value-of select="@Name"/>

    @classmethod
    def mFrom_<xsl:value-of select="@Name"/>(arg):
        for a in cls.__members__:
            if cls.__members__[a].value._<xsl:value-of select="@Name"/>_ == arg:
                return cls.__members__[a]
        raise(Exception(f"<xsl:value-of select="../../../@Name"/> does not have EnumField <xsl:value-of select="@Name"/> value for {arg}"))

    def bEq_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is arg.__class__:
            return (self.value._<xsl:value-of select="@Name"/>_ == arg.value._<xsl:value-of select="@Name"/>_)
        return (self.value._<xsl:value-of select="@Name"/>_ == arg)

    def bLt_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is arg.__class__:
            return (self.value._<xsl:value-of select="@Name"/>_ &lt; arg.value._<xsl:value-of select="@Name"/>_)
        return (self.value._<xsl:value-of select="@Name"/>_ &lt; arg)

    def bLtEq_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is arg.__class__:
            return (self.value._<xsl:value-of select="@Name"/>_ &lt;= arg.value._<xsl:value-of select="@Name"/>_)
        return (self.value._<xsl:value-of select="@Name"/>_ &lt;= arg)

    def bGt_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is arg.__class__:
            return (self.value._<xsl:value-of select="@Name"/>_ &gt; arg.value._<xsl:value-of select="@Name"/>_)
        return (self.value._<xsl:value-of select="@Name"/>_ &gt; arg)

    def bGtEq_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is arg.__class__:
            return (self.value._<xsl:value-of select="@Name"/>_ &gt;= arg.value._<xsl:value-of select="@Name"/>_)
        return (self.value._<xsl:value-of select="@Name"/>_ &gt;= arg)

    def bMaxWith_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is not arg.__class__:
            larg=cls.mFrom_<xsl:value-of select="@Name"/>(arg)
        else:
            larg=arg
        if larg.bGt_<xsl:value-of select="@Name"/>(self):
            return larg
        return self

    def bMinWith_<xsl:value-of select="@Name"/>(self, arg):
        if self.__class__ is not arg.__class__:
            larg=cls.mFrom_<xsl:value-of select="@Name"/>(arg)
        else:
            larg=arg
        if larg.bLt_<xsl:value-of select="@Name"/>(self):
            return larg
        return self

    </xsl:for-each>
</xsl:for-each>

</xsl:if>

<xsl:if test="$ProcessEnums !='Only' and $ProcessUtils !='Only'">

#//////// read in any topmatter
#//////// begin

##include "../../src/<xsl:value-of select="$ProjectName"/>_topmatter.cpp"

#//////// end




class <xsl:value-of select="$ProjectName"/>(vertica_sdk.TransformFunction):

    def __init__(self, srvInterface):
        #//Localized parameters
<xsl:if test="count(./Parameters/Column)>0">
        self.local_parameters=df_row_ref(np.recarray((1,), dtype=[<xsl:for-each select="./Parameters/Column"><xsl:choose>
        <xsl:when test="@DTyp='Int' or @DTyp='Lng'">('<xsl:value-of select="@Name"/>', np.int64),</xsl:when>
        <xsl:when test="@DTyp='Dbl'">('<xsl:value-of select="@Name"/>', np.float64),</xsl:when>
        <xsl:when test="@DTyp='Bln'">('<xsl:value-of select="@Name"/>', np.bool),</xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">('<xsl:value-of select="@Name"/>', 'O'),</xsl:when></xsl:choose>
</xsl:for-each>]), 0)
</xsl:if>
<xsl:if test="count(./Parameters/Column)>0">
        <xsl:for-each select="./Parameters/Column">
        self.local_parameters.<xsl:value-of select="@Name"/>=<xsl:choose><xsl:when test="@DTyp='Int' or @DTyp='Lng'"><xsl:if test="@Default='NULL'">vint_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Dbl'"><xsl:if test="@Default='NULL'">vfloat_null</xsl:if><xsl:if test="@Default != 'NULL'"><xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Bln'"><xsl:if test="@Default='NULL'">vbool_null</xsl:if><xsl:if test="@Default != 'NULL'">vbool_<xsl:value-of select="@Default"/></xsl:if></xsl:when>
        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">"<xsl:value-of select="@Default"/>"</xsl:when></xsl:choose>
</xsl:for-each>
</xsl:if>

        <xsl:if test="count(./Parameters/Column)>0">

        paramReader = srvInterface.getParamReader()           
            <xsl:for-each select="./Parameters/Column">
        if paramReader.containsParameter("<xsl:value-of select="@Name"/>"):<xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getInt("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getFloat("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getBool("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
            self.local_parameters.<xsl:value-of select="@Name"/> = paramReader.getString("<xsl:value-of select="@Name"/>") 
                    </xsl:when>
            </xsl:choose></xsl:for-each>
        </xsl:if>

    def processPartition(self, srvInterface, inputReader, outputWriter):

        try:# {


            row=0
            rowM1=-1
            first_row=0
            last_row=-1

            row_to_output=[]
            row_index_last=[]
            row_index_next=[]

            static = df_row_ref(np.recarray((1,), dtype=[<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I' or @Use='T']">
            <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        ("<xsl:value-of select="@Name"/>", np.int64), </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        ("<xsl:value-of select="@Name"/>", np.float64), </xsl:when>
                    <xsl:when test="@DTyp='Dte' or @DTyp='DTm'">
                        ("<xsl:value-of select="@Name"/>", 'datetime64[s]'), </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        ("<xsl:value-of select="@Name"/>", np.bool), </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        ("<xsl:value-of select="@Name"/>", 'O'), </xsl:when>
            </xsl:choose></xsl:if>
            </xsl:for-each>
                        ])
                        , 0)

            <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I' or @Use='O' or @Use='T']">
            <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'">
            static.<xsl:value-of select="@Name"/> = <xsl:choose><xsl:when test="@InitValue!='NULL'">
                        <xsl:choose><xsl:when test="@DTyp='Str' or @DTyp='VLS'">"<xsl:value-of select="@InitValue"/>"</xsl:when>
                        <xsl:otherwise><xsl:value-of select="@InitValue"/></xsl:otherwise></xsl:choose></xsl:when>
                        <xsl:otherwise><xsl:value-of select='@DTyp'/>_null
                        </xsl:otherwise></xsl:choose>
                        </xsl:if></xsl:for-each>

            <xsl:if test="count(./Columns/Column[(@Use='IO' or @Use='I' or @Use='O' or @Use='T') 
                    and (count(@Static)=0 or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'))])>0">
            tv = df_row_ref(np.array([(<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I' or @Use='O' or @Use='T']">
            <xsl:if test="count(@Static)=0 or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                        <xsl:when test="@InitValue!='NULL'">
                        <xsl:choose><xsl:when test="@DTyp='Str' or @DTyp='VLS'">"<xsl:value-of select="@InitValue"/>",</xsl:when>
                        <xsl:otherwise><xsl:value-of select="@InitValue"/>,</xsl:otherwise></xsl:choose></xsl:when>
                        <xsl:otherwise><xsl:value-of select="@DTyp"/>_null,</xsl:otherwise></xsl:choose>
                        </xsl:if></xsl:for-each>) for x in range(0, inputReader.getNumRows()) ],
                        dtype=[<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I' or @Use='O' or @Use='T']">
            <xsl:if test="count(@Static)=0 or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        ("<xsl:value-of select="@Name"/>", np.int64),</xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        ("<xsl:value-of select="@Name"/>", np.float64),</xsl:when>
                    <xsl:when test="@DTyp='Dte' or @DTyp='DTm'">
                        ("<xsl:value-of select="@Name"/>", 'datetime64[s]'),</xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        ("<xsl:value-of select="@Name"/>", np.bool),</xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        ("<xsl:value-of select="@Name"/>", 'O'),</xsl:when>
            </xsl:choose></xsl:if>
            </xsl:for-each>
                        ]).view(np.recarray).copy()
                        , 0)
            </xsl:if>
            tv_empty_copy=tv.copy()

            #//Vertica::log("WDS-Message: hey");
            #//WDSThrow("Huh");

            try:# {
                while True:

                <xsl:if test="count(./Parameters/Column[@Name='InputBlockMaxLength'])>0">
                    if (self.local_parameters.InputBlockMaxLength &gt; 0 and row &gt;= self.local_parameters.InputBlockMaxLength) :
                        vt_report_error(0, "Partition by blocks are limited to InputBlockMaxLength rows", "")
                </xsl:if>

                    if row==0:#{

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
                <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                        try:# { 
                            static.<xsl:value-of select="@Name"/> = inputReader.getInt(<xsl:value-of select="position()-1"/>)
                        #}
                        except Exception as e:
                            static.<xsl:value-of select="@Name"/> = <xsl:value-of select="@DTyp"/>_null
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                        try:# { 
                            static.<xsl:value-of select="@Name"/> = inputReader.getFloat(<xsl:value-of select="position()-1"/>)
                        #}
                        except Exception as e:
                            static.<xsl:value-of select="@Name"/> = <xsl:value-of select="@DTyp"/>_null
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                        try:# { 
                            if inputReader.isNull(<xsl:value-of select="position()-1"/>):
                                static.<xsl:value-of select="@Name"/> = Dte_null
                            else:
                                static.<xsl:value-of select="@Name"/> = np.datetime64(inputReader.getDate(<xsl:value-of select="position()-1"/>).isoformat(),'s')
                        #}
                        except Exception as e:
                            static.<xsl:value-of select="@Name"/> = <xsl:value-of select="@DTyp"/>_null
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                        try:# { 
                            if inputReader.isNull(<xsl:value-of select="position()-1"/>):
                                static.<xsl:value-of select="@Name"/> = DTm_null
                            else:
                                static.<xsl:value-of select="@Name"/> = np.datetime64(inputReader.getTimeStamp(<xsl:value-of select="position()-1"/>).isoformat(),'s')
                        #}
                        except Exception as e:
                            static.<xsl:value-of select="@Name"/> = <xsl:value-of select="@DTyp"/>_null
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                        try:# { 
                            static.<xsl:value-of select="@Name"/> = inputReader.getBool(<xsl:value-of select="position()-1"/>)
                        #}
                        except Exception as e:
                            static.<xsl:value-of select="@Name"/> = <xsl:value-of select="@DTyp"/>_null
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                        try:# { 
                            static.<xsl:value-of select="@Name"/> = inputReader.getString(<xsl:value-of select="position()-1"/>)
                        #}
                        except Exception as e:
                            static.<xsl:value-of select="@Name"/> = <xsl:value-of select="@DTyp"/>_null
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>

                        row_to_output.append(True)
                        row_index_last.append(vint_null)
                        row_index_next.append(vint_null)

                    #} 
                    else:# {

                        row_to_output.append(True)
                        row_index_next[rowM1]=row
                        row_index_last.append(rowM1)
                        row_index_next.append(vint_null)

                    #}

            <xsl:if test="count(./Columns/Column[(@Use='IO' or @Use='I') 
                    and (count(@Static)=0 or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'))])>0">
                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I']">
                <xsl:if test="count(@Static)=0 or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                    try:
                        tmp_vint  = inputReader.getInt(<xsl:value-of select="position()-1"/>)
                    except:
                        tmp_vint = vint_null
                    tv[row].<xsl:value-of select="@Name"/> = tmp_vint
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                    try:
                        tmp_vfloat  = inputReader.getFloat(<xsl:value-of select="position()-1"/>)
                    except:
                        tmp_vfloat = vfloat_null
                    tv[row].<xsl:value-of select="@Name"/> = tmp_vfloat
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                    try:
                        if inputReader.isNull(<xsl:value-of select="position()-1"/>):
                            tmp_dte = Dte_null
                        else:
                            tmp_dte  = np.datetime64(inputReader.getDate(<xsl:value-of select="position()-1"/>).isoformat(),'s')
                    except:
                        tmp_dte = Dte_null
                    tv[row].<xsl:value-of select="@Name"/> = tmp_dte
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                    try:
                        if inputReader.isNull(<xsl:value-of select="position()-1"/>):
                            tmp_dtm = DTm_null
                        else:
                            tmp_dtm  = np.datetime64(inputReader.getTimestamp(<xsl:value-of select="position()-1"/>).isoformat(),'s')
                    except:
                        tmp_dtm = DTm_null
                    tv[row].<xsl:value-of select="@Name"/> = tmp_dtm
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                    try:
                        tmp_vbool  = inputReader.getBool(<xsl:value-of select="position()-1"/>)
                    except:
                        tmp_vbool = Bln_null
                    tv[row].<xsl:value-of select="@Name"/> = tmp_vbool
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                    try:
                        tmp_vstring  = inputReader.getString(<xsl:value-of select="position()-1"/>)
                    except:
                        tmp_vstring = Str_null
                    tv[row].<xsl:value-of select="@Name"/> = tmp_vstring
                    </xsl:when>
                </xsl:choose></xsl:if></xsl:for-each>
            </xsl:if>

                    row+=1
                    rowM1+=1
                    if not inputReader.next():
                        break


            #////// catch inputReader erros
            #} 
            except Exception as e:
                raise e

            last_row=row


            #//////// begin

            ##include "../../src/<xsl:value-of select="$ProjectName"/>_guts.cpp"
            first_row, last_row=<xsl:value-of select="$ProjectName"/>_guts(self.local_parameters, first_row, last_row, row_to_output, row_index_last, row_index_next, static, tv, tv_empty_copy)

            
            #//////// end

            #//////// in general, an output block
            row=first_row
            while (row is not None) and (row != vint_null) and (row &lt; last_row): #{
                if row_to_output[row]:

                <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']">
                <xsl:if test="translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1'"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                    try:
                        if static.<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setInt(<xsl:value-of select="position()-1"/>, static.<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                    try:
                        if static.<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setDbl(<xsl:value-of select="position()-1"/>, static.<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                    try:
                        tmp_str=str(static.<xsl:value-of select="@Name"/>)
                        if (tmp_str == 'None') or (tmp_str == 'NaT'):
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setDate(<xsl:value-of select="position()-1"/>, datetime.datetime.fromisoformat(tmp_str).date())
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                    try:
                        tmp_str=str(static.<xsl:value-of select="@Name"/>)
                        if (tmp_str == 'None') or (tmp_str == 'NaT'):
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setTimestamp(<xsl:value-of select="position()-1"/>, datetime.datetime.fromisoformat(tmp_str))
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                    try:
                        if static.<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setBool(<xsl:value-of select="position()-1"/>, static.<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                    try:
                        if static.<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setString(<xsl:value-of select="position()-1"/>, static.<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                </xsl:choose></xsl:if>
                <xsl:if test="count(@Static)=0 or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')"><xsl:choose>
                    <xsl:when test="@DTyp='Int' or @DTyp='Lng'">
                    try:
                        if tv[row].<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setInt(<xsl:value-of select="position()-1"/>, tv[row].<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Dbl'">
                    try:
                        if tv[row].<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setDbl(<xsl:value-of select="position()-1"/>, tv[row].<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Dte'">
                    try:
                        tmp_str=str(tv[row].<xsl:value-of select="@Name"/>)
                        if (tmp_str == 'None') or (tmp_str == 'NaT'):
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setDate(<xsl:value-of select="position()-1"/>, datetime.datetime.fromisoformat(tmp_str).date())
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='DTm'">
                    try:
                        tmp_str=str(tv[row].<xsl:value-of select="@Name"/>)
                        if (tmp_str == 'None') or (tmp_str == 'NaT'):
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setTimestamp(<xsl:value-of select="position()-1"/>, datetime.datetime.fromisoformat(tmp_str))
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Bln'">
                    try:
                        if (tv[row].<xsl:value-of select="@Name"/> is None) or (tv[row].<xsl:value-of select="@Name"/> == Bln_null ):
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setBool(<xsl:value-of select="position()-1"/>, tv[row].<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                    <xsl:when test="@DTyp='Str' or @DTyp='VLS'">
                    try:
                        if tv[row].<xsl:value-of select="@Name"/> is None:
                            outputWriter.setNull(<xsl:value-of select="position()-1"/>)
                        else:
                            outputWriter.setString(<xsl:value-of select="position()-1"/>, tv[row].<xsl:value-of select="@Name"/>)
                    except Exception as e:
                        raise e
                    </xsl:when>
                </xsl:choose></xsl:if>
                </xsl:for-each>

                    outputWriter.next()
                    row=row_index_next[row]
                    #}

        except Exception as e:
                    raise Exception("Exception writing output while processing partition{}, BlockID:{}, RowIndex:{}: []".format([ str(static.<xsl:value-of select="$BlockID"/>), str(row), str(e)]))

        #////// general wrapping up
        #} 


class <xsl:value-of select="$ProjectName"/>_Factory(vertica_sdk.TransformFunctionFactory):
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
    def createTransformFunction(cls, srvInterface):
        return <xsl:value-of select="$ProjectName"/>(srvInterface) 

</xsl:if>

    </xsl:template>

    <xsl:template match="/">
        <xsl:for-each select="/UDxs/UDTF">
            <xsl:call-template name="UDTF_Python"/>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>
