''' super basic example of
    1: a python class
    2: a subclass
    3: "MonkeyPatching" the subclass
    4: a basic numpy array
    '''


import os,sys
import pudb
import argparse
import numpy as np
import traceback



#CodeDoc - CJW - Here, we are embedding all functions in the body of the if-statement.
#We are doing this so that any import * lines do not pull these functions.
#These are strictly for testing this code.

class A(object):
    #StyleDoc - CJW - class comments are read directly from the first un-named string
    '''Class A is a small wrapper around a numpy array
    '''
    '''Additional doc strings will not show up when calling help(A)
    '''
    #StyleDoc - CJW - using leading _ to denote what in other languages is private or not generally to be used directly

    #CodeDoc - CJW - variables in this scope are available to all instances of this class
    _class_variable_A=None
    _class_variable_B=None

    #CodeDoc - CJW - default constructor
    #There can only be one __init__ constructor in Python (overloading is not possible)
    def __init__(self
                ,datatype=None
                ,rows=None
                ,cols=None
                ,data=None):
        self._datatype=datatype
        self._rows=rows
        self._cols=cols
        self._data=data

    #CodeDoc - CJW - a constructor class method which sets some parameters
    #This enables a constructor of the form:  a=A.zeros(nrows,ncols)
    @classmethod
    def zeros(cls,nrows,ncols):
        return cls(datatype=np.double
            ,rows=nrows
            ,cols=ncols
            ,data=np.zeros([nrows,ncols],dtype=np.double)
            )

    def __repr__(self):
        return str(self._data)


class B(A):
    '''A sub-class of A, an example of using the sub-class to set up a different constructor
    '''
    def __init__(self,nrows,ncols):
        super().__init__(
            datatype=np.double
            ,rows=nrows
            ,cols=ncols
            ,data=np.zeros([nrows,ncols],dtype=np.double)
            )
        self._data+=123.45




#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        #_parser.add_argument("arg1", help="first argument")
        #_parser.add_argument("arg2", help="second argument")
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        print()
        print("Test of " + __file__)
        a=A
        print()
        print('a default is an instance of A, print(type(a)):')
        print(type(a))
        print('print(a):')
        print(a)
        print()
        print('resetting a using zeros constructor')
        a=A.zeros(10,5)
        print('a=A.zeros(10,5);help(a)')
        help(a)
        print("a=",a)
        print('dir(a)')
        print(dir(a))

    
        print()
        #Forcing a monkeypatch, just by adding a field
        B._hey=8
        print('Forcing a monkeypatch, just by adding a field to the class (definition), B._hey=8')
        print()
        print('print(dir(B)):')
        print(dir(B))

        #adding a method to a class
        print('MonkeyPatch, via adding an attribute:')
        print('def hmm(slf, arg1): slf._data-=arg1')
        print('setattr(B,"hmm",hmm)')
        def hmm(slf, arg1): slf._data-=arg1
        setattr(B,'hmm',hmm)
        print()
        print('now create an instance of B, b=B(3,7)')
        b=B(3,7)
        print("b=",b)
        print('now run the new monkey-patched method, b.hmm(12.345)')
        b.hmm(12.345)
        print("b=",b)
        print('print(dir(b))')
        print(dir(b))


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


