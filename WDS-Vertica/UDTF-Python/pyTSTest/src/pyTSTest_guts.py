import numpy as np

from pyTSTest_Enums import *
from pyTSTest_Utils import *

def pyTSTest_guts(local_parameters, first_row, last_row, row_to_output, row_index_last, row_index_next, static, tv, tv_empty_clone):

            start=first_row
            stop=last_row

            #int i;
            #for (i=start; i<stop; i++) {
                #ymdFromDateADT(TestDate[i],y[i],m[i],d[i]);
            #}

            #ExState lStateX(ExState::A);

            #for (i=start; i<stop; i++) {
            #    if (lStateX==ExState::A) lStateX=ExState::Z;
            #    else lStateX=ExState::A;
            #    lState[i]=lStateX.Label();
            #    lState_Code[i]=lStateX.Code();
            #}

            for i in range(start,stop):
                o=tv[i].TestDate.astype(object)
                tv[i].y=o.year
                tv[i].m=o.month
                tv[i].d=o.day

            _lState=ExState.A
            _lState_Lag1=ExState.Unk

            for i in range(start, stop):
                if _lState is ExState.A:
                    _lState=ExState.Z
                else:
                    _lState=ExState.A
                tv[i].lState=_lState.Label()
                tv[i].lState_Code=_lState.Code()

            return (first_row, last_row)




