'''
WDSModelPrep.py

Uses the generateDS_unsnaked parsers for WDSModel.xsd.

There are several objects which can be treated as lists or sets.
For something such as Model[s] (plural as the set version, only 
0-or-1 Models object can be include or 0-or-more Model Objects.
(If there is a Models object, any Model objects must be contained
therewithin, or 0-or-more Model objects (without any Models object)
can be in the parent).

As far as the bound python object, the potential list of Model objects 
can be manipulated with:
        get_Model (returns list)
        set_Model (sets list)
        add_Model (adds to list)
        insert_Model_at
        replace_Model_at

But as an at-most-one element, if not used, Project.Models is None.

Therefore, to unify the treatment, after parsing, a processing is done:
    -   if parent.Models is not None and parent.Model is empty:
        parent.Model = parent.Models.Model
    -   if parent.Models is None and parent.Model is not None:
        parent.Model = parent.Models.Model

In this manner, one can naturally index:
    parent.Model[#]

The generateDS created classes should only output the plural form.

The objects this applies to include:
    Model[s]
    ComponentModel[s]
    Variable[s]
    Response[s]
    Variable[s]
    Source[s]
    Constant[s]
    Transformation[s]
    CleanLimit[s]
    DropIndex[s]    (yes, plural would be Indices, but it is only one)
    CriticalValue[s]
    CriticalWord[s]
    CoefficientSet[s]


AAAAList elements are only for short-hand purposes for inititial writing.
Processing will replace these with their plural/value versions.
Elements with list versions are:
    CriticalValue[List]
    CriticalWord[List]
    DropIndex[List]
    Coefficient[List]

For simplicity, Value[s] that are never strings might also use <v> elements,
non-numerics can use <w> elements.

'''

from collections import OrderedDict as __OrderedDict

import WDS.Wranglers.gXMLParsers.gWDSModel as __gWDSModel
import WDS.Wranglers.gXMLParsers.gWDSModel_literal as __gWDSModel_literal

#Monkey patching CriticalValues, CleanLimits, and CoefficientSets to add as_list() methods

def __v_as_CriticalValue(self):
    return __gWDSModel.CriticalValue(Position=int(self.Position), valueOf_=self.valueOf_)
setattr(__gWDSModel.v,"as_CriticalValue",__v_as_CriticalValue)

def __v_as_CleanLimit(self):
    return __gWDSModel.CleanLimit(Position=int(self.Position), valueOf_=self.valueOf_)
setattr(__gWDSModel.v,"as_CleanLimit",__v_as_CleanLimit)

def __v_as_Coefficient(self):
    return __gWDSModel.Coefficient(Position=int(self.Position), valueOf_=self.valueOf_)
setattr(__gWDSModel.v,"as_Coefficient",__v_as_Coefficient)

def __CriticalValues_as_list(self):
    rv=[]
    if hasattr(self,"v") and (len(self.v)>0):
        n = len(self.v)
        rv=[None for i in range(0, n)]
        found_anyPosition = False
        for i,c in enumerate(self.v):
            if c.Position:
                found_anyPosition = True
                rv[int(c.Position)] = c.valueOf_
            else:
                if not found_anyPosition:
                    rv[i] = c.valueOf_
                else:
                    if rv[i]:
                        raise(Exception("in CriticalValues_as_list, Position ", i, " cannot be filled twice"))
                    else:
                        rv[i] = c.valueOf_
    elif hasattr(self,"CriticalValue") and (len(self.CriticalValue)>0):
        n = len(self.CriticalValue)
        rv=[None for i in range(0, n)]
        found_anyPosition = False
        for i,c in enumerate(self.CriticalValue):
            if c.Position:
                found_anyPosition = True
                rv[int(c.Position)] = c.valueOf_
            else:
                if not found_anyPosition:
                    rv[i] = c.valueOf_
                else:
                    if rv[i]:
                        raise(Exception("in CriticalValues_as_list, Position ", i, " cannot be filled twice"))
                    else:
                        rv[i] = c.valueOf_
    return rv

setattr(__gWDSModel.CriticalValues,"as_list",__CriticalValues_as_list)

