'''A cython wrap of the basic Artificials.[hc] code '''

from libc.stdlib cimport free
import numpy as np
cimport numpy as np
from libc.stdlib cimport malloc, free

import polars as pl

cdef extern from "stddef.h":
    ctypedef Py_UNICODE wchar_t

cdef extern from "../../../WDS-C/include/WDS/ModelSpec/Artificials.h":
    ctypedef enum eTreatment:
        e_Unknown            "eTreatment::e_Unknown"
        e_None               "eTreatment::e_None"
        e_Constant           "eTreatment::e_Constant"
        e_CodedMissings      "eTreatment::e_CodedMissings"
        e_DiscreteLC         "eTreatment::e_DiscreteLC"
        e_DiscreteRC         "eTreatment::e_DiscreteRC"
        e_Hats               "eTreatment::e_Hats"
        e_iHats              "eTreatment::e_iHats"
        e_BSplineOrder2      "eTreatment::e_BSplineOrder2"
        e_BSplineOrder3      "eTreatment::e_BSplineOrder3"
        e_Categorical        "eTreatment::e_Categorical"
        e_CategoricalNumeric "eTreatment::e_CategoricalNumeric"

cdef extern from "../../../WDS-C/include/WDS/ModelSpec/Artificials.h":
    cdef eTreatment eTreatmentFromLong(long arg)
    cdef bint eTreatment_bIn(int vacount, ...) 
    cdef const wchar_t* eTreatmentLabel(eTreatment arg) 
    cdef eTreatment eTreatmentClean(wchar_t* data, int n) 
    cdef int nArtificialCount(int nCritVals, eTreatment Treatment) 
    cdef int nArtificialIndex_First(int nCritVals, eTreatment Treatment) 
    cdef int nArtificialIndex_Last(int nCritVals, eTreatment Treatment) 
    cdef int fArtificials_Numeric(double* SourceValue, int nSourceValueRowCount, eTreatment Treatment, double* CriticalValues, int nCritVals, double* CleanLimits, int nCleanLimits, double* Arts, int nArts, int nArtsRowCount, int nArtsColumnCount, int nArtsRowOffset, int nArtsColumnOffset, bint bRowMajor) 
    cdef int fArtificialsScored_Numeric(double* SourceValue, int nSourceValueRowCount, eTreatment Treatment, double* CriticalValues, int nCritVals, double* CleanLimits, int nCleanLimits, double* Coefficients, int nCoefficients, int nCoefficientSets, double* Results, int nResults, int nResultsRowCount, int nResultsColumnCount, int nResultsRowOffset, int nResultsColumnOffset, bint bRowMajor) 
    cdef int fArtificials_CategoricalNumeric(double* SourceValue, int nSourceValueRowCount, eTreatment Treatment, double** CriticalValues, int* nCritVals_, double* CleanLimits, int nCleanLimits, double* Arts, int nArts, int nArtsRowCount, int nArtsColumnCount, int nArtsRowOffset, int nArtsColumnOffset, bint bRowMajor) 
    cdef int fArtificialsScored_CategoricalNumeric(double* SourceValue, int nSourceValueRowCount, eTreatment Treatment, double** CriticalValues, int* nCritVals_, double* CleanLimits, int nCleanLimits, double* Coefficients, int nCoefficients, int nCoefficientSets, double* Results, int nResults, int nResultsRowCount, int nResultsColumnCount, int nResultsRowOffset, int nResultsColumnOffset, bint bRowMajor) 
    cdef int fArtificials_Categorical(wchar_t** SourceValue, int nSourceValueRowCount, eTreatment Treatment, wchar_t*** CriticalValues, int* nCritVals_, double* CleanLimits, int nCleanLimits, double* Arts, int nArts, int nArtsRowCount, int nArtsColumnCount, int nArtsRowOffset, int nArtsColumnOffset, bint bRowMajor) 
    cdef int fArtificialsScored_Categorical(wchar_t** SourceValue, int nSourceValueRowCount, eTreatment Treatment, wchar_t*** CriticalValues, int* nCritVals_, double* CleanLimits, int nCleanLimits, double* Coefficients, int nCoefficients, int nCoefficientSets, double* Results, int nResults, int nResultsRowCount, int nResultsColumnCount, int nResultsRowOffset, int nResultsColumnOffset, bint bRowMajor) 


