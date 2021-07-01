// MatrixUtil.cpp : additional matrix functions

#include "ModelUtil.h"
#include "WDS\Comp\Matrix.h"
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

}

