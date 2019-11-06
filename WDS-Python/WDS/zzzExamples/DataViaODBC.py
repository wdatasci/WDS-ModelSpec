''' 1: basic ODBC
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback
import collections


import time
import os.path as osp

import pyodbc


#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":

    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser


    def main(args=None):

        print('this uses the "Vertica" unixodbc dataset name defined in /etc/odbc.ini and "VerticaDriver" defined in /etc/odbcinst.ini')

        print('this is also set-up with the example VMart database, the standard Vertica example')

        cn=pyodbc.connect('DSN=Vertica',autocommit=True)

        cr=cn.cursor()

        q='select * from store.store_dimension limit 10'
        print()
        print('query=%s' % q)

        qr=cr.execute(q)

        print()
        print('dir of result set')
        print(dir(qr))


        fromthehelp='''
         |  description
         |      This read-only attribute is a sequence of 7-item sequences.  Each of these
         |      sequences contains information describing one result column: (name, type_code,
         |      display_size, internal_size, precision, scale, null_ok).  All values except
         |      name, type_code, and internal_size are None.  The type_code entry will be the
         |      type object used to create values for that column (e.g. `str` or
         |      `datetime.datetime`).
         |      
         |      This attribute will be None for operations that do not return rows or if the
         |      cursor has not had an operation invoked via the execute() method yet.
         |      
         |      The type_code can be interpreted by comparing it to the Type Objects defined in
         |      the DB API and defined the pyodbc module: Date, Time, Timestamp, Binary,
         |      STRING, BINARY, NUMBER, and DATETIME.
         |  
        '''

        print()
        print('result column descriptions')
        for i,c in enumerate(qr.description):
            #print(i,c)
            #CodeDoc - CJW - using %s for the field forces effectively a str() wrap and allows for None to be represented.....
            print('column %d, name=%s, type_code=%s, display_size=%s, internal_size=%d, precision=%d, scale=%d, null_ok=%d' % (i,c[0],str(c[1]),c[2],c[3],c[4],c[5],c[6]) )


        row=qr.fetchone()
        s=' '.join(['%s' % c for c in map(lambda x:x[0],row.cursor_description)])
        print()
        print('dir of row')
        print(dir(row))

        print('cursor_description of row')
        print(row.cursor_description)
        

        print()
        print('column names')
        print(s)


        print()

        print('result set:')
        print(row)

        for row in qr:
            print(row)

        qr=cr.execute(q)

        for row in qr:
            d=row.cursor_description
            rd=collections.OrderedDict()
            for i,c in enumerate(map(lambda x:x[0],row.cursor_description)):
                rd[c]=row[i]
            s=',        '.join(['%s:%s' % (a,b) for a,b in rd.items()])
            print(s)



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


