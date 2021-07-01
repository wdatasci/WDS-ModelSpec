#ifndef WDS_VERTICA_VUTILITIES_LOADED
#define WDS_VERTICA_VUTILITIES_LOADED

#include <math.h>
#include <climits>

#ifndef WDS_MINMAX_DEFINED
#define WDS_MINMAX_DEFINED
vint min(vint a, vint b) { if (a!=vint_null && b!=vint_null) { if (a<b) return a; else return b; } return vint_null; }
vint max(vint a, vint b) { if (a!=vint_null && b!=vint_null) { if (a>b) return a; else return b; } return vint_null; }
vfloat min(vfloat a, vfloat b) { if (a!=vfloat_null && b!=vfloat_null) { if (a<b) return a; else return b; } return vfloat_null; }
vfloat max(vfloat a, vfloat b) { if (a!=vfloat_null && b!=vfloat_null) { if (a>b) return a; else return b; } return vfloat_null; }
#endif

#include "WDS/Util/core.h"
#include <cstdarg>
#include <regex>


class WDSException :  virtual public std::exception {
    private:
        std::string msg;
    public:
        WDSException(const char* arg, const char* file, int line) { 
            msg=std::string(arg);
            msg+=std::string(", FILE:")+std::string(file);
            msg+=std::string(", LINE:")+std::to_string(line);
        }
        virtual const char* what() const throw() { return msg.c_str(); }
        virtual ~WDSException() throw() {}
};

#define WDSThrow(args...) do { char __lcl_buf[1000]; sprintf(__lcl_buf,args); throw WDSException(__lcl_buf, __FILE__, __LINE__); } while (0)


bool bMatchLike(const std::string& a, const char* b) {
    try {
        const std::regex rb(b, std::regex_constants::basic);
        return std::regex_match(a,rb);
    } catch (const std::regex_error& e) { 
        if (e.code()==std::regex_constants::error_collate) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"collate"); 
        if (e.code()==std::regex_constants::error_ctype) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"ctype"); 
        if (e.code()==std::regex_constants::error_escape) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"escape"); 
        if (e.code()==std::regex_constants::error_backref) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"backref"); 
        if (e.code()==std::regex_constants::error_brack) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"brack"); 
        if (e.code()==std::regex_constants::error_paren) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"paren"); 
        if (e.code()==std::regex_constants::error_brace) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"brace"); 
        if (e.code()==std::regex_constants::error_badbrace) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"badbrace"); 
        if (e.code()==std::regex_constants::error_range) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"range"); 
        if (e.code()==std::regex_constants::error_space) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"space"); 
        if (e.code()==std::regex_constants::error_badrepeat) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"badrepeat"); 
        if (e.code()==std::regex_constants::error_complexity) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"complexity"); 
        if (e.code()==std::regex_constants::error_stack) WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,"stack"); 
        WDSThrow("bMatchLike error(std::string& '%s',const char* '%s'): %s",a.c_str(),b,e.what()); 
    } catch (std::exception e) { WDSThrow("bMatchLike error(std::string& '%s',const char* '%s')",a.c_str(),b); }
    return false;
}

bool bMatchLike(const VString* a, const std::string b) { return bMatchLike(a->str().c_str(),b.c_str()); }

bool bMatchLike(const std::string& a, const std::string& b) { return bMatchLike(a,b.c_str()); }



bool bIn(std::string& arg0,std::string& arg1) { return (arg0.compare(arg1)==0); }

//bool bIn(std::string  arg0,std::string& arg1) { return (arg0.compare(arg1)==0); }

bool bIn(std::string& arg0,const char* arg1) { return (arg0.compare(arg1)==0); }

//bool bIn(std::string arg0,const char* arg1) { return (arg0.compare(arg1)==0); }

bool bIn(std::string& arg0,std::string& arg1, std::string& arg2) { if (arg0.compare(arg1)==0) return true; return (arg0.compare(arg2)==0); }

//bool bIn(std::string  arg0,std::string& arg1, std::string& arg2) { if (arg0.compare(arg1)==0) return true; return (arg0.compare(arg2)==0); }

bool bIn(std::string& arg0,const char* arg1, const char* arg2) { if (arg0.compare(arg1)==0) return true; return (arg0.compare(arg2)==0); }

//bool bIn(std::string  arg0,const char* arg1, const char* arg2) { if (arg0.compare(arg1)==0) return true; return (arg0.compare(arg2)==0); }

bool bIn(std::string& arg0,std::string& arg1, std::string& arg2, std::string& arg3) { if (arg0.compare(arg3)==0) return true; return bIn(arg0,arg1,arg2); }

//bool bIn(std::string  arg0,std::string& arg1, std::string& arg2, std::string& arg3) { if (arg0.compare(arg3)==0) return true; return bIn(arg0,arg1,arg2); }

bool bIn(std::string& arg0,const char* arg1, const char* arg2, const char* arg3) { if (arg0.compare(arg3)==0) return true; return bIn(arg0,arg1,arg2); }

