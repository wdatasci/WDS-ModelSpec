#!/usr/bin/env python3


import ArtificialsCythonWrapped as art_c

import numpy as np

np.set_printoptions(linewidth=np.inf)

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
        CleanLimits=np.array([[ -8, 10.5 ]],np.double)
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
        Coef=2.0-4.0*np.random.rand(3,nArtificials)
        print("Coef=",Coef,type(Coef))
        XAS=art_c.fArtificialsScored(X,T,CriticalValues,CleanLimits=CleanLimits,CoefficientSets=Coef)
        print("Labels=",art_c.fArtificialsScoredLabels(Coef.shape[0]))
        print("XAS=",XAS)
        print(type(XAS))





