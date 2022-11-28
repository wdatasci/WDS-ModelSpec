#!/usr/bin/env python3


import Artificials_PurePython as art_c

import numpy as np

np.set_printoptions(linewidth=np.inf)

import polars as pl
pl.cfg.Config.set_tbl_cols(20)
pl.cfg.Config.set_tbl_rows(100)


if __name__=="__main__":
    #print(dir(art_c))
    #print(art_c.__name__)
    s="Buckets"
    print("s=",s," clean treatment=",art_c._eTreatmentClean(s))
    X=np.ndarray((41,1),dtype=np.double)
    for i in range(0,41):
        X[i,0]=(i-20.0)/2.0;
    X[2,0]=np.nan
    X[10,0]=np.nan

    for iT,T in enumerate(["Hats","Levels","DiscreteRC","DiscreteLC","iHats","BZ2","BZ3"]):

        CriticalValues=[ -6, -1, 3, 6, 8, 9 ]
        CleanLimits=[ -8, 10.5 ]
        nArtificials=art_c._nArtificialCount(len(CriticalValues),T)
        print("X=")
        print(X)
        print("T=",T)
        print("CriticalValues=",CriticalValues)
        print("CleanLimits=",CleanLimits)
        print("nArtificials=",nArtificials)
        print("Labels=",art_c.fArtificialLabels(len(CriticalValues),T))
        XA=art_c.fArtificials(X.flatten().tolist(),T,CriticalValues,CleanLimits,bShow=True,bShowInputs=True)
        #print("XA=",XA)
        Coef=2.0-4.0*np.random.rand(3,nArtificials)
        print("Coef=",Coef,type(Coef))
        print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
        XAS=art_c.fArtificialsScored(X.flatten().tolist(),T,CriticalValues,CleanLimits=CleanLimits,CoefficientsSet=Coef.tolist(),bShow=True,bShowInputs=True)
        #print("XAS=",XAS)
        print(type(XAS))


    Y=['']*41 #np.ndarray((41,1),dtype=str)
    for i in range(0,41):
        Y[i]=chr(65+i)
    Y[2]=''
    Y[10]=''
    Y=pl.DataFrame({'y':Y})


    print("Y=")
    print(Y)
    print(Y.to_numpy().tolist())
    T='Categorical'
    CriticalValues=[['A','D'],['e','d'],['X','Y','Z','G','x','y']]
    print("Treatment='Categorical' with CriticalValues="+str(CriticalValues))
    print("YA=")
    YA,YALabels=art_c.fArtificials(Y.to_numpy().flatten().tolist(),T,CriticalValues,bShow=True,bShowInputs=True)
    nArtificials=art_c._nArtificialCount(len(CriticalValues),T)
    Coef=2.0-4.0*np.random.rand(3,nArtificials)
    print(type(YA))
    #YS=Y.hstack(pl.DataFrame(YA))
    #print(YS)
    print("Treatment="+T+" with CriticalValues="+str(CriticalValues))
    print("Coef=",Coef,type(Coef))
    print("Coef=",Coef.tolist(),type(Coef))

    print("YAS=")
    YAS=art_c.fArtificialsScored(Y.to_numpy().flatten().tolist(),T,CriticalValues,CoefficientsSet=Coef.tolist(),bShow=True,bShowInputs=True)
    print("Treatment='Categorical' with CriticalValues="+str(CriticalValues))
    print("Coef=",Coef,type(Coef))
    print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
    #YAS=Y.hstack(pl.DataFrame(YAS))
    exit()



    Y=[0]*41 #np.ndarray((41,1),dtype=str)
    for i in range(0,41):
        Y[i]=(65+i)
    Y[2]=np.nan
    Y[10]=np.nan
    Y=pl.DataFrame({'y':Y})


    print("Y=")
    print(Y)
    T='CategoricalNumeric'
    CriticalValues=[[65, 69],[103,108],[110,112,114,115,118]]
    print("Treatment=" + T + " with CriticalValues="+str(CriticalValues))
    print("YA=")
    YA,YALabels=art_c.fArtificials(Y.to_numpy(),T,CriticalValues,bShow=True,bShowInputs=True)
    nArtificials=art_c._nArtificialCount(len(CriticalValues),T)
    Coef=2.0-4.0*np.random.rand(3,nArtificials)
    print(type(YA))
    #YS=Y.hstack(pl.DataFrame(YA))
    #print(YA)

    print("Treatment="+T+" with CriticalValues="+str(CriticalValues))
    print("Coef=",Coef,type(Coef))
    print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
    print("YAS=")
    YAS=art_c.fArtificialsScored(Y.to_numpy(),T,CriticalValues,CoefficientsSet=Coef.tolist(),bShow=True,bShowInputs=True)
    #YAS=Y.hstack(pl.DataFrame(YAS))
    #print(YAS)





