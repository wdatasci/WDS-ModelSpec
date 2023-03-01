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

import copy

import polars as pl
import pandas as pd

import WDS.Comp.Artificials_CythonWrapped as art_c

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
setattr(__gWDSModel.CriticalValues,"np",__CriticalValues_as_numpy)

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
    if (nclms == 2) and (CleanLimits[0] is not None) and (CleanLimits[1] is not None):
        tmp = []
        for i, v in enumerate(CleanLimits):
            tmp.append(__gWDSModel.CleanLimit(Position=i, valueOf_=v
                , gds_collector_=cself.gds_collector_, parent_object_=cself))
        cself.set_CleanLimit(tmp)
    elif (nclms == 2):
        if CleanLimits[0] is not None:
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
setattr(__gWDSModel.CleanLimits,"np",__CleanLimits_as_numpy)


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
    if Responses_as_list in (None,'',[]):
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
setattr(__gWDSModel.CoefficientsSet,"np",__CoefficientsSet_as_numpy)
setattr(__gWDSModel.Variable,"Coefficients_as_numpy",__CoefficientsSet_as_numpy)
setattr(__gWDSModel.Variable,"Coefficients_np",__CoefficientsSet_as_numpy)

__ElementsWithSets = ['Coefficients'
                        ,
                        ]

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

for w in __ElementsWithSets:
    s='def bHas' + w + '''Set(arg):
    return hasattr(arg,"''' + w + 'Set") and (arg.'+w+'Set is not None)'
    #print(s)
    eval(compile(s, 'bHas'+w+'Set', 'exec'), globals(), globals())
    sOuter += '''
    if (arg2=="'''+w+'Set") and (bHas'+w+'Set(arg)): return True'''

sOuter += '''
    return False'''
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

def __add_new_ComponentModel(Model=None, Name=None, Responses=None):
    rv = __gWDSModel.ComponentModel(Name=Name, Handle=Name)
    Model.add_ComponentModel(rv)
    if Responses:
        rv.Responses_from(Responses)
    else:
        Responses = Model.ModelDirectives.Responses.as_list()
        if Responses:
            rv.Responses_from(Responses)
    return rv


setattr(__gWDSModel.Model,"add_new_ComponentModel",__add_new_ComponentModel)

def add_Variable(Model=None, Name=None, Treatment=None, CriticalValues=None, CleanLimits=None, Coefficients=None
        , DropIndexs=None
        , Source=None
        , ResponseUse=None
        , SegmentedBy=None
        , Static=None
        , ProcessFirst=None
        ):
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
    rv.DropIndexs_from_list(DropIndexs)
    if Source and type(Source) is str:
        rv.Source[0].valueOf_ = Source
    rv.VariableModelDirectives = __gWDSModel.VariableModelDirectiveType(parent_object_=rv, gds_collector_=Model.gds_collector_)
    rv.VariableModelDirectives.ResponseUse = ResponseUse
    if ResponseUse == 'SegmentationOnly':
        rv.VariableModelDirectives.set_SpecialUse('SegmentationOnly')
    if SegmentedBy:
        rv.SegmentedBy=SegmentedBy
    if Static:
        if type(Static) is bool:
            rv.VariableModelDirectives.Static = 'Yes' if Static else 'No'
        else:
            rv.VariableModelDirectives.Static = Static
    if ProcessFirst:
        if type(ProcessFirst) is bool:
            rv.VariableModelDirectives.set_ProcessFirst('Yes' if ProcessFirst else 'No')
        else:
            rv.VariableModelDirectives.set_ProcessFirst(ProcessFirst)
    return rv

def __add_Variable(self, **args): #Name=None, Treatment=None, CriticalValues=None, CleanLimits=None, Coefficients=None
    return add_Variable(Model=self, **args) #Name=None, Treatment=None, CriticalValues=None, CleanLimits=None, Coefficients=None

setattr(__gWDSModel.Model,"add_Variable",__add_Variable)
setattr(__gWDSModel.ComponentModel,"add_Variable",__add_Variable)

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
setattr(__gWDSModel.ComponentModel,"get_Variable",__get_Variable)

def __add_DropIndex(self, indx):
    __DropIndexs_fix(self)
    if type(indx) in (int, float, str):
        indx = int(indx)
        found = False
        for v0 in self.DropIndexs.DropIndex:
            if v0.valueOf_ == indx:
                break
        if not found:
            self.DropIndexs.DropIndex.append(__gWDSModel.Int(indx, parent_object_=self.DropIndexs))
    elif type(indx) is list:
        for v in indx:
            __add_DropIndex(self, v)
    elif type(indx) is __gWDSModel.DropIndex:
            __add_DropIndex(self, indx.valueOf_)
    else:
        raise(Exception("Cannot add type, "+str(type(indx))+", to DropIndexs"))


