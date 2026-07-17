<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:param name="NumpyOrObject" select="Numpy"/>
    <xsl:param name="ProcessEnums" select="No"/>
    <xsl:param name="ProcessUtils" select="No"/>
    <xsl:param name="UseNaT" select="No"/>
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


<xsl:if test="$ProcessEnums != 'Only' and $ProcessUtils != 'Only'">

import fcntl
import os
import sys
import threading
import subprocess
from pathlib import Path
import zipfile
import traceback

from _snowflake import vectorized
import pandas as pd
import numpy as np
from <xsl:value-of select="@Name"/>_Utils import *
from <xsl:value-of select="@Name"/>_Enums import *
import <xsl:value-of select="@Name"/>_guts as guts

import datetime
import dateutil.parser
_isoparser=dateutil.parser.isoparser()



</xsl:if>

<xsl:if test="$ProcessUtils='Yes' or $ProcessUtils='Only'">

import numpy as np
import math

import datetime
import dateutil.parser

import sys
import datetime
import math

from namespaceop import *
from MonthID import *


class nmspace(object):
    def __init__(self, **kwrds):
        self.__dict__.update(kwrds)

    def update(self, kwrds):
        #self.__dict__.update(kwrds)
        for k,v in kwrds.items():
            if not k.startswith('_'):
                self.__dict__[k] = v

    def update(self, **kwrds):
        #self.__dict__.update(kwrds)
        for k,v in kwrds.items():
            if not k.startswith('_'):
                self.__dict__[k] = v

    def place(self, dct):
        for k,v in self.__dict__.items():
            if not k.startswith('_'):
                dct[k] = v

    def print(self):
        for k,v in self.__dict__.items():
            print(k, v)



vint_null=-sys.maxsize
Int_null=vint_null

def IsIntNULL(arg):
    if arg is None:
        return True
    if type(arg) is bool:
        return False
    if arg == vint_null:
        return True
    try:
        if np.isnan(arg):
            return True
        else:
            return False
    except Exception as e:
        return False
    return False

vfloat_null=math.nan
Dbl_null=vfloat_null

def IsDblNULL(arg):
    if arg is None:
        return True
    try:
        if np.isnan(arg):
            return True
        else:
            return False
    except Exception as e:
        return True
    return False

vbool_null=None
Bln_null=None
vbool_false=False
vbool_true=True

# using Unix epoch just because of negative as null
<xsl:choose><xsl:when test="$UseNaT='Yes'">
Dte_null=np.datetime64("NaT")
DTm_null=np.datetime64("NaT")
    
def IsDTmNULL(arg):
    if arg is None: 
        return True
    if issubclass(type(arg), np.datetime64):
        return np.isnat(arg)
    if issubclass(type(arg),datetime.datetime):
        return False
    if issubclass(type(arg),datetime.date):
        return False
    try:
        if math.isnan(arg): return True
        return (arg &lt;= 0)
    except:
        try:
            if type(arg) is not str:
                rv=str(arg)
                if rv.lower() in ('none','na','nan','nat'): return True
            rv=dateutil.parser.parse(str(arg))
            return (rv.year &lt; 1970)
        except:
            return True

</xsl:when><xsl:otherwise>
Dte_null=datetime.datetime(1970,1,1)
Dte_null=Dte_null.replace(tzinfo=None) # UnixEpoch
DTm_null=Dte_null

def IsDTmNULL(arg):
    if arg is None: 
        return True
    if issubclass(type(arg),datetime.datetime):
        return (arg.replace(tzinfo=None) &lt;= DTm_null)
    if issubclass(type(arg),datetime.date):
        return (arg.year &lt; 1970 ) or (datetime.date(arg.year, arg.month, arg.day) == datetime.date(1970,1,1))
    try:
        if math.isnan(arg): return True
        return (arg&lt;=0)
    except:
        try:
            if type(arg) is not str:
                rv=str(arg)
                if rv.lower() in ('none','na','nan','nat'): return True
            rv=dateutil.parser.parse(str(arg))
            return (rv.year &lt; 1970)
        except:
            return True

</xsl:otherwise>
</xsl:choose>


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

from <xsl:value-of select="@Name"/>_Utils import *

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
    def mFrom_<xsl:value-of select="@Name"/>(cls, arg):
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

# Get the location of the import directory. Snowflake sets the import
# directory location so code can retrieve the location via sys._xoptions.
IMPORT_DIRECTORY_NAME = "snowflake_import_directory"
import_dir = sys._xoptions[IMPORT_DIRECTORY_NAME]
sys.path.insert(0,import_dir)
os.environ['LD_LIBRARY_PATH'] = import_dir

