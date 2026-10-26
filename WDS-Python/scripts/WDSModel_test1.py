#!/usr/bin/env python3.9 
'''Copyright (c) 2019-2027 Wypasek Data Science, Inc.
Released under the MIT open source license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import os
import sys
import pudb
import argparse
import traceback

import time
import os.path as osp
import re
import string
import datetime

import WDS
import WDS.Comp
import WDS.Wranglers

from WDS.Wranglers.gXMLParsers import gWDSModel
from WDS.Wranglers.gXMLParsers import gWDSModel_literal

from WDS.Comp.WDSModelPrep import *


from WDS.history import *
history_init(globals())

# for testing purposes when -i is used
rv = None
rv_literal = None
rvmo = None
x = None

def main(args=None):
    if not args:
        raise(Exception('nothing passed into main'))

    if args.recap:
        print("argument recap:")
        print("    --xml: ", args.xml)
        print("    --recap: ", args.recap)
        print("    --pudb: ", args.pudb)
        sys.exit()

    global rv
    global rv_literal
    rv = gWDSModel.parse(args.xml)
    rv_literal = gWDSModel_literal.parseLiteral(args.xml)

    print(rv)

    if type(rv) is gWDSModel.Projects:
        print("using Projects")
        if rv.Name:
            print("with name ",rv.Name)

    if type(rv) is gWDSModel.Project:
        print("using single Project")
        if rv.Name:
            print("with name ",rv.Name)

    print("top name is ", rv.Name)

    if rv.Models:
        print("using Models, a list of Model, with names")
        for mdl in rv.Models.Model:
            print(mdl.Name)

    if rv.Model:
        print("using a list of Model, with names")
        for mdl in rv.Model:
            print(mdl.Name)

    if rv.gds_elementtree_node_.xpath('count(./Models/Model/ComponentModels/ComponentModel[@Name="Applicability"])'):
        m = rv.Models.Model[0].ComponentModels

    global rvmo, x
    rvmo = WDSModelFromFile(args.xml)
    x=rvmo.Models.Model[0].ComponentModels.ComponentModel[1].Variables.Variable[0]
    x.CriticalValues_from_list([625, 660, 740])
    x.CoefficientsSet_from([[0, 1, 2, 3], [4, 6, 7, 8]])
    print(x)

if __name__=='__main__':
    def main_argparser():
        _parser=argparse.ArgumentParser()
        _parser.add_argument("-x", "--xml"
                , help="WDSModel spec file"
                )
        _parser.add_argument("--recap"
                            , help="recap arguments"
                            , action="store_true"
                            )
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser

    l_argparser = main_argparser()
    try:
        args=l_argparser.parse_args()
        if args.pudb:
            pudb.set_trace()
        main(args=args)
    except Exception as e:
        print(str(e))
        print(traceback.format_tb(e.__traceback__))






