/*
MIT License

Copyright (c) 2019,2020,2021,2022 Wypasek Data Science, Inc.

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

/* %PullWordsFromColumn pulls all of the string values from a dataset column 
and concatenates the values into a delimited string. */

%global PullWOrdsFromColumn_Loaded;
%let PullWOrdsFromColumn_Loaded=1;


%macro PullWordsFromColumn(lDataSetName,lColumnName,lTargetMacroVariable,dlm=|,whereclause=(1=1),wrapinquotes=);

	%local lDataSetName lColumnName lTargetMacroVariable dlm whereclause wrapinquotes;
	%global &lTargetMacroVariable;

	data _null_;
		length PullWordsFromColumnTarget $4000 PullWordsFromColumnTargetLength 8.;
		retain PullWordsFromColumnTarget("") PullWordsFromColumnTargetLength(0);
		set &lDataSetName end=PullWordsFromColumnEOF;
		where &whereclause;
		templength=length(trim(&lColumnName));
		%if &wrapinquotes eq %then %do;
			substr(PullWordsFromColumnTarget,PullWordsFromColumnTargetLength+1,PullWordsFromColumnTargetLength+templength)=&lColumnName;
			PullWordsFromColumnTargetLength=PullWordsFromColumnTargetLength+templength;
		%end; %else %do;
			substr(PullWordsFromColumnTarget,PullWordsFromColumnTargetLength+1,PullWordsFromColumnTargetLength+templength+2)=
					'"' || trim(&lColumnName) || '"';
			PullWordsFromColumnTargetLength=PullWordsFromColumnTargetLength+templength+2;
		%end;
		if PullWordsFromColumnEOF then do;
			call symput("&lTargetMacroVariable",PullWordsFromColumnTarget);
		end; else do;
			PullWordsFromColumnTargetLength=PullWordsFromColumnTargetLength+1;
			substr(PullWordsFromColumnTarget,PullWordsFromColumnTargetLength,1)="&dlm";
		end;
	run;
		
%put PullWordsFromColumn(&lDataSetName,&lColumnName) = &&&lTargetMacroVariable;
%put Number of Words in PullWordsFromColumn(&lDataSetName,&lColumnName) = %WordCount(%quote(&&&lTargetMacroVariable),dlm=&dlm);
		
%mend;



