//a few pieces from FRAMEWRK.C of the Excel2013SDK until they can be removed

#include <windows.h>
#include <malloc.h>
#include <wchar.h>
#include "XLCALL.H"
#include "XLCALL.CPP"
#include "FRAMEWRK.H"
#include "MemoryManager.h"
#include <stdarg.h>

#ifdef __cplusplus
extern "C" {
#endif

LPSTR GetTempMemory(size_t cBytes)
{
	return MGetTempMemory(cBytes);
}

void FreeAllTempMemory(void)
{
	MFreeAllTempMemory();
}


#ifdef __cplusplus
}
#endif

