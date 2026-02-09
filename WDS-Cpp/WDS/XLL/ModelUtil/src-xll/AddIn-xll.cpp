// original starts with the DllMain call as in dllmain.cpp example from the xll12-master distribution
//#define NOMINMAX //defined in ensure.h for _WIN32
#include <Windows.h>
#include "ensure.h"
#define VC_EXTRALEAN
#include "XLCALL.H"
#include "auto.h"
#include "xll.h"
//#include "alert.h"
//#include "oper.h"

#define XLL_TRACE // XLL_INFORMATION(__FUNCTION__)

using namespace xll;


#pragma warning(disable: 4100)
extern "C"
BOOL WINAPI
//BOOL APIENTRY 
//DllMain( HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved )
DllMain([[maybe_unused]] HINSTANCE hDLL
	, ULONG ul_reason_for_call
	, [[maybe_unused]] LPVOID lpReserved )
{
	static HINSTANCE xll_hModule;

    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
		xll_hModule = hDLL;
		//from the xll12 example
		DisableThreadLibraryCalls(hDLL);
		break;
    case DLL_THREAD_ATTACH:
		break;
    case DLL_THREAD_DETACH:
		break;
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

//from xll12
//template<class X>
//int Auto_(const char* caption)
//{
//	try {
//		Auto<X>::Call();
//	}
//	catch (const std::exception& ex) {
//		MessageBoxA(GetActiveWindow(), ex.what(), caption, MB_OK);
//
//		return FALSE;
//	}
//	catch (...) {
//		MessageBoxA(GetActiveWindow(), "Unknown exception", caption, MB_OK);
//
//		return FALSE;
//	}
//
//	return TRUE;
//}


//in xll24, this is in xlauto.cpp
// Called by Excel when the xll is opened.
extern "C"
int __declspec(dllexport) WINAPI
xlAutoOpen(void)
{
	//from xll12
	//int rc;
	//rc = Auto_<OpenBefore>(__FUNCTION__);
	//if (rc != TRUE)
	//	return rc;
	//rc = Auto_<Open>(__FUNCTION__);
	//if (rc != TRUE)
	//	return rc;
	//rc = Auto_<OpenAfter>(__FUNCTION__);
	//return rc;
	//from xll24
	XLL_TRACE;
	try {
		ensure(Auto<Open>::Call());
		ensure(Auto<Register>::Call());
		ensure(Auto<OpenAfter>::Call());
	}
	catch (const std::exception& ex) {
		XLL_ERROR(ex.what());
		return FALSE;
	}
	catch (...) {
		XLL_ERROR(__FUNCTION__ ": unknown exception");
		return FALSE;
	}
	return TRUE;
}

extern "C"
int __declspec(dllexport) WINAPI
xlAutoClose(void)
{
	//xll12
	//return Auto_<Close>(__FUNCTION__);
	//xll24
	XLL_TRACE;
	try {
		ensure(Auto<CloseBefore>::Call());
		ensure(Auto<Close>::Call());
	}
	catch (const std::exception& ex) {
		XLL_ERROR(ex.what());
		return FALSE;
	}
	catch (...) {
		XLL_ERROR(__FUNCTION__ ": unknown exception");
		return FALSE;
	}
	return TRUE;
}

extern "C" int __declspec(dllexport) WINAPI
xlAutoAdd(void)
{
	//xll12
	//return Auto_<Add>(__FUNCTION__);
	//xll24
	XLL_TRACE;
	try {
		ensure(Auto<Add>::Call());
	}
	catch (const std::exception& ex) {
		XLL_ERROR(ex.what());
		return FALSE;
	}
	catch (...) {
		XLL_ERROR("Unknown exception in xlAutoAdd");
		return FALSE;
	}
	return TRUE;
}

extern "C" int __declspec(dllexport) WINAPI
xlAutoRemove(void)
{
	//xll12
	//return Auto_<Remove>(__FUNCTION__);
	//xll24
	XLL_TRACE;
	try {
		ensure(Auto<Remove>::Call());
		ensure(Auto<Unregister>::Call());
	}
	catch (const std::exception& ex) {
		XLL_ERROR(ex.what());
		return FALSE;
	}
	catch (...) {
		XLL_ERROR("Unknown exception in xlAutoRemove");
		return FALSE;
	}
	return TRUE;
}

extern "C" void __declspec(dllexport) WINAPI
xlAutoFree12(LPXLOPER12 px)
{
	//xll12
	//if (px->xltype & xlbitDLLFree)
	//	delete px;
	//else if (px->xltype & xlbitXLFree)
	//	Excel12(xlFree, 0, 1, px);
	//xll24
	XLL_TRACE;
	if (px->xltype & xlbitDLLFree) {
		px->xltype &= ~xlbitDLLFree;
		static_cast<OPER*>(px)->~OPER();
	}
}

extern "C" LPXLOPER12 __declspec(dllexport) WINAPI
xlAutoRegister12(const LPXLOPER12 pxName)
{
	//xll12
	//static XLOPER12 xResult;
	//xResult = *pxName;
	//return &xResult;
	//xll24
	XLL_TRACE;
	static XLOPER12 o;
	try {
		auto addin = AddIn::find(OPER(*pxName));
		o = addin ? XlfRegister(addin) : ErrValue;
	}
	catch (const std::exception& ex) {
		XLL_ERROR(ex.what());
		o = ErrValue;
	}
	catch (...) {
		XLL_ERROR("Unknown exception in xlAutoRegister12");
		o = ErrValue;
	}
	return &o;
}

//xll12
//extern "C" const XLOPER12* WINAPI
//xlAddInManagerInfo12(LPXLOPER12 pxAction)
//{
//	XLL_TRACE;
//	static OPER xInfo;
//	if (Excel(xlCoerce, *pxAction, OPER(xltypeInt)) == 1) {
//		xInfo = AddInManagerInfo();
//	}
//	else {
//		xInfo = ErrValue;
//	}
//	return &xInfo;
//}
//xl24
extern "C" const XLOPER12* WINAPI
xlAddInManagerInfo12(LPXLOPER12 pxAction)
{
	XLL_TRACE;
	static XLOPER12 errValue{ Err(xlerrValue) };
	if (Excel(xlCoerce, *pxAction, OPER(xltypeInt)) == 1) {
		return AddInManagerInfo();
	}
	return &errValue;
}