cpdef _eTreatmentClean(str arg):
    cdef wchar_t* warg=arg
    cdef str rv=<str> eTreatmentLabel(eTreatmentClean(warg, len(arg)) )
    return rv

cpdef _eTreatmentToLong(str arg):
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

cpdef _eTreatmentFromLong(long arg):
    cdef str rv=<str> eTreatmentFromLong(arg)
    return rv
    
cpdef _nArtificialCount(int nCritVals, str Treatment):
    cdef wchar_t* warg=Treatment
    cdef int rv=nArtificialCount(nCritVals, eTreatmentClean(warg, len(Treatment)) )
    return rv

cpdef _nArtificialIndex_First(int nCritVals, str Treatment):
    cdef wchar_t* warg=Treatment
    cdef int rv=nArtificialIndex_First(nCritVals, eTreatmentClean(warg, len(Treatment))) 
    return rv

cpdef _nArtificialIndex_Last(int nCritVals, str Treatment):
    cdef wchar_t* warg=Treatment
    cdef int rv=nArtificialIndex_Last(nCritVals, eTreatmentClean(warg, len(Treatment))) 
    return rv


cpdef _fArtificials_Numeric(np.ndarray[double, ndim=2] SourceValue
                            , str Treatment
                            , np.ndarray[double, ndim=2] CriticalValues
                            , np.ndarray[double, ndim=2] CleanLimits):
    cdef wchar_t* warg=Treatment
    cdef int nrows=SourceValue.shape[0]
    cdef int nArts=_nArtificialCount(CriticalValues.shape[1], Treatment) 
    cdef double[:,::1] rv=np.ndarray((nrows, nArts),dtype=np.double)
    cdef double* CL=NULL
    cdef int nCL=0
    if CleanLimits.shape[1]>0: 
        CL=&CleanLimits[0,0]
        nCL=CleanLimits.shape[1]
    cdef int rc = 0
    rc = fArtificials_Numeric(&SourceValue[0,0]
                            , nrows
                            , eTreatmentClean(warg, len(Treatment))
                            , &CriticalValues[0,0]
                            , CriticalValues.shape[1]
                            , CL
                            , nCL
                            , &rv[0,0]
                            , nArts
                            , nrows
                            , nArts
                            , 0
                            , 0
                            , True) 
    if rc!=0: raise("Error in fArtificials_Numeric")
    return rv.base


cpdef _fArtificialsScored_Numeric(np.ndarray[double, ndim=2] SourceValue
                            , str Treatment
                            , np.ndarray[double, ndim=2] CriticalValues
                            , np.ndarray[double, ndim=2] CleanLimits
                            , np.ndarray[double, ndim=2] Coefficients
                            ):
    cdef wchar_t* warg=Treatment
    cdef int nrows=SourceValue.shape[0]
    cdef int nArts=nArtificialCount(CriticalValues.shape[2], eTreatmentClean(warg, len(Treatment))) 
    cdef int nScores=Coefficients.shape[0]
    cdef double[:,::1] rv=np.empty((nrows, nScores))
    cdef double* CL=NULL
    cdef int nCL=0
    if CleanLimits.shape[1]>0: 
        CL=&CleanLimits[0,0]
        nCL=CleanLimits.shape[1]
    cdef int rc= fArtificialsScored_Numeric(&SourceValue[0,0]
                            , nrows
                            , eTreatmentClean(warg, len(Treatment))
                            , &CriticalValues[0,0]
                            , CriticalValues.shape[1]
                            , CL
                            , nCL
                            , &Coefficients[0,0]
                            , Coefficients.shape[1]
                            , Coefficients.shape[0]
                            , &rv[0,0]
                            , nScores
                            , nrows
                            , nScores
                            , 0
                            , 0
                            , True) 
    if rc!=0: raise(Exception("Error in fArtificialsScored_Numeric"))
    return rv.base



