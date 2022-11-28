#!/usr/bin/env python3


import Artificials_CythonWrapped as art_c
import Artificials_PurePython as art_p

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

        CriticalValues=np.array([[ -6, -1, 3, 6, 8, 9 ]],np.double)
        CleanLimits=np.array([[ -8, 9.5 ]],np.double)
        nArtificials=art_c._nArtificialCount(CriticalValues.shape[1],T)
        print("X=")
        print(X)
        print("T=",T)
        print("CriticalValues=",CriticalValues)
        print("CleanLimits=",CleanLimits)
        print("nArtificials=",nArtificials)
        XA=art_c.fArtificials(X,T,CriticalValues,CleanLimits)
        print("Labels=",art_c.fArtificialLabels(CriticalValues.shape[1],T))
        print("XA=",XA)
        XAP=art_p.fArtificials(X.flatten().tolist(),T,CriticalValues.flatten().tolist(),CleanLimits.flatten().tolist(),bShow=True,bShowInputs=True)
        for j,nm in enumerate(XAP[1]):
            print('Column difference for ',nm,' sum()=',np.sum(XA[nm].flatten()-XAP[0][j]))
        Coef=2.0-4.0*np.random.rand(3,nArtificials)
        print("Coef=",Coef,type(Coef))
        XAS=art_c.fArtificialsScored(X,T,CriticalValues,CleanLimits=CleanLimits,CoefficientsSet=Coef)
        print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
        print("XAS=",XAS)
        print(type(XAS))
        CoefL=[[0.0 for i in range(0,nArtificials)] for j in range(0,3)]
        for i in range(0,3):
            for j in range(0, nArtificials):
                CoefL[i][j]=Coef[i,j]
        print("CoefL=",CoefL)
        print("PurePython XAS=")
        XASP=art_p.fArtificialsScored(X.flatten().tolist(),T,CriticalValues.flatten().tolist(),CleanLimits=CleanLimits.flatten().tolist(),CoefficientsSet=CoefL,bShow=True,bShowInputs=True)
        for j,nm in enumerate(XASP[1]):
            print('Column difference for ',nm,' sum()=',np.sum(XAS[nm].flatten()-XASP[0][j]))


    Y=['']*41 #np.ndarray((41,1),dtype=str)
    for i in range(0,41):
        Y[i]=chr(65+i)
    Y[2]=''
    Y[10]=''
    Y=pl.DataFrame({'y':Y})


    print("Y=")
    print(Y)
    T='Categorical'
    CriticalValues=[['A','D'],['e','d'],['X','Y','Z','G','x','y']]
    print("Treatment='Categorical' with CriticalValues="+str(CriticalValues))
    YA=art_c.fArtificials(Y.to_numpy(),T,CriticalValues)
    nArtificials=art_c._nArtificialCount(len(CriticalValues),T)
    Coef=2.0-4.0*np.random.rand(3,nArtificials)
    CoefL=[[0.0 for i in range(0,nArtificials)] for j in range(0,3)]
    for i in range(0,3):
        for j in range(0, nArtificials):
            CoefL[i][j]=Coef[i,j]
    print("YA=",YA)
    print(type(YA))
    YS=Y.hstack(pl.DataFrame(YA))
    print(YS)
    print("YA (pure python)")
    YAP=art_p.fArtificials(Y.to_numpy().flatten().tolist(),T,CriticalValues,bShow=True,bShowInputs=True)
    for j,nm in enumerate(YAP[1]):
        print('Column difference for ',nm,' sum()=',np.sum(YA[nm].flatten()-YAP[0][j]))

    YAS=art_c.fArtificialsScored(Y.to_numpy(),T,CriticalValues,CoefficientsSet=Coef)
    print("Treatment='Categorical' with CriticalValues="+str(CriticalValues))
    print("Coef=",Coef,type(Coef))
    print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
    YASS=Y.hstack(pl.DataFrame(YAS))
    print(YASS)
    print("YAS (pure python)")
    YASP=art_p.fArtificialsScored(Y.to_numpy().flatten().tolist(),T,CriticalValues,CoefficientsSet=CoefL,bShow=True,bShowInputs=True)
    for j,nm in enumerate(YASP[1]):
        print('Column difference for ',nm,' sum()=',np.sum(YAS[nm].flatten()-YASP[0][j]))



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
    YA=art_c.fArtificials(Y.to_numpy(),T,CriticalValues)
    nArtificials=art_c._nArtificialCount(len(CriticalValues),T)
    Coef=2.0-4.0*np.random.rand(3,nArtificials)
    CoefL=[[0.0 for i in range(0,nArtificials)] for j in range(0,3)]
    for i in range(0,3):
        for j in range(0, nArtificials):
            CoefL[i][j]=Coef[i,j]
    print("YA=",YA)
    print(type(YA))
    YS=Y.hstack(pl.DataFrame(YA))
    print(YS)
    print('YA= (pure python)')
    YAP=art_p.fArtificials(Y.to_numpy().flatten().tolist(),T,CriticalValues,bShow=True,bShowInputs=True)
    for j,nm in enumerate(YAP[1]):
        print('Column difference for ',nm,' sum()=',np.sum(YA[nm].flatten()-YAP[0][j]))

    YAS=art_c.fArtificialsScored(Y.to_numpy(),T,CriticalValues,CoefficientsSet=Coef)
    print("Treatment='Categorical' with CriticalValues="+str(CriticalValues))
    print("Coef=",Coef,type(Coef))
    print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
    YASS=Y.hstack(pl.DataFrame(YAS))
    print(YASS)
    print('YAS (pure python)')
    YASP=art_p.fArtificialsScored(Y.to_numpy().flatten().tolist(),T,CriticalValues,CoefficientsSet=CoefL,bShow=True,bShowInputs=True)
    for j,nm in enumerate(YASP[1]):
        print('Column difference for ',nm,' sum()=',np.sum(YAS[nm].flatten()-YASP[0][j]))





