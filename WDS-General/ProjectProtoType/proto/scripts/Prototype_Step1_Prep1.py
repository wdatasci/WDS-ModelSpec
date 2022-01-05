#!/usr/bin/env python3

import os,sys
import os.path as osp

import gtmp.lProject_config as lProject

from WDS.Wranglers.dir_walk import *
from WDS.Wranglers.Excel import *
import WDS.ModelSpec.FieldMD as mFieldMD
from WDS.ModelSpec.FieldMD import *

import re


def lFileNameCleaner(s):
    if s.endswith(".csv"):
        lv=s.replace(".Prep1.csv","")
        lv=s.replace(".csv","")
    lv=lv.replace("_xlsm_","_")
    lv=lv.replace("_xlsb_","_")
    lv=lv.replace("_xlsx_","_")
    lv=lv.replace("_xls_","_")
    return lv



# Temporary processing can also classify the sets of files that were
# previously extracted.  Not all have to be loaded.

def ProcessSet11(d, f, dold, dnew, setn=11, lastrow=1000000, BaseFieldMDs=None):
    fp=osp.join(d,f)
    fid=open(fp,'r')
    csv_fid=csv.reader(fid)
    newrowlist=[]
    newheadernames=[]
    newheader=[]
    columnemptyind=[]
    lastrow=None
    ncols=0
    ii=-1
    for i,row in enumerate(csv_fid):
        if (ii>0) or (row.count('')!=len(row)): ii+=1
        if (ii==0) and (setn>=10):
            lastrow=row
        elif ( (ii==0) and (setn in(1,2)) ) or ( (ii==1) and (setn in(11,12)) ):
            if setn in (1,2):
                for j,v in enumerate(row):
                    if len(v)>0:
                        columnemptyind.append(False)
                        newheadernames.append(v)
                    else:
                        columnemptyind.append(True)
                        newheadernames.append("Col"+str(j))
            else:
                for j,v in enumerate(row):
                    if len(lastrow[j])>0 or len(row[j])>0:
                        columnemptyind.append(False)
                        newheadernames.append(lastrow[j]+" "+v)
                    else:
                        columnemptyind.append(True)
                        newheadernames.append("Col"+str(j))
            ncols=len(newheadernames)
        elif ii>0:
            if row.count('')!=ncols:
                newrowlist.append(row)
                for j,v in enumerate(row):
                    if columnemptyind[j] and (len(v)>0):
                        columnemptyind[j]=False
        #end if
    #next i
    fid.close()
    csv_fid=None
    ncols=len(newheadernames)
    columnindex=list(range(ncols))
    columnindexback=list(range(ncols))

    isColumnSubset=False
    if True in columnemptyind:
        isColumnSubset=True
        k=-1
        for j,v in enumerate(newheadernames):
            if not columnemptyind[j]:
                k+=1
                columnindex[k]=j
                columnindexback[j]=k
                newheader.append(v)
        final_ncols=k
    else:
        newheader=newheadernames
        final_ncols=ncols

    if BaseFieldMDs is not None:
        for j,v in enumerate(newheader):
            lv=v.strip()
            if v!=lv: 
                newheader[j]=lv
                v=lv
            found=v in BaseFieldMDs
            if not found:
                for fldname in BaseFieldMDs:
                    found=BaseFieldMDs[fldname].isAlias(v)
                    if found:
                        newheader[j]=fldname
                        break
            if not found:
                if mFieldMD.WrdCheckRE1.findall(v):
                    newname=mFieldMD.CleanName(v)
                    newheader[j]=newname
                    BaseFieldMDs[newname]=mFieldMD.FieldMD(name=newname,aliases=[v],sources=[fp])
                else:
                    newheader[j]="Col"+str(j)
                    BaseFieldMDs[newheader[j]]=mFieldMD.FieldMD(name=CleanName(newheader[j]))

        #print(BaseFieldMDs)
        for row in newrowlist:
            for jj in range(final_ncols):
                j=columnindex[jj]
                try:
                    fld=BaseFieldMDs[newheader[jj]]
                    fld.mDTypCheck(row[j]
                        ,isReturnRequested=False
                        #,isDTypDiscoverable=True   #commented out to allow lBaseFieldMDs to drive
                        ,isLengthDiscoverable=True
                        )
                except Exception as e:
                    print('>'*20,'<'*20)
                    print("d/f=",osp.join(d,f))
                    print("jj=",jj,"j=",j)
                    print("columnindex=",columnindex)
                    #print("newrowlist=",newrowlist)
                    print("final_ncols=",final_ncols)
                    print("newheader=",newheader)
                    #print("row=",row)
                    print("len(row)=",len(row))
                    print(d,f,dnew)
                    traceback.print_exc(file=sys.stdout)
                    print('>'*20,'<'*20)
                    print(traceback.format_tb(e.__traceback__))
                    print(newheader)
                    print(j,jj)
                    sys.exit()

    print(newheader)
    fn=lFileNameCleaner(f)
    fid=open(osp.join(dnew,fn+".Prep1.csv"),'w')
    toAppendFileDate=True
    if toAppendFileDate:
        try:
            filedate=CleanDate(fn)
            fileMonthID=MonthID(filedate)
            fileLastBusDay=MonthID2LastBusinessDayInMonth(fileMonthID)
            newheader.append("FileDate")
            newheader.append("FileMonthID")
            newheader.append("FileLastBusDay")
            if 'FileDate' not in BaseFieldMDs: BaseFieldMDs['FileDate']=mFieldMD.FieldMD(name='FileDate',DTyp=eDTyp.Dte)
            if 'FileMonthID' not in BaseFieldMDs: BaseFieldMDs['FileMonthID']=mFieldMD.FieldMD(name='FileMonthID',DTyp=eDTyp.Int)
            if 'FileLastBusDay' not in BaseFieldMDs: BaseFieldMDs['FileLastBusDay']=mFieldMD.FieldMD(name='FileLastBusDay',DTyp=eDTyp.Dte)
        except:
            toAppendFileDate=False




    csv_fid=csv.DictWriter(fid, dialect=csv.excel, fieldnames=newheader)
    csv_fid.writeheader()
    for row in newrowlist:
        if (row.count('')<ncols):
            if isColumnSubset:
                newrow=collections.OrderedDict(map(lambda i:(newheader[columnindexback[i]],row[i]),filter(lambda i:not columnemptyind[i],range(ncols))))
            else:
                newrow=collections.OrderedDict(map(lambda i:(newheader[columnindexback[i]],row[i]),range(ncols)))
            if toAppendFileDate:
                newrow["FileDate"]=filedate
                newrow["FileMonthID"]=fileMonthID
                newrow["FileLastBusDay"]=fileLastBusDay
            if ('AccountNumber' in newrow) and (newrow['AccountNumber'] in (None, '')): continue
            csv_fid.writerow(newrow)
    fid.close()

    fnsql=fn+".Prep1.Load.sql"
    fid=open(osp.join(dnew,fnsql),'w')
    print("header=",newheader)
    print("schema=",lProject.lSchema)
    print("table=",f.replace(".csv",""))
    #pudb.set_trace()
    fid.write(BaseFieldMDs.mCreateTable(header=newheader
            , schema=lProject.lSchema
            , table=fn
            , fn=osp.join(osp.abspath(dnew).replace("/mnt/c/","/").replace("/mnt/d/","/"),f.replace(".csv",".Prep1.csv"))
            #, toJustDrop=True
            ) )
    fid.close()
    os.system(lProject.VSQL+' -f '+osp.join(osp.abspath(dnew).replace("/mnt/c/","/").replace("/mnt/d/","/"),fnsql))





