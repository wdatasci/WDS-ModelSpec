
import WDS.Wranglers.gXMLParsers.gWDSModel as __gWDSModel
import WDS.Wranglers.gXMLParsers.gWDSModel_literal as __gWDSModel_literal


def WDSModel(filename):
    if type(filename) is str:
        rv = __gWDSModel.parse(filename)
    else:
        rv = __gWDSModel.parse(filename.read())
    return rv

def preprocess(self):
        pass




if __name__=='__main__':
    global rv
    rv = None


    def main(args=None):
        if not args: raise(Exception('nothing passed into main'))
        if args.recap:
            print("argument recap:")
            print("    --xml: ", args.xml)
            print("    --recap: ", args.recap)
            print("    --pudb: ", args.pudb)
            sys.exit()
        global rv
        rv = WDSModel(args.xml)
        return 0

    def main_argparser():
        _parser=argparse.ArgumentParser()
        _parser.add_argument("-x", "--xml", help="WDSModel spec file")
        _parser.add_argument("--recap", help="recap arguments", action="store_true")
        _parser.add_argument("--pudb", help="turn on the pudb debugger before main", action="store_true")
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






