/*
Copyright (c) 2019 Wypasek Data Science, Inc. (WDataSci, WDS)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

// ModelUtil.cpp: Defines a main set of exported functions for the XLL

#define EXCEL12
#include "ModelUtil.h"
#include <string>
#include "xlcall.h"
#include "oper.h"

using namespace xll;
using namespace std;

using namespace WDS::Comp::Matrix;

std::wstring pascal_string_to_wstring(wchar_t* str) {
	std::wstring rv = L"";
	size_t j;
	j = (size_t)str[0];
	if (j > 0) {
		rv = std::wstring(&str[1], j);
	}
	return rv;
}

int pascal_string_compare(wchar_t* str1, wchar_t* str2) {
	int n1 = (size_t)str1[0];
	int n2 = (size_t)str2[0];
	if (n1 == 0 && n2==0) return 0;
	if (n1==0 && n2 > 0) return -1;
	if (n1>0 && n2 ==0) return 1;
	for (int i = 1; i <= n1 && i <= n2; i++) {
		if (str1[i] < str2[i]) return -1;
		else if (str1[i] > str2[i]) return 1;
	}
	return 0;
}

std::wstring xltypeMulti_to_wstring(LPXLOPER12 arg0, size_t r, size_t c)
{
	std::wstring rv = L"";
	LPXLOPER12 varg1=nullptr;
	size_t nrows, ncols;
	int rc;
	bool bThrowError = true;
	if (arg0 != nullptr && arg0->xltype == xltypeMulti) {
		try {
			nrows = (size_t) arg0->val.array.rows;
			ncols = (size_t) arg0->val.array.columns;
			if (r < nrows && c < ncols) {
				bThrowError = false;
				try {
					switch (arg0->val.array.lparray[r*ncols+c].xltype) {
					case xltypeErr:
					case xltypeNil:
					case xltypeMissing:
						rv = L"";
						break;
					case xltypeInt:
					case xltypeNum:
						try {
							rv = std::to_wstring(arg0->val.array.lparray[r*ncols+c].val.num);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					case xltypeStr:
						try {
							rv = pascal_string_to_wstring(arg0->val.array.lparray[r*ncols+c].val.str);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					default:
						varg1 = new XLOPER12();
						rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeStr));
						if (rc == xlretSuccess) {
							try {
								rv = pascal_string_to_wstring((wchar_t*)(varg1->val.str));
							}
							catch (...) {
								bThrowError = true;
							}
						}
						Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
						break;
					}
				}
				catch (...) {
					bThrowError = true;
				}
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	if (bThrowError) throw std::exception("Error in xltypeMulti_to_wstring");
	return rv;
}

double xltypeMulti_to_double(LPXLOPER12 arg0, size_t r, size_t c, bool bStrict, double defv)
{
	double rv = 0.0;
	LPXLOPER12 varg1=nullptr;
	size_t nrows, ncols;
	int rc;
	bool bThrowError = true;
	if (arg0 != nullptr && arg0->xltype == xltypeMulti) {
		try {
			nrows = (size_t)arg0->val.array.rows;
			ncols = (size_t)arg0->val.array.columns;
			if (r < nrows && c < ncols) {
				bThrowError = false;
				try {
					switch (arg0->val.array.lparray[r*ncols + c].xltype) {
					case xltypeInt:
					case xltypeNum:
						try {
							rv = (double)(arg0->val.array.lparray[r*ncols + c].val.num);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					case xltypeMissing:
					case xltypeErr:
					case xltypeNil:
						bThrowError = true;
						break;
					case xltypeBool:
						if (arg0->val.array.lparray[r*ncols + c].val.xbool)
							rv = 1.0;
						else
							rv = 0.0;
						break;
					case xltypeStr:
						try {
							rv = std::stod(pascal_string_to_wstring(arg0->val.array.lparray[r*ncols + c].val.str));
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					default:
						varg1 = new XLOPER12();
						rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeNum));
						if (rc == xlretSuccess) {
							try {
								rv = (double)(varg1->val.num);
							}
							catch (...) {
								bThrowError = true;
							}
						}
						Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
						break;
					}
				}
				catch (...) {
					bThrowError = true;
				}
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	if (bStrict && bThrowError) throw std::exception("Error in xltypeMulti_to_double");
	if (bThrowError) rv = defv;
	return rv;
}

long xltypeMulti_to_long(LPXLOPER12 arg0, size_t r, size_t c, bool bStrict, long defv)
{
	long rv = 0;
	LPXLOPER12 varg1=nullptr;
	size_t nrows, ncols;
	int rc;
	bool bThrowError = true;
	if (arg0 != nullptr && arg0->xltype == xltypeMulti) {
		try {
			nrows = (size_t) arg0->val.array.rows;
			ncols = (size_t) arg0->val.array.columns;
			if (r < nrows && c < ncols) {
				bThrowError = false;
				try {
					switch (arg0->val.array.lparray[r*ncols + c].xltype) {
					case xltypeInt:
					case xltypeNum:
						try {
							rv = (long)(arg0->val.array.lparray[r*ncols + c].val.num);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					case xltypeMissing:
					case xltypeErr:
					case xltypeNil:
						bThrowError = true;
						break;
					case xltypeBool:
						if (arg0->val.array.lparray[r*ncols + c].val.xbool)
							rv = 1;
						else
							rv = 0;
						break;
					case xltypeStr:
						try {
							rv = std::stol(pascal_string_to_wstring(arg0->val.array.lparray[r*ncols + c].val.str));
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					default:
						varg1 = new XLOPER12();
						rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeNum));
						if (rc == xlretSuccess) {
							try {
								rv = (long)(varg1->val.num);
							}
							catch (...) {
								bThrowError = true;
							}
						}
						Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
						break;
					}
				}
				catch (...) {
					bThrowError = true;
				}
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	if (bStrict && bThrowError) throw std::exception("Error in xltypeMulti_to_long");
	if (bThrowError) rv = defv;
	return rv;
}

std::wstring LPOPER_to_wstring(LPXLOPER12 arg0, size_t r, size_t c)
{
	std::wstring rv = L"";
	bool bThrowError = false;
	LPXLOPER12 varg1 = nullptr;
	size_t nrows, ncols;
	int rc;
	if (arg0 != nullptr) {
		try {
			switch (arg0->xltype)
			{
			case xltypeStr:
				rv = pascal_string_to_wstring(arg0->val.str);
				break;
			case xltypeInt:
			case xltypeNum:
				rv = std::to_wstring(arg0->val.num);
				break;
			case xltypeBool:
				if (arg0->val.xbool) rv = L"TRUE";
				else rv = L"FALSE";
				break;
			case xltypeMissing:
				//rv = L"Missing";
				rv = L"";
				break;
			case xltypeErr:
				rv = L"";
				break;
			case xltypeNil:
				rv = L"";
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_wstring(arg0, r, c);
				break;
			case xltypeSRef:
			case xltypeRef:
				try {
					varg1 = new XLOPER12();
					rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeMulti));
					if (rc == xlretSuccess) {
						try {
							rv = xltypeMulti_to_wstring(varg1, r, c);
						}
						catch (...) {
							bThrowError = true;
						}
					}
					Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
				}
				catch (...) {
					bThrowError = true;
				}
				break;
			default:
				bThrowError = true;
				break;
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	else {
		bThrowError = true;
	}
	if (bThrowError) throw std::exception("Error in LPOPER_to_wstring");
	return rv;
}

double LPOPER_to_double(LPXLOPER12 arg0, size_t r, size_t c)
{
	double rv = 0.0;
	bool bThrowError = false;
	LPXLOPER12 varg1 = nullptr;
	size_t nrows, ncols;
	int rc;
	if (arg0 != nullptr) {
		try {
			switch (arg0->xltype)
			{
			case xltypeStr:
				rv = std::stod(pascal_string_to_wstring(arg0->val.str));
				break;
			case xltypeInt:
			case xltypeNum:
				rv = (double)(arg0->val.num);
				break;
			case xltypeBool:
				if (arg0->val.xbool) rv = 1.0;
				else rv = 0.0;
				break;
			case xltypeMissing:
				rv = nan(""); //NAN
				break;
			case xltypeErr:
				rv = nan(""); //NAN;
				break;
			case xltypeNil:
				rv = nan(""); //NAN;
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_double(arg0, r, c,false,nan(""));
				break;
			case xltypeSRef:
			case xltypeRef:
				try {
					varg1 = new XLOPER12();
					rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeMulti));
					if (rc == xlretSuccess) {
						try {
							rv = xltypeMulti_to_double(varg1, r, c,false,nan(""));
						}
						catch (...) {
							bThrowError = true;
						}
					}
					Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
				}
				catch (...) {
					bThrowError = true;
				}
				break;
			default:
				bThrowError = true;
				break;
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	else {
		bThrowError = true;
	}
	if (bThrowError) rv = nan(""); 
	return rv;
}

long LPOPER_to_long(LPXLOPER12 arg0, size_t r, size_t c)
{
	long rv = 0;
	bool bThrowError = false;
	LPXLOPER12 varg1 = nullptr;
	size_t nrows, ncols;
	int rc;
	if (arg0 != nullptr) {
		try {
			switch (arg0->xltype)
			{
			case xltypeStr:
				rv = std::stol(pascal_string_to_wstring(arg0->val.str));
				break;
			case xltypeInt:
			case xltypeNum:
				rv = (long)(arg0->val.num);
				break;
			case xltypeBool:
				if (arg0->val.xbool) rv = 1;
				else rv = 0;
				break;
			case xltypeMissing:
				rv = LONG_MAX;
				break;
			case xltypeErr:
				rv = LONG_MAX;
				break;
			case xltypeNil:
				rv = LONG_MAX;
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_long(arg0, r, c,false,LONG_MAX);
			case xltypeSRef:
			case xltypeRef:
				try {
					varg1 = new XLOPER12();
					rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeMulti));
					if (rc == xlretSuccess) {
						try {
							rv = xltypeMulti_to_long(varg1, r, c,false,LONG_MAX);
						}
						catch (...) {
							bThrowError = true;
						}
					}
					Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
				}
				catch (...) {
					bThrowError = true;
				}
				break;
			default:
				bThrowError = true;
				break;
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	else {
		bThrowError = true;
	}
	if (bThrowError) rv = LONG_MAX;
	return rv;
}




long LPOPER_to_bool(LPXLOPER12 arg0, size_t r, size_t c)
{
	bool rv = false;
	bool bThrowError = false;
	LPXLOPER12 varg1 = nullptr;
	size_t nrows, ncols;
	const wchar_t* TRUEWORDS[] = { L"TRUE",L"T",L"1",L"true",L"t",L"YES",L"Y",L"yes",L"y" };
	wstring tmpstring;
	int rc;
	if (arg0 != nullptr) {
		try {
			switch (arg0->xltype)
			{
			case xltypeStr:
				tmpstring = pascal_string_to_wstring(arg0->val.str);
				for (int i = 0; i < 9; i++) {
					if (tmpstring.compare(TRUEWORDS[i]) == 0)
						return true;
				}
				break;
			case xltypeInt:
			case xltypeNum:
				rv = (bool)(arg0->val.num);
				break;
			case xltypeBool:
				if (arg0->val.xbool) rv = 1;
				else rv = 0;
				break;
			case xltypeMissing:
			case xltypeErr:
			case xltypeNil:
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_long(arg0, r, c,false,LONG_MAX);
			case xltypeSRef:
			case xltypeRef:
				try {
					varg1 = new XLOPER12();
					rc = Excel12f(xlCoerce, varg1, 2, arg0, TempInt12(xltypeBool));
					if (rc == xlretSuccess) {
							rv = varg1->val.xbool;
					}
					Excel12f(xlFree, 0, 1, (LPXLOPER12)varg1);
				}
				catch (...) {
					bThrowError = true;
				}
				break;
			default:
				bThrowError = true;
				break;
			}
		}
		catch (...) {
			bThrowError = true;
		}
	}
	else {
		bThrowError = true;
	}
	if (bThrowError) rv = false;
	return rv;
}







iMatrix iMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, long defv, bool bLimitRows, long RowLimit, bool bLimitColumns, long ColumnLimit) {
	LPXLOPER12 cmArg = nullptr;
	bool bWasArgCoerced = false;
	if (lCoerceToMultiIfNecessary(Arg, cmArg, bWasArgCoerced) != xlretSuccess)
		throw exception("Failed xlCoerce");
	try {
		mIndex mi = 0;
		mIndex mj = 0;
		int nrows = (int) cmArg->val.array.rows;
		int ncols = (int) cmArg->val.array.columns;
		if (bLimitRows && nrows > RowLimit) nrows = (int) RowLimit;
		if (bLimitColumns && ncols > ColumnLimit) ncols = (int) ColumnLimit;
		iMatrix result(nrows, ncols);
		for (mj = 0; mj < ncols; mj++)
			for (mi = 0; mi < nrows; mi++)
				result[mi, mj] = xltypeMulti_to_long(cmArg, mi.ast(), mj.ast(), bStrict, defv);
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		return result;
	}
	catch (exception& e) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		throw std::exception("iMatrixFromLPXLOPER Error"); 
	}
	lFreeIfNecessary(cmArg, bWasArgCoerced);
	return iMatrix(1, 1);
}


iMatrix iMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, long defv) {
	return iMatrixFromLPXLOPER(Arg, bStrict, defv, false, 0, false, 0);
}


dMatrix dMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, long defv, bool bLimitRows, long RowLimit, bool bLimitColumns, long ColumnLimit) {
	LPXLOPER12 cmArg = nullptr;
	bool bWasArgCoerced = false;
	if (lCoerceToMultiIfNecessary(Arg, cmArg, bWasArgCoerced) != xlretSuccess)
		throw exception("Failed xlCoerce");
	try {
		mIndex mi = 0;
		mIndex mj = 0;
		int nrows = (int) cmArg->val.array.rows;
		int ncols = (int) cmArg->val.array.columns;
		if (bLimitRows && nrows > RowLimit) nrows = (int) RowLimit;
		if (bLimitColumns && ncols > ColumnLimit) ncols = (int) ColumnLimit;
		dMatrix result(nrows, ncols);
		for (mj = 0; mj < ncols; mj++)
			for (mi = 0; mi < nrows; mi++)
				result[mi, mj] = xltypeMulti_to_double(cmArg, mi.ast(), mj.ast(), bStrict, defv);
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		return result;
	}
	catch (exception& e) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		throw std::exception("dMatrixFromLPXLOPER Error"); 
	}
	return dMatrix(1, 1);
}


static AddIn XLL_WDS_Comp_zzzInternal_SubMatrix(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_zzzInternal_SubMatrix", 4), L"WDS.Comp.zzzInternal.SubMatrix")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LONG, L"direction", L"is a 0/1 indicator for 0-Across Rows (vertical) or 1-Across Columns (horizontal)")
	.Arg(XLL_LONG, L"startrow", L"is the 1-Based beginrowng row (outside of limits defaults to input size).")
	.Arg(XLL_LONG, L"endrow", L"is the 1-Based ending row (outside of limits defaults to input size).")
	.Arg(XLL_LONG, L"startcolumn", L"is the 1-Based beginrowng column (outside of limits defaults to input size).")
	.Arg(XLL_LONG, L"endcolumn", L"is the 1-Based ending column(outside of limits defaults to input size).")
	.Category(L"WDS.Comp.zzzInternal")
	.FunctionHelp(L"SubMatrix - A non-volatile sub-matrix of a rectangular object.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_zzzInternal_SubMatrix(LPXLOPER12 Arg0, long direction, long startrow, long endrow, long startcolumn, long endcolumn)
{

	int nrows, ncols;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(Arg0);
	LPXLOPER12 cmArg0 = nullptr;
	bool bWasArg0Coerced = false;
	LPXLOPER12 cmOpts = nullptr;
	bool bWasOptsCoerced = false;
	int rc;

	try {

		if (lCoerceToMultiIfNecessary(Arg0, cmArg0, bWasArg0Coerced) != xlretSuccess)
			throw exception("Failed xlCoerce");

		nrows = (int) cmArg0->val.array.rows;
		ncols = (int) cmArg0->val.array.columns;

		if (startrow == LONG_MAX) startrow = 1;
		else if (startrow <= 0) startrow = 1;
		else if (startrow > nrows) startrow = nrows + 1;
		if (endrow == LONG_MAX) endrow = nrows;
		else if (endrow > nrows) endrow = nrows;

		if (startcolumn == LONG_MAX) startcolumn = 1;
		else if (startcolumn <= 0) startcolumn = 1;
		else if (startcolumn > ncols) startcolumn = ncols + 1;
		if (endcolumn == LONG_MAX) endcolumn = ncols;
		else if (endcolumn > ncols) endcolumn = ncols;

		startrow -= 1;
		startcolumn -= 1;

		if (direction == 0) {
			result = new OPER12(endrow - startrow, endcolumn - startcolumn);
			int i, j, ri, rj, ij;
			for (rj = 0, j = startcolumn; j < endcolumn; rj++, j++) {
				for (ri = 0, i = startrow; i < endrow; ri++, i++) {
					ij = i * ncols + j;
					switch (cmArg0->val.array.lparray[ij].xltype) {
					case xltypeInt:
					case xltypeNum:
						(*result)(ri, rj) = cmArg0->val.array.lparray[ij].val.num;
						break;
					case xltypeNil:
					case xltypeMissing:
					case xltypeErr:
						//(*result)(ri, rj) = cmArg0->val.array.lparray[ij].val.err;
						//(*result)(ri, rj) = OPER();
						break;
					case xltypeBool:
						(*result)(ri, rj) = cmArg0->val.array.lparray[ij].val.xbool;
						break;
					case xltypeStr:
						try {
						wstring tmpstring = L"";
							tmpstring = pascal_string_to_wstring(cmArg0->val.array.lparray[ij].val.str);
							(*result)(ri, rj) = tmpstring;
						}
						catch (...) {
						}
						break;
					default:
						break;
					}
				}
			}
		}
		else {
			result = new OPER12(endcolumn - startcolumn, endrow - startrow);
			int i, j, ri, rj;
			for (rj = 0, j = startcolumn; j < endcolumn; rj++, j++) {
				for (ri = 0, i = startrow; i < endrow; ri++, i++) {
					(*result)(rj, ri) = xltypeMulti_to_double(cmArg0, i, j, false, 0.0);
				}
			}
		}

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sub matrix");
	}

	lFreeIfNecessary(cmArg0, bWasArg0Coerced);
	lFreeIfNecessary(cmOpts, bWasOptsCoerced);

	result->xltype = result->xltype | xlbitXLFree;

	return result;

}




static AddIn XLL_WDS_Comp_Matrix_SubMatrix(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_SubMatrix", 4), L"WDS.Comp.Matrix.SubMatrix")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LONG, L"direction", L"is a 0/1 indicator for 0-Across Rows (vertical) or 1-Across Columns (horizontal)")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional array of {MaxRows}, {BeginRow, EndRow}, or {BeginRow,EndRow,BeginColumn,EndColumn}")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"SubMatrix - A non-volatile sub-matrix of a rectangular object.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_SubMatrix(LPXLOPER12 Arg0, long direction, LPXLOPER12 Opts)
{

	long beginrow = 0, endi = -1, beginj = 0, endj = -1;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	try {
		beginrow = LONG_MAX;
		endi = LONG_MAX;
		beginj = LONG_MAX;
		endj = LONG_MAX;

		if (!useless_LPXLOPER(Opts)) {

			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			if (lOpts.n_elem == 1) {
				endi = lOpts.at(0);
			}
			else if (lOpts.n_elem == 2) {
				beginrow = lOpts.at(0);
				endi = lOpts.at(1);
			}
			else if (lOpts.n_elem == 4) {
				beginrow = lOpts.at(0);
				endi = lOpts.at(1);
				beginj = lOpts.at(2);
				endj = lOpts.at(3);
			}
		}

		result = WDS_Comp_zzzInternal_SubMatrix(Arg0, direction, beginrow, endi, beginj, endj);

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sum across");
		result->xltype = result->xltype | xlbitXLFree;
	}

	return result;

}



static AddIn XLL_WDS_Comp_Matrix_Rows(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_Rows", 4), L"WDS.Comp.Matrix.Rows")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LPXLOPER, L"Ind", L"is a (1-based) single value or array of {SingleRowIndex}, {BeginRow, EndRow}, or {BeginRow,EndRow,BeginColumn,EndColumn}")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional maximum number of columns.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Rows - A subset of the rows of a rectangular object.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_Rows(LPXLOPER12 Arg0, LPXLOPER12 Ind, LPXLOPER12 Opts)
{

	long beginrow = LONG_MAX, endrow = LONG_MAX, begincol = LONG_MAX, endcol = LONG_MAX;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	require_usual_suspect_LPXLOPER(Ind);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	try {

		if (!useless_LPXLOPER(Ind)) {

			iMatrix lInd = iMatrixFromLPXLOPER(Ind, true, 0);
			if (lInd.n_elem == 1) {
				beginrow = lInd.at(0);
				endrow = lInd.at(0);
			}
			else if (lInd.n_elem == 2) {
				beginrow = lInd.at(0);
				endrow = lInd.at(1);
			}
			else if (lInd.n_elem == 4) {
				beginrow = lInd.at(0);
				endrow = lInd.at(1);
				begincol = lInd.at(2);
				endcol = lInd.at(3);
			}
		}

		if (!useless_LPXLOPER(Opts)) {
			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			long tmp = lOpts(0, 0);
			if (tmp == 0) {
				result = new OPER12();
				result->xltype = result->xltype | xlbitXLFree;
				return result;
			}
			if (begincol == LONG_MAX) {
				begincol = 1;
				endcol = tmp;
			} else if (endcol - begincol + 1 > tmp)
				endcol = begincol + tmp - 1;
		}

		result = WDS_Comp_zzzInternal_SubMatrix(Arg0, 0, beginrow, endrow, begincol, endcol);

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sum across rows");
		result->xltype = result->xltype | xlbitXLFree;
	}

	return result;

}



static AddIn XLL_WDS_Comp_Matrix_Columns(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_Columns", 4), L"WDS.Comp.Matrix.Columns")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LPXLOPER, L"Ind", L"is a (1-based) single value or array of {SingleColumnIndex}, {BeginColumn, EndColumn}, or {BeginRow,EndRow,BeginColumn,EndColumn}")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional maximum number of rows.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Columns - A subset of the columns of a rectangular object.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_Columns(LPXLOPER12 Arg0, LPXLOPER12 Ind, LPXLOPER12 Opts)
{

	long beginrow = LONG_MAX, endrow = LONG_MAX, begincol = LONG_MAX, endcol = LONG_MAX;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	require_usual_suspect_LPXLOPER(Ind);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	try {

		if (!useless_LPXLOPER(Ind)) {
			iMatrix lInd = iMatrixFromLPXLOPER(Ind, true, 0);
			if (lInd.n_elem == 1) {
				begincol = lInd.at(0);
				endcol = lInd.at(0);
			}
			else if (lInd.n_elem == 2) {
				begincol = lInd.at(0);
				endcol = lInd.at(1);
			}
			else if (lInd.n_elem == 4) {
				beginrow = lInd.at(0);
				endrow = lInd.at(1);
				begincol = lInd.at(2);
				endcol = lInd.at(3);
			}
		}

		if (!useless_LPXLOPER(Opts)) {
			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			long tmp = lOpts(0, 0);
			if (tmp == 0) {
				result = new OPER12();
				result->xltype = result->xltype | xlbitXLFree;
				return result;
			}
			if (beginrow == LONG_MAX) {
				beginrow = 1;
				endrow = tmp;
			} else if (endrow - beginrow + 1 > tmp)
				endrow = beginrow + tmp - 1;
		}

		result = WDS_Comp_zzzInternal_SubMatrix(Arg0, 0, beginrow, endrow, begincol, endcol);

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sum across rows");
		result->xltype = result->xltype | xlbitXLFree;
	}

	return result;

}


static AddIn XLL_WDS_Comp_Matrix_ColumnSet(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_ColumnSet", 4), L"WDS.Comp.Matrix.ColumnSet")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a rectangular object.")
	.Arg(XLL_LPXLOPER, L"ColumnSet", L"is a vector of 1-Based column indices.")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional row limit.")
	.Category(L"WDS.Comp.Matrix")
	.FunctionHelp(L"ColumnSet - A non-volatile sub-matrix of a rectangular object.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_ColumnSet(LPXLOPER12 Arg0, LPXLOPER12 ColumnSet, LPXLOPER12 Opts)
{

	int nrows, ncols;
	long beginrow = LONG_MAX, endrow = LONG_MAX, begincol = LONG_MAX, endcol = LONG_MAX;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	require_usual_suspect_LPXLOPER(ColumnSet);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	LPXLOPER12 cmArg0 = nullptr;
	bool bWasArg0Coerced = false;
	bool bWasArg0SRef = false;
	LPXLOPER12 cmOpts = nullptr;
	bool bWasOptsCoerced = false;

	try {

		require_usual_suspect_LPXLOPER(Arg0);
		require_usual_suspect_LPXLOPER(ColumnSet);

		if (lCoerceToMultiIfNecessary(Arg0, cmArg0, bWasArg0Coerced) != xlretSuccess)
			throw exception("Failed xlCoerce");
		nrows = (int) cmArg0->val.array.rows;
		ncols = (int) cmArg0->val.array.columns;
		beginrow = 1;
		endrow = nrows;

		if (!useless_LPXLOPER(Opts)) {
			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			long tmp = lOpts(0, 0);
			if (tmp == 0) {
				result = new OPER12();
				result->xltype = result->xltype | xlbitXLFree;
				return result;
			}
			if (endrow > tmp) 
				endrow = tmp;
		}


		iMatrix lColumnSet = iMatrixFromLPXLOPER(ColumnSet, true, 0);

		int rNCols = lColumnSet.n_elem;

		beginrow -=1;

		result = new OPER12(endrow - beginrow, rNCols);
		int i, j, ri, rj, ij;
		for (rj = 0; rj < rNCols; rj++) {
			j = lColumnSet.at(rj);
			if (j >= 1 && j <= ncols) {
				j -= 1;
				for (ri = 0, i = beginrow; i < endrow; ri++, i++) {
					ij = i * ncols + j;
					switch (cmArg0->val.array.lparray[ij].xltype) {
					case xltypeInt:
					case xltypeNum:
						(*result)(ri, rj) = cmArg0->val.array.lparray[ij].val.num;
						break;
					case xltypeNil:
					case xltypeMissing:
					case xltypeErr:
						//(*result)(ri, rj) = cmArg0->val.array.lparray[ij].val.err;
						//(*result)(ri, rj) = OPER();
						break;
					case xltypeBool:
						(*result)(ri, rj) = cmArg0->val.array.lparray[ij].val.xbool;
						break;
					case xltypeStr:
						try {
							wstring tmpstring = L"";
							tmpstring = pascal_string_to_wstring(cmArg0->val.array.lparray[ij].val.str);
							(*result)(ri, rj) = tmpstring;
						}
						catch (...) {
						}
						break;
					default:
						break;
					}
				}
			}
		}

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sub matrix");
	}

	lFreeIfNecessary(cmArg0, bWasArg0Coerced);
	lFreeIfNecessary(cmOpts, bWasOptsCoerced);

	result->xltype = result->xltype | xlbitXLFree;

	return result;

}




static AddIn XLL_WDS_Comp_zzzInternal_SumAcross(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_zzzInternal_SumAcross", 4), L"WDS.Comp.zzzInternal.SumAcross")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LONG, L"direction", L"is a 0/1 indicator for 0-Across Rows (vertical) or 1-Across Columns (horizontal)")
	.Arg(XLL_LONG, L"startrow", L"is the 1-Based beginrowng row (outside of limits defaults to input size).")
	.Arg(XLL_LONG, L"endrow", L"is the 1-Based ending row (outside of limits defaults to input size).")
	.Arg(XLL_LONG, L"startcolumn", L"is the 1-Based beginrowng column (outside of limits defaults to input size).")
	.Arg(XLL_LONG, L"endcolumn", L"is the 1-Based ending column(outside of limits defaults to input size).")
	.Category(L"WDS.Comp.zzzInternal")
	.FunctionHelp(L"Sum Across - An optimized sum across the rows or columns of a rectangular object.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_zzzInternal_SumAcross(LPXLOPER12 Arg0, long direction, long startrow, long endrow, long startcolumn, long endcolumn)
{

	int nrows, ncols;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	
	LPXLOPER12 cmArg0 = nullptr;
	bool bWasArg0Coerced = false;
	LPXLOPER12 cmOpts = nullptr;
	bool bWasOptsCoerced = false;

	try {

		if (lCoerceToMultiIfNecessary(Arg0, cmArg0, bWasArg0Coerced)!=xlretSuccess)
			throw exception("Failed xlCoerce"); 

		nrows = (int) cmArg0->val.array.rows;
		ncols = (int) cmArg0->val.array.columns;

		if (startrow == LONG_MAX) startrow = 1;
		else if (startrow <= 0) startrow = 1;
		else if (startrow > nrows) startrow = nrows + 1;
		if (endrow == LONG_MAX) endrow = nrows;
		else if (endrow > nrows) endrow = nrows;

		if (startcolumn == LONG_MAX) startcolumn = 1;
		else if (startcolumn <= 0) startcolumn = 1;
		else if (startcolumn > ncols) startcolumn = ncols + 1;
		if (endcolumn == LONG_MAX) endcolumn = ncols;
		else if (endcolumn > ncols) endcolumn = ncols;

		startrow -= 1;
		startcolumn -= 1;

		if (direction == 0) {
			result = new OPER12(1, endcolumn - startcolumn);
			double s, t;
			int i, j, ri, rj;
			for (rj=0, j = startcolumn; j < endcolumn; rj++, j++) {
				s = 0.0;
				for (ri=0, i = startrow; i < endrow; ri++, i++) {
					t = xltypeMulti_to_double(cmArg0, i, j, false, 0.0);
					s += t;
				}
				(*result)(0, rj) = s;
			}
		}
		else {
			result = new OPER12(endrow - startrow, 1);
			double s, t;
			int i, j, ri, rj;
			for (ri=0, i = startrow; i < endrow; ri++, i++) {
				s = 0.0;
				for (rj=0, j = startcolumn; j < endcolumn; rj++, j++) {
					t = xltypeMulti_to_double(cmArg0, i, j, false, 0.0);
					s += t;
				}
				(*result)(ri, 0) = s;
			}
		}

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sum across columns");
	}

	lFreeIfNecessary(cmArg0, bWasArg0Coerced);
	lFreeIfNecessary(cmOpts, bWasOptsCoerced);

	result->xltype = result->xltype | xlbitXLFree;

	return result;

}




static AddIn XLL_WDS_Comp_Matrix_SumAcross(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_SumAcross", 4), L"WDS.Comp.Matrix.SumAcross")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LONG, L"direction", L"is a 0/1 indicator for 0-Across Rows (vertical) or 1-Across Columns (horizontal)")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional array of {MaxRows}, {BeginRow, EndRow}, or {BeginRow,EndRow,BeginColumn,EndColumn}")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Sum Across - An optimized sum across the rows or columns of a Matrix/Range.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_SumAcross(LPXLOPER12 Arg0, long direction, LPXLOPER12 Opts)
{

	long beginrow = 0, endi = -1, beginj = 0, endj = -1;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	try {
		beginrow = LONG_MAX;
		endi = LONG_MAX;
		beginj = LONG_MAX;
		endj = LONG_MAX;

		if (!useless_LPXLOPER(Opts)) {

			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			if (lOpts.n_elem == 1) {
				endi = (long) lOpts.at(0);
			}
			else if (lOpts.n_elem == 2) {
				beginrow = (long) lOpts.at(0);
				endi = (long) lOpts.at(1);
			}
			else if (lOpts.n_elem == 4) {
				beginrow = (long) lOpts.at(0);
				endi = (long) lOpts.at(1);
				beginj = (long) lOpts.at(2);
				endj = (long) lOpts.at(3);
			}
		}

		result = WDS_Comp_zzzInternal_SumAcross(Arg0, direction, beginrow, endi, beginj, endj);

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sum across");
		result->xltype = result->xltype | xlbitXLFree;
	}

	return result;

}



static AddIn XLL_WDS_Comp_Matrix_SumAcrossRows(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_SumAcrossRows", 4), L"WDS.Comp.Matrix.SumAcrossRows")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional array of {MaxColumns}, {BeginColumn, EndColumn}, or {BeginRow,EndRow,BeginColumn,EndColumn}")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Sum Across - An optimized sum across the rows (vertical) of a Matrix/Range.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_SumAcrossRows(LPXLOPER12 Arg0, long direction, LPXLOPER12 Opts)
{

	long beginrow = 0, endi = -1, beginj = 0, endj = -1;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	try {
		beginrow = LONG_MAX;
		endi = LONG_MAX;
		beginj = LONG_MAX;
		endj = LONG_MAX;

		if (!useless_LPXLOPER(Opts)) {

			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			if (lOpts.n_elem == 1) {
				endi = (long) lOpts.at(0);
			}
			else if (lOpts.n_elem == 2) {
				beginrow = (long) lOpts.at(0);
				endi = (long) lOpts.at(1);
			}
			else if (lOpts.n_elem == 4) {
				beginrow = (long) lOpts.at(0);
				endi = (long) lOpts.at(1);
				beginj = (long) lOpts.at(2);
				endj = (long) lOpts.at(3);
			}
		}

		result = WDS_Comp_zzzInternal_SumAcross(Arg0, 0, beginrow, endi, beginj, endj);

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or sum across rows");
		result->xltype = result->xltype | xlbitXLFree;
	}

	return result;

}



static AddIn XLL_WDS_Comp_Matrix_SumAcrossColumns(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_SumAcrossColumns", 4), L"WDS.Comp.Matrix.SumAcrossColumns")
	.Arg(XLL_LPXLOPER, L"Arg0", L"is a LPXLOPER12")
	.Arg(XLL_LPXLOPER, L"opts", L"is an optional array of {MaxRows}, {BeginColumn, EndColumn}, or {BeginRow,EndRow,BeginColumn,EndColumn}")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Sum Across Columns - An optimized sum across the columns of a Matrix/Range.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_SumAcrossColumns(LPXLOPER12 Arg0, LPXLOPER12 Opts)
{

	long beginrow = 0, endi = -1, beginj = 0, endj = -1;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg0);
	allow_missings_only_LPXLOPER_or_exit(Opts);

	try {
		beginrow = LONG_MAX;
		endi = LONG_MAX;
		beginj = LONG_MAX;
		endj = LONG_MAX;

		if (!useless_LPXLOPER(Opts)) {

			iMatrix lOpts = iMatrixFromLPXLOPER(Opts, true, 0);
			if (lOpts.n_elem == 1) {
				endj = (long) lOpts.at(0);
			}
			else if (lOpts.n_elem == 2) {
				beginj = (long) lOpts.at(0);
				endj = (long) lOpts.at(1);
			}
			else if (lOpts.n_elem == 4) {
				beginrow = (long) lOpts.at(0);
				endi = (long) lOpts.at(1);
				beginj = (long) lOpts.at(2);
				endj = (long) lOpts.at(3);
			}
		}

		result = WDS_Comp_zzzInternal_SumAcross(Arg0, 1, beginrow, endi, beginj, endj);

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result->xltype = result->xltype | xlbitXLFree;
		result = new OPER12(L"Error, in coercion or sum across columns");
	}

	return result;

}


dMatrix dMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, double defv) {
	return dMatrixFromLPXLOPER(Arg, bStrict, defv, false, 0, false, 0);
}

static AddIn XLL_WDS_Comp_Matrix_RowNormed(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Comp_Matrix_RowNormed", 4), L"WDS.Comp.Matrix.RowNormed")
	.Arg(XLL_LPXLOPER, L"Arg", L"is an LPXLOPER12")
	.Arg(XLL_LPXLOPER, L"bStrict", L"is a flag to throw on bad values.")
	.Arg(XLL_LPXLOPER, L"defv", L"is the default value to use when not strict, defaults to NaN.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Row Normalization - Each target row is the unit sum normalized version of the source.")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Comp_Matrix_RowNormed(LPXLOPER12 Arg, LPXLOPER12 bStrict, LPXLOPER12 defv)
{

	using namespace WDS::Comp::Matrix;

	int i, j, nrows, ncols;

	LPOPER12 result=nullptr;
	require_usual_suspect_LPXLOPER(Arg);
	allow_missings_only_LPXLOPER_or_exit(bStrict);
	allow_missings_only_LPXLOPER_or_exit(defv);

	LPXLOPER12 cmArg=nullptr;
	bool bWasArgCoerced = false;
	require_usual_suspect_LPXLOPER(Arg);
	if (lCoerceToMultiIfNecessary(Arg, cmArg, bWasArgCoerced) != xlretSuccess) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		result = new OPER12(L"Error, in coercion in Matrix.RowNormed");
		if (result!=nullptr) result->xltype = result->xltype | xlbitXLFree;
	return result;
	}
	bool lbStrict = true;
	double ldefv = 0.0;

	if (useless_LPXLOPER(bStrict) ) {
		lbStrict = true;
	}
	else lbStrict = LPOPER_to_bool(bStrict,0,0);

	if (useless_LPXLOPER(defv)) {
		ldefv = nan("");
	}
	else
		ldefv = LPOPER_to_double(defv, 0, 0);


	try {

			dMatrix A=dMatrixFromLPXLOPER(cmArg,lbStrict,ldefv);


			RowNormInPlace(A);

			nrows = (int) A.nrows();
			ncols = (int) A.ncols();
			mIndex mi = 0;
			mIndex mj = 0;
			int i, j;
			result = new OPER12(nrows, ncols);
			for (i = 0, mi = 0; i < nrows; i++, mi++) {
				for (j = 0, mj = 0; j < ncols; j++, mj++) {
					(*result)(i, j) = A[mi, mj];
				}
			}

		}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or row-normalization");
	}

	lFreeIfNecessary(cmArg, bWasArgCoerced);

	if (result!=nullptr) result->xltype = result->xltype | xlbitXLFree;

	return result;

}





dMatrix NormedBaseOdds(int n, int m, int Offset, dMatrix& BaseOdds, dMatrix& Topology) {
	dMatrix result = BaseOdds.submat(span(Offset*n, (Offset + 1)*n), span::all);
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
	dMatrix result = BaseOdds(span(_Offset*n, (_Offset + 1)*n-1), span(nbase*n,(nbase+1)*n-1));
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
			i = (int) ijs.at(0, k);
			j = (int) ijs.at(1, k);
			v = (double) vs.at(rowindex, k);
			result(i, j) *= exp(v);
		}
	}
	RowNormInPlace(result);
	return result;
}



static AddIn XLL_WDS_Comp_Matrix_NormedBaseOdds(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_NormedBaseOdds", 4), L"WDS.Comp.Matrix.NormedBaseOdds")
	.Arg(XLL_LONG, L"Offset", L"is an integer for the block offset when BaseOdds is a vertical stack of nxn matrices.")
	.Arg(XLL_LPXLOPER, L"BaseOdds", L"is an (m*n)xn matrix of base odds where m is the number of blocks and n is the number of states.")
	.Arg(XLL_LPXLOPER, L"Topology", L"is an nxn 0/1 matrix of valid transitions.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"NormedBaseOdds - Returns a normalized transition matrix from a BaseOdds matrix.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_NormedBaseOdds(long Offset, LPXLOPER12 BaseOdds, LPXLOPER12 Topology)
{
	LPOPER12 oResult = nullptr;
	require_usual_suspect_LPXLOPER(BaseOdds);
	require_usual_suspect_LPXLOPER(Topology);
	LPXLOPER12 cmBaseOdds = nullptr;
	bool bWasBaseOddsCoerced = false;
	LPXLOPER12 cmTopology = nullptr;
	bool bWasTopologyCoerced = false;

	try {
		if (lCoerceToMultiIfNecessary(BaseOdds, cmBaseOdds, bWasBaseOddsCoerced) != xlretSuccess)
			throw exception("Failed xlCoerce on BaseOdds");
		if (lCoerceToMultiIfNecessary(Topology, cmTopology, bWasTopologyCoerced) != xlretSuccess)
			throw exception("Failed xlCoerce on Topology");
		int n = cmBaseOdds->val.array.columns;
		ensure(n == cmTopology->val.array.columns && n == cmTopology->val.array.rows);
		int nrows = (int) cmBaseOdds->val.array.rows;
		int m = nrows / n;
		ensure(nrows == n * m);
		dMatrix lBaseOdds = dMatrixFromLPXLOPER(BaseOdds,false,0.0);
		dMatrix lTopology = dMatrixFromLPXLOPER(Topology,false,0.0);
		dMatrix mResult = NormedBaseOdds(n, m, (int)Offset, lBaseOdds, lTopology);


		LPOPER12 oResult = new OPER12(n, n);
		mIndex mi = 0, mj = 0;
		int i = 0, j = 0;
		for (j = 0, mj = 0; j < n; j++, mj++)
			for (i = 0, mi = 0; i < n; i++, mi++)
				(*oResult)(i, j) = mResult[mi, mj];

	}
	catch (exception& e) {
		if (oResult != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)oResult);
		std::string ew = e.what();
		oResult = new OPER12(L"Error, in NormedBaseOdds: "+std::wstring(ew.begin(), ew.end()));
	}
	lFreeIfNecessary(cmBaseOdds, bWasBaseOddsCoerced);
	lFreeIfNecessary(cmTopology, bWasTopologyCoerced);

	oResult->xltype = oResult->xltype | xlbitXLFree;

	return oResult;
}





static AddIn XLL_WDS_Comp_Matrix_ScoredAndNormedBaseOdds(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_ScoredAndNormedBaseOdds", 4), L"WDS.Comp.Matrix.ScoredAndNormedBaseOdds")
	.Arg(XLL_LONG, L"Index", L"is an index into Offset and vs vectors.")
	.Arg(XLL_LONG, L"Offset", L"is a (#Rows)x1 matrix of integers for the block offset when BaseOdds is a vertical stack of nxn matrices.")
	.Arg(XLL_LPXLOPER, L"BaseOdds", L"is an (m*n)xn matrix of base odds where m is the number of blocks and n is the number of states.")
	.Arg(XLL_LPXLOPER, L"Topology", L"is an nxn 0/1 matrix of valid transitions.")
	.Arg(XLL_LPXLOPER, L"IJs", L"is a 2x(#v) matrix of indices for the pre-normalized factors.")
	.Arg(XLL_LPXLOPER, L"Vs", L"is a (#Rows)x(#v) matrix of log-domain values to apply at IJ locations prior to normalization.")
	.Arg(XLL_BOOL, L"UseTailFactorFlag", L"is a boolean to trigger a tail factor.")
	.Arg(XLL_LPXLOPER, L"TailFactor", L"is a factor matrix applied in the vanilla domain before normalization.")
	.Arg(XLL_LONG, L"TailIndex", L"is an index from the end of the horizon, used against the tail cut-off.")
	.Arg(XLL_LONG, L"TailCutOff", L"is the tail cut-off.  A TailIndex < TailCutoff triggers a additional tail factor.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"ScoredAndNormedBaseOdds - Returns a scored and normalized transition matrix from a BaseOdds matrix.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_ScoredAndNormedBaseOdds(long Index
	, LPXLOPER12 Offset
	, LPXLOPER12 BaseOdds
	, LPXLOPER12 Topology
	, LPXLOPER12 IJs
	, LPXLOPER12 Vs
	, bool bUseTailFactorFlag
	, LPXLOPER12 TailFactor
	, long TailIndex
	, long TailCutOff)
{
	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(BaseOdds);
	require_usual_suspect_LPXLOPER(Topology);
	allow_missings_only_LPXLOPER_or_exit(IJs);
	allow_missings_only_LPXLOPER_or_exit(Vs);
	allow_missings_only_LPXLOPER_or_exit(TailFactor);
	LPOPER12 oResult = nullptr;
	LPXLOPER12 cmOffset = nullptr;
	bool bWasOffsetCoerced = false;
	LPXLOPER12 cmBaseOdds = nullptr;
	bool bWasBaseOddsCoerced = false;
	LPXLOPER12 cmTopology = nullptr;
	bool bWasTopologyCoerced = false;
	bool bUseVs = false;
	LPXLOPER12 cmIJs = nullptr;
	bool bWasIJsCoerced = false;
	LPXLOPER12 cmVs = nullptr;
	bool bWasVsCoerced = false;
	LPXLOPER12 cmTailFactor = nullptr;
	bool bWasTailFactorCoerced = false;

	try {
		int nIndex = 1;
		if (lCoerceToMultiIfNecessary(Offset, cmOffset, bWasOffsetCoerced) != 0)
			throw std::exception("Coerce error in ScoredAndNormedBaseOdds.");
		nIndex = cmOffset->val.array.rows;
		Index -= 1;
		ensure(Index >= 0 && Index < nIndex);
		if (lCoerceToMultiIfNecessary(BaseOdds, cmBaseOdds, bWasBaseOddsCoerced) != 0)
			throw std::exception("Coerce error in ScoredAndNormedBaseOdds.");
		if (lCoerceToMultiIfNecessary(Topology, cmTopology, bWasTopologyCoerced)!=0)
			throw std::exception("Coerce error in ScoredAndNormedBaseOdds.");
		int n = cmBaseOdds->val.array.columns;
		ensure(n == cmTopology->val.array.columns && n == cmTopology->val.array.rows);
		int nrows = (int) cmBaseOdds->val.array.rows;
		int m = nrows / n;
		ensure(nrows == n * m);
		if (IJs->xltype == xltypeMulti || IJs->xltype == xltypeSRef || IJs->xltype == xltypeRef) {
			bUseVs = true;
			if (lCoerceToMultiIfNecessary(IJs, cmIJs, bWasIJsCoerced)!=0)
			throw std::exception("Coerce error in ScoredAndNormedBaseOdds.");
			if (lCoerceToMultiIfNecessary(Vs, cmVs, bWasVsCoerced)!=0)
			throw std::exception("Coerce error in ScoredAndNormedBaseOdds.");
			ensure(cmIJs->val.array.columns == cmVs->val.array.columns);
			ensure(cmVs->val.array.rows >= nIndex);
		}
		if (bUseTailFactorFlag) {
			if (lCoerceToMultiIfNecessary(TailFactor, cmTailFactor, bWasTailFactorCoerced)!=0)
			throw std::exception("Coerce error in ScoredAndNormedBaseOdds.");
			ensure(cmTailFactor->val.array.columns == n && cmTailFactor->val.array.rows == n);
		}

		iMatrix lOffset = iMatrixFromLPXLOPER(Offset,false,0.0,true,nrows,true,1);
		dMatrix lBaseOdds = dMatrixFromLPXLOPER(BaseOdds,false,0.0);
		dMatrix lTopology = dMatrixFromLPXLOPER(Topology,false,0.0);
		iMatrix lIJs = (bUseVs) ? iMatrixFromLPXLOPER(IJs,false,0) : iMatrix(1, 1);
		dMatrix lVs = (bUseVs) ? dMatrixFromLPXLOPER(Vs,false,0.0,true,nrows,false,0) : dMatrix(1, 1);
		dMatrix lTailFactor = (bUseTailFactorFlag) ? dMatrixFromLPXLOPER(TailFactor,false,0.0) : dMatrix(1, 1);
		
		dMatrix mResult = ScoredAndNormedBaseOdds((int) Index, n, m, 0, lOffset, lBaseOdds, lTopology, bUseVs, lIJs, lVs
					, bUseTailFactorFlag, lTailFactor, TailIndex, TailCutOff);

		LPOPER12 oResult = new OPER12(n, n);
		mIndex mi = 0, mj = 0;
		int i = 0, j = 0;
		for (j = 0, mj = 0; j < n; j++, mj++)
			for (i = 0, mi = 0; i < n; i++, mi++)
				(*oResult)(i, j) = mResult[mi, mj];

	}
	catch (exception& e) {
		if (oResult != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)oResult);
		std::string ew = e.what();
		oResult = new OPER12(L"Error, in ScoredAndNormedBaseOdds: "+std::wstring(ew.begin(), ew.end()));
	}
	lFreeIfNecessary(cmOffset, bWasOffsetCoerced);
	lFreeIfNecessary(cmBaseOdds, bWasBaseOddsCoerced);
	lFreeIfNecessary(cmTopology, bWasTopologyCoerced);
	lFreeIfNecessary(cmIJs, bWasIJsCoerced);
	lFreeIfNecessary(cmVs, bWasVsCoerced);
	lFreeIfNecessary(cmTailFactor, bWasTailFactorCoerced);

	oResult->xltype = oResult->xltype | xlbitXLFree;

	return oResult;
}


static AddIn XLL_WDS_Comp_Matrix_Mult(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_Matrix_Mult", 4), L"WDS.Comp.Matrix.Mult")
	.Arg(XLL_LPXLOPER, L"A", L"is an m1xn1 matrix.")
	.Arg(XLL_LPXLOPER, L"B", L"is an m2xn2 matrix.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"Mult - Returns a simple matrix multiplication when n1==m2.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_Matrix_Mult(LPXLOPER12 A, LPXLOPER12 B) {
	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(A);
	require_usual_suspect_LPXLOPER(B);
	LPOPER12 oResult = nullptr;
	LPXLOPER12 cmA = nullptr;
	bool bWasACoerced = false;
	LPXLOPER12 cmB = nullptr;
	bool bWasBCoerced = false;

	try {
			if (lCoerceToMultiIfNecessary(A, cmA, bWasACoerced)!=0)
			throw std::exception("Coerce error for A in Matrix.Mult.");
			if (lCoerceToMultiIfNecessary(B, cmB, bWasBCoerced)!=0)
			throw std::exception("Coerce error for B in Matrix.Mult.");
		ensure(cmA->val.array.columns = cmB->val.array.rows);
		dMatrix A = dMatrixFromLPXLOPER(cmA,false,0.0);
		dMatrix B = dMatrixFromLPXLOPER(cmB,false,0.0);
		dMatrix mResult = A * B;

		size_t nrows = (size_t) mResult.nrows();
		size_t ncols = (size_t) mResult.ncols();
		LPOPER12 oResult = new OPER12(nrows,ncols);
		mIndex mi = 0, mj = 0;
		size_t i = 0, j = 0;
		for (j = 0, mj = 0; j < ncols; j++, mj++)
			for (i = 0, mi = 0; i < nrows; i++, mi++)
				(*oResult)(i, j) = mResult[mi, mj];

	}
	catch (exception& e) {
		if (oResult != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)oResult);
		std::string ew = e.what();
		oResult = new OPER12(L"Error, in Matrix.Mult: "+std::wstring(ew.begin(), ew.end()));
	}
	lFreeIfNecessary(cmA, bWasACoerced);
	lFreeIfNecessary(cmB, bWasBCoerced);

	oResult->xltype = oResult->xltype | xlbitXLFree;
	return oResult;
}




static AddIn XLL_WDS_Comp_RFScheduled(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_RFScheduled", 4), L"WDS.Comp.RFScheduled")
	.Arg(XLL_LPXLOPER, L"PanelInd", L"is an indicator vector, any value other than 0 resets the schedule.  Use for panel data or to resync to a time period.")
	.Arg(XLL_LPXLOPER, L"LoanAgeMos", L"is a loan age vector as an input.")
	.Arg(XLL_LPXLOPER, L"PrinBal", L"is the EOM Principal Balance at LoanAgeMos where PanelInd<>0.")
	.Arg(XLL_LPXLOPER, L"IntRatePct", L"is periodic interest rate, expressed as a percent (values<1 are corrected to *100).")
	.Arg(XLL_LPXLOPER, L"TermMos", L"is a remaining term vector.  At LoanAgeMos=0, represents the original term.")
	.Arg(XLL_LPXLOPER, L"PmtAmt", L"is an optional total scheduled Principal and Interest amount. If invalid or positive, recalculates based on the PMT function.")
	.Arg(XLL_LPXLOPER, L"stoprow", L"is an optional length limiter.")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"RFScheduled - Returns a basic competing-risk-free amortization schedule [EOMPrinBal, PrinPmtAmt, IntPmtAmt, PmtAmt].")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_RFScheduled(
	 LPXLOPER12 PanelInd
	, LPXLOPER12 LoanAgeMos
	, LPXLOPER12 PrinBal
	, LPXLOPER12 IntRatePct
	, LPXLOPER12 TermMos
	, LPXLOPER12 PmtAmt
	, LPXLOPER12 stoprow
	)
{

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(PanelInd);
	require_usual_suspect_LPXLOPER_or_exit(LoanAgeMos);
	require_usual_suspect_LPXLOPER_or_exit(IntRatePct);
	require_usual_suspect_LPXLOPER_or_exit(TermMos);
	allow_missings_only_LPXLOPER_or_exit(PmtAmt);
	require_usual_suspect_LPXLOPER_or_exit(stoprow);

	LPOPER12 oResult = nullptr;
	LPXLOPER12 cmPanelInd = nullptr;
	bool bWasPanelIndCoerced = false;
	LPXLOPER12 cmLoanAgeMos = nullptr;
	bool bWasLoanAgeMosCoerced = false;
	LPXLOPER12 cmPrinBal = nullptr;
	bool bWasPrinBalCoerced = false;
	LPXLOPER12 cmIntRatePct = nullptr;
	bool bWasIntRatePctCoerced = false;
	LPXLOPER12 cmTermMos = nullptr;
	bool bWasTermMosCoerced = false;
	bool bUsingPmtAmt = false;
	LPXLOPER12 cmPmtAmt = nullptr;
	bool bWasPmtAmtCoerced = false;

	LPXLOPER12 tempXLOPER = nullptr;

	int nrows = 0;

	try {

		if (lCoerceToMultiIfNecessary(PanelInd, cmPanelInd, bWasPanelIndCoerced) != 0)
			throw std::exception("Coerce error in RFScheduled.");
		nrows = (int) cmPanelInd->val.array.rows;
		if (stoprow!=nullptr && stoprow->xltype == xltypeNum) {
			long tmplong = (long)stoprow->val.num;
			if (nrows > tmplong) nrows = tmplong;
		}
		ensure(nrows >= 1);

		if (lCoerceToMultiIfNecessary(LoanAgeMos, cmLoanAgeMos, bWasLoanAgeMosCoerced)!=0) 
			throw std::exception("Coerce error in RFScheduled.");
		ensure(cmLoanAgeMos->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(PrinBal, cmPrinBal, bWasPrinBalCoerced)!=0) 
			throw std::exception("Coerce error in RFScheduled.");
		ensure(cmPrinBal->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(IntRatePct, cmIntRatePct, bWasIntRatePctCoerced)!=0) 
			throw std::exception("Coerce error in RFScheduled.");
		ensure(cmIntRatePct->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(TermMos, cmTermMos, bWasTermMosCoerced)!=0) 
			throw std::exception("Coerce error in RFScheduled.");
		ensure(cmTermMos->val.array.rows >= nrows);
		
		if (PmtAmt==nullptr || PmtAmt->xltype == xltypeErr || PmtAmt->xltype == xltypeMissing || PmtAmt->xltype == xltypeNil) {
			bUsingPmtAmt = false;
		}
		else {
			if (lCoerceToMultiIfNecessary(PmtAmt, cmPmtAmt, bWasPmtAmtCoerced) == 0) {
				ensure(cmPmtAmt->val.array.rows >= nrows);
				bUsingPmtAmt = true;
			}
			else
				bUsingPmtAmt = false;
		}


		int i, j, iM1;
		oResult = new OPER12(nrows, 7);
		double tempdouble = 0.0;
		double tempdouble2 = 0.0;
		long templong = 0;
		double prinbal = 0.0;
		long term = 0;
		double intratepct = 0.0;
		double pmt = 0.0;
		int last_panelindex = 0;
		int rc = 0;
		for (i = 0, iM1=-1; i < nrows; i++, iM1++) {
			templong = xltypeMulti_to_long(cmPanelInd, i, 0, false, 0);
			if (i == 0 || templong != 0) {
				last_panelindex = i;
				prinbal = xltypeMulti_to_double(cmPrinBal, i, 0, false, 0);
				(*oResult)(i, 0) = prinbal;
				(*oResult)(i, 1) = 0.0;
				(*oResult)(i, 2) = 0.0;
				(*oResult)(i, 3) = 0.0;
				intratepct = xltypeMulti_to_double(cmIntRatePct, i, 0, false, 0);
				if (intratepct < 1.0) intratepct *= 100.0;
				intratepct /= 1200.0;
				term = xltypeMulti_to_long(cmTermMos, i, 0, false, 0);
				if (bUsingPmtAmt)
					pmt = xltypeMulti_to_double(cmPmtAmt, i, 0, false, 0);
				else {
					if (tempXLOPER == nullptr) tempXLOPER = new XLOPER12();
					rc = Excel12(xlfPmt, tempXLOPER, 4, TempNum12(intratepct), TempInt12(term), TempNum12(prinbal), TempNum12(0.0));
					if (rc == xlretSuccess) {
						pmt = (double) tempXLOPER->val.num;
					}
					else {
						pmt = 0.0;
					}
				}
				if (prinbal > 1e-6 && pmt<-1e-6) {
					(*oResult)(i, 4) = pmt+intratepct/(1.0+intratepct)*(prinbal-pmt);
					(*oResult)(i, 5) = -intratepct/(1.0+intratepct)*(prinbal-pmt);
					(*oResult)(i, 6) = pmt;
				}
			}
			else {
				if (prinbal > 1e-2) {
					tempdouble = -prinbal * intratepct;
					if (tempdouble < pmt) tempdouble = pmt;
					tempdouble2 = pmt - tempdouble;
					if (-tempdouble2 > prinbal) tempdouble2 = -prinbal;
					(*oResult)(i, 1) = tempdouble2;
					(*oResult)(i, 2) = tempdouble;
					(*oResult)(i, 3) = tempdouble+tempdouble2;
					prinbal += tempdouble2;
					(*oResult)(i, 0) = prinbal;
					if (i > last_panelindex + 1) {
						(*oResult)(i, 4) = (*oResult)(iM1, 4) + tempdouble2;
						(*oResult)(i, 5) = (*oResult)(iM1, 5) + tempdouble;
						(*oResult)(i, 6) = (*oResult)(iM1, 6) + tempdouble + tempdouble2;
					}
					else {
						(*oResult)(i, 4) = tempdouble2;
						(*oResult)(i, 5) = tempdouble;
						(*oResult)(i, 6) = tempdouble + tempdouble2;
					}
				}
				else if (prinbal > 0) {
					(*oResult)(i, 1) = 0.0;
					(*oResult)(i, 2) = -prinbal;
					(*oResult)(i, 3) = -prinbal;
					prinbal = 0.0;
					(*oResult)(i, 0) = prinbal;
					if (i > last_panelindex + 1) {
						(*oResult)(i, 4) = (*oResult)(iM1, 4) + tempdouble2;
						(*oResult)(i, 5) = (*oResult)(iM1, 5) + tempdouble;
						(*oResult)(i, 6) = (*oResult)(iM1, 6) + tempdouble - tempdouble2;
					}
					else {
						(*oResult)(i, 4) = 0.0;
						(*oResult)(i, 5) = -prinbal;
						(*oResult)(i, 6) = -prinbal;

					}
				}
				else {
					if (i > last_panelindex + 1) {
						(*oResult)(i, 4) = (*oResult)(iM1, 4) ;
						(*oResult)(i, 5) = (*oResult)(iM1, 5) ;
						(*oResult)(i, 6) = (*oResult)(iM1, 6) ;
					}
				}
			}
		}

	}
	catch (exception& e) {
		if (oResult != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)oResult);
		std::string ew = e.what();
		oResult = new OPER12(L"Error, in RFScheduled: "+std::wstring(ew.begin(), ew.end()));
	}
	lFreeIfNecessary(cmPanelInd, bWasPanelIndCoerced);
	lFreeIfNecessary(cmLoanAgeMos, bWasLoanAgeMosCoerced);
	lFreeIfNecessary(cmPrinBal, bWasPrinBalCoerced);
	lFreeIfNecessary(cmIntRatePct, bWasIntRatePctCoerced);
	lFreeIfNecessary(cmTermMos, bWasTermMosCoerced);
	lFreeIfNecessary(cmPmtAmt, bWasPmtAmtCoerced);

	if (oResult!=nullptr) oResult->xltype = oResult->xltype | xlbitXLFree;
	return oResult;
}


static AddIn XLL_WDS_Comp_RollIt(
	Function(XLL_LPOPER, XLL_DECORATE(L"WDS_Comp_RollIt", 4), L"WDS.Comp.RollIt")
	.Arg(XLL_LPXLOPER, L"PanelInd", L"is an indicator vector, any value other than 0 resets the schedule.  Use for panel data or to resync to a time period.")
	.Arg(XLL_LPXLOPER, L"LoanAgeMos", L"is a loan age vector as an input.")
	.Arg(XLL_LPXLOPER, L"WAM", L"is a remaining term vector.  At LoanAgeMos=0, represents the original term.")
	.Arg(XLL_LPXLOPER, L"RFSched", L"is the output from RFScheduled.")
	.Arg(XLL_LPXLOPER, L"NDist", L"is the Actuals Unit Distribution.")
	.Arg(XLL_LPXLOPER, L"PrinBalDist", L"is the Actuals PrinBal Distribution.")
	.Arg(XLL_LPXLOPER, L"Offset", L"is a (#Rows)x1 matrix of integers for the block offset when BaseOdds is a vertical stack of nxn matrices.")
	.Arg(XLL_LPXLOPER, L"BaseOdds", L"is an (m*n)xn matrix of base odds where m is the number of blocks and n is the number of states.")
	.Arg(XLL_LPXLOPER, L"Topology", L"is an nxn 0/1 matrix of valid transitions.")
	.Arg(XLL_LPXLOPER, L"DelqDelta", L"is a Topology-like matrix of expected lags in EOM vs Scheduled.")
	.Arg(XLL_LPXLOPER, L"IJs", L"is a 2x(#v) matrix of (Base 1) indices for the pre-normalized factors.")
	.Arg(XLL_LPXLOPER, L"Vs", L"is a (#Rows)x(#v) matrix of log-domain values to apply at IJ locations prior to normalization.")
	.Arg(XLL_BOOL, L"UseTailFactorFlag", L"is a boolean to trigger a tail factor.")
	.Arg(XLL_LPXLOPER, L"TailFactor", L"is a factor matrix applied in the vanilla domain before normalization.")
	.Arg(XLL_LONG, L"TailIndex", L"is an index from the end of the horizon, used against the tail cut-off.")
	.Arg(XLL_LONG, L"TailCutOff", L"is the tail cut-off.  A TailIndex < TailCutoff triggers a additional tail factor.")
	.Arg(XLL_LPXLOPER, L"stoprow", L"is an optional length limiter.")
	.Arg(XLL_BOOL, L"UseDbgDirective", L"is an optional boolean to a simple return of a few preprogrammed debugging directives.")
	.Arg(XLL_LPXLOPER, L"DbgDirective", L"is an optional debugging directive.")
	.Arg(XLL_LPXLOPER, L"DbgOption", L"is an optional secondary debugging directive.")
	.Arg(XLL_LPXLOPER, L"DbgIndex", L"is an optional index for the debugging directive (usually a row to run through).")
	.Category(L"WDS.Comp")
	.FunctionHelp(L"RollIt - Roll Forward.")
);
extern "C" __declspec(dllexport) LPOPER12  WINAPI
WDS_Comp_RollIt(
	 LPXLOPER12 PanelInd
	, LPXLOPER12 LoanAgeMos
	, LPXLOPER12 WAM
	, LPXLOPER12 RFSched
	, LPXLOPER12 NDist
	, LPXLOPER12 PrinBalDist
	, LPXLOPER12 Offset
	, LPXLOPER12 BaseOdds
	, LPXLOPER12 Topology
	, LPXLOPER12 DelqDelta
	, LPXLOPER12 IJs
	, LPXLOPER12 Vs
	, bool bUseTailFactorFlag
	, LPXLOPER12 TailFactor
	, long TailIndex
	, long TailCutOff
	, LPXLOPER12 stoprow
	, bool bUseDbgDirective
	, LPXLOPER12 DbgDirective
	, LPXLOPER12 DbgOption
	, LPXLOPER12 DbgIndex
	)
{
	LPOPER12 result = nullptr;

	require_usual_suspect_LPXLOPER_or_exit(PanelInd);
	require_usual_suspect_LPXLOPER_or_exit(LoanAgeMos);
	require_usual_suspect_LPXLOPER_or_exit(WAM);
	require_usual_suspect_LPXLOPER_or_exit(RFSched);
	require_usual_suspect_LPXLOPER_or_exit(NDist);
	require_usual_suspect_LPXLOPER_or_exit(PrinBalDist);
	require_usual_suspect_LPXLOPER_or_exit(Offset);
	require_usual_suspect_LPXLOPER_or_exit(BaseOdds);
	require_usual_suspect_LPXLOPER_or_exit(Topology);
	require_usual_suspect_LPXLOPER_or_exit(DelqDelta);
	allow_missings_only_LPXLOPER_or_exit(IJs);
	allow_missings_only_LPXLOPER_or_exit(Vs);
	allow_missings_only_LPXLOPER_or_exit(TailFactor);
	allow_missings_only_LPXLOPER_or_exit(stoprow);
	allow_missings_only_LPXLOPER_or_exit(DbgDirective);
	allow_missings_only_LPXLOPER_or_exit(DbgOption);
	allow_missings_only_LPXLOPER_or_exit(DbgIndex);

	LPOPER12 oResult = nullptr;
	LPXLOPER12 cmPanelInd = nullptr;
	bool bWasPanelIndCoerced = false;
	LPXLOPER12 cmLoanAgeMos = nullptr;
	bool bWasLoanAgeMosCoerced = false;
	LPXLOPER12 cmWAM = nullptr;
	bool bWasWAMCoerced = false;
	LPXLOPER12 cmRFSched = nullptr;
	bool bWasRFSchedCoerced = false;
	LPXLOPER12 cmNDist = nullptr;
	bool bWasNDistCoerced = false;
	LPXLOPER12 cmPrinBalDist = nullptr;
	bool bWasPrinBalDistCoerced = false;
	LPXLOPER12 cmOffset = nullptr;
	bool bWasOffsetCoerced = false;
	LPXLOPER12 cmBaseOdds = nullptr;
	bool bWasBaseOddsCoerced = false;
	LPXLOPER12 cmTopology = nullptr;
	bool bWasTopologyCoerced = false;
	LPXLOPER12 cmDelqDelta = nullptr;
	bool bWasDelqDeltaCoerced = false;
	bool bUseVs = false;
	LPXLOPER12 cmIJs = nullptr;
	bool bWasIJsCoerced = false;
	LPXLOPER12 cmVs = nullptr;
	bool bWasVsCoerced = false;
	LPXLOPER12 cmTailFactor = nullptr;
	bool bWasTailFactorCoerced = false;

	LPXLOPER12 cmDbgDirective = nullptr;
	bool bWasDbgDirectiveCoerced = false;
	LPXLOPER12 cmDbgOption = nullptr;
	bool bWasDbgOptionCoerced = false;
	LPXLOPER12 cmDbgIndex = false;
	bool bWasDbgIndexCoerced = false;

	LPXLOPER12 tempXLOPER = nullptr;

	int nrows = 0;

	int row=0, rowM1=-1, rowP1=1;
	int NStates = 0;
	int i, j, k;
	mIndex mi=0, mj=0;


	try {
		if (lCoerceToMultiIfNecessary(PanelInd, cmPanelInd, bWasPanelIndCoerced) != 0)
			throw std::exception("Coerce Error in Rollit.");
		nrows = (int) cmPanelInd->val.array.rows;
		if (stoprow!=nullptr && stoprow->xltype == xltypeNum) {
			long tmplong = (long)stoprow->val.num;
			if (nrows > tmplong) nrows = tmplong;
		}
		ensure(nrows >= 1);

		if (lCoerceToMultiIfNecessary(LoanAgeMos, cmLoanAgeMos, bWasLoanAgeMosCoerced) != 0)
			throw std::exception("Coerce Error in Rollit.");
		ensure(cmLoanAgeMos->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(WAM, cmWAM, bWasWAMCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		ensure(cmWAM->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(RFSched, cmRFSched, bWasRFSchedCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		ensure(cmRFSched->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(NDist, cmNDist, bWasNDistCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		ensure(cmNDist->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(PrinBalDist, cmPrinBalDist, bWasPrinBalDistCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		ensure(cmPrinBalDist->val.array.rows >= nrows);
		if (lCoerceToMultiIfNecessary(Offset, cmOffset, bWasOffsetCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		ensure(cmOffset->val.array.rows >= nrows);

		if (lCoerceToMultiIfNecessary(BaseOdds, cmBaseOdds, bWasBaseOddsCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		if (lCoerceToMultiIfNecessary(Topology, cmTopology, bWasTopologyCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		int NStates = cmTopology->val.array.rows;
		ensure(NStates == cmTopology->val.array.columns);
		int mbase = cmBaseOdds->val.array.rows / NStates;
		int nbase = cmBaseOdds->val.array.columns / NStates;
		if (lCoerceToMultiIfNecessary(DelqDelta, cmDelqDelta, bWasDelqDeltaCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
		NStates = cmDelqDelta->val.array.rows;
		ensure(NStates == cmDelqDelta->val.array.columns && NStates == cmDelqDelta->val.array.rows);
		ensure(cmBaseOdds->val.array.rows == NStates * mbase);
		ensure((nbase>3) && cmBaseOdds->val.array.columns == NStates * nbase);
		if (IJs->xltype == xltypeMulti || IJs->xltype == xltypeSRef || IJs->xltype == xltypeRef) {
			bUseVs = true;
			if (lCoerceToMultiIfNecessary(IJs, cmIJs, bWasIJsCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
			if (lCoerceToMultiIfNecessary(Vs, cmVs, bWasVsCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
			ensure(cmIJs->val.array.columns == cmVs->val.array.columns);
			ensure(cmVs->val.array.rows >= nrows);
		}
		iMatrix lIJs = (bUseVs) ? iMatrixFromLPXLOPER(cmIJs,false,0) : iMatrix(1, 1);
		if (bUseVs) lIJs-=1;
		dMatrix lVs = (bUseVs) ? dMatrixFromLPXLOPER(cmVs,false,0.0,true,nrows,false,0) : dMatrix(1, 1);
		if (bUseTailFactorFlag) {
			if (lCoerceToMultiIfNecessary(TailFactor, cmTailFactor, bWasTailFactorCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
			ensure(cmTailFactor->val.array.columns == NStates && cmTailFactor->val.array.rows == NStates);
		}
		dMatrix lTailFactor = (bUseTailFactorFlag) ? dMatrixFromLPXLOPER(cmTailFactor,false,0.0) : dMatrix(1, 1);

		long lDbgDirective = 0;
		long lDbgOption = 0;
		long lDbgIndex = 0;
		if (bUseDbgDirective) {
			if (lCoerceToMultiIfNecessary(DbgDirective, cmDbgDirective, bWasDbgDirectiveCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
			lDbgDirective = LPOPER_to_long(cmDbgDirective, 0, 0);
			if (lCoerceToMultiIfNecessary(DbgOption, cmDbgOption, bWasDbgOptionCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
			lDbgOption = LPOPER_to_long(cmDbgOption, 0, 0);
			if (lCoerceToMultiIfNecessary(DbgIndex, cmDbgIndex, bWasDbgIndexCoerced)!=0)
			throw std::exception("Coerce Error in Rollit.");
			lDbgIndex = LPOPER_to_long(cmDbgIndex, 0, 0);
		}

		iMatrix lOffset = iMatrixFromLPXLOPER(cmOffset,false,0.0,true,nrows,false,0);
		dMatrix lBaseOdds = dMatrixFromLPXLOPER(cmBaseOdds,false,0.0);
		dMatrix lTopology = dMatrixFromLPXLOPER(cmTopology,false,0.0);
		dMatrix lDelqDelta = dMatrixFromLPXLOPER(cmDelqDelta,false,0.0);
		int NAbsorbing = 0;
		bool found = false;
		for (i = NStates - 1, NAbsorbing = 0, found = false; !found && i >= 0; i--, NAbsorbing++) {
			found = (fabs(lTopology.at(i, i) - 1.0) > 1e-6);
		}
		if (found) NAbsorbing -= 1;
		int NTerminal = 0;
		for (i = NStates - NAbsorbing - 1, NTerminal = 0, found = false; !found && i >= 0; i--, NTerminal++) {
			found = (fabs(lTopology.at(i, i) - 0.0) > 1e-6);
		}
		if (found) NTerminal -= 1;
		int NSurviving = NStates - NAbsorbing - NTerminal;
		int IndexFirstRecurrent = 0;
		for (i =  0, found = false, IndexFirstRecurrent=0; !found && i <NSurviving; i++, IndexFirstRecurrent++) {
			found = (fabs(lTopology.at(i, i) - 0.0) > 1e-6);
		}
		if (found) IndexFirstRecurrent -= 1;


		
		int NTotalCols = NStates * 4 + 6;

		dMatrix mDbg(1,1, fill::zeros);
		dMatrix mNDist(nrows, NStates, fill::zeros);
		dMatrix mPrinBalDist(nrows, NStates, fill::zeros);
		dMatrix mPmtPrinAmt(nrows, NStates, fill::zeros);
		dMatrix mPmtIntAmt(nrows, NStates, fill::zeros);

		dMatrix mNSurv(nrows, 1, fill::zeros);
		dMatrix mNMat(nrows, 1, fill::zeros);
		dMatrix mNMatPost(nrows, 1, fill::zeros);
		dMatrix mPrinBalSurv(nrows, 1, fill::zeros);
		dMatrix mPrinBalMat(nrows, 1, fill::zeros);
		dMatrix mPrinBalMatPost(nrows, 1, fill::zeros);

		double tempdouble = 0.0;
		double tempdouble2 = 0.0;
		double tempdouble3 = 0.0;
		double tempdouble4 = 0.0;
		long templong = 0;
		long templong2 = 0;
		long loanage = 0;
		long mtm = 0;
		double cnt = 0.0;
		double prinbal = 0.0;
		long term = 0;
		double intratepct = 0.0;
		double pmt = 0.0;
		int rc = 0;
		int firstrow_forpanel = 0;
		bool bIsRowLastRowForPanel=false;
		bool bDbgStop = false;

				dMatrix MPmtPrinAmtI = dMatrix(1, NStates, fill::zeros);
				dMatrix MPmtPrinAmtJ = dMatrix(1, NStates, fill::zeros);
				dMatrix MPmtPrinAmt = dMatrix(NStates, NStates, fill::zeros);
				dMatrix MPmtIntAmtI = dMatrix(1, NStates, fill::zeros);
				dMatrix MPmtIntAmtJ = dMatrix(1, NStates, fill::zeros);
				dMatrix MPmtIntAmt = dMatrix(NStates, NStates, fill::zeros);
				dMatrix lMPmtPrinAmtBackPatch = dMatrix(24, 1, fill::zeros);
				dMatrix lMPmtIntAmtBackPatch = dMatrix(24, 1, fill::zeros);

		if (nrows==1) 
			templong2 = xltypeMulti_to_long(cmPanelInd, 0, 0, false, 0);
		else
			templong2 = xltypeMulti_to_long(cmPanelInd, 1, 0, false, 0);

		for (row = 0, rowM1 = -1, rowP1=1; !bDbgStop && row < nrows; row++, rowM1++, rowP1++) {
			if (row == nrows - 1) {
				bIsRowLastRowForPanel = true;
				templong = templong2;
			}
			else {
				templong = templong2;
				templong2 = xltypeMulti_to_long(cmPanelInd, rowP1, 0, false, 0);
				bIsRowLastRowForPanel = (templong2 != 0);
			}
			mtm = xltypeMulti_to_long(cmWAM, row, 0, false, 0);
			if (row == 0 || templong != 0) {
				firstrow_forpanel = row;
				mtm = xltypeMulti_to_long(cmWAM, row, 0, false, 0);
				prinbal = 0.0;
				cnt = 0.0;
				for (j = 0; j < NStates; j++) {
					tempdouble = xltypeMulti_to_double(cmNDist, row, j, false, 0);
					mNDist.at(row, j) = tempdouble;
					if (j < NSurviving) cnt += tempdouble;
					tempdouble = xltypeMulti_to_double(cmPrinBalDist, row, j, false, 0);
					mPrinBalDist.at(row, j) = tempdouble;
					if (j < NSurviving) prinbal += tempdouble;
				}
				memset(lMPmtPrinAmtBackPatch.memptr(), 0, 24 * sizeof(double));
				memset(lMPmtIntAmtBackPatch.memptr(), 0, 24 * sizeof(double));
				double lprinbal = xltypeMulti_to_double(cmRFSched, firstrow_forpanel, 0, false, 0.0);   //PrinBal
				double lpmtamt = xltypeMulti_to_double(cmRFSched, firstrow_forpanel, 6, false, 0.0); // last PmtAmt
				double lpmtprinamt = xltypeMulti_to_double(cmRFSched, firstrow_forpanel, 4, false, 0.0); // last PmtAmt
				double lpmtintamt = xltypeMulti_to_double(cmRFSched, firstrow_forpanel, 5, false, 0.0); // last PmtAmt
				double lirfactor = -lpmtintamt / (lprinbal - lpmtprinamt);
				lirfactor /= (1.0 + lirfactor);
				for (k = 1; k < 24 && k < NStates; k++) {
					lMPmtPrinAmtBackPatch[k] = lMPmtPrinAmtBackPatch[k - 1] - lpmtprinamt;
					lMPmtIntAmtBackPatch[k] = lMPmtIntAmtBackPatch[k - 1] - lpmtintamt;
					lprinbal -= lpmtprinamt;
					lpmtintamt = -lirfactor * lprinbal;
					lpmtprinamt = lpmtamt - lpmtintamt;
				}

			}
			else if (cnt > 1e-6 && prinbal > 1e-6) {
				dMatrix MUnits = ScoredAndNormedBaseOdds(row, NStates, mbase, 0, lOffset, lBaseOdds, lTopology, bUseVs, lIJs, lVs, bUseTailFactorFlag, lTailFactor, mtm, TailCutOff);
				for (mi = NStates - NAbsorbing; mi < NStates; mi++)
					MUnits[mi, mi] = 1.0;
				if (bUseDbgDirective && lDbgDirective == 1 && row + 1 == lDbgIndex) {
					mDbg = MUnits;
					bDbgStop = true;
				}

				MPmtPrinAmt = dMatrix(NStates, NStates, fill::zeros);
				MPmtIntAmt = dMatrix(NStates, NStates, fill::zeros);
				MPmtPrinAmtI = dMatrix(1, NStates, fill::zeros);
				MPmtPrinAmtJ = dMatrix(1, NStates, fill::zeros);
				MPmtIntAmtI = dMatrix(1, NStates, fill::zeros);
				MPmtIntAmtJ = dMatrix(1, NStates, fill::zeros);

				for (mj = 0; mj < NStates; mj++) {
					int delqoffsetj = (int)lDelqDelta[0, mj];
					j = row + delqoffsetj;
					i = rowM1 + delqoffsetj;
					if (j > firstrow_forpanel) {
						MPmtPrinAmtJ[mj] = xltypeMulti_to_double(cmRFSched, j, 4, false, 0.0);
						MPmtIntAmtJ[mj] = xltypeMulti_to_double(cmRFSched, j, 5, false, 0.0);
					}
					else if (j < firstrow_forpanel && j>firstrow_forpanel - 24) {
						MPmtPrinAmtJ[mj] = lMPmtPrinAmtBackPatch[firstrow_forpanel - j];
						MPmtIntAmtJ[mj] = lMPmtIntAmtBackPatch[firstrow_forpanel - j];
					}
					if (i > firstrow_forpanel) {
						MPmtPrinAmtI[mj] = xltypeMulti_to_double(cmRFSched, i, 4, false, 0.0);
						MPmtIntAmtI[mj] = xltypeMulti_to_double(cmRFSched, i, 5, false, 0.0);
					}
					else if (i < firstrow_forpanel && i>firstrow_forpanel - 24) {
						MPmtPrinAmtI[mj] = lMPmtPrinAmtBackPatch[firstrow_forpanel - i];
						MPmtIntAmtI[mj] = lMPmtIntAmtBackPatch[firstrow_forpanel - i];
					}
				}

				for (mj = 0; mj < NStates; mj++) {
					int delqoffsetj = (int)lDelqDelta[0, mj];
					if (abs(delqoffsetj) < 1000) {
						for (mi = 0; mi < NStates; mi++) {
							if (lTopology[mi, mj] > 0.0) {
								MPmtPrinAmt[mi, mj] = MPmtPrinAmtJ[mj] - MPmtPrinAmtI[mi];
								MPmtIntAmt[mi, mj] = MPmtIntAmtJ[mj] - MPmtIntAmtI[mi];
							}
						}
					}
				}
				if (bUseDbgDirective && lDbgDirective == 2 && row + 1 == lDbgIndex) {
					if (lDbgOption == 0) {
						mDbg = MPmtPrinAmt;
						for (mj = 0; mj < NStates; mj++) {
							mDbg[mj, 0] = MPmtPrinAmtI[mj];
							mDbg[0, mj] = MPmtPrinAmtJ[mj];
						}
					}
					else if (lDbgOption == 1) {
						mDbg = MPmtIntAmt;
						for (mj = 0; mj < NStates; mj++) {
							mDbg[mj, 0] = MPmtIntAmtI[mj];
							mDbg[0, mj] = MPmtIntAmtJ[mj];
						}
					}
					else if (lDbgOption == 2)
						mDbg = MPmtPrinAmtI;
					else if (lDbgOption == 3)
						mDbg = MPmtIntAmtI;
					else if (lDbgOption == 4)
						mDbg = MPmtPrinAmtJ;
					else if (lDbgOption == 5)
						mDbg = MPmtIntAmtJ;
					else if (lDbgOption == 6)
						mDbg = lMPmtPrinAmtBackPatch;
					else if (lDbgOption == 7)
						mDbg = lMPmtIntAmtBackPatch;
					bDbgStop = true;
				}
				MPmtPrinAmt %= MUnits;
				MPmtIntAmt %= MUnits;
				if (bUseDbgDirective && lDbgDirective == 3 && row + 1 == lDbgIndex) {
					if (lDbgOption == 0)
						mDbg = MPmtPrinAmt;
					else
						mDbg = MPmtIntAmt;
					bDbgStop = true;
				}
				mNDist(row, span::all) = mNDist(rowM1, span::all)*MUnits(span::all, span::all);
				dMatrix rollPrinBalLag1 = mPrinBalDist(rowM1, span::all)*MUnits(span::all, span::all);
				mPmtPrinAmt(row, span::all) = mNDist(rowM1, span::all)*MPmtPrinAmt(span::all, span::all);
				mPmtIntAmt(row, span::all) = mNDist(rowM1, span::all)*MPmtIntAmt(span::all, span::all);
				mPrinBalDist(row, span::all) = rollPrinBalLag1(0, span::all) + mPmtPrinAmt(row, span::all);
				if (bUseDbgDirective && lDbgDirective == 4 && row + 1 == lDbgIndex) {
					if (lDbgOption == 0)
						mDbg = mPrinBalDist(rowM1, span::all);
					else if (lDbgOption == 1)
						mDbg = rollPrinBalLag1;
					else if (lDbgOption == 2)
						mDbg = mPmtPrinAmt(row, span::all);
					else if (lDbgOption == 3)
						mDbg = mNDist(rowM1, span::all);
					else if (lDbgOption == 4)
						mDbg = mNDist(row, span::all);
					bDbgStop = true;
				}
				for (mj = 0; mj < NStates; mj++) {
					if (mPrinBalDist(row, mj) < 0.0) {
						mPmtPrinAmt(row, mj) -= mPrinBalDist(row, mj);
						mPrinBalDist(row, mj) = 0.0;
					}
				}
				cnt = 0.0;
				prinbal = 0.0;
				for (mj=0; mj < NStates - NAbsorbing- NTerminal; mj++) {
					cnt += mNDist[row, mj];
					prinbal += mPrinBalDist[row, mj];
				}
			}
			if (mtm > 0) {
				mNSurv(row, 0) = cnt;
				mPrinBalSurv(row, 0) = prinbal;
			}
			else if (mtm <= 0) {
				tempdouble = 0.0;
				tempdouble2 = 0.0;
				for (mj=0; mj < NStates - NAbsorbing- NTerminal; mj++) {
					if (bIsRowLastRowForPanel || ( lDelqDelta[0,mj]>=0 && mNDist[row,mj]>0) ) {
						cnt -= mNDist[row, mj];
						mNMat(row, 0) += mNDist[row, mj];
						mNDist[row, mj] = 0.0;
						prinbal -= mPrinBalDist[row, mj];
						mPrinBalMat[row, mj] += mPrinBalDist[row, mj];
						mPrinBalDist[row, mj] = 0.0;;
					}
				}
			}
			if (mtm < 0) {
				mNMatPost(row, 0) =mNMatPost(rowM1,0)+mNMat(rowM1,0);
				mPrinBalMatPost(row, 0) = mPrinBalMatPost(rowM1,0)+mPrinBalMat(rowM1,0);
			}
		}

		if (!bUseDbgDirective) {
			oResult = new OPER12(nrows, NStates * 4 + 6);
			for (k = 0; k < nrows; k++) {
				for (j = 0; j < NStates; j++) {
					(*oResult)(k, j) = mNDist(k, j);
					(*oResult)(k, j + NStates) = mPrinBalDist(k, j);
					(*oResult)(k, j + 2 * NStates) = mPmtPrinAmt(k, j);
					(*oResult)(k, j + 3 * NStates) = mPmtIntAmt(k, j);
					(*oResult)(k, j + 3 * NStates+1) = mNSurv(k, 0);
					(*oResult)(k, j + 3 * NStates+2) = mNMat(k, 0);
					(*oResult)(k, j + 3 * NStates+3) = mNMatPost(k, 0);
					(*oResult)(k, j + 3 * NStates+4) = mPrinBalSurv(k, 0);
					(*oResult)(k, j + 3 * NStates+5) = mPrinBalMat(k, 0);
					(*oResult)(k, j + 3 * NStates+6) = mPrinBalMatPost(k, 0);
				}
			}
		}
		else if (bUseDbgDirective) {
			oResult = new OPER12((int) mDbg.n_rows,(int) mDbg.n_cols);
			for (k = 0; k < (int) mDbg.n_rows; k++) {
				for (j = 0; j < (int) mDbg.n_cols; j++) {
					(*oResult)(k, j) = mDbg(k, j);
				}
			}
		}
	}
	catch (exception& e) {
		if (oResult != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)oResult);
		std::string ew = e.what();
		oResult = new OPER12(L"Error, in RollIt: "+std::wstring(ew.begin(), ew.end()));
	}
	lFreeIfNecessary(cmPanelInd, bWasPanelIndCoerced);
	lFreeIfNecessary(cmLoanAgeMos, bWasLoanAgeMosCoerced);
	lFreeIfNecessary(cmWAM, bWasWAMCoerced);
	lFreeIfNecessary(cmRFSched, bWasRFSchedCoerced);
	lFreeIfNecessary(cmNDist, bWasNDistCoerced);
	lFreeIfNecessary(cmPrinBalDist, bWasPrinBalDistCoerced);
	lFreeIfNecessary(cmOffset, bWasOffsetCoerced);
	lFreeIfNecessary(cmBaseOdds, bWasBaseOddsCoerced);
	lFreeIfNecessary(cmTopology, bWasTopologyCoerced);
	lFreeIfNecessary(cmDelqDelta, bWasDelqDeltaCoerced);
	lFreeIfNecessary(cmIJs, bWasIJsCoerced);
	lFreeIfNecessary(cmVs, bWasVsCoerced);
	lFreeIfNecessary(cmTailFactor, bWasTailFactorCoerced);
	lFreeIfNecessary(cmDbgDirective, bWasDbgDirectiveCoerced);
	lFreeIfNecessary(cmDbgOption, bWasDbgOptionCoerced);
	lFreeIfNecessary(cmDbgIndex, bWasDbgIndexCoerced);

	oResult->xltype = oResult->xltype | xlbitXLFree;

	return oResult;
}




static AddIn XLL_WDS_Util_SimpleFirsts(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Util_SimpleFirsts", 4), L"WDS.Util.SimpleFirsts")
	.Arg(XLL_LPXLOPER, L"Arg", L"is an column")
	.Arg(XLL_LPXLOPER, L"inputrowlimit", L"is an optional maximum number of rows to consider.")
	.Arg(XLL_LPXLOPER, L"outputrowlimit", L"is an optional maximum number of rows to return.")
	.Category(L"WDS.Util")
	.FunctionHelp(L"Return just the list of first values in panels.")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Util_SimpleFirsts(LPXLOPER12 Arg, LPXLOPER12 inputrowlimit, LPXLOPER12 outputrowlimit)
{

	using namespace WDS::Comp::Matrix;

	int i, iM1, j, nrows, ncols;

	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg);
	allow_missings_only_LPXLOPER_or_exit(inputrowlimit);
	allow_missings_only_LPXLOPER_or_exit(outputrowlimit);

	LPXLOPER12 cmArg = nullptr;
	bool bWasArgCoerced = false;
	require_usual_suspect_LPXLOPER(Arg);
	if (lCoerceToMultiIfNecessary(Arg, cmArg, bWasArgCoerced) != xlretSuccess) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		result = new OPER12(L"Error, in coercion in Util.SimpleFirsts");
		if (result != nullptr) result->xltype = result->xltype | xlbitXLFree;
		return result;
	}


	nrows = cmArg->val.array.rows;

	if (!useless_LPXLOPER(inputrowlimit)) {
		int tempint = (int)LPOPER_to_long(inputrowlimit, 0, 0);
		if (tempint < nrows) nrows = tempint;
	}

	int outrows = nrows;
	if (!useless_LPXLOPER(outputrowlimit)) {
		int tempint = (int)LPOPER_to_long(outputrowlimit, 0, 0);
		if (tempint < outrows) outrows = tempint;
	}

	if (nrows <= 1) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		return Arg;
	}

	try {

		j = 1;
		LPXLOPER12 thisrow = nullptr;
		LPXLOPER12 lastrow = &(cmArg->val.array.lparray[0]);
		for (i = 1, iM1 = 0; i < nrows; iM1 = i, i++) {
			thisrow = &(cmArg->val.array.lparray[i]);
			if (thisrow->xltype != lastrow->xltype)
				j++;
			else {
				switch (thisrow->xltype)
				{
				case xltypeStr:
					if (pascal_string_compare(thisrow->val.str, lastrow->val.str) != 0) j++;
					break;
				case xltypeInt:
				case xltypeNum:
					if (thisrow->val.num != lastrow->val.num) j++;
					break;
				case xltypeBool:
					if (thisrow->val.xbool != lastrow->val.xbool) j++;
					break;
				case xltypeErr:
					j++;
					break;
				case xltypeMissing:
				case xltypeNil:
				case xltypeMulti:
				case xltypeSRef:
				case xltypeRef:
					break;
				default:
					break;
				}
			}
			lastrow = thisrow;
		}
		result = new OPER12(j, 1);
		lastrow = nullptr;
		j = -1;
		for (i = 0, iM1 = -1; i < nrows; iM1 = i, i++) {
			thisrow = &(cmArg->val.array.lparray[i]);
			switch (thisrow->xltype)
			{
			case xltypeStr:
				if (i == 0 || lastrow->xltype != xltypeStr || pascal_string_compare(thisrow->val.str, lastrow->val.str)) {
					j++;
					(*result)(j, 0) = pascal_string_to_wstring(thisrow->val.str);
				}
				break;
			case xltypeInt:
			case xltypeNum:
				if (i == 0 || lastrow->xltype != thisrow->xltype || thisrow->val.num != lastrow->val.num) {
					j++;
					(*result)(j, 0) = thisrow->val.num;
				}
				break;
			case xltypeBool:
				if (i == 0 || lastrow->xltype != thisrow->xltype || thisrow->val.xbool != lastrow->val.xbool) {
					j++;
					(*result)(j, 0) = thisrow->val.xbool;
				}
				break;
			case xltypeErr:
				j++;
				(*result)(j, 0) = TempErr12(thisrow->val.err);
				break;
			case xltypeMissing:
			case xltypeMulti:
			case xltypeSRef:
			case xltypeRef:
				break;
			default:
				break;
			}
			lastrow = thisrow;
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or SimpeFirsts");
	}

	lFreeIfNecessary(cmArg, bWasArgCoerced);

	if (result!=nullptr) result->xltype = result->xltype | xlbitXLFree;

	return result;

}



static AddIn XLL_WDS_Util_SimpleSort(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_Util_SimpleSort", 4), L"WDS.Util.SimpleSort")
	.Arg(XLL_LPXLOPER, L"Arg", L"is an column")
	.Arg(XLL_LPXLOPER, L"inputrowlimit", L"is an optional maximum number of rows to consider.")
	.Arg(XLL_LPXLOPER, L"outputrowlimit", L"is an optional maximum number of rows to return.")
	.Arg(XLL_LPXLOPER, L"bReturnJustIndices", L"is an optional flag to return just the sort indices.")
	.Arg(XLL_LPXLOPER, L"inputcolumn", L"is an optional column of a matrix input on which to operate (1-Based).")
	.Arg(XLL_LPXLOPER, L"bReturnJustUnique", L"is an optional flag to return just the unique values (by string rep).")
	.Arg(XLL_LPXLOPER, L"bReverseOrder", L"is an optional flag to reverse the sort order.")
	.Category(L"WDS.Util")
	.FunctionHelp(L"Returns a sorted column.")
);
extern "C" __declspec(dllexport) LPXLOPER12  WINAPI
WDS_Util_SimpleSort(LPXLOPER12 Arg
	, LPXLOPER12 inputrowlimit
	, LPXLOPER12 outputrowlimit
	, LPXLOPER12 bReturnJustIndices
	, LPXLOPER12 inputcolumn
	, LPXLOPER12 bReturnJustUnique
	, LPXLOPER12 bReverseOrder
) {

	using namespace WDS::Comp::Matrix;

	int i, iM1, j, k, kP1, nrows, ncols;
	int firsti, lasti, comp1, comp2;
	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER(Arg);
	allow_missings_only_LPXLOPER_or_exit(inputrowlimit);
	allow_missings_only_LPXLOPER_or_exit(outputrowlimit);
	allow_missings_only_LPXLOPER_or_exit(bReturnJustIndices);
	allow_missings_only_LPXLOPER_or_exit(inputcolumn);

	LPXLOPER12 cmArg = nullptr;
	bool bWasArgCoerced = false;
	require_usual_suspect_LPXLOPER(Arg);
	if (lCoerceToMultiIfNecessary(Arg, cmArg, bWasArgCoerced) != xlretSuccess) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		result = new OPER12(L"Error, in coercion in Util.SimpleFirsts");
		if (result != nullptr) result->xltype = result->xltype | xlbitXLFree;
		return result;
	}


	nrows = cmArg->val.array.rows;
	ncols = cmArg->val.array.columns;

	if (!useless_LPXLOPER(inputrowlimit)) {
		int tempint = (int)LPOPER_to_long(inputrowlimit, 0, 0);
		if (tempint < nrows) nrows = tempint;
	}

	int outrows = nrows;
	if (!useless_LPXLOPER(outputrowlimit)) {
		int tempint = (int)LPOPER_to_long(outputrowlimit, 0, 0);
		if (tempint < outrows) outrows = tempint;
	}

	if (nrows <= 1) {
		lFreeIfNecessary(cmArg, bWasArgCoerced);
		return Arg;
	}

	try {

		bool lbReturnJustIndices = false;
		if (!useless_LPXLOPER(bReturnJustIndices)) {
			lbReturnJustIndices = LPOPER_to_bool(bReturnJustIndices, 0, 0);
		}

		bool lbReturnJustUnique = false;
		if (!useless_LPXLOPER(bReturnJustUnique)) {
			lbReturnJustUnique = LPOPER_to_bool(bReturnJustUnique, 0, 0);
		}

		bool lbReverseOrder = false;
		if (!useless_LPXLOPER(bReverseOrder)) {
			lbReverseOrder = LPOPER_to_bool(bReverseOrder, 0, 0);
		}


		int xcol = 0;
		if (!useless_LPXLOPER(inputcolumn)) {
			xcol = (int)LPOPER_to_long(inputcolumn, 0, 0) - 1;
			ensure(xcol >= 0 && xcol < cmArg->val.array.columns);
		}


		wMatrix wWords(nrows, 1);
		dMatrix dWords(nrows, 1);
		iMatrix ind(nrows, 3, fill::zeros);
		LPXLOPER12 thisrow = nullptr;

		j = -1;
		int outcount = 0;
		for (i = 0, iM1 = -1; i < nrows; iM1 = i, i++) {
			wWords(i, 0) = LPOPER_to_wstring(cmArg, i, xcol);
			thisrow = &(cmArg->val.array.lparray[i*ncols + xcol]);
			ind(i, 0) = thisrow->xltype;
			switch (thisrow->xltype)
			{
			case xltypeInt:
			case xltypeNum:
				dWords(i, 0) = thisrow->val.num;
				break;
			case xltypeBool:
				dWords(i, 0) = (thisrow->val.xbool) ? 1 : 0;
				break;
			case xltypeStr:
			case xltypeErr:
			case xltypeMissing:
			case xltypeMulti:
			case xltypeSRef:
			case xltypeRef:
				break;
			default:
				break;
			}
			if (i == 0) {
				outcount = 1;
				ind(i, 1) = -1;
				ind(i, 2) = -1;
				firsti = 0;
				lasti = 0;
			}
			else if (i == 1) {
				k = wWords(0, 0).compare(wWords(1, 0));
				if (lbReturnJustUnique && k == 0) {
					ind(i, 1) = -2;
				}
				else {
					outcount += 1;
					if ((!lbReverseOrder && k > 0) || (lbReverseOrder && k < 0)) { //less than only element
						firsti = 1;
						ind(1, 1) = -1;
						ind(1, 2) = 0;
						ind(0, 1) = 1;
						ind(0, 2) = -1;
						lasti = 0;
					}
					else { //greater than or equal to only element
						firsti = 0;
						ind(0, 1) = -1;
						ind(0, 2) = 1;
						ind(1, 1) = 0;
						ind(1, 2) = -1;
						lasti = 1;
					}
				}
			}
			else {
				k = firsti;
				kP1 = ind(k, 2);
				bool found = false;
				comp1 = wWords[k].compare(wWords[i]);
				if (lbReturnJustUnique && comp1 == 0) {
					ind(i, 1) = -2;
				}
				else {
					if ((!lbReverseOrder && comp1 >= 0) || (lbReverseOrder && comp1 <= 0)) {
						outcount += 1;
						firsti = i;
						ind(i, 1) = -1;
						ind(i, 2) = k;
						ind(k, 1) = i;
						found = true;
					}
					else {
						k = kP1;
						kP1 = ind(k, 2);
						for (j = 0; (k >= 0) && !found && j < i; j++) { //only have to check against all existing elements
							comp1 = wWords[k].compare(wWords[i]);
							if (lbReturnJustUnique && comp1 == 0) {
								ind(i, 1) = -2;
								found = true;
								break;
							}
							else {
								if ((!lbReverseOrder && comp1 >= 0) || (lbReverseOrder && comp1 <= 0)) {
									outcount += 1;
									ind(i, 1) = ind(k, 1);
									ind(ind(k, 1), 2) = i;
									ind(i, 2) = k;
									ind(k, 1) = i;
									found = true;
									break;
								}
								else {
									k = kP1;
									if (k >= 0) kP1 = ind(k, 2);
								}
								if (k < 0) break;
							}
						}
					}
					if (!found) {
						outcount += 1;
						ind(lasti, 2) = i;
						ind(i, 1) = lasti;
						ind(i, 2) = -1;
						lasti = i;
					}
				}
			}
		}

		result = new OPER12(outcount, 1);
		k = firsti;
		if (lbReturnJustIndices) {
			for (i = 0; i < outcount; i++) {
				(*result)(i, 0) = k + 1;
				k = ind(k, 2);
			}
		}
		else {
			for (i = 0; i < outcount; i++) {
				switch (ind(k, 0))
				{
				case xltypeInt:
				case xltypeNum:
					(*result)(i, 0) = dWords(k, 0);
					break;
				case xltypeBool:
					(*result)(i, 0) = (dWords(k, 0) != 0) ? true : false;
					break;
				case xltypeStr:
					(*result)(i, 0) = wWords(k, 0);
				case xltypeErr:
				case xltypeMissing:
				case xltypeMulti:
				case xltypeSRef:
				case xltypeRef:
					break;
				default:
					break;
				}
				k = ind(k, 2);
			}
		}

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		std::string ew = e.what();
		result = new OPER12(L"Error, in SimpleSort: " + std::wstring(ew.begin(), ew.end()));
	}

	lFreeIfNecessary(cmArg, bWasArgCoerced);

	if (result != nullptr) result->xltype = result->xltype | xlbitXLFree;

	return result;

}