#end function



if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        _parser.add_argument("-s", "--path_of_source_directory"
                , help="first argument, path of source directory"
                , default=lProject.lDataExtracted
                )
        _parser.add_argument("-p", "--path_of_target_directory"
                , help="second argument, path of target directory"
                , default=lProject.lDataExtractedLoadScripts
                )
        _parser.add_argument("--glob", "--glob-pattern"
                            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
                            , default='*.csv'
                            )
        _parser.add_argument("--nrows" 
                            , help="maximum number of rows to process"
                            , default=10000000
                            , type=int
                            )
        _parser.add_argument("--ncols" 
                            , help="maximum number of columns to process"
                            , default=None
                            )
        _parser.add_argument("--BaseFieldMDs-file" 
                            , help="an alternative filename to gtmp/lBaseFieldMDs.py for new runs"
                            , default="gtmp/lBaseFieldMDs.py"
                            )
        _parser.add_argument("--BaseFieldMDs-base-class" 
                            , help="an alternative filename to gtmp/lBaseFieldMDs.py for new runs"
                            , default="lBaseFieldMDs"
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
        if not osp.isdir(path_of_target_directory):
            os.makedirs(path_of_target_directory,mode=777,exist_ok=True)
        path_of_source_directory=args.path_of_source_directory
        dd=LocalDirectory(path_of_source_directory)

        BaseFieldMDs=None
        if osp.exists(args.BaseFieldMDs_file):
            tmpstr=args.BaseFieldMDs_file.replace(".py","").replace("/",".")
            print(tmpstr)
            gtmp_BaseFieldMDs=__import__(tmpstr)
            print(dir(gtmp_BaseFieldMDs))
            print(args.BaseFieldMDs_base_class)
            BaseFieldMDs=getattr(gtmp_BaseFieldMDs,args.BaseFieldMDs_base_class).BaseFieldMDs
        else:
            BaseFieldMDs=FieldMDs(name="BaseFieldMDs")

        if True: 
            list0=[]
            list1=[]
            list2=[]
            list3=[]
            for d,f in dd.walk(globpattern=args.glob,isRecursive=args.recursive,isFilesOnly=args.isFilesOnly): #,ignore=["gExtracted"]):
                print("d=",d,"f=",f)
                c=1
                if c==0: list0.append((d,f))
                elif c==1: list1.append((d,f))
                elif c==2: list2.append((d,f))
                elif c==3: list3.append((d,f))

            print("list0=", list0)
            print("list1=", list1)
            print("list2=", list2)
            print("list3=", list2)

            if True:
                print("list1==========================")
                for d,f in list1:
                    print("d=",d,"f=",f)
                    #CheckFile(d,f,lastrow=20)
                    ProcessSet11(d,f,args.path_of_source_directory,args.path_of_target_directory,setn=1,lastrow=args.nrows,BaseFieldMDs=BaseFieldMDs)
                    BaseFieldMDs.mPrint(toPrintNameAsAlias=True
                            ,toPrintHeader=True
                            ,fid=args.new_BaseFieldMDs_file
                            ,toHoldColNNames=True
                            )


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



