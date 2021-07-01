#!/usr/bin/env python3

import os,sys
import pudb
import argparse
import traceback

import time
import os.path as osp
import glob
import fnmatch
import re
import string
from enum import Enum
import datetime

from WDS.Util.MonthID import *


def CheckFile(d,f, lastrow=1):
    rv=0
    fid=open(osp.join(d,f),'r')
    csv_fid=csv.reader(fid)
    for i,row in enumerate(csv_fid):
        print(i,row)
        if i==0:
            if row[0].lower().startswith("inv"):
                rv=1
            elif row[0].lower() in ("loan", "loan number", "loan #"):
                rv=2
            elif row[0].lower().startswith("loans extended"):
                rv=3
        if i==1:
            if row[0].lower() in ('loan number'):
                rv=2
            elif row[0].lower().startswith('investor') and ("Loan Number" in row):
                rv=2
            if (rv>0) and row[0].lower() in ("no","no."):
                if lastrow==1:
                    fid.close()
                    return rv+10
            if (rv>0):
                if lastrow==1:
                    fid.close()
                    return rv
        if i>=lastrow: break
    fid.close()
    return rv


class eDTyp(Enum):
    Unk = 0
    Dbl = 1
    Lng = 2
    Int = 3
    Dte = 4
    DTm = 5
    Str = 6
    VLS = 7
    Byt = 8
    Bln = 9

NbrCheckRE1=re.compile("[0-9.]+")
WrdCheckRE1=re.compile("[^\d\-.,\s]+")

#cleaners for DTypCheck
def CleanStr(slf,tv,v,isLengthDiscoverable,toReturn=False): 
    if tv is str:
        v=v.rstrip()
        if isLengthDiscoverable:
            if v!=slf.NULLStr:
                lv=len(v)
                if lv>slf.length: slf.length=lv
        return v
    elif tv is bytes:
        sv=v.decode()
        sv=sv.rstrip()
        if isLengthDiscoverable:
            if v!=slf.NULLStr:
                lv=len(sv)
                if lv>slf.length: slf.length=lv
        return sv
    else:
        sv=str(v)
        sv=sv.rstrip()
        if isLengthDiscoverable:
            if v!=slf.NULLStr:
                lv=len(sv)
                if lv>slf.length: slf.length=lv
        return sv

def CleanBln(slf,tv,v,toReturn=False):
    if tv is bool: return v
    #check other accepted boolean equivalents
    if v in (1,0): return (v==1)
    if tv is str:
        lv=tv.lower() in ("t","true","on","1","yes","y")
        if lv: return True
        lv=tv.lower() in ("f","false","off","0","no","n")
        if lv: return False
    try:
        x=float(v)
        if float.is_integer(x) and (int(x) in (0,1)): return (int(x)==1)
        if (math.fabs(x)<1e-8) or (math.fabs(x-1.0)<1e-8): return (math.fabs(x-1.0)<1e-8)
    except:
        pass
    if toReturn:
        return False
    raise Exception('in mDTypCheck for Bln, could not convert '+str(v))

def CleanDbl(slf,tv,v,toReturn=False,isDateEpochExcel=False):
    if tv is float: return v
    if tv in (datetime.date, datetime.datetime):
        if isDateEpochExcel:
            lv=v-DateEpochExcel
        else:
            lv=v-DateEpoch
        lv=float(lv.tm_days)+float(lv.tm_hours)/24.0+float(lv.tm_min)/60.0+float(lv.tm_sec)/60.0
        return lv
    lv=None
    try:
        lv=float(v)
        if toReturn: return lv
        return
    except:
        if slf.isNULLable: 
            if toReturn: return None
    raise Exception('in mDTypCheck for Dbl, could not convert '+str(v))

def CleanInt(slf,tv,v,toReturn=False,isDateEpochExcel=False):
    if tv is int: return v
    if tv in (datetime.date, datetime.datetime):
        if isDateEpochExcel:
            lv=v-DateEpochExcel
        else:
            lv=v-DateEpoch
        lv=int(lv.tm_days)
        return lv
    lv=None
    try:
        lv=int(v)
        if toReturn: return lv
        return
    except:
        if slf.isNULLable:
            if toReturn: return None
    raise Exception('in mDTypCheck for Int/Lng, could not convert '+str(v))


