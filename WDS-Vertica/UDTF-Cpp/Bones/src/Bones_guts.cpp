
            //////// in general, a guts block

            int start=Offset;
            int stop=start+N;

            if (EndPointInclusive==vbool_true) stop+=1;

            if (BlockMaxLength!=vint_null && stop-start>BlockMaxLength) stop=BlockMaxLength+start;

            //RowIndex is initialized to a vector of length 1 since 1 row was input.
            RowIndex[0]=start;
            for (int i=start+1;i<stop;i++) RowIndex.push_back(i);

            // last_row represents last row index of the input reader
            // the output writer will use last_row as the last 
            // index to write, so it must be adjusted here
            
            last_row=stop-start;