cpdef _fArtificials_CategoricalNumeric(np.ndarray[double, ndim=2] SourceValue
                            , str Treatment
                            , list _CriticalValues
                            , np.ndarray[double, ndim=2] CleanLimits):
    cdef int* nCritVals   = <int *> malloc((len(_CriticalValues)+1)*sizeof(int))
    nCritVals[0]=len(_CriticalValues)
    cdef double **CriticalValues = <double **> malloc(nCritVals[0]*sizeof(double *))
    cdef int i
    cdef int j
    for i in range(0,nCritVals[0]):
        nCritVals[i+1]=len(_CriticalValues[i])
        CriticalValues[i]=<double *> malloc(nCritVals[i+1]*sizeof(double))
        for j in range(0,nCritVals[i+1]):
            CriticalValues[i][j]=_CriticalValues[i][j]
    cdef wchar_t* warg=Treatment
    cdef int nrows=SourceValue.shape[0]
    cdef int nArts=nArtificialCount(nCritVals[0], eTreatmentClean(warg, len(Treatment))) 
    cdef double[:,::1] rv=np.empty((nrows, nArts)) #,dtype=double)
    cdef double* CL=NULL
    cdef int nCL=0
    if CleanLimits.shape[1]>0: 
        CL=&CleanLimits[0,0]
        nCL=CleanLimits.shape[1]
    cdef int rc= fArtificials_CategoricalNumeric(&SourceValue[0,0]
                            , nrows
                            , eTreatmentClean(warg, len(Treatment))
                            , &CriticalValues[0]
                            , &nCritVals[0]
                            , CL
                            , nCL
                            , &rv[0,0]
                            , nArts
                            , nrows
                            , nArts
                            , 0
                            , 0
                            , True) 
    return np.asarray(rv)

cpdef _fArtificialsScored_CategoricalNumeric(np.ndarray[double, ndim=2] SourceValue
                            , str Treatment
                            , list _CriticalValues
                            , np.ndarray[double, ndim=2] CleanLimits
                            , np.ndarray[double, ndim=2] Coefficients
                            ):
    cdef int* nCritVals   = <int *> malloc((len(_CriticalValues)+1)*sizeof(int))
    nCritVals[0]=len(_CriticalValues)
    cdef double **CriticalValues = <double **> malloc(nCritVals[0]*sizeof(double *))
    cdef int i
    cdef int j
    for i in range(0,nCritVals[0]):
        nCritVals[i+1]=len(_CriticalValues[i])
        CriticalValues[i]=<double *> malloc(nCritVals[i+1]*sizeof(double))
        for j in range(0,nCritVals[i+1]):
            CriticalValues[i][j]=_CriticalValues[i][j]
    cdef wchar_t* warg=Treatment
    cdef int nrows=SourceValue.shape[0]
    cdef int nArts=nArtificialCount(nCritVals[0], eTreatmentClean(warg, len(Treatment))) 
    cdef int nScores=Coefficients.shape[0]
    cdef double[:,::1] rv=np.empty((nrows, nScores)) #,dtype=double)
    cdef double* CL=NULL
    cdef int nCL=0
    if CleanLimits.shape[1]>0: 
        CL=&CleanLimits[0,0]
        nCL=CleanLimits.shape[1]
    cdef int rc= fArtificialsScored_CategoricalNumeric(&SourceValue[0,0]
                            , nrows
                            , eTreatmentClean(warg, len(Treatment))
                            , &CriticalValues[0]
                            , &nCritVals[0]
                            , CL
                            , nCL
                            , &Coefficients[0,0]
                            , nArts
                            , nScores
                            , &rv[0,0]
                            , nScores
                            , nrows
                            , nScores
                            , 0
                            , 0
                            , True) 
    return rv.base



