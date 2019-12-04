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

/* WDS - Notes
    This library of SAS macros, tested with WPS, is based on core utilities 
    used by Christian Wypasek (who never trusted SAS autos when he first 
    learned the language).

    In the user's or common SAS macro library, it is assumed that some autoexec.sas
    file will: 
        - Define a macro variable wds which contains the path to the parent directory of 
        this file, such as (on Windows):
            %let wds=<<<<root-path>>>\WDataSci\WDS-ModelSpec\master\WDS-SAS\Macros;
        - Include this file.

    As with "wds", the user can also define other short-hand variables to other macro 
    libraries.  Then, regardless of a SAS autos path, a call of 
        %LoadMacros(wds.File1 other.File2) 
    will be expanded to 
        %include "&wds\File1.sas"; %include "&other\File2.sas";


    This file also includes macro functions for:
        - WordCount, returns the word count of a string, with optional non-space delimiter
        - IsDefined, returns True if defined, use via %if %IsDefined(arg) ne %then.....

*/


%macro WordCount(WordCountArg, dlm=%str( ), WordCountLimit=1024, WordCountTest=0);
    %local WordCountI WordCountIP1;
    %let WordCountI=0;
    %let WordCountIP1=1;
    %do %while ( (&WordCountIP1 le &WordCountLimit) and ( %length(%qscan(%superq(WordCountArg),&WordCountIP1,%str(&dlm))) gt 0 ) );
        %if &WordCountTest ne 0 %then %put WordCountIP1=&WordCountIP1 %qscan(%superq(WordCountArg),&WordCountIP1,%str(&dlm));
        %let WordCountI=&WordCountIP1;
        %let WordCountIP1=%eval(&WordCountIP1 +1);
    %end;
    &WordCounti
%mend;

%macro LoadMacros(LoadMacrosArg, dlm=%str( ));
    %local LoadMacrosN LoadMacrosI LoadMacrosTempString LoadMacrosTempN LoadMacrosTempString1 LoadMacrosTempString2;
    %let LoadMacrosN=%WordCount(%nrquote(&LoadMacrosArg),dlm=%str(&dlm));
    %put LoadMacrosN=&LoadMacrosN;
    %do LoadMacrosI=1 %to &LoadMacrosN;
        %let LoadMacrosTempString=%qscan(%superq(LoadMacrosArg),&LoadMacrosI,%str(&dlm));
        %put LoadMacros is working on "&LoadMacrosTempString";
        %let LoadMacrosTempN=%WordCount(&LoadMacrosTempString,dlm=%str(.));
        %put LoadMacrosTempN=&LoadMacrosTempN;
        %if &LoadMacrosTempN eq 1 %then %do;
            %put LoadMacros is including "&LoadMacrosTempString..sas";
            %if %sysfunc(fileexist("&LoadMacrosTempString..sas")) %then %do;
                %include "&LoadMacrosTempString..sas";
            %end; %else %do;
                %put LoadMacros cannot resolve &LoadMacrosTempString to "&LoadMacrosTempString..sas";
            %end;
        %end; %else %if &LoadMacrosTempN eq 2 %then %do;
            %let LoadMacrosTempString1=%qscan(&LoadMacrosTempString,1,%str(.));
            %put LoadMacrosTempString1=&LoadMacrosTempString1;
            %if %symexist(&LoadMacrosTempString1) %then %do;
                %let LoadMacrosTempString2=%qscan(&LoadMacrosTempString,2,%str(.));
                %put LoadMacrosTempString2=&LoadMacrosTempString2;
                %if %symexist(&LoadMacrosTempString2._Loaded) %then %do;
                    %put LoadMacros already has &LoadMacrosTempString2 loaded;
                %end; %else %do;
                    %put LoadMacros is including "&LoadMacrosTempString";
                    %put    where &LoadMacrosTempString1=%superq(&LoadMacrosTempString1);
                    %put    and file is %superq(&LoadMacrosTempString1)%str(\)%qscan(&LoadMacrosTempString,2,%str(.)).sas;
                    %if %sysfunc(fileexist("%superq(&LoadMacrosTempString1)%str(\)%qscan(&LoadMacrosTempString,2,%str(.)).sas")) %then %do;
                        %include "%superq(&LoadMacrosTempString1)%str(\)%qscan(&LoadMacrosTempString,2,%str(.)).sas";
                    %end; %else %do;
                        %put LoadMacros cannot resolve &LoadMacrosTempString to  "%superq(&LoadMacrosTempString1)%str(\)%qscan(&LoadMacrosTempString,2,%str(.)).sas";
                    %end;
                %end;
            %end; %else %do;
                %put LoadMacros cannot resolve shorthand &LoadMacrosTempString1;
            %end;
        %end; %else %do;
            %put LoadMacros cannot resolve &LoadMacrosTempString;
        %end;
    %end;
%mend;





/* test >>> 

%let x=hey what the heck   ;
%put xxx&x.xxx;


%let xc=%WordCount(&x,WordCountTest=1);
%put WordCount(&x,WordCountTest=1)=&xc;

%let xc=%WordCount(&x,dlm=t);
%put WordCount(&x,dlm=t)=&xc;

%let xc=%WordCount(&x,dlm=h);
%put WordCount(&x,dlm=h)=&xc;

%let xc=%WordCount(&x,dlm=k,WordCountTest=1);
%put WordCount(&x,dlm=k,WordCountTest=1)=&xc;

%let x=%str(hey what the heck   );
%put xxx&x.xxx;

%let xc=%WordCount(&x,dlm=k,WordCountTest=1);
%put WordCount(&x,dlm=k,WordCountTest=1)=&xc;

%let x=%str(hey what the heck   );


%LoadMacros(wds.range what.the huh);

 <<< test */


