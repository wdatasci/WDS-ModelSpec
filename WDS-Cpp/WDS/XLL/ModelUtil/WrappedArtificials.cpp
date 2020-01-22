// WrappedArtificials.cpp : wrapping of the C code, WDS/ModelSpec/Artificials.h

#include "ModelUtil.h"

std::wstring pascal_string_to_wstring(wchar_t* str) {
	std::wstring rv = L"";
	size_t j;
	j = (size_t)str[0];
	if (j > 0) {
		rv = std::wstring(&str[1], j);
	}
	return rv;
}

std::wstring xltypeMulti_to_wstring(LPXLOPER12 arg0, size_t r, size_t c)
{
	std::wstring rv;
	XLOPER12 varg1;
	size_t nrows, ncols;
	int rc;
	bool bThrowError = true;
	if (arg0 != nullptr && arg0->xltype == xltypeMulti) {
		try {
			nrows = arg0->val.array.rows;
			ncols = arg0->val.array.columns;
			if (r < nrows && c < ncols) {
				bThrowError = false;
				try {
					switch (arg0->val.array.lparray[c*nrows + r].xltype) {
					case xltypeInt:
					case xltypeNum:
						try {
							rv = std::to_wstring(arg0->val.array.lparray[c*nrows + r].val.num);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					case xltypeStr:
						try {
							rv = pascal_string_to_wstring(arg0->val.array.lparray[c*nrows + r].val.str);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					default:
						rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeStr));
						if (rc != xlretUncalced) {
							try {
								rv = pascal_string_to_wstring((wchar_t*)(varg1.val.str));
							}
							catch (...) {
								bThrowError = true;
							}
						}
						Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
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

double xltypeMulti_to_double(LPXLOPER12 arg0, size_t r, size_t c)
{
	double rv;
	XLOPER12 varg1;
	size_t nrows, ncols;
	int rc;
	bool bThrowError = true;
	if (arg0 != nullptr && arg0->xltype == xltypeMulti) {
		try {
			nrows = arg0->val.array.rows;
			ncols = arg0->val.array.columns;
			if (r < nrows && c < ncols) {
				bThrowError = false;
				try {
					switch (arg0->val.array.lparray[c*nrows + r].xltype) {
					case xltypeInt:
					case xltypeNum:
						try {
							rv = (double)(arg0->val.array.lparray[c*nrows + r].val.num);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					case xltypeStr:
						try {
							rv = std::stod(pascal_string_to_wstring(arg0->val.array.lparray[c*nrows + r].val.str));
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					default:
						rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeNum));
						if (rc != xlretUncalced) {
							try {
								rv = (double)(varg1.val.num);
							}
							catch (...) {
								bThrowError = true;
							}
						}
						Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
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

long xltypeMulti_to_long(LPXLOPER12 arg0, size_t r, size_t c)
{
	long rv;
	XLOPER12 varg1;
	size_t nrows, ncols;
	int rc;
	bool bThrowError = true;
	if (arg0 != nullptr && arg0->xltype == xltypeMulti) {
		try {
			nrows = arg0->val.array.rows;
			ncols = arg0->val.array.columns;
			if (r < nrows && c < ncols) {
				bThrowError = false;
				try {
					switch (arg0->val.array.lparray[c*nrows + r].xltype) {
					case xltypeInt:
					case xltypeNum:
						try {
							rv = (long)(arg0->val.array.lparray[c*nrows + r].val.num);
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					case xltypeStr:
						try {
							rv = std::stol(pascal_string_to_wstring(arg0->val.array.lparray[c*nrows + r].val.str));
						}
						catch (...) {
							bThrowError = true;
						}
						break;
					default:
						rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeNum));
						if (rc != xlretUncalced) {
							try {
								rv = (long)(varg1.val.num);
							}
							catch (...) {
								bThrowError = true;
							}
						}
						Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
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

std::wstring LPOPER_to_wstring(LPXLOPER12 arg0, size_t r, size_t c)
{
	std::wstring rv;
	bool bThrowError = false;
	XLOPER12 varg1;
	bool bUsingvarg1 = false;
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
			case xltypeMissing:
				rv = L"Missing";
				break;
			case xltypeErr:
				rv = L"Error";
				break;
			case xltypeNil:
				rv = L"Nil";
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_wstring(arg0, r, c);
			case xltypeSRef:
			case xltypeRef:
				try {
					bUsingvarg1 = true;
					rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeMulti));
					if (rc == xlretSuccess) {
						try {
							rv = xltypeMulti_to_wstring(&varg1, r, c);
						}
						catch (...) {
							bThrowError = true;
						}
					}
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
	if (bUsingvarg1) Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
	if (bThrowError) throw std::exception("Error in LPOPER_to_wstring");
	return rv;
}

double LPOPER_to_double(LPXLOPER12 arg0, size_t r, size_t c)
{
	double rv;
	bool bThrowError = false;
	XLOPER12 varg1;
	bool bUsingvarg1 = false;
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
			case xltypeMissing:
				rv = NAN;
				break;
			case xltypeErr:
				rv = NAN;
				break;
			case xltypeNil:
				rv = NAN;
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_double(arg0, r, c);
			case xltypeSRef:
			case xltypeRef:
				try {
					bUsingvarg1 = true;
					rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeMulti));
					if (rc == xlretSuccess) {
						try {
							rv = xltypeMulti_to_double(&varg1, r, c);
						}
						catch (...) {
							bThrowError = true;
						}
					}
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
	if (bUsingvarg1) Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
	if (bThrowError) throw std::exception("Error in LPOPER_to_wstring");
	return rv;
}

long LPOPER_to_long(LPXLOPER12 arg0, size_t r, size_t c)
{
	long rv;
	bool bThrowError = false;
	XLOPER12 varg1;
	bool bUsingvarg1 = false;
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
			case xltypeMissing:
				rv = NAN;
				break;
			case xltypeErr:
				rv = NAN;
				break;
			case xltypeNil:
				rv = NAN;
				break;
			case xltypeMulti:
				rv = xltypeMulti_to_long(arg0, r, c);
			case xltypeSRef:
			case xltypeRef:
				try {
					bUsingvarg1 = true;
					rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeMulti));
					if (rc == xlretSuccess) {
						try {
							rv = xltypeMulti_to_long(&varg1, r, c);
						}
						catch (...) {
							bThrowError = true;
						}
					}
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
	if (bUsingvarg1) Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
	if (bThrowError) throw std::exception("Error in LPOPER_to_wstring");
	return rv;
}






using namespace xll;

#include "WDS\ModelSpec\Artificials.h"

static AddIn XLL_WDS_ModelSpec_CleanTreatment(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_CleanTreatment", 4), L"WDS.ModelSpec.CleanTreatment")
	.Arg(XLL_LPXLOPER, L"TreatmentString", L"a variable treatment or alias")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns the standardized treatment name given an alias")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_CleanTreatment(LPOPER12 arg0)
{
	static OPER result;
	XLOPER12 varg1;
	eTreatment Treatment = e_Unknown;
	size_t i, j;
	size_t nrows, ncols;
	int tempint = 0, rc=0;
	std::wstring tempstring;
	long templong = -1;
	try {
		tempstring = LPOPER_to_wstring(arg0, 0, 0);
		Treatment = eTreatmentClean(tempstring.data(), tempstring.length());
		if (Treatment == e_Unknown) {
			templong=LPOPER_to_long(arg0, 0, 0);
			Treatment = eTreatmentFromLong(templong);
		}
	}
	catch (...) {
		templong=LPOPER_to_long(arg0, 0, 0);
		Treatment = eTreatmentFromLong(templong);
	}

	/*
	if (arg0 != nullptr) {
		try {
			switch (arg0->xltype)
			{
			case xltypeInt:
			case xltypeNum:
				templong=LPOPER_to_long(arg0, 0, 0);
				//try {
					//Treatment = eTreatmentFromInt((int)arg0->val.num);
				//}
				//catch (...) {
					//Treatment = e_Unknown;
				//}
				break;
			case xltypeMissing:
			case xltypeErr:
			case xltypeNil:
				break;
			case xltypeMulti:
				nrows = arg0->val.array.rows;
				ncols = arg0->val.array.columns;
				result = OPER(nrows, ncols);
				if (nrows >= 1 && ncols >= 1)
					Treatment = eTreatmentFromInt((int)(arg0->val.array.lparray[0].val.num));
				break;
			case xltypeSRef:
				rc = Excel12f(xlCoerce, &varg1, 2, arg0, TempInt12(xltypeMulti));
				if (rc != xlretUncalced) {
					nrows = varg1.val.array.rows;
					ncols = varg1.val.array.columns;
					if (nrows >= 1 && ncols >= 1) {
						switch (varg1.val.array.lparray[0].xltype) {
						case xltypeInt:
						case xltypeNum:
							try {
								Treatment = eTreatmentFromInt((int)(varg1.val.array.lparray[0].val.num));
							}
							catch (...) {
								Treatment = e_Unknown;
							}
							break;
						case xltypeStr:
							try {
								j = (int)varg1.val.array.lparray[0].val.str[0];
								if (j > 0) {
									tempstring = std::wstring(&varg1.val.array.lparray[0].val.str[1],j);
									Treatment = eTreatmentClean(tempstring.data(), tempstring.length());
								}
								//Treatment = eTreatmentClean(varg1.val.array.lparray[0]);
							}
							catch (...) {
								Treatment = e_Unknown;
							}
							break;
						default:
							Treatment = e_Unknown;
							break;
						}
					}
				}
				Excel12f(xlFree, 0, 1, (LPXLOPER12)&varg1);
				break;
			case xltypeStr:
				tempstring = arg0->to_string();
				Treatment = eTreatmentClean(tempstring.data(), tempstring.length());
				break;
			case xltypeRef:
			default:
				result = OPER(L"if non-Missing/Err/Nil, name_text should be the name (or point to a single range with the name) of an open workbook!");
				break;
			}
		}
		catch (...) {
			Treatment = e_Unknown;
		}
	}
	*/

	tempstring = eTreatmentLabel(Treatment);
	result = OPER(tempstring);
	return &result;
}

