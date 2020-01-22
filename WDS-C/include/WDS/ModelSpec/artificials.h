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
        bool rv=false;
        size_t i=0;
        eTreatment arg=va_arg(valist, eTreatment);
        for (i=2; !rv && i<= vacount; i++) 
            rv=(arg==va_arg(valist, eTreatment));
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



    eTreatment eTreatmentClean(wchar_t* data, size_t n){
        if (n<=0) return e_Unknown;
        if (n==7 && wcsncmp(data,L"Unknown",n)==0) return e_Unknown;
        if (n==4 && wcsncmp(data,L"None",n)==0) return e_None;
        if (n==8 && wcsncmp(data,L"Constant",n)==0) return e_Constant;
        if (n==13 && wcsncmp(data,L"CodedMissings",n)==0) return e_CodedMissings;
        if (n==10 && wcsncmp(data,L"DiscreteLC",n)==0) return e_DiscreteLC;
        if (n==10 && wcsncmp(data,L"DiscreteRC",n)==0) return e_DiscreteRC;
        if (n==4 && wcsncmp(data,L"Hats",n)==0) return e_Hats;
        if (n==5 && wcsncmp(data,L"iHats",n)==0) return e_iHats;
        if (n==13 && wcsncmp(data,L"BSplineOrder2",n)==0) return e_BSplineOrder2;
        if (n==13 && wcsncmp(data,L"BSplineOrder3",n)==0) return e_BSplineOrder3;
        if (n==11 && wcsncmp(data,L"Categorical",n)==0) return e_Categorical;
        if (n==18 && wcsncmp(data,L"CategoricalNumeric",n)==0) return e_CategoricalNumeric;

        char sdata[32];
        memset(sdata,0,32);
        if (n>31) n=31;
        int i = 0;
        size_t j = 0;
        for (i = 0; i < n; i++) {
            j = (size_t)data[i];
            if (j>0 && j<256) {
                //if (j >= 97 && j <= 122) j-=32;
                if (j >= 65 && j <= 90) j+=32;
                sdata[i] = (char) j;
            }
        }

        if (wcsncmp(data,L"unknown",n)==0) return e_Unknown;
        if (wcsncmp(data,L"none",n)==0) return e_None;
        if (wcsncmp(data,L"constant",n)==0) return e_Constant;
        if (wcsncmp(data,L"codedmissings",n)==0) return e_CodedMissings;
        if (wcsncmp(data,L"discretelc",n)==0) return e_DiscreteLC;
        if (wcsncmp(data,L"discreterc",n)==0) return e_DiscreteRC;
        if (wcsncmp(data,L"hats",n)==0) return e_Hats;
        if (wcsncmp(data,L"ihats",n)==0) return e_iHats;
        if (wcsncmp(data,L"bsplineorder2",n)==0) return e_BSplineOrder2;
        if (wcsncmp(data,L"bsplineorder3",n)==0) return e_BSplineOrder3;
        if (wcsncmp(data,L"categorical",n)==0) return e_Categorical;
        if (wcsncmp(data,L"categoricalnumeric",n)==0) return e_CategoricalNumeric;

        if (strcmp(sdata,"straight")==0) return e_None;
        if (strcmp(sdata,"numeric")==0) return e_None;
        if (strcmp(sdata,"missings")==0) return e_CodedMissings;

        if (strcmp(sdata,"bucketslc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"levelslc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"discretizelc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"intervalslc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"disclc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"bz0lc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"bso0lc")==0) return e_DiscreteLC;
        if (strcmp(sdata,"caglad")==0) return e_DiscreteLC;
        if (strcmp(sdata,"collor")==0) return e_DiscreteLC;
        if (strcmp(sdata,"lcrl")==0) return e_DiscreteLC;

        if (strcmp(sdata,"buckets")==0) return e_DiscreteRC;
        if (strcmp(sdata,"levels")==0) return e_DiscreteRC;
        if (strcmp(sdata,"discretize")==0) return e_DiscreteRC;
        if (strcmp(sdata,"intervals")==0) return e_DiscreteRC;
        if (strcmp(sdata,"disc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"bz0")==0) return e_DiscreteRC;
        if (strcmp(sdata,"bso0")==0) return e_DiscreteRC;

        if (strcmp(sdata,"bucketsrc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"levelsrc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"discretizerc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"intervalsrc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"discrc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"bz0rc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"bso0rc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"cadlag")==0) return e_DiscreteRC;
        if (strcmp(sdata,"corlol")==0) return e_DiscreteRC;
        if (strcmp(sdata,"rcll")==0) return e_DiscreteRC;

        if (strcmp(sdata,"buckets")==0) return e_DiscreteRC;
        if (strcmp(sdata,"levels")==0) return e_DiscreteRC;
        if (strcmp(sdata,"discretize")==0) return e_DiscreteRC;
        if (strcmp(sdata,"intervals")==0) return e_DiscreteRC;
        if (strcmp(sdata,"disc")==0) return e_DiscreteRC;
        if (strcmp(sdata,"bz0")==0) return e_DiscreteRC;
        if (strcmp(sdata,"bso0")==0) return e_DiscreteRC;

        if (strcmp(sdata,"bz1")==0) return e_Hats;
        if (strcmp(sdata,"bso1")==0) return e_Hats;
        if (strcmp(sdata,"integratedhats")==0) return e_iHats;
        if (strcmp(sdata,"bsplineo2")==0) return e_BSplineOrder2;
        if (strcmp(sdata,"bz2")==0) return e_BSplineOrder2;
        if (strcmp(sdata,"bso2")==0) return e_BSplineOrder2;
        if (strcmp(sdata,"bsplineo3")==0) return e_BSplineOrder3;
        if (strcmp(sdata,"bz3")==0) return e_BSplineOrder3;
        if (strcmp(sdata,"bso3")==0) return e_BSplineOrder3;
        if (strcmp(sdata,"cat")==0) return e_Categorical;
        if (strcmp(sdata,"string")==0) return e_Categorical;
        if (strcmp(sdata,"ncat")==0) return e_CategoricalNumeric;
        if (strcmp(sdata,"ncategorical")==0) return e_CategoricalNumeric;

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
                return nCritVals+2;
                break;
            case e_Hats:
            case e_iHats:
                return nCritVals+1;
                break;
            case e_BSplineOrder2:
                return nCritVals;
                break;
            case e_BSplineOrder3:
                return nCritVals-1;
                break;
            case e_Categorical:
            case e_CategoricalNumeric:
                return nCritVals+1;
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

        size_t tmp=nArtificialCount(nCritVals, Treatment);

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
                return tmp-1;
                break;
            default:
                return 0;
                break;
        }

        return tmp-1;
    }


    //local fArtificialsLabels_Args={"Treatment","CriticalValues","VariableBaseName"}

#define at_(r,c) (bRowMajor) ? ((r+nArtsRowOffset)*nArtsColumnCount+c+nArtsColumnOffset) : ((r+nArtsRowOffset)+(c+nArtsColumnOffset)*nArtsRowCount)

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

        double xMci, xMciM1, xMciM2;
        double fo0, fo1, fo2, fo3;

        switch (Treatment) {
            case e_Unknown:
                return -1;
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
                return -1;
                break;
            default:
                return -1;
                break;
        }

		if (nCritVals > NCRITVALS_MAX) return -1;
		if (nArts > NARTVALS_MAX) return -1;

        if (nSourceValueRowCount<1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return -1;
        if (nArtsRowCount<nSourceValueRowCount+nArtsRowOffset) return -1;
        if (nArtsColumnOffset<0 || nArtsColumnOffset+nArts>nArtsColumnCount) return -1;
        if (nArtsRowCount<nSourceValueRowCount) return -1;

        bool bUsingRowOffsets=false;
        bUsingRowOffsets=(nSourceValueRowCount>1) 
            || (nArtsRowOffset>0) 
            || (nArtsColumnOffset>0) 
            ;


        double eps=0.00000001;
        double Cnstnt=1.0;

		double CleanLimitLeftVal = NAN;
		double CleanLimitRightVal = NAN;
        bool bUsingCleanLimitLeft=false, bUsingCleanLimitRight=false;
        double dCVs[NCRITVALS_MAX-1], dCVsdiv2[NCRITVALS_MAX-1], d2CVs[NCRITVALS_MAX-2], d2CVsdiv2[NCRITVALS_MAX-2], d3CVs[NCRITVALS_MAX-3];


        if (nCleanLimits>0) {
            bUsingCleanLimitLeft=true;
            CleanLimitLeftVal=CleanLimits[0];
        }
        if (nCleanLimits>1) {
            bUsingCleanLimitRight=true;
            CleanLimitRightVal=CleanLimits[1];
        }

        size_t nCritValsM1=nCritVals-1;


        if (eTreatment_bIn(3, Treatment, e_Categorical, e_CategoricalNumeric)) { //then
            return -1;
        } else if (Treatment == e_Constant) { //then
            if (nCritVals<=0) return -2;
            Cnstnt = CriticalValues[0];
            //Cnstnt = CVs[{1, 1}]
        } else if (!(Treatment == e_None || Treatment == e_Constant)) { //then
            //--wrap already addressed above
            //--check the critical values for order
            //if not CVs:isOrdered() then
            for (iM1=0,i=1; i<nCritVals; i++, iM1++) {
                if (CriticalValues[iM1]>=CriticalValues[i]-eps) return -2;
            }
            //if wds.bIn(varm.Treatment, eTreatment.Hats, eTreatment.iHats, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3) then
            if (eTreatment_bIn(5, Treatment, e_Hats, e_iHats, e_BSplineOrder2, e_BSplineOrder3)) {
                //dCVs=mat.dMatrix_SimpleDiffVector(CVs,1)
                for (iM1=0,i=1; i<nCritVals; i++, iM1++) 
                    dCVs[iM1]=CriticalValues[i]-CriticalValues[iM1];
                if (Treatment == e_iHats) 
                    for (iM1=0; iM1<nCritValsM1; iM1++) 
                        dCVsdiv2[iM1]=dCVs[iM1]/2.0;
            } //end
            //if wds.bIn(varm.Treatment, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3, eTreatment.iHats) then
            if (eTreatment_bIn(4, Treatment, e_iHats, e_BSplineOrder2, e_BSplineOrder3)) {
                //d2CVs=mat.dMatrix_SimpleDiffVector(CVs,2)
                for (iM2=0,i=2; i<nCritVals; i++, iM2++) 
                    d2CVs[iM2]=CriticalValues[i]-CriticalValues[iM2];
                if (Treatment == e_iHats) 
                    for (iM2=0; i<nCritVals-2; iM2++) 
                        d2CVsdiv2[iM2]=d2CVs[iM2]/2.0;
            } //end
            //if BSplineOrder3 then
            if (Treatment == e_BSplineOrder3) {
                //d3CVs=mat.dMatrix_SimpleDiffVector(CVs,3)
                for (iM3=0,i=3; i<nCritVals; i++, iM3++) 
                    dCVs[iM3]=CriticalValues[i]-CriticalValues[iM3];
            } //end
        } //end


        size_t nrows = nSourceValueRowCount;
        bool bSingleRow = (nrows==1);

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
				return -1;
				break;

			default:

				bIsMissing = !(isfinite(tempval));
				bIsMissing = (!bIsMissing) && (bUsingCleanLimitLeft && (tempval < CleanLimitLeftVal));
				bIsMissing = (!bIsMissing) && (bUsingCleanLimitRight && (tempval < CleanLimitRightVal));

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

							if ((Treatment == e_DiscreteRC) && (x >= CriticalValues[1] - eps)) { //then
								Arts[at_(r, ia)] = 0.0;
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
							for (jM1 = 0, j = 1, ia = 2; j < nCritVals; jM1++, j++, ia++)
								Arts[at_(r, ia)] += d2CVsdiv2[jM1];

							j = 0;
							ia = 1;
							Arts[at_(r, ia)] += dCVs[j] / 2.0;
						}
						else {

							if ((Treatment == e_DiscreteLC) && (x <= CriticalValues[nCritValsM1] - eps)) { //then
								i += 1;
								ia += 1;
							} //end

							Arts[at_(r, ia)] = 1.0;

						} //end

					}
					else {


						for (ia = 0; ia < nArts; ia++)
							Arts[at_(r, ia)] = 0.0;

						//--'main guts of the function.....

						//--'find the critical value inteArtsal.....
						i = nCritValsM1;
						if (Treatment == e_DiscreteLC) {// then
							found = false;
							for (j = nCritValsM1; (!found) && (j > 0); j--)
								found = (x > CriticalValues[j] + eps);
							i = j;
							ia = j + 1;
						}
						else if (Treatment == e_DiscreteRC) {// then
							found = false;
							for (j = nCritValsM1; (!found) && (j > 0); j--)
								found = (x > CriticalValues[j] - eps);
							i = j;
							ia = j + 1;
						}
						else {
							found = false;
							for (j = nCritValsM1; (!found) && (j > 0); j--)
								found = (x >= CriticalValues[j]);
							i = j;
							ia = j + 1;
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

							tempdouble = pow((x - CriticalValues[i]), 2.0) / dCVsdiv2[i];

							iaP1 = ia + 1;

							Arts[at_(r, iaP1)] = tempdouble;
							Arts[at_(r, ia)] = (x - CriticalValues[i] - tempdouble);

							for (ii = 1; ii < i; ii++) {
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
							if (i == 1) {
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
							if (i == 2) {
								//--'fo2 is a catch all where not defined
								fo2 = 1 - fo0 - fo1;
							}
							else if (i > 2) {
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

							if (iaM1 > 1) {
								if (iaM1 < nArts - 1)
									Arts[at_(r, iaM1)] += fo1;
								else
									Arts[at_(r, nArts - 1)] += fo1;
							}


							if (iaM2 > 1)
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

							if (i > 1)
								xMciM1 = (x - CriticalValues[iM1]);
							if (i > 2)
								xMciM2 = (x - CriticalValues[iM2]);

							fo0 = 0.0;
							fo1 = 0.0;
							fo2 = 0.0;
							fo3 = 0.0;

							if (i < nCritVals - 2)
								//--' u+v=1,a+b=1,p+q=1
								//--' u[0]*a[0]*p[0]
								fo0 = xMci / d3CVs[i] * xMci / d2CVs[i] * xMci / dCVs[i];
							if (i == 1)
								fo1 = 1.0 - fo0;
							else if (i < nCritVals - 2)
								//--' u[-1]*(a[-1]*q[0] + b*p[0])
								//--'+v[0]*(a[0]*p[0])
								fo1 = (xMciM1 / d3CVs[iM1]) * (xMciM1 / d2CVs[iM1] * (1.0 - xMci / dCVs[i])
									+ (1.0 - xMci / d2CVs[i]) * (xMci / dCVs[i])) +
									(1.0 - xMci / d3CVs[i]) * (xMci / d2CVs[i] * xMci / dCVs[i]);

							if (i == 2)
								fo2 = 1.0 - fo0 - fo1;
							else if ((i > 2) && (i < nCritValsM1))
								//--' u[-2]*(b[-1]*q[0])
								//--'+v[-1]*(a[-1]*q[0]+b[0]*p[0])
								fo2 = (xMciM2 / d3CVs[iM2]) * ((1.0 - xMciM1 / d2CVs[iM1]) * (1.0 - xMci / dCVs[i]))
								+ (1.0 - xMciM1 / d3CVs[iM1]) * (xMciM1 / d2CVs[iM1] * (1.0 - xMci / dCVs[i])
									+ (1.0 - xMci / d2CVs[i]) * (xMci / dCVs[i]));
							if (i == 3)
								fo3 = 1.0 - fo0 - fo1 - fo2;
							else if ((i > 3) && (i < nCritVals))
								//--' v[-2]*b[-1]*p[0]
								fo3 = (1.0 - xMciM2 / d3CVs[iM2]) * (1.0 - xMciM1 / d2CVs[iM1]) * (1.0 - xMci / dCVs[i]);

							if (i == nCritVals - 2)
								fo1 = 1.0 - fo2 - fo3;
							if (i == nCritVals - 1)
								fo2 = 1.0 - fo3;
							if (ia < nArts)
								Arts[at_(r, ia)] = fo0;
							else
								Arts[at_(r, nArts)] = fo0;
							if (iaM1 > 1) {
								if (iaM1 < nArts)
									Arts[at_(r, iaM1)] = fo1;
								else
									Arts[at_(r, nArts)] += fo1;
							}
							if (iaM2 > 1) {
								if (iaM2 < nArts)
									Arts[at_(r, iaM2)] = fo2;
								else
									Arts[at_(r, nArts)] += fo2;
							}
							if (iaM3 > 1) {
								if (iaM3 < nArts)
									Arts[at_(r, iaM3)] = fo3;
								else
									Arts[at_(r, nArts)] += fo3;
							}

							break;

						default:
							return -1;
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
    int fArtificials_CategoricalNumeric(double* SourceValue  // possibly a vector
            , size_t nSourceValueRowCount
            , eTreatment Treatment
            , double** CriticalValues
            , size_t nCritVals_[]
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

        double xMci, xMciM1, xMciM2;
        double fo0, fo1, fo2, fo3;

        switch (Treatment) {
            case e_Unknown:
                return -1;
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
                return -1;
                break;
            case e_CategoricalNumeric:
                break;
            default:
                return -1;
                break;
        }

        size_t nCritVals=nCritVals_[0];

		if (nCritVals > NCRITVALS_MAX) return -1;
		if (nArts > NARTVALS_MAX) return -1;

        if (nSourceValueRowCount<1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return -1;
        if (nArtsRowCount<nSourceValueRowCount+nArtsRowOffset) return -1;
        if (nArtsColumnOffset<0 || nArtsColumnOffset+nArts>nArtsColumnCount) return -1;
        if (nArtsRowCount<nSourceValueRowCount) return -1;

        bool bUsingRowOffsets=false;
        bUsingRowOffsets=(nSourceValueRowCount>1) 
            || (nArtsRowOffset>0) 
            || (nArtsColumnOffset>0) 
            ;


        double eps=0.00000001;
        double Cnstnt=1.0;

		double CleanLimitLeftVal = NAN;
		double CleanLimitRightVal = NAN;
        bool bUsingCleanLimitLeft=false, bUsingCleanLimitRight=false;


        size_t nCritValsM1=nCritVals-1;


        //--any imbedded sets are expected to be expanded outside

        size_t nrows = nSourceValueRowCount;
        bool bSingleRow = (nrows==1);

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
                Arts[at_(r,0)] = 1.0;
            } else {
                found=false;
                for (i=0, iP1=1; (!found) && (i<nCritVals); i++, iP1++) 
                    for (j=0; (!found) && (j<nCritVals_[iP1]); j++) 
                        found=(fabs(tempval-CriticalValues[i][j])<eps);
                if (found) 
                    Arts[at_(r,i-1)]=1.0;
                else
                    Arts[at_(r,0)]=1.0;
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
        size_t ii, iia, iiaM1, iiaP1;

        double xMci, xMciM1, xMciM2;
        double fo0, fo1, fo2, fo3;

        switch (Treatment) {
            case e_Unknown:
                return -1;
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
                return -1;
                break;
            case e_Categorical:
                break;
            case e_CategoricalNumeric:
                return -1;
                break;
            default:
                return -1;
                break;
        }

        size_t nCritVals=nCritVals_[0];

		if (nCritVals > NCRITVALS_MAX) return -1;
		if (nArts > NARTVALS_MAX) return -1;

        if (nSourceValueRowCount<1 || nArtsRowOffset<0 || nArtsRowOffset>nArtsRowCount) return -1;
        if (nArtsRowCount<nSourceValueRowCount+nArtsRowOffset) return -1;
        if (nArtsColumnOffset<0 || nArtsColumnOffset+nArts>nArtsColumnCount) return -1;
        if (nArtsRowCount<nSourceValueRowCount) return -1;

        bool bUsingRowOffsets=false;
        bUsingRowOffsets=(nSourceValueRowCount>1) 
            || (nArtsRowOffset>0) 
            || (nArtsColumnOffset>0) 
            ;


        double eps=0.00000001;
        double Cnstnt=1.0;

		double CleanLimitLeftVal = NAN;
		double CleanLimitRightVal = NAN;
        bool bUsingCleanLimitLeft=false, bUsingCleanLimitRight=false;


        size_t nCritValsM1=nCritVals-1;


        //--any imbedded sets are expected to be expanded outside

        size_t nrows = nSourceValueRowCount;
        bool bSingleRow = (nrows==1);

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

            tempstring=SourceValue[r];

            //case e_Categorical:
            for (ia = 0; ia < nArts; ia++)
                Arts[at_(r, ia)] = 0.0;

			bIsMissing = (tempstring.length()<1);
            if (bIsMissing) {
                Arts[at_(r,0)] = 1.0;
            } else {
                found=false;
                for (i=0, iP1=1; (!found) && (i<nCritVals); i++, iP1++) 
                    for (j=0; (!found) && (j<nCritVals_[iP1]); j++) 
                        found=(CriticalValues[i][j].compare(tempstring)==0);
                if (found) 
                    Arts[at_(r,i-1)]=1.0;
                else
                    Arts[at_(r,0)]=1.0;
            }
        }

        return 0;
    }


            /*

               local fArtificialsScored_Args={"Treatment","Input","CriticalValues","CoefficientValues","CleanLimitLeftVal","CleanLimitRightVal"}

               fArtificialsScored=
               AddToModuleHelp{
               fArtificialsScored=[==[
               Returns a matrix of scored artificials given treatment parameters and a value or vector of values.]==]
               } ..
               function(...)
               local args=fVarArgs(fArtificialsScored_Args,...)
               local varm=args.VariableMatter or fVariableMatter(args.Treatment,args.CriticalValues,args.CleanLimitLeftvalue,args.CleanLimitRightValue,args.CoefficientValues)
               local Input=dMatrix_WrapOrRef(args.Input)
               local CoefficientValues=dMatrix_WrapOrRef(args.CoefficientValues)
               local VariableBaseName=args.VariableBaseName or args.Name or varm.ArtBaseName or varm.Name
               local suffix_sep=args.Separator or ""
               local rv={}
               local CVs=varm.CritVals
               local Cnstnt
               local CleanLimitLeftVal=args.CleanLimitLeftVal or (args.CleanLimits and args.CleanLimits[1]) or NULL
               local CleanLimitRightVal=args.CleanLimitRightVal or (args.CleanLimits and args.CleanLimits[2]) or NULL
               local dCVs={} --for sequential differences
               local d2CVs={} --for two-step sequential differences
               local d3CVs={} --for three-step sequential differences

               local eps=0.00000001

               local rv


               if CoefficientValues.n_cols ~= varm.nArtVars then
               error("Error, Number:="..(WDSContextID + 1)..", "..WDSModuleName..", Description:=Invalid Coefficients")
               end

               local Coef=dMatrix_WrapOrRef(CoefficientValues)
               local nscores=CoefficientValues.n_rows

               if wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then
               --make sure any imbeds are expanded
               CVs=dMatrix(CVs)
               for i=1,CVs.n_rows do
               for j=1,CVs.n_cols do
               if _M_G.type(CVs{i,j})=="table" then
               CVs[{i,j}]=dMatrix(CVs{i,j})
               end
               end
               end
               elseif Constant then
               Cnstnt = CVs[{1, 1}]
               elseif not (None or varm.Treatment == eTreatment.Constant) then
               --wrap already addressed above
               --check the critical values for order
               if not CVs:isOrdered() then
               error(" Number:="..(WDSContextID + 1)..WDSModuleName..", Description:=Invalid Knots")
               end
               if wds.bIn(varm.Treatment, eTreatment.Hats, eTreatment.iHats, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3) then
               dCVs=mat.dMatrix_SimpleDiffVector(CVs,1)
               end
               if wds.bIn(varm.Treatment, eTreatment.BSplineOrder2, eTreatment.BSplineOrder3, eTreatment.iHats) then
               d2CVs=mat.dMatrix_SimpleDiffVector(CVs,2)
               end
               if BSplineOrder3 then
               d3CVs=mat.dMatrix_SimpleDiffVector(CVs,3)
               end
               end

               local nrows = Input.n_rows

               local rc=dMatrix(nrows, nscores)

               local tempval, tempdouble, x
            local r, i, ia, k, found
                local bIsMissing

                --[[
                'CodeDoc - CJW :
                    '   For consistency, using:
                    '       r for row index
                    '       i for critical value index or the artificial index in the usual sense, X_0, X_1, ..., X_{n}
            '       ia for the VBA 'option base 1' artificial index
                '       k for score index
                --]]

                for r = 1, nrows do 

                    tempval = Input[r]

                        if None then

                            ia = 1
                                for k = 1, nscores do
                                    rc[{r, k}] = Coef[{k, ia}] * tempval
                                        end --k

                                        elseif Constant then

                                        ia = 1

                                        for k = 1, nscores do
                                            rc[{r, k}] = Coef[{k, ia}] * Cnstnt
                                                end --k

                                                elseif wds.bIn(varm.Treatment, eTreatment.Categorical, eTreatment.CategoricalNumeric) then

                                                found = false
                                                if mat.isNULLOrError(tempval) then
                                                    found = true
                                                        i = 0
                                                else
                                                    for _i = 1, varm.nCritVals do
                                                        for j = 1, varm.nCritValRows do
                                                            if wds.isEmpty(CVs{j, _i}) then
                                                                break
                                                                    end
                                                                    --Note: CJW, this is not efficient, but in case CVs{j, _i} 
            --is not expanded into rows.........
                if mat.isMatrix(CVs{j, _i}) then
                    local CVsji=CVs{j, _i}
            for k=1,#CVsji.data do
                if varm.Treatment==eTreatment.CategoricalNumeric then
                    if _M_G.math.abs(tempval-CVs.data[k])<0.000001 then
                        i=_i
                            found = true
                            break
                            end
                    else
                        if tempval == CVsji.data[k] then
                            i=_i
                                found = true
                                break
                                end
                                end
                                end
                                if found then
                                    i=_i
                                        break
                                        end
                                else
                                    if varm.Treatment==eTreatment.CategoricalNumeric then
                                        if _M_G.math.abs(tempval-CVs{j, _i})<0.000001 then
                                            i=_i
                                                found = true
                                                break
                                                end
                                        else
                                            if tempval == CVs{j, _i} then
                                                i=_i
                                                    found = true
                                                    break
                                                    end
                                                    end
                                                    end
                                                    end
                                                    if found then
                                                        break
                                                            end
                                                            end
                                                            end

                                                            if found then
                                                                ia = i + 1
                                                            else
                                                                ia = 1
                                                                    end

                                                                    for k = 1, nscores do
                                                                        rc[{r, k}] = Coef{k, ia}
            end --k

                                                    else
                                                        bIsMissing = not mat.isNumeric(tempval)
                                                            if not bIsMissing and varm.bUseCLLeft and not ( NULL==CleanLimitLeftVal ) then
                                                                bIsMissing = tempval < CleanLimitLeftVal
                                                                    end
                                                                    if not bIsMissing and varm.bUseCLRight and not ( NULL==CleanLimitRightVal ) then
                                                                        bIsMissing = tempval > CleanLimitRightVal
                                                                            end

                                                                            if bIsMissing then
                                                                                ia = 1
                                                                                    for k = 1, nscores do
                                                                                        rc[{r, k}] = Coef(k, ia)
                                                                                            end --k
                                                                            else

                                                                                --'just to keep things communicable and relatable to usual mathematical discussion

                                                                                    x = mat.CDbl(tempval)

                                                                                    if CodedMissings then
                                                                                        --'simple case, missings have already been addressed
                                                                                            i = 1
                                                                                            ia = 2
                                                                                            for k = 1, nscores do
                                                                                                rc[{r, k}] = Coef{k, 2} * x
                                                                                                    end --k
                                                                                                    elseif x <= CVs(1) + eps then
                                                                                                    --'all non-missing first artificials are 1 left of the first critical value, except iHats and DiscreteRC
                                                                                                    i = 1
                                                                                                    ia = 2
                                                                                                    if iHats then
                                                                                                        tempdouble = x - CVs(1)
                                                                                                            for k = 1, nscores do
                                                                                                                rc[{r, k}] = Coef{k, 2} * tempdouble
                                                                                                                    end --k
                                                                                                    else
                                                                                                        if (DiscreteRC) and (x >= CVs(1) - eps) then
                                                                                                            i = i + 1
                                                                                                                ia = ia + 1
                                                                                                                end
                                                                                                                for k = 1, nscores do
                                                                                                                    rc[{r, k}] = Coef{k, ia}
            end --k
                end
                elseif x >= CVs(varm.nCritVals) - eps then
                --'all non-missing last artificials are 1 right of the last critical value, except iHats and DiscreteLC
                i = varm.nCritVals
                ia = varm.nArtVars
                if iHats then
                    tempdouble = (x - CVs(i) + dCVs(i - 1) / 2)
                        for k = 1, nscores do
                            rc[{r, k}] = Coef(k, ia) * tempdouble
                                end --k
                                for k = 1, nscores do
                                    for j = 2, varm.nCritVals - 1 do
                                        ia = j + 1
                                            rc[{r, k}] = rc{r, k} + Coef{k, ia} * d2CVs(j - 1) / 2
                                            end --j
                                            j = 1
                                            ia = 2
                                            rc[{r, k}] = rc{r, k} + Coef{k, ia} * dCVs(j) / 2
                                            end --k
                else
                    if (DiscreteLC) and (x <= CVs(varm.nCritVals) - eps) then
                        i = i + 1
                            ia = ia + 1
                            end
                            for k = 1, nscores do
                                rc[{r, k}] = Coef{k, ia}
            end --k
                end
                    else

                        --'main guts of the function.....

                            --'find the critical value interval.....
                            local i=varm.nCritVals-1
                            if DiscreteLC then
                                for _i = varm.nCritVals - 1, 1, -1 do
                                    if x > CVs(_i) + eps then
                                        i=_i
                                            break
                                            end
                                            end
                                            i=i+1
                                            elseif DiscreteRC then
                                            for _i = varm.nCritVals - 1, 1, -1 do
                                                if x > CVs(_i) - eps then
                                                    i=_i
                                                        break
                                                        end
                                                        end
                                                        i=i+1
                                                else
                                                    for _i = varm.nCritVals - 1, 1, -1 do
                                                        if x >= CVs(_i) then
                                                            i=_i
                                                                break
                                                                end
                                                                end
                                                                end


                                                                --'usual VBA index
                                                                ia = i + 1
                                                                if DiscreteLC or varm.Treatment == eTreatment.DiscreteRC then
                                                                    for k = 1, nscores do
                                                                        rc[{r, k}] = Coef{k, ia}
            end --k
                elseif Hats then
                tempdouble = (x - CVs(i)) / dCVs(i)
                for k = 1, nscores do
                    rc[{r, k}] = rc{r, k} + Coef{k, ia + 1} * tempdouble
                        rc[{r, k}] = rc{r, k} + Coef{k, ia} * (1 - tempdouble)
                        end --k
                        elseif iHats then
                        tempdouble = ((x - CVs(i)) ^ 2 / dCVs(i) / 2)

                        iaP1 = ia + 1
                        for k = 1, nscores do
                            rc[{r, k}] = rc[{r, k}] + Coef{k, iaP1} * tempdouble
                                rc[{r, k}] = rc[{r, k}] + Coef{k, ia} * (x - CVs(i) - tempdouble)
                                end --k
                                for ii = 1, (i - 1) do
                                    iia = ii + 1
                                        iiaP1 = iia + 1
                                        for k = 1, nscores do
                                            rc[{r, k}] = rc[{r, k}] + Coef{k, iiaP1} * dCVs(ii) / 2
                                                rc[{r, k}] = rc[{r, k}] + Coef{k, iia} * dCVs(ii) / 2
                                                end --k
                                                end --ii

                                                elseif BSplineOrder2 then
                                                --'first artificial is a left catch all, necessary through knot3
                                                --'i+2 is more akin to the "usual" index, mapped back to "option base 1" with 0 being the missing code variable
                                                iM1 = i - 1
                                                ia = i + 2
                                                iaM1 = ia - 1
                                                iaM2 = ia - 2

                                                xMci = (x - CVs(i))
                                                xMciM1 = 0

                                                if i > 1 then
                                                    xMciM1 = (x - CVs(iM1))
                                                        end

                                                        --'the last artificial is a right catch all
                                                        --'therefore, fo0, [f]unction [o]ffset [0], stops with CVs(varm.nCritVals-2)
                                                        --'and fo1 is a catch all at CVs(varm.nCritVals-1)

                                                        fo0 = 0
                                                        fo1 = 0
                                                        fo2 = 0

                                                        if i < varm.nCritVals - 1 then
                                                            fo0 = xMci / d2CVs(i) * xMci / dCVs(i)
                                                                end
                                                                if i == 1 then
                                                                    --'fo1 is a catch all where not defined
                                                                        fo1 = 1 - fo0
                                                                        elseif i < varm.nCritVals - 1 then
                                                                        fo1 = xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                                                        + (1 - xMci / d2CVs(i)) * xMci / dCVs(i)
                                                                        end
                                                                        if i == 2 then
                                                                            --'fo2 is a catch all where not defined
                                                                                fo2 = 1 - fo0 - fo1
                                                                                elseif i > 2 then
                                                                                fo2 = (1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))
                                                                                end
                                                                                if i == varm.nCritVals - 1 then
                                                                                    fo1 = 1 - fo2
                                                                                        end

                                                                                        local lrc={}
            for i=1, varm.nArtVars do
                lrc[i]=0.0
                    end

                    if ia < varm.nArtVars then
                        lrc[ia] = fo0
                    else
                        lrc[varm.nArtVars] = fo0
                            end

                            if iaM1 > 1 then
                                if iaM1 < varm.nArtVars then
                                    lrc[iaM1] = fo1
                                else
                                    lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo1
                                        end
                                        end

                                        if iaM2 > 1 then
                                            lrc[iaM2] = lrc[iaM2] + fo2
                                                end


                                                for k = 1, nscores do

                                                    for i = 1, varm.nArtVars do
                                                        rc[{r, k}] = rc[{r, k}] + Coef[{k, i}] * lrc[i]
                                                            end

                                                            end

                                                            elseif BSplineOrder3 then


                                                            iM1 = i - 1
                                                            iM2 = i - 2
                                                            ia = i + 2
                                                            iaM1 = ia - 1
                                                            iaM2 = ia - 2
                                                            iaM3 = ia - 3

                                                            xMci = (x - CVs(i))
                                                            xMciM1 = 0
                                                            xMciM2 = 0

                                                            if i == 3 then
                                                                x = x
                                                                    end
                                                                    if i > 1 then
                                                                        xMciM1 = (x - CVs(iM1))
                                                                            end
                                                                            if i > 2 then
                                                                                xMciM2 = (x - CVs(iM2))
                                                                                    end

                                                                                    fo0 = 0
                                                                                    fo1 = 0
                                                                                    fo2 = 0
                                                                                    fo3 = 0

                                                                                    if i < varm.nCritVals - 2 then
                                                                                        --' u+v=1,a+b=1,p+q=1
                                                                                            --' u[0]*a[0]*p[0]
                                                                                            fo0 = xMci / d3CVs(i) * xMci / d2CVs(i) * xMci / dCVs(i)
                                                                                            end
                                                                                            if i == 1 then
                                                                                                fo1 = 1 - fo0
                                                                                                    elseif i < varm.nCritVals - 2 then
                                                                                                    --' u[-1]*(a[-1]*q[0] + b*p[0])
                                                                                                    --'+v[0]*(a[0]*p[0])

                                                                                                    fo1 = (xMciM1 / d3CVs(iM1)) * (xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i)) 
                                                                                                            + (1 - xMci / d2CVs(i)) * (xMci / dCVs(i))) + 
                                                                                                    (1 - xMci / d3CVs(i)) * (xMci / d2CVs(i) * xMci / dCVs(i))

                                                                                                    end
                                                                                                    if i == 2 then
                                                                                                        fo2 = 1 - fo0 - fo1
                                                                                                            elseif i > 2 and i < varm.nCritVals - 1 then
                                                                                                            --' u[-2]*(b[-1]*q[0])
                                                                                                            --'+v[-1]*(a[-1]*q[0]+b[0]*p[0])
                                                                                                            fo2 = (xMciM2 / d3CVs(iM2)) * ((1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i)))
                                                                                                            + (1 - xMciM1 / d3CVs(iM1)) * (xMciM1 / d2CVs(iM1) * (1 - xMci / dCVs(i))
                                                                                                                    + (1 - xMci / d2CVs(i)) * (xMci / dCVs(i)))
                                                                                                            end
                                                                                                            if i == 3 then
                                                                                                                fo3 = 1 - fo0 - fo1 - fo2
                                                                                                                    elseif i > 3 then
                                                                                                                    --' v[-2]*b[-1]*p[0]
                                                                                                                    fo3 = (1 - xMciM2 / d3CVs(iM2)) * (1 - xMciM1 / d2CVs(iM1)) * (1 - xMci / dCVs(i))
                                                                                                                    end



                                                                                                                    if i == varm.nCritVals - 2 then
                                                                                                                        fo1 = 1 - fo2 - fo3
                                                                                                                            end
                                                                                                                            if i == varm.nCritVals - 1 then
                                                                                                                                fo2 = 1 - fo3
                                                                                                                                    end

                                                                                                                                    local lrc={}
            for i=1, varm.nArtVars do
                lrc[i]=0.0
                    end

                    if ia < varm.nArtVars then
                        lrc[ia] = fo0
                    else
                        lrc[varm.nArtVars] = fo0
                            end
                            if iaM1 > 1 then
                                if iaM1 < varm.nArtVars then
                                    lrc[iaM1] = fo1
                                else
                                    lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo1
                                        end
                                        end
                                        if iaM2 > 1 then
                                            if iaM2 < varm.nArtVars then
                                                lrc[iaM2] = fo2
                                            else
                                                lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo2
                                                    end
                                                    end
                                                    if iaM3 > 1 then
                                                        if iaM3 < varm.nArtVars then
                                                            lrc[iaM3] = fo3
                                                        else
                                                            lrc[varm.nArtVars] = lrc[varm.nArtVars] + fo3
                                                                end
                                                                end

                                                                for k = 1, nscores do

                                                                    for i = 1, varm.nArtVars do
                                                                        rc[{r, k}] = rc[{r, k}] + Coef[{k, i}] * lrc[i]
                                                                            end

                                                                            end



                                                                            end
                                                                            end
                                                                            end
                                                                            end
                                                                            end --r

                                                                            return rc

                                                                            end

                                                                            return _ENV


                                                                            */


//#if defined(__cplusplus)
//        }
//#endif
