#pragma once

#include "windows.h"
#include "AddIn-xll12.h"
#include <string>
#include "xlcall.h"

//#pragma comment(linker, "/include:" XLL_DECORATE("hey", 4))
//#pragma comment(linker, "/include:" XLL_DECORATE("hey2", 4))
//#pragma comment(linker, "/include:" XLL_DECORATE("hey3", 4))


std::wstring pascal_string_to_wstring(wchar_t* str);

std::wstring xltypeMulti_to_wstring(LPXLOPER12 arg0, size_t r, size_t c);
double xltypeMulti_to_double(LPXLOPER12 arg0, size_t r, size_t c);
long xltypeMulti_to_long(LPXLOPER12 arg0, size_t r, size_t c);

std::wstring LPOPER_to_wstring(LPXLOPER12 arg0, size_t r, size_t c);
double LPOPER_to_double(LPXLOPER12 arg0, size_t r, size_t c);
long LPOPER_to_long(LPXLOPER12 arg0, size_t r, size_t c);





