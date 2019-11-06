// ModelUtil.cpp: Defines a main set of exported functions for the XLL

#include "ModelUtil.h"
#include <string>
#include "xlcall.h"

using namespace xll;

#include "WDSMatrix.h"
using namespace WDSMatrix;

static AddIn XLL_WDS_Comp_Matrix_RowNormed(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Comp_Matrix_RowNormed", 4), L"WDS.Comp.Matrix.RowNormed")
	.Arg(XLL_LPXLOPER, L"arg0", L"is a LPOPER")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Row Normalization - Each target row is the unit sum normalized version of the source.")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Comp_Matrix_RowNormed(LPXLOPER12 arg0)
{

	int i, j, nrows, ncols;

	static OPER12 result;
	XLOPER12 varg0;
	int rc;

	try {

		rc = Excel12f(xlCoerce, &varg0, 2, arg0, TempInt12(xltypeMulti));

		if (rc != xlretUncalced) {

			nrows = varg0.val.array.rows;
			ncols = varg0.val.array.columns;

			dMatrix A(nrows, ncols);
			mIndex mi = 0;
			mIndex mj = 0;

			double s, t;
			for (mi = 0; mi < nrows; mi++) {
				s = 0.0;
				for (mj = 0; mj < ncols; mj++) {
					i = int(mi) * ncols + int(mj);
					if (varg0.val.array.lparray[i].xltype == xltypeNum)
						t = (double)(varg0.val.array.lparray[i].val.num);
					else
						t = 0.0;
					A[mi, mj] = t;
					s += t;
				}
				if (fabs(s) > 1e-6) {
					for (mj = 0; mj < ncols; mj++)
						A[mi, mj] /= s;
				}
			}

			result = OPER12(nrows, ncols);
			for (mi = 0; mi < nrows; mi++) {
				for (mj = 0; mj < ncols; mj++) {
					result(mi, mj) = A[mi, mj];
				}
			}

		}
		else {
			result = OPER12(L"Error, xlretUncalced");
		}
	}
	catch (...) {
		result = OPER12(L"Error, in coercion or row-normalization");
	}

	try {
		Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg0);
	}
	catch (...) {
		result = OPER12(L"Error, in xlFree of coercion product");
	}

	result.xltype = result.xltype | xlbitXLFree;

	return &result;


}



