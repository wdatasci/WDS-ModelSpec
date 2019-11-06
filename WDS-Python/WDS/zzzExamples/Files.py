''' 1: basic file examples
    2: csv module examples
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


#CodeDoc - CJW - see examples/HelloWorld.py
if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        dirn='./zzzExamples'
        _parser.add_argument("path_of_example_directory"
                            , help="first argument, path of example directory"
                            , nargs='?'
                            , default=dirn + "/data")
        _parser.add_argument("example_file"
                            , help="example file name"
                            , nargs='?'
                            , default="housing.csv")
        _parser.add_argument("path_of_example_output_directory"
                            , help="first argument, path of output directory"
                            , nargs='?'
                            , default=dirn + "/output")
        _parser.add_argument("example_file"
                            , help="example file name"
                            , nargs='?'
                            , default="housing.csv")
        _parser.add_argument("example_output_file"
                            , help="example output file name"
                            , nargs='?'
                            , default="Files_Output.csv")
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
        fn=osp.join(args.path_of_example_directory,args.example_file)
        fno=osp.join(args.path_of_example_output_directory,args.example_output_file)
        print("example file:%s" % fn)
        print("example output file:%s" % fno)

        print()
        print('using a with statement, reading 10 lines, also written to output file:')
        with open(fn,'r') as fidw, open(fno,'w') as fidwo :
            for i in range(10):
                row=fidw.readline()
                fidwo.write(row)
                print("row[%d]:%s" % (i,row))
        print()
        print('characters of last row')
        for ch in row:
            print("%c - %d" % (ch, ord(ch)))

        #CodeDoc - CJW - example, uncommented throws an error because fidw is closed at the exit of the with-statement
        #fidw.readline()


        print()
        print('reading 10 lines:')
        fid=open(fn,'r')
        
        r=fid.readline()
        i=-1
        while r:
            i+=1
            print("row[%d]:%s" % (i,r))
            if i>9: break
            r=fid.readline()

        
        print()
        print('using csv module')
        print('as iterator')
        #just re-positioning instead of re-opening
        fid.seek(0) 
        csv_reader=csv.reader(fid)
        for i,row in enumerate(csv_reader):
            print("row[%d]:%s" % (i,row))
            if i>9: break

        #CodeDoc - CJW - the seek also resets the reader
        fid.seek(0)
        print('using sniffer, has_header?:%s' % csv.Sniffer().has_header(fid.read(10000)))
        fid.seek(0)
        print('using sniffer, dialect:')
        dialect=csv.Sniffer().sniff(fid.read(10000))
        fid.seek(0)

        for s in dir(dialect):
            if s[0]!='_':
                try:
                    print('%s:%s' % (s,str(dialect.__dict__[s])))
                except Exception as e:
                    print('%s:Empty or None or Exception when calling dialect[s]' % s)
                if s=='lineterminator':
                    print('for line terminator, len()=%d' % len(dialect.lineterminator))
                    for i,c in enumerate(dialect.lineterminator):
                        print('ord for %d:%d' % (i,ord(c)))

        
        print()
        print('comparing sniffed dialect against csv.excel')
        for s in dir(dialect):
            if s[0]!='_':
                try:
                    print('%s:%s, csv.excel.%s:%s, match:%s' % (s,str(dialect.__dict__[s]),s,str(csv.excel.__dict__[s]),str(dialect.__dict__[s]==csv.excel.__dict__[s])))
                except Exception as e:
                    print('%s:Empty or None or Exception when calling dialect[s]' % s)

        print()
        print("using DictReader")
        fid.seek(0)
        dr=csv.DictReader(fid,restkey='ExtraColumn',restval=None,dialect=dialect)
        for i,row in enumerate(dr):
            print("row[%d]:%s" % (i,row))
            if i>9: break

        print()
        print('setting QUOTE_NONNUMERIC in the dialect')
        #CodeDoc - CJW - setting the quoting as below seems not to work alone because of parsing of the fieldnames in the first row
        #CodeDoc - CJW - It also did not appear to work when resetting in dr after initialization
        #CodeDoc - CJW - It works here, because we are pulling the field names from the previous DictReader and we have to skip the header row in processing.
        dialect.quoting=csv.QUOTE_NONNUMERIC
        fid.seek(0)
        r=fid.readline()
        drn=csv.DictReader(fid,fieldnames=dr.fieldnames,restkey='ExtraColumn',restval=None,dialect=dialect)
        for i,row in enumerate(drn):
            print("row[%d]:%s" % (i,row))
            if i>9: break

        fid.close()

        print()
        print('using DictWriter')

        data=collections.OrderedDict()
        data['z']=34
        data['AA']='Hey'
        data['X']='Quote" In the Middle'
        print('Example OrderedDict:',data)

        fido=open(fno,'w')
        dw=csv.DictWriter(fido, fieldnames=list(data.keys()), dialect=csv.excel)
        dw.writeheader()
        dw.writerow(data)
        data['X']='no quote'
        dw.writerow(data)
        fido.close()

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


