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
    DropIndex[s]    (yes, plural would be Indices, but it is only one, Indexs is used internally)
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
WDSModelBase=__gWDSModel
import WDS.Wranglers.gXMLParsers.gWDSModel_literal as __gWDSModel_literal

import numpy as np

import pudb

# a quick expansion of hasattr
def bHasNonEmptyAttr(self, nm):
    if hasattr(self,nm):
        if getattr(self,nm) is None:
            return False
        tmp = getattr(self,nm)
        if type(tmp) in (list, str):
            return (len(tmp)>0)
        else:
            if tmp:
                return True
            else:
                return False
    return False

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

def __CriticalValues_from_list(self,CriticalValues):
    if type(self) is __gWDSModel.Variable:
        self.CriticalValues=[]
        self.CriticalValues = __gWDSModel.CriticalValues(parent_object_=self, gds_collector_=self.gds_collector_)
        self.CriticalValues.CriticalValues_from_list(CriticalValues)
    else:
        if type(CriticalValues) not in (list, tuple):
            CriticalValues = [CriticalValues]
        ncrits = len(CriticalValues)
        self.v = []
        self.CriticalValue = []
        if ncrits > 0:
            tmp = []
            for i, v in enumerate(CriticalValues):
                tmp.append(__gWDSModel.CriticalValue(Position=i, valueOf_=v
                    , gds_collector_=self.gds_collector_, parent_object_=self))
            self.set_CriticalValue(tmp)

setattr(__gWDSModel.Variable,"CriticalValues_from_list",__CriticalValues_from_list)
setattr(__gWDSModel.CriticalValues,"CriticalValues_from_list",__CriticalValues_from_list)

def __CriticalValues_as_list(self):
    rv=[]
    if bHasNonEmptyAttr(self, "v"):
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
    elif bHasNonEmptyAttr(self, "CriticalValue"):
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

def __CriticalValues_as_numpy(self):
    return np.array([self.as_list()], dtype=np.float64)
setattr(__gWDSModel.CriticalValues,"as_numpy",__CriticalValues_as_numpy)

def __Collect_CleanLimits(self):
    if not ( hasattr(self,'CleanLimits') 
            or hasattr(self, 'CleanLimit')
            or hasattr(self, 'LeftLimit')
            or hasattr(self, 'RightLimit')):
        return None
    if type(self) is __gWDSModel.Variable:
        if self.CleanLimits:
            cself=self.CleanLimits
        else:
            self.set_CleanLimits(__gWDSModel.CleanLimits(CleanLimit=self.CleanLimit, LeftLimit=self.LeftLimit, RightLimit=self.RightLimit
                , gds_collector_=self.gds_collector_, parent_object=self))
            cself=self.CleanLimits
            if cself.CleanLimit: 
                for c in cself.CleanLimit: 
                    c.parent_object_=cself
            if cself.LeftLimit: 
                cself.LeftLimit.parent_object_=cself
            if cself.RightLimit: 
                cself.RightLimit.parent_object_=cself
            self.CleanLimit=[]
            self.LeftLimit=None
            self.RightLimit=None
    if type(self) is __gWDSModel.CleanLimits:
        return __Collect_CleanLimits(self.parent_object_)
    return (self, cself)

def __CleanLimits_from_list(self, CleanLimits):
    self2, cself = __Collect_CleanLimits(self)
    if self2 is not self:
        raise(Exception("huh"))
    if type(CleanLimits) not in (list, tuple):
        CleanLimits = [CleanLimits]
    nclms = len(CleanLimits)
    cself.v = []
    cself.CleanLimit = []
    if (nclms == 2) and CleanLimits[0] and CleanLimits[1]:
        tmp = []
        for i, v in enumerate(CleanLimits):
            tmp.append(__gWDSModel.CleanLimit(Position=i, valueOf_=v
                , gds_collector_=cself.gds_collector_, parent_object_=cself))
        cself.set_CleanLimit(tmp)
    elif (nclms == 2):
        if CleanLimits[0]:
            self.set_LeftLimit(__gWDSModel.LeftLimit(valueOf_=CleanLimits[0]
                , gds_collector_=cself.gds_collector_, parent_object=cself))
        else:
            self.set_RightLimit(__gWDSModel.LeftLimit(valueOf_=CleanLimits[1]
                , gds_collector_=cself.gds_collector_, parent_object=cself))
    else:
        print("Note: setting clean limits with only one designation, sets the LeftLimit")
        self.set_LeftLimit(__gWDSModel.LeftLimit(valueOf_=CleanLimits[0]
                , gds_collector_=cself.gds_collector_, parent_object=cself))