//bool bIn(std::string  arg0,const char* arg1, const char* arg2, const char* arg3) { if (arg0.compare(arg3)==0) return true; return bIn(arg0,arg1,arg2); }

bool bIn(std::string& arg0,std::string& arg1, std::string& arg2, std::string& arg3, std::string& arg4) { if (arg0.compare(arg4)==0) return true; return bIn(arg0,arg1,arg2,arg3); }
bool bIn(std::string& arg0,const char* arg1, const char* arg2, const char* arg3, const char* arg4) { if (arg0.compare(arg4)==0) return true; return bIn(arg0,arg1,arg2,arg3); }


bool bVStringIn(const VString* nArgs, ...) {
    va_list lArgs;
    va_start(lArgs, nArgs);
    bool rc=false;
    const VString* data=va_arg(lArgs,const VString*);
    if ( data->isNull() ) {
        va_end(lArgs);
        return false;
    }
    const VString* ldata;
    while ((!rc) && (ldata = va_arg(lArgs, const VString*))) {
        if ( data->equal(ldata) ) rc=true;
    }
    va_end(lArgs);
    return rc;
}


bool bIsAbsLt(vfloat a, vfloat b) {
    if (a==vfloat_null || b==vfloat_null) return false;
    return (fabs(a)<b);
}

bool bIsLt(vfloat a, vfloat b) {
    if (a==vfloat_null || b==vfloat_null) return false;
    return (a<b);
}

bool bIsAbsGt(vfloat a, vfloat b) {
    if (a==vfloat_null || b==vfloat_null) return false;
    return (fabs(a)>b);
}

bool bIsGt(vfloat a, vfloat b) {
    if (a==vfloat_null || b==vfloat_null) return false;
    return (a>b);
}

bool bIsNA(vint arg) { return ( arg==vint_null || arg==LONG_MIN || arg==LONG_MAX ); }
bool bIsNA(vfloat arg) { return ( arg==vfloat_null || isnan((long double) arg) || isinf((long double) arg) ); }

bool bIsPos(vint arg) { if (bIsNA(arg)) return false; else return (arg>0); }
bool bIsPos(vfloat arg) { if (bIsNA(arg)) return false; else return (arg>0.0); }

bool bIsNeg(vint arg) { if (bIsNA(arg)) return false; else return (arg<0); }
bool bIsNeg(vfloat arg) { if (bIsNA(arg)) return false; else return (arg<0.0); }


double dNAz(vfloat arg) { if (bIsNA(arg)) return 0.0; return (double) arg; }
int iNAz(vint arg) { if (bIsNA(arg)) return 0; return (int) arg; }

double iMax(vint a, vint b) { 
    if (bIsNA(a)) {
        if (bIsNA(b)) return b;
        else return vint_null;
    } else {
        if (bIsNA(b)) return a;
        if (a>=b) return a;
        return b;
    }
    return vint_null;
}

double dMin(vint a, vint b) { 
    if (bIsNA(a)) {
        if (bIsNA(b)) return b;
        else return vint_null;
    } else {
        if (bIsNA(b)) return a;
        if (a>=b) return b;
        return a;
    }
    return vint_null;
}

double dMax(vfloat a, vfloat b) { 
    if (bIsNA(a)) {
        if (bIsNA(b)) return b;
        else return vfloat_null;
    } else {
        if (bIsNA(b)) return a;
        if (a>=b) return a;
        return b;
    }
    return vfloat_null;
}

double dMin(vfloat a, vfloat b) { 
    if (bIsNA(a)) {
        if (bIsNA(b)) return b;
        else return vfloat_null;
    } else {
        if (bIsNA(b)) return a;
        if (a>=b) return b;
        return a;
    }
    return vfloat_null;
}

int iIf10(bool arg) { if (arg) return 1; else return 0; }

double dIf10(bool arg) { if (arg) return 1.0; else return 0.0; }


//Although not clear in docs, it appears that DateADT is the number of days since 2000-01-01.
//Because of the MonthID definition (2000-01 maps to 1), we will base calcs on this basis.
//
//This leap year treatment should work from 1801 through 2199.

DateADT dtWDSRefDate1900=(DateADT) -36524; //(int) dateIn("1900-01-01",false);
DateADT dtWDSRefDate2000=(DateADT) 0; //(int) dateIn("2000-01-01",false);
DateADT dtWDSRefDate2100=(DateADT) 36525; //(int) dateIn("2100-01-01",false);

int iWDSRefDate1900= -36524;
int iWDSRefDate19000228= -36466;
int iWDSRefDate2000= 0;
int iWDSRefDate2100= 36525;
int iWDSRefDate21000228= 36583;

int iWDSRefYear=2000;
int iWDSRefMonth=1;
int iWDSRefDay=1;

