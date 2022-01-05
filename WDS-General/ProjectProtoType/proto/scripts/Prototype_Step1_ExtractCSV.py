#!/usr/bin/env python3

import gtmp.lProject_config as lProject
import re
import string

from WDS.Wranglers.dir_walk import *
from WDS.Wranglers.Excel import *

lNameTransform_re1=re.compile("[^:A-Z_a-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD-.0-9\u00B7\u0300-\u036F\u203F-\u2040]+")
lNameTransform_re2=re.compile("[\s]+")
lNameTransform_re3=re.compile(".xlsx$")
lNameTransform_re4=re.compile("^_")
lNameTransform_re5=re.compile("_-")
lNameTransform_re6=re.compile("-_")
lNameTransform_re_end=re.compile("_csv")


def lBaseNameTransform(lName,lFullPath):
    rv=lNameTransform_re1.sub(" ",lName.strip())
    rv=lNameTransform_re2.sub(" ",rv)
    rv=lNameTransform_re2.sub("_",rv)
    rv=lNameTransform_re3.sub("",rv)
    rv=lNameTransform_re4.sub("",rv)
    rv=lNameTransform_re5.sub("-",rv)
    rv=lNameTransform_re6.sub("-",rv)
    return rv

def lNameTransform(lName,lFullPath):
    rv=lNameTransform_re1.sub(" ",lName.strip())
    rv=lNameTransform_re2.sub(" ",rv)
    rv=lNameTransform_re2.sub("_",rv)
    rv=lNameTransform_re3.sub("",rv)
    rv=lNameTransform_re4.sub("",rv)
    rv=rv.replace(".","_")
    rv=rv.replace("_Sheet_","_")
    rv=lNameTransform_re_end.sub(".csv",rv)
    return rv

if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        _parser.add_argument("-p", "--path_of_target_directory"
                , help="first argument, path of target directory"
                , default=lProject.lData
                )
        _parser.add_argument("--glob", "--glob-pattern"
                            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
                            , default='*.xls*'
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

        print(lProject.lDataExtracted)

        if True: 
            for d,f in dd.walk(globpattern=args.glob,isRecursive=args.recursive,isFilesOnly=args.isFilesOnly,ignore=["gExtracted","bak"]):
                print("d=",d,"f=",f)
                #if not f.startswith('X'): continue
                targetbasename=lBaseNameTransform(f,d)
                print("  TargetBase d=",lProject.lDataExtracted,"f=",targetbasename)
                Excel2CSV(osp.join(d,f)
                        , targetdir=lProject.lDataExtracted
                        , targetbasename=targetbasename
                        , NameTransform=lNameTransform
                        , isPreviewNameOnly=args.isListOnly
                        , nrows=args.nrows
                        )


    l_argparser = main_argparser()
    try:
        args=l_argparser.parse_args()
        if args.pudb:
            pudb.set_trace()
        main(args=args)
    except Exception as e:
        print("Hey")
        print(e)
        print(traceback.format_tb(e.__traceback__))