setattr(__gWDSModel.CleanLimits,"from_list",__CleanLimits_from_list)
setattr(__gWDSModel.Variable,"CleanLimits_from_list",__CleanLimits_from_list)

def __CleanLimits_from(self,CleanLimits=None, LeftLimit=None, RightLimit=None):
    if CleanLimits:
        self.from_list(CleanLimits)
    elif LeftLimit:
        self.set_LeftLimit(__gWDSModel.LeftLimit(valueOf_=LeftLimit
                , gds_collector_=self.gds_collector_, parent_object_=self))
    elif RightLimit:
        self.set_LeftLimit(__gWDSModel.RightLimit(valueOf_=RightLimit
                , gds_collector_=self.gds_collector_, parent_object_=self))

setattr(__gWDSModel.CleanLimits,"from",__CleanLimits_from_list)

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

def __CleanLimits_as_numpy(self):
    return np.array([self.as_list()], dtype=np.float64)
setattr(__gWDSModel.CleanLimits,"as_numpy",__CleanLimits_as_numpy)


def __Responses_from(self, Responses):
    if type(self) in (__gWDSModel.Model, __gWDSModel.ComponentModel):
        if self.ModelDirectives is None:
            self.ModelDirectives = __gWDSModel.ModelDirectives(parent_object_=self, gds_collector_=self.gds_collector_)
        self.ModelDirectives.Responses_from(Responses)
    elif type(self) is __gWDSModel.ModelDirectives:
        if self.Responses is None:
            self.Responses = __gWDSModel.Responses(parent_object_=self, gds_collector_=self.gds_collector_)
        self.Responses.Responses_from(Responses)
    elif type(self) is __gWDSModel.Responses:
        self.Response = []
        if type(Responses) not in (list, tuple):
            Response = [Response]
        for i, w in enumerate(Responses):
            self.add_Response(__gWDSModel.Response(Position=i, valueOf_=w
                , gds_collector_=self.gds_collector_, parent_object_=self))

setattr(__gWDSModel.Responses,"Responses_from",__Responses_from)
setattr(__gWDSModel.ModelDirectives,"Responses_from",__Responses_from)
setattr(__gWDSModel.Model,"Responses_from",__Responses_from)
setattr(__gWDSModel.ComponentModel,"Responses_from",__Responses_from)


def __Find_Responses(self):
    if bHasNonEmptyAttr(self, "ModelDirectives"):
        if bHasNonEmptyAttr(self.ModelDirectives, "Responses"):
            return self.ModelDirectives.Responses
        elif bHasNonEmptyAttr(self.ModelDirectives, "Response"):
            mProcessElementWithList(self.ModelDirectives, "Response")
            return self.ModelDirectives.Responses
        else:
            #keep going
            return __Find_Responses(self.parent_object_)
    if self.parent_object_ is None:
        return None
    return __Find_Responses(self.parent_object_)

setattr(__gWDSModel.Variable,"mFindResponses",__Find_Responses)


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

