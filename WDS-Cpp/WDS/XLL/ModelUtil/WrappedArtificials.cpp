// WrappedArtificials.cpp : wrapping of the C code, WDS/ModelSpec/Artificials.h

#include "ModelUtil.h"
//#include "WDS\Comp\Matrix.h"
using namespace WDS::Comp::Matrix;


using namespace xll;

#include "WDS\ModelSpec\Artificials.h"
namespace WDS::ModelSpec {

eTreatment lCleanTreatment(LPXLOPER12 arg0) {
	eTreatment result = e_Unknown;
	std::wstring tempstring;
	long templong = -1;
	try {
		tempstring = LPOPER_to_wstring(arg0, 0, 0);
		result = eTreatmentClean(tempstring.data(), tempstring.length());
		if (result == e_Unknown) {
			templong = LPOPER_to_long(arg0, 0, 0);
			result = eTreatmentFromLong(templong);
		}
	}
	catch (...) {
		//try {
		//	templong = LPOPER_to_long(arg0, 0, 0);
		//	result = eTreatmentFromLong(templong);
		//}
		//catch (...) {
			result = e_Unknown;
		//}
	}
	return result;
}


static AddIn XLL_WDS_ModelSpec_CleanTreatment(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_CleanTreatment", 4), L"WDS.ModelSpec.CleanTreatment")
	.Arg(XLL_LPXLOPER, L"TreatmentString", L"a variable treatment or alias")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns the standardized treatment name given an alias")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_CleanTreatment(LPOPER12 arg0)
{
	LPOPER result=nullptr;
	require_usual_suspect_LPXLOPER_or_exit(arg0);
	eTreatment Treatment = lCleanTreatment(arg0);
	std::wstring tempstring;
	tempstring = eTreatmentLabel(Treatment);
	result = new OPER(tempstring);
	if (result != nullptr) (*result).xltype = (*result).xltype | xlbitXLFree;
	return result;
}

static AddIn XLL_WDS_ModelSpec_nArtificialCount(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_nArtificialCount", 4), L"WDS.ModelSpec.nArtificialCount")
	.Arg(XLL_LPXLOPER, L"nCriticalValues", L"the number of critical values used")
	.Arg(XLL_LPXLOPER, L"TreatmentString", L"a variable treatment or alias")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns the count of artificials created for a given critical value set and a treatment")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_nArtificialCount(LPXLOPER12 _nCriticalValues, LPOPER12 _Treatment)
{
	LPOPER result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(_nCriticalValues);
	require_usual_suspect_LPXLOPER_or_exit(_Treatment);
	LPXLOPER12 __nCriticalValues = nullptr;
	bool bWas_nCriticalValuesCoerced = false;
	try {
		if (lCoerceToMultiIfNecessary(_nCriticalValues, __nCriticalValues, bWas_nCriticalValuesCoerced) != 0)
			throw exception("Coerce error for nCriticalValues in nArtificialsCount.");
		int nCriticalValues = (int)LPOPER_to_long(__nCriticalValues,0,0);
		eTreatment Treatment = lCleanTreatment(_Treatment);
		int rv = nArtificialCount(nCriticalValues, Treatment);
		result = new OPER(rv);
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		std::string ew = e.what();
		result = new OPER12(L"Error, in nArtificialsCount: " + std::wstring(ew.begin(), ew.end()));
	}

	lFreeIfNecessary(__nCriticalValues, bWas_nCriticalValuesCoerced);

	if (result != nullptr) (*result).xltype = (*result).xltype | xlbitXLFree;
	return result;
}

static AddIn XLL_WDS_ModelSpec_ArtificialLabels(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_ArtificialLabels", 4), L"WDS.ModelSpec.ArtificialLabels")
	.Arg(XLL_LPXLOPER, L"nCriticalValues", L"the number of critical values used")
	.Arg(XLL_LPXLOPER, L"TreatmentString", L"a variable treatment or alias")
	.Arg(XLL_LPXLOPER, L"LabelBase", L"(optional) base variable name, defaults to X")
	.Arg(XLL_LPXLOPER, L"LabelConnector", L"(optional) connector between label parts")
	.Arg(XLL_LPXLOPER, L"LabelSuffix", L"(optional) at the end of each label")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns the count of artificials created for a given critical value set and a treatment")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_ArtificialLabels(LPXLOPER12 _nCriticalValues, LPOPER12 _Treatment, LPOPER12 _LabelBase, LPOPER12 _LabelConnector, LPOPER12 _LabelSuffix)
{
	LPOPER result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(_nCriticalValues);
	require_usual_suspect_LPXLOPER_or_exit(_Treatment);
	LPXLOPER12 __nCriticalValues = nullptr;
	bool bWas_nCriticalValuesCoerced = false;
	std::wstring LabelBase = LPOPER_to_wstring(_LabelBase, 0, 0,L"X");
	std::wstring LabelConnector = LPOPER_to_wstring(_LabelConnector, 0, 0);
	std::wstring LabelSuffix = LPOPER_to_wstring(_LabelSuffix, 0, 0);
	try {
		if (lCoerceToMultiIfNecessary(_nCriticalValues, __nCriticalValues, bWas_nCriticalValuesCoerced) != 0)
			throw exception("Coerce error for nCriticalValues in ArtificialLabels.");
		int nCriticalValues = (int)LPOPER_to_long(__nCriticalValues,0,0);
		eTreatment Treatment = lCleanTreatment(_Treatment);
		int rv = nArtificialCount(nCriticalValues, Treatment);
		int first = nArtificialIndex_First(nCriticalValues, Treatment);
		result = new OPER12(1,rv);
		int i, j;
		std::wstring w;
		for (i = 0, j = first; i < rv; i++, j++) {
			w = LabelBase + LabelConnector + to_wstring(j) + LabelSuffix;
			(*result)(0, i) = w;
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		std::string ew = e.what();
		result = new OPER12(L"Error, in ArtificialLabels: " + std::wstring(ew.begin(), ew.end()));
	}

	lFreeIfNecessary(__nCriticalValues, bWas_nCriticalValuesCoerced);

	if (result != nullptr) (*result).xltype = (*result).xltype | xlbitXLFree;
	return result;
}


static AddIn XLL_WDS_ModelSpec_ScoreLabels(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_ScoreLabels", 4), L"WDS.ModelSpec.ScoreLabels")
	.Arg(XLL_LPXLOPER, L"nScores", L"the number of critical values used")
	.Arg(XLL_LPXLOPER, L"LabelBase", L"(optional) base variable name, defaults to X")
	.Arg(XLL_LPXLOPER, L"LabelConnector", L"(optional) connector between label parts")
	.Arg(XLL_LPXLOPER, L"LabelSuffix", L"(optional) at the end of each label")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns the count of artificials created for a given critical value set and a treatment")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_ScoreLabels(LPXLOPER12 _nScores, LPOPER12 _LabelBase, LPOPER12 _LabelConnector, LPOPER12 _LabelSuffix)
{
	LPOPER result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(_nScores);
	LPXLOPER12 __nScores = nullptr;
	bool bWas_nScoresCoerced = false;
	std::wstring LabelBase = LPOPER_to_wstring(_LabelBase, 0, 0,L"X");
	std::wstring LabelConnector = LPOPER_to_wstring(_LabelConnector, 0, 0);
	std::wstring LabelSuffix = LPOPER_to_wstring(_LabelSuffix, 0, 0);
	try {
		if (lCoerceToMultiIfNecessary(_nScores, __nScores, bWas_nScoresCoerced) != 0)
			throw exception("Coerce error for nScores in ScoreLabels.");
		int nScores = (int)LPOPER_to_long(__nScores,0,0);
		int first = 1;
		result = new OPER12(1,nScores);
		int i, j;
		std::wstring w;
		for (i = 0, j = first; i < nScores; i++, j++) {
			w = LabelBase + LabelConnector + to_wstring(j) + LabelSuffix;
			(*result)(0, i) = w;
		}
	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		std::string ew = e.what();
		result = new OPER12(L"Error, in ScoreLabels: " + std::wstring(ew.begin(), ew.end()));
	}

	lFreeIfNecessary(__nScores, bWas_nScoresCoerced);

	if (result != nullptr) (*result).xltype = (*result).xltype | xlbitXLFree;
	return result;
}





static AddIn XLL_WDS_ModelSpec_Artificials(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_Artificials", 4), L"WDS.ModelSpec.Artificials")
	.Arg(XLL_LPXLOPER, L"XInput", L"a column vector of source variable values")
	.Arg(XLL_LPXLOPER, L"TreatmentString", L"variable spec treatment")
	.Arg(XLL_LPXLOPER, L"CriticalValues", L"critical values for the variable spec")
	.Arg(XLL_LPXLOPER, L"CleanLimits", L"(optional) clean limits for the variable spec")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns a matrix of processed artificial variables based on a column input and variable specs.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_Artificials(
	LPXLOPER12 XInput
	, LPXLOPER12 TreatmentString
	, LPXLOPER12 CriticalValues
	, LPXLOPER12 CleanLimits
) {
	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(XInput);
	require_usual_suspect_LPXLOPER_or_exit(TreatmentString);
	allow_missings_only_LPXLOPER_or_exit(CriticalValues);
	allow_missings_only_LPXLOPER_or_exit(CleanLimits);

	eTreatment Treatment = lCleanTreatment(TreatmentString);
	if (Treatment == e_None || Treatment == e_Unknown) return XInput;
	ensure(Treatment != e_Unknown);


	LPXLOPER12 cmXInput = nullptr;
	bool bWasXInputCoerced = false;
	LPXLOPER12 cmCriticalValues = nullptr;
	bool bWasCriticalValuesCoerced = false;
	LPXLOPER12 cmCleanLimits = nullptr;
	bool bWasCleanLimitsCoerced = false;

	try {

		int rc = 0;
		if (lCoerceToMultiIfNecessary(XInput, cmXInput, bWasXInputCoerced)!=0)
					throw exception("Coerce error for XInput in Artificials.");
		ensure(cmXInput->val.array.columns == 1);

		int nrows, ncols;
		size_t i, j, ij;
		size_t nArts, nArts_first, nArts_last;

		nrows = cmXInput->val.array.rows;
		ncols = 1;
		mIndex mi = 0;
		mIndex mj = 0;
		double tempdouble = 0;

		if (lCoerceToMultiIfNecessary(CriticalValues, cmCriticalValues, bWasCriticalValuesCoerced)!=0)
			throw std::exception("Coerce error for CriticalValues in Artificials.");

		size_t nCrit_nrows, nCrit_ncols, nCLs, nCL_nrows, nCL_ncols;
		nCrit_nrows = cmCriticalValues->val.array.rows;
		nCrit_ncols = cmCriticalValues->val.array.columns;
		ensure((int)nCrit_ncols >= 1);

		if (Treatment == e_Constant) {
			try {
				tempdouble = LPOPER_to_double(cmCriticalValues, 0, 0);
				result = new OPER12(nrows, ncols);
				for (i = 0; i < nrows; i++)
					(*result)(i, 0) = tempdouble;
			}
			catch (...) {
				if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
				result = new OPER12(L"Error, in coercion product first element of CriticalValues");
			}

		}
		else if (Treatment == e_Categorical) {

			wstring* X = nullptr;
			//X = (wstring*)malloc(sizeof(wstring)*nrows);
			X = new wstring[nrows];

			for (i = 0; i < nrows; i++) {
				try {
					X[i] = LPOPER_to_wstring(cmXInput, i, 0);
				}
				catch (...) {
					X[i] = L"";
				}
			}

			int* nCrits = nullptr;
			nCrits = (int*)malloc(sizeof(int)*(nCrit_ncols + 1));
			nCrits[0] = nCrit_ncols;

			wstring** Crits = nullptr;
			//Crits = (wstring**)malloc(sizeof(wstring*)*nCrit_ncols);
			Crits = new wstring*[nCrit_ncols];
			for (i = 0; i < nCrit_ncols; i++) {
				//Crits[i] = (wstring*)malloc(sizeof(wstring)*(nCrit_nrows + 1));
				Crits[i] = new wstring[nCrit_nrows + 1];
				nCrits[i + 1] = 0;
				for (j = 0; j < nCrit_nrows; j++) {
					try {
						Crits[i][j] = LPOPER_to_wstring(cmCriticalValues, j, i);
						nCrits[i + 1] += 1;
					}
					catch (...) {
						Crits[i][j] = wstring();
					}
				}
				Crits[i][j] = wstring();
			}


			int nCL_nrows = 0, nCL_ncols = 0, nCLs = 0;

			nArts = nArtificialCount(nCrit_ncols, Treatment);
			nArts_first = nArtificialIndex_First(nCrit_ncols, Treatment);
			nArts_last = nArtificialIndex_Last(nCrit_ncols, Treatment);

			double* A = nullptr;
			A = (double*)malloc(sizeof(double)*nrows*nArts);
			memset(A, 0, sizeof(double)*nrows*nArts);

			int rc;

			rc = fArtificials_Categorical(X, nrows, Treatment, Crits, nCrits, NULL, 0, A, nArts, nrows, nArts, 0, 0, false);
			for (i = 0; i < nCrit_ncols; i++) {
				delete[] Crits[i];
			}
			delete[] Crits;
			free(nCrits);
			delete[] X;


			result = new OPER12(nrows, nArts);
			for (j = 0, ij = 0; j < nArts; j++) {
				for (i = 0; i < nrows; i++, ij++) {
					(*result)(i, j) = A[ij];
				}
			}

			free(A);

		}
		else if (Treatment == e_CategoricalNumeric) {

			double* X = nullptr;
			X = (double*)malloc(sizeof(double)*nrows);

			for (i = 0; i < nrows; i++) {
				try {
					X[i] = LPOPER_to_double(cmXInput, i, 0);
				}
				catch (...) {
					X[i] = nan("");
				}
			}

			nCrit_nrows = cmCriticalValues->val.array.rows;
			nCrit_ncols = cmCriticalValues->val.array.columns;
			int* nCrits = nullptr;
			nCrits = (int*)malloc(sizeof(int)*(nCrit_ncols + 1));
			nCrits[0] = nCrit_ncols;

			double** Crits = nullptr;
			Crits = (double**)malloc(sizeof(double*)*nCrit_ncols);
			for (i = 0; i < nCrit_ncols; i++) {
				Crits[i] = (double*)malloc(sizeof(double)*(nCrit_nrows + 1));
				nCrits[i + 1] = 0;
				for (j = 0; j < nCrit_nrows; j++) {
					try {
						Crits[i][j] = LPOPER_to_double(cmCriticalValues, j, i);
						nCrits[i + 1] += 1;
					}
					catch (...) {
						Crits[i][j] = nan("");
					}
				}
				Crits[i][j] = nan("");
			}


			int nCL_nrows = 0, nCL_ncols = 0, nCLs = 0;

			nArts = nArtificialCount(nCrit_ncols, Treatment);
			nArts_first = nArtificialIndex_First(nCrit_ncols, Treatment);
			nArts_last = nArtificialIndex_Last(nCrit_ncols, Treatment);

			double* A = nullptr;
			A = (double*)malloc(sizeof(double)*nrows*nArts);
			memset(A, 0, sizeof(double)*nrows*nArts);

			int rc;

			rc = fArtificials_CategoricalNumeric(X, nrows, Treatment, Crits, nCrits, NULL, 0, A, nArts, nrows, nArts, 0, 0, false);
			for (i = 0; i < nCrit_ncols; i++) {
				free(Crits[i]);
			}
			free(Crits);
			free(nCrits);
			free(X);

			result = new OPER12(nrows, nArts);
			for (j = 0, ij = 0; j < nArts; j++) {
				for (i = 0; i < nrows; i++, ij++) {
					(*result)(i, j) = A[ij];
				}
			}

			free(A);

		}
		else {

			double* X = nullptr;
			X = (double*)malloc(sizeof(double)*nrows);

			for (i = 0; i < nrows; i++) {
				try {
					X[i] = LPOPER_to_double(cmXInput, i, 0);
				}
				catch (...) {
					X[i] = nan("");
				}
			}

			nCrit_nrows = cmCriticalValues->val.array.rows;
			nCrit_ncols = cmCriticalValues->val.array.columns;
			int nCrits = nCrit_ncols;
			double* Crits = nullptr;
			if (nCrit_ncols == 1 && nCrit_nrows > 1) {
				nCrits = nCrit_nrows;
			}
			Crits = (double*)malloc(sizeof(double)*nCrits);
			for (i = 0; i < nCrits; i++) {
				try {
					if (nCrits != nCrit_ncols)
						Crits[i] = LPOPER_to_double(cmCriticalValues, i, 0);
					else
						Crits[i] = LPOPER_to_double(cmCriticalValues, 0, i);
				}
				catch (...) {
				}
			}

			int nCL_nrows = 0, nCL_ncols = 0, nCLs = 0;
			//dMatrix CLs;
			double* CLs = nullptr;

			if (usual_suspect_LPXLOPER(CleanLimits)) {
				if (lCoerceToMultiIfNecessary(CleanLimits, cmCleanLimits, bWasCleanLimitsCoerced) != 0)
					throw exception("Coerce error for CleanLimits in Artificials.");
				nCL_nrows = cmCleanLimits->val.array.rows;
				nCL_ncols = cmCleanLimits->val.array.columns;
				nCLs = nCL_ncols;
				if (nCL_ncols == 1 && nCL_nrows > 1) {
					nCLs = nCL_nrows;
				}
				CLs = (double*)malloc(sizeof(double)*nCLs);
				for (i = 0; i < nCLs; i++) {
					try {
						if (nCLs != nCL_ncols)
							CLs[i] = LPOPER_to_double(cmCleanLimits, i, 0);
						else
							CLs[i] = LPOPER_to_double(cmCleanLimits, 0, i);
					}
					catch (...) {
					}
				}
			}

			nArts = nArtificialCount(nCrits, Treatment);
			nArts_first = nArtificialIndex_First(nCrits, Treatment);
			nArts_last = nArtificialIndex_Last(nCrits, Treatment);

			//double* A = nullptr;
			//A = (double*)malloc(sizeof(double)*nrows*nArts);
			//memset(A, 0, sizeof(double)*nrows*nArts);
			dMatrix A(nrows, nArts, fill::zeros);

			int rc;

			rc = fArtificials_Numeric(X, nrows, Treatment, Crits, nCrits, CLs, nCLs, A.memptr(), nArts, nrows, nArts, 0, 0, false);

			result = new OPER12(nrows, nArts);
			for (j = 0, ij = 0; j < nArts; j++) {
				for (i = 0; i < nrows; i++, ij++) {
					(*result)(i, j) = A[ij];
				}
			}

			free(X);
			free(Crits);
			free(CLs);
			//free(A);


		}

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		std::string ew = e.what();
		result = new OPER12(L"Error, in Artificials: "+std::wstring(ew.begin(), ew.end()));
	}

	lFreeIfNecessary(cmXInput, bWasXInputCoerced);
	lFreeIfNecessary(cmCriticalValues, bWasCriticalValuesCoerced);
	lFreeIfNecessary(cmCleanLimits, bWasCleanLimitsCoerced);

	if (result != nullptr) result->xltype = result->xltype | xlbitXLFree;
	return result;


}

static AddIn XLL_WDS_ModelSpec_ArtificialsScored(
	Function(XLL_LPXLOPER, XLL_DECORATE(L"WDS_ModelSpec_ArtificialsScored", 4), L"WDS.ModelSpec.ArtificialsScored")
	.Arg(XLL_LPXLOPER, L"XInput", L"a column vector of source variable values")
	.Arg(XLL_LPXLOPER, L"TreatmentString", L"variable spec treatment")
	.Arg(XLL_LPXLOPER, L"CriticalValues", L"critical values for the variable spec")
	.Arg(XLL_LPXLOPER, L"CleanLimits", L"(optional) clean limits for the variable spec")
	.Arg(XLL_LPXLOPER, L"Coefficients", L"coefficient values for the variable spec, rectangular and assumed to be nScores x nArtificials")
	.Category(L"WDS.ModelSpec")
	.FunctionHelp(L"Returns a matrix of processed and scored artificial variables based on a column input and variable specs.")
);
extern "C" __declspec(dllexport) LPXLOPER12 WINAPI
WDS_ModelSpec_ArtificialsScored(
	LPXLOPER12 XInput
	, LPXLOPER12 TreatmentString
	, LPXLOPER12 CriticalValues
	, LPXLOPER12 CleanLimits
	, LPXLOPER12 Coefficients
) {
	LPOPER12 result = nullptr;
	require_usual_suspect_LPXLOPER_or_exit(XInput);
	require_usual_suspect_LPXLOPER_or_exit(TreatmentString);
	allow_missings_only_LPXLOPER_or_exit(CriticalValues);
	allow_missings_only_LPXLOPER_or_exit(CleanLimits);
	require_usual_suspect_LPXLOPER_or_exit(Coefficients);

	LPXLOPER12 cmXInput = nullptr;
	bool bWasXInputCoerced = false;
	LPXLOPER12 cmCriticalValues = nullptr;
	bool bWasCriticalValuesCoerced = false;
	LPXLOPER12 cmCleanLimits = nullptr;
	bool bWasCleanLimitsCoerced = false;
	LPXLOPER12 cmCoefficients = nullptr;
	bool bWasCoefficientsCoerced = false;

	try {

		eTreatment Treatment = lCleanTreatment(TreatmentString);
		if (Treatment == e_None) return XInput;
		ensure(Treatment != e_Unknown);

		int rc = 0;
		if (lCoerceToMultiIfNecessary(XInput, cmXInput, bWasXInputCoerced) != 0)
			throw exception("Coerce error for XInput in ArtificialsScored.");
		ensure(cmXInput->val.array.columns == 1);

		int nrows, ncols;
		size_t i, j, ij;
		size_t nArts, nArts_first, nArts_last;
		size_t nResults, nResults_first, nResults_last;

		nrows = cmXInput->val.array.rows;
		ncols = 1;
		mIndex mi = 0;
		mIndex mj = 0;
		double tempdouble = 0;

		if (lCoerceToMultiIfNecessary(CriticalValues, cmCriticalValues, bWasCriticalValuesCoerced) != 0)
			throw exception("Coerce error for CriticalValues in ArtificialsScored.");
		size_t nCrit_nrows, nCrit_ncols, nCLs, nCL_nrows, nCL_ncols;
		nCrit_nrows = cmCriticalValues->val.array.rows;
		nCrit_ncols = cmCriticalValues->val.array.columns;
		ensure(nCrit_ncols >= 1);

		if (lCoerceToMultiIfNecessary(Coefficients, cmCoefficients, bWasCoefficientsCoerced) != 0)
			throw exception("Coerce error for Coefficients in ArtificialsScored.");
		dMatrix Coeffs = dMatrixFromLPXLOPER(cmCoefficients, false, 0.0);
		size_t nCoef_nrows, nCoef_ncols;
		nCoef_nrows = Coeffs.nrows();
		nCoef_ncols = Coeffs.ncols();

		nArts = nArtificialCount(nCrit_ncols, Treatment);
		nArts_first = nArtificialIndex_First(nCrit_ncols, Treatment);
		nArts_last = nArtificialIndex_Last(nCrit_ncols, Treatment);

		ensure(nCoef_ncols >= 1 && nCoef_ncols == nArts);

		if (Treatment == e_Categorical) {

			wstring* X = nullptr;
			//X = (wstring*)malloc(sizeof(wstring)*nrows);
			X = new wstring[nrows];

			for (i = 0; i < nrows; i++) {
				try {
					X[i] = LPOPER_to_wstring(cmXInput, i, 0);
				}
				catch (...) {
					X[i] = L"";
				}
			}

			int* nCrits = nullptr;
			nCrits = (int*)malloc(sizeof(int) * (nCrit_ncols + 1));
			nCrits[0] = nCrit_ncols;

			wstring** Crits = nullptr;
			//Crits = (wstring**)malloc(sizeof(wstring*)*nCrit_ncols);
			Crits = new wstring * [nCrit_ncols];
			for (i = 0; i < nCrit_ncols; i++) {
				//Crits[i] = (wstring*)malloc(sizeof(wstring)*(nCrit_nrows + 1));
				Crits[i] = new wstring[nCrit_nrows + 1];
				nCrits[i + 1] = 0;
				for (j = 0; j < nCrit_nrows; j++) {
					try {
						Crits[i][j] = LPOPER_to_wstring(cmCriticalValues, j, i);
						nCrits[i + 1] += 1;
					}
					catch (...) {
						Crits[i][j] = wstring();
					}
				}
				Crits[i][j] = wstring();
			}


			int nCL_nrows = 0, nCL_ncols = 0, nCLs = 0;

			double* A = nullptr;
			A = (double*)malloc(sizeof(double) * nrows * nCoef_nrows);
			memset(A, 0, sizeof(double) * nrows * nCoef_nrows);



			int rc;

			rc = fArtificialsScored_Categorical(X, nrows, Treatment, Crits, nCrits, NULL, 0, Coeffs.memptr(), nCoef_ncols, nCoef_nrows, A, nCoef_nrows, nrows, nCoef_nrows, 0, 0, false);
			for (i = 0; i < nCrit_ncols; i++) {
				delete[] Crits[i];
			}
			delete[] Crits;
			free(nCrits);
			delete[] X;


			result = new OPER12(nrows, nCoef_nrows);
			for (j = 0, ij = 0; j < nCoef_nrows; j++) {
				for (i = 0; i < nrows; i++, ij++) {
					(*result)(i, j) = A[ij];
				}
			}

			free(A);

		}
		else if (Treatment == e_CategoricalNumeric) {

			double* X = nullptr;
			X = (double*)malloc(sizeof(double) * nrows);

			for (i = 0; i < nrows; i++) {
				try {
					X[i] = LPOPER_to_double(cmXInput, i, 0);
				}
				catch (...) {
					X[i] = nan("");
				}
			}

			nCrit_nrows = cmCriticalValues->val.array.rows;
			nCrit_ncols = cmCriticalValues->val.array.columns;
			int* nCrits = nullptr;
			nCrits = (int*)malloc(sizeof(int) * (nCrit_ncols + 1));
			nCrits[0] = nCrit_ncols;

			double** Crits = nullptr;
			Crits = (double**)malloc(sizeof(double*) * nCrit_ncols);
			for (i = 0; i < nCrit_ncols; i++) {
				Crits[i] = (double*)malloc(sizeof(double) * (nCrit_nrows + 1));
				nCrits[i + 1] = 0;
				for (j = 0; j < nCrit_nrows; j++) {
					try {
						Crits[i][j] = LPOPER_to_double(cmCriticalValues, j, i);
						nCrits[i + 1] += 1;
					}
					catch (...) {
						Crits[i][j] = nan("");
					}
				}
				Crits[i][j] = nan("");
			}


			int nCL_nrows = 0, nCL_ncols = 0, nCLs = 0;



			double* A = nullptr;
			A = (double*)malloc(sizeof(double) * nrows * nCoef_nrows);
			memset(A, 0, sizeof(double) * nrows * nCoef_nrows);

			int rc;

			rc = fArtificialsScored_CategoricalNumeric(X, nrows, Treatment, Crits, nCrits, NULL, 0, Coeffs.memptr(), nCoef_ncols, nCoef_nrows, A, nCoef_nrows, nrows, nCoef_nrows, 0, 0, false);
			for (i = 0; i < nCrit_ncols; i++) {
				free(Crits[i]);
			}
			free(Crits);
			free(nCrits);
			free(X);

			result = new OPER12(nrows, nCoef_nrows);
			for (j = 0, ij = 0; j < nCoef_nrows; j++) {
				for (i = 0; i < nrows; i++, ij++) {
					(*result)(i, j) = A[ij];
				}
			}

			free(A);

		}
		else {

			double* X = nullptr;
			X = (double*)malloc(sizeof(double) * nrows);

			for (i = 0; i < nrows; i++) {
				try {
					X[i] = LPOPER_to_double(cmXInput, i, 0);
				}
				catch (...) {
					X[i] = nan("");
				}
			}

			nCrit_nrows = cmCriticalValues->val.array.rows;
			nCrit_ncols = cmCriticalValues->val.array.columns;
			int nCrits = nCrit_ncols;
			double* Crits = nullptr;
			if (nCrit_ncols == 1 && nCrit_nrows > 1) {
				nCrits = nCrit_nrows;
			}
			Crits = (double*)malloc(sizeof(double) * nCrits);
			for (i = 0; i < nCrits; i++) {
				try {
					if (nCrits != nCrit_ncols)
						Crits[i] = LPOPER_to_double(cmCriticalValues, i, 0);
					else
						Crits[i] = LPOPER_to_double(cmCriticalValues, 0, i);
				}
				catch (...) {
				}
			}

			int nCL_nrows = 0, nCL_ncols = 0, nCLs = 0;
			//dMatrix CLs;
			double* CLs = nullptr;

			if (usual_suspect_LPXLOPER(CleanLimits)) {
				if (lCoerceToMultiIfNecessary(CleanLimits, cmCleanLimits, bWasCleanLimitsCoerced) != 0)
					throw exception("Coerce error for CleanLimits in ArtificialsScored.");
				nCL_nrows = cmCleanLimits->val.array.rows;
				nCL_ncols = cmCleanLimits->val.array.columns;
				nCLs = nCL_ncols;
				if (nCL_ncols == 1 && nCL_nrows > 1) {
					nCLs = nCL_nrows;
				}
				CLs = (double*)malloc(sizeof(double) * nCLs);
				for (i = 0; i < nCLs; i++) {
					try {
						if (nCLs != nCL_ncols)
							CLs[i] = LPOPER_to_double(cmCleanLimits, i, 0);
						else
							CLs[i] = LPOPER_to_double(cmCleanLimits, 0, i);
					}
					catch (...) {
					}
				}
			}

			double* A = nullptr;
			A = (double*)malloc(sizeof(double) * nrows * nCoef_nrows);
			memset(A, 0, sizeof(double) * nrows * nCoef_nrows);

			int rc;

			rc = fArtificialsScored_Numeric(X, nrows, Treatment, Crits, nCrits, CLs, nCLs, Coeffs.memptr(), nCoef_ncols, nCoef_nrows, A, nCoef_nrows, nrows, nCoef_nrows, 0, 0, false);

			result = new OPER12(nrows, nCoef_nrows);
			for (j = 0, ij = 0; j < nCoef_nrows; j++) {
				for (i = 0; i < nrows; i++, ij++) {
					(*result)(i, j) = A[ij];
				}
			}

			free(X);
			free(Crits);
			free(CLs);
			free(A);


		}

	}
	catch (exception& e) {
		if (result != nullptr) Excel12f(xlFree, 0, 1, (LPXLOPER12)result);
		std::string ew = e.what();
		result = new OPER12(L"Error, in ArtificialsScored: " + std::wstring(ew.begin(), ew.end()));
	}

	lFreeIfNecessary(cmXInput, bWasXInputCoerced);
	lFreeIfNecessary(cmCriticalValues, bWasCriticalValuesCoerced);
	lFreeIfNecessary(cmCleanLimits, bWasCleanLimitsCoerced);
	lFreeIfNecessary(cmCoefficients, bWasCoefficientsCoerced);

	if (result != nullptr) result->xltype = result->xltype | xlbitXLFree;
	return result;

}

}
