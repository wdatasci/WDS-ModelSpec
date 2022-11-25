'''namespaceop.py

A decorator for a function that replaces the local namespace of the function 
with that of its argument.

In this way, syntax like one might use at a module level can be done within a namespace.

Older versions of python used to let one re-assign __G (the global namespace) and the module namespace.
This used to allow one use an implied scope without an object prefix.

a = 1
b = 3

This can also be done now in limited cases, such as in the __init__ of a class:

class hey(object):
    def __init__(self):
        a = 1
        b = 3
        vars(self).update(vars())

For which, x=hey(), would have x.a=1 and x.b=3.

The decorator @namespaceop compiles the body of a function and evaluates it on the namespace of its arguement.

    x=hey()

    @namespaceop
    def what(input):
        x = 11
        a += x
        x += b

    what(x)

After which, x.a = 12 and the namespace x (the input namespace) has had x.x added to it.

This does also work for methods within classes:

    class hey(object):
        @namespaceop
        def __init__(self):
            a=1
            b=2

        @namespaceop
        def withsomestuff(self):
            x=17
            a+=x
            x+=b


Note:
- The target of the function has no return value. 
- There only one argument, the namespace.  Any inputs or outputs of the targeted function go through the namespace.
- Any "temporary" or variables meant to be kept local will need to be deleted before exiting the function.
- At compile time, the decorator re-compiles the souce code of the target.
  - The re-compiled code can then be run on a different local namespace.
  - The global namespace is the same as the function being wrapped, there is no need to global module level variables.
- The decorator gobbles (to use a TeX term) the first two lines of the source code of the target.
  - It does this by making the @namespaceop/def lines inoccuous.
  - There should not be any line returns between :'s in the function def.

'''

import inspect

def namespaceop(func):
    __func = inspect.getsource(func)
    __func_lines = inspect.getsourcelines(func)
    __func_name = func.__name__
    print(__func_lines)
    n = __func.count('\n',0,__func.index(':'))
    __func = compile('if True:#'+__func.replace('\n','',n),func.__name__,'exec')
    def __func_wrapped(arg):
        try:
            if type(arg) is dict:
                eval(__func,func.__globals__,arg)
            else:
                eval(__func,func.__globals__,vars(arg))
        except Exception as e:
            raise(Exception('namespaceop error in '+__func_name+' at func lineno '+str(e.__traceback__.tb_next.tb_lineno)
                + ', file lineno '+str(__func_lines[1]+e.__traceback__.tb_next.tb_lineno)+' line:\n'+__func_lines[0][e.__traceback__.tb_next.tb_lineno]))
    return __func_wrapped

def namespaceop_using__dict__(func):
    __func = inspect.getsource(func)
    __func_lines = inspect.getsourcelines(func)
    __func_name = func.__name__
    print(__func_lines)
    n = __func.count('\n',0,__func.index(':'))
    __func = compile('if True:#'+__func.replace('\n','',n),func.__name__,'exec')
    def __func_wrapped(arg):
        try:
            eval(__func,func.__globals__,arg)
        except Exception as e:
            raise(Exception('namespaceop error in '+__func_name+' at func lineno '+str(e.__traceback__.tb_next.tb_lineno)
                + ', file lineno '+str(__func_lines[1]+e.__traceback__.tb_next.tb_lineno)+' line:\n'+__func_lines[0][e.__traceback__.tb_next.tb_lineno]))
    return __func_wrapped




if __name__=='__main__':
    
    class hey(object):
        def __init__(self):
            self.a = 1
            self.b = 2

    x = hey()

    @namespaceop
    def what(input):
        x = 11
        a+= x
        x+= b

    x = hey()
    print('x.a = ',x.a)
    print('x.b = ',x.b)
    try:
        print('x.c = ',x.c)
    except Exception as e:
        print(str(e))
    try:
        print('x.x = ',x.x)
    except Exception as e:
        print(str(e))
    
    what(x)
    
    print('x.a = ',x.a)
    print('x.b = ',x.b)
    try:
        print('x.c = ',x.c)
    except Exception as e:
        print(str(e))
    try:
        print('x.x = ',x.x)
    except Exception as e:
        print(str(e))

    @namespaceop
    def huh(input):
        x = 11
        x = z
        a+= x
        x+= b

    #For debugging purposes, throw an error and report the function and file line numbers
    huh(x)