def __CoefficientsSet_from(self, Coefficients, Responses_as_list=None):
    if not Responses_as_list:
        try:
            # path down is:
            #   Models/Model/ComponentModels/ComponentModel/Variables/Variable
            # or
            #   Models/Model/Variables/Variable
            # Responses are at the closest Model or ComponentModel level
            #
            # trying ..(Variable)/..(Variables)/..(Model)/ModelDirectives/Responses
                          #x.parent_object_.parent_object_.parent_object_.parent_object_.ModelDirectives.Responses.as_list()
            Responses_as_list = self.mFindResponses().as_list()
        except Exception as e:
            raise(Exception('cannot call mFindResponses.as_list() in Coefficents.from, ' + str(e)))
    if type(Responses_as_list) not in (list, tuple):
        Responses_as_list = [Responses_as_list]
    nresp = len(Responses_as_list)    
    if nresp != len(Coefficients):
        raise(Exception('in Coefficients.from, len(Coefficients) != len(Responses_as_list), Coef='+str(Coefficients)+', Resp='+str(Responses_as_list)))

    #pudb.set_trace()

    cset = None
    if bHasNonEmptyAttr(self,"CoefficientList"):
        mProcessElementWithList(self, "Coefficient")
        self.CoefficientsList = []

    if bHasNonEmptyAttr(self,"CoefficientsSet"):
        cset = self.CoefficientsSet
        if bHasNonEmptyAttr(cset,"CoefficientList"):
            mProcessElementWithList(cset, "Coefficient")
        if bHasNonEmptyAttr(self.CoefficientsSet,"Coefficients"):
            if bHasNonEmptyAttr(self,"Coefficients"):
                for i, c in enumerate(self.Coefficients):
                    for j, c2 in enumerate(cset.Coefficients):
                        if c.Response == c2.Response:
                            raise(Exception("Response ",c.Response," has Coefficients at both the Variable and Variable.CoefficientsSet levels"))
                    c.parent_object_ = cset
                    self.CoefficientsSet.add_Coefficients(c)
                self.Coefficients = []
    
    if cset is None:
        self.set_CoefficientsSet(__gWDSModel.CoefficientsSet(gds_collector_=self.gds_collector_, parent_object_=self))
        cset = self.CoefficientsSet
        if bHasNonEmptyAttr(self,"Coefficients"):
            for i, c in enumerate(self.Coefficients):
                c.parent_object_ = cset
                cset.add_Coefficients(c)
            self.Coefficients = []
    
    for i, r in enumerate(Responses_as_list):
        found = False
        if bHasNonEmptyAttr(cset,"Coefficients"):
            for j, c in enumerate(cset.Coefficients):
                if c.Response==r:
                    found = True
                    break
        tmp = __gWDSModel.Coefficients(Response=r
            , gds_collector_=cset.gds_collector_, parent_object_=cset)
        for k, v in enumerate(Coefficients[i]):
            tmp.add_Coefficient(__gWDSModel.Coefficient(Position=k, valueOf_=v
            , gds_collector_=cset.gds_collector_, parent_object_=tmp))
        if found:
           cset.replace_Coefficients_at(j,tmp)
        else:
            cset.add_Coefficients(tmp)

setattr(__gWDSModel.Variable,"CoefficientsSet_from",__CoefficientsSet_from)

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

def __CoefficientsSet_as_list(self,Responses=None):
    if type(self) is __gWDSModel.Variable:
        return self.CoefficientsSet.as_list(Responses)
    if Responses is None:
        Responses = self.parent_object_.mFindResponses().as_list()
    if type(Responses) is str:
        Responses = [Responses, ]
    rv=__OrderedDict()
    for r in Responses:
        rv[r] = []
    if self.Coefficients and len(self.Coefficients)>0:
        for c in self.Coefficients:
            rv[c.Response]=c.as_list()
    elif self.CoefficientsSet and len(self.CoefficientsSet.Coefficients)>0:
        for c in self.CoefficientsSet.Coefficients:
            rv[c.Response]=c.as_list()
    return list(rv.values())
setattr(__gWDSModel.CoefficientsSet,"as_list",__CoefficientsSet_as_list)
setattr(__gWDSModel.Variable,"Coefficients_as_list",__CoefficientsSet_as_list)

