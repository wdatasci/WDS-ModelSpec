'''
Copyright (c) 2019-2027 Wypasek Data Science, Inc.
Released under the MIT open source license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Unix-like history and ! during a python session.

Usage:
    from WDS.history import history_init

    #instantiate link to global namespace with

    history_init(globals())

    history() # to list history
    history(last=10) # to list the last 10 lines of history

    hbang(i) # as in shell, !### will run history line ###
             #  hbang(i) will evaluate history line i in the global namespace

'''
#import sys
from WDS.namespaceop import namespaceop
#_using__dict__

#if hasattr(sys,'ps1'):
import readline
#_using__dict__
@namespaceop
def history_init(arg):
    __history_namespace = locals()
    def history(last=None):
        n=readline.get_current_history_length()
        start = n-last if (last is not None) else 0
        for i in range(start,n):
            print( i, readline.get_history_item(i) )
    def hbang(i=None):
        global __history_namespace
        readline.add_history(readline.get_history_item(i))
        eval(compile(readline.get_history_item(i),"history line "+str(i),"exec"),globals(),__history_namespace)
#else:
#    @namespaceop_using__dict__
#    def history_init(arg):
#        def history(arg): pass
#        def hbang(arg): pass
#