def __CleanLimits_as_list(self):
    rv=[]
    if bHasCleanLimit(self):
        for c in self.CleanLimit:
            rv.append(c.valueOf_)
    elif self.LeftLimit:
        if self.RightLimit:
            rv=[self.LeftLimit.valueOf_,self.RightLimit.valueOf_]
        else:
            rv=[self.LeftLimit.valueOf_,None]
    elif self.RightLimit:
        rv=[None,self.RightLimit.valueOf_]
    return rv

setattr(__gWDSModel.CleanLimits,"as_list",__CleanLimits_as_list)

def __Responses_as_list(self):
    rv=[]
    if hasattr(self,"Response") and (len(self.Response)>0):
        n = len(self.Response)
        rv=[None for i in range(0, n)]
        found_anyPosition = False
        for i,c in enumerate(self.Response):
            if c.Position:
                found_anyPosition = True
                rv[int(c.Position)] = c.valueOf_
            else:
                if not found_anyPosition:
                    rv[i] = c.valueOf_
                else:
                    if rv[i]:
                        raise(Exception("in Responses_as_list, Position ", i, " cannot be filled twice"))
                    else:
                        rv[i] = c.valueOf_
    return rv

setattr(__gWDSModel.Responses,"as_list",__Responses_as_list)

def __Coefficients_as_list(self):
    rv=[]
    if hasattr(self,"v") and (len(self.v)>0):
        n = len(self.v)
        rv=[None for i in range(0, n)]
        found_anyPosition = False
        for i,c in enumerate(self.v):
            if c.Position:
                found_anyPosition = True
                rv[int(c.Position)] = c.valueOf_
            else:
                if not found_anyPosition:
                    rv[i] = c.valueOf_
                else:
                    if rv[i]:
                        raise(Exception("in Coefficients_as_list, Position ", i, " cannot be filled twice"))
                    else:
                        rv[i] = c.valueOf_
    elif hasattr(self,"Coefficient") and (len(self.Coefficient)>0):
        n = len(self.Coefficient)
        rv=[None for i in range(0, n)]
        found_anyPosition = False
        for i,c in enumerate(self.Coefficient):
            if c.Position:
                found_anyPosition = True
                rv[int(c.Position)] = c.valueOf_
            else:
                if not found_anyPosition:
                    rv[i] = c.valueOf_
                else:
                    if rv[i]:
                        raise(Exception("in Coefficients_as_list, Position ", i, " cannot be filled twice"))
                    else:
                        rv[i] = c.valueOf_
    return rv
setattr(__gWDSModel.Coefficients,"as_list",__Coefficients_as_list)
setattr(__gWDSModel.CoefficientSet,"as_list",__Coefficients_as_list)

def __CoefficientSets_as_list(self,Responses):
    rv=__OrderedDict()
    for r in Responses:
        rv[r] = []
    if self.Coefficients and len(self.Coefficients)>0:
        for c in self.Coefficients:
            rv[c.Response]=c.as_list()
    elif self.CoefficientSet and len(self.CoefficientSet)>0:
        for c in self.CoefficientSet:
            rv[c.Response]=c.as_list()
    return list(rv.values())
setattr(__gWDSModel.CoefficientSets,"as_list",__CoefficientSets_as_list)


__ElementsWithPlurals = ['Project'
                        , 'Model'
                        , 'ComponentModel'
                        , 'Response'
                        , 'Variable'
                        , 'Source'
                        , 'Constant'
                        , 'Transformation'
                        , 'CleanLimit'
                        , 'DropIndex'
                        , 'CriticalValue'
                        , 'CriticalWord'
                        , 'Coefficient'
                        ]

__ElementsWithLists = ['Response'
                        , 'CleanLimit'
                        , 'DropIndex'
                        , 'CleanLimit'
                        , 'CriticalValue'
                        , 'CriticalWord'
                        , 'Coefficient'
                        ]

sOuter = '''def bHas(arg,arg2):
    '''

