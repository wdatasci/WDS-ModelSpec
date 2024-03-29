/*Copyright (c) 2019-2022 Wypasek Data Science, Inc.
Released under the MIT open source license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
#pragma once


//The WDS::ModelSpec includes a set of core functions for artificial variable treatments.
//The core is just C code for inclusion in other languages via compiled wrappers, such as Python or Lua.

#include "wchar.h"

#include <math.h>
#include <stdarg.h>

#define compTag0 Constants

#define NCRITVALS_MAX 30
#define NARTVALS_MAX 32
#define NRESULTVALS_MAX 32

#define wdsTreatmentError -1
#define wdsCriticalValuesError -2
#define wdsArtificialsLocationError -3
#define wdsResultsLocationError -4
#define wdsCoefficientsError -5

#define compTag0e Constants

#if defined(__cplusplus)

#include <string>
using namespace std;
namespace WDS::ModelSpec {

#else

#include "stdbool.h"

#endif


#if defined(_WINDOWS)

#else

#define lstrlenW wcslen
#define lstrcmpW wcscmp

#endif

#define compTag1 enum eTreatment start
#if defined(__cplusplus)
enum eTreatment {
#else
typedef enum {
#endif
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
#if defined(__cplusplus)
}
;
#else
}
eTreatment
;
#endif

#define compTag2 eTreatmentFromLong start
eTreatment eTreatmentFromLong(long arg) {
    if (arg < -1 || arg >(int) e_CategoricalNumeric) return e_Unknown;
    return (eTreatment)arg;
}

#define compTag3 eTreatment_bIn start
bool eTreatment_bIn(int vacount, ...) {
    va_list valist;
    va_start(valist, vacount);
    bool rv = false;
    int i = 0;
    eTreatment arg = va_arg(valist, eTreatment);
    for (i = 2; !rv && i <= vacount; i++)
        rv = (arg == va_arg(valist, eTreatment));
    va_end(valist);
    return rv;
}

#define compTag4 eTreatmentLabel start
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


#define compTag5 eTreatmentClean start

eTreatment eTreatmentClean(wchar_t* data, int n) {
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
    int j = 0;
    for (i = 0; i < n; i++) {
        j = (int)data[i];
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

#define compTag5 nArtificialCount start

int nArtificialCount(int nCritVals, eTreatment Treatment) {

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

#define compTag6 nArtificialIndex_First start

int nArtificialIndex_First(int nCritVals, eTreatment Treatment) {

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

#define compTag6 nArtificialIndex_Last start

int nArtificialIndex_Last(int nCritVals, eTreatment Treatment) {

    int tmp = nArtificialCount(nCritVals, Treatment);

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

#define compTag6 __fArtificials_temp1 start

int __fArtificials_temp1(eTreatment Treatment,
        int* nCleanLimits,
        double* CleanLimits,
        bool* bUsingCleanLimitLeft,
        double* CleanLimitLeftVal,
        bool* bUsingCleanLimitRight,
        double* CleanLimitRightVal,
        int* nCritVals,
        double* CriticalValues,
        double* Cnstnt,
        double* dCVs,
        double* dCVsdiv2,
        double* d2CVs,
        double* d2CVsdiv2,
        double* d3CVs,
        double* eps
        ) {

    int i, iM1, iM2, iM3;

    if (*nCleanLimits > 0) {
        *bUsingCleanLimitLeft = true;
        *CleanLimitLeftVal = CleanLimits[0];
    }
    if (*nCleanLimits > 1) {
        *bUsingCleanLimitRight = true;
        *CleanLimitRightVal = CleanLimits[1];
    }

    int nCritValsM1 = *nCritVals - 1;


    if (eTreatment_bIn(3, Treatment, e_Categorical, e_CategoricalNumeric)) {
        return wdsTreatmentError;
    }
    else if (Treatment == e_Constant) {
        if (*nCritVals <= 0) return wdsCriticalValuesError;
        *Cnstnt = CriticalValues[0];
    }
    else if (!(Treatment == e_None || Treatment == e_Constant)) {
        for (iM1 = 0, i = 1; i < *nCritVals; i++, iM1++) {
            if (CriticalValues[iM1] >= CriticalValues[i] - *eps) return wdsCriticalValuesError;
        }
        if (eTreatment_bIn(5, Treatment, e_Hats, e_iHats, e_BSplineOrder2, e_BSplineOrder3)) {
            for (iM1 = 0, i = 1; i < *nCritVals; i++, iM1++)
                dCVs[iM1] = CriticalValues[i] - CriticalValues[iM1];
            if (Treatment == e_iHats)
                for (iM1 = 0; iM1 < nCritValsM1; iM1++)
                    dCVsdiv2[iM1] = dCVs[iM1] / 2.0;
        }
        if (eTreatment_bIn(4, Treatment, e_iHats, e_BSplineOrder2, e_BSplineOrder3)) {
            for (iM2 = 0, i = 2; i < *nCritVals; i++, iM2++)
                d2CVs[iM2] = CriticalValues[i] - CriticalValues[iM2];
            if (Treatment == e_iHats)
                for (iM2 = 0, i = 2; i < *nCritVals; i++, iM2++)
                    d2CVsdiv2[iM2] = d2CVs[iM2] / 2.0;
        }
        if (Treatment == e_BSplineOrder3) {
            for (iM3 = 0, i = 3; i < *nCritVals; i++, iM3++)
                d3CVs[iM3] = CriticalValues[i] - CriticalValues[iM3];
        }
    }

    return 0;

}

#define compTag7 fArtificials_Numeric start

#define at_(r,c) (bRowMajor) ? ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset) : ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)
#define score_at_(r,c) (bRowMajor) ? ((r+nResultsRowOffset)*nResultsColumnCount+c+nResultsColumnOffset) : ((r+nResultsRowOffset)+(c+nResultsColumnOffset)*nResultsRowCount)

// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificials_Numeric(double* SourceValue  // possibly a vector
        , int nSourceValueRowCount
        , eTreatment Treatment
        , double* CriticalValues
        , int nCritVals
        , double* CleanLimits
        , int nCleanLimits
        , double* Arts
        , int nArts            // just the column count expected to be returned with (Treatment, nCritVals)
        // This could be determined within, but generally has already be calculated to allocate
        // space for Arts.
        , int nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
        , int nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
        , int nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
        , int nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
        , bool bRowMajor
        ) {

    int i, j;
    int iM1;
    int iM2;
    int ii, iia, iiaP1;


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

    //bool bUsingRowOffsets = false;
    //bUsingRowOffsets = (nSourceValueRowCount > 1)
    //	|| (nArtsRowOffset > 0)
    //	|| (nArtsColumnOffset > 0)
    //	;


    double eps = 1e-14;
    double Cnstnt = 1.0;

    double CleanLimitLeftVal = nan(""); // NAN;
    double CleanLimitRightVal = nan(""); // NAN;
    bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;
    double dCVs[NCRITVALS_MAX - 1], dCVsdiv2[NCRITVALS_MAX - 1], d2CVs[NCRITVALS_MAX - 2], d2CVsdiv2[NCRITVALS_MAX - 2], d3CVs[NCRITVALS_MAX - 3];


    int nCritValsM1 = nCritVals - 1;


    int rc = __fArtificials_temp1(Treatment,
            &nCleanLimits,
            CleanLimits,
            &bUsingCleanLimitLeft,
            &CleanLimitLeftVal,
            &bUsingCleanLimitRight,
            &CleanLimitRightVal,
            &nCritVals,
            CriticalValues,
            &Cnstnt,
            dCVs,
            dCVsdiv2,
            d2CVs,
            d2CVsdiv2,
            d3CVs,
            &eps);

    if (rc != 0) return rc;

    int nrows = nSourceValueRowCount;
    //bool bSingleRow = (nrows == 1);

    double tempval, tempdouble, x;
    int r, ia, iaM1, iaM2, iaM3, iaP1;
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

                                if (i < nCritValsM1-1) {
                                    //--' a+b=1,p+q=1
                                    //--' a*p
                                    fo0 = xMci / d2CVs[i] * xMci / dCVs[i];
                                }
                                if (i == 0) {
                                    //--'fo1 is a catch all where not defined
                                    fo1 = 1.0 - fo0;
                                }
                                else if (i < nCritValsM1-1) {
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

#define compTag8 fArtificials_Numeric start

// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificialsScored_Numeric(double* SourceValue  // possibly a vector
        , int nSourceValueRowCount
        , eTreatment Treatment
        , double* CriticalValues
        , int nCritVals
        , double* CleanLimits
        , int nCleanLimits
        , double* Coefficients
        , int nCoefficients
        , int nCoefficientSets
        , double* Results
        , int nResults
        , int nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
        , int nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
        , int nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
        , int nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
        , bool bRowMajor
        , bool bCoefRowMajor
        ) {

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

    //bool bUsingRowOffsets = false;
    //bUsingRowOffsets = (nSourceValueRowCount > 1)
    //	|| (nResultsRowOffset > 0)
    //	|| (nResultsColumnOffset > 0)
    //	;


    double eps = 0.0000000001;
    double Cnstnt = 1.0;

    double CleanLimitLeftVal = nan(""); // NAN;
    double CleanLimitRightVal = nan(""); // NAN;
    bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;
    double dCVs[NCRITVALS_MAX - 1], dCVsdiv2[NCRITVALS_MAX - 1], d2CVs[NCRITVALS_MAX - 2], d2CVsdiv2[NCRITVALS_MAX - 2], d3CVs[NCRITVALS_MAX - 3];


    int rc = __fArtificials_temp1(Treatment,
            &nCleanLimits,
            CleanLimits,
            &bUsingCleanLimitLeft,
            &CleanLimitLeftVal,
            &bUsingCleanLimitRight,
            &CleanLimitRightVal,
            &nCritVals,
            CriticalValues,
            &Cnstnt,
            dCVs,
            dCVsdiv2,
            d2CVs,
            d2CVsdiv2,
            d3CVs, 
            &eps);

    if (rc != 0) return rc;


    int nArts = nArtificialCount(nCritVals, Treatment);
    if (nArts != nCoefficients) return wdsCoefficientsError;


    int nrows = nSourceValueRowCount;

    double tempval;
    int r, ir, ia;
    bool bIsMissing;

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
                if (bCoefRowMajor)
                    for (ir = 0; ir < nCoefficientSets; ir++)
                        Results[score_at_(r, ir)] = tempval * Coefficients[ir*nCoefficients];
                else
                    for (ir = 0; ir < nCoefficientSets; ir++)
                        Results[score_at_(r, ir)] = tempval * Coefficients[ir];
                break;

            case e_Constant:
                if (bCoefRowMajor)
                    for (ir = 0; ir < nCoefficientSets; ir++)
                        Results[score_at_(r, ir)] = Cnstnt * Coefficients[ir*nCoefficients];
                else
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

                    ir = 0;

                    if (bCoefRowMajor)
                        for (ir = 0; ir < nCoefficientSets; ir++)
                            Results[score_at_(r, ir)] = Coefficients[ir*nCoefficients];
                    else
                        for (ir = 0; ir < nCoefficientSets; ir++)
                            Results[score_at_(r, ir)] = Coefficients[ir];

                }
                else {

                    double Arts[20];
                    memset(Arts, 0, 20 * sizeof(double));

                    rc = fArtificials_Numeric(&tempval, 1, Treatment, CriticalValues, nCritVals, CleanLimits, nCleanLimits, Arts, nArts, 1, nArts, 0, 0, bRowMajor);

                    for (ir = 0; ir < nCoefficientSets; ir++) {
                        Results[score_at_(r, ir)] = 0.0;
                        if (bCoefRowMajor)
                            for (ia = 0; ia < nArts; ia++)
                                Results[score_at_(r, ir)] += Arts[ia] * Coefficients[ia + ir*nCoefficients];
                        else
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

#define compTag9 fArtificials_CategoricalNumeric start

// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificials_CategoricalNumeric(double* SourceValue  // possibly a vector
        , int nSourceValueRowCount
        , eTreatment Treatment
        , double** CriticalValues
        , int* nCritVals_
        , double* CleanLimits
        , int nCleanLimits
        , double* Arts
        , int nArts            // just the column count expected to be returned with (Treatment, nCritVals)
        // This could be determined within, but generally has already be calculated to allocate
        // space for Arts.
        , int nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
        , int nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
        , int nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
        , int nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
        , bool bRowMajor
        ) {

    int i, j;
    int iP1; 

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

    int nCritVals = nCritVals_[0];

    if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
    if (nArts > NARTVALS_MAX) return wdsArtificialsLocationError;

    if (nSourceValueRowCount < 1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return wdsArtificialsLocationError;
    if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset) return wdsArtificialsLocationError;
    if (nArtsColumnOffset<0 || nArtsColumnOffset + nArts>nArtsColumnCount) return wdsArtificialsLocationError;
    if (nArtsRowCount < nSourceValueRowCount) return wdsArtificialsLocationError;

    //bool bUsingRowOffsets = false;
    //bUsingRowOffsets = (nSourceValueRowCount > 1)
    //	|| (nArtsRowOffset > 0)
    //	|| (nArtsColumnOffset > 0)
    //	;


    double eps = 0.00000001;

    //double CleanLimitLeftVal = nan(""); // NAN;
    //double CleanLimitRightVal = nan(""); // NAN;
    //bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;


    //int nCritValsM1 = nCritVals - 1;


    //--any imbedded sets are expected to be expanded outside

    int nrows = nSourceValueRowCount;

    double tempval;
    int r, ia;
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

#define compTag10 fArtificialsScored_CategoricalNumeric start

// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificialsScored_CategoricalNumeric(double* SourceValue  // possibly a vector
        , int nSourceValueRowCount
        , eTreatment Treatment
        , double** CriticalValues
        , int* nCritVals_
        , double* CleanLimits
        , int nCleanLimits
        , double* Coefficients
        , int nCoefficients
        , int nCoefficientSets
        , double* Results
        , int nResults
        , int nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
        , int nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
        , int nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
        , int nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
        , bool bRowMajor
        , bool bCoefRowMajor
        ) {

    int i, j;
    int iP1;


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

    int nCritVals = nCritVals_[0];

    if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
    if (nResults > NARTVALS_MAX) return wdsResultsLocationError;

    if (nSourceValueRowCount < 1 || nResultsRowOffset<0 || nResultsRowOffset>nResultsRowCount) return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset) return wdsResultsLocationError;
    if (nResultsColumnOffset<0 || nResultsColumnOffset + nResults>nResultsColumnCount) return wdsResultsLocationError;
    if (nResultsRowCount < nSourceValueRowCount) return wdsResultsLocationError;

    //bool bUsingRowOffsets = false;
    //bUsingRowOffsets = (nSourceValueRowCount > 1)
    //	|| (nResultsRowOffset > 0)
    //	|| (nResultsColumnOffset > 0)
    //	;


    double eps = 0.00000001;

    //double CleanLimitLeftVal = nan(""); // NAN;
    //double CleanLimitRightVal = nan(""); // NAN;
    //bool bUsingCleanLimitLeft = false, bUsingCleanLimitRight = false;


    //int nCritValsM1 = nCritVals - 1;

    int nArts = nArtificialCount(nCritVals, Treatment);
    if (nArts != nCoefficients) return wdsCoefficientsError;


    //--any imbedded sets are expected to be expanded outside

    int nrows = nSourceValueRowCount;

    double tempval;
    int r, ir, ia;
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
            if (bCoefRowMajor)
                for (ir = 0; ir < nCoefficientSets; ir++) {
                    Results[score_at_(r, ir)] = Coefficients[ir*nCoefficients];
                }
            else
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
                        if (bCoefRowMajor)
                            for (ir = 0; ir < nCoefficientSets; ir++) {
                                Results[score_at_(r, ir)] = Coefficients[ia + ir*nCoefficients];
                            }
                        else
                            for (ir = 0; ir < nCoefficientSets; ir++) {
                                Results[score_at_(r, ir)] = Coefficients[ia*nCoefficientSets + ir];
                            }
                        break;
                    }
                }
                if (found) break;
            }
            if (!found) {
                if (bCoefRowMajor)
                    for (ir = 0; ir < nCoefficientSets; ir++) {
                        Results[score_at_(r, ir)] = Coefficients[ir*nCoefficients];
                    }
                else
                    for (ir = 0; ir < nCoefficientSets; ir++) {
                        Results[score_at_(r, ir)] = Coefficients[ir];
                    }
            }
        }
    }

    return 0;
}

#define compTag11 fArtificialsScored_Categorical start

#if defined(__cplusplus)
// The main Artificials and ArtificialsScored functions in C do not allocate space. 
int fArtificials_Categorical(std::wstring* SourceValue  // possibly a vector
        , int nSourceValueRowCount
        , eTreatment Treatment
        , std::wstring** CriticalValues
        , int* nCritVals_
        , double* CleanLimits   // meaningless for Categorical, left in for argument list consistency
        , int nCleanLimits   // meaningless for Categorical, left in for argument list consistency
        , double* Arts
        , int nArts            // just the column count expected to be returned with (Treatment, nCritVals)
        // This could be determined within, but generally has already be calculated to allocate
        // space for Arts.
        , int nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
        , int nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
        , int nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
        , int nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
        , bool bRowMajor
        ) {
#else
    // The main Artificials and ArtificialsScored functions in C do not allocate space. 
    int fArtificials_Categorical(wchar_t** SourceValue  // possibly a vector
            , int nSourceValueRowCount
            , eTreatment Treatment
            , wchar_t*** CriticalValues
            , int* nCritVals_
            , double* CleanLimits   // meaningless for Categorical, left in for argument list consistency
            , int nCleanLimits   // meaningless for Categorical, left in for argument list consistency
            , double* Arts
            , int nArts            // just the column count expected to be returned with (Treatment, nCritVals)
            // This could be determined within, but generally has already be calculated to allocate
            // space for Arts.
            , int nArtsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nArtsRowOffset
            , int nArtsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nArtsColumnOffset
            , int nArtsRowOffset // generally = 0, but can be used to imbed result into a system matrix
            , int nArtsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
            , bool bRowMajor
            ) {
#endif

        int i, j;
        int iP1;

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

        int nCritVals = nCritVals_[0];

        if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
        if (nArts > NARTVALS_MAX) return wdsArtificialsLocationError;

        if (nSourceValueRowCount < 1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return wdsArtificialsLocationError;
        if (nArtsRowCount < nSourceValueRowCount + nArtsRowOffset) return wdsArtificialsLocationError;
        if (nArtsColumnOffset<0 || nArtsColumnOffset + nArts>nArtsColumnCount) return wdsArtificialsLocationError;
        if (nArtsRowCount < nSourceValueRowCount) return wdsArtificialsLocationError;

        //--any imbedded sets are expected to be expanded outside

        int nrows = nSourceValueRowCount;

#if defined(__cplusplus)
        std::wstring tempstring;
#else
        wchar_t* tempstring;
#endif
        int r, ia;
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

#if defined(__cplusplus)
            bIsMissing = (tempstring.length() < 1);
#else
            bIsMissing = (lstrlenW(tempstring) < 1);
#endif
            if (bIsMissing) {
                Arts[at_(r, 0)] = 1.0;
            }
            else {
                found = false;
                ia = 0;
                for (i = 0, iP1 = 1; (!found) && (i < nCritVals); i++, iP1++) {
                    for (j = 0; (!found) && (j < nCritVals_[iP1]); j++) {
#if defined(__cplusplus)
                        found = (CriticalValues[i][j].compare(tempstring) == 0);
#else
                        found = (lstrcmpW((wchar_t*)CriticalValues[i][j], tempstring) == 0);
#endif
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

#define compTag12 fArtificialsScored_Categorical start

#if defined(__cplusplus)
    // The main Artificials and ArtificialsScored functions in C do not allocate space. 
    int fArtificialsScored_Categorical(std::wstring* SourceValue  // possibly a vector
            , int nSourceValueRowCount
            , eTreatment Treatment
            , std::wstring** CriticalValues
            , int* nCritVals_
            , double* CleanLimits   // meaningless for Categorical, left in for argument list consistency
            , int nCleanLimits   // meaningless for Categorical, left in for argument list consistency
            , double* Coefficients
            , int nCoefficients
            , int nCoefficientSets
            , double* Results
            , int nResults
            , int nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
            , int nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
            , int nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
            , int nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
            , bool bRowMajor
            , bool bCoefRowMajor
            ) {
#else
        int fArtificialsScored_Categorical(wchar_t** SourceValue  // possibly a vector
                , int nSourceValueRowCount
                , eTreatment Treatment
                , wchar_t*** CriticalValues
                , int* nCritVals_
                , double* CleanLimits   // meaningless for Categorical, left in for argument list consistency
                , int nCleanLimits   // meaningless for Categorical, left in for argument list consistency
                , double* Coefficients
                , int nCoefficients
                , int nCoefficientSets
                , double* Results
                , int nResults
                , int nResultsRowCount    // generally >= nSourceValueRowCount, but must be >= nSourceValueRowCount+nResultsRowOffset
                , int nResultsColumnCount // generally = nArtificialsCount, but must be >= nArtificialsCount+nResultsColumnOffset
                , int nResultsRowOffset // generally = 0, but can be used to imbed result into a system matrix
                , int nResultsColumnOffset // generally = 0, but can be used to imbed result into a system matrix
                , bool bRowMajor
                , bool bCoefRowMajor
                ) {
#endif

            int i, j;
            int iP1;

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

            int nCritVals = nCritVals_[0];

            if (nCritVals > NCRITVALS_MAX) return wdsCriticalValuesError;
            if (nResults > NARTVALS_MAX) return wdsResultsLocationError;

            if (nSourceValueRowCount < 1 || nResultsRowOffset<0 || nResultsRowOffset>nResultsRowCount) return wdsResultsLocationError;
            if (nResultsRowCount < nSourceValueRowCount + nResultsRowOffset) return wdsResultsLocationError;
            if (nResultsColumnOffset<0 || nResultsColumnOffset + nResults>nResultsColumnCount) return wdsResultsLocationError;
            if (nResultsRowCount < nSourceValueRowCount) return wdsResultsLocationError;

            //bool bUsingRowOffsets = false;
            //bUsingRowOffsets = (nSourceValueRowCount > 1)
            //	|| (nResultsRowOffset > 0)
            //	|| (nResultsColumnOffset > 0)
            //	;


            int nArts = nArtificialCount(nCritVals, Treatment);
            if (nArts != nCoefficients) return wdsCoefficientsError;



            //--any imbedded sets are expected to be expanded outside

            int nrows = nSourceValueRowCount;

            //local rc=dMatrix(nrows, varm.nArtVars)

#if defined(__cplusplus)
            std::wstring tempstring;
#else
            wchar_t* tempstring;
#endif
            int r, ir, ia;
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

#if defined(__cplusplus)
                bIsMissing = (tempstring.length() < 1);
#else
                bIsMissing = (lstrlenW(tempstring) < 1);
#endif
                if (bIsMissing) {
                    if (bCoefRowMajor)
                        for (ir = 0; ir < nCoefficientSets; ir++) {
                            Results[score_at_(r, ir)] = Coefficients[ir*nCoefficients];
                        }
                    else
                        for (ir = 0; ir < nCoefficientSets; ir++) {
                            Results[score_at_(r, ir)] = Coefficients[ir];
                        }
                }
                else {
                    found = false;
                    ia = 0;
                    for (i = 0, iP1 = 1; (!found) && (i < nCritVals); i++, iP1++) {
                        for (j = 0; (!found) && (j < nCritVals_[iP1]); j++) {
#if defined(__cplusplus)
                            found = (CriticalValues[i][j].compare(tempstring) == 0);
#else
                            found = (lstrcmpW(CriticalValues[i][j], tempstring) == 0);
#endif
                            if (found) {
                                ia = i + 1;
                                if (bCoefRowMajor)
                                    for (ir = 0; ir < nCoefficientSets; ir++) {
                                        Results[score_at_(r, ir)] = Coefficients[ia + ir*nCoefficients];
                                    }
                                else
                                    for (ir = 0; ir < nCoefficientSets; ir++) {
                                        Results[score_at_(r, ir)] = Coefficients[ia*nCoefficientSets + ir];
                                    }
                                break;
                            }
                        }
                        if (found) break;
                    }
                    if (!found) {
                        if (bCoefRowMajor)
                            for (ir = 0; ir < nCoefficientSets; ir++) {
                                Results[score_at_(r, ir)] = Coefficients[ir*nCoefficients];
                            }
                        else
                            for (ir = 0; ir < nCoefficientSets; ir++) {
                                Results[score_at_(r, ir)] = Coefficients[ir];
                            }
                    }
                }
            }

            return 0;
        }


#if defined(__cplusplus)
    }
#endif