cpdef _fArtificials_Categorical(np.ndarray[str, ndim=2] SourceValue
                            , str Treatment
                            , list _CriticalValues
                            ):
    cdef int* nCritVals   = <int *> malloc((len(_CriticalValues)+1)*sizeof(int))
    nCritVals[0]=len(_CriticalValues)
    cdef wchar_t ***CriticalValues = <wchar_t ***> malloc(nCritVals[0]*sizeof(wchar_t **))
    cdef int i
    cdef int j
    for i in range(0,nCritVals[0]):
        nCritVals[i+1]=len(_CriticalValues[i])
        CriticalValues[i]=<wchar_t **> malloc(nCritVals[i+1]*sizeof(wchar_t *))
        for j in range(0,nCritVals[i+1]):
            CriticalValues[i][j]=_CriticalValues[i][j]
    cdef wchar_t* warg=Treatment
    cdef int nrows=SourceValue.shape[0]
    cdef int nArts=nArtificialCount(nCritVals[0], eTreatmentClean(warg, len(Treatment))) 
    cdef double[:,::1] rv=np.empty((nrows, nArts)) #,dtype=double)
    cdef double z=0.0;
    cdef wchar_t* arg
    cdef int rc
    for i in range(0,nrows):
        arg=SourceValue[i,0]
        rc= fArtificials_Categorical(&arg
                            , 1
                            , eTreatmentClean(warg, len(Treatment))
                            , &CriticalValues[0]
                            , &nCritVals[0]
                            , &z
                            , 0
                            , &rv[i,0]
                            , nArts
                            , 1
                            , nArts
                            , 0
                            , 0
                            , True) 
    return np.asarray(rv)

cpdef _fArtificialsScored_Categorical(np.ndarray[str, ndim=2] SourceValue
                            , str Treatment
                            , list _CriticalValues
                            , np.ndarray[double, ndim=2] Coefficients
                            ):
    cdef int* nCritVals   = <int *> malloc((len(_CriticalValues)+1)*sizeof(int))
    nCritVals[0]=len(_CriticalValues)
    cdef wchar_t ***CriticalValues = <wchar_t ***> malloc(nCritVals[0]*sizeof(wchar_t **))
    cdef int i
    cdef int j
    cdef double z=0.0
    for i in range(0,nCritVals[0]):
        nCritVals[i+1]=len(_CriticalValues[i])
        CriticalValues[i]=<wchar_t **> malloc(nCritVals[i+1]*sizeof(wchar_t *))
        for j in range(0,nCritVals[i+1]):
            CriticalValues[i][j]=_CriticalValues[i][j]
    cdef wchar_t* warg=Treatment
    cdef int nrows=SourceValue.shape[0]
    cdef int nArts=nArtificialCount(nCritVals[0], eTreatmentClean(warg, len(Treatment))) 
    cdef int nScores=Coefficients.shape[0]
    cdef double[:,::1] rv=np.empty((nrows, nScores))
    cdef wchar_t* arg
    cdef int rc

    for i in range(0,nrows):
        arg=SourceValue[i]
        rc= fArtificialsScored_Categorical(&arg
                            , 1
                            , eTreatmentClean(warg, len(Treatment))
                            , &CriticalValues[0]
                            , &nCritVals[0]
                            , &z
                            , 0
                            , &Coefficients[0,0]
                            , nArts
                            , nScores
                            , &rv[i,0]
                            , nScores
                            , i
                            , nScores
                            , 0
                            , 0
                            , True) 
    return rv.base