DateADT ymdToDateADT(int y, int m, int d) {
    int dc=0;
    int lpcm= (y-2000) % 4;
    int lpc=(y-2000-lpcm)/4;
    int lpcday0=lpc*1461;
    bool negday=(d<0); // some calls will shift left after calcs
    if (negday || d==0)
        dc=lpcday0+lpcm*365+1;
    else
        dc=lpcday0+lpcm*365+d;
    if (lpcm>0 || m>2) dc+=1;
    if (m==2) dc+=31;
    else if (m==3) dc+=59;
    else if (m==4) dc+=90;
    else if (m==5) dc+=120;
    else if (m==6) dc+=151;
    else if (m==7) dc+=181;
    else if (m==8) dc+=212;
    else if (m==9) dc+=243;
    else if (m==10) dc+=273;
    else if (m==11) dc+=304;
    else if (m==12) dc+=334;
    if (dc<iWDSRefDate19000228) dc+=1;
    if (dc>=iWDSRefDate19000228) dc-=1;
    if (negday) dc+=d;
    return dc;
}

void ymdFromDateADT(DateADT& arg, vint& y, vint& m, vint& d) {
    if (arg==vint_null) {
        y=vint_null;
        m=vint_null;
        d=vint_null;
    }
    int iarg=(int) arg;
    //correct for 1900 or 2100....
    if (iarg<=iWDSRefDate19000228) iarg-=1;
    if (iarg>iWDSRefDate21000228) iarg+=1;
    int dc=iarg - iWDSRefDate2000;
    int dcm=dc % 1461;
    if (dcm<0) dcm+=1461; //usa as a proper modulus function
    int lpc=(dc-dcm)/1461; //leap year count
    int lpcday0=lpc*1461;
    int lpcday=dc-lpcday0;
    int day0=0;
    int lpcy=0;
    if (lpcday<60) {
        y=lpc*4+iWDSRefYear;
        if (lpcday<31) {
            m=1;
            d=lpcday;
        } else {
            m=2;
            d=lpcday-31;
        }
        d+=1;
        return;
    } else {
        lpcday0+=1;
        lpcy=(dc-lpcday0)/365;
        y=lpc*4+lpcy+iWDSRefYear;
        dcm-=1;
        lpcday-=1;
        day0=lpcday-lpcy*365;
        if (day0<31 ) { m=1;  d=day0; } 
        else if (day0<59 ) { m=2;  d=day0-31 ; }
        else if (day0<90 ) { m=3;  d=day0-59 ; }
        else if (day0<120) { m=4;  d=day0-90 ; }
        else if (day0<151) { m=5;  d=day0-120; }
        else if (day0<180) { m=6;  d=day0-151; }
        else if (day0<212) { m=7;  d=day0-180; }
        else if (day0<243) { m=8;  d=day0-212; }
        else if (day0<273) { m=9;  d=day0-243; }
        else if (day0<304) { m=10; d=day0-273; }
        else if (day0<334) { m=11; d=day0-304; }
        else               { m=12; d=day0-334; }
        d+=1;
        return;
    }
    return;
}

vint iDate2Year(DateADT& arg) { 
    if (arg==vint_null) return vint_null;
    vint y=-1,m=-1,d=-1;
    ymdFromDateADT(arg,y,m,d);
    return y;
}

vint iDate2MonthID(DateADT arg) { 
    if (arg==vint_null) return vint_null;
    vint y=-1,m=-1,d=-1;
    ymdFromDateADT(arg,y,m,d);
    return (y-2000)*12+m;
}

int ymd2MonthID(int& y, int& m, int& d) {
    return (y-2000)*12+m;
}

int ym2MonthID(int& y, int& m) {
    return (y-2000)*12+m;
}


DateADT dMonthID2Date(int arg, int d) {
    int m=(arg-1) % 12;
    if ( m < 0 ) m+=12;
    int y=(arg-m)/12+2000;
    return ymdToDateADT(y,m+1,d);
}

DateADT dMonthID2Date(int arg) {
    return dMonthID2Date(arg, 1);
}

DateADT dtAddMonths(DateADT& arg, int arg2, int d2) {  //d2==0 keeps the existing day, d2==-1 moves to EOM
    if (arg==vint_null) return vint_null;
    vint y=-1,m=-1,d=-1;
    ymdFromDateADT(arg,y,m,d);
    vint mid=(y-2000)*12+m;
    vint midParg2=mid+arg2;
    if (d2==-1) {
        midParg2+=1;
    } else if (d2==0) {
        d2=d;
    } else {
        d2=1;
    }
    int m2=(midParg2-1) % 12;
    if ( m2 < 0 ) m2+=12;
    int y2=(midParg2-m2)/12+2000;
    m2+=1;
    if (d2>28) {
        if (m2==2) return d2=min(d2,28);
        else if (m2==4 || m2==6 || m2==9 || m2==11) d2=min(d2,30);
    }
    return ymdToDateADT(y2,m2,d2);
}
   
DateADT dtAddMonths(DateADT& arg, int arg2) {
    return dtAddMonths(arg,arg2,0);
}
   
DateADT dtEOM(DateADT& arg) {
    return dtAddMonths(arg,0,-1);
}
   
vint iDateDiffDays(DateADT a, DateADT b) {
    if (a==vint_null || b==vint_null) return vint_null;
    return (b-a);
}





#endif