<xsl:value-of select="./Info/Python/Depends[@SQL='Snowflake']/module_head"/>

<xsl:if test="count(./Info/Python/Depends[@SQL='Snowflake']/Imports/@ExtractedTo)>0">

# File lock class for synchronizing write access to /tmp.
class FileLock:
   def __enter__(self):
      self._lock = threading.Lock()
      self._lock.acquire()
      self._fd = open('/tmp/lockfile.LOCK', 'w+')
      fcntl.lockf(self._fd, fcntl.LOCK_EX)

   def __exit__(self, type, value, traceback):
      self._fd.close()
      self._lock.release()

</xsl:if>

<xsl:for-each select="./Info/Python/Depends[@SQL='Snowflake']/Imports[count(@ExtractedTo)>0]">

# Get the path to the ZIP file and set the location to extract to.
zip_file_path = import_dir + "/<xsl:value-of select="."/>"
extracted = '<xsl:value-of select="./@ExtractedTo"/>'

# Extract the contents of the ZIP. This is done under the file lock
# to ensure that only one worker process unzips the contents.
with FileLock():
   if not os.path.isdir(extracted):
      with zipfile.ZipFile(zip_file_path, 'r') as myzip:
         myzip.extractall(extracted)

</xsl:for-each>



class <xsl:value-of select="$ProjectName"/>(object):

    def __init__(self):
        self.local_parameters = nmspace(<xsl:if test="count(./Parameters/Column)>0"><xsl:for-each select="./Parameters/Column"><xsl:text>
            </xsl:text><xsl:choose>
            <xsl:when test="@DTyp='Int' or @DTyp='Lng'"><xsl:value-of select="@Name"/> = <xsl:value-of select="@Default"/>,</xsl:when>
            <xsl:when test="@DTyp='Dte' or @DTyp='Dte'"><xsl:value-of select="@Name"/> = _isoparser('<xsl:value-of select="@Default"/>'),</xsl:when>
            <xsl:when test="@DTyp='Dbl'"><xsl:value-of select="@Name"/> = <xsl:value-of select="@Default"/>,</xsl:when>
            <xsl:when test="@DTyp='Bln'"><xsl:value-of select="@Name"/> = <xsl:value-of select="@Default"/>,</xsl:when>
            <xsl:when test="@DTyp='Str' or @DTyp='VLS'"><xsl:value-of select="@Name"/> = '<xsl:value-of select="@Default"/>',</xsl:when></xsl:choose>
</xsl:for-each></xsl:if>)

        global _WORKER_ORCHESTRATORS
        self.__WORKER_ORCHESTRATORS = _WORKER_ORCHESTRATORS

        <xsl:value-of select="./Info/Python/Depends[@SQL='Snowflake']/class__init__"/>


    @vectorized(input=pd.DataFrame)
    def end_partition(self, df):
        return self.processPartition(df)


    def processPartition(self, df):

        try:# {

            nrows = df.shape[0]

            row=0
            rowM1=-1
            first_row=0
            last_row=-1

            row_to_output=[]
            row_index_last=[]
            row_index_next=[]

            <xsl:if test="count(./Parameters/Column)>0"><xsl:for-each select="./Parameters/Column"><xsl:text>
            </xsl:text>self.local_parameters.<xsl:value-of select="@Name"/> = df['<xsl:value-of 
                select="translate(@Name,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"
                />'][0]</xsl:for-each></xsl:if>

            <xsl:if test="count(./Parameters/Column[@Name='InputBlockMaxSize'])>0">
            if ((self.local_parameters.InputBlockMaxSize is not None) and 
                (self.local_parameters.InputBlockMaxSize > 0) and
                (nrows > self.local_parameters.InputBlockMaxSize) ):
                raise Exception(f'Partition by blocks are limited to {self.local_parameters.InputBlockMaxSize} rows')
            </xsl:if>


            self.row_tracing = nmspace(first_row=0
                          , last_row=nrows
                          , row_to_output=row_to_output
                          , row_index_last=row_index_last
                          , row_index_next=row_index_next
                          )

            local_asset = nmspace( _local_parameters = self.local_parameters
                                  , _row_tracing = self.row_tracing
                                  , _self = self
                                  )
            
                
            <xsl:for-each select="./Columns/Column[@Use='IO' or @Use='I' or @Use='O' or @Use='T']"><xsl:text>
            </xsl:text>#Use=<xsl:value-of select="@Use"/> Static=<xsl:value-of select="@Static"/> BlockID=<xsl:value-of select="@BlockID"/> DTyp=<xsl:value-of select="@DTyp"/> Default=<xsl:value-of select="@Default"/>

            #local_asset.<xsl:value-of select="@Name"/> = <xsl:choose>
                <xsl:when test="@Use='IO' or @Use='I'">df['<xsl:value-of 
                select="translate(@Name,'abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ')"
                />']<xsl:if 
                test="not (count(@Static)=0 and count(@BlockID)=0) and (translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')">[0]</xsl:if></xsl:when>
                <xsl:when test="@Use='O' or @Use='T'"><xsl:if
                test="(count(@Static)=0 and count(@BlockID)=0) or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')">pd.Series([</xsl:if><xsl:choose>
                        <xsl:when test="count(@Default)=0">None</xsl:when>
                        <xsl:when test="@DTyp='Int' or @DTyp='Lng' or @DTyp='Dbl' or @DTyp='Bln'"><xsl:value-of select="@Default"/></xsl:when>
                        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">'<xsl:value-of select="@Default"/>'</xsl:when>
                        <xsl:when test="@DTyp='Dte' or @DTyp='DTm'">_isoparser('<xsl:value-of select="@Default"/>')</xsl:when>
                </xsl:choose><xsl:if
                test="(count(@Static)=0 and count(@BlockID)=0) or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')">]*nrows<xsl:choose>
                <xsl:when test="@DTyp='Int' or @DTyp='Lng'">,dtype=np.int64</xsl:when>
                <xsl:when test="@DTyp='Dbl'">,dtype=np.float64</xsl:when>
                <xsl:when test="@DTyp='Bln'">,dtype=bool</xsl:when>
                <xsl:when test="@DTyp='Str' or @DTyp='VLS'">,dtype=str</xsl:when>
                </xsl:choose>)</xsl:if></xsl:when></xsl:choose>

            local_asset.<xsl:value-of select="@Name"/> = <xsl:choose>
                <xsl:when test="@Use='IO' or @Use='I'">df['<xsl:value-of 
                select="@Name"
                />']<xsl:if 
                test="not (count(@Static)=0 and count(@BlockID)=0) and (translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')">[0]</xsl:if></xsl:when>
                <xsl:when test="@Use='O' or @Use='T'"><xsl:if
                test="(count(@Static)=0 and count(@BlockID)=0) or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')">pd.Series([</xsl:if><xsl:choose>
                        <xsl:when test="count(@Default)=0">None</xsl:when>
                        <xsl:when test="@DTyp='Int' or @DTyp='Lng' or @DTyp='Dbl' or @DTyp='Bln'"><xsl:value-of select="@Default"/></xsl:when>
                        <xsl:when test="@DTyp='Str' or @DTyp='VLS'">'<xsl:value-of select="@Default"/>'</xsl:when>
                        <xsl:when test="@DTyp='Dte' or @DTyp='DTm'">_isoparser('<xsl:value-of select="@Default"/>')</xsl:when>
                </xsl:choose><xsl:if
                test="(count(@Static)=0 and count(@BlockID)=0) or not(translate(substring(@Static,1,1),'YySsTt','111111')='1' or translate(substring(@BlockID,1,1),'YySsTt','111111')='1')">]*nrows<xsl:choose>
                <xsl:when test="@DTyp='Int' or @DTyp='Lng'">,dtype=np.int64</xsl:when>
                <xsl:when test="@DTyp='Dbl'">,dtype=np.float64</xsl:when>
                <xsl:when test="@DTyp='Bln'">,dtype=bool</xsl:when>
                <xsl:when test="@DTyp='Str' or @DTyp='VLS'">,dtype=str</xsl:when>
                </xsl:choose>)</xsl:if></xsl:when></xsl:choose></xsl:for-each>

            guts.<xsl:value-of select="$ProjectName"/>_guts(local_asset)

            #//////// in other XSLT UDTFs, the row_to_output, _next, and _prior are 
            #//////// followed to reorder output rows, this needs to be implemented for Snowflake/Python 
            #//////// when needed

            #vectorized snowflake return of just output variables in the order of the output schema
            #this follows the Vertica UDTF getReturnType
            #for snowflake/vectorized/pandas, as long as there is one series, all statics fill 
            #a column automatically

            return pd.DataFrame({<xsl:for-each select="./Columns/Column[@Use='IO' or @Use='O']">
                        '<xsl:value-of select="@Name"/>"':local_asset.<xsl:value-of select="@Name"/>,</xsl:for-each>
                    })

        except Exception as e:
            raise Exception('Exception in <xsl:value-of select="$ProjectName"/>, '+str(e)+', '+traceback.format_exc())

        #////// general wrapping up
        #} 


</xsl:if>

    </xsl:template>

    <xsl:template match="/">
        <xsl:for-each select="/UDxs/UDTF">
            <xsl:call-template name="UDTF_Python"/>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>