cpdef fViewCorrectly(Source=None, as_column=True, as_float=True):
    if (type(Source) is not np.ndarray) and hasattr(Source, 'as_numpy'):
        return getattr(Source, 'as_numpy')()
    if type(Source) in (np.array, np.ndarray):
        if len(Source.shape) == 2:
            return Source
        else:
            if as_column:
                return Source.view().reshape((len(Source),1))
            else:
                return Source.view().reshape((1,len(Source)))
    if type(Source) is pl.Series:
        if as_column:
            return Source.to_numpy().reshape((len(Source),1))
        else:
            return Source.to_numpy().reshape((1,len(Source)))
    if type(Source) is tuple:
        if type(Source[0]) is tuple:
            if as_float:
                return fViewCorrectly(np.array(*Source,dtype=np.float64), as_column, as_float)
            else:
                return fViewCorrectly(np.array(*Source,dtype=type(Source[0][0])), as_column, as_float)
        else:
            if as_float:
                return fViewCorrectly(np.array(Source,dtype=np.float64), as_column, as_float)
            else:
                return fViewCorrectly(np.array(Source,dtype=type(Source[0])), as_column, as_float)
    if type(Source) is list:
        if type(Source[0]) is list:
            if as_float:
                return fViewCorrectly(np.array(*Source,dtype=np.float64), as_column, as_float)
            else:
                return fViewCorrectly(np.array(*Source,dtype=type(Source[0][0])), as_column, as_float)
        else:
            if as_float:
                return fViewCorrectly(np.array(Source,dtype=np.float64), as_column, as_float)
            else:
                return fViewCorrectly(np.array(Source,dtype=type(Source[0])), as_column, as_float)
    return Source

cpdef fViewCorrectlyAsColumn(Source, as_float=True): return fViewCorrectly(Source, as_column=True, as_float=as_float)

cpdef fViewCorrectlyAsRow(Source, as_float=True): return fViewCorrectly(Source, as_column=False, as_float=as_float)

cpdef fArtificials(Source=None
        , Treatment=None
        , CriticalValues=None
        , CleanLimits=None
        , str LabelBase='Art'
        , str LabelConnector='_'
        , str LabelSuffix=""
        , DropIndexs=None
        ):
    if Source is None or Treatment is None or CriticalValues is None: raise("Insufficient arguments to fArtificials")
    cdef str trt=_eTreatmentClean(Treatment);
    rv=None
    if trt=="Categorical":
        rv = _fArtificials_Categorical(fViewCorrectlyAsColumn(Source),trt,CriticalValues)
        lbls = fArtificialLabels(len(CriticalValues)
                                                , Treatment
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                            )
    elif trt=="CategoricalNumeric":
        if CleanLimits is None:
            rv = _fArtificials_CategoricalNumeric(fViewCorrectlyAsColumn(Source),trt,fViewCorrectlyAsRow(CriticalValues),np.ndarray((0,0),dtype=np.double))
        else:
            rv = _fArtificials_CategoricalNumeric(fViewCorrectlyAsColumn(Source),trt,fViewCorrectlyAsRow(CriticalValues),fViewCorrectlyAsRow(CleanLimits))
        lbls = fArtificialLabels(len(CriticalValues)
                                                , Treatment
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                            )
    else:
        CriticalValues = fViewCorrectlyAsRow(CriticalValues)
        if CleanLimits is None:
            rv = _fArtificials_Numeric(fViewCorrectlyAsColumn(Source),trt,CriticalValues,np.ndarray((0,0),dtype=np.double))
        else:
            rv = _fArtificials_Numeric(fViewCorrectlyAsColumn(Source),trt,CriticalValues,fViewCorrectlyAsRow(CleanLimits))
        lbls = fArtificialLabels(CriticalValues.shape[1]
                                                , Treatment
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                            )
    if DropIndexs:
        if type(DropIndexs) is not list:
            if type(DropIndexs) in (int, float):
                DropIndexs = [int(DropIndexs)]
            else:
                DropIndexs = getattr(DropIndexs,'as_list')()
        ncrits = CriticalValues.shape[1]
        limits = [_nArtificialIndex_First(ncrits, Treatment),_nArtificialIndex_Last(ncrits, Treatment)]
        if min(DropIndexs)<limits[0] or max(DropIndexs)>limits[1]:
            raise(Exception("In fArtificials, index limits exceeded, "+str(DropIndexs)+" must be within "+str(limits)))
        DropIndexs.sort(reverse=True)
        for i in DropIndexs:
            lbls.pop(i)
            rv=np.delete(rv,i,1)
    rv.dtype = [(lbl,np.double) for lbl in lbls]
    return rv.view(np.recarray)