for w in __ElementsWithPlurals:
    s='def bIs' + w + '''(arg):
    return type(arg) is __gWDSModel.'''+w
    print(s)
    eval(compile(s, 'bIs'+w, 'exec'), globals(), globals())
    s='def bHas' + w + '''(arg):
    return hasattr(arg,"'''+w+'") and (arg.'+w+' is not None) and (len(arg.'+w+')>0)'
    sOuter += '''
    if (arg2=="'''+w+'") and (bHas'+w+'(arg)): return True'''
    print(s)
    eval(compile(s, 'bHas'+w, 'exec'), globals(), globals())
    s='def bIs' + w + '''s(arg):
    return type(arg) is __gWDSModel.'''+w+'s'
    print(s)
    eval(compile(s, 'bIs'+w+'s', 'exec'), globals(), globals())
    s='def bHas' + w + '''s(arg):
    return hasattr(arg,"'''+w+'s") and (arg.'+w+'s is not None)'
    print(s)
    eval(compile(s, 'bHas'+w, 'exec'), globals(), globals())
    sOuter += '''
    if (arg2=="'''+w+'s") and (bHas'+w+'s(arg)): return True'''
    s='def mPreProcess' + w + '''(arg):
    if (bHas'''+w+'(arg)) and (not bHas'+w+'s(arg)):'+'''
        arg.'''+w+'s = __gWDSModel.'+w+'s('+w+'=arg.'+w+''')
        arg.'''+w+''' = []
    #elif (not bHas'''+w+'(arg)) and (bHas'+w+'s(arg)):'+'''
        #arg.'''+w+' = arg.'+w+'s.'+w+'''
        '''
    print(s)
    eval(compile(s, 'mPreProcess'+w, 'exec'), globals(), globals())

for w in __ElementsWithLists:
    s='def bHas' + w + '''List(arg):
    return hasattr(arg,"''' + w + 'List") and (arg.'+w+'List is not None)'
    print(s)
    eval(compile(s, 'bHas'+w+'List', 'exec'), globals(), globals())
    sOuter += '''
    if (arg2=="'''+w+'List") and (bHas'+w+'List(arg)): return True'''

eval(compile(sOuter, 'bHas', 'exec'), globals(), globals())

del s
del w
del sOuter


def WDSModel(filename):
    if type(filename) is str:
        rv = __gWDSModel.parse(filename)
    else:
        rv = __gWDSModel.parse(filename.read())
    print(rv)
    mPreProcess(rv)
    print(rv)
    return rv


def mProcessList(self):
    for nm in __ElementsWithLists:
        s = None
        if bHas(self,nm+"List"):
            s=getattr(self,nm+"List").valueOf_
        if s:
            tempv=getattr(__gWDSModel,nm+'s')()
            for i,w in enumerate(s.split(' ')):
                getattr(tempv,'add_'+nm)(getattr(__gWDSModel,nm)(valueOf_=float(w)))
            setattr(self,nm+'s',tempv)
            setattr(self,nm+'List',None)

def mPreProcess(self):
    mProcessList(self)
    if bHasCleanLimit(self) or bHasCleanLimits(self):
        mPreProcessCleanLimit(self)
        for m in self.CleanLimits.CleanLimit:
            mPreProcess(m)

    if bHasVariable(self) or bHasVariables(self):
        mPreProcessVariable(self)
        for v in self.Variables.Variable:
            mPreProcess(v)

    if bHasResponses(self) or bHasResponse(self):
        mPreProcessResponse(self)

    if bHasProject(self) or bHasProjects(self):
        mPreProcessProject(self)
        for p in self.Projects.Project:
            mPreProcess(p)
    
    if bIsProject(self):
        if bHasModel(self) or bHasModels(self):
            mPreProcessModel(self)
            for m in self.Models.Model:
                mPreProcess(m)
        if bHasComponentModel(self) or bHasComponentModels(self):
            mPreProcessComponentModel(self)
            for m in self.ComponentModels.ComponentModel:
                mPreProcess(m)
    elif bIsModel(self) or bIsComponentModel(self):
        if bHasComponentModel(self) or bHasComponentModels(self):
            mPreProcessComponentModel(self)
            for m in self.ComponentModels.ComponentModel:
                mPreProcess(m)
        if bHasVariable(self) or bHasVariables(self):
            mPreProcessVariable(self)
            for v in self.Variables.Variable:
                mPreProcess(v)
    elif bIsVariable(self):
        if bHasCleanLimit(self) or bHasCleanLimits(self):
            mPreProcessCleanLimit(self)
            for m in self.CleanLimits.CleanLimit:
                mPreProcess(m)
        if bHasVariable(self) or bHasVariables(self):
            mPreProcessVariable(self)
            for v in self.Variables.Variable:
                mPreProcess(v)
    elif bIsVariable(self):
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






