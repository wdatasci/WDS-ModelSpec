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

/* %Iterator provides a simple iterator constructor, see usage below. */

%LoadMacros(wds.range);

%global Iterator_Loaded;
%let Iterator_Loaded=1;

%macro IteratorInit(name, arg, dlm=%str( ));
    %global &name._List &name._Count &name._Index &name._Index_Lag1 &name._Word &name._Word_Lag1 &name._dlm;
    %let &name._List=%nrquote(&arg);
    %let &name._Count=%WordCount(%nrquote(&arg),dlm=%str(&dlm));
    %let &name._Index_Lag1=-1;
    %let &name._Index=0;
    %let &name._Word_Lag1=;
    %let &name._Word=;
    %let &name._dlm=%str(&dlm);
%mend;

%macro IteratorRangeInit(name, start, stop, step=1, dlm=%str( ));
    %global &name._List &name._Count &name._Index &name._Index_Lag1 &name._Word &name._Word_Lag1 &name._dlm;
    %let &name._List=%range(start=&start,stop=&stop,step=&step,dlm=%str(&dlm));
    %let &name._Count=%WordCount(%superq(&name._List),dlm=%str(&dlm));
    %let &name._Index_Lag1=-1;
    %let &name._Index=0;
    %let &name._Word_Lag1=;
    %let &name._Word=;
    %let &name._dlm=%str(&dlm);
%mend;

%macro IteratorReset(name);
    %global &name._List &name._Count &name._Index &name._Index_Lag1 &name._Word &name._Word_Lag1 &name._dlm;
    %let &name._Index_Lag1=-1;
    %let &name._Index=0;
    %let &name._Word_Lag1=;
    %let &name._Word=;
%mend;

%macro IteratingOver(name);
    %global &name._List &name._Count &name._Index &name._Index_Lag1 &name._Word &name._Word_Lag1 &name._dlm;
    %if %superq(&name._Index) lt %superq(&name._Count) %then %do;
        %let &name._Index_Lag1=&&&name._Index;
        %let &name._Word_Lag1=&&&name._Word;
        %let &name._Index=%eval(&&&name._Index+1);
        %let &name._Word=%qscan(%superq(&name._List),&&&name._Index,%superq(&name._dlm));
    1 %end;
    %else %do;
        %let &name._Index_Lag1=-1;
        %let &name._Index=0;
        %let &name._Word_Lag1=;
        %let &name._Word=;
    0 %end;
%mend;

/* test >>> 

%put Start of Test;

%IteratorInit(Hey, a b c e f g x y z);
%do %while (%IteratingOver(Hey));
    %put index=&Hey_Index word=&Hey_Word;
%end;
%do %while (%IteratingOver(Hey));
    %put index=&Hey_Index word=&Hey_Word;
%end;

%IteratorInit(What, a|b|c, dlm=|);
%do %while (%IteratingOver(What));
    %put index=&What_Index word=&What_Word;
%end;

%put End of Test;

 <<< test */

