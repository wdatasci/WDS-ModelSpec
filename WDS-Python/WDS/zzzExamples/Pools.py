''' 1: basic read of an xslx or xlsm file
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback
import math
import random
import numpy

import time
import os.path as osp


import concurrent.futures
import multiprocessing as mp

#CodeDoc - CJW - hints from concurrent futures doc and 
#https://www.programcreek.com/python/example/8456/multiprocessing.Manager


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    112272535095293,
    112582705942171,
    ]

for x in range(PRIMES[5],PRIMES[5]+2):
    PRIMES.append(x)



def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime2(i):
    global PRIMES
    n=PRIMES[i]
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


global inq, outq

def is_prime3(i):
    global inq,outq,PRIMES
    n=PRIMES[i]
    iv=inq.get()
    time.sleep(random.uniform(0,1)*2)
    rv=numpy.zeros((3,iv+3))
    rv[0,0]=i
    rv[1,0]=iv
    #rv[2,0]=n
    outq.put(rv)
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True




if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        #default positional
        #RefDoc - CJW - hint from https://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments
        fn='./zzzExamples/output/ExcelWrite_Out.xlsm'
        _parser.add_argument("Excel_to_write"
                            , help="first argument, xml to load"
                            , nargs='?'
                            , default=fn
                            )
        fn2='./zzzExamples/data/Book1.xlsm'
        _parser.add_argument("Excel_to_extract_vba_from"
                            , help="An existing xlsm to extract vbaProject.bin from"
                            , nargs='?'
                            , default=fn2
                            )
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):

        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
                print('%d is prime: %s' % (number, prime))

        #using the PRIMES as already defined for the spawned processes
        n=len(PRIMES)
        ln=list(range(n))
        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            for number, prime in zip(ln, executor.map(is_prime2, ln)):
                print('index %d, %d is prime: %s' % (number, PRIMES[number], prime))

        #pudb.set_trace()
        ex=concurrent.futures.ProcessPoolExecutor(max_workers=3)
        m=mp.Manager()
        global inq,outq
        inq=m.Queue()
        for i,v in enumerate(PRIMES):
            inq.put(i+7)
        outq=m.Queue()
        for number, prime in zip(ln, ex.map(is_prime3, ln)):
            print('index %d, %d is prime: %s' % (number, PRIMES[number], prime))
        
        while not outq.empty():
            print(outq.get())

        print()
        print('fin')

    #end def main
        

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