def __CoefficientsSet_as_numpy(self, Responses=None):
    if type(self) is __gWDSModel.Variable:
        return self.CoefficientsSet.as_numpy(Responses)
    return np.array(self.as_list(Responses), dtype=np.float64)
setattr(__gWDSModel.CoefficientsSet,"as_numpy",__CoefficientsSet_as_numpy)
setattr(__gWDSModel.Variable,"Coefficients_as_numpy",__CoefficientsSet_as_numpy)

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
    #print(s)
    eval(compile(s, 'bIs'+w, 'exec'), globals(), globals())
    s='def bHas' + w + '''(arg):
    return hasattr(arg,"'''+w+'") and (arg.'+w+' is not None) and (len(arg.'+w+')>0)'
    sOuter += '''
    if (arg2=="'''+w+'") and (bHas'+w+'(arg)): return True'''
    #print(s)
    eval(compile(s, 'bHas'+w, 'exec'), globals(), globals())
    s='def bIs' + w + '''s(arg):
    return type(arg) is __gWDSModel.'''+w+'s'
    #print(s)
    eval(compile(s, 'bIs'+w+'s', 'exec'), globals(), globals())
    s='def bHas' + w + '''s(arg):
    return hasattr(arg,"'''+w+'s") and (arg.'+w+'s is not None)'
    #print(s)
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
    #print(s)
    eval(compile(s, 'mPreProcess'+w, 'exec'), globals(), globals())

for w in __ElementsWithLists:
    s='def bHas' + w + '''List(arg):
    return hasattr(arg,"''' + w + 'List") and (arg.'+w+'List is not None)'
    #print(s)
    eval(compile(s, 'bHas'+w+'List', 'exec'), globals(), globals())
    sOuter += '''
    if (arg2=="'''+w+'List") and (bHas'+w+'List(arg)): return True'''

eval(compile(sOuter, 'bHas', 'exec'), globals(), globals())

del s
del w
del sOuter

def WDSModel(Name=None, Responses=None):
    rv = __gWDSModel.Model(Name=Name, Handle=Name)
    rv.set_ModelDirectives(__gWDSModel.ModelDirectives(parent_object_=rv, gds_collector_=rv.gds_collector_))
    if Responses:
        rv.Responses_from(Responses)
    return rv

def add_Variable(Model=None, Name=None, Treatment=None, CriticalValues=None, CleanLimits=None, Coefficients=None):
    rv = __gWDSModel.Variable(Name=Name, Handle=Name, Treatment=Treatment, parent_object_=Model, gds_collector_=Model.gds_collector_)
    if Model.Variables is None:
        Model.Variables = __gWDSModel.Variables(parent_object_=Model, gds_collector_=Model.gds_collector_)
    Model.Variables.add_Variable(rv)
    rv.add_Source(__gWDSModel.Source(valueOf_=Name, parent_object_=rv, gds_collector_=Model.gds_collector_))
    rv.CriticalValues_from_list(CriticalValues)
    if CleanLimits:
        rv.CleanLimits_from_list(CleanLimits)
    if Coefficients:
        rv.CoefficientsSet_from(Coefficients)
    rv.VariableModelDirectives = __gWDSModel.VariableModelDirectiveType(parent_object_=rv, gds_collector_=Model.gds_collector_)
    return rv

def __add_Variable(self, Name=None, Treatment=None, CriticalValues=None, CleanLimits=None, Coefficients=None):
    return add_Variable(Model=self, Name=None, Treatment=None, CriticalValues=None, CleanLimits=None, Coefficients=None)

setattr(__gWDSModel.Model,"add_Variable",__add_Variable)

def __get_Variable(self, Name=None):
    if Name is not None:
        if bHasVariable(self) or bHasVariables(self):
            mPreProcessVariable(self)
        for vrbl in self.Variables.Variable:
            if vrbl.Name == Name:
                return vrbl
        return None
    else:
        return None
    
