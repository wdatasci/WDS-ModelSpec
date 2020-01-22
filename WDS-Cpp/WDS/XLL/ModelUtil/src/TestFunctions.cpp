// TestFunctions.cpp : Simple test functions (can be stripped out)

#include "ModelUtil.h"
#include <string>
#include "xlcall.h"

using namespace xll;

#include "WDS\Comp\Matrix.h"
using namespace WDS::Comp::Matrix;
//#include "WDS\ModelSpec\Artificials.h"
//using namespace WDS::ModelSpec;

static AddIn XLL_WDS_Test_Matrix_Inv(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Test_Matrix_Inv", 4), L"WDS.Test.Matrix.Inv")
	.Arg(XLL_LPXLOPER, L"arg0", L"is a LPOPER")
	.Category(L"WDS.Test")
	.FunctionHelp(L"Huh?")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Test_Matrix_Inv(LPXLOPER12 arg0)
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
			if (nrows != ncols) {
				result = OPER12(L"Error, not square");
			}
			else {
				dMatrix A(nrows, ncols);
				mIndex mi = 0;
				mIndex mj = 0;

				for (mi = 0; mi < nrows; mi++) {
					for (mj = 0; mj < ncols; mj++) {
						i = int(mi) * ncols + int(mj);
						if (varg0.val.array.lparray[i].xltype == xltypeNum)
							A[mi, mj] = (double)(varg0.val.array.lparray[i].val.num);
						else
							A[mi, mj] = 0.0;
					}
				}

				dMatrix B = inv(A);

				result = OPER12(nrows, ncols);

				for (mi = 0; mi < nrows; mi++) {
					for (mj = 0; mj < ncols; mj++) {
						result(mi, mj) = B[mi, mj];
					}
				}
			}

		}
		else {
			result = OPER12(L"Error, xlretUncalced");
		}
	}
	catch (...) {
		result = OPER12(L"Error, in coercion or inverting");
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


static AddIn XLL_WDS_Test_Type(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Test_Type", 4), L"WDS.Test.Type")
	.Arg(XLL_WORD, L"arg0", L"is a WORD")
	.Arg(XLL_LPXLOPER, L"other", L"is a LPXLOPER12")
	.Category(L"WDS.Test")
	.FunctionHelp(L"Huh?")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Test_Type(WORD arg0, LPXLOPER12 arg1)
{
	const OPER oarg1(&arg1);

	std::wstring rv = L"Unk";

	if (arg1 == nullptr) {
		rv = L"arg1 is nullptr";
	}
	else {
		try {
			switch (arg1->xltype)
			{
			case xltypeNum:
				rv = L"Num";
				break;
			case xltypeStr:
				rv = L"Str";
				break;
			case xltypeBool:
				rv = L"Bool";
				break;
			case xltypeErr:
				rv = L"Err";
				break;
			case xltypeMissing:
				rv = L"Missing";
				break;
			case xltypeNil:
				rv = L"Nil";
				break;
			case xltypeMulti:
				rv = L"Multi";
				break;
			case xltypeRef:
				rv = L"Ref";
				break;
			case xltypeSRef:
				rv = L"SRef";
				break;
			default:
				rv = L"Unhandled Type, " + std::to_wstring(arg1->xltype);
				break;
			}
		}
		catch (std::exception e) {
			std::string ew = e.what();
			rv = std::wstring(ew.begin(), ew.end());
		}
	}

	static OPER result;
	result = rv;
	return &result;

}


static AddIn XLL_WDS_Test_Array_20_10(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Test_Array_20_10", 4), L"WDS.Test.Array_20_10")
	.Arg(XLL_WORD, L"arg0", L"is a WORD")
	.Arg(XLL_LPXLOPER, L"other", L"is a LPXLOPER12")
	.Category(L"WDS.Test")
	.FunctionHelp(L"Huh?")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Test_Array_20_10(WORD arg0, LPXLOPER12 arg1)
{
	//const OPER oarg1(&arg1);

	static OPER result;
	result = OPER(20, 10);

	int i, j;
	for (i = 0; i < 20; i++) {
		for (j = 0; j < 10; j++) {
			result(i, j) = (double)(i + j + .31);
		}
	}

	result(10, 4) = L"Hey";

	return &result;

}



static AddIn XLL_WDS_Test_DoubleArrayFrom(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Test_DoubleArrayFrom", 4), L"WDS.Test.DoubleArrayFrom")
	.Arg(XLL_WORD, L"arg0", L"is a WORD")
	.Arg(XLL_LPXLOPER, L"other", L"is a LPXLOPER12")
	.Category(L"WDS.Test")
	.FunctionHelp(L"Huh?")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Test_DoubleArrayFrom(WORD arg0, LPXLOPER12 arg1)
{
	int i, j, nrows, ncols;

	static OPER result;

	if (arg1->xltype == xltypeMulti) {
		nrows = arg1->val.array.rows;
		ncols = arg1->val.array.columns;
		result = OPER(nrows, ncols);
		for (i = 0; i < nrows; i++)
			for (j = 0; j < ncols; j++) {
				if (arg1->val.array.lparray[i*ncols + j].xltype == xltypeNum)
					result(i, j) = arg1->val.array.lparray[i*ncols + j];
			}
	}
	else if (arg1->xltype == xltypeSRef) {

		XLOPER12 varg1;

		int rc = Excel12f(xlCoerce, &varg1, 2, arg1, TempInt12(xltypeMulti));
		if (rc != xlretUncalced) {

			nrows = varg1.val.array.rows;
			ncols = varg1.val.array.columns;
			result = OPER(nrows, ncols);

			for (i = 0; i < nrows; i++)
				for (j = 0; j < ncols; j++) {
					//result(i, j) = varg2(i, j);
					if (varg1.val.array.lparray[i*ncols + j].xltype == xltypeNum)
						result(i, j) = varg1.val.array.lparray[i*ncols + j];
				}

		}
		Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
	}
	else {
		result = OPER(1, 1);
		result.xltype = xltypeMulti | xlbitXLFree;
		result(0, 0) = "Huh?";
	}

	return &result;

}



