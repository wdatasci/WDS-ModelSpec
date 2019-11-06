// original is from the dllmain.cpp example from the xll12-master distribution

// dllmain.cpp : Defines the entry point for the DLL application.


#include "ensure.h"
#define NOMINMAX
#define VC_EXTRALEAN
#include "XLCALL.H"
#include "auto.h"

using namespace xll;


HINSTANCE xll_hModule;

#pragma warning(disable: 4100)
extern "C"
BOOL WINAPI
//BOOL APIENTRY 
DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
		xll_hModule = hModule;
		//from the xll12 example
		DisableThreadLibraryCalls(hModule);		
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}


template<class X>
int Auto_(const char* caption)
{
	try {
		Auto<X>::Call();
	}
	catch (const std::exception& ex) {
		MessageBoxA(GetActiveWindow(), ex.what(), caption, MB_OK);

		return FALSE;
	}
	catch (...) {
		MessageBoxA(GetActiveWindow(), "Unknown exception", caption, MB_OK);

		return FALSE;
	}

	return TRUE;
}

// Called by Excel when the xll is opened.
extern "C"
int __declspec(dllexport) WINAPI
xlAutoOpen(void)
{
	int rc;

	rc = Auto_<OpenBefore>(__FUNCTION__);
	if (rc != TRUE)
		return rc;
	rc = Auto_<Open>(__FUNCTION__);
	if (rc != TRUE)
		return rc;
	rc = Auto_<OpenAfter>(__FUNCTION__);

	return rc;
}

extern "C"
int __declspec(dllexport) WINAPI
xlAutoClose(void)
{
	return Auto_<Close>(__FUNCTION__);
}

extern "C"
int __declspec(dllexport) WINAPI
xlAutoAdd(void)
{
	return Auto_<Add>(__FUNCTION__);
}

extern "C"
int __declspec(dllexport) WINAPI
xlAutoRemove(void)
{
	return Auto_<Remove>(__FUNCTION__);
}

extern "C"
void __declspec(dllexport) WINAPI
xlAutoFree12(LPXLOPER12 px)
{
	if (px->xltype & xlbitDLLFree)
		delete px;
	else if (px->xltype & xlbitXLFree)
		Excel12(xlFree, 0, 1, px);
}

extern "C"
LPXLOPER12 __declspec(dllexport) WINAPI
xlAutoRegister12(LPXLOPER12 pxName)
{
	static XLOPER12 xResult;

	xResult = *pxName;

	return &xResult;
}
