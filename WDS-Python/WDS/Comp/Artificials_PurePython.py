'''A Pure-Python version of the basic Artificials.[hc] code 

Copyright (c) 2019-2022 Wypasek Data Science, Inc.
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
from typing import Union, List, Dict, Tuple, Sequence
from enum import Enum
import math

#define compTag0 Constants

NCRITVALS_MAX=30
NARTVALS_MAX=32
NRESULTVALS_MAX=32

wdsTreatmentError=-1
wdsCriticalValuesError=-2
wdsArtificialsLocationError=-3
wdsResultsLocationError=-4
wdsCoefficientsError=-5

#define compTag0e Constants


#define compTag1 enum eTreatment start
class eTreatment(Enum):
    e_Unknown = -1
    e_None = 0
    e_Constant = 1
    e_CodedMissings = 2
    e_DiscreteLC = 3
    e_DiscreteRC = 4
    e_Hats = 5
    e_iHats = 6
    e_BSplineOrder2 = 7
    e_BSplineOrder3 = 8
    e_Categorical = 9
    e_CategoricalNumeric = 10

#define compTag2 eTreatmentFromLong start
def eTreatmentFromLong(arg: int) -> eTreatment:
    iarg = int(arg)
    if (arg < -1 or arg > eTreatment.e_CategoricalNumeric): 
        return eTreatment.e_Unknown
    for trt in eTreatment:
        if iarg == trt.value:
            return trt
    return eTreatment.e_Unknown

#define compTag3 eTreatment_bIn start
def eTreatment_bIn(*valist) -> bool:
    arg = valist[0]
    if type(arg) is eTreatment:
        arg = arg.value
    for i, v in enumerate(valist):
        if i==0:
            arg = v
            if type(arg) is int:
                arg = eTreatmentFromLong(arg)
        else:
            if type(v) is int:
                if arg.value==v:
                    return True
            elif type(v) is eTreatment:
                if arg==v:
                    return True
    return False

#define compTag4 eTreatmentLabel start
def eTreatmentLabel(arg: eTreatment) -> str:
    s = arg.name
    return s[2:]


#define compTag5 eTreatmentClean start

def eTreatmentClean(data: str, n: Union[int, None]=None) -> str:
    if n is None:
        n=len(data)
    if (n <= 0) :
        return eTreatment.e_Unknown;
    if (n == 7 and data=="Unknown") :
        return eTreatment.e_Unknown;
    if (n == 4 and data == "None") :
        return eTreatment.e_None;
    if (n == 8 and data == "Constant") :
        return eTreatment.e_Constant;
    if (n == 13 and data == "CodedMissings") :
        return eTreatment.e_CodedMissings;
    if (n == 10 and data == "DiscreteLC") :
        return eTreatment.e_DiscreteLC;
    if (n == 10 and data == "DiscreteRC") :
        return eTreatment.e_DiscreteRC;
    if (n == 4 and data == "Hats") :
        return eTreatment.e_Hats;
    if (n == 5 and data == "iHats") :
        return eTreatment.e_iHats;
    if (n == 13 and data == "BSplineOrder2") :
        return eTreatment.e_BSplineOrder2;
    if (n == 13 and data == "BSplineOrder3") :
        return eTreatment.e_BSplineOrder3;
    if (n == 11 and data == "Categorical") :
        return eTreatment.e_Categorical;
    if (n == 18 and data == "CategoricalNumeric") :
        return eTreatment.e_CategoricalNumeric;

    sdata = data.lower()

    if (data == "unknown"): return eTreatment.e_Unknown;
    if (data == "none"): return eTreatment.e_None;
    if (data == "constant"): return eTreatment.e_Constant;
    if (data == "codedmissings"): return eTreatment.e_CodedMissings;
    if (data == "discretelc"): return eTreatment.e_DiscreteLC;
    if (data == "discreterc"): return eTreatment.e_DiscreteRC;
    if (data == "hats"): return eTreatment.e_Hats;
    if (data == "ihats"): return eTreatment.e_iHats;
    if (data == "bsplineorder2"): return eTreatment.e_BSplineOrder2;
    if (data == "bsplineorder3"): return eTreatment.e_BSplineOrder3;
    if (data == "categorical"): return eTreatment.e_Categorical;
    if (data == "categoricalnumeric"): return eTreatment.e_CategoricalNumeric;

    if (sdata == "straight"): return eTreatment.e_None;
    if (sdata == "numeric"): return eTreatment.e_None;
    if (sdata == "missings"): return eTreatment.e_CodedMissings;

    if (sdata == "bucketslc"): return eTreatment.e_DiscreteLC;
    if (sdata == "levelslc"): return eTreatment.e_DiscreteLC;
    if (sdata == "discretizelc"): return eTreatment.e_DiscreteLC;
    if (sdata == "intervalslc"): return eTreatment.e_DiscreteLC;
    if (sdata == "disclc"): return eTreatment.e_DiscreteLC;
    if (sdata == "bz0lc"): return eTreatment.e_DiscreteLC;
    if (sdata == "bso0lc"): return eTreatment.e_DiscreteLC;
    if (sdata == "caglad"): return eTreatment.e_DiscreteLC;
    if (sdata == "collor"): return eTreatment.e_DiscreteLC;
    if (sdata == "lcrl"): return eTreatment.e_DiscreteLC;

    if (sdata == "buckets"): return eTreatment.e_DiscreteRC;
    if (sdata == "levels"): return eTreatment.e_DiscreteRC;
    if (sdata == "discretize"): return eTreatment.e_DiscreteRC;
    if (sdata == "intervals"): return eTreatment.e_DiscreteRC;
    if (sdata == "disc"): return eTreatment.e_DiscreteRC;
    if (sdata == "bz0"): return eTreatment.e_DiscreteRC;
    if (sdata == "bso0"): return eTreatment.e_DiscreteRC;

    if (sdata == "bucketsrc"): return eTreatment.e_DiscreteRC;
    if (sdata == "levelsrc"): return eTreatment.e_DiscreteRC;
    if (sdata == "discretizerc"): return eTreatment.e_DiscreteRC;
    if (sdata == "intervalsrc"): return eTreatment.e_DiscreteRC;
    if (sdata == "discrc"): return eTreatment.e_DiscreteRC;
    if (sdata == "bz0rc"): return eTreatment.e_DiscreteRC;
    if (sdata == "bso0rc"): return eTreatment.e_DiscreteRC;
    if (sdata == "cadlag"): return eTreatment.e_DiscreteRC;
    if (sdata == "corlol"): return eTreatment.e_DiscreteRC;
    if (sdata == "rcll"): return eTreatment.e_DiscreteRC;

    if (sdata == "buckets"): return eTreatment.e_DiscreteRC;
    if (sdata == "levels"): return eTreatment.e_DiscreteRC;
    if (sdata == "discretize"): return eTreatment.e_DiscreteRC;
    if (sdata == "intervals"): return eTreatment.e_DiscreteRC;
    if (sdata == "disc"): return eTreatment.e_DiscreteRC;
    if (sdata == "bz0"): return eTreatment.e_DiscreteRC;
    if (sdata == "bso0"): return eTreatment.e_DiscreteRC;

    if (sdata == "bz1"): return eTreatment.e_Hats;
    if (sdata == "bso1"): return eTreatment.e_Hats;
    if (sdata == "integratedhats"): return eTreatment.e_iHats;
    if (sdata == "bsplineo2"): return eTreatment.e_BSplineOrder2;
    if (sdata == "bz2"): return eTreatment.e_BSplineOrder2;
    if (sdata == "bso2"): return eTreatment.e_BSplineOrder2;
    if (sdata == "bsplineo3"): return eTreatment.e_BSplineOrder3;
    if (sdata == "bz3"): return eTreatment.e_BSplineOrder3;
    if (sdata == "bso3"): return eTreatment.e_BSplineOrder3;
    if (sdata == "cat"): return eTreatment.e_Categorical;
    if (sdata == "string"): return eTreatment.e_Categorical;
    if (sdata == "ncat"): return eTreatment.e_CategoricalNumeric;
    if (sdata == "ncategorical"): return eTreatment.e_CategoricalNumeric;

    return eTreatment.e_Unknown;


#define compTag5 nArtificialCount start

def nArtificialCount(nCritVals: int, Treatment: Union[str,eTreatment]) -> int:

    if type(Treatment) is str:
        Treatment = eTreatmentClean(Treatment)

    match Treatment:
        case eTreatment.e_Unknown:
            return 0
        case eTreatment.e_None:
            return 1
        case eTreatment.e_Constant:
            return 1
        case eTreatment.e_CodedMissings:
            return 2
        case eTreatment.e_DiscreteLC | eTreatment.e_DiscreteRC:
            return nCritVals + 2
        case eTreatment.e_Hats | eTreatment.e_iHats:
            return nCritVals + 1
        case eTreatment.e_BSplineOrder2:
            return nCritVals
        case eTreatment.e_BSplineOrder3:
            return nCritVals - 1
        case eTreatment.e_Categorical | eTreatment.e_CategoricalNumeric:
            return nCritVals + 1
        case _:
            return 0
    return  0

#define compTag6 nArtificialIndex_First start

def nArtificialIndex_First(nCritVals: int, Treatment: eTreatment) -> int:

    match Treatment:
        case eTreatment.e_Unknown:
            return 1
        case eTreatment.e_None:
            return 1
        case eTreatment.e_Constant:
            return 1
        case _:
            return 0
    return  0


#define compTag6 nArtificialIndex_Last start

def nArtificialIndex_Last(nCritVals: int, Treatment: eTreatment) -> int:

    tmp = nArtificialCount(nCritVals, Treatment)

    match Treatment:
        case eTreatment.e_Unknown:
            return 1
        case eTreatment.e_None:
            return 1
        case eTreatment.e_Constant:
            return 1
        case eTreatment.e_CodedMissings:
            return 1
        case eTreatment.e_DiscreteLC:
            return tmp - 1
        case eTreatment.e_DiscreteRC:
            return tmp - 1
        case eTreatment.e_Hats:
            return tmp - 1
        case eTreatment.e_iHats:
            return tmp - 1
        case eTreatment.e_BSplineOrder2:
            return tmp - 1
        case eTreatment.e_BSplineOrder3:
            return tmp - 1
        case eTreatment.e_Categorical:
            return tmp - 1
        case eTreatment.e_CategoricalNumeric:
            return tmp - 1
        case _:
            return 0
    return tmp - 1

#define compTag6 __fArtificials_temp1 start

def __fArtificials_temp1(Treatment: eTreatment,
        nCleanLimits: int,
        CleanLimits: List,
        bUsingCleanLimitLeft: bool,
        CleanLimitLeftVal: float,
        bUsingCleanLimitRight: bool,
        CleanLimitRightVal: float,
        nCritVals: int,
        CriticalValues: List,
        Cnstnt: float,
        dCVs: List,
        dCVsdiv2: List,
        d2CVs: List,
        d2CVsdiv2: List,
        d3CVs: List,
        eps: float
        ) -> List:


    if (nCleanLimits > 0) :
        bUsingCleanLimitLeft = True
        CleanLimitLeftVal = CleanLimits[0]
    if (nCleanLimits > 1) :
        bUsingCleanLimitRight = True
        CleanLimitRightVal = CleanLimits[1]

    nCritValsM1 = nCritVals - 1

    if (eTreatment_bIn(Treatment, eTreatment.e_Categorical, eTreatment.e_CategoricalNumeric)) :
        return wdsTreatmentError
    elif (Treatment == eTreatment.e_Constant) :
        if (nCritVals <= 0): return wdsCriticalValuesError
        Cnstnt = CriticalValues[0]
    elif (not (Treatment == eTreatment.e_None or Treatment == eTreatment.e_Constant)) :
        for i, v in enumerate(CriticalValues):
            #if (CriticalValues[iM1] >= CriticalValues[i] - *eps) return wdsCriticalValuesError;
            if i==0:
                lv = v
            else:
                if ( lv >= v - eps ): return wdsCriticalValuesError
        if (eTreatment_bIn(Treatment, eTreatment.e_Hats, eTreatment.e_iHats, eTreatment.e_BSplineOrder2, eTreatment.e_BSplineOrder3)) :
            dCVs = [ 0.0 for i in range(0, nCritVals-1) ]
            for i, v in enumerate(CriticalValues):
                if i==0:
                    lv = v
                    iM1 = 0
                else:
                    dCVs[iM1] = v - lv
                    iM1 = i
            if (Treatment == eTreatment.e_iHats):
                dCVsdiv2 = [ 0.0 for i in range(0, nCritVals-1) ]
                for iM1 in range(0, nCritValsM1):
                    dCVsdiv2[iM1] = dCVs[iM1] / 2.0
        if (eTreatment_bIn(Treatment, eTreatment.e_iHats, eTreatment.e_BSplineOrder2, eTreatment.e_BSplineOrder3)) :
            d2CVs = [ 0.0 for i in range(0, nCritVals-2) ]
            iM2 = -1
            for i in range(2, nCritVals):
                iM2 += 1
                d2CVs[iM2] = CriticalValues[i] - CriticalValues[iM2]
            if (Treatment == eTreatment.e_iHats):
                d2CVsdiv2 = [ 0.0 for i in range(0, nCritVals-2) ]
                iM2 = -1
                for i in range(2, nCritVals):
                    iM2 += 1
                    d2CVsdiv2[iM2] = d2CVs[iM2] / 2.0
        if (Treatment == eTreatment.e_BSplineOrder3) :
            d3CVs = [ 0.0 for i in range(0, nCritVals-3) ]
            iM3 = -1
            for i in range(3, nCritVals):
                iM3 += 1
                d3CVs[iM3] = CriticalValues[i] - CriticalValues[iM3]

    return (0,
        nCleanLimits,
        CleanLimits,
        bUsingCleanLimitLeft,
        CleanLimitLeftVal,
        bUsingCleanLimitRight,
        CleanLimitRightVal,
        nCritVals,
        CriticalValues,
        Cnstnt,
        dCVs,
        dCVsdiv2,
        d2CVs,
        d2CVsdiv2,
        d3CVs,
        )

#define compTag7 fArtificials_Numeric start

def fArtificials_Numeric(SourceValue: Union[float, List[float]] # // possibly a vector
        , nSourceValueRowCount: int
        , Treatment: eTreatment
        , CriticalValues: Union[int,float,List[float],List[List[float]]]
        , nCritVals: int
        , CleanLimits: List[float]
        , nCleanLimits: int
        , Arts: List[float]
        , nArts: int
        , nArtsRowCount: int
        , nArtsColumnCount: int
        , nArtsRowOffset: int
        , nArtsColumnOffset: int
        , bRowMajor: bool
        ) -> int :

    if bRowMajor:
        def at_(r,c):
            return ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset)
    else:
        def at_(r,c): 
            return ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)

    if Treatment in (eTreatment.e_Unknown, eTreatment.e_Categorical, eTreatment.e_CategoricalNumeric):
        return wdsTreatmentError

    #print(CriticalValues)
    #print(type(CriticalValues))
    #print(type(CriticalValues[0]))
    if type(CriticalValues) in (int,float):
        CriticalValues=[CriticalValues,]
    elif type(CriticalValues[0]) is list:
        CriticalValues=CriticalValues.flatten()
    elif hasattr(CriticalValues,'aslist'):
        CriticalValues=CriticalValues.aslist().flatten()
    #print(CriticalValues)
    #print(type(CriticalValues))
    #print(type(CriticalValues[0]))

    if (nCritVals > NCRITVALS_MAX):
        return wdsCriticalValuesError;
    if (nArts > NARTVALS_MAX):
        return wdsArtificialsLocationError;

    if (nSourceValueRowCount < 1 or nArtsRowOffset<0 or nArtsRowOffset>nArtsRowCount):
        return wdsArtificialsLocationError;
    if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset):
        return wdsArtificialsLocationError;
    if (nArtsColumnOffset<0 or nArtsColumnOffset + nArts>nArtsColumnCount):
        return wdsArtificialsLocationError;
    if (nArtsRowCount < nSourceValueRowCount):
        return wdsArtificialsLocationError;

    eps = 1.0e-14
    Cnstnt = 1.0

    CleanLimitLeftVal = math.nan #nan(""); // NAN;
    CleanLimitRightVal = math.nan #nan(""); // NAN;
    bUsingCleanLimitLeft = False
    bUsingCleanLimitRight = False
    dCVs=[]
    dCVsdiv2=[]
    d2CVs=[]
    d2CVsdiv2=[]
    d3CVs=[]

    nCritValsM1 = nCritVals - 1


    rc, nCleanLimits, CleanLimits, bUsingCleanLimitLeftVal, CleanLimitLeftVal, bUsingCleanLimitRight, CleanLimitRightVal, nCritVals, CriticalValues, Cnstnt, dCVs, dCVsdiv2, d2CVs, d2CVsdiv2, d3CVs = __fArtificials_temp1(Treatment,
            nCleanLimits,
            CleanLimits,
            bUsingCleanLimitLeft,
            CleanLimitLeftVal,
            bUsingCleanLimitRight,
            CleanLimitRightVal,
            nCritVals,
            CriticalValues,
            Cnstnt,
            dCVs,
            dCVsdiv2,
            d2CVs,
            d2CVsdiv2,
            d3CVs,
            eps);

    if (rc != 0):
        return rc

    nrows = nSourceValueRowCount

    #/*
    #   --[[
    #   'CodeDoc - CJW :
    #   '   For consistency, using:
    #   '       r for row index
    #   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
    #   '       ia for the VBA 'option base 1' artificial index
    #   '       k for score index
    #   --]]
    # */

    for r in range(0, nrows):

        if nrows==1 and type(SourceValue) is not list:
            tempval = SourceValue
        else:
            tempval = SourceValue[r]

        match (Treatment) :
            case eTreatment.e_None:
                Arts[at_(r, 0)] = tempval
            case eTreatment.e_Constant:
                Arts[at_(r, 0)] = Cnstnt
            case eTreatment.e_Categorical | eTreatment.e_CategoricalNumeric:
                return wdsTreatmentError
            case _:

                bIsMissing = math.isinf(tempval) or math.isnan(tempval)
                bIsMissing = bIsMissing or ((not bIsMissing) and (bUsingCleanLimitLeft and (tempval < CleanLimitLeftVal)))
                bIsMissing = bIsMissing or ((not bIsMissing) and (bUsingCleanLimitRight and (tempval > CleanLimitRightVal)))

                if (bIsMissing) :

                    i = 0
                    ia = 0

                    Arts[at_(r, ia)] = 1.0
                    for ia in range(1,nArts):
                        Arts[at_(r, ia)] = 0.0

                else:


                    #//--just to keep things communicable and relatable to usual mathematical discussion
                    x = tempval;
                    #print(x,CriticalValues[0])

                    if (Treatment == eTreatment.e_CodedMissings) :

                        Arts[at_(r, 0)] = 0.0
                        Arts[at_(r, 1)] = x

                    elif (x <= CriticalValues[0] + eps) :
                        Arts[at_(r, 0)] = 0.0
                        i = 1
                        ia = 1

                        if (Treatment == eTreatment.e_iHats) :

                            Arts[at_(r, ia)] = x - CriticalValues[0]

                        else:

                            if ((Treatment == eTreatment.e_DiscreteRC) and (x >= CriticalValues[0] - eps)) :

                                i = i + 1
                                ia = ia + 1

                            Arts[at_(r, ia)] = 1.0

                        for iai in range(ia+1, nArts):
                            Arts[at_(r, ia)] = 0.0

                    elif (x >= CriticalValues[nCritValsM1] - eps) :

                        for ia in range(0, nArts):
                            Arts[at_(r, ia)] = 0.0

                        #//--'all non-missing last artificials are 1 right of the last critical value, except iHats and DiscreteLC
                        i = nCritValsM1
                        ia = nArts - 1

                        if (Treatment == eTreatment.e_iHats) :
                            Arts[at_(r, ia)] = x - CriticalValues[i] + dCVs[i - 1] / 2.0
                            ia = 1
                            for j in range(1, nCritVals-1):
                                ia += 1
                                Arts[at_(r, ia)] += d2CVs[j - 1] / 2.0
                            Arts[at_(r, 1)] += dCVs[0] / 2.0
                        else: 

                            if ((Treatment == eTreatment.e_DiscreteLC) and (x <= CriticalValues[nCritValsM1] + eps)) :
                                i -= 1
                                ia -= 1

                            Arts[at_(r, ia)] = 1.0

                    else:

                        for ia in range(0, nArts):
                            Arts[at_(r, ia)] = 0.0

                        if (Treatment == eTreatment.e_DiscreteLC):
                            found = False
                            i = 0
                            ia = 1
                            for j in range(0, nCritVals-1):
                                if ((x > CriticalValues[j] + eps and x <= CriticalValues[j + 1]) or
                                        (x > CriticalValues[j] and x <= CriticalValues[j + 1] + eps)
                                        ):
                                    found = True
                                    i = j
                                    ia = i + 2
                                    break
                        elif (Treatment == eTreatment.e_DiscreteRC): 
                            found = False
                            i = 0
                            ia = 1
                            for j in range(0, nCritVals-1):
                                if (math.fabs(x - CriticalValues[j + 1]) < eps):
                                    found = True
                                    i = j + 1
                                    ia = i + 2
                                    break
                                elif (x > CriticalValues[j] and x < CriticalValues[j + 1]):
                                    found = True
                                    i = j
                                    ia = i + 2
                                    break
                        else:
                            found = False;
                            i = 0
                            ia = 1
                            for j in range(0, nCritVals-1):
                                if ((x >= CriticalValues[j] and x < CriticalValues[j + 1]) or
                                        (x >= CriticalValues[j] - eps and x < CriticalValues[j + 1])
                                        ):
                                    found = True
                                    i = j
                                    ia = i + 1

                        match Treatment:

                            case eTreatment.e_DiscreteLC:
                                Arts[at_(r, ia)] = 1.0
                            case eTreatment.e_DiscreteRC:
                                Arts[at_(r, ia)] = 1.0
                            case eTreatment.e_Hats:
                                tempdouble = (x - CriticalValues[i]) / dCVs[i]
                                Arts[at_(r, ia + 1)] = tempdouble
                                Arts[at_(r, ia)] = (1.0 - tempdouble)
                            case eTreatment.e_iHats:
                                tempdouble = math.pow((x - CriticalValues[i]), 2.0) / dCVs[i] / 2.0
                                iaP1 = ia + 1
                                Arts[at_(r, iaP1)] = tempdouble
                                Arts[at_(r, ia)] = (x - CriticalValues[i] - tempdouble)
                                for ii in range(0, i):
                                    iia = ii + 1
                                    iiaP1 = iia + 1
                                    Arts[at_(r, iiaP1)] += dCVsdiv2[ii]
                                    Arts[at_(r, iia)] += dCVsdiv2[ii]
                            case eTreatment.e_BSplineOrder2:
                                iM1 = i - 1
                                ia = i + 2
                                iaM1 = ia - 1
                                iaM2 = ia - 2
                                xMci = (x - CriticalValues[i])
                                xMciM1 = 0.0
                                if (i > 0) :
                                    xMciM1 = (x - CriticalValues[iM1])

                                #//-- 'the last artificial is a right catch all
                                #//-- 'therefore, fo0, [f]unction [o]ffset [0], stops with CVs(varm.nCritVals-2)
                                #//-- 'and fo1 is a catch all at CVs(varm.nCritVals-1)

                                fo0 = 0.0
                                fo1 = 0.0
                                fo2 = 0.0

                                if (i < nCritValsM1-1) :
                                    #//--' a+b=1,p+q=1
                                    #//--' a*p
                                    fo0 = xMci / d2CVs[i] * xMci / dCVs[i]
                                if (i == 0) :
                                    #//--'fo1 is a catch all where not defined
                                    fo1 = 1.0 - fo0
                                elif (i < nCritValsM1-1) :
                                    #//--'the starting interpolation of the preceding basis * corresponding right side of lower order Hat
                                    #//--'+the starting right interpolation of preceding basis * corresponding left side of lower order Hat
                                    #//--' a*q
                                    #//--' +b*p
                                    fo1 = xMciM1 / d2CVs[iM1] * (1 - xMci / dCVs[i]) + (1 - xMci / d2CVs[i]) * xMci / dCVs[i]
                                if (i == 1) :
                                    #//--'fo2 is a catch all where not defined
                                    fo2 = 1 - fo0 - fo1
                                elif (i > 1) :
                                    #//--'the remaining right interpolation of second preceding basis * corresponding right side of lower order Hat
                                    #//--' b*q
                                    fo2 = (1 - xMciM1 / d2CVs[iM1]) * (1 - xMci / dCVs[i])
                                if (i == nCritValsM1 - 1) :
                                    fo1 = 1.0 - fo2


                                if (ia < nArts - 1):
                                    Arts[at_(r, ia)] = fo0
                                else:
                                    Arts[at_(r, nArts - 1)] = fo0

                                if (iaM1 > 0) :
                                    if (iaM1 < nArts - 1) :
                                        Arts[at_(r, iaM1)] += fo1
                                    else:
                                        Arts[at_(r, nArts - 1)] += fo1


                                if (iaM2 > 0) :
                                    Arts[at_(r, iaM2)] += fo2

                            case eTreatment.e_BSplineOrder3:

                                iM1 = i - 1;
                                iM2 = i - 2;
                                ia = i + 2;
                                iaM1 = ia - 1;
                                iaM2 = ia - 2;
                                iaM3 = ia - 3;

                                xMci = (x - CriticalValues[i]);
                                xMciM1 = 0.0;
                                xMciM2 = 0.0;

                                if (i > 0):
                                    xMciM1 = (x - CriticalValues[iM1]);
                                if (i > 1):
                                    xMciM2 = (x - CriticalValues[iM2]);

                                fo0 = 0.0;
                                fo1 = 0.0;
                                fo2 = 0.0;
                                fo3 = 0.0;

                                if (i < nCritValsM1 - 2):
                                    #//--' u+v=1,a+b=1,p+q=1
                                    #//--' u[0]*a[0]*p[0]
                                    fo0 = xMci / d3CVs[i] * xMci / d2CVs[i] * xMci / dCVs[i];
                                if (i == 0):
                                    fo1 = 1.0 - fo0;
                                elif (i < nCritValsM1 - 2):
                                    #//--' u[-1]*(a[-1]*q[0] + b*p[0])
                                    #//--'+v[0]*(a[0]*p[0])
                                    fo1 = ( (xMciM1 / d3CVs[iM1]) * (xMciM1 / d2CVs[iM1] * (1.0 - xMci / dCVs[i])
                                            + (1.0 - xMci / d2CVs[i]) * (xMci / dCVs[i])) +
                                        (1.0 - xMci / d3CVs[i]) * (xMci / d2CVs[i] * xMci / dCVs[i])
                                        )

                                if (i == 1):
                                    fo2 = 1.0 - fo0 - fo1;
                                elif ((i > 1) and (i < nCritValsM1 - 1)):
                                    #//--' u[-2]*(b[-1]*q[0])
                                    #//--'+v[-1]*(a[-1]*q[0]+b[0]*p[0])
                                    fo2 = (
                                            (xMciM2 / d3CVs[iM2]) * ((1.0 - xMciM1 / d2CVs[iM1]) * (1.0 - xMci / dCVs[i]))
                                        + (1.0 - xMciM1 / d3CVs[iM1]) * (xMciM1 / d2CVs[iM1] * (1.0 - xMci / dCVs[i])
                                                + (1.0 - xMci / d2CVs[i]) * (xMci / dCVs[i]))
                                        )
                                if (i == 2):
                                    fo3 = 1.0 - fo0 - fo1 - fo2;
                                elif (i > 2):
                                    #//--' v[-2]*b[-1]*p[0]
                                    fo3 = (1.0 - xMciM2 / d3CVs[iM2]) * (1.0 - xMciM1 / d2CVs[iM1]) * (1.0 - xMci / dCVs[i]);
                                #//else if ((i > 2) and (i < nCritValsM1))

                                if (i == nCritValsM1 - 2):
                                    fo1 = 1.0 - fo2 - fo3;
                                if (i == nCritValsM1 - 1):
                                    fo2 = 1.0 - fo3;

                                if (ia < nArts - 1):
                                    Arts[at_(r, ia)] = fo0;
                                else:
                                    Arts[at_(r, nArts - 1)] = fo0;

                                if (iaM1 > 0) :
                                    if (iaM1 < nArts - 1):
                                        Arts[at_(r, iaM1)] = fo1;
                                    else:
                                        Arts[at_(r, nArts - 1)] += fo1;
                                if (iaM2 > 0) :
                                    if (iaM2 < nArts - 1):
                                        Arts[at_(r, iaM2)] = fo2;
                                    else:
                                        Arts[at_(r, nArts - 1)] += fo2;
                                if (iaM3 > 0) :
                                    if (iaM3 < nArts - 1):
                                        Arts[at_(r, iaM3)] = fo3;
                                    else:
                                        Arts[at_(r, nArts - 1)] += fo3;

                            case _:
                                return wdsTreatmentError
    return 0

#define compTag8 fArtificials_Numeric start

def fArtificialsScored_Numeric(SourceValue: Union[float, List] #  // possibly a vector
        , nSourceValueRowCount: int
        , Treatment: eTreatment
        , CriticalValues: List[float]
        , nCritVals: int
        , CleanLimits: List[float]
        , nCleanLimits: int
        , Coefficients: List[float]
        , nCoefficients: int
        , nCoefficientSets: int
        , Results: List[float]
        , nResults: int
        , nResultsRowCount: int #    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
        , nResultsColumnCount: int # // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
        , nResultsRowOffset: int # // generally = 0, but can be used to imbed result into a system matrix
        , nResultsColumnOffset: int # // generally = 0, but can be used to imbed result into a system matrix
        , bRowMajor: bool
        , bCoefRowMajor: bool
        ) -> int:

    if bRowMajor:
        def at_(r,c):
            return ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset)
    else:
        def at_(r,c): 
            return ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)

    if bCoefRowMajor:
        def score_at_(r,c):
            return ((r+nResultsRowOffset)*nResultsColumnCount+c+nResultsColumnOffset) 
    else:
        def score_at_(r,c):
            return ((r+nResultsRowOffset)+(c+nResultsColumnOffset)*nResultsRowCount)

    if Treatment in (eTreatment.e_Unknown, eTreatment.e_Categorical, eTreatment.e_CategoricalNumeric):
        return wdsTreatmentError

    if type(CriticalValues) in (int,float):
        CriticalValues=[CriticalValues,]
    elif type(CriticalValues[0]) is list:
        CriticalValues=CriticalValues[0]

    if (nCritVals > NCRITVALS_MAX):
        return wdsCriticalValuesError;
    if (nResults > NRESULTVALS_MAX):
        return wdsResultsLocationError;

    if (nSourceValueRowCount < 1 or nResultsRowOffset<0 or nResultsRowOffset>nResultsRowCount):
        return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset):
        return wdsResultsLocationError;
    if (nResultsColumnOffset<0 or nResultsColumnOffset + nResults>nResultsColumnCount):
        return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount):
        return wdsResultsLocationError;

    eps = 0.0000000001;
    Cnstnt = 1.0;

    CleanLimitLeftVal = math.nan #nan(""); // NAN;
    CleanLimitRightVal = math.nan #nan(""); // NAN;
    bUsingCleanLimitLeft = False
    bUsingCleanLimitRight = False
    dCVs=[]
    dCVsdiv2=[]
    d2CVs=[]
    d2CVsdiv2=[]
    d3CVs=[]

    nCritValsM1 = nCritVals - 1


    rc, nCleanLimits, CleanLimits, bUsingCleanLimitLeftVal, CleanLimitLeftVal, bUsingCleanLimitRight, CleanLimitRightVal, nCritVals, CriticalValues, Cnstnt, dCVs, dCVsdiv2, d2CVs, d2CVsdiv2, d3CVs = __fArtificials_temp1(Treatment,
            nCleanLimits,
            CleanLimits,
            bUsingCleanLimitLeft,
            CleanLimitLeftVal,
            bUsingCleanLimitRight,
            CleanLimitRightVal,
            nCritVals,
            CriticalValues,
            Cnstnt,
            dCVs,
            dCVsdiv2,
            d2CVs,
            d2CVsdiv2,
            d3CVs,
            eps);

    if (rc != 0):
        return rc


    nArts = nArtificialCount(nCritVals, Treatment)
    if (nArts != nCoefficients):
        return wdsCoefficientsError

    nrows = nSourceValueRowCount

    #/*
    #   --[[
    #   'CodeDoc - CJW :
    #   '   For consistency, using:
    #   '       r for row index
    #   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
    #   '       ia for the VBA 'option base 1' artificial index
    #   '       k for score index
    #   --]]
    # */

    for r in range(0, nrows):

        tempval = SourceValue[r];

        match Treatment:
            case eTreatment.e_None:
                if (bCoefRowMajor):
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = tempval * Coefficients[ir*nCoefficients]
                else:
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = tempval * Coefficients[ir]
            case eTreatment.e_Constant:
                if (bCoefRowMajor):
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = Cnstnt * Coefficients[ir*nCoefficients];
                else:
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = Cnstnt * Coefficients[ir];

            case eTreatment.e_Categorical:
                return wdsTreatmentError
            case eTreatment.e_CategoricalNumeric:
                return wdsTreatmentError

            case eTreatment.e_CodedMissings | eTreatment.e_Hats | eTreatment.e_iHats | eTreatment.e_DiscreteLC | eTreatment.e_DiscreteRC | eTreatment.e_BSplineOrder2 | eTreatment.e_BSplineOrder3:

                bIsMissing = math.isinf(tempval) or math.isnan(tempval)
                bIsMissing = bIsMissing or ((not bIsMissing) and (bUsingCleanLimitLeft and (tempval < CleanLimitLeftVal)))
                bIsMissing = bIsMissing or ((not bIsMissing) and (bUsingCleanLimitRight and (tempval > CleanLimitRightVal)))

                if (bIsMissing) :

                    ir = 0

                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = Coefficients[ir][0] #*nCoefficients]

                else: 

                    Arts = [0.0 for i in range(0, nArts)]

                    rc = fArtificials_Numeric(tempval, 1, Treatment, CriticalValues, nCritVals, CleanLimits, nCleanLimits, Arts, nArts, 1, nArts, 0, 0, bRowMajor);

                    #print(Coefficients)
                    #print(type(Coefficients))
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = 0.0;
                        for ia in range(0, nArts):
                            Results[score_at_(r, ir)] += Arts[ia] * Coefficients[ir][ia]

            case _:
                return wdsTreatmentError

    return 0

#define compTag9 fArtificials_CategoricalNumeric start

def fArtificials_CategoricalNumeric(SourceValue: Union[int, float, List] #  // possibly a vector
        , nSourceValueRowCount: int
        , Treatment: eTreatment
        , CriticalValues: List[int | float]
        , nCritVals_: List[int]
        , CleanLimits: List[int | float]
        , nCleanLimits: int
        , Arts: List[float]
        , nArts: int #            // just the column count expected to be returned with (Treatment, nCritVals)
         #// This could be determined within, but generally has already be calculated to allocate
         #// space for Arts.
         , nArtsRowCount: int    #// generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
         , nArtsColumnCount: int # // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
         , nArtsRowOffset: int #// generally = 0, but can be used to imbed result into a system matrix
         , nArtsColumnOffset: int # // generally = 0, but can be used to imbed result into a system matrix
         , bRowMajor: bool
         ):

    if bRowMajor:
        def at_(r,c):
            return ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset)
    else:
        def at_(r,c): 
            return ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)

    if Treatment != eTreatment.e_CategoricalNumeric:
        return wdsTreatmentError

    nCritVals = nCritVals_[0]

    if (nCritVals > NCRITVALS_MAX):
        return wdsCriticalValuesError
    if (nArts > NARTVALS_MAX):
        return wdsArtificialsLocationError

    if (nSourceValueRowCount < 1 or nArtsRowOffset<0 or nArtsRowOffset>nArtsRowCount):
        return wdsArtificialsLocationError
    if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset):
        return wdsArtificialsLocationError
    if (nArtsColumnOffset<0 or nArtsColumnOffset + nArts>nArtsColumnCount):
        return wdsArtificialsLocationError
    if (nArtsRowCount < nSourceValueRowCount):
        return wdsArtificialsLocationError

    eps = 0.00000001

    nrows = nSourceValueRowCount

    print(SourceValue)
    for r in range(0, nrows):

        if nrows==1 and type(tempval) is not list:
            tempval = SourceValue
        else:
            tempval = SourceValue[r]

        for ia in range(0, nArts):
            Arts[at_(r, ia)] = 0.0

        bIsMissing = math.isinf(tempval) or math.isnan(tempval)
        if (bIsMissing) :
            Arts[at_(r, 0)] = 1.0
        else:
            found = False
            for i, v in enumerate(CriticalValues):
                for j, vv in enumerate(v):
                    found = (math.fabs(tempval - vv) < eps)
                    if found:
                        break
                if found:
                    Arts[at_(r,i+1)] = 1.0
                    break
            if (not found):
                Arts[at_(r, 0)] = 1.0;

    return 0

#define compTag10 fArtificialsScored_CategoricalNumeric start

def fArtificialsScored_CategoricalNumeric(SourceValue: Union[int, float, list[Union[int, float]]]
        , nSourceValueRowCount: int
        , Treatment: eTreatment
        , CriticalValues: list[list[Union[int, float]]]
        , nCritVals_: int
        , CleanLimits: List[Union[int, float]]
        , nCleanLimits: int
        , Coefficients: List[List[float]]
        , nCoefficients: int
        , nCoefficientSets: int
        , Results: List[List[float]]
        , nResults: int
        , nResultsRowCount: int #    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
        , nResultsColumnCount: int # // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
        , nResultsRowOffset: int # // generally = 0, but can be used to imbed result into a system matrix
        , nResultsColumnOffset: int # // generally = 0, but can be used to imbed result into a system matrix
        , bRowMajor: bool
        , bCoefRowMajor: bool
        ) -> int:

    if bRowMajor:
        def at_(r,c):
            return ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset)
    else:
        def at_(r,c): 
            return ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)

    if bCoefRowMajor:
        def score_at_(r,c):
            return ((r+nResultsRowOffset)*nResultsColumnCount+c+nResultsColumnOffset) 
    else:
        def score_at_(r,c):
            return ((r+nResultsRowOffset)+(c+nResultsColumnOffset)*nResultsRowCount)

    if Treatment != eTreatment.e_CategoricalNumeric:
        return wdsTreatmentError

    nCritVals = nCritVals_[0]

    if (nCritVals > NCRITVALS_MAX):
        return wdsCriticalValuesError;
    if (nResults > NARTVALS_MAX):
        return wdsResultsLocationError;

    if (nSourceValueRowCount < 1 or nResultsRowOffset<0 or nResultsRowOffset>nResultsRowCount):
        return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset):
        return wdsResultsLocationError;
    if (nResultsColumnOffset<0 or nResultsColumnOffset + nResults>nResultsColumnCount):
        return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount):
        return wdsResultsLocationError;

    eps = 0.00000001

    nArts = nArtificialCount(nCritVals, Treatment)
    if (nArts != nCoefficients):
        return wdsCoefficientsError

    nrows = nSourceValueRowCount

    #/*
    #   --[[
    #   'CodeDoc - CJW :
    #   '   For consistency, using:
    #   '       r for row index
    #   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
    #   '       ia for the VBA 'option base 1' artificial index
    #   '       k for score index
    #   --]]
    # */

    for r in range(0, nrows):

        if nrows==1 and type(tempval) is not list:
            tempval = SourceValue
        else:
            tempval = SourceValue[r]

        bIsMissing = math.isinf(tempval) or math.isnan(tempval)
        if (bIsMissing):
            for ir in range(0, nCoefficientSets):
                Results[score_at_(r, ir)] = Coefficients[ir][0]
        else:
            found = False
            for i, v in enumerate(CriticalValues):
                for j, vv in enumerate(v):
                    found = (math.fabs(tempval - vv) < eps)
                    if found:
                        break
                if found:
                    iP1=i+1
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = Coefficients[ir][iP1]
                    break
            if (not found):
                for ir in range(0, nCoefficientSets):
                    Results[score_at_(r, ir)] = Coefficients[ir][0]

    return 0


#define compTag11 fArtificialsScored_Categorical start

def fArtificials_Categorical(SourceValue: Union[str, List[str]]
    , nSourceValueRowCount: int
    , Treatment: eTreatment
    , CriticalValues: List[List[str]]
    , nCritVals_: int
    , CleanLimits: List[None] #   // meaningless for Categorical, left in for argument list consistency
    , nCleanLimits: int #   // meaningless for Categorical, left in for argument list consistency
    , Arts: List[List[float]]
    , nArts: int #            // just the column count expected to be returned with (Treatment, nCritVals)
    #// This could be determined within, but generally has already be calculated to allocate
    #// space for Arts.
    , nArtsRowCount: int #    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
    , nArtsColumnCount: int # // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
    , nArtsRowOffset: int # // generally = 0, but can be used to imbed result into a system matrix
    , nArtsColumnOffset: int # // generally = 0, but can be used to imbed result into a system matrix
    , bRowMajor: bool
    ) -> int:

    if bRowMajor:
        def at_(r,c):
            return ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset)
    else:
        def at_(r,c): 
            return ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)

    if Treatment != eTreatment.e_Categorical:
        return wdsTreatmentError

    nCritVals = nCritVals_[0]

    if (nCritVals > NCRITVALS_MAX):
        return wdsCriticalValuesError
    if (nArts > NARTVALS_MAX):
        return wdsArtificialsLocationError

    if (nSourceValueRowCount < 1 or nArtsRowOffset<0 or nArtsRowOffset>nArtsRowCount):
        return wdsArtificialsLocationError
    if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset):
        return wdsArtificialsLocationError
    if (nArtsColumnOffset<0 or nArtsColumnOffset + nArts>nArtsColumnCount):
        return wdsArtificialsLocationError
    if (nArtsRowCount < nSourceValueRowCount):
        return wdsArtificialsLocationError

    nrows = nSourceValueRowCount

    #/*
    #   --[[
    #   'CodeDoc - CJW :
    #   '   For consistency, using:
    #   '       r for row index
    #   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
    #   '       ia for the VBA 'option base 1' artificial index
    #   '       k for score index
    #   --]]
    # */

    print("SourceValue")
    print(SourceValue)
    for r in range(0, nrows):

        if nrows==1 and type(SourceValue) is not list:
            tempstring = SourceValue
        else:
            tempstring = SourceValue[r]

        for ia in range(0, nArts):
            Arts[at_(r, ia)] = 0.0;

        bIsMissing = len(tempstring)==0

        if (bIsMissing) :
            Arts[at_(r, 0)] = 1.0
        else:
            found = False
            for i, v in enumerate(CriticalValues):
                for j, vv in enumerate(v):
                    found = (tempstring == vv)
                    if found:
                        break
                if found:
                    Arts[at_(r,i+1)] = 1.0
                    break
            if (not found):
                Arts[at_(r, 0)] = 1.0;

    return 0

#define compTag12 fArtificialsScored_Categorical start

def fArtificialsScored_Categorical(SourceValue: Union[str, List[str]]
        , nSourceValueRowCount: int
        , Treatment: eTreatment
        , CriticalValues: List[List[str]]
        , nCritVals_: List[int]
        , CleanLimits: List[None] #   // meaningless for Categorical, left in for argument list consistency
        , nCleanLimits: int #   // meaningless for Categorical, left in for argument list consistency
        , Coefficients: List[List[float]]
        , nCoefficients: int
        , nCoefficientSets: int
        , Results: List[float]
        , nResults: int
        , nResultsRowCount: int #    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
        , nResultsColumnCount: int # // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
        , nResultsRowOffset: int # // generally = 0, but can be used to imbed result into a system matrix
        , nResultsColumnOffset: int # // generally = 0, but can be used to imbed result into a system matrix
        , bRowMajor: bool
        , bCoefRowMajor: bool
        ):
    if Treatment != eTreatment.e_Categorical: 
        return wdsTreatmentError

    if bCoefRowMajor:
        def score_at_(r,c):
            return ((r+nResultsRowOffset)*nResultsColumnCount+c+nResultsColumnOffset) 
    else:
        def score_at_(r,c):
            return ((r+nResultsRowOffset)+(c+nResultsColumnOffset)*nResultsRowCount)


    nCritVals = nCritVals_[0]

    if (nCritVals > NCRITVALS_MAX):
        return wdsCriticalValuesError;
    if (nResults > NARTVALS_MAX):
        return wdsResultsLocationError;
    
    if (nSourceValueRowCount < 1 or nResultsRowOffset<0 or nResultsRowOffset>nResultsRowCount):
        return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset):
        return wdsResultsLocationError;
    if (nResultsColumnOffset<0 or nResultsColumnOffset + nResults>nResultsColumnCount):
        return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount):
        return wdsResultsLocationError;
    
    
    nArts = nArtificialCount(nCritVals, Treatment)
    if (nArts != nCoefficients):
        return wdsCoefficientsError;
    
    nrows = nSourceValueRowCount
    
    #/*
    #   --[[
    #   'CodeDoc - CJW :
    #   '   For consistency, using:
    #   '       r for row index
    #   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
    #   '       ia for the VBA 'option base 1' artificial index
    #   '       k for score index
    #   --]]
    # */
    
    for r in range(0, nrows):

        if nrows==1 and type(SourceValue) is not list:
            tempstring = SourceValue
        else:
            tempstring = SourceValue[r]

        bIsMissing = len(tempstring)==0
        if (bIsMissing):
            for ir in range(0, nCoefficientSets):
                Results[score_at_(r, ir)] = Coefficients[ir][0]
        else:
            found = False
            for i, v in enumerate(CriticalValues):
                found = ( tempstring in vv )
                if found:
                    iP1=i+1
                    for ir in range(0, nCoefficientSets):
                        Results[score_at_(r, ir)] = Coefficients[ir][iP1]
                    break
            if (not found):
                for ir in range(0, nCoefficientSets):
                    Results[score_at_(r, ir)] = Coefficients[ir][0]

    return 0



def _eTreatmentToLong(arg:str)->int:
    if arg=="e_Unknown": return 0
    if arg=="e_None": return 1
    if arg=="e_Constant": return 2
    if arg=="e_CodedMissings": return 3
    if arg=="e_DiscreteLC": return 4
    if arg=="e_DiscreteRC": return 5
    if arg=="e_Hats": return 6
    if arg=="e_iHats": return 7
    if arg=="e_BSplineOrder2": return 8
    if arg=="e_BSplineOrder3": return 9
    if arg=="e_Categorical": return 10
    if arg=="e_CategoricalNumeric": return 11
    return 0


def _fArtificials_Numeric(SourceValue: Union[float, List[float]]
        , _Treatment: Union[str, eTreatment]
        , CriticalValues: Union[float, List[float]]
        , CleanLimits: Union[None, float, List[float]]):

    if type(_Treatment) is str:
        Treatment = eTreatmentClean(_Treatment, len(_Treatment))
    else:
        Treatment = _Treatment
    if type(SourceValue) is float:
        SourceValue=[SourceValue,]
    nrows = len(SourceValue)
    if type(CriticalValues) in (int,float):
        CriticalValues=[CriticalValues,]
    elif type(CriticalValues[0]) is list:
        CriticalValues=CriticalValues[0]
    nCrits = len(CriticalValues)
    if type(CleanLimits) is None:
        CleanLimits=[]
    elif type(CleanLimits) is float:
        CleanLimits=[CleanLimits,]
    nCL=len(CleanLimits)

    nArts=nArtificialCount(nCrits, Treatment) 
    Arts=[0.0 for i in range(0, nrows*nArts)]

    CL=None
    if type(CleanLimits) in(int, float):
        CL=[CleanLimits,]
    else:
        CL=CleanLimits
    nCL=len(CL)

    rc = fArtificials_Numeric(SourceValue
                            , nrows
                            , Treatment
                            , CriticalValues
                            , nCrits
                            , CL
                            , nCL
                            , Arts
                            , nArts
                            , nrows
                            , nArts
                            , 0
                            , 0
                            , True) 
    if rc!=0: 
        raise(Exception("Error in fArtificials_Numeric"))
    return Arts


def _fArtificialsScored_Numeric(SourceValue: Union[float, List[float]]
        , _Treatment: str
        , CriticalValues: Union[float, List[float]]
        , CleanLimits: Union[None, float, List[float]]
        , Coefficients: List[List[float]]
        ):
    if type(_Treatment) is eTreatment:
        Treatment = _Treatment
    else:
        Treatment = eTreatmentClean(_Treatment, len(_Treatment))
    if type(SourceValue) is float:
        SourceValue=[SourceValue,]
    nrows = len(SourceValue)
    if type(CriticalValues) in (int,float):
        CriticalValues=[CriticalValues,]
    elif type(CriticalValues[0]) is list:
        CriticalValues=CriticalValues[0]

    nCrits = len(CriticalValues)
    if type(CleanLimits) is None:
        CleanLimits=[]
    elif type(CleanLimits) is float:
        CleanLimits=[CleanLimits,]
    nCL=len(CleanLimits)

    nCoefficientSets = len(Coefficients)
    nCoefficients = len(Coefficients[0])
    nArts=nArtificialCount(nCrits, Treatment) 
    rv=[0.0 for i in range(0, nrows*nCoefficients)]

    rc= fArtificialsScored_Numeric(SourceValue
                            , nrows
                            , Treatment
                            , CriticalValues
                            , nCrits
                            , CleanLimits
                            , nCL
                            , Coefficients
                            , nCoefficients
                            , nCoefficientSets
                            , rv
                            , nCoefficientSets
                            , nrows
                            , nCoefficientSets
                            , 0
                            , 0
                            , True
                            , True) 
    if rc!=0: 
        raise(Exception("Error in fArtificialsScored_Numeric"))
    return rv



def _fArtificials_CategoricalNumeric(_SourceValue: Union[int, float, List[Union[int, float]]]
    , _Treatment: str
    , _CriticalValues: List[List[Union[int, float]]]
    , _CleanLimits: Union[int, float, List[Union[int, float]]]
    ):
    if type(_SourceValue) in (int, float):
        SourceValue=[_SourceValue,]
    else:
        SourceValue=_SourceValue
    nrows = len(SourceValue)
    if type(_Treatment) is str:
        Treatment = eTreatmentClean(_Treatment, len(_Treatment))
    else:
        Treatment = _Treatment
    nCritVals = len(_CriticalValues)
    nCritVals_ = [0 for i in range(0, nCritVals+1)]
    nCritVals_[0]=len(_CriticalValues)
    for i in range(0, nCritVals):
        nCritVals_[i+1] = len(_CriticalValues[i])
    nrows=len(SourceValue)
    nArts=nArtificialCount(nCritVals, Treatment)
    rv = [0.0 for i in range(0, nrows * nArts)]
    if type(_CleanLimits) in (int,float):
        CL=[_CleanLimits,]
    else:
        CL=_CleanLimits
    nCL = len(CL)
    #print("nrows=",nrows)
    rc = fArtificials_CategoricalNumeric(SourceValue
                            , nrows
                            , Treatment
                            , _CriticalValues
                            , nCritVals_
                            , CL
                            , nCL
                            , rv
                            , nArts
                            , nrows
                            , nArts
                            , 0
                            , 0
                            , True) 
    return rv

def _fArtificialsScored_CategoricalNumeric(_SourceValue: Union[int, float, List[Union[int, float]]]
        , _Treatment: str
        , _CriticalValues: List[List[Union[int, float]]]
        , _CleanLimits: Union[int, float, List[Union[int, float]]]
        , Coefficients: List[List[float]]
        ):
    if type(_SourceValue) in (int, float):
        SourceValue=[_SourceValue,]
    else:
        SourceValue=_SourceValue
    nrows = len(SourceValue)
    if type(_Treatment) is str:
        Treatment = eTreatmentClean(_Treatment, len(_Treatment))
    else:
        Treatment = _Treatment
    nCritVals = len(_CriticalValues)
    nCritVals_ = [0 for i in range(0, nCritVals+1)]
    nCritVals_[0]=len(_CriticalValues)
    for i in range(0, nCritVals):
        nCritVals_[i+1] = len(_CriticalValues[i])
    nrows=len(SourceValue)
    nArts=nArtificialCount(nCritVals, Treatment)
    rv = [0.0 for i in range(0, nrows * nArts)]
    if type(_CleanLimits) in (int,float):
        CL=[_CleanLimits,]
    else:
        CL=_CleanLimits
    nCL = len(CL)
    nCoefficientSets = len(Coefficients)
    nScores = nCoefficientSets
    nCoefficients = len(Coefficients[0])
    rv=[0.0 for i in range(0, nrows*nScores) ]
    rc= fArtificialsScored_CategoricalNumeric(SourceValue
                            , nrows
                            , Treatment
                            , _CriticalValues
                            , nCritVals_
                            , CL
                            , nCL
                            , Coefficients
                            , nCoefficients
                            , nCoefficientSets
                            , rv
                            , nScores
                            , nrows
                            , nScores
                            , 0
                            , 0
                            , True
                            , True) 
    return rv


def _fArtificials_Categorical(_SourceValue: Union[str, List[str]]
        , _Treatment: Union[str, eTreatment]
        , _CriticalValues: List[List[str]]
        )->List[float]:
    if type(_Treatment) is str:
        Treatment = eTreatmentClean(_Treatment, len(_Treatment))
    else:
        Treatment = _Treatment
    if type(_SourceValue) is str:
        SourceValue=[_SourceValue,]
    else:
        SourceValue=_SourceValue
    nrows = len(SourceValue)
    nCritVals = len(_CriticalValues)
    nCritVals_ = [0 for i in range(0, nCritVals+1) ]
    nCritVals_[0]=nCritVals
    for i in range(0,nCritVals_[0]):
        nCritVals_[i+1]=len(_CriticalValues[i])
    nArts=nArtificialCount(nCritVals, Treatment)
    rv=[0.0 for i in range(0, nrows*nArts)]
    rc = fArtificials_Categorical(SourceValue
                            , nrows
                            , Treatment
                            , _CriticalValues
                            , nCritVals_
                            , []
                            , 0
                            , rv
                            , nArts
                            , nrows
                            , nArts
                            , 0
                            , 0
                            , True) 
    return rv

def _fArtificialsScored_Categorical(_SourceValue: Union[str, List[str]]
        , _Treatment: str
        , _CriticalValues: List[List[str]]
        , Coefficients: List[List[float]]
        )->List[float]:
    if type(_Treatment) is str:
        Treatment = eTreatmentClean(_Treatment, len(_Treatment))
    else:
        Treatment = _Treatment
    if type(_SourceValue) is str:
        SourceValue=[_SourceValue,]
    else:
        SourceValue=_SourceValue
    nrows = len(SourceValue)
    nCritVals = len(_CriticalValues)
    nCritVals_ = [0 for i in range(0, nCritVals+1) ]
    for i in range(0,nCritVals_[0]):
        nCritVals_[i+1]=len(_CriticalValues[i])
    nArts=nArtificialCount(nCritVals, Treatment)
    nCoefficientSets=len(Coefficients)
    nCoefficients=len(Coefficients[0])
    nScores=nCoefficientSets
    rv=[0.0 for i in range(0, nrows*nScores)]
    rc = fArtificialsScored_Categorical(SourceValue
                            , nrows
                            , Treatment
                            , _CriticalValues
                            , nCritVals_
                            , []
                            , 0
                            , Coefficients
                            , nArts
                            , nScores
                            , rv
                            , nScores
                            , nrows
                            , nScores
                            , 0
                            , 0
                            , True
                            , True) 
    return rv

_eTreatmentClean = eTreatmentClean
_eTreatmentFromLong = eTreatmentFromLong
_nArtificialCount = nArtificialCount
_nArtificialIndex_First = nArtificialIndex_First
_nArtificialIndex_Last = nArtificialIndex_Last




def fArtificials(Source=None
        , Treatment=None
        , CriticalValues=None
        , CleanLimits=None
        , LabelBase:str='Art'
        , LabelConnector:str='_'
        , LabelSuffix:str=""
        , DropIndexs:Union[None,int,List[int]]=None
        , bShow:bool=False
        , bShowInputs:bool=False
        ):
    bRowMajor=True
    if Source is None or Treatment is None or CriticalValues is None: raise("Insufficient arguments to fArtificials")
    if type(Source) in (int, float, str):
        nrows=1
    else:
        nrows=len(Source)
    trt=_eTreatmentClean(Treatment);
    rv=None
    if trt==eTreatment.e_Categorical:
        rv = _fArtificials_Categorical(Source,trt,CriticalValues)
        lbls = fArtificialLabels(len(CriticalValues)
                                                , Treatment
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                            )
    elif trt==eTreatment.e_CategoricalNumeric:
        if CleanLimits is None:
            rv = _fArtificials_CategoricalNumeric(Source,trt,CriticalValues,[])
        else:
            rv = _fArtificials_CategoricalNumeric(Source,trt,CriticalValues,CleanLimits)
        lbls = fArtificialLabels(len(CriticalValues)
                                                , Treatment
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                            )
    else:
        CriticalValues = CriticalValues
        if CleanLimits is None:
            rv = _fArtificials_Numeric(Source,trt,CriticalValues,[])
        else:
            rv = _fArtificials_Numeric(Source,trt,CriticalValues,CleanLimits)
        lbls = fArtificialLabels(len(CriticalValues)
                                                , Treatment
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                            )
    ncrits = len(CriticalValues)
    nArts = nArtificialCount(ncrits, trt)
    rv1=[]
    for i in range(0,nArts):
        rv1.append(rv[i::nArts])
    rv=rv1
    if DropIndexs:
        if type(DropIndexs) is not list:
            if type(DropIndexs) in (int, float):
                DropIndexs = [int(DropIndexs)]
            elif hasattr(DropIndexs,'as_list'):
                DropIndexs = getattr(DropIndexs,'as_list')()
            else:
                DropIndexs = []
        if len(DropIndexs)>0:
            limits = [_nArtificialIndex_First(ncrits, Treatment),_nArtificialIndex_Last(ncrits, Treatment)]
            if min(DropIndexs)<limits[0] or max(DropIndexs)>limits[1]:
                raise(Exception("In fArtificials, index limits exceeded, "+str(DropIndexs)+" must be within "+str(limits)))
            DropIndexs.sort(reverse=True)
            for i in DropIndexs:
                lbls.pop(i)
                rv.pop(i)

    if True: #Even though bRowMajor==True, rv has already been mapped to columns
        if bShow:
            nlbls=len(lbls)
            print("Labels", lbls)
            srv=[0.0 for j in range(0, nlbls)]
            for i in range(0,nrows):
                for j in range(0,nlbls):
                    srv[j]=rv[j][i]
                if bShowInputs:
                    print(i,Source[i], srv)
                else:
                    print(i,srv)

    return [rv,lbls]


def fArtificialsScored(Source=None
                            , Treatment=None
                            , CriticalValues=None
                            , CleanLimits=None
                            , CoefficientsSet=None
                            , LabelBase:str='Score'
                            , LabelConnector:str='_'
                            , LabelSuffix:str=""
                            , LabelStart:int=1
                            , bShow:bool=False
                            , bShowInputs:bool=False
                            ):
    bRowMajor=True
    if Source is None or Treatment is None or CriticalValues is None: raise("Insufficient arguments to fArtificials")
    trt=_eTreatmentClean(Treatment);
    nrows=len(Source)
    nScores=0
    rv=[0.0 for i in range(0, nrows*nScores)]
    if trt==eTreatment.e_Categorical:
        rv = _fArtificialsScored_Categorical(Source,trt,CriticalValues,CoefficientsSet)
    else:
        if CoefficientsSet is None: 
            raise("Insufficient arguments to fArtificials")
        if trt==eTreatment.e_CategoricalNumeric:
            if CleanLimits is None:
                rv = _fArtificialsScored_CategoricalNumeric(Source,trt,CriticalValues,[],CoefficientsSet)
            else:
                rv = _fArtificialsScored_CategoricalNumeric(Source,trt,CriticalValues,CleanLimits,CoefficientsSet)
        else:
            if CleanLimits is None:
                rv = _fArtificialsScored_Numeric(Source,trt,CriticalValues,[],CoefficientsSet)
            else:
                rv = _fArtificialsScored_Numeric(Source,trt,CriticalValues,CleanLimits,CoefficientsSet)

    nScores=len(CoefficientsSet)
    labels = fArtificialsScoredLabels(nScores
                                                , LabelStart=LabelStart
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                                )

    if bRowMajor:
        rv1=rv
        rv=[[0.0 for j in range(0,nScores)] for i in range(0, nrows)]
        for i in range(0,nrows):
            for j in range(0,nScores):
                rv[i][j]=rv1[i*nScores+j]
        if bShow:
            print("Labels", labels)
            for i in range(0,nrows):
                if bShowInputs:
                    print(i, Source[i], rv[i])
                else:
                    print(i, rv[i])
    else:
        rv1=rv
        rv=[[0.0 for i in range(0,nrows)] for i in range(0, nScores)]
        for j in range(0,nScores):
            for i in range(0,nrows):
                rv[j][i]=rv1[i+j*nrows]
        if bShow:
            print("Labels", labels)
            srv=[0.0 for j in range(0, nScores)]
            for i in range(0,nrows):
                for j in range(0,nScores):
                    srv[j]=rv[j][i]
                if bShowInputs:
                    print(i,Source[i], srv)
                else:
                    print(i,srv)

    return [rv, labels]

def fArtificialLabels(nCriticalValues:int, sTreatment:str, LabelBase:str="X", LabelConnector:str="", LabelSuffix:str=""):
    n=_nArtificialCount(nCriticalValues, sTreatment)
    First=_nArtificialIndex_First(nCriticalValues, sTreatment)
    rv=[]
    j=First-1
    for i in range(0,n):
        j+=1
        rv.append(LabelBase + LabelConnector + str(j) + LabelSuffix)
    return rv

def fArtificialsScoredLabels(nScores:int, LabelStart:int =0, LabelBase:str ="X", LabelConnector:str ="", LabelSuffix:str =""):
    rv=[]
    j=LabelStart-1
    for i in range(0,nScores):
        j+=1
        rv.append(LabelBase + LabelConnector + str(j) + LabelSuffix)
    return rv