cpdef fArtificialsScored(Source=None
                            , Treatment=None
                            , CriticalValues=None
                            , CleanLimits=None
                            , CoefficientsSet=None
                            , str LabelBase='Score'
                            , str LabelConnector='_'
                            , str LabelSuffix=""
                            , int LabelStart=1
                            ):
    if Source is None or Treatment is None or CriticalValues is None: raise("Insufficient arguments to fArtificials")
    cdef str trt=_eTreatmentClean(Treatment);
    Source = fViewCorrectlyAsColumn(Source)
    cdef int nrows=Source.shape[0]
    CoefficientsSet = fViewCorrectly(CoefficientsSet)
    cdef int nScores=CoefficientsSet.shape[0]
    cdef double[:,::1] rv # =np.empty((nrows, nScores))
    if trt=="Categorical":
        if CleanLimits is None: raise("Insufficient arguments to fArtificials")
        rv = _fArtificialsScored_Categorical(fViewCorrectlyAsColumn(Source,as_float=False),trt,CriticalValues,CleanLimits)
    else:
        if CoefficientsSet is None: raise("Insufficient arguments to fArtificials")
        if trt=="CategoricalNumeric":
            if CleanLimits is None:
                rv = _fArtificialsScored_CategoricalNumeric(fViewCorrectlyAsColumn(Source),trt,CriticalValues,np.ndarray((0,0),dtype=np.double),CoefficientsSet)
            else:
                rv = _fArtificialsScored_CategoricalNumeric(fViewCorrectlyAsColumn(Source),trt,CriticalValues,CleanLimits,CoefficientsSet)
        else:
            if CleanLimits is None:
                rv = _fArtificialsScored_Numeric(fViewCorrectlyAsColumn(Source),trt,CriticalValues,np.ndarray((0,0),dtype=np.double),CoefficientsSet)
            else:
                rv = _fArtificialsScored_Numeric(fViewCorrectlyAsColumn(Source),trt,fViewCorrectlyAsRow(CriticalValues),fViewCorrectlyAsRow(CleanLimits),CoefficientsSet)
    rv.base.dtype = [(lbl,np.double) for lbl in fArtificialsScoredLabels(nScores
                                                , LabelStart=LabelStart
                                                , LabelBase=LabelBase
                                                , LabelConnector=LabelConnector
                                                , LabelSuffix=LabelSuffix
                                                )]
    return rv.base.view(np.recarray)

cpdef fArtificialLabels(int nCriticalValues, str sTreatment, str LabelBase="X", str LabelConnector="", str LabelSuffix=""):
    cdef int n=_nArtificialCount(nCriticalValues, sTreatment)
    cdef int First=_nArtificialIndex_First(nCriticalValues, sTreatment)
    #cdef int Last=_nArtificialIndex_Last(nCriticalValues, sTreatment)
    cdef int i
    rv=[]
    cdef int j=First-1
    for i in range(0,n):
        j+=1
        rv.append(LabelBase + LabelConnector + str(j) + LabelSuffix)
    return rv

cpdef fArtificialsScoredLabels(int nScores, int LabelStart=0, str LabelBase="X", str LabelConnector="", str LabelSuffix=""):
    #cdef int Last=_nArtificialIndex_Last(nCriticalValues, sTreatment)
    rv=[]
    cdef int i
    cdef int j=LabelStart-1
    for i in range(0,nScores):
        j+=1
        rv.append(LabelBase + LabelConnector + str(j) + LabelSuffix)
    return rv