setattr(__gWDSModel.Variable,"add_DropIndex",__add_DropIndex)


def __DropIndexs_fix(self):
    other = None
    if bHas(self,"DropIndex") or bHas(self,"DropIndices") or bHas(self,"DropIndexs") or bHas(self,"DropIndexes"):
        if self.DropIndexs and len(self.DropIndexs.DropIndex)>0:
            if self.DropIndices and len(self.DropIndices.DropIndex)>0:
                raise(Exception('error in mProcessList, DropIndices and DropIndexs cannot both be used, internal is DropIndexs'))
            self.DropIndices = None
            if self.DropIndexes and len(self.DropIndexes.DropIndex)>0:
                raise(Exception('error in mProcessList, DropIndexes and DropIndexs cannot both be used, internal is DropIndexs'))
            self.DropIndexes = None
        else:
            if bHas(self,'DropIndices') and len(self.DropIndices.DropIndex)>0:
                if self.DropIndexes and len(self.DropIndexes.DropIndex)>0:
                    raise(Exception('error in mProcessList, DropIndices and DropIndexs cannot both be used, internal is DropIndexs'))
                self.DropIndexes = None
                other = self.DropIndices
            if bHas(self,'DropIndexes') and len(self.DropIndexes.DropIndex)>0:
                other = self.DropIndices
    if bHas(self,"DropIndexs") == False or self.DropIndexs is None:
        if other:
            self.DropIndexs = __gWDSModel.DropIndexs(DropIndex=other.DropIndex
                    , parent_object_=self, gds_collector_=self.gds_collector_)
            if self.DropIndexs.DropIndex !=[]:
                for v in self.DropIndexs.DropIndex:
                    v.parent_object_ = self.DropIndexs
            if type(other) is __gWDSModel.DropIndices:
                __gWDSModel.DropIndices = None
            elif type(other) is __gWDSModel.DropIndexes:
                __gWDSModel.DropIndexes = None
            other = None
        else:
            self.DropIndexs = __gWDSModel.DropIndexs(parent_object_=self, gds_collector_=self.gds_collector_)
    if bHas(self,"DropIndex") and self.DropIndex != []:
        for v in self.DropIndex:
            self.DropIndexs.add_DropIndex(v.valueOf_)
        self.DropIndex = []
        

def __DropIndexs_as_list(self):
    rv=[]
    if self.DropIndex is not []:
        for c in self.DropIndex:
            rv.append(c.valueOf_)
    return rv

setattr(__gWDSModel.DropIndexs,"as_list",__DropIndexs_as_list)

def __DropIndexs_from_list(self,DropIndexs):
    if DropIndexs is None:
        return
    if type(DropIndexs) in (list,tuple):
        if type(DropIndexs[0]) in (list,tuple):
            DropIndexs = DropIndexs[0]
    if type(DropIndexs) not in (list, tuple):
        DropIndexs = [int(DropIndexs)]
    if len(DropIndexs) is None:
        return
    for di in DropIndexs:
        self.add_DropIndex(di)

setattr(__gWDSModel.Variable,"DropIndexs_from_list",__DropIndexs_from_list)




def WDSModelFromFile(filename):
    if type(filename) is str:
        rv = __gWDSModel.parse(filename)
    else:
        rv = __gWDSModel.parse(filename.read())
    print(rv)
    print()
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
    __DropIndexs_fix(self)
    if not just_DropIndexs:
        for nm in __ElementsWithLists:
            mProcessElementWithList(self, nm)

def mPreProcess(self):
    mProcessList(self)

    if bHasCriticalValue(self) or bHasCriticalValues(self):
        mPreProcessCriticalValue(self)
        for m in self.CriticalValues.CriticalValue:
            mPreProcess(m)

    if bHasCleanLimit(self) or bHasCleanLimits(self):
        mPreProcessCleanLimit(self)
        for m in self.CleanLimits.CleanLimit:
            mPreProcess(m)

    if bHasVariable(self) or bHasVariables(self):
        mPreProcessVariable(self)
        for v in self.Variables.Variable:
            mPreProcess(v)

    if (bHasResponses(self) or bHasResponse(self)) and not (bIsCoefficients(self)):
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
            #for m in self.CleanLimits.CleanLimit:
                #mPreProcess(m)
        if bHasCriticalValue(self) or bHasCriticalValues(self):
            mPreProcessCriticalValue(self)
            #for v in self.CriticalValues.CriticalValue:
                #mPreProcess(v)
        if bHas(self,'CoefficientsSet'):
            for cs in self.CoefficientsSet.Coefficients:
                mPreProcess(cs)
    elif bIsCoefficients(self):
        for c in self.Coefficient:
            mPreProcess(c)
    elif bIsCleanLimit(self) or bIsCriticalValue(self) or bIsCoefficient(self):
        if type(self.valueOf_) is str:
            if len(self.valueOf_) == 0:
                if bIsCoefficient(self):
                    self.valueOf_ = 0.0
                else:
                    self.valueOf_=None
            else:
                try:
                    v=eval(self.valueOf_)
                    self.valueOf_=v
                except:
                    pass
    else:
        pass
       
