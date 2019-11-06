''' 1: basic XML
    2: generateDS results, this one uses a pmml xsd to bind, so it must load a 4.3 compatible pmml
    '''


#basic python imports
import os,sys
import pudb
import argparse
import traceback


import time
import os.path as osp
import xml.etree.ElementTree as xmlet
#using lxml because of xslt support
import lxml.etree as lxmlet

import xml.dom.minidom as minidom
import xml

#import zzzExamples.output.generateDS_example_pmml_4_0 as genDS_pmml
import zzzExamples.output.generateDS_example_pmml_4_3 as genDS_pmml


if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #positional
        #default positional
        fn='./zzzExamples/data/IrisMultinomReg.xml'
        _parser.add_argument("xml_to_load"
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
        #CodeDoc - CJW - default and nargs='?' for xml_to_load creates a non-empty args
        if not args:
            #raise('nothing passed into main')
            print('nothing passed into main, using '+args.xml_to_load)
        
        x1=genDS_pmml.parse(args.xml_to_load)

        print()
        print(dir(x1))

        #this filters to just the names of models
        #this is also an example of the filter iterator
        for m in filter(lambda x:(x.find('Model')>-1 and x.find('set_')==-1 and x.find('add_')==-1 and x.find('get_')==-1 and x.find('insert_')==-1 and x.find('replace_')==-1),dir(x1)):
            #print(x1.__dict__[m])
            print("for model %s, non-empty? %d" % (m,len(x1.__dict__[m])>0) )

        return

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


