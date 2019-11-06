//The xll12 error messaging manipulates the registry, which is avoided here.

#include <exception>
#include "error.h" // the xll12 error header

using namespace std;

//replacements for the base xll12 function to eliminate the registry calls

int
XLL_ALERT(const char* text, const char* caption, DWORD level, UINT type, bool force)
{
	try {
		//if ((xll_alert_level&level) || force) {
		(IDCANCEL == MessageBoxA(GetForegroundWindow(), text, caption, MB_OKCANCEL | type));
			//if (IDCANCEL == MessageBoxA(GetForegroundWindow(), text, caption, MB_OKCANCEL | type))
				//xll_alert_level = (xll_alert_level & ~level);
		//}
	}
	catch (const std::exception& ex) {
		MessageBoxA(GetForegroundWindow(), ex.what(), "Alert", MB_OKCANCEL | MB_ICONERROR);
	}

	//return static_cast<int>(xll_alert_level);
	return static_cast<int>(XLL_ALERT_WARNING);
}

//from xll12-master error.cpp
int
XLL_ERROR(const char* e, bool force)
{
	return XLL_ALERT(e, "Error", XLL_ALERT_ERROR, MB_ICONERROR, force);
}
int
XLL_WARNING(const char* e, bool force)
{
	return XLL_ALERT(e, "Warning", XLL_ALERT_WARNING, MB_ICONWARNING, force);
}
int
XLL_INFO(const char* e, bool force)
{
	return XLL_ALERT(e, "Information", XLL_ALERT_INFO, MB_ICONINFORMATION, force);
}
