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

/* %StripWords strips a second set of words from a first set. */

%LoadMacros(wds.range wds.Iterator);

%global StripWords_Loaded;
%let StripWords_Loaded=1;

%macro StripWords(first, second, dlm=%str( ));
    /*Note: watch the semicolons, if placed after the Inits, it will be output in the macro expansion*/
    %IteratorInit(StripWords_First,%nrquote(&first),dlm=%str(&dlm))
    %IteratorInit(StripWords_Second,%nrquote(&second),dlm=%str(&dlm))
    %local StripWords_RV StripWords_N StripWords_Found;
    %let StripWords_RV=;
    %let StripWords_N=0;
    %do %while (%IteratingOver(StripWords_First));%let StripWords_Found=0;%IteratorReset(StripWords_Second)
        %do %while ( (&StripWords_Found eq 0 ) and %IteratingOver(StripWords_Second) );
            %if &StripWords_First_Word eq &StripWords_Second_Word %then %let StripWords_Found=1;
        %end;
        %if &StripWords_Found eq 0 %then %do;%if &StripWords_N %then %do;&dlm%end;%else %let StripWords_N=1;&StripWords_First_Word%end;
    %end;
%mend;
        

/* test >>> 

%put Start of Test;

%let x=a b c d e f g what the heck;

%let y=d e the huh;

%let z=%StripWords(&x,&y);

%put x=&x;
%put y=&y;
%put z=&z;

%put End of Test;

 <<< test */

