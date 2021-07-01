#ifndef WDS_UTIL_CORE_LOADED
#define WDS_UTIL_CORE_LOADED

#include <math.h>


#ifndef WDS_MINMAX_DEFINED
#define WDS_MINMAX_DEFINED
int min(int& a, int& b) { if (a<b) return a; return b; }
int max(int& a, int& b) { if (a>b) return a; return b; }
double min(double& a, double& b) { if (a<b) return a; return b; }
double max(double& a, double& b) { if (a>b) return a; return b; }
#endif

double _dNAz(double arg) { if (isnan((long double) arg)) return 0.0; if (isinf((long double) arg)) return 0.0; return arg; }


double fRoundTo2Dec(double arg) { return round(arg*100.0)/100.0; }

double PMT(double i, int nper, double pv, double fv, int ptyp)
{
    if (isnan((long double) i)) return FP_NAN;
    if (isnan((long double) pv)) return FP_NAN;
    if (isnan((long double) fv)) return FP_NAN;
    if (nper<=0) return FP_NAN;

    if (fabs(i)<1.0e-6) return -(pv+fv)/((double) nper);

    double iP1=i+1.0;
    double pow_iP1_nper=pow(iP1,nper);

    if (ptyp==0) {
        if (fabs(fv)<=1e-6) {
            return -i*pv*pow_iP1_nper/(pow_iP1_nper-1.0) ;
        } else {
            return -i*(pv*pow_iP1_nper+fv)/(pow_iP1_nper-1.0) ;
        }
    } else {
        if (fabs(fv)<=1e-6) {
            return -i*pv*pow_iP1_nper/iP1/(pow_iP1_nper-1.0) ;
        } else {
            return -i*(pv*pow_iP1_nper+fv)/iP1/(pow_iP1_nper-1.0) ;
        }
    }
    
}

double PV(double i, int nper, double pmt, double fv, int ptyp) {
    if (isnan((long double) i)) return FP_NAN;
    if (isnan((long double) pmt)) return FP_NAN;
    if (isnan((long double) fv)) return FP_NAN;
    if (nper<=0) return FP_NAN;

    if (fabs(i)<1.0e-6) return -pmt*nper-fv;

    double iP1=i+1.0;
    double pow_iP1_nper=pow(iP1,nper);

    if (ptyp==0) {
        if (fabs(fv)<=1e-6) {
            return -pmt*(pow_iP1_nper-1.0)/i/pow_iP1_nper;
        } else {
            return -pmt*(pow_iP1_nper-1.0)/i/pow_iP1_nper-fv/pow_iP1_nper;
        }
    } else {
        if (fabs(fv)<=1e-6) {
            return -pmt*iP1*(pow_iP1_nper-1.0)/i/pow_iP1_nper;
        } else {
            return -pmt*iP1*(pow_iP1_nper-1.0)/i/pow_iP1_nper-fv/pow_iP1_nper;
        }
    }
}

double FV(double i, int nper, double pmt, double pv, int ptyp) {
    if (isnan((long double) i)) return FP_NAN;
    if (isnan((long double) pmt)) return FP_NAN;
    if (isnan((long double) pv)) return FP_NAN;
    if (nper<=0) return FP_NAN;

    if (fabs(i)<1.0e-6) return -pmt*nper-pv;

    double iP1=i+1.0;
    double pow_iP1_nper=pow(iP1,nper);

    if (ptyp==0) {
            return -pmt/(i/(pow_iP1_nper-1.0))-pv*pow_iP1_nper;
    } else {
            return -pmt/(i/iP1/(pow_iP1_nper-1.0))-pv*pow_iP1_nper;
    }
}


double NPER(double i, double pmt, double pv)
{
    if (isnan((long double) i)) return FP_NAN;
    if (isnan((long double) pv)) return FP_NAN;
    if (isnan((long double) pmt)) return FP_NAN;
    if (i<=0) return FP_NAN;
    if (pv<=0) return FP_NAN;
    if (pmt>=0) return FP_NAN;

    try {
        double iP1=i+1.0;
        //double tmp=(1.0-pv*i/pmt);
        double tmp=(1.0+pv*i/pmt); //pmt is expected to be negative
        if (tmp<=0) return FP_NAN;
        return -log(tmp)/log(iP1);
    } catch (...) {
        return FP_NAN;
    }

    return FP_NAN;
}


#endif