def plDF(arg):
    return pl.DataFrame(arg.view(dtype=np.float64),columns=arg.dtype.fields)


def fArtificials(arg, VariableSpec):
    return plDF(art_c.fArtificials(arg,VariableSpec.Treatment,VariableSpec.CriticalValues.as_numpy(),VariableSpec.CleanLimits.as_numpy(),LabelBase=VariableSpec.Name))

def fArtificialsScored(arg, VariableSpec):
    return plDF(art_c.fArtificialsScored(arg,VariableSpec.Treatment,VariableSpec.CriticalValues.as_numpy(),VariableSpec.CleanLimits.as_numpy(),VariableSpec.CoefficientsSet.as_numpy(),LabelBase=VariableSpec.Name))

def ModelBuildingMD_Constructor():
    class _ModelBuildingMD(object):
        def __init__(self, mdl):
            self._mdl = mdl
            self.Resp_arts_names = {}
            self.Resp_arts_droplist ={}
            for r in mdl.ModelDirectives.Responses.as_list():
                self.Resp_arts_names[r]=[]
                self.Resp_arts_droplist[r]=[]
        def add_arts(self, vrbl, cols):
            if vrbl.VariableModelDirectives.ResponseUse=='All':
                for r in self._mdl.ModelDirectives.Responses.as_list():
                    self.Resp_arts_names[r].extend(cols)
                    if vrbl.DropIndexs.DropIndex != []:
                        self.Resp_arts_droplist[r].extend([cols[i] for i in vrbl.DropIndexs.as_list()])
            else:
                r = vrbl.VariableModelDirectives.ResponseUse
                self.Resp_arts_names[r].extend(cols)
                if vrbl.DropIndexs.DropIndex != []:
                    self.Resp_arts_droplist[r].extend([cols[i] for i in vrbl.DropIndexs.as_list()])
        def effective_names(self, r):
            return [x for x in filter(lambda x: not (x in self.Resp_arts_droplist[r]), self.Resp_arts_names[r])]

    return _ModelBuildingMD

def fAddToSystem(variable, arg, system_matrix_Resp1, system_matrix_Resp2):
    if variable.get_VariableModelDirectives().ResponseUse == "All":
        if system_matrix_Resp1 is not None and not system_matrix_Resp1.is_empty():
            system_matrix_Resp1.hstack(arg, in_place=True)
        else:
            system_matrix_Resp1 = arg
        if system_matrix_Resp2 is not None and not system_matrix_Resp2.is_empty():
            system_matrix_Resp2.hstack(arg, in_place=True)
        else:
            system_matrix_Resp2 = copy.copy(arg)
    elif variable.get_VariableModelDirectives().ResponseUse == "Resp1":
        if system_matrix_Resp1 is not None and not system_matrix_Resp1.is_empty():
            system_matrix_Resp1.hstack(arg, in_place=True)
        else:
            system_matrix_Resp1 = arg
    elif variable.get_VariableModelDirectives().ResponseUse == "Resp2":
        if system_matrix_Resp2 is not None and not system_matrix_Resp2.is_empty():
            system_matrix_Resp2.hstack(arg, in_place=True)
        else:
            system_matrix_Resp2 = arg
    return [system_matrix_Resp1, system_matrix_Resp2]