def CleanDte(slf,tv,v,toReturn=False,isDateEpochExcel=False):
    #CleanDate is from the date utilities in MonthID.py
    if tv is datetime.date: return v
    if tv is datetime.datetime: return v.date()
    lv=None

    try:
        lv=CleanDate(v,tv=tv,isDateEpochExcel=isDateEpochExcel)
    except Exception as e:
        raise Exception('Error in CleanDte: '+e.args[0]+'\n'+e.__traceback__)
    
    if lv is None:
        if slf.isNULLable:
            return None
        else:
            raise Exception('in mDTypCheck for Dte, year is less than '+str(DateUsefulMin))
    if lv<DateUsefulMin:
        if slf.isNULLable:
            return None
        else:
            raise Exception('in mDTypCheck for Dte, year is less than '+str(DateUsefulMin))
    elif lv>DateUsefulMax:
        if slf.isNULLable:
            return None
        else:
            raise Exception('in mDTypCheck for Dte, year is greater than '+str(DateUsefulMax))
    else:
        return lv

def CleanDTm(slf,tv,v,toReturn=False,isDateEpochExcel=False):
    if tv is datetime.datetime: return v
    if tv is datetime.date: return datetime.datetime(v.year,v.month,v.day,0,0,0)
    lv=None
    try:
        if tv in (int,float):
            if isDateEpochExcel:
                if (tv is float) and (v.as_integer_ratio()[1]!=1):
                    f=v-int(v)
                    s=int(f*86400)
                else:
                    s=0
                lv=DateEpochExcel+datetime.timedelta(int(v),s,0)
                if lv.year>2040:
                    print('WARNING, in mDTypCheck, with isDateEpochExcel, converted int/float to a year>2040, might not be Excel Date')
            else:
                if (tv is float) and (v.as_integer_ratio()[1]!=1):
                    f=v-int(v)
                    s=int(f*86400)
                else:
                    s=0
                lv=DateEpoch+datetime.timedelta(int(v),s,0)
                if lv.year>2040:
                    print('WARNING, in mDTypCheck, with isDateEpochExcel=False, converted int/float to a year>2040, might be Excel Date')
        elif tv in (str,bytes):
            lv=v if tv is str else v.decode()
            prs=DateFormatRE3.findall(lv)
            if (len(prs)==1) and (len(prs[0])>=5) and (prs[0][1]==prs[0][3]) and (prs[0][7]==prs[0][9]): 
                try:
                    lv=datetime.datetime(int(prs[0][0]),int(prs[0][2]),int(prs[0][4]),int(prs[0][6]),int(prs[0][8]),inv(prs[0][10]))
                except:
                    lv=None
            else:
                found=False
                for f in (DateFormatRE1, DateFormatRE2):
                    prs=f.findall(lv)
                    if (len(prs)==1) and (len(prs[0])>=5) and (prs[0][1]==prs[0][3]): 
                        try:
                            lv=datetime.date(int(prs[0][0]),int(prs[0][2]),int(prs[0][4]))
                            found=True
                            break
                        except:
                            pass
                if not found:
                    lv=None
    except:
        if toReturn==False:
            raise Exception('in mDTypCheck for Dte, year is less than '+str(DateUsefulMin))
        lv=None
    if lv is None:
        if slf.isNULLable:
            return None
        else:
            raise Exception('in mDTypCheck for Dte, year is less than '+str(DateUsefulMin))
    if lv<DateUsefulMin:
        if slf.isNULLable:
            return None
        else:
            raise Exception('in mDTypCheck for Dte, year is less than '+str(DateUsefulMin))
    elif lv>DateUsefulMax:
        if slf.isNULLable:
            return None
        else:
            raise Exception('in mDTypCheck for Dte, year is greater than '+str(DateUsefulMax))
    else:
        return lv