setattr(__gWDSModel.Model,"get_Variable",__get_Variable)


def __add_DropIndex(self, indx):
    mProcessList(self, just_DropIndexs=True)
    if self.DropIndexs is None:
        self.DropIndexs = __gWDSModel.DropIndexs(parent_object_=self)
    mProcessList(self, just_DropIndexs=True)
    self.DropIndexs.add_DropIndex(__gWDSModel.Int(indx, parent_object_=self.DropIndexs))

setattr(__gWDSModel.Variable,"add_DropIndex",__add_DropIndex)

def WDSModelFromFile(filename):
    if type(filename) is str:
        rv = __gWDSModel.parse(filename)
    else:
        rv = __gWDSModel.parse(filename.read())
    #print(rv)
    mPreProcess(rv)
    #print(rv)
    return rv

def mProcessElementWithList(self, nm):
    s = None
    if bHas(self,nm+"List"):
        tmp=getattr(self,nm+"List")
        if type(tmp) is list:
            return None
        s=getattr(tmp,'valueOf_')
    else:
        return None
    if s:
        if bHas(self, nm+"s"):
            tmp = getattr(self, nm+s)
            if len(getattr(tmp, nm)) > 0:
                raise(Exception('element '+nm+'s has '+nm+' values but parent element was also given a '+nm+'List '+s))
        tempv=getattr(__gWDSModel,nm+'s')(gds_collector_=self.gds_collector_, parent_object_=self)
        if hasattr(getattr(self,nm+"List"),"Response"):
            tempv.Response = getattr(getattr(self,nm+"List"),"Response")
        for i,w in enumerate(s.split(' ')):
            getattr(tempv,'add_'+nm)(getattr(__gWDSModel,nm)(valueOf_=float(w)
                , gds_collector_=tempv.gds_collector_, parent_object_=tempv))
        setattr(self,nm+'s',tempv)
    setattr(self,nm+'List',None)


def mProcessList(self, just_DropIndexs=False):
    '''Takes care of any unusual DropIndexs, DropIndices, or DropIndexes and then processes List-valued elements'''
    if bHas(self,"DropIndex") or bHas(self,"DropIndices") or bHas(self,"DropIndexs") or bHas(self,"DropIndexes"):
        if bHas(self,"DropIndices") or bHas(self,"DropIndexs") or bHas(self,"DropIndexes"):
            if self.DropIndexs and len(self.DropIndexs.DropIndex)>0:
                if self.DropIndices and len(self.DropIndices.DropIndex)>0:
                    raise(Exception('error in mProcessList, DropIndices and DropIndexs cannot both be used, internal is DropIndexs'))
                self.DropIndices = None
                if self.DropIndexes and len(self.DropIndexes.DropIndex)>0:
                    raise(Exception('error in mProcessList, DropIndexes and DropIndexs cannot both be used, internal is DropIndexs'))
                self.DropIndexes = None
            elif self.DropIndices and len(self.DropIndices.DropIndex)>0:
                if self.DropIndexes and len(self.DropIndexes.DropIndex)>0:
                    raise(Exception('error in mProcessList, DropIndices and DropIndexs cannot both be used, internal is DropIndexs'))
                self.DropIndexes = None
                self.DropIndexs = self.DropIndices
                self.DropIndices = None
            elif self.DropIndexes and len(self.DropIndexes.DropIndex)>0:
                if self.DropIndices and len(self.DropIndices.DropIndices)>0:
                    raise(Exception('error in mProcessList, DropIndices and DropIndexs cannot both be used, internal is DropIndexs'))
                self.DropIndexs = self.DropIndexes
                self.DropIndexes = None
                self.DropIndices = None
        if bHasDropIndex(self) or bHasDropIndexs(self):
            mPreProcessDropIndex(self)
    if not just_DropIndexs:
        for nm in __ElementsWithLists:
            mProcessElementWithList(self, nm)

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






