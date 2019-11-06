''' 1: basic read of an xslx or xlsm file
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback
import math

from datetime import date


import time
import os.path as osp

import xlsxwriter as xw

#CodeDoc - CJW - the apt-get did not install XlsxWriter's vba_extract.py, using the guts here
#https://github.com/jmcnamara/XlsxWriter/blob/master/examples/vba_extract.py

from zipfile import ZipFile


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

        w0=ZipFile(args.Excel_to_extract_vba_from)
        vba=w0.read('xl/vbaProject.bin')
        fn3='./zzzExamples/output/vbaProject.bin'
        with open(fn3,'wb') as fd:
            fd.write(vba)

        #from xslxwriter.readthedocs.io
        w=xw.Workbook(args.Excel_to_write)
        w.add_vba_project(fn3)
        s=w.add_worksheet()
        s.set_column('A:A',20)
        bf=w.add_format({'bold':True})
        s.write('A1','Hello')
        s.write('A2','World',bf)
        s.write(2,0,123)
        s.write_formula('B3','=local_test_function(A3)')
        s.write(3,0,123.456)

        w.close()

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


