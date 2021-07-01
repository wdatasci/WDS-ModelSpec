#pragma once

//The WDS::ModelSpec includes a set of core functions for artificial variable treatments.
//The core is just C code for inclusion in other languages via compiled wrappers, such as Python or Lua.


//#if defined(__cplusplus)

//#include <string>
//using namespace std;
//namespace WDS::ModelSpec {

//#else

#include "wchar.h"

//#endif

#include <math.h>
#include <stdarg.h>

#define NCRITVALS_MAX 30
#define NARTVALS_MAX 32
#define NRESULTVALS_MAX 32

#define wdsTreatmentError -1
#define wdsCriticalValuesError -2
#define wdsArtificialsLocationError -3
#define wdsResultsLocationError -4
#define wdsCoefficientsError -5

enum eTreatment {
	e_Unknown = -1
	, e_None = 0
	, e_Constant = 1
	, e_CodedMissings = 2
	, e_DiscreteLC = 3
	, e_DiscreteRC = 4
	, e_Hats = 5
	, e_iHats = 6
	, e_BSplineOrder2 = 7
	, e_BSplineOrder3 = 8
	, e_Categorical = 9
	, e_CategoricalNumeric = 10
}
;

eTreatment eTreatmentFromLong(long arg) {
	if (arg < -1 || arg >(int) e_CategoricalNumeric) return e_Unknown;
	return (eTreatment)arg;
}

bool eTreatment_bIn(int vacount, ...) {
	va_list valist;
	va_start(valist, vacount);
	bool rv = false;
	size_t i = 0;
	eTreatment arg = va_arg(valist, eTreatment);
	for (i = 2; !rv && i <= vacount; i++)
		rv = (arg == va_arg(valist, eTreatment));
	va_end(valist);
	return rv;
}

const wchar_t* eTreatmentLabel(eTreatment arg) {
	switch (arg) {
	case e_Unknown:
		return L"Unknown";
		break;
	case e_None:
		return L"None";
		break;
	case e_Constant:
		return L"Constant";
		break;
	case e_CodedMissings:
		return L"CodedMissings";
		break;
	case e_DiscreteLC:
		return L"DiscreteLC";
		break;
	case e_DiscreteRC:
		return L"DiscreteRC";
		break;
	case e_Hats:
		return L"Hats";
		break;
	case e_iHats:
		return L"iHats";
		break;
	case e_BSplineOrder2:
		return L"BSplineOrder2";
		break;
	case e_BSplineOrder3:
		return L"BSplineOrder3";
		break;
	case e_Categorical:
		return L"Categorical";
		break;
	case e_CategoricalNumeric:
		return L"CategoricalNumeric";
		break;
	default:
		return L"Unknown";
		break;
	}
	return L"Unknown";
}



eTreatment eTreatmentClean(wchar_t* data, size_t n) {
	if (n <= 0) return e_Unknown;
	if (n == 7 && wcsncmp(data, L"Unknown", n) == 0) return e_Unknown;
	if (n == 4 && wcsncmp(data, L"None", n) == 0) return e_None;
	if (n == 8 && wcsncmp(data, L"Constant", n) == 0) return e_Constant;
	if (n == 13 && wcsncmp(data, L"CodedMissings", n) == 0) return e_CodedMissings;
	if (n == 10 && wcsncmp(data, L"DiscreteLC", n) == 0) return e_DiscreteLC;
	if (n == 10 && wcsncmp(data, L"DiscreteRC", n) == 0) return e_DiscreteRC;
	if (n == 4 && wcsncmp(data, L"Hats", n) == 0) return e_Hats;
	if (n == 5 && wcsncmp(data, L"iHats", n) == 0) return e_iHats;
	if (n == 13 && wcsncmp(data, L"BSplineOrder2", n) == 0) return e_BSplineOrder2;
	if (n == 13 && wcsncmp(data, L"BSplineOrder3", n) == 0) return e_BSplineOrder3;
	if (n == 11 && wcsncmp(data, L"Categorical", n) == 0) return e_Categorical;
	if (n == 18 && wcsncmp(data, L"CategoricalNumeric", n) == 0) return e_CategoricalNumeric;

	char sdata[32];
	memset(sdata, 0, 32);
	if (n > 31) n = 31;
	int i = 0;
	size_t j = 0;
	for (i = 0; i < n; i++) {
		j = (size_t)data[i];
		if (j > 0 && j < 256) {
			//if (j >= 97 && j <= 122) j-=32;
			if (j >= 65 && j <= 90) j += 32;
			sdata[i] = (char)j;
		}
	}

	if (wcsncmp(data, L"unknown", n) == 0) return e_Unknown;
	if (wcsncmp(data, L"none", n) == 0) return e_None;
	if (wcsncmp(data, L"constant", n) == 0) return e_Constant;
	if (wcsncmp(data, L"codedmissings", n) == 0) return e_CodedMissings;
	if (wcsncmp(data, L"discretelc", n) == 0) return e_DiscreteLC;
	if (wcsncmp(data, L"discreterc", n) == 0) return e_DiscreteRC;
	if (wcsncmp(data, L"hats", n) == 0) return e_Hats;
	if (wcsncmp(data, L"ihats", n) == 0) return e_iHats;
	if (wcsncmp(data, L"bsplineorder2", n) == 0) return e_BSplineOrder2;
	if (wcsncmp(data, L"bsplineorder3", n) == 0) return e_BSplineOrder3;
	if (wcsncmp(data, L"categorical", n) == 0) return e_Categorical;
	if (wcsncmp(data, L"categoricalnumeric", n) == 0) return e_CategoricalNumeric;

	if (strcmp(sdata, "straight") == 0) return e_None;
	if (strcmp(sdata, "numeric") == 0) return e_None;
	if (strcmp(sdata, "missings") == 0) return e_CodedMissings;

	if (strcmp(sdata, "bucketslc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "levelslc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "discretizelc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "intervalslc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "disclc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "bz0lc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "bso0lc") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "caglad") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "collor") == 0) return e_DiscreteLC;
	if (strcmp(sdata, "lcrl") == 0) return e_DiscreteLC;

	if (strcmp(sdata, "buckets") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "levels") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "discretize") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "intervals") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "disc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "bz0") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "bso0") == 0) return e_DiscreteRC;

	if (strcmp(sdata, "bucketsrc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "levelsrc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "discretizerc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "intervalsrc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "discrc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "bz0rc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "bso0rc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "cadlag") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "corlol") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "rcll") == 0) return e_DiscreteRC;

	if (strcmp(sdata, "buckets") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "levels") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "discretize") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "intervals") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "disc") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "bz0") == 0) return e_DiscreteRC;
	if (strcmp(sdata, "bso0") == 0) return e_DiscreteRC;

	if (strcmp(sdata, "bz1") == 0) return e_Hats;
	if (strcmp(sdata, "bso1") == 0) return e_Hats;
	if (strcmp(sdata, "integratedhats") == 0) return e_iHats;
	if (strcmp(sdata, "bsplineo2") == 0) return e_BSplineOrder2;
	if (strcmp(sdata, "bz2") == 0) return e_BSplineOrder2;
	if (strcmp(sdata, "bso2") == 0) return e_BSplineOrder2;
	if (strcmp(sdata, "bsplineo3") == 0) return e_BSplineOrder3;
	if (strcmp(sdata, "bz3") == 0) return e_BSplineOrder3;
	if (strcmp(sdata, "bso3") == 0) return e_BSplineOrder3;
	if (strcmp(sdata, "cat") == 0) return e_Categorical;
	if (strcmp(sdata, "string") == 0) return e_Categorical;
	if (strcmp(sdata, "ncat") == 0) return e_CategoricalNumeric;
	if (strcmp(sdata, "ncategorical") == 0) return e_CategoricalNumeric;

	return e_Unknown;
}