def fModelPrep(data, modelspec, to_score=False, score_basename='Score' ):
    rv={}
    rv['woSuffix']={}
    resplist = modelspec.ModelDirectives.Responses.as_list()
    if to_score:
        rv[score_basename]=0.0
    for resp in resplist:
        rv[resp]={}
        if to_score:
            rv[resp+'_'+score_basename]={}
            rv[resp+'_'+score_basename][score_basename]=0.0
    
    if type(data) is pd.DataFrame:
        #first past to gather ProcessFirst variables that are used for segmentation purposes only
        for v in modelspec.Variables.Variable:
            if v.VariableModelDirectives.ProcessFirst=='Yes' and v.VariableModelDirectives.SpecialUse=='SegmentationOnly':
                if v.Treatment in('Categorical','NCategorical'):
                    rv['woSuffix'][v.Name]=pd.DataFrame(art_c.fArtificials(data[v.Source[0].valueOf_].to_numpy()
                        ,v.Treatment
                        ,CriticalValues=v.CriticalValues.as_list()
                        ,LabelBase=v.Name).flatten())
                else:
                    rv['woSuffix'][v.Name]=pd.DataFrame(art_c.fArtificials(data[v.Source[0].valueOf_].to_numpy()
                        ,v.Treatment
                        ,CriticalValues=v.CriticalValues
                        ,CleanLimits=v.CleanLimits
                        ,LabelBase=v.Name).flatten())

        #second pass is to gather the rest of the process first variables that may depend on segmentation variables
        for v in modelspec.Variables.Variable:
            if v in rv['woSuffix']:
                continue
            elif v.VariableModelDirectives.ProcessFirst=='Yes':
                if v.Treatment in('Categorical','NCategorical'):
                    rv['woSuffix'][v.Name]=pd.DataFrame(art_c.fArtificials(data[v.Source[0].valueOf_].to_numpy()
                        ,v.Treatment
                        ,CriticalValues=v.CriticalValues.as_list()
                        ,LabelBase=v.Name).flatten())
                else:
                    rv['woSuffix'][v.Name]=pd.DataFrame(art_c.fArtificials(data[v.Source[0].valueOf_].to_numpy()
                        ,v.Treatment
                        ,CriticalValues=v.CriticalValues
                        ,CleanLimits=v.CleanLimits
                        ,LabelBase=v.Name).flatten())

            else:
                continue

        #process drops for early processed variables
        if to_score == False:  # for now, hold drops, later, valid unsegmented by flag will be passed into fArtificialsScored
            for v in modelspec.Variables.Variable:
                if v in rv['woSuffix']:
                    if v.DropIndexs:
                        drops=v.DropIndexs.as_list()
                        drops.sort(reverse=True)
                        for i in drops:
                            rv['woSuffix'][v.Name].drop(rv['woSuffix'][v.Name].columns[i],axis=1,inplace=True)

        #process segmentation variables for early processed variables
        for v in modelspec.Variables.Variable:
            if v in rv['woSuffix']:
                if v.Name in rv['woSuffix'] and v.SegmentedBy:
                    for i in range(rv['woSuffix'][v.Name].shape[1]):
                        rv['woSuffix'][v.Name].iloc[:,i]=rv['woSuffix'][v.Name].iloc[:,i]*rv['woSuffix'][v.SegmentedBy.Name].iloc[:,1]

        #segmentation only variables are not used in modeling, but for the others>>>
        #add suffixes as needed to track model and static use:
        for v in modelspec.Variables.Variable:
            if v.Name in rv['woSuffix']:
                if v.VariableModelDirectives.ResponseUse == 'All' or v.VariableModelDirectives.ResponseUse in modelspec.ModelDirectives.Responses.as_list():
                    Static_Suffix = '_Static' if (v.VariableModelDirectives.Static == 'Yes') else ''
                    if v.VariableModelDirectives.ResponseUse == 'All':
                        respset = modelspec.ModelDirectives.Responses.as_list()
                    else:
                        respset = [v.VariableModelDirectives.ResponseUse]
                    for resp in respset:
                        tmp = rv['woSuffix'][v.Name]
                        if to_score:
                            ri = resplist.index(resp)
                            coefs = v.CoefficientsSet.as_list()[ri]
                            rv[resp+'_'+score_basename][v.Name+Static_Suffix+'_'+resp] = tmp @ coefs
                            rv[resp+'_'+score_basename][score_basename] = rv[resp+'_'+score_basename][score_basename]+rv[resp+'_'+score_basename][v.Name+Static_Suffix+'_'+resp]
                            rv[score_basename] = rv[score_basename]+rv[resp+'_'+score_basename][v.Name+Static_Suffix+'_'+resp]
                        tmpc = tmp.columns
                        tmprn = {}
                        for c in tmpc:
                            tmprn[c]=c+Static_Suffix+'_'+resp
                        rv[resp][v.Name+'_'+resp] = tmp.rename(columns=tmprn)


        #now process remaining
        for v in modelspec.Variables.Variable:
            print('Processing ',v.Name)
            if v.Name in rv['woSuffix']:
                pass
            else:
                if v.Treatment in('Categorical','NCategorical'):
                    rv['woSuffix'][v.Name]=pd.DataFrame(art_c.fArtificials(data[v.Source[0].valueOf_].to_numpy()
                        ,v.Treatment
                        ,CriticalValues=v.CriticalValues.as_list()
                        ,LabelBase=v.Name).flatten())
                else:
                    rv['woSuffix'][v.Name]=pd.DataFrame(art_c.fArtificials(data[v.Source[0].valueOf_].to_numpy()
                        ,v.Treatment
                        ,CriticalValues=v.CriticalValues
                        ,CleanLimits=v.CleanLimits
                        ,LabelBase=v.Name).flatten())
        
                if to_score == False:
                    if v.DropIndexs:
                        drops=v.DropIndexs.as_list()
                        drops.sort(reverse=True)
                        for i in drops:
                            rv['woSuffix'][v.Name].drop(rv['woSuffix'][v.Name].columns[i],axis=1,inplace=True)
        
                if v.SegmentedBy:
                    for i in range(rv['woSuffix'][v.Name].shape[1]):
                        rv['woSuffix'][v.Name].iloc[:,i]=rv['woSuffix'][v.Name].iloc[:,i]*rv['woSuffix'][v.SegmentedBy.Name].iloc[:,1]

                if v.VariableModelDirectives.ResponseUse == 'All' or v.VariableModelDirectives.ResponseUse in modelspec.ModelDirectives.Responses.as_list():
                    Static_Suffix = '_Static' if (v.VariableModelDirectives.Static == 'Yes') else ''
                    if v.VariableModelDirectives.ResponseUse == 'All':
                        respset = modelspec.ModelDirectives.Responses.as_list()
                    else:
                        respset = [v.VariableModelDirectives.ResponseUse]
                    for resp in respset:
                        tmp = rv['woSuffix'][v.Name]
                        if to_score:
                            ri = resplist.index(resp)
                            coefs = v.CoefficientsSet.as_list()[ri]
                            rv[resp+'_'+score_basename][v.Name+Static_Suffix+'_'+resp] = tmp @ coefs
                            rv[resp+'_'+score_basename][score_basename] = rv[resp+'_'+score_basename][score_basename]+rv[resp+'_'+score_basename][v.Name+Static_Suffix+'_'+resp]
                            rv[score_basename] = rv[score_basename]+rv[resp+'_'+score_basename][v.Name+Static_Suffix+'_'+resp]
                        tmpc = tmp.columns
                        tmprn = {}
                        for c in tmpc:
                            tmprn[c]=c+Static_Suffix+'_'+resp
                        rv[resp][v.Name+'_'+resp] = tmp.rename(columns=tmprn)


    return rv

