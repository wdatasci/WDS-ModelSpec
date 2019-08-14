'''A file system directory and file walk iterator.
Copyright 2019, Wypasek Data Science, Inc., (WDataSci/WDS)

Note: This module started as a simple python example of a 
classes/inheritance and an iterator. It provides glob 
features to os.walk.

As a file system walker/iterator, it is often used to find 
text files for processing.
'''

import os,sys
import pudb
import argparse
import traceback

import time
import os.path as osp
import glob
import fnmatch
import re


#A simple example with a  file descriptor for an example

class OSObject(object):
    '''A simple class as an example with a  file descriptor for an example
    '''
    def __init__(self):
        self._fd=None
        self._local_path=None

    def isfile(self): return osp.isfile(self._local_path)

    def isdir(self): return osp.isdir(self._local_path)

    def islink(self): return osp.islink(self._local_path)


class LocalFile(OSObject):
    def __init__(self
                ,local_path=None
                ):
        super().__init__()
        if not local_path: pass
        if ( osp.exists(local_path) and osp.isfile(local_path) ):
            #self._fd=open(local_path,'r')
            self._local_path=local_path
        else:
            raise Exception('invalid path for LocalFile, '+local_path)


class LocalDirectory(OSObject):
    def __init__(self
                ,local_path=None
                ):
        super().__init__()
        if not local_path: pass
        if ( osp.exists(local_path) and osp.isdir(local_path) ):
            self._local_path=local_path
        else:
            raise Exception('invalid path for LocalDirectory, '+local_path)

    def walk(self
                , globpattern='*'
                , ignorebase=['~','tmp']
                , ignore=None
                , isCaseInsensitive=True
                , isRecursive=False
                , isFilesOnly=False
                ):
        '''Generator for (path, file) traversing a directory.
            named arguments:
                globpattern='*' a refining glob pattern
                isCaseInsensitive=True
                isRecursive=False
                isFilesOnly=False
            When object is a directory, file=None
        '''
        ign=[]
        if ignorebase: ign.extend(ignorebase)
        if ignore: ign.extend(ignore)
        if len(ign)==0: ign=None

        if self._local_path:
            if globpattern=='*':
                for  d,sd,sf in os.walk(self._local_path):
                    if not isRecursive:
                        if not isFilesOnly:
                            for ssd in sd:
                                found=False
                                rv=osp.join(d,ssd)
                                if ign:
                                    for ig in ign:
                                        if rv.count(ig):
                                            found=True
                                            break
                                if not found: yield (rv, None)
                        for f in sf:
                                found=False
                                rv=osp.join(d,f)
                                if ign:
                                    for ig in ign:
                                        if rv.count(ig):
                                            found=True
                                            break
                                if not found: yield (d, f)
                        break
                    else:
                        if (sd is None) and (sf is None): #and empty directory and a leaf
                            if not isFilesOnly:
                                found=False
                                if ign:
                                    for ig in ign:
                                        if rv.count(d):
                                            found=True
                                            break
                                if not found: yield (d, None)
                        for f in sf:
                                found=False
                                rv=osp.join(d,f)
                                if ign:
                                    for ig in ign:
                                        if rv.count(ig):
                                            found=True
                                            break
                                if not found: yield (d,f)
            else:
                if isCaseInsensitive:
                    regex=fnmatch.translate(globpattern)
                    regexobj=re.compile('(?i)'+regex)
                    for  d,sd,sf in os.walk(self._local_path):
                        v=d
                        if not isRecursive:
                            if not isFilesOnly:
                                for ssd in sd:
                                    vv=osp.join(v,ssd)
                                    if regexobj.match(vv):
                                        found=False
                                        if ign:
                                            for ig in ign:
                                                if vv.count(ig):
                                                    found=True
                                                    break
                                        if not found: yield (vv, None)
                            for f in sf:
                                    vv=osp.join(v,f)
                                    if regexobj.match(vv):
                                        found=False
                                        if ign:
                                            for ig in ign:
                                                if vv.count(ig):
                                                    found=True
                                                    break
                                        if not found: yield (v, f)
                            break
                        else:
                            if (sd is None) and (sf is None): #and empty directory and a leaf
                                if (regexobj.match(v)) and (not isFilesOnly):
                                    found=False
                                    if ign:
                                        for ig in ign:
                                            if v.count(ig):
                                                found=True
                                                break
                                    if not found: yield (v, None)
                            else:
                                for f in sf:
                                    vv=osp.join(v,f)
                                    if regexobj.match(vv):
                                        found=False
                                        if ign:
                                            for ig in ign:
                                                if vv.count(ig):
                                                    found=True
                                                    break
                                        if not found: yield (v, f)
                else:
                    for f in glob.glob(osp.join(self._local_path,globpattern), recursive=isRecursive):
                        if osp.isdir(f) and (not isFilesOnly):
                            found=False
                            if ign:
                                for ig in ign:
                                    if f.count(ig):
                                        found=True
                                        break
                            if not found: yield (f, None)
                        else:
                            found=False
                            if ign:
                                for ig in ign:
                                    if f.count(ig):
                                        found=True
                                        break
                            if not found: 
                                h,t = osp.split(f)
                                yield (h,t)
        else:
            raise Exception('local_path not set for LocalDirectory')
        
    
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        _parser.add_argument("path_of_target_directory"
                            , help="first argument, path of target directory")
        #optional switches
        _parser.add_argument("--glob", "--glob-pattern"
                            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
                            , default='*'
                            )
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
        _parser.add_argument("--no-recursive"
                            , help="optional argument, for recursive flag set to False for glob"
                            , action='store_false'
                            , dest='recursive'
                            , default=None )
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
            print("    --glob: ", args.glob)
            print("    --CaseSensitive: ", args.CaseSensitive)
            print("    --recursive: ", args.recursive)
            print("    --recap: ", args.recap)
            print("    --pudb: ", args.pudb)
            sys.exit()

        path_of_target_directory=args.path_of_target_directory
        dd=LocalDirectory(path_of_target_directory)

        for d,f in dd.walk(globpattern=args.glob,isRecursive=args.recursive,isFilesOnly=args.isFilesOnly):
            print("d=",d,"f=",f)



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


