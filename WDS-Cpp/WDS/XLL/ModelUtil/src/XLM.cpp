
#include "XLM.h"
#include <string>

using namespace xll;

//XLM documentation can be obtained online from
//https://www.myonlinetraininghub.com/excel-4-macro-functions
//segments from the help files were extracted from the pdf.

//The basis of the wrappers for GET.WORKSPACE and GET.WORKBOOK came from the xll12 examples.

// look to Excel V4 macro GET.WORKSPACE documentation for input code
// 23 Full path of the default startup directory or folder.
// 44 A three-column array of all currently registered procedures in dynamic link libraries (DLLs).

static AddIn XLLAddIn_XLM_GET_WORKSPACE(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"XLM_GET_WORKSPACE", 4), L"XLM.GET.WORKSPACE")
	.Arg(XLL_WORD, L"type_num", L"is a number specifying the type of workspace information you want.")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
XLM_GET_WORKSPACE(WORD type_num)
{
	static OPER result;
	result = Excel(xlfGetWorkspace, OPER(type_num));
	return &result;
}


static AddIn XLLAddIn_XLM_GET_WORKBOOK(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"XLM_GET_WORKBOOK", 4), L"XLM.GET.WORKBOOK")
	.Arg(XLL_WORD, L"type_num", L"is a number that specifies what type of workbook information you want.")
	.Arg(XLL_LPOPER, L"name_text", L"is the name of an open workbook. If name_text is omitted, it is assumed to be the active workbook.")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
XLM_GET_WORKBOOK(WORD type_num, LPOPER12 name_text)
{
	static OPER result;
	if (name_text == nullptr) {
		result = Excel(xlfGetWorkbook, OPER(type_num));
	}
	else {
		try {
			switch (name_text->xltype)
			{
			case xltypeMissing:
			case xltypeErr:
			case xltypeNil:
				result = Excel(xlfGetWorkbook, OPER(type_num));
				break;
			case xltypeSRef:
			case xltypeStr:
				result = Excel(xlfGetWorkbook, OPER(type_num), OPER(name_text->to_string()));
				break;
			case xltypeRef:
			default:
				result = OPER(L"if non-Missing/Err/Nil, name_text should be the name (or point to a single range with the name) of an open workbook!");
				break;
			}
		}
		catch (std::exception e) {
			std::string ew = e.what();
			std::wstring ewl = std::wstring(ew.begin(), ew.end());
			result = OPER(ewl);
		}
	}
	return &result;
}


static AddIn XLLAddIn_XLM_GET_DOCUMENT(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"XLM_GET_DOCUMENT", 4), L"XLM.GET.DOCUMENT")
	.Arg(XLL_WORD, L"type_num", L"is a number that specifies what type of information you want.")
	.Arg(XLL_LPOPER, L"name_text", L"is the name of an open workbook. If name_text is omitted, it is assumed to be the active workbook.")
	.Uncalced()
	.Category(L"WDS.XLM")
	.FunctionHelp(L"A wrapper for the XLM Get.Workspace function.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
XLM_GET_DOCUMENT(WORD type_num, LPOPER12 name_text)
{
	static OPER result;
	if (name_text == nullptr) {
		result = Excel(xlfGetDocument, OPER(type_num));
	}
	else {
		try {
			switch (name_text->xltype)
			{
			case xltypeMissing:
			case xltypeErr:
			case xltypeNil:
				result = Excel(xlfGetDocument, OPER(type_num));
				break;
			case xltypeSRef:
			case xltypeStr:
				result = Excel(xlfGetDocument, OPER(type_num), OPER(name_text->to_string()));
				break;
			case xltypeRef:
			default:
				result = OPER(L"if non-Missing/Err/Nil, name_text should be the name (or point to a single range with the name) of an open workbook!");
				break;
			}
		}
		catch (std::exception e) {
			std::string ew = e.what();
			std::wstring ewl = std::wstring(ew.begin(), ew.end());
			result = OPER(ewl);
		}
	}
	return &result;
}


