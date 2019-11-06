''' 1: basic read of an xslx or xlsxm file
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

import xlrd


#CodeDoc - CJW - See examples/BasicXML.py

#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        #default positional
        fn='./zzzExamples/data/Book1.xlsm'
        _parser.add_argument("Excel_to_load"
                            , help="first argument, xml to load"
                            , nargs='?'
                            , default=fn
                            )
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):
        
        w=xlrd.open_workbook(args.Excel_to_load)

        print()
        print('dir of xlrd')
        print('commented out')
        #for nm in dir(w):
            #print(nm)

        print()
        print('sheet names')
        for nm in w.sheet_names():
            print(nm)


        print()
        print('named ranges')
        for k in w.name_map:
            r=w.name_map[k]
            if type(r) is list:
                r=r[0]
            print('name=%s, scope=%d, formula_text=%s' % (r.name,r.scope,r.formula_text))

        print()
        s=w.sheet_by_index(0)
        print('Sheet index 0, name=%s', s.name)
        print('upper left corner')
        nrows=s.nrows
        if (nrows>4):
            nrows=4
        ncols=s.ncols
        if (ncols>10):
            ncols=10
        for i in range(nrows):
            for j in range(ncols):
                tmp_string='unk'
                #CodeDoc - CJW - xlrd may not give you more than string/numeric/date
                #the format mappings may not be complete (CJW, I suspect this is due to the complexity of the xlsx formatting details
                #which may allow for some simplification by "grouping" formats such as in by column, row, etc.
                #but this is generally good enough and we will have to identify integer/long columns later
                if (s.cell(i,j).ctype==1): tmp_string=s.cell(i,j).value
                elif (s.cell(i,j).ctype==2): tmp_string='%10.6f' % s.cell(i,j).value
                elif (s.cell(i,j).ctype==3): tmp_string='%d' % s.cell(i,j).value
                print( ('cell(i=%d,j=%d)[ctype=%d]=' % (i,j,s.cell(i,j).ctype) ) + tmp_string)
                
        print()
        print('dumping a csv')
        for s in w.sheets():
            print('sheet name:%s' % s.name)
            nrows=s.nrows
            ncols=s.ncols
            for i in range(nrows):
                tmp_string=''
                for j in range(ncols):
                    if j: tmp_string+=','
                    if (s.cell(i,j).ctype==1): tmp_string+=s.cell(i,j).value.strip()
                    elif (s.cell(i,j).ctype==2): tmp_string+=(s.cell(i,j).value.__str__())
                    #elif (s.cell(i,j).ctype==3): tmp_string+=('%d' % s.cell(i,j).value).strip()
                    #elif (s.cell(i,j).ctype==3): tmp_string+=(str(xlrd.xldate.xldate_as_datetime(s.cell(i,j).value,w.datemode))).strip()
                    elif (s.cell(i,j).ctype==3): 
                        if (math.fabs(math.trunc(s.cell(i,j).value)-s.cell(i,j).value)<1e-8):
                            try:
                                y,m,d,hh,mm,ss=xlrd.xldate.xldate_as_tuple(s.cell(i,j).value,w.datemode)
                                tmp_string+=str(date(y,m,d)).strip()
                            except Exception as e:
                                print("skipped a bad date cast")
                        else:
                            tmp_string+=(str(xlrd.xldate.xldate_as_datetime(s.cell(i,j).value,w.datemode))).strip()
                print(tmp_string)

        print()
        print('datemode of workbook:',w.datemode)

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


