''' 1: basic iterator examples
    2: filter examples
    3: creating an iterator class
    4: traversing a directory
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback


import time
import os.path as osp
import glob
import fnmatch
import re


#CodeDoc - CJW - Here, we are embedding all functions in the body of the if-statement.
#see HelloWorld and MonkeyPatch examples for argparse and class notes


#RefDoc - CJW - iterators vs generators references:
#   http://nvie.com/posts/iterators-vs-generators
#   http://www.learningpython.com/2009/02/23/iterators-iterables-and-generators-oh-my/#LookingMoreCloselyAtTheIterator

#RefDoc - CJW - simple decorator references:
#https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#what-can-you-do-with-decorators
#https://www.python-course.eu/python3_decorators.php   -- not that helpful....


#CodeDoc - CJW - simple logging decorator:
__module_log__=''
class LogIt(object):
    def __init__(self,arg):
        global __module_log__
        __module_log__+=str.format('decorating call {} at time.monotonic()={}\n',arg,time.monotonic())
    def __call__(self,fnc):
        global __module_log__
        __module_log__+=str.format('decorating {} at time.monotonic()={}\n',fnc.__name__,time.monotonic())
        def _LogItWrap(*args,**kwargs):
            global __module_log__
            __module_log__+=str.format('Entered into {} at time.monotonic()={}\n',fnc.__name__,time.monotonic())
            fnc(*args,**kwargs)
            __module_log__+=str.format('Exited from {} at time.monotonic()={}\n',fnc.__name__,time.monotonic())
        return _LogItWrap



#A simple example with a  file descriptor for an example

class OSObject(object):
    '''A simple class as an example with a  file descriptor for an example
    '''
    def __init__(self):
        self._fd=None
        self._local_path=None


class LocalFile(OSObject):
    def __init__(self
                ,local_path=None
                ):
        super().__init__()
        if not local_path:
            pass
        if (    osp.exists(local_path)
            and osp.isfile(local_path)
            ):
            self._fd=open(local_path,'r')
            self._local_path=local_path
        else:
            raise Exception('invalid path for LocalFile, '+local_path)



class LocalDirectory(OSObject):
    def __init__(self
                ,local_path=None
                ):
        super().__init__()
        if not local_path:
            pass
        if (    osp.exists(local_path)
            and osp.isdir(local_path)
            ):
            self._local_path=local_path
        else:
            raise Exception('invalid path for LocalDirectory, '+local_path)

    @LogIt('ClassMethod')
    def os_walk_list(self):
        ''' uses a list-wrap to realize the generator
        '''
        if self._local_path:
            return list(os.walk(self._local_path,))
        else:
            raise Exception('local_path not set for LocalDirectory')
        

    @LogIt('ClassMethod')
    def os_walk(self):
        ''' a printing example to use the "generator" aspect of os.walk
        '''
        if self._local_path:
            i=0
            for v in os.walk(self._local_path):
                i+=1
                print(str.format('element {} of os.walk({}): ',i,self._local_path),v)
            return list(os.walk(self._local_path,))
        else:
            raise Exception('local_path not set for LocalDirectory')
        
    
    

    @LogIt('ClassMethod')
    def glob_list(self
                ,arg                        #glob pattern
                ,case_insensitive=True
                ,recursive=False
                ):
        if self._local_path:
            if arg:
                larg=(arg)
                if case_insensitive:
                    #RefDoc - CJW - hint from https://stackoverflow.com/questions/500864/case-insensitive-python-regular-expression-without-re-compile
                    rv=[]
                    bSubDirInSearch=(arg.find(osp.sep)>=0)
                    regex=fnmatch.translate(arg)
                    regexobj=re.compile('(?i)'+regex)
                    for d,sd,f in os.walk(self._local_path):
                        for v in f:
                            vv=osp.join(d,v)
                            #print(vv)
                            if regexobj.match(vv):
                                rv.append(vv)
                    return rv
                else:
                    return glob.glob(osp.join(self._local_path
                                            ,larg
                                            )
                                        ,recursive=recursive
                                )
            else:
                raise Exception('glob argument not passed')
        else:
            raise Exception('local_path not set for LocalDirectory')
        
    #a class within a class, restricting it's use, at least symbolically, in this class namespace
    class iterator_example(object):
        def __init__(self):
            self._local_data=3

        def __iter__(self):
            self._local_i=-1
            return self

        def __next__(self):
            self._local_i+=1
            #exit criterion
            if self._local_i>=self._local_data: 
                raise StopIteration
            #next value (including the first) yielded
            return self._local_i
            

    #CodeDoc - CJW - until I can figure out how to get the class within a class to access the outside class's namespace
    def iterator_directory_contents(self): return self._iterator_directory_contents(self._local_path)

    def iterator_subdirectories(self): return self._iterator_subdirectories(self._local_path)

    #a class within a class, restricting it's use, at least symbolically, in this class namespace
    class _iterator_directory_contents(object):
        ''' a simple iterator exploiting the glob.iglob iterator
        '''
        def __init__(self
                , local_path
                ):
            self._local_data=glob.iglob(osp.join(local_path,'*'),recursive=False)

        def __iter__(self):
            return self

        def __next__(self):
            return self._local_data.__next__()
            #CodeDoc - CJW - this does not need the exit throw since the glob.iglob iterator raise of StopIteration is not caught
            #But, if the value is stored first, it can be checked against other criterion before returning, such as in the next example.
            #This will be done in the WDS library.

    class _iterator_subdirectories(object):
        ''' a simple iterator exploiting the glob.iglob iterator
        '''
        def __init__(self
                , local_path
                ):
            self._local_data=glob.iglob(osp.join(local_path,'*'),recursive=False)

        def __iter__(self):
            return self

        def __next__(self):
            rv=self._local_data.__next__()
            #print(rv,osp.isdir(rv))
            while not osp.isdir(rv):
                rv=self._local_data.__next__()
            return rv

    #@LogIt('ClassMethod')
    def generator_subdirectories(self):
        for sd in self._iterator_subdirectories(self._local_path):
            yield sd
            sdd=LocalDirectory(sd)
            for ssdd in sdd.generator_subdirectories():
                yield ssdd






#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        _parser.add_argument("path_of_target_directory"
                            , help="first argument, path of target directory")
        #optional switches
        _parser.add_argument("--glob_pattern"
                            , help="optional argument for unix-like glob pattern (watch escaping when using p_m)"
                            , default=None
                            )
        _parser.add_argument("-i", "--case-insensitive", "--CaseInsensitive"
                            , help="optional argument, for case insensitive"
                            , dest="case_insensitive"
                            , action='store_true'
                            , default=True )
        _parser.add_argument("-I", "--case-sensitive", "--CaseSensitive"
                            , help="optional argument, for case sensitive"
                            , action='store_false'
                            , dest='case_insensitive'
                            , default=None )
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
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        if not args:
            raise('nothing passed into main')

        for i in range(10): print()

        path_of_target_directory=args.path_of_target_directory
        print("path_of_target_directory=",path_of_target_directory)
        dd=LocalDirectory(path_of_target_directory)

        print()
        print('os_walk_list method:')
        print(dd.os_walk_list())
       
        print()
        print('os_walk method:')
        print(dd.os_walk())

        print()
        if args.glob_pattern:
            if args.case_insensitive:
                print('glob.iglob method:')
            else:
                print('glob.glob method:')
            print(dd.glob_list(args.glob_pattern
                    ,recursive=args.recursive
                    ,case_insensitive=args.case_insensitive
                    ))
        else:
            print('no glob pattern provided')

        print()
        print('iterator examples')

        print()
        print('directory contents')
        for i in dd.iterator_directory_contents(): print(i)

        print()
        print('directory subdirectories')
        for i in dd.iterator_subdirectories(): print(i)

        print()
        print('directory subdirectories via generator recursively')
        for i in dd.generator_subdirectories(): print(i)


        print('Log message')
        global __module_log__
        print(__module_log__)

        print()
        print('fin')
        

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


