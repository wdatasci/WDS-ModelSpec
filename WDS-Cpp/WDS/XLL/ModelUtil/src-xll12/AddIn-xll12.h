// based on the xll.h from the xll12-master distribution

#pragma once
#define _CRT_SECURE_NO_WARNINGS
//#define NENSURE    //use to kill xll12 "ensure" replacement for "assert"
//#define NOMINMAX   //moved as a global preprocessor definition
#define VC_EXTRALEAN
#define WIN32_LEAN_AND_MEAN
#include <Windows.h>


// Module handle from DllMain
extern HINSTANCE xll_hModule;
extern HINSTANCE xll_Instance;

#include "fp.h"
#include "error.h"
#include "on.h"
#include "addin.h"
#include "handle.h"
//#include "test.h"

//#include "XLCALL.H"
#include "FRAMEWRK.H"


//#ifndef _LIB
//#pragma comment(linker, "/include:" XLL_DECORATE("xll_this", 0))
//#pragma comment(linker, "/include:" XLL_DECORATE("xll_trace", 4))
////#pragma comment(linker, "/include:" XLL_DECORATE("xll_paste_function", 0))
////#pragma comment(linker, "/include:" XLL_DECORATE("xll_make_doc", 0))
//#pragma comment(linker, "/include:" XLL_DECORATE("xll_make_shfb", 0))
//#pragma comment(linker, "/include:" XLL_DECORATE("xll_get_workbook", 4))
//#pragma comment(linker, "/include:" XLL_DECORATE("xll_get_workspace", 4))
//#endif // _LIB


