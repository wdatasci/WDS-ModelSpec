''' 1: DataFrame like stuff
    2: numpy, pandas
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback


import time
import os.path as osp

import csv
import collections

import datetime

import numpy as np
import pandas as pd

import pyodbc

#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        _parser.add_argument("nrows"
                            , help="common number of rows"
                            , nargs='?'
                            , default=10)
        _parser.add_argument("ncols"
                            , help="common number of columns"
                            , nargs='?'
                            , default=5)
        _parser.add_argument("path_of_example_output_directory"
                            , help="first argument, path of output directory"
                            , nargs='?'
                            , default="./zzzExamples/output")
        _parser.add_argument("example_output_file"
                            , help="example output file name"
                            , nargs='?'
                            , default="DataFrame_Stuff_Output.csv")
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        if not args:
            raise('nothing passed into main')

        print()
        fno=osp.join(args.path_of_example_output_directory,args.example_output_file)
        print("example output file:%s" % fno)



        cn=pyodbc.connect('DSN=Vertica',autocommit=True)

        cr=cn.cursor()

        q='select store_key,store_number from store.store_dimension limit 10'
        q='select store_key,store_name,store_number from store.store_dimension limit 10'
        q='select * from store.store_dimension limit 10'
        print()
        print('query=%s' % q)

        qr=cr.execute(q)
        data=qr.fetchall()
        print('results:')
        print(data)

        print('result column descriptions')
        for i,c in enumerate(qr.description):
            #print(i,c)
            #CodeDoc - CJW - using %s for the field forces effectively a str() wrap and allows for None to be represented.....
            print('column %d, name=%s, type_code=%s, display_size=%s, internal_size=%d, precision=%d, scale=%d, null_ok=%d' % (i,c[0],str(c[1]),c[2],c[3],c[4],c[5],c[6]) )

        dt=np.dtype([(c[0],c[1]) for c in qr.description])
        def l_numpy_dtype_str(arg):
            if arg[1] is str: return 'U%d' % arg[4]
            if arg[1] is int: return 'i8'
            if arg[1] is datetime.date: return 'datetime64[D]'
            return 'f8'
        dt=[(c[0],l_numpy_dtype_str(c)) for c in qr.description]
        print('numpy dtype of cursor description')
        print(dt)

        #CodeDoc - CJW - the data[0] comes back as a pyodbc row object instead of the list of tuples as it prints out.
        #this needs to be converted
        xdata=[tuple(map(lambda arg:data[i].__getattribute__(arg[0]),qr.description)) for i in range(qr.rowcount)]

        print('numpy dtype of query result')
        x=np.array(xdata,dtype=dt)
        print(x)

        print()
        print('first string field')
        for c in filter(lambda x:x[1] is str, qr.description):
            print(c[0])
            print(x[c[0]])
            break

        print()
        print('row 0')
        print(xdata[0])


        print('row 0, store_name')
        print("x[0]['store_name']")
        print(x[0]['store_name'])


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