class FieldMD(object):
    
    def __init__(self, 
                name="None", 
                aliases=[],
                DTyp=eDTyp.Int,
                isDTypDiscoverable=True,
                isDateEpochExcel=False,
                isLengthDiscoverable=True,
                length=0,
                isNULLable=True,
                NULLStr='NULL',
                toCastAtLoad=False,
                isPrimaryKey=False,
                isExcluded=False,
                default=None
                #, scan_details=False,
                ):
        self.name=name
        #self.refname=name # a reference name for checking if there are dups in a header row
        self.aliases=[]
        for a in aliases: 
            if (a!=name) and (self.aliases.count(a)==0): self.aliases.append(a)
        self.DTyp=DTyp
        self.isDTypDiscoverable=isDTypDiscoverable
        self.isLengthDiscoverable=isLengthDiscoverable
        self.length=length
        self.isDateEpochExcel=isDateEpochExcel
        self.isNULLable=isNULLable
        self.NULLStr=NULLStr
        self.toCastAtLoad=toCastAtLoad
        self.isPrimaryKey=isPrimaryKey
        self.isExcluded=isExcluded
        #self.scan_details=scan_details
        self.default=default

    def mPrint(self,indnt='    ',sindnt='    ',toPrintNameAsAlias=False):
        rv="FieldMD(name='%s'\n" % self.name
        if (len(self.aliases)==0) and (toPrintNameAsAlias==False):
            rv+=indnt + ",aliases=[]\n"
        else:
            rv+=indnt + ",aliases=["
            if toPrintNameAsAlias: rv+=("'%s'\n%s%s,'%s'" % (self.name,indnt,sindnt,self.name))
            for i,v in enumerate(self.aliases):
                if (i>0) or toPrintNameAsAlias: rv+='\n'+indnt+sindnt+","
                rv+=("'%s'" % v)
            rv+='\n'+indnt+sindnt+']\n'
        rv+=indnt + ",DTyp="+str(self.DTyp)+'\n'
        rv+=indnt + ",isDTypDiscoverable="+str(self.isDTypDiscoverable)+'\n'
        rv+=indnt + ",isLengthDiscoverable="+str(self.isLengthDiscoverable)+'\n'
        rv+=indnt + ",length="+str(self.length)+'\n'
        rv+=indnt + ",isNULLable="+str(self.isNULLable)+'\n'
        rv+=indnt + ",NULLStr='"+str(self.NULLStr)+"'"+'\n'
        rv+=indnt + ",toCastAtLoad="+str(self.toCastAtLoad)+'\n'
        rv+=indnt + ",isPrimaryKey="+str(self.isPrimaryKey)+'\n'
        rv+=indnt + ",isExcluded="+str(self.isExcluded)+'\n'
        #if self.DTyp in (eDTyp.Str,eDTyp.VLS):
            #rv+=indnt + (",default='%s'" % self.default)+'\n'
        #else:
        if self.default is None:
            rv+=indnt + ",default=None"+'\n'
        else:
            if self.DTyp is eDTyp.Str or self.DTyp is eDTyp.VLS:
                rv+=indnt + ",default='"+str(self.default)+"'"+'\n'
            else:
                rv+=indnt + ",default="+str(self.default)+'\n'
        rv+=indnt + ")\n"
        return rv


    def mDTypCheck(self,v
            ,isReturnRequested=False
            ,isDTypDiscoverable=None
            ,isLengthDiscoverable=None
            ,isDateEpochExcel=False
            ):
        '''mDTypCheck takes a value for the field and checks it against
            the simplified data table (DTyp).  
            If isReturnRequested, then a possible cleaned value is returned.
            If the FieldMD is discoverable, the FieldMD DTyp is updated
            with the type observed.
                Notes:
                    - everything starts out assumed to be Int
                    - any value (even if it has a different representation,
                      such as a string) does not change the DTyp as long
                      as it can be cast to that type
                    - the "order" is as follows:
                        - Once determined or set to be a Str, VLS, or Byt,
                          the type never changes. However, the maximum 
                          length is tracked for generating SQL table schemas.
                        - For Bln, any usual value does not change the type,
                          such as values with 0,1,T,F,Yes,No,On,Off, etc.
                        - Once a non-integer Dbl is observed, it is never
                          automatically changed back to Int/Lng.
                        - Once a Dte or DTm is observed, it is never 
                          automatically changed back to Int/Lng/Dbl, and
                          it makes inferences based on POSIX epocs by default
                          (but can be changed to Excel or other).
                        - Any datetime.datetime types with 00:00:00[.000]
                          do not change a Dte to DTm, but once a non-date
                          DTm is observed, the type is never automatically 
                          changed back to Dte.
                    - datetime objects are handled as the R rhdf5 library
                      would write a date or chron value to an HDF5 compound
                      dataset.  The time portion is also as Excel might handle.
                      Dates are the number of days since 1970-01-01 and a 
                      fractional part is the time as a fraction of day.
                      Excel dates are offset by 25568. Since this is about 
                      70 years, numeric values to be dates are taken to be
                      Excel dates if they would otherwise show up as 
                      past 2040.
        '''
        if self.DTyp is eDTyp.Byt: raise Exception('mDTypCheck for Byt TODO')
        if isDTypDiscoverable is None: isDTypDiscoverable=self.isDTypDiscoverable
        if isLengthDiscoverable is None: isLengthDiscoverable=self.isLengthDiscoverable
        if (not isReturnRequested) and (not isDTypDiscoverable): return
        tv=type(v)
        if isReturnRequested and not isDTypDiscoverable:
            if (v is None) and (not self.isNULLable):
                raise Exception('in mDTypCheck, could not convert a None for a FieldMD with not isNULLable')
            if self.DTyp in (eDTyp.Str, eDTyp.VLS): 
                return CleanStr(self,tv,v,isLengthDiscoverable,toReturn=True)
            elif self.DTyp is eDTyp.Bln:
                return CleanBln(self,tv,v,toReturn=True)
            elif self.DTyp is eDTyp.Dbl:
                return CleanDbl(self,tv,v,toReturn=True,isDateEpochExcel=isDateEpochExcel)
            elif self.DTyp in (eDTyp.Int, eDTyp.Lng):
                return CleanInt(self,tv,v,toReturn=True,isDateEpochExcel=isDateEpochExcel)
            elif self.DTyp is eDTyp.Dte:
                return CleanDte(self,tv,v,toReturn=True,isDateEpochExcel=isDateEpochExcel)
            elif self.DTyp is eDTyp.DTm:
                return CleanDTm(self,tv,v,toReturn=True,isDateEpochExcel=isDateEpochExcel)
            else:
                raise Exception('in mDTypCheck, uncaught case for '+str(self.DTyp)+' for v='+str(v))

        if (not isDTypDiscoverable) and isLengthDiscoverable and (self.DTyp in (eDTyp.Str, eDTyp.VLS)): 
            try:
                lv=CleanStr(self,tv,v,isLengthDiscoverable,toReturn=False)
            except:
                pass
            return

        #nothing gets changed if empty or Byt
        if (v is None) or (self.DTyp is eDTyp.Byt): return v
        #nothing gets changed if an empty string, equivalent to None
        if (tv in (str, bytes)) and len(v)==0: 
            if self.isNULLable:
                return None
            else:
                raise Exception('in mDTypCheck, cannot convert return empty string or None for not isNULLable')
        #DTyp does not get changed for strings, only max length can change
        if self.DTyp in (eDTyp.Str, eDTyp.VLS):
            try:
                lv=CleanStr(self,tv,v,isLengthDiscoverable,toReturn=False)
                if isReturnRequested: return lv.rstrip()
                return
            except:
                pass
        #if type matches DTyp nothing changes for Int/Lng, Dbl, Bln, Dte, DTm
        if (tv is int) and (self.DTyp in (eDTyp.Int, eDTyp.Long)): return v
        if (tv is float) and (self.DTyp is eDTyp.Dbl): return v
        if (tv is datetime.datetime) and (self.DTyp is eDTyp.DTm): return v
        if (tv is datetime.date) and (self.DTyp is eDTyp.Dte): return v
        if (tv is bool) and (self.DTyp is eDTyp.Bln): return v

        #short circuit the string types if there are obvious characters
        if tv is str:
            if WrdCheckRE1.findall(v):
                self.DTyp=eDTyp.Str
                if isReturnRequested: return v.rstrip()
                return
        if tv is bytes:
            lv=v.decode()
            if WrdCheckRE1.findall(lv):
                self.DTyp=eDTyp.Str
                if isReturnRequested: return lv.rstrip()
                return


        if self.DTyp in (eDTyp.Int,eDTyp.Lng):
            try:
                lv=CleanInt(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                if isReturnRequested: return lv
                return
            except:
                try:
                    lv=CleanBln(self,tv,v,toReturn=False)
                    self.DTyp=eDTyp.Bln
                    if isReturnRequested: return lv
                    return
                except:
                    try:
                        lv=CleanDbl(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                        self.DTyp=eDTyp.Dbl
                        if isReturnRequested: return lv
                        return
                    except:
                        try:
                            lv=CleanDTm(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                            self.DTyp=eDTyp.DTm
                            if isReturnRequested: return lv
                            return
                        except:
                            try:
                                lv=CleanDte(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                                self.DTyp=eDTyp.Dte
                                if isReturnRequested: return lv
                                return
                            except:
                                if tv is bytes:
                                    lv=v.decode()
                                else:
                                    lv=str(v)
                                self.DTyp=Str
                                if isReturnRequested: return lv.rstrip()
                                return
        elif self.DTyp is eDTyp.Dbl:
                    try:
                        lv=CleanDbl(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                        if isReturnRequested: return lv
                        return
                    except:
                        try:
                            lv=CleanDTm(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                            self.DTyp=eDTyp.DTm
                            if isReturnRequested: return lv
                            return
                        except:
                            try:
                                lv=CleanDte(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                                self.DTyp=eDTyp.Dte
                                if isReturnRequested: return lv
                                return
                            except:
                                if tv is bytes:
                                    lv=v.decode()
                                else:
                                    lv=str(v)
                                self.DTyp=Str
                                if isReturnRequested: return lv.rstrip()
                                return
        elif self.DTyp is eDTyp.Dte:
                        try:
                            lv=CleanDTm(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                            self.DTyp=eDTyp.DTm
                            if isReturnRequested: return lv
                            return
                        except:
                            try:
                                lv=CleanDte(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                                self.DTyp=eDTyp.Dte
                                if isReturnRequested: return lv
                                return
                            except:
                                if tv is bytes:
                                    lv=v.decode()
                                else:
                                    lv=str(v)
                                self.DTyp=Str
                                if isReturnRequested: return lv.rstrip()
                                return
        elif self.DTyp is eDTyp.DTm:
                        try:
                            lv=CleanDTm(self,tv,v,toReturn=False,isDateEpochExcel=isDateEpochExcel)
                            if isReturnRequested: return lv
                            return
                        except:
                                if tv is bytes:
                                    lv=v.decode()
                                else:
                                    lv=str(v)
                                self.DTyp=Str
                                if isReturnRequested: return lv.rstrip()
                                return
        else:
            self.DTyp=eDTyp.Str
            if tv is bytes:
                lv=v.decode()
            else:
                lv=str(v)
            lv=lv.rstrip()
            if lv!=self.NULLStr:
                self.length=max(self.length,len(lv))
            if isReturnRequested: return lv
            return

        raise Exception("in mDTypCheck, check for implementation for "+str(v)+" self.DTyp="+str(self.DTyp))


    def isAlias(self, name):
        lname=name.lower().strip()
        if lname==self.name.lower():
            return True
        for a in self.aliases:
            if lname==a.lower():
                return True
        return False

### end of class def


class FieldMDs(dict):
    def __init__(self,
                name="None"
                ):
        dict.__init__(self)
        self.name=name
    def __setitem__(self,key,value):
        if type(value) is not FieldMD:
            raise Exception("Only FieldMD objects can be inserted into FieldMDs collection")
        fld=None
        if key in self:
            fld=self[key]
        else:
            lv=value.name.lower()
            found=False
            for fldname in self:
                fld=self[fldname]
                for a in fld.aliases:
                    if lv==a.lower():
                        found=True
                        break
                if found: break
            if not found:
                fld=None
        if fld:
            for a in value.aliases: 
                if (a!=fld.name) and (fld.aliases.count(a)==0): fld.aliases.append(a)
            if value.DTyp!=fld.DTyp:
                if ( (value.DTyp in (eDTyp.Byt,eDTyp.VLS,eDTyp.Str,eDTyp.Bln))
                    or (fld.DTyp in (eDTyp.Byt,eDTyp.VLS,eDTyp.Str,eDTyp.Bln))):
                    fld.DTyp=max(value.DTyp,fld.DTyp)
                    fld.length=max(value.length,fld.length)
                elif ( (value.DTyp in (eDTyp.Dte,eDTyp.DTM))
                    or (fld.DTyp in (eDTyp.Dbl.Dte,eDTyp.DTM)) ):
                    fld.DTyp=max(value.DTyp,fld.DTyp)
                    fld.length=0
                elif ( (value.DTyp in (eDTyp.Dbl,eDTyp.Lng,eDTyp.Int))
                    or (fld.DTyp in (eDTyp.Dbl,eDTyp.Lng,eDTyp.Int)) ):
                    fld.DTyp=min(value.DTyp,fld.DTyp)
                    fld.length=0
                else:
                    fld.DTyp=value.DTyp
                    fld.length=value.length
            fld.isDTypDiscoverable= value.isDTypDiscoverable and fld.isDTypDiscoverable
            fld.isLengthDiscoverable= value.isLengthDiscoverable and fld.isLengthDiscoverable
            fld.isDateEpochExcel= value.isDateEpochExcel or fld.isDateEpochExcel
            fld.isNULLable=  value.isNULLable or fld.isNULLable
            fld.NULLStr=  value.NULLStr or fld.NULLStr
            fld.toCastAtLoad= value.toCastAtLoad or fld.toCastAtLoad
            fld.isPrimaryKey= value.isPrimaryKey
            fld.isExcluded= value.isExcluded or fld.isExcluded
            fld.default= value.default if value.default else fld.default
        else:
            dict.__setitem__(self,key,value)



    def mPrint(self,fid=sys.stdout,toPrintHeader=False,toPrintNameAsAlias=False,toHoldColNNames=False):
        lisWritingFile=False
        if type(fid) is str:
            lisWritingFile=True
            fid=open(fid,'w')
        if toPrintHeader:
            fid.write("from WDS.ModelSpec.FieldMD import *\n")
            fid.write("%s=FieldMDs(name='%s')\n" % (self.name,self.name))
        fldnames=self.keys()
        lfldnames=list(fldnames)
        lfldnames.sort()
        for fldname in lfldnames:
            hold=False
            if toHoldColNNames:
                if fldname.startswith('Col') and (len(fldname)>3):
                    hold= (not WrdCheckRE1.findall(fldname[3:]))
            if not hold:
                fld=self[fldname]
                fid.write("%s['%s']=" % (self.name, fld.name))
                fid.write(fld.mPrint(toPrintNameAsAlias=toPrintNameAsAlias))
        if lisWritingFile:
            fid.write("\n")
            fid.write("if __name__=='__main__':\n")
            fid.write("    print('args=',sys.argv)\n")
            fid.write("    fid=sys.stdout\n")
            fid.write("    if len(sys.argv)>1: fid=sys.argv[1]\n")
            fid.write("    BaseFieldMDs.mPrint(toPrintNameAsAlias=True\n")
            fid.write("            ,fid=fid\n")
            fid.write("            ,toPrintHeader=True\n")
            fid.write("            ,toHoldColNNames=True\n")
            fid.write("            )\n")
            fid.close()


    # the following function takes an array of FieldMD and constructs the SQL code for creating a table to read in a flat file
    def mCreateTable(self
            , header=[]
            , schema="test"
            , table="test"
            , fn=None
            , engine="Vertica"
            , toJustDrop=False
            ):
        lTable=table.replace("-","_")
        q="drop table if exists %s.%s cascade;\n" % ( schema, lTable ) 
        if toJustDrop: return q
        q+="create table if not exists %s.%s (\n" % ( schema, lTable )

        anyCasts=False
        ddlq=""
        castq=""

        header_seen={}
        for fi,fldname in enumerate(header):
            if fi > 0:
                ddlq+="\n, "
                castq+="\n, "
            lnm=""
            if fldname in header_seen:
                header_seen[fldname]+=1
                lnm="%s%d" % (fldname,header_seen[fldname])
            else:
                header_seen[fldname]=1
                lnm="%s" % fldname
            fld=self[fldname]
            ddlq+=lnm+' '
            if fld.toCastAtLoad:
                anyCasts=True
                castq+=lnm+'_FILLER FILLER varchar\n, '
                if fld.DTyp is eDTyp.Str or fld.DTyp is eDTyp.VLS:
                    castq+=lnm+' as NULLIF(RTRIM('+lnm+'_FILLER),'+"'"+fld.NULLStr+"') "
                elif fld.DTyp is eDTyp.Int or fld.DTyp is eDTyp.Lng:
                    castq+=lnm+' as CAST(NULLIF(LTRIM(RTRIM('+lnm+'_FILLER)),'+"'"+fld.NULLStr+"') AS DECIMAL(32,0))::INTEGER "
                else:
                    castq+=lnm+' as NULLIF(LTRIM(RTRIM('+lnm+'_FILLER)),'+"'"+fld.NULLStr+"') "
            else:
                castq+=lnm
            if fld.DTyp is eDTyp.Dbl:
                ddlq+="float "
            elif fld.DTyp is eDTyp.Int:
                ddlq+="int "
            elif fld.DTyp is eDTyp.Lng:
                ddlq+="bigint "
            elif fld.DTyp is eDTyp.Dte:
                ddlq+="date "
            elif fld.DTyp is eDTyp.DTm:
                ddlq+="datetime "
            elif fld.DTyp is eDTyp.Str:
                ddlq+="char(%d) " % max(1,fld.length)
            elif fld.DTyp is eDTyp.VLS:
                ddlq+="varchar(%d) " % max(1,fld.length)
            if (fld.default is None) or (fld.default in('NULL','None')):
                ddlq+=" default NULL"
            else:
                if type(fld.default) is str:
                    ddlq+=" default '%s' " % fld.default
                elif type(fld.default) is bytes:
                    ddlq+=" default '%s' " % fld.default.decode()
                elif type(fld.default) is datetime.date:
                    ddlq+=" default '%s' " % fld.default.isoformat()
                elif type(fld.default) is datetime.datetime:
                    ddlq+=" default '%s' " % fld.default.isoformat()
                else:
                    ddlq+=" default %s " % str(fld.default)
        q+=ddlq
        #q+="\n) engine=%s default charset=latin1; \n" % engine
        q+="\n); \n" 
        if fn:
            q+="\n\n" 
            q+="copy %s.%s" % ( schema, lTable )
            if anyCasts:
                q+='(\n'
                q+=castq
                q+='\n) '
            else:
                q+=' '
            q+="from '%s' \n" % ( fn )
            q+="   parser fcsvparser(header=true) "
            q+="   delimiter ',' enclosed by '"+'"'+"' abort on error record terminator '\\r\\n' "
            q+="   rejected data '%s.rejected' " % fn
            q+="   exceptions '%s.exceptions' " % fn
            q+="   ;\n\n"
        return q



# the following function takes a flat file and cleans the data for loading into MySQL and returns the query for loading


def clean_flatfile(
        filename="",
        FieldMD=[],
        dlm=",",
        schema="test",
        table="test",
        path=None
        ):


    if path is None:
        path=os.getcwd()

    fd=open(filename,'rU')
    fdo=open(filename+'.clean','w')

    #c=csv.reader(fd,delimiter=dlm,quoting=csv.QUOTE_MINIMAL)
    c=csv.reader(fd,dialect=csv.excel)
    #w=csv.writer(fdo,delimiter=dlm,quoting=csv.QUOTE_MINIMAL)
    w=csv.writer(fdo,dialect=csv.excel)

    #throw away first row of reader
    c.next()


    fldnms=[]
    for f in FieldMD:
        fldnms.append(f.name)
    w.writerow(fldnms)


    nflds=len(FieldMD)
    
    #for row in c:
    #row=c.next()
    for row in c:
        fldi=-1
        clean_row=[]
        for fld in row:
            fldi+=1
            if FieldMD[fldi].type in('int','float','double'):
                fld=fld.replace('$','').replace(',','')
                if len(fld)==0:
                    fld=FieldMD[fldi].default
            elif FieldMD[fldi].type in('date'):
                if len(fld)==0:
                    fld=FieldMD[fldi].default
                else:
                    try:
                        #print fld
                        #fld=parse_date(fld)
                        fldsplit=fld.strip().split(' ')
                        fldsplit=fldsplit[0]
                        fldsplit=fldsplit.split('/')                        
                        fld=datetime.date(int(fldsplit[2]),int(fldsplit[0]),int(fldsplit[1]))
                        fld=fld.isoformat()
                    except Exception as e:
                        fld=FieldMD[fldi].default
            else:
                if len(fld)>FieldMD[fldi].length:
                    fld=fld[0:FieldMD[fldi].length]
            clean_row.append(fld)
        if fldi<nflds-1:
            for fld in FieldMD[fldi+1:]:
                clean_row.append(fld.default)
        #print clean_row
        w.writerow(clean_row)


    fd.close()
    fdo.close()

    q="load data local infile '%s/%s' replace into table %s.%s \n" % (path,filename+'.clean',schema,table)
    if dlm=='\t':
        q+="fields terminated by '\\t' \n"
    else:
        q+="fields terminated by '%s' \n" % dlm
    q+="optionally enclosed by '\"'  lines terminated by '\\n' \n"
    q+="ignore 1 lines ; \n"

    return q




if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        _parser.add_argument("-p", "--path_of_target_directory"
                , help="first argument, path of target directory"
                , default=lProject.lDataExtracted
                )
        _parser.add_argument("--glob", "--glob-pattern"
                            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
                            , default='*.csv'
                            )
        _parser.add_argument("--nrows" 
                            , help="maximum number of rows to process"
                            , default=None
                            )
        _parser.add_argument("--ncols" 
                            , help="maximum number of columns to process"
                            , default=None
                            )
        _parser.add_argument("--BaseFieldMDs-file" 
                            , help="an alternative filename to gtmp/lBaseFieldMDs.py for new runs"
                            , default="gtmp/lBaseFieldMDs.py"
                            )
        _parser.add_argument("--new-BaseFieldMDs-file" 
                            , help="an alternative filename to gtmp/lBaseFieldMDs.py for new runs"
                            , default="gtmp/lBaseFieldMDs.py"
                            )
        _parser.add_argument("-l", "--list", "--dry-run", "--list-only"
                            , help="only display file names, do not process"
                            , dest="isListOnly"
                            , action='store_true'
                            , default=False )
        _parser.add_argument("-i", "--CaseInsensitive", "--case-insensitive"
                            , help="optional argument, for case insensitive"
                            , dest="CaseInsensitive"
                            , action='store_true'
                            , default=True )
        _parser.add_argument("-I", "--CaseSensitive", "--case-sensitive"
                            , help="optional argument, for case sensitive"
                            , action='store_false'
                            , dest='CaseInsensitive'
                            , default=None )
        _parser.add_argument("--files-only"
                            , help="only return file names (not directoy only names)"
                            , action='store_true'
                            , dest='isFilesOnly'
                            , default=True )
        _parser.add_argument("--no-files-only"
                            , help="return all file and directory names as separate items"
                            , action='store_false'
                            , dest='isFilesOnly'
                            , default=True )
        _parser.add_argument("-r", "--recursive"
                            , help="optional argument, for recursive flag for glob"
                            , action='store_true'
                            #, dest='recursive_flag'
                            , default=True )
        _parser.add_argument("--recap"
                            , help="recap arguments"
                            , action="store_true"
                            )
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser

    def main(args=None):
        if not args:
            raise('nothing passed into main')

        if args.recap:
            print("argument recap:")
            print("    path_of_target_directory: ", args.path_of_target_directory)
            print("    --glob: ", args.glob)
            print("    --nrows: ", args.nrows)
            print("    --ncols: ", args.ncols)
            print("    --CaseInsensitive: ", args.CaseInsensitive)
            print("    --recursive: ", args.recursive)
            print("    --isListOnly: ", args.isListOnly)
            print("    --recap: ", args.recap)
            print("    --pudb: ", args.pudb)
            sys.exit()

        path_of_target_directory=args.path_of_target_directory
        dd=LocalDirectory(path_of_target_directory)

        BaseFieldMDs=None
        if osp.exists(args.BaseFieldMDs_file):
            tmpstr=args.BaseFieldMDs_file.replace(".py","").replace("/",".")
            print(tmpstr)
            gtmp_BaseFieldMDs=__import__(tmpstr)
            print(dir(gtmp_BaseFieldMDs))
            BaseFieldMDs=gtmp_BaseFieldMDs.lBaseFieldMDs.BaseFieldMDs
        else:
            BaseFieldMDs=FieldMDs(name="BaseFieldMDs")

        if True: 
            list0=[]
            list1=[]
            list2=[]
            list3=[]
            list11=[]
            list12=[]
            for d,f in dd.walk(globpattern=args.glob,isRecursive=args.recursive,isFilesOnly=args.isFilesOnly): #,ignore=["gExtracted"]):
                print("d=",d,"f=",f)
                c=CheckFile(d,f)
                if c==0: list0.append((d,f))
                elif c==1: list1.append((d,f))
                elif c==2: list2.append((d,f))
                elif c==3: list3.append((d,f))
                elif c==11: list11.append((d,f))
                elif c==12: list12.append((d,f))

            print("list0=", list0)
            print("list1=", list1)
            print("list2=", list2)
            print("list11=", list11)
            print("list12=", list12)

            if False:
                print("list0==========================")
                for d,f in list0:
                    print("d=",d,"f=",f)
                    CheckFile(d,f,lastrow=20)

            if False:
                print("list1==========================")
                for d,f in list1:
                    print("d=",d,"f=",f)
                    CheckFile(d,f,lastrow=20)

            if False:
                print("list2==========================")
                for d,f in list2:
                    print("d=",d,"f=",f)
                    CheckFile(d,f,lastrow=20)

            if True:
                print("list11==========================")
                for d,f in list11:
                    print("d=",d,"f=",f)
                    CheckFile(d,f,lastrow=20)
                    ProcessSet11(d,f,lProject.lDataExtractedLoadScripts,lastrow=20,BaseFieldMDs=BaseFieldMDs)
                    BaseFieldMDs.mPrint(toPrintNameAsAlias=True
                            ,toPrintHeader=True
                            ,fid=args.new_BaseFieldMDs_file
                            )
                    break

            if False:
                print("list12==========================")
                for d,f in list12:
                    print("d=",d,"f=",f)
                    CheckFile(d,f,lastrow=20)







    l_argparser = main_argparser()
    try:
        args=l_argparser.parse_args()
        if args.pudb:
            pudb.set_trace()
        main(args=args)
    except Exception as e:
        print("Hey")
        print('-'*60)
        traceback.print_exc(file=sys.stdout)
        print('-'*60)
        print(traceback.format_tb(e.__traceback__))



