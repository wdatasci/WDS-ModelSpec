''' super basic example of
    1: Hello World
    2: importing modules
    3: pudb
    4: argparse
    5: exception handling
    '''


import os,sys
import pudb
import argparse
import traceback



#CodeDoc - CJW - Here, we are embedding all functions in the body of the if-statement.
#We are doing this so that any import * lines do not pull these functions.
#These are strictly for testing this code.

if __name__=="__main__":
    def main_argparser():
        _parser=argparse.ArgumentParser()
        #CodeDoc - CJW - see examples/Iterators.py for additional argument examples
        #positional
        #see generateDS_example_usage.py for default positional usage
        _parser.add_argument("arg1", help="first argument")
        _parser.add_argument("arg2", help="second argument")
        #optional switches
        _parser.add_argument("--pudb"
                            , help="turn on the pudb debugger before main"
                            , action="store_true"
                            )
        return _parser

    def main(args=None):
        print("Test of " + __file__)
        print("Hello World!")

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


