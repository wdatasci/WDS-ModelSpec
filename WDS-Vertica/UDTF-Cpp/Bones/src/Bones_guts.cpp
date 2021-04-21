
            //////// in general, a guts block

            int start=Offset;
            int stop=start+N;

			if (EndPointInclusive==vbool_true) stop+=1;

			if (BlockMaxLength!=vint_null && stop-start>BlockMaxLength) stop=BlockMaxLength+start;

            for (int i=start;i<stop;i++) RowIndex.push_back(i);

            // last_row represents last row index of the input reader
            // the output writer will use last_row as the last 
            // index to write, so it must be adjusted here
            
            last_row=stop-start;