size_t nArtificialCount(size_t nCritVals, eTreatment Treatment) {

	switch (Treatment) {
	case e_Unknown:
		return 0;
		break;
	case e_None:
		return 1;
		break;
	case e_Constant:
		return 1;
		break;
	case e_CodedMissings:
		return 2;
		break;
	case e_DiscreteLC:
	case e_DiscreteRC:
		return nCritVals + 2;
		break;
	case e_Hats:
	case e_iHats:
		return nCritVals + 1;
		break;
	case e_BSplineOrder2:
		return nCritVals;
		break;
	case e_BSplineOrder3:
		return nCritVals - 1;
		break;
	case e_Categorical:
	case e_CategoricalNumeric:
		return nCritVals + 1;
		break;
	default:
		return 0;
		break;
	}

	return  0;
}

size_t nArtificialIndex_First(size_t nCritVals, eTreatment Treatment) {

	switch (Treatment) {
	case e_Unknown:
	case e_None:
	case e_Constant:
		return 1;
		break;
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
	case e_Categorical:
	case e_CategoricalNumeric:
		return 0;
		break;
	default:
		return 0;
		break;
	}

	return 0;
}

size_t nArtificialIndex_Last(size_t nCritVals, eTreatment Treatment) {

	size_t tmp = nArtificialCount(nCritVals, Treatment);

	switch (Treatment) {
	case e_Unknown:
	case e_None:
	case e_Constant:
	case e_CodedMissings:
		return 1;
		break;
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
	case e_Categorical:
	case e_CategoricalNumeric:
		return tmp - 1;
		break;
	default:
		return 0;
		break;
	}

	return tmp - 1;
}

int __fArtificials_temp1(eTreatment& Treatment,
	size_t& nCleanLimits,
	double* CleanLimits,
	bool& bUsingCleanLimitLeft,
	double& CleanLimitLeftVal,
	bool& bUsingCleanLimitRight,
	double& CleanLimitRightVal,
	size_t& nCritVals,
	double* CriticalValues,
	double& Cnstnt,
	double* dCVs,
	double* dCVsdiv2,
	double* d2CVs,
	double* d2CVsdiv2,
	double* d3CVs,
	double& eps
) {

	int i, iM1, iM2, iM3;

	if (nCleanLimits > 0) {
		bUsingCleanLimitLeft = true;
		CleanLimitLeftVal = CleanLimits[0];
	}
	if (nCleanLimits > 1) {
		bUsingCleanLimitRight = true;
		CleanLimitRightVal = CleanLimits[1];
	}

	size_t nCritValsM1 = nCritVals - 1;


	if (eTreatment_bIn(3, Treatment, e_Categorical, e_CategoricalNumeric)) {
		return wdsTreatmentError;
	}
	else if (Treatment == e_Constant) {
		if (nCritVals <= 0) return wdsCriticalValuesError;
		Cnstnt = CriticalValues[0];
	}
	else if (!(Treatment == e_None || Treatment == e_Constant)) {
		for (iM1 = 0, i = 1; i < nCritVals; i++, iM1++) {
			if (CriticalValues[iM1] >= CriticalValues[i] - eps) return wdsCriticalValuesError;
		}
		if (eTreatment_bIn(5, Treatment, e_Hats, e_iHats, e_BSplineOrder2, e_BSplineOrder3)) {
			for (iM1 = 0, i = 1; i < nCritVals; i++, iM1++)
				dCVs[iM1] = CriticalValues[i] - CriticalValues[iM1];
			if (Treatment == e_iHats)
				for (iM1 = 0; iM1 < nCritValsM1; iM1++)
					dCVsdiv2[iM1] = dCVs[iM1] / 2.0;
		}
		if (eTreatment_bIn(4, Treatment, e_iHats, e_BSplineOrder2, e_BSplineOrder3)) {
			for (iM2 = 0, i = 2; i < nCritVals; i++, iM2++)
				d2CVs[iM2] = CriticalValues[i] - CriticalValues[iM2];
			if (Treatment == e_iHats)
				for (iM2 = 0, i = 2; i < nCritVals; i++, iM2++)
					d2CVsdiv2[iM2] = d2CVs[iM2] / 2.0;
		}
		if (Treatment == e_BSplineOrder3) {
			for (iM3 = 0, i = 3; i < nCritVals; i++, iM3++)
				d3CVs[iM3] = CriticalValues[i] - CriticalValues[iM3];
		}
	}

	return 0;

}


#define at_(r,c) (bRowMajor) ? ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset) : ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)
#define score_at_(r,c) (bRowMajor) ? ((r+nResultsRowOffset)*nResultsColumnCount+c+nResultsColumnOffset) : ((r+nResultsRowOffset)+(c+nResultsColumnOffset)*nResultsRowCount)

// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificials_Numeric(double* SourceValue  // possibly a vector
	, size_t nSourceValueRowCount
	, eTreatment Treatment
	, double* CriticalValues
	, size_t nCritVals
	, double* CleanLimits
	, size_t nCleanLimits
	, double* Arts
	, size_t nArts            // just the column count expected to be returned with (Treatment, nCritVals)
	// This could be determined within, but generally has already be calculated to allocate
	// space for Arts.
	, size_t nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
	, size_t nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
	, size_t nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
	, size_t nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
	, bool bRowMajor
) {

	size_t i, j, k;
	size_t iM1, jM1, kM1;
	size_t iM2, jM2, kM2;
	size_t iM3, jM3, kM3;
	size_t iP1, jP1, kP1;
	size_t ii, iia, iiaM1, iiaP1;

	size_t ib1, jb1, kb1;
	size_t ib1M1, jb1M1, kb1M1;
	size_t ib1M2, jb1M2, kb1M2;

	double xMci, xMciM1, xMciM2;
	double fo0, fo1, fo2, fo3;

	switch (Treatment) {
	case e_Unknown:
		return wdsTreatmentError;
		break;
	case e_None:
	case e_Constant:
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
		break;
	case e_Categorical:
	case e_CategoricalNumeric:
		return wdsTreatmentError;
		break;
	default:
		return wdsTreatmentError;
		break;
	}

	if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
	if (nArts > NARTVALS_MAX) return wdsArtificialsLocationError;

	if (nSourceValueRowCount < 1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return wdsArtificialsLocationError;
	if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset) return wdsArtificialsLocationError;
	if (nArtsColumnOffset<0 || nArtsColumnOffset + nArts>nArtsColumnCount) return wdsArtificialsLocationError;
	if (nArtsRowCount < nSourceValueRowCount) return wdsArtificialsLocationError;

	bool bUsingRowOffsets = false;
	bUsingRowOffsets = (nSourceValueRowCount > 1)
		|| (nArtsRowOffset > 0)
		|| (nArtsColumnOffset > 0)
		;


	double eps = 0.00000001;
	double Cnstnt = 1.0;

	double CleanLimitLeftVal = nan(""); // NAN;
	double CleanLimitRightVal = nan(""); // NAN;
	bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;
	double dCVs[NCRITVALS_MAX - 1], dCVsdiv2[NCRITVALS_MAX - 1], d2CVs[NCRITVALS_MAX - 2], d2CVsdiv2[NCRITVALS_MAX - 2], d3CVs[NCRITVALS_MAX - 3];


	size_t nCritValsM1 = nCritVals - 1;


	int rc = __fArtificials_temp1(Treatment,
		nCleanLimits,
		CleanLimits,
		bUsingCleanLimitLeft,
		CleanLimitLeftVal,
		bUsingCleanLimitRight,
		CleanLimitRightVal,
		nCritVals,
		CriticalValues,
		Cnstnt,
		dCVs,
		dCVsdiv2,
		d2CVs,
		d2CVsdiv2,
		d3CVs,
		eps);

	if (rc != 0) return rc;

	size_t nrows = nSourceValueRowCount;
	bool bSingleRow = (nrows == 1);

	double tempval, tempdouble, x;
	size_t r, ia, iaM1, iaM2, iaM3, iaP1;
	size_t ib1a, ib1aM1, ib1aM2, ib1aM3, ib1aP1;
	bool found, bIsMissing;

	/*
	   --[[
	   'CodeDoc - CJW :
	   '   For consistency, using:
	   '       r for row index
	   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
	   '       ia for the VBA 'option base 1' artificial index
	   '       k for score index
	   --]]
	   */

	for (r = 0; r < nrows; r++) {

		tempval = SourceValue[r];

		switch (Treatment) {
			//if None then
		case e_None:
			Arts[at_(r, 0)] = tempval;
			break;

			//elseif Constant then
		case e_Constant:
			Arts[at_(r, 0)] = Cnstnt;
			break;

			//elseif wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then
		case e_Categorical:
		case e_CategoricalNumeric:
			return wdsTreatmentError;
			break;

		default:

			bIsMissing = !(isfinite(tempval));
			bIsMissing = bIsMissing || ((!bIsMissing) && (bUsingCleanLimitLeft && (tempval < CleanLimitLeftVal)));
			bIsMissing = bIsMissing || ((!bIsMissing) && (bUsingCleanLimitRight && (tempval > CleanLimitRightVal)));

			if (bIsMissing) {

				i = 0;
				ia = 0;

				Arts[at_(r, ia)] = 1.0;
				for (ia = 1; ia < nArts; ia++)
					Arts[at_(r, ia)] = 0.0;

			}
			else {


				//--just to keep things communicable and relatable to usual mathematical discussion
				x = tempval;

				if (Treatment == e_CodedMissings) {

					Arts[at_(r, 0)] = 0.0;
					Arts[at_(r, 1)] = x;

				}
				else if (x <= CriticalValues[0] + eps) { //then 
					Arts[at_(r, 0)] = 0.0;
					//--'all non-missing first artificials are 1 left of the first critical value, except iHats and DiscreteRC
					i = 1;
					ia = 1;

					if (Treatment == e_iHats) { //then

						Arts[at_(r, ia)] = x - CriticalValues[0];

					}
					else {

						if ((Treatment == e_DiscreteRC) && (x >= CriticalValues[0] - eps)) { //then

							i = i + 1;
							ia = ia + 1;
						}

						Arts[at_(r, ia)] = 1.0;

					}

					for (ia = ia + 1; ia < nArts; ia++)
						Arts[at_(r, ia)] = 0.0;

				}
				else if (x >= CriticalValues[nCritValsM1] - eps) {

					for (ia = 0; ia < nArts; ia++)
						Arts[at_(r, ia)] = 0.0;

					//--'all non-missing last artificials are 1 right of the last critical value, except iHats and DiscreteLC
					i = nCritValsM1;
					ia = nArts - 1; //nArtVars

					if (Treatment == e_iHats) {
						Arts[at_(r, ia)] = x - CriticalValues[i] + dCVs[i - 1] / 2.0;
						//VB - base 1
						//For j = 2 To varm.nCritVals - 1
						//    ia = j + 1
						//    rc(r, ia) = rc(r, ia) + d2CVs(1, j - 1) / 2
						//Next
						for (j = 1, ia = 2; j < nCritVals - 1; j++, ia++) {
							Arts[at_(r, ia)] += d2CVs[j - 1] / 2.0;
						}
						Arts[at_(r, 1)] += dCVs[0] / 2.0;
					}
					else {

						if ((Treatment == e_DiscreteLC) && (x <= CriticalValues[nCritValsM1] + eps)) { //then
							i -= 1;
							ia -= 1;

						} //end

						Arts[at_(r, ia)] = 1.0;

					} //end

				}
				else {

					for (ia = 0; ia < nArts; ia++)
						Arts[at_(r, ia)] = 0.0;

					if (Treatment == e_DiscreteLC) {// then
						found = false;
						i = 0;
						ia = 1;
						for (j = 0; (!found) && j < nCritVals - 1; j++) {
							if ((x > CriticalValues[j] + eps && x <= CriticalValues[j + 1]) ||
								(x > CriticalValues[j] && x <= CriticalValues[j + 1] + eps)
								) {
								found = true;
								i = j;
								ia = i + 2;
							}
						}
					}
					else if (Treatment == e_DiscreteRC) {// then
						found = false;
						i = 0;
						ia = 1;
						for (j = 0; (!found) && j < nCritVals - 1; j++) {
							if (fabs(x - CriticalValues[j + 1]) < eps) {
								found = true;
								i = j + 1;
								ia = i + 2;
							}
							else if (x > CriticalValues[j] && x < CriticalValues[j + 1]) {
								found = true;
								i = j;
								ia = i + 2;
							}
						}
					}
					else {
						found = false;
						i = 0;
						ia = 1;
						for (j = 0; (!found) && j < nCritVals - 1; j++) {
							if ((x >= CriticalValues[j] && x < CriticalValues[j + 1]) ||
								(x >= CriticalValues[j] - eps && x < CriticalValues[j + 1])
								) {
								found = true;
								i = j;
								ia = i + 1;
							}
						}
					}

					switch (Treatment) {

					case e_DiscreteLC:
					case e_DiscreteRC:

						Arts[at_(r, ia)] = 1.0;

						break;

					case e_Hats:

						tempdouble = (x - CriticalValues[i]) / dCVs[i];

						Arts[at_(r, ia + 1)] = tempdouble;
						Arts[at_(r, ia)] = (1.0 - tempdouble);

						break;

					case e_iHats:

						tempdouble = pow((x - CriticalValues[i]), 2.0) / dCVs[i] / 2.0;

						iaP1 = ia + 1;

						Arts[at_(r, iaP1)] = tempdouble;
						Arts[at_(r, ia)] = (x - CriticalValues[i] - tempdouble);

						for (ii = 0; ii < i; ii++) {
							iia = ii + 1;
							iiaP1 = iia + 1;
							Arts[at_(r, iiaP1)] += dCVsdiv2[ii];
							Arts[at_(r, iia)] += dCVsdiv2[ii];
						}

						break;
					case e_BSplineOrder2:
						//--'the first artificial is a left catch all, necessary through knot3
						//--'k+2 is more akin to the "usual" index, mapped back to "option base 1" with 0 being the missing code variable

						iM1 = i - 1;
						ia = i + 2;
						iaM1 = ia - 1;
						iaM2 = ia - 2;

						xMci = (x - CriticalValues[i]);
						xMciM1 = 0.0;

						if (i > 0) {
							xMciM1 = (x - CriticalValues[iM1]);
						}

						//-- 'the last artificial is a right catch all
						//-- 'therefore, fo0, [f]unction [o]ffset [0], stops with CVs(varm.nCritVals-2)
						//-- 'and fo1 is a catch all at CVs(varm.nCritVals-1)

						fo0 = 0.0;
						fo1 = 0.0;
						fo2 = 0.0;

						if (i < nCritValsM1) {
							//--' a+b=1,p+q=1
							//--' a*p
							fo0 = xMci / d2CVs[i] * xMci / dCVs[i];
						}
						if (i == 0) {
							//--'fo1 is a catch all where not defined
							fo1 = 1.0 - fo0;
						}
						else if (i < nCritValsM1) {
							//--'the starting interpolation of the preceding basis * corresponding right side of lower order Hat
							//--'+the starting right interpolation of preceding basis * corresponding left side of lower order Hat
							//--' a*q
							//--' +b*p
							fo1 = xMciM1 / d2CVs[iM1] * (1 - xMci / dCVs[i])
								+ (1 - xMci / d2CVs[i]) * xMci / dCVs[i]
								;
						}
						if (i == 1) {
							//--'fo2 is a catch all where not defined
							fo2 = 1 - fo0 - fo1;
						}
						else if (i > 1) {
							//--'the remaining right interpolation of second preceding basis * corresponding right side of lower order Hat
							//--' b*q
							fo2 = (1 - xMciM1 / d2CVs[iM1]) * (1 - xMci / dCVs[i]);
						}
						if (i == nCritValsM1 - 1) {
							fo1 = 1.0 - fo2;
						}


						if (ia < nArts - 1)
							Arts[at_(r, ia)] = fo0;
						else
							Arts[at_(r, nArts - 1)] = fo0;

						if (iaM1 > 0) {
							if (iaM1 < nArts - 1)
								Arts[at_(r, iaM1)] += fo1;
							else
								Arts[at_(r, nArts - 1)] += fo1;
						}


						if (iaM2 > 0)
							Arts[at_(r, iaM2)] += fo2;

						break;

					case e_BSplineOrder3:

						iM1 = i - 1;
						iM2 = i - 2;
						ia = i + 2;
						iaM1 = ia - 1;
						iaM2 = ia - 2;
						iaM3 = ia - 3;

						xMci = (x - CriticalValues[i]);
						xMciM1 = 0.0;
						xMciM2 = 0.0;

						if (i > 0)
							xMciM1 = (x - CriticalValues[iM1]);
						if (i > 1)
							xMciM2 = (x - CriticalValues[iM2]);

						fo0 = 0.0;
						fo1 = 0.0;
						fo2 = 0.0;
						fo3 = 0.0;

						if (i < nCritValsM1 - 2)
							//--' u+v=1,a+b=1,p+q=1
							//--' u[0]*a[0]*p[0]
							fo0 = xMci / d3CVs[i] * xMci / d2CVs[i] * xMci / dCVs[i];
						if (i == 0)
							fo1 = 1.0 - fo0;
						else if (i < nCritValsM1 - 2)
							//--' u[-1]*(a[-1]*q[0] + b*p[0])
							//--'+v[0]*(a[0]*p[0])
							fo1 = (xMciM1 / d3CVs[iM1]) * (xMciM1 / d2CVs[iM1] * (1.0 - xMci / dCVs[i])
								+ (1.0 - xMci / d2CVs[i]) * (xMci / dCVs[i])) +
								(1.0 - xMci / d3CVs[i]) * (xMci / d2CVs[i] * xMci / dCVs[i]);

						if (i == 1)
							fo2 = 1.0 - fo0 - fo1;
						else if ((i > 1) && (i < nCritValsM1 - 1))
							//--' u[-2]*(b[-1]*q[0])
							//--'+v[-1]*(a[-1]*q[0]+b[0]*p[0])
							fo2 = (xMciM2 / d3CVs[iM2]) * ((1.0 - xMciM1 / d2CVs[iM1]) * (1.0 - xMci / dCVs[i]))
							+ (1.0 - xMciM1 / d3CVs[iM1]) * (xMciM1 / d2CVs[iM1] * (1.0 - xMci / dCVs[i])
								+ (1.0 - xMci / d2CVs[i]) * (xMci / dCVs[i]));
						if (i == 2)
							fo3 = 1.0 - fo0 - fo1 - fo2;
						else if (i > 2)
							//--' v[-2]*b[-1]*p[0]
							fo3 = (1.0 - xMciM2 / d3CVs[iM2]) * (1.0 - xMciM1 / d2CVs[iM1]) * (1.0 - xMci / dCVs[i]);
						//else if ((i > 2) && (i < nCritValsM1))

						if (i == nCritValsM1 - 2)
							fo1 = 1.0 - fo2 - fo3;
						if (i == nCritValsM1 - 1)
							fo2 = 1.0 - fo3;

						if (ia < nArts - 1)
							Arts[at_(r, ia)] = fo0;
						else
							Arts[at_(r, nArts - 1)] = fo0;

						if (iaM1 > 0) {
							if (iaM1 < nArts - 1)
								Arts[at_(r, iaM1)] = fo1;
							else
								Arts[at_(r, nArts - 1)] += fo1;
						}
						if (iaM2 > 0) {
							if (iaM2 < nArts - 1)
								Arts[at_(r, iaM2)] = fo2;
							else
								Arts[at_(r, nArts - 1)] += fo2;
						}
						if (iaM3 > 0) {
							if (iaM3 < nArts - 1)
								Arts[at_(r, iaM3)] = fo3;
							else
								Arts[at_(r, nArts - 1)] += fo3;
						}

						break;

					default:
						return wdsTreatmentError;
						break;
					}
				}
			}
			break;
		}
	}
	return 0;
}

// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificialsScored_Numeric(double* SourceValue  // possibly a vector
	, size_t nSourceValueRowCount
	, eTreatment Treatment
	, double* CriticalValues
	, size_t nCritVals
	, double* CleanLimits
	, size_t nCleanLimits
	, double* Coefficients
	, size_t nCoefficients
	, size_t nCoefficientSets
	, double* Results
	, size_t nResults
	, size_t nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
	, size_t nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
	, size_t nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
	, size_t nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
	, bool bRowMajor
) {

	size_t i, j, k;
	size_t iM1, jM1, kM1;
	size_t iM2, jM2, kM2;
	size_t iM3, jM3, kM3;
	size_t iP1, jP1, kP1;
	size_t ii, iia, iiaM1, iiaP1;

	double xMci, xMciM1, xMciM2;
	double fo0, fo1, fo2, fo3;

	switch (Treatment) {
	case e_Unknown:
		return wdsTreatmentError;
		break;
	case e_None:
	case e_Constant:
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
		break;
	case e_Categorical:
	case e_CategoricalNumeric:
		return wdsTreatmentError;
		break;
	default:
		return wdsTreatmentError;
		break;
	}

	if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
	if (nResults > NRESULTVALS_MAX) return wdsResultsLocationError;

	if (nSourceValueRowCount < 1 || nResultsRowOffset<0 || nResultsRowOffset>nResultsRowCount) return wdsResultsLocationError;
	if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset) return wdsResultsLocationError;
	if (nResultsColumnOffset<0 || nResultsColumnOffset + nResults>nResultsColumnCount) return wdsResultsLocationError;
	if (nResultsRowCount < nSourceValueRowCount) return wdsResultsLocationError;

	bool bUsingRowOffsets = false;
	bUsingRowOffsets = (nSourceValueRowCount > 1)
		|| (nResultsRowOffset > 0)
		|| (nResultsColumnOffset > 0)
		;


	double eps = 0.00000001;
	double Cnstnt = 1.0;

	double CleanLimitLeftVal = nan(""); // NAN;
	double CleanLimitRightVal = nan(""); // NAN;
	bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;
	double dCVs[NCRITVALS_MAX - 1], dCVsdiv2[NCRITVALS_MAX - 1], d2CVs[NCRITVALS_MAX - 2], d2CVsdiv2[NCRITVALS_MAX - 2], d3CVs[NCRITVALS_MAX - 3];

	size_t nCritValsM1 = nCritVals - 1;

	int rc = __fArtificials_temp1(Treatment,
		nCleanLimits,
		CleanLimits,
		bUsingCleanLimitLeft,
		CleanLimitLeftVal,
		bUsingCleanLimitRight,
		CleanLimitRightVal,
		nCritVals,
		CriticalValues,
		Cnstnt,
		dCVs,
		dCVsdiv2,
		d2CVs,
		d2CVsdiv2,
		d3CVs, eps);

	if (rc != 0) return rc;


	size_t nArts = nArtificialCount(nCritVals, Treatment);
	if ((int)nArts != nCoefficients) return wdsCoefficientsError;


	size_t nrows = nSourceValueRowCount;
	bool bSingleRow = (nrows == 1);

	double tempval, tempdouble, tempdouble2, x;
	size_t r, ir, ia, iaM1, iaM2, iaM3, iaP1;
	bool found, bIsMissing;

	/*
	   --[[
	   'CodeDoc - CJW :
	   '   For consistency, using:
	   '       r for row index
	   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
	   '       ia for the VBA 'option base 1' artificial index
	   '       k for score index
	   --]]
	   */

	for (r = 0; r < nrows; r++) {

		tempval = SourceValue[r];

		switch (Treatment) {
		case e_None:
			for (ir = 0; ir < nCoefficientSets; ir++)
				Results[score_at_(r, ir)] = tempval * Coefficients[ir];
			break;

		case e_Constant:
			for (ir = 0; ir < nCoefficientSets; ir++)
				Results[score_at_(r, ir)] = Cnstnt * Coefficients[ir];
			break;

		case e_Categorical:
		case e_CategoricalNumeric:
			return wdsTreatmentError;
			break;

		case e_CodedMissings:
		case e_Hats:
		case e_iHats:
		case e_DiscreteLC:
		case e_DiscreteRC:
		case e_BSplineOrder2:
		case e_BSplineOrder3:

			bIsMissing = !(isfinite(tempval));
			bIsMissing = bIsMissing || ((!bIsMissing) && (bUsingCleanLimitLeft && (tempval < CleanLimitLeftVal)));
			bIsMissing = bIsMissing || ((!bIsMissing) && (bUsingCleanLimitRight && (tempval > CleanLimitRightVal)));

			if (bIsMissing) {

				i = 0;
				ir = 0;

				for (ir = 0; ir < nCoefficientSets; ir++)
					Results[score_at_(r, ir)] = Coefficients[ir];

			}
			else {

				double Arts[20];
				memset(Arts, 0, 20 * sizeof(double));

				rc = fArtificials_Numeric(&tempval, 1, Treatment, CriticalValues, nCritVals, CleanLimits, nCleanLimits, Arts, nArts, 1, nArts, 0, 0, bRowMajor);

				for (ir = 0; ir < nCoefficientSets; ir++) {
					Results[score_at_(r, ir)] = 0.0;
					for (ia = 0; ia < nArts; ia++)
						Results[score_at_(r, ir)] += Arts[ia] * Coefficients[ia*nCoefficientSets + ir];
				}
			}

			break;
		default:
			return wdsTreatmentError;
			break;
		}
	}
	return 0;
}


// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificials_CategoricalNumeric(double* SourceValue  // possibly a vector
	, size_t nSourceValueRowCount
	, eTreatment Treatment
	, double** CriticalValues
	, size_t* nCritVals_
	, double* CleanLimits
	, size_t nCleanLimits
	, double* Arts
	, size_t nArts            // just the column count expected to be returned with (Treatment, nCritVals)
	// This could be determined within, but generally has already be calculated to allocate
	// space for Arts.
	, size_t nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
	, size_t nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
	, size_t nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
	, size_t nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
	, bool bRowMajor
) {

	size_t i, j, k;
	size_t iM1, jM1, kM1;
	size_t iM2, jM2, kM2;
	size_t iM3, jM3, kM3;
	size_t iP1, jP1, kP1;

	double xMci, xMciM1, xMciM2;
	double fo0, fo1, fo2, fo3;

	switch (Treatment) {
	case e_Unknown:
		return wdsTreatmentError;
		break;
	case e_None:
	case e_Constant:
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
	case e_Categorical:
		return wdsTreatmentError;
		break;
	case e_CategoricalNumeric:
		break;
	default:
		return wdsTreatmentError;
		break;
	}

	size_t nCritVals = nCritVals_[0];

	if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
	if (nArts > NARTVALS_MAX) return wdsArtificialsLocationError;

	if (nSourceValueRowCount < 1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return wdsArtificialsLocationError;
	if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset) return wdsArtificialsLocationError;
	if (nArtsColumnOffset<0 || nArtsColumnOffset + nArts>nArtsColumnCount) return wdsArtificialsLocationError;
	if (nArtsRowCount < nSourceValueRowCount) return wdsArtificialsLocationError;

	bool bUsingRowOffsets = false;
	bUsingRowOffsets = (nSourceValueRowCount > 1)
		|| (nArtsRowOffset > 0)
		|| (nArtsColumnOffset > 0)
		;


	double eps = 0.00000001;
	double Cnstnt = 1.0;

	double CleanLimitLeftVal = nan(""); // NAN;
	double CleanLimitRightVal = nan(""); // NAN;
	bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;


	size_t nCritValsM1 = nCritVals - 1;


	//--any imbedded sets are expected to be expanded outside

	size_t nrows = nSourceValueRowCount;
	bool bSingleRow = (nrows == 1);

	double tempval, tempdouble, x;
	size_t r, ia, iaM1, iaM2, iaM3, iaP1;
	bool found, bIsMissing;

	/*
	   --[[
	   'CodeDoc - CJW :
	   '   For consistency, using:
	   '       r for row index
	   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
	   '       ia for the VBA 'option base 1' artificial index
	   '       k for score index
	   --]]
	   */

	for (r = 0; r < nrows; r++) {

		tempval = SourceValue[r];

		//case e_CategoricalNumeric:
		for (ia = 0; ia < nArts; ia++)
			Arts[at_(r, ia)] = 0.0;

		bIsMissing = !(isfinite(tempval));
		if (bIsMissing) {
			Arts[at_(r, 0)] = 1.0;
		}
		else {
			found = false;
			for (i = 0, iP1 = 1; (!found) && (i < nCritVals); i++, iP1++) {
				for (j = 0; (!found) && (j < nCritVals_[iP1]); j++) {
					found = (fabs(tempval - CriticalValues[i][j]) < eps);
					if (found) {
						ia = i + 1;
						Arts[at_(r, ia)] = 1.0;
						break;
					}
				}
				if (found) break;
			}
			if (!found)
				Arts[at_(r, 0)] = 1.0;
		}
	}


	return 0;
}


// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificialsScored_CategoricalNumeric(double* SourceValue  // possibly a vector
	, size_t nSourceValueRowCount
	, eTreatment Treatment
	, double** CriticalValues
	, size_t* nCritVals_
	, double* CleanLimits
	, size_t nCleanLimits
	, double* Coefficients
	, size_t nCoefficients
	, size_t nCoefficientSets
	, double* Results
	, size_t nResults
	, size_t nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
	, size_t nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
	, size_t nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
	, size_t nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
	, bool bRowMajor
) {

	size_t i, j, k;
	size_t iM1, jM1, kM1;
	size_t iM2, jM2, kM2;
	size_t iM3, jM3, kM3;
	size_t iP1, jP1, kP1;

	double xMci, xMciM1, xMciM2;
	double fo0, fo1, fo2, fo3;

	switch (Treatment) {
	case e_Unknown:
		return wdsTreatmentError;
		break;
	case e_None:
	case e_Constant:
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
	case e_Categorical:
		return wdsTreatmentError;
		break;
	case e_CategoricalNumeric:
		break;
	default:
		return wdsTreatmentError;
		break;
	}

	size_t nCritVals = nCritVals_[0];

	if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
	if (nResults > NARTVALS_MAX) return wdsResultsLocationError;

	if (nSourceValueRowCount < 1 || nResultsRowOffset<0 || nResultsRowOffset>nResultsRowCount) return wdsResultsLocationError;
	if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset) return wdsResultsLocationError;
	if (nResultsColumnOffset<0 || nResultsColumnOffset + nResults>nResultsColumnCount) return wdsResultsLocationError;
	if (nResultsRowCount < nSourceValueRowCount) return wdsResultsLocationError;

	bool bUsingRowOffsets = false;
	bUsingRowOffsets = (nSourceValueRowCount > 1)
		|| (nResultsRowOffset > 0)
		|| (nResultsColumnOffset > 0)
		;


	double eps = 0.00000001;
	double Cnstnt = 1.0;

	double CleanLimitLeftVal = nan(""); // NAN;
	double CleanLimitRightVal = nan(""); // NAN;
	bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;


	size_t nCritValsM1 = nCritVals - 1;

	size_t nArts = nArtificialCount(nCritVals, Treatment);
	if ((int)nArts != nCoefficients) return wdsCoefficientsError;


	//--any imbedded sets are expected to be expanded outside

	size_t nrows = nSourceValueRowCount;
	bool bSingleRow = (nrows == 1);

	double tempval, tempdouble, x;
	size_t r, ir, ia, iaM1, iaM2, iaM3, iaP1;
	bool found, bIsMissing;

	/*
	   --[[
	   'CodeDoc - CJW :
	   '   For consistency, using:
	   '       r for row index
	   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
	   '       ia for the VBA 'option base 1' artificial index
	   '       k for score index
	   --]]
	   */

	for (r = 0; r < nrows; r++) {

		tempval = SourceValue[r];

		//case e_CategoricalNumeric:

		bIsMissing = !(isfinite(tempval));
		if (bIsMissing) {
			for (ir = 0; ir < nCoefficientSets; ir++) {
				Results[score_at_(r, ir)] = Coefficients[ir];
			}
		}
		else {
			found = false;
			for (i = 0, iP1 = 1; (!found) && (i < nCritVals); i++, iP1++) {
				for (j = 0; (!found) && (j < nCritVals_[iP1]); j++) {
					found = (fabs(tempval - CriticalValues[i][j]) < eps);
					if (found) {
						ia = i + 1;
						ia *= nCoefficientSets;
						for (ir = 0; ir < nCoefficientSets; ir++) {
							Results[score_at_(r, ir)] = Coefficients[ia + ir];
						}
						break;
					}
				}
				if (found) break;
			}
			if (!found) {
				for (ir = 0; ir < nCoefficientSets; ir++) {
					Results[score_at_(r, ir)] = Coefficients[ir];
				}
			}
		}
	}

	return 0;
}



// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificials_Categorical(std::wstring* SourceValue  // possibly a vector
	, size_t nSourceValueRowCount
	, eTreatment Treatment
	, std::wstring** CriticalValues
	, size_t* nCritVals_
	, double* CleanLimits   // meaningless for Categorical, left in for argument list consistency
	, size_t nCleanLimits   // meaningless for Categorical, left in for argument list consistency
	, double* Arts
	, size_t nArts            // just the column count expected to be returned with (Treatment, nCritVals)
	// This could be determined within, but generally has already be calculated to allocate
	// space for Arts.
	, size_t nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
	, size_t nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
	, size_t nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
	, size_t nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
	, bool bRowMajor
) {

	size_t i, j, k;
	size_t iM1, jM1, kM1;
	size_t iM2, jM2, kM2;
	size_t iM3, jM3, kM3;
	size_t iP1, jP1, kP1;

	double xMci, xMciM1, xMciM2;
	double fo0, fo1, fo2, fo3;

	switch (Treatment) {
	case e_Unknown:
		return wdsTreatmentError;
		break;
	case e_None:
	case e_Constant:
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
		return wdsTreatmentError;
		break;
	case e_Categorical:
		break;
	case e_CategoricalNumeric:
		return wdsTreatmentError;
		break;
	default:
		return wdsTreatmentError;
		break;
	}

	size_t nCritVals = nCritVals_[0];

	if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
	if (nArts > NARTVALS_MAX) return wdsArtificialsLocationError;

	if (nSourceValueRowCount < 1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return wdsArtificialsLocationError;
	if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset) return wdsArtificialsLocationError;
	if (nArtsColumnOffset<0 || nArtsColumnOffset + nArts>nArtsColumnCount) return wdsArtificialsLocationError;
	if (nArtsRowCount < nSourceValueRowCount) return wdsArtificialsLocationError;

	bool bUsingRowOffsets = false;
	bUsingRowOffsets = (nSourceValueRowCount > 1)
		|| (nArtsRowOffset > 0)
		|| (nArtsColumnOffset > 0)
		;


	double eps = 0.00000001;
	double Cnstnt = 1.0;

	double CleanLimitLeftVal = nan(""); // NAN;
	double CleanLimitRightVal = nan(""); // NAN;
	bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;


	size_t nCritValsM1 = nCritVals - 1;


	//--any imbedded sets are expected to be expanded outside

	size_t nrows = nSourceValueRowCount;
	bool bSingleRow = (nrows == 1);

	//local rc=dMatrix(nrows, varm.nArtVars)

	//local tempval, tempdouble, x
	double tempval, tempdouble, x;
	std::wstring tempstring;
	//local r, i, ia, k, found
	size_t r, ia, iaM1, iaM2, iaM3, iaP1;
	//local bIsMissing
	bool found, bIsMissing;

	/*
	   --[[
	   'CodeDoc - CJW :
	   '   For consistency, using:
	   '       r for row index
	   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
	   '       ia for the VBA 'option base 1' artificial index
	   '       k for score index
	   --]]
	   */

	for (r = 0; r < nrows; r++) {

		tempstring = SourceValue[r];

		//case e_Categorical:
		for (ia = 0; ia < nArts; ia++)
			Arts[at_(r, ia)] = 0.0;

		bIsMissing = (tempstring.length() < 1);
		if (bIsMissing) {
			Arts[at_(r, 0)] = 1.0;
		}
		else {
			found = false;
			ia = 0;
			for (i = 0, iP1 = 1; (!found) && (i < nCritVals); i++, iP1++) {
				for (j = 0; (!found) && (j < nCritVals_[iP1]); j++) {
					found = (CriticalValues[i][j].compare(tempstring) == 0);
					if (found) {
						ia = i + 1;
						Arts[at_(r, ia)] = 1.0;
						break;
					}
				}
				if (found) break;
			}
			if (!found)
				Arts[at_(r, 0)] = 1.0;
		}
	}

	return 0;
}


// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificialsScored_Categorical(std::wstring* SourceValue  // possibly a vector
	, size_t nSourceValueRowCount
	, eTreatment Treatment
	, std::wstring** CriticalValues
	, size_t* nCritVals_
	, double* CleanLimits   // meaningless for Categorical, left in for argument list consistency
	, size_t nCleanLimits   // meaningless for Categorical, left in for argument list consistency
	, double* Coefficients
	, size_t nCoefficients
	, size_t nCoefficientSets
	, double* Results
	, size_t nResults
	, size_t nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
	, size_t nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
	, size_t nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
	, size_t nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
	, bool bRowMajor
) {

	size_t i, j, k;
	size_t iM1, jM1, kM1;
	size_t iM2, jM2, kM2;
	size_t iM3, jM3, kM3;
	size_t iP1, jP1, kP1;

	double xMci, xMciM1, xMciM2;
	double fo0, fo1, fo2, fo3;

	switch (Treatment) {
	case e_Unknown:
		return wdsTreatmentError;
		break;
	case e_None:
	case e_Constant:
	case e_CodedMissings:
	case e_DiscreteLC:
	case e_DiscreteRC:
	case e_Hats:
	case e_iHats:
	case e_BSplineOrder2:
	case e_BSplineOrder3:
		return wdsTreatmentError;
		break;
	case e_Categorical:
		break;
	case e_CategoricalNumeric:
		return wdsTreatmentError;
		break;
	default:
		return wdsTreatmentError;
		break;
	}

	size_t nCritVals = nCritVals_[0];

	if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
	if (nResults > NARTVALS_MAX) return wdsResultsLocationError;

	if (nSourceValueRowCount < 1 || nResultsRowOffset<0 || nResultsRowOffset>nResultsRowCount) return wdsResultsLocationError;
	if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset) return wdsResultsLocationError;
	if (nResultsColumnOffset<0 || nResultsColumnOffset + nResults>nResultsColumnCount) return wdsResultsLocationError;
	if (nResultsRowCount < nSourceValueRowCount) return wdsResultsLocationError;

	bool bUsingRowOffsets = false;
	bUsingRowOffsets = (nSourceValueRowCount > 1)
		|| (nResultsRowOffset > 0)
		|| (nResultsColumnOffset > 0)
		;


	double eps = 0.00000001;
	double Cnstnt = 1.0;

	double CleanLimitLeftVal = nan(""); // NAN;
	double CleanLimitRightVal = nan(""); // NAN;
	bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;


	size_t nCritValsM1 = nCritVals - 1;


	size_t nArts = nArtificialCount(nCritVals, Treatment);
	if ((int)nArts != nCoefficients) return wdsCoefficientsError;



	//--any imbedded sets are expected to be expanded outside

	size_t nrows = nSourceValueRowCount;
	bool bSingleRow = (nrows == 1);

	//local rc=dMatrix(nrows, varm.nArtVars)

	//local tempval, tempdouble, x
	double tempval, tempdouble, x;
	std::wstring tempstring;
	//local r, i, ia, k, found
	size_t r, ir, ia, iaM1, iaM2, iaM3, iaP1;
	//local bIsMissing
	bool found, bIsMissing;

	/*
	   --[[
	   'CodeDoc - CJW :
	   '   For consistency, using:
	   '       r for row index
	   '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
	   '       ia for the VBA 'option base 1' artificial index
	   '       k for score index
	   --]]
	   */

	for (r = 0; r < nrows; r++) {

		tempstring = SourceValue[r];

		//case e_Categorical:

		bIsMissing = (tempstring.length() < 1);
		if (bIsMissing) {
			for (ir = 0; ir < nCoefficientSets; ir++) {
				Results[score_at_(r, ir)] = Coefficients[ir];
			}
		}
		else {
			found = false;
			ia = 0;
			for (i = 0, iP1 = 1; (!found) && (i < nCritVals); i++, iP1++) {
				for (j = 0; (!found) && (j < nCritVals_[iP1]); j++) {
					found = (CriticalValues[i][j].compare(tempstring) == 0);
					if (found) {
						ia = i + 1;
						ia *= nCoefficientSets;
						for (ir = 0; ir < nCoefficientSets; ir++) {
							Results[score_at_(r, ir)] = Coefficients[ia + ir];
						}
						break;
					}
				}
				if (found) break;
			}
			if (!found) {
				for (ir = 0; ir < nCoefficientSets; ir++) {
					Results[score_at_(r, ir)] = Coefficients[ir];
				}
			}
		}
	}

	return 0;
}


//#if defined(__cplusplus)
//        }
//#endif
