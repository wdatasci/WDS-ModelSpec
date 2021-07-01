
#include "XLM.h"
#include "ModelUtil.h"
#include <string>

using namespace std;
using namespace xll;

//XLM documentation can be obtained online from
//https://www.myonlinetraininghub.com/excel-4-macro-functions
//segments from the help files were extracted from the pdf.

//The basis of the wrappers for GET.WORKSPACE and GET.WORKBOOK came from the xll12 examples.

// look to Excel V4 macro GET.WORKSPACE documentation for input code
// 23 Full path of the default startup directory or folder.
// 44 A three-column array of all currently registered procedures in dynamic link libraries (DLLs).

static AddIn XLLAddIn_WDS_XLM_GET_WORKSPACE(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_XLM_GET_WORKSPACE", 4), L"WDS.XLM.GET.WORKSPACE")
	.Arg(XLL_WORD, L"type_num", L"is a number specifying the type of workspace information you want.")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function (Use.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_XLM_GET_WORKSPACE(WORD type_num)
{
	LPOPER12 result = nullptr;
	try {
		result = new OPER12();
		if (Excel12f(xlfGetWorkspace, result, 1, TempInt12(type_num)) != 0) {
			Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
			result = new OPER12(L"Error, in Get.Workspace");
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or Get.Workspace");
	}
		result->xltype = result->xltype | xlbitXLFree;
	return result;
}


static AddIn XLLAddIn_WDS_XLM_GET_XLL_NAME(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_XLM_GET_XLL_NAME", 4), L"WDS.XLM.GET.XLL_Name")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"Get the XLL Name.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_XLM_GET_XLL_NAME()
{
	LPOPER12 result = nullptr;
	try {
		result = new OPER12();
		if (Excel12f(xlGetName, result, 0) != 0) {
			Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
			result = new OPER12(L"Error, in Get.XLL_Name");
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, Get.XLL_Name");
	}
		result->xltype = result->xltype | xlbitXLFree;

	return result;
}


/*
static AddIn XLLAddIn_WDS_XLM_UNREGISTER_XLL(
	Macro(XLL_DECORATE(L"WDS_XLM_UNREGISTER_XLL", 0), L"WDS.XLM.UNREGISTER.XLL")
);
extern "C" __declspec(dllexport) int WINAPI
WDS_XLM_UNREGISTER_XLL()
{
	LPOPER12 name = nullptr;
	LPOPER12 result = nullptr;
	try {
		name = new OPER12();
		if (Excel12f(xlGetName, name, 0) != 0) {
			Excel12f(xlFree, 0, 1, (LPXLOPER12)name);
		}
		else {
			result = new OPER12();
			Excel12f(xlfUnregister, result, 1, name);
			//Excel12f(xlFree, 0, 1, (LPXLOPER12)name);
			//Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		}
	}
	catch (exception& e) {
		return 1;
		//if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)name);
		//if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
	}

	return 0;
}
*/


static AddIn XLLAddIn_WDS_XLM_GET_WORKBOOK(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_XLM_GET_WORKBOOK", 4), L"WDS.XLM.GET.WORKBOOK")
	.Arg(XLL_WORD, L"type_num", L"is a number that specifies what type of workbook information you want.")
	.Arg(XLL_LPOPER, L"name_text", L"is the name of an open workbook. If name_text is omitted, it is assumed to be the active workbook.")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_XLM_GET_WORKBOOK(WORD type_num, LPOPER12 name_text)
{
	LPOPER12 result = nullptr;
	wstring tmpstring;
	try {
		result = new OPER12();
		wstring tmpstring = LPOPER_to_wstring(name_text,0,0);
		if (useless_LPXLOPER(name_text) || tmpstring.length()==0 ) {
			if (Excel12f(xlfGetDocument, result, 1, TempInt12(type_num)) != 0) {
				Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER12(L"Error, in Get.Workbook");
			}
		}
		else {
			if (Excel12f(xlfGetDocument, result, 2, TempInt12(type_num), OPER(tmpstring)) != 0) {
				Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER12(L"Error, in Get.Workbook, (check if name is an open workbook)");
			}
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or Get.Document");
	}
	result->xltype = result->xltype | xlbitXLFree;
	return result;
}


static AddIn XLLAddIn_WDS_XLM_GET_DOCUMENT(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_XLM_GET_DOCUMENT", 4), L"WDS.XLM.GET.DOCUMENT")
	.Arg(XLL_WORD, L"type_num", L"is a number that specifies what type of information you want.")
	.Arg(XLL_LPXLOPER, L"name_text", L"is the name of an open workbook. If name_text is omitted, it is assumed to be the active workbook.")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_XLM_GET_DOCUMENT(WORD type_num, LPXLOPER12 name_text)
{
	LPOPER12 result = nullptr;
	wstring tmpstring;
	try {
		result = new OPER12();
		wstring tmpstring = LPOPER_to_wstring(name_text,0,0);
		if (useless_LPXLOPER(name_text) || tmpstring.length()==0 ) {
			if (Excel12f(xlfGetDocument, result, 1, TempInt12(type_num)) != 0) {
				Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER12(L"Error, in Get.Document");
			}
		}
		else {
			if (Excel12f(xlfGetDocument, result, 2, TempInt12(type_num), OPER(tmpstring)) != 0) {
				Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER12(L"Error, in Get.Document, (check if name is an open workbook)");
			}
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER12(L"Error, in coercion or Get.Document");
	}
	result->xltype = result->xltype | xlbitXLFree;
	return result;
}
