// MatrixUtil.cpp : additional matrix functions

#include "MatrixUtil.h"
namespace WDS::Comp::Matrix {

	void RowNormInPlace(dMatrix& arg) {
		size_t nrows = arg.nrows();
		size_t ncols = arg.ncols();
		mIndex mi = 0;
		mIndex mj = 0;
		double s, t;
		for (mi = 0; mi < nrows; mi++) {
			s = 0.0;
			for (mj = 0; mj < ncols; mj++) {
				s += arg[mi, mj];
			}
			if (fabs(s) > 1e-6) {
				for (mj = 0; mj < ncols; mj++)
					arg[mi, mj] /= s;
			}
		}
	}

	dMatrix RowNorm(dMatrix& arg) {
		dMatrix out(arg);
		RowNormInPlace(out);
		return out;
	}

	dMatrix NormedBaseOdds(int n, int m, int Offset, dMatrix& BaseOdds, dMatrix& Topology) {
		dMatrix result = BaseOdds.submat(span(Offset * n, (Offset + 1) * n), span::all);
		result %= Topology;
		RowNormInPlace(result);
		return result;
	}

	dMatrix OffsetBaseOdds(int rowindex
		, int n
		, int m
		, int nbase
		, iMatrix& Offset
		, dMatrix& BaseOdds
		, dMatrix& Topology
	) {
		int _Offset = Offset.at(rowindex, 0);
		dMatrix result = BaseOdds(span(_Offset * n, (_Offset + 1) * n - 1), span(nbase * n, (nbase + 1) * n - 1));
		result %= Topology;
		return result;
	}


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
		, int tail_cutoff) {
		dMatrix result = OffsetBaseOdds(rowindex, n, m, nbase, Offset, BaseOdds, Topology);
		if (bUseTailFctor && (tail < tail_cutoff))
			result %= TailFactor;
		int nk = (int)vs.ncols();
		int i, j, k;
		if (bUseVs) {
			double v = 0.0;
			for (k = 0; k < nk; k++) {
				i = (int)ijs.at(0, k);
				j = (int)ijs.at(1, k);
				v = (double)vs.at(rowindex, k);
				result(i, j) *= exp(v);
			}
		}
		RowNormInPlace(result);
		return result;
	}



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
		, int tail_cutoff) {
		dMatrix result = OffsetBaseOdds(rowindex, n, m, nbase, Offset, BaseOdds, Topology);
		if (bUseTailFctor && (tail < tail_cutoff))
			result %= TailFactor;
		int nk = (int)vs.ncols();
		int i, j, k;
		if (bUseVs) {
			double v = 0.0;
			for (k = 0; k < nk; k++) {
				i = (int)ijs.at(0, k);
				j = (int)ijs.at(1, k);
				v = (double)vs.at(rowindex, k);
				result(i, j) *= exp(v);
			}
		}
		RowNormInPlace(result);
		if (bUseP_Vs) {
			nk = (int)p_vs.ncols();
			double v = 0.0;
			for (k = 0; k < nk; k++) {
				i = (int)p_ijs.at(0, k);
				j = (int)p_ijs.at(1, k);
				v = (double)p_vs.at(rowindex, k);
				result(i, j) *= v;
			}
		}
		return result;
	}

}

