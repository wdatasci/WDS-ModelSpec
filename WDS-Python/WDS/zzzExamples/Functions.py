''' 1: basic function examples
    2: passing functions
    3: lambdas
    4: decorators
    '''


import os,sys
import pudb
import argparse
import numpy as np
import math
import traceback



#CodeDoc - CJW - Here, we are embedding all functions in the body of the if-statement.
#see HelloWorld and MonkeyPatch examples for argparse and class notes


#example from a coding interview

def NPV( discount_rate  #constant
        ,arg1  # array of values
        ):
    ''' 
        simple npv calc,
        discount_rate is per-period
        arg1 is an iterable array of values where discount_rate is applied at the end of each period
        '''
    s=0
    for i,v in enumerate(arg1):
        s+=(0.0+v)/(1.0+discount_rate)**(i+1.0)
    return s


def NPV2( discount_rate  #constant
        ,arg1  # array of values
        ,verbose=False  #to turn on prints
        ):
    ''' 
        simple npv calc, without iterator
        '''
    l=len(arg1)
    x=list(range(l))
    if verbose: print(x)
    if verbose: y=np.array(list(range(l)),dtype=np.double)
    if verbose: print(y)
    if verbose: y=(1.0+np.array(list(range(l)),dtype=np.double))
    if verbose: print(y)
    if verbose: y=(1.0+discount_rate)**(1.0+np.array(list(range(l)),dtype=np.double))
    if verbose: print(y)
    y=np.array(arg1,dtype=np.double)/((1.0+discount_rate)**(1.0+np.array(list(range(l)),dtype=np.double)))
    if verbose: print(y)
    y=sum(y)
    if verbose: print(y)
    return (y)


def NPV_FirstDerivative( discount_rate  #constant
        ,arg1  # array of values
        ):
    ''' 
        simple npv calc, without iterator
        '''
    l=len(arg1)
    x=list(range(l))
    i=1.0+np.array(list(range(l)),dtype=np.double)
    y=np.array(arg1,dtype=np.double)*(-i)
    y/=(1.0+discount_rate)**(1.0+i)
    y=sum(y)
    return (y)


# this is not generalized, this is just for a code example

def InvF( target    #goal value to find to find
        ,initial_guess  #starting point
        ,arg1           #array of values
        ,fnc            #function to use
        ,fnc_deriv=None #function inverse to use if available
        ,eps=1.0e-6     #acceptible target difference
        ,verbose=False  #to turn on prints
        ):
    '''InvF( target    #goal value to find to find
        ,initial_guess  #starting point
        ,arg1           #array of values
        ,fnc            #function to use
        ,fnc_deriv=None #function inverse to use if available
        ,eps=1.0e-6     #acceptible target difference
        )
    returns the discount rate which solves target=fnc(result,arg1)
    '''
    xnp1=initial_guess
    fxnp1=fnc(xnp1,arg1)
    diff=target-fxnp1

    if math.fabs(diff)<eps:
        return xnp1

    use_deriv=(fnc_deriv is not None)

    if not use_deriv:
        xn=initial_guess/2.0
        fxn=fnc(xn,arg1)

    i=-1
    while math.fabs(diff) > eps:
        i+=1
        xn=xnp1
        if i:
            fxn=fxnp1
        else:
            fxn=fnc(xn,arg1)
        if use_deriv:
            fpxn=fnc_deriv(xn,arg1)
            if math.fabs(fpxn)<=eps:
                raise('near-zero derivative encountered at '+xn)
        else:
            huh=1
        #since we are finding the root, the target function is actually fnc-target
        #which does not contribute to derivative
        xnp1=xn-(fxn-target)/fpxn
        fxnp1=fnc(xnp1,arg1)
        diff=target-fxnp1
        if verbose: print("xn=",xn)
        if verbose: print("fxn=",fxn)
        if verbose: print("fpxn=",fpxn)
        if verbose: print("xnp1=",xnp1)
        if verbose: print("fxnp1=",xnp1)
        if verbose: print("diff=",diff)


    return (xnp1)





    



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
        a=[10,11,12,13,14]
        print("a=",a)
        r=.01
        print("r=",r)
        print("npv=NPV(r,a)=",NPV(r,a))
        print("using verbose setting in NPV2")
        y=NPV2(r,a,verbose=True)
        print("npv=NPV2(r,a)=",NPV2(r,a))
        target_value=50.0
        initial_guess=-0.01
        print("target_value=",target_value)
        print("initial_guess=",initial_guess)
        y=InvF(target_value,initial_guess,a,NPV2,NPV_FirstDerivative)
        print("y=InvF(target_value,initial_guess,a,NPV2,NPV_FirstDerivative)=",y)

        print("using a lambda as the function:")

        f=lambda discount_rate, arg1: sum(np.array(arg1,dtype=np.double)/((1.0+discount_rate)**(1.0+np.array(list(range(len(arg1))),dtype=np.double))))
        fderiv=lambda discount_rate, arg1: sum(np.array(arg1,dtype=np.double)*(-(1.0+np.array(list(range(len(arg1))),dtype=np.double)))
                                                    /((1.0+discount_rate)**(2.0+np.array(list(range(len(arg1))),dtype=np.double))))
        print("f=",f)
        print("npv=f(r,a)=",f(r,a))
        y=InvF(target_value,initial_guess,a,f,fderiv)
        print("y=InvF(target_value,initial_guess,a,f,fderiv)=",y)


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