def fVariable2SQL(v,to_score=True):
    sql = ''
    artlist=[]
    if v.Treatment in('Categorical','NCategorical'):

        sql = sql + '\n        , if( not ( false '
        for cvi,cv in enumerate(v.CriticalValues.as_list()):
            sql = sql + '\n              or ' + v.Source[0].valueOf_ + ' in ' + str(tuple(cv)).replace(',)',')')
        sql = sql + '\n            ),1,0)'
        if v.SegmentedBy:
            sql = sql + ' * ' + v.SegmentedBy.Name + '_1'
        sql = sql + '\n          as ' + v.Name+'_'+'0'
        artlist.append(v.Name+'_'+'0')

        for cvi,cv in enumerate(v.CriticalValues.as_list()):
            sql = sql + '\n        , if(' + v.Source[0].valueOf_ 
            sql = sql + ' in ' + str(tuple(cv)).replace(',)',')')
            sql = sql + '\n            ,1,0)'
            if v.SegmentedBy:
                sql = sql + ' * ' + v.SegmentedBy.Name + '_1'
            sql = sql + '\n          as ' + v.Name+'_'+str(cvi+1)
            artlist.append(v.Name+'_'+str(cvi+1))

    elif v.Treatment == 'CodedMissings':
        CleanLimit = [v.CleanLimits.CleanLimit[0].valueOf_, v.CleanLimits.CleanLimit[1].valueOf_]
        cvl = v.CriticalValues.as_list()
        cvln = len(cvl)

        sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is null or ' + v.Source[0].valueOf_ + ' not between (' +
                str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') ,1,0)')
        if v.SegmentedBy:
            sql = sql + '\n            * ' + v.SegmentedBy.Name + '_1'
        sql = sql + '\n       as ' + v.Name+'_'+'0'
        artlist.append(v.Name+'_0')

        sql = sql + ('\n        , if( not (' + v.Source[0].valueOf_ + ' is null or ' + v.Source[0].valueOf_ + ' not between (' +
                str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') ) ,' + v.Source[0].valueOf_ + ',0)')
        if v.SegmentedBy:
            sql = sql + '\n            * ' + v.SegmentedBy.Name + '_1'
        sql = sql + '\n       as ' + v.Name+'_'+'1'
        artlist.append(v.Name+'_1')

    elif v.Treatment == 'DiscreteLC':
        CleanLimit = [v.CleanLimits.CleanLimit[0].valueOf_, v.CleanLimits.CleanLimit[1].valueOf_]
        cvl = v.CriticalValues.as_list()
        cvln = len(cvl)

        sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is null or ' + v.Source[0].valueOf_ + ' not between (' +
                str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') ,1,0)')
        if v.SegmentedBy:
            sql = sql + '\n            * ' + v.SegmentedBy.Name + '_1'
        sql = sql + '\n       as ' + v.Name+'_'+'0'
        artlist.append(v.Name+'_0')

        for cvi in range(0,cvln+1):
            if cvi == 0:
                cv = cvl[cvi]
                sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is not null and ' + v.Source[0].valueOf_ + ' between (' +
                        str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') and  ' + v.Source[0].valueOf_ + ' <= (' +
                        str(cv) + ') ,1,0)')
            elif cvi == cvln:                                      
                sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is not null and (' + v.Source[0].valueOf_ + ') between (' +
                        str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') and ' + v.Source[0].valueOf_ + ' > (' + str(cv)
                        + ') ,1,0)')
            else:                                                  
                cvr = cvl[cvi]                                     
                sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is not null and ' + v.Source[0].valueOf_ + ' between (' +
                        str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') and ' + v.Source[0].valueOf_ + ' > (' + str(cv)
                        + ') and ' +  v.Source[0].valueOf_ + ' <= (' + str(cvr) + ') ,1,0)' )
                cv = cvr
            if v.SegmentedBy:
                sql = sql + '\n            * ' + v.SegmentedBy.Name + '_1'
            sql = sql + '\n           as ' + v.Name+'_'+str(cvi+1)
            artlist.append(v.Name+'_'+str(cvi+1))

    elif v.Treatment == 'Hats':
        
        cvlist = v.CriticalValues.as_list()
        cvln = len(cvlist)
        cvlist.append(cvlist[-1])
        CleanLimit = [v.CleanLimits.CleanLimit[0].valueOf_, v.CleanLimits.CleanLimit[1].valueOf_]

        sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is null or ' + v.Source[0].valueOf_ + ' not between (' +
                str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') ,1,0)')
        if v.SegmentedBy:
            sql = sql + '\n            * ' + v.SegmentedBy.Name + '_1'
        sql = sql + '\n           as ' + v.Name+'_'+'0'
        artlist.append(v.Name+'_0')

        for cvi in range(0,cvln):
            if cvi == 0:
                cv = cvlist[cvi]
                cvr = cvlist[cvi+1]
                sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is not null and ' + v.Source[0].valueOf_ + ' between (' +
                        str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') and  ' + v.Source[0].valueOf_ + ' <= (' +
                        str(cvr) + ')' )
                sql = sql + '\n            ,if(' + v.Source[0].valueOf_ + ' <= (' + str(cv) + ')'
                sql = sql + '\n                ,1'
                sql = sql + '\n                ,( (' + str(cvr) + ') - ' + v.Source[0].valueOf_ + ' ) / ( ' + str( cvr - cv ) + ' ) '
                sql = sql + '\n                )'
                sql = sql + '\n            ,0)'
            elif cvi == cvln-1:                                      
                cvl = cv
                cv = cvr
                sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is not null and ' + v.Source[0].valueOf_ + ' between (' +
                        str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') and ' + v.Source[0].valueOf_ + ' > (' +
                        str(cvl) + ')' )
                sql = sql + '\n            ,if(' + v.Source[0].valueOf_ + ' <= (' + str(cv) + ')'
                sql = sql + '\n                ,( ' + v.Source[0].valueOf_ + ' - (' + str(cvl) + ') ) / ( ' + str( cv - cvl ) + ' ) '
                sql = sql + '\n                ,1'
                sql = sql + '\n                )'
                sql = sql + '\n            ,0)'
            else:                                                  
                cvl = cv
                cv = cvr
                cvr = cvlist[cvi+1]                                     
                sql = sql + ('\n        , if(' + v.Source[0].valueOf_ + ' is not null and ' + v.Source[0].valueOf_ + ' between (' +
                        str(CleanLimit[0]) + ') and (' + str(CleanLimit[1]) + ') and ' + v.Source[0].valueOf_ + ' > (' + str(cvl)
                        + ') and ' +  v.Source[0].valueOf_ + ' <= (' + str(cvr) + ')' )
                sql = sql + '\n            ,if(' + v.Source[0].valueOf_ + ' <= (' + str(cv) + ')'
                sql = sql + '\n                ,( ' + v.Source[0].valueOf_ + ' - (' + str(cvl) + ') ) / ( ' + str( cv - cvl ) + ' ) '
                sql = sql + '\n                ,( (' + str(cvr) + ') - ' + v.Source[0].valueOf_ + ' ) / ( ' + str( cvr - cv ) + ' ) '
                sql = sql + '\n               )'
                sql = sql + '\n            ,0)'
            if v.SegmentedBy:
                sql = sql + '\n            * ' + v.SegmentedBy.Name + '_1'
            sql = sql + '\n           as ' + v.Name+'_'+str(cvi+1)
            artlist.append(v.Name+'_'+str(cvi+1))

    else: #else is not implemented here
        raise(Exception('treatment ' + v.Treatment + ' is not implemented here'))

    return [sql, artlist]


