
            //////// in general, a guts block
            //


            int start=first_row;
            int stop=last_row;

            int i;
            for (i=start; i<stop; i++) {
                ymdFromDateADT(TestDate[i],y[i],m[i],d[i]);
            }

            ExState lStateX(ExState::A);

            for (i=start; i<stop; i++) {
                if (lStateX==ExState::A) lStateX=ExState::Z;
                else lStateX=ExState::A;
                lState[i]=lStateX.Label();
                lState_Code[i]=lStateX.Code();
            }





