#pragma once
// MatrixUtil.h : additional matrix functions

#include "ModelUtil.h"
#include "WDS\Comp\Matrix.h"

namespace WDS::Comp::Matrix {

	void RowNormInPlace(dMatrix& arg);
	
	

	dMatrix RowNorm(dMatrix& arg); 

	dMatrix NormedBaseOdds(int n, int m, int Offset, dMatrix& BaseOdds, dMatrix& Topology);

	dMatrix OffsetBaseOdds(int rowindex
		, int n
		, int m
		, int nbase
		, iMatrix& Offset
		, dMatrix& BaseOdds
		, dMatrix& Topology
	) ; 


	dMatrix ScoredAndNormedBaseOdds(int rowindex
		, int n
		, int m
		, int nbase
		, iMatrix& Offset
		, dMatrix& BaseOdds
		, dMatrix& Topology
		, bool bUseVs
		, iMatrix& ijs
		, dMatrix& vs
		, bool bUseTailFctor
		, dMatrix& TailFactor
		, int tail
		, int tail_cutoff); 



	dMatrix ScoredAndNormedBaseOddsWithPostFactor(int rowindex
		, int n
		, int m
		, int nbase
		, iMatrix& Offset
		, dMatrix& BaseOdds
		, dMatrix& Topology
		, bool bUseVs
		, iMatrix& ijs
		, dMatrix& vs
		, bool bUseP_Vs
		, iMatrix& p_ijs
		, dMatrix& p_vs
		, bool bUseTailFctor
		, dMatrix& TailFactor
		, int tail
		, int tail_cutoff);  

}