def fCompModelToSQL(modelspec, source_table='data', score_basename='Score', score_prefix='', score_suffix='', join_keys=None, to_score=True,
        starting_with=True, final_with=True, 
        with_prefix='pass', with_final_tag='final', with_marginals=True, with_statics=True):

    if bHasComponentModels(modelspec):
        if starting_with:
            sql = 'with '
        else:
            sql = ' '
        for i in range(0, len(modelspec.ComponentModels.ComponentModel)):
            cmdl = modelspec.ComponentModels.ComponentModel[i]
            if i:
                sql = sql + '\n, '
            sql = sql + '\n' + fCompModelToSQL(cmdl
                    , source_table=source_table
                    , score_basename=cmdl.Name
                    , final_with=False
                    , starting_with=False
                    , with_prefix='prep'+cmdl.Name
                    , with_final_tag=cmdl.Name
                    , with_marginals=(with_marginals and len(cmdl.ModelDirectives.Responses.as_list())>1)
                    , with_statics=(with_statics and (cmdl.Name not in ('Applicability','Baseline','PreCond','PreConditioning')))
                    , join_keys=join_keys
                    )
    
        return '---\n'+sql+'\n---'

    else:

        rv={}
        rv['woSuffix']={}
        resplist = modelspec.ModelDirectives.Responses.as_list()
        for resp in resplist:
            rv[resp]={}
    
        found = False
        for v in modelspec.Variables.Variable:
            if v.VariableModelDirectives.ProcessFirst=='Yes' and v.VariableModelDirectives.SpecialUse=='SegmentationOnly':
                found = True
                break

        sql1 = ''
        if found:
            for v in modelspec.Variables.Variable:
                if v.VariableModelDirectives.ProcessFirst=='Yes' and v.VariableModelDirectives.SpecialUse=='SegmentationOnly':
                    if v.Treatment in('Categorical','NCategorical'):
                        vsql, artlist = fVariable2SQL(v)
                        sql1 = sql1 + vsql
                    else: #else is not implemented here
                        raise(Exception('Non [N]Categoricals not for segmentation only is not implemented here'))
                    rv['woSuffix'][v.Name] = artlist

        if starting_with:
            sql = 'with '
        else:
            sql = ''

        anyyet = False

        if sql1:
            anyyet = True
            sql = sql + with_prefix + '1 as ('
            sql = sql + '\n    select 1 as _in' + with_prefix + '1'
            for k in join_keys:
                sql = sql + '\n        , pass0.' + k
            sql = sql + sql1
            sql = sql + '\n    from ' + source_table + ' pass0)'
        
        found = False
        for v in modelspec.Variables.Variable:
            if v.Name in rv['woSuffix']:
                pass
            elif v.VariableModelDirectives.ProcessFirst=='Yes':
                found = True
                break

        sql2 = ''
        if found:
            #second pass to gather other ProcessFirst variables that are not used for segmentation purposes only
            for v in modelspec.Variables.Variable:
                if v in rv['woSuffix']:
                    continue
                elif v.VariableModelDirectives.ProcessFirst=='Yes':
                    found = True
                    vsql, artlist = fVariable2SQL(v,to_score= ( v.VariableModelDirectives.ResponseUse == 'All' or v.VariableModelDirectives.ResponseUse in resplist ))
                    sql2 = sql2 + vsql
                    rv['woSuffix'][v.Name] = artlist

        if sql2:
            if anyyet:
                sql = sql + '\n, ' + with_prefix + '2 as ('
            else:
                sql = sql + with_prefix + '2 as ('
            sql = sql + '\n    select 1 as _in' + with_prefix + '2'
            for k in join_keys:
                sql = sql + '\n        , pass0.' + k
            sql = sql + sql2
            sql = sql + '\n    from ' + source_table + ' pass0 '
            if anyyet:
                sql = sql + '    join ' + with_prefix + '1 on ' 
                for i,k in enumerate(join_keys):
                    if i:
                        sql = sql + ' and '
                    sql = sql + ' pass0.'+k+'=' + with_prefix + '1.'+k
            sql = sql + ')'
            anyyet = True
        
        found = False
        for v in modelspec.Variables.Variable:
            if v.Name in rv['woSuffix']:
                pass
            elif v.VariableModelDirectives.ResponseUse == 'All' or v.VariableModelDirectives.ResponseUse in resplist:
                found = True
                break

        sql3 = ''
        if found:
            #third pass is to gather the rest
            #now process remaining
            for v in modelspec.Variables.Variable:
                if v.Name in rv['woSuffix']:
                    pass
                else:
                    vsql, artlist = fVariable2SQL(v,to_score= ( v.VariableModelDirectives.ResponseUse == 'All' or v.VariableModelDirectives.ResponseUse in resplist ))
                    sql3 = sql3 + vsql
                    rv['woSuffix'][v.Name] = artlist
    
        if sql3:
            if anyyet:
                sql = sql + '\n, ' + with_prefix + '3 as ('
            else:
                sql = sql + with_prefix + '3 as ('
            sql = sql + '\n    select 1 as _in' + with_prefix + '3'
            for k in join_keys:
                sql = sql + '\n        , pass0.' + k
            sql = sql + sql3
            sql = sql + '\n    from ' + source_table + ' pass0 '
            if anyyet:
                if sql1:
                    sql = sql + '\n    join ' + with_prefix + '1 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '1.'+k
                if sql2:
                    sql = sql + '\n    join ' + with_prefix + '2 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '2.'+k
            sql = sql + ')'
            anyyet = True
        
    
        if to_score:

            sql = sql + '\n, ' + with_prefix + 'marginals as ( select 1 as _in' + with_prefix + 'marginals'
            for k in join_keys:
                sql = sql + '\n        , pass0.' + k
            marginals = []
            for v in modelspec.Variables.Variable:
                if v.Name in rv['woSuffix']:
                    if v.VariableModelDirectives.ResponseUse == 'All' or v.VariableModelDirectives.ResponseUse in modelspec.ModelDirectives.Responses.as_list():
                        Static_Suffix = '_Static' if (v.VariableModelDirectives.Static == 'Yes') else ''
                        if v.VariableModelDirectives.ResponseUse == 'All':
                            respset = resplist
                        else:
                            respset = [v.VariableModelDirectives.ResponseUse]
                        for resp in respset:
                            if to_score:
                                ri = resplist.index(resp)
                                coefs = v.CoefficientsSet.as_list()[ri]
                                sql = sql + '\n        , ( 0.0 '
                                for arti, art in enumerate(rv['woSuffix'][v.Name]):
                                    sql = sql + ' + (' + str(coefs[arti]) + ')*'+art
                                sql = sql + ' ) as ' + v.Name + Static_Suffix + '_' + resp
                                marginals.append(v.Name + Static_Suffix + '_' + resp)

            sql = sql + '\n    from ' + source_table + ' pass0 '
            if anyyet:
                if sql1:
                    sql = sql + '\n    join ' + with_prefix + '1 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '1.'+k
                if sql2:
                    sql = sql + '\n    join ' + with_prefix + '2 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '2.'+k
                if sql3:
                    sql = sql + '\n    join ' + with_prefix + '3 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '3.'+k
            sql = sql + ')'
        
            sql = sql + '\n, ' + with_prefix + with_final_tag +' as ( select 1 as _in' + with_prefix + with_final_tag
            for k in join_keys:
                sql = sql + '\n        , pass0.' + k
            sql = sql + '\n        , ( 0.0 '
            for nm in marginals:
                sql = sql + ' + ' + nm 
            sql = sql + ' ) as ' + score_basename
            if with_marginals:
                for r in resplist:
                    sql = sql + '\n        , ( 0.0 '
                    for nm in marginals:
                        if nm.endswith(r):
                            sql = sql + ' + ' + nm
                    sql = sql + ' ) as ' + score_basename + '_' + r
            if with_statics:
                for r in resplist:
                    sql = sql + '\n        , ( 0.0 '
                    for nm in marginals:
                        if nm.endswith(r) and (nm.find('_Static_')>-1):
                            sql = sql + ' + ' + nm
                    sql = sql + ' ) as ' + score_basename + '_Static_' + r
    
            sql = sql + '\n    from ' + source_table + ' pass0 '
            if anyyet:
                if sql1:
                    sql = sql + '\n    join ' + with_prefix + '1 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '1.'+k
                if sql2:
                    sql = sql + '\n    join ' + with_prefix + '2 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '2.'+k
                if sql3:
                    sql = sql + '\n    join ' + with_prefix + '3 on ' 
                    for i,k in enumerate(join_keys):
                        if i:
                            sql = sql + ' and '
                        sql = sql + ' pass0.'+k+'=' + with_prefix + '3.'+k
            sql = sql + '\n    join ' + with_prefix + 'marginals on ' 
            for i,k in enumerate(join_keys):
                if i:
                    sql = sql + ' and '
                sql = sql + ' pass0.'+k+'=' + with_prefix + 'marginals.'+k
            sql = sql + ')'
    
    return sql



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






