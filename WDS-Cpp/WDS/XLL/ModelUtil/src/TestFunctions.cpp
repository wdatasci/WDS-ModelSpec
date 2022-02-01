// TestFunctions.cpp : Simple test functions (can be stripped out)

#include "ModelUtil.h"
#include <string>
#include "xlcall.h"

using namespace xll;

#include "WDS\Comp\Matrix.h"
using namespace WDS::Comp::Matrix;

static AddIn XLL_WDS_Test_Matrix_Inv(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Test_Matrix_Inv", 4), L"WDS.Test.Matrix.Inv")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPOPER")
	.Category(L"WDS.Test")
	.FunctionHelp(L"Huh?")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Test_Matrix_Inv(LPXLOPER12 Arg0)
{

	int i, j, nrows, ncols;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(Arg0);
	LPXLOPER12 cmArg0=nullptr;
	bool bWasArg0Coerced = false;

	try {

		if (lCoerceToMultiIfNecessary(Arg0, cmArg0, bWasArg0Coerced) == 0) {

			nrows = cmArg0->val.array.rows;
			ncols = cmArg0->val.array.columns;
			if (nrows != ncols) {
				result = new OPER12(L"Error, not square");
			}
			else {
				dMatrix A(nrows, ncols);
				mIndex mi = 0;
				mIndex mj = 0;

				for (mi = 0; mi < nrows; mi++) {
					for (mj = 0; mj < ncols; mj++) {
						i = int(mi) * ncols + int(mj);
						if (cmArg0->val.array.lparray[i].xltype == xltypeNum)
							A[mi, mj] = (double)(cmArg0->val.array.lparray[i].val.num);
						else
							A[mi, mj] = 0.0;
					}
				}

				dMatrix B = inv(A);

				result = new OPER12(nrows, ncols);

				for (mi = 0; mi < nrows; mi++) {
					for (mj = 0; mj < ncols; mj++) {
						(*result)(mi, mj) = B[mi, mj];
					}
				}
			}

		}
		else {
			if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
			result = new OPER12(L"Error, in coerce in Matrix.Inv");
		}
	}
	catch (...) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coerce or matrix inversion.");
	}

	lFreeIfNecessary(cmArg0, bWasArg0Coerced);

	if (result != NULL) (*result).xltype = (*result).xltype | xlbitXLFree;

	return result;


}


static AddIn XLL_WDS_Test_Type(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Test_Type", 4), L"WDS.Test.Type")
	.Arg(XLL_WORD, L"arg0", L"is a WORD")
	.Arg(XLL_LPXLOPER, L"other", L"is a LPXLOPER12")
	.Category(L"WDS.Test")
	.FunctionHelp(L"Huh?")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
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

	LPOPER result = new OPER(rv);

	if (result != NULL) (*result).xltype = (*result).xltype | xlbitXLFree;

	return result;
}




