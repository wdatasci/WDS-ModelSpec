#pragma once

#include "windows.h"
#include "AddIn-xll12.h"
#include <string>
#include "xlcall.h"
#include "WDS/Comp/Matrix.h"

//#pragma comment(linker, "/include:" XLL_DECORATE("hey", 4))
//#pragma comment(linker, "/include:" XLL_DECORATE("hey2", 4))
//#pragma comment(linker, "/include:" XLL_DECORATE("hey3", 4))


#define useless_LPXLOPER(arg) ( arg == nullptr || arg->xltype == xltypeErr || arg->xltype ==xltypeNil || arg->xltype ==xltypeMissing ) 
//#define non_missing_useless_LPXLOPER(arg) ( arg == nullptr || arg->xltype == xltypeErr || arg->xltype ==xltypeNil ) 
#define non_missing_useless_LPXLOPER(arg) ( arg!=nullptr && (arg->xltype == xltypeErr || arg->xltype ==xltypeNil) ) 

#define usual_suspect_LPXLOPER(arg) (  ! useless_LPXLOPER(arg) )

//idea from KLAX ensure
#define require_usual_suspect_LPXLOPER(arg) if ( useless_LPXLOPER(arg) ) \
		throw std::exception("Usual suspect for: \"" #arg "\" required, file \"" ENSURE_STRZ_(__FILE__) "\" line \"" ENSURE_STRZ_(__LINE__) "\" "); \
		else (void)0;

#define require_usual_suspect_LPXLOPER_or_exit(arg) if ( useless_LPXLOPER(arg) ) \
		{ result=new OPER12("Usual suspect required for " #arg); (*result).xltype = (*result).xltype | xlbitXLFree; return result; }

#define require_string_LPXLOPER_or_exit(arg) if ( useless_LPXLOPER(arg) || arg->xltype!=xltypeStr ) \
		{ result=new OPER12("Usual suspect required for " #arg); (*result).xltype = (*result).xltype | xlbitXLFree; return result; }

#define allow_missings_only_LPXLOPER_or_exit(arg) if ( non_missing_useless_LPXLOPER(arg) ) \
		{ result=new OPER12("Usual suspect required for " #arg); (*result).xltype = (*result).xltype | xlbitXLFree; return result; }


inline int lFreeIfNecessary(LPXLOPER12& target, bool& bWasCoercedFlag) {
	int rc = -1;
	try {
		if (bWasCoercedFlag && target != nullptr) {
			rc = Excel12f(xlFree, 0, 1, (LPXLOPER12)target);
			if (rc != xlretSuccess) throw std::exception("xlFree error"); 
			target = nullptr;
		}
	} 
	catch (std::exception& e) {
	}
	return rc;
}


inline int lCoerceToMultiIfNecessary(LPXLOPER12& arg, LPXLOPER12& target, bool& bWasCoercedFlag) {
	int rc = -1;
	bool bWasTargetNew = false;
	try {
		require_usual_suspect_LPXLOPER(arg);
		ensure(target == nullptr);
		rc = -2;
		if (arg->xltype != xltypeMulti) {
			target = new XLOPER12();
			bWasTargetNew = true;
			rc = Excel12f(xlCoerce, target, 2, arg, TempInt12(xltypeMulti));
			if (useless_LPXLOPER(target)) { rc = -2;  throw std::exception("xlCoerce Error"); }
			bWasCoercedFlag = true;
		}
		else {
			target = arg;
			bWasCoercedFlag = false;
			rc = 0;
		}
	}
	catch (std::exception& e) {
		lFreeIfNecessary(target, bWasTargetNew);
	}
	return rc;
}

std::wstring pascal_string_to_wstring(wchar_t* str);

std::wstring xltypeMulti_to_wstring(LPXLOPER12 arg0, size_t r, size_t c);
double xltypeMulti_to_double(LPXLOPER12 arg0, size_t r, size_t c, bool bStrict, double defv);
long xltypeMulti_to_long(LPXLOPER12 arg0, size_t r, size_t c, bool bStrict, long defv);

std::wstring LPOPER_to_wstring(LPXLOPER12 arg0, size_t r, size_t c);
double LPOPER_to_double(LPXLOPER12 arg0, size_t r, size_t c);
long LPOPER_to_long(LPXLOPER12 arg0, size_t r, size_t c);

	WDS::Comp::Matrix::dMatrix dMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, long defv, bool bLimitRows, long RowLimit, bool bLimitColumns, long ColumnLimit);
	WDS::Comp::Matrix::dMatrix dMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, double defv);
	WDS::Comp::Matrix::iMatrix iMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, long defv, bool bLimitRows, long RowLimit, bool bLimitColumns, long ColumnLimit);
	WDS::Comp::Matrix::iMatrix iMatrixFromLPXLOPER(LPXLOPER12 Arg, bool bStrict, long defv);




