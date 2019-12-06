/*
MIT License

Copyright (c) 2019 Wypasek Data Science, Inc.

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

/* %CrossProductWords returns a collection of words from the cross product of combinations of lists. */

%LoadMacros(wds.range wds.Iterator);

%global CrossProductWords_Loaded;
%let CrossProductWords_Loaded=1;

%macro CrossProductWords(first, second, third, JoinChar=, dlm=%str( ));
    /*Note: watch the semicolons, if placed after the Inits, it will be output in the macro expansion*/
    %local CrossProductWords_N;
    %let CrossProductWords_N=0;
    %IteratorInit(CPWs_First,%nrquote(&first),dlm=%str(&dlm))
    %IteratorInit(CPWs_Second,%nrquote(&second),dlm=%str(&dlm))
    %IteratorInit(CPWs_Third,%nrquote(&third),dlm=%str(&dlm))
    %do %while ( %IteratingOver(CPWs_First) );
    %do %while ( %IteratingOver(CPWs_Second) );
        %if &CPWs_Third_Count eq 0 %then %do;
            %if &CrossProductWords_N %then %do;&dlm%end; %else %let CrossProductWords_N=1;
            %do;&CPWs_First_Word&JoinChar&CPWs_Second_Word%end;
        %end; %else %do;
            %do %while ( %IteratingOver(CPWs_Third) );
                %if &CrossProductWords_N %then %do;&dlm%end;%else %let CrossProductWords_N=1;
                %do;&CPWs_First_Word&JoinChar&CPWs_Second_Word&JoinChar&CPWs_Third_Word%end;
            %end;
        %end;
    %end;
    %end;
%mend;
        

/* test >>> 

%put Start of Test;

%let x=a b c d e f g what the heck;

%let y=d e the huh;

%let z=%CrossProductWords(&x,&y);

%put x=&x;
%put y=&y;
%put z=&z;

%let z=%CrossProductWords(a b c, 1 2 3, x y z);
%put z=&z;
%let z=%CrossProductWords(a b c, 1 2 3, x y z, joinchar=-);
%put z=&z;

%put End of Test;

 <<< test */

