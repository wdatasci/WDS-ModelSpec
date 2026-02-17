
#include "XLM.h"
#include "ModelUtil.h"
#include <string>

//primarily for any catch (exception e) with unused e
#pragma warning (disable:4101)

using namespace std;
using namespace xll;

//XLM documentation can be obtained online from
//https://www.myonlinetraininghub.com/excel-4-macro-functions
//segments from the help files were extracted from the pdf.

//The basis of the wrappers for GET.WORKSPACE and GET.WORKBOOK came from the xll12/xll24 examples.

// look to Excel V4 macro GET.WORKSPACE documentation for input code
// 23 Full path of the default startup directory or folder.
// 44 A three-column array of all currently registered procedures in dynamic link libraries (DLLs).

AddIn XLLAddIn_WDS_XLM_GET_WORKSPACE(
	Function(XLL_LPOPER, "WDS_XLM_GET_WORKSPACE", "WDS.XLM.GET.WORKSPACE")
	.Arguments({
		Arg(XLL_LPOPER, "type_num", "is a number specifying the type of workspace information you want.")
		})
	.Uncalced()
	.Category("WDS.XLM")
	.FunctionHelp("A wrapper for the XLM Get.Workspace function (from xll24 test.cpp).")
);
LPOPER WINAPI
WDS_XLM_GET_WORKSPACE(LPOPER type_num)
{
#pragma XLLEXPORT
	//static OPER o;
	//o = Excel(xlfGetWorkspace, *type_num);
	//return &o;
	LPOPER result = nullptr;
	try {
		result = new OPER();
		if (Excel12(xlfGetWorkspace, result, 1, *type_num) != 0) {
			Excel12(xlFree, 0, 1, (LPXLOPER12)result);
			result = new OPER(L"Error, in Get.Workspace");
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER(L"Error, in coercion or Get.Workspace");
	}
	//result->xltype = result->xltype | xlbitXLFree;
	return result;
}


AddIn XLLAddIn_WDS_XLM_GET_XLL_NAME(
	Function(XLL_LPOPER, "WDS_XLM_GET_XLL_NAME", "WDS.XLM.GET.XLL_Name")
	.Uncalced()
	.Category("WDS.XLM")
	.FunctionHelp("Get the XLL Name.")
);
LPOPER WINAPI
WDS_XLM_GET_XLL_NAME()
{
#pragma XLLEXPORT
	LPOPER result = nullptr;
	try {
		result = new OPER();
		if (Excel12(xlGetName, result, 0) != 0) {
			Excel12(xlFree, 0, 1, result);
			result = new OPER(L"Error, in Get.XLL_Name");
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12(xlFree, 0, 1, result);
		result = new OPER(L"Error, Get.XLL_Name");
	}
	//result->xltype = result->xltype | xlbitXLFree;

	return result;
}


AddIn XLLAddIn_WDS_XLM_UNREGISTER_XLL(
	Macro("WDS_XLM_UNREGISTER_XLL", "WDS.XLM.UNREGISTER.XLL")
);
int WINAPI
WDS_XLM_UNREGISTER_XLL()
{
#pragma XLLEXPORT
	LPOPER name = nullptr;
	LPOPER result = nullptr;
	try {
		name = new OPER();
		if (Excel12(xlGetName, name, 0) != 0) {
			Excel12(xlFree, 0, 1, (LPXLOPER12)name);
		}
		else {
			result = new OPER();
			Excel12(xlfUnregister, result, 1, name);
		}
	}
	catch (exception& e) {
		return 1;
	}

	return 0;
}

AddIn XLLAddIn_WDS_XLM_GET_WORKBOOK(
	Function(XLL_LPOPER, "WDS_XLM_GET_WORKBOOK", "WDS.XLM.GET.WORKBOOK")
	.Arguments({
		Arg(XLL_LPOPER, "type_num", "is a number that specifies what type of workbook information you want.")
		,Arg(XLL_LPOPER, "name_text", "is the name of an open workbook. If name_text is omitted, it is assumed to be the active workbook.")
		})
	.Uncalced()
	.Category("WDS.XLM")
	.FunctionHelp("A wrapper for the XLM Get.Workspace function.")
);
LPOPER WINAPI
WDS_XLM_GET_WORKBOOK(LPOPER type_num, LPOPER name_text)
{
#pragma XLLEXPORT
	LPOPER result = nullptr;
	wstring tmpstring;
	try {
		result = new OPER();
		wstring tmpstring = LPOPER_to_wstring(name_text,0,0);
		if (useless_LPXLOPER(name_text) || tmpstring.length()==0 ) {
			if (Excel12(xlfGetDocument, result, 1, *type_num) != 0) {
				Excel12(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER(L"Error, in Get.Workbook");
			}
		}
		else {
			//if (Excel12(xlfGetDocument, result, 2, *type_num, OPER(tmpstring)) != 0) {
			if (Excel12(xlfGetDocument, result, 2, *type_num, name_text) != 0) {
				Excel12(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER(L"Error, in Get.Workbook, (check if name is an open workbook)");
			}
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER(L"Error, in coercion or Get.Document");
	}
	//result->xltype = result->xltype | xlbitXLFree;
	return result;
}


AddIn XLLAddIn_WDS_XLM_GET_DOCUMENT(
	Function(XLL_LPOPER, "WDS_XLM_GET_DOCUMENT", "WDS.XLM.GET.DOCUMENT")
	.Arguments({
		Arg(XLL_LPOPER, "type_num", "is a number that specifies what type of information you want.")
		,Arg(XLL_LPOPER, "name_text", "is the name of an open workbook. If name_text is omitted, it is assumed to be the active workbook.")
		})
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function.")
);
LPOPER WINAPI
WDS_XLM_GET_DOCUMENT(LPOPER type_num, LPOPER name_text)
{
#pragma XLLEXPORT
	LPOPER result = nullptr;
	wstring tmpstring;
	try {
		result = new OPER();
		wstring tmpstring = LPOPER_to_wstring(name_text,0,0);
		if (useless_LPXLOPER(name_text) || tmpstring.length()==0 ) {
			if (Excel12(xlfGetDocument, result, 1, *type_num) != 0) {
				Excel12(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER(L"Error, in Get.Document");
			}
		}
		else {
			if (Excel12(xlfGetDocument, result, 2, *type_num, OPER(tmpstring)) != 0) {
				Excel12(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER(L"Error, in Get.Document, (check if name is an open workbook)");
			}
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12(xlFree, 0, 1, (LPXLOPER12)result);
		result = new OPER(L"Error, in coercion or Get.Document");
	}
	//result->xltype = result->xltype | xlbitXLFree;
	return result;
}

