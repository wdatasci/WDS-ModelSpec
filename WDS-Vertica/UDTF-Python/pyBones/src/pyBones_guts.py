import numpy as np

from pyBones_Utils import *

def pyBones_guts(local_parameters, first_row, last_row, row_to_output, row_index_last, row_index_next, static, tv, tv_empty_clone):

            #//////// in general, a guts block
            start=static.Offset
            if (start is None) or (start == Int_null):
                start=0
            if (static.N is None) or (static.N == Int_null):
                stop=start+1
            else:
                stop=start+static.N

            if local_parameters.EndPointInclusive :
                stop+=1

            if (local_parameters.BlockMaxLength!=Int_null)  and (stop-start>local_parameters.BlockMaxLength) :
                stop=local_parameters.BlockMaxLength+start

            # the numpy.recarray underlying tv can be extended via
            tv.parent.resize((stop-start,))

            #//RowIndex is initialized to a vector of length 1 since 1 row was input.
            tv.RowIndex=start
            i=0
            j=start
            stopM1=stop-1
            while j<stopM1:
                row_index_next[i]=i+1
                row_to_output.append(True)
                row_index_last.append(i)
                row_index_next.append(None)
                i+=1
                j+=1
                tv[i].RowIndex=j

            #// last_row represents last row index of the input reader
            #// the output writer will use last_row as the last 
            #// index to write, so it must be adjusted here
            
            last_row=stop-start

            return (first_row, last_row)



