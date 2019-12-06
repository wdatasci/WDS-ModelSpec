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

/* %ArtificialTreatment creates artificial variables based upon a standardized set of options. 
    See the WDS Model Specification documentation for details.

    This implementation is SAS-only, as opposed to calling a common C-block of code.
    
    Use "options mprint;" to see macro generated code in the log.


    This first version is written pedantically, streamlining will occur with updates.

*/

%LoadMacros(wds.range wds.Iterator wds.StripWords wds.CrossProductWords);

%global ArtificialTreatments_Loaded;
%let ArtificialTreatments_Loaded=1;


%macro CleanTreatment(arg);
    %local uarg;
    %let uarg=%upcase(&arg);
    %if &uarg eq STRAIGHT                 %then %do;None%end;
    %else %if &uarg eq NUMERIC            %then %do;None%end;
    %else %if &uarg eq MISSINGS           %then %do;CodedMissings%end;
    %else %if &uarg eq BUCKETSLC          %then %do;DiscreteLC%end;
    %else %if &uarg eq LEVELSLC           %then %do;DiscreteLC%end;
    %else %if &uarg eq DISCRETIZELC       %then %do;DiscreteLC%end;
    %else %if &uarg eq INTERVALSLC        %then %do;DiscreteLC%end;
    %else %if &uarg eq DISCLC             %then %do;DiscreteLC%end;
    %else %if &uarg eq BZ0LC              %then %do;DiscreteLC%end;
    %else %if &uarg eq BSO0LC             %then %do;DiscreteLC%end;
    %else %if &uarg eq CAGLAD             %then %do;DiscreteLC%end;
    %else %if &uarg eq COLLOR             %then %do;DiscreteLC%end;
    %else %if &uarg eq LCRL               %then %do;DiscreteLC%end;
    %else %if &uarg eq BUCKETS            %then %do;Discrete%end;
    %else %if &uarg eq LEVELS             %then %do;Discrete%end;
    %else %if &uarg eq DISCRETIZE         %then %do;Discrete%end;
    %else %if &uarg eq INTERVALS          %then %do;Discrete%end;
    %else %if &uarg eq DISC               %then %do;Discrete%end;
    %else %if &uarg eq BZ0                %then %do;Discrete%end;
    %else %if &uarg eq BSO0               %then %do;Discrete%end;
    %else %if &uarg eq CADLAG             %then %do;Discrete%end;
    %else %if &uarg eq CORLOL             %then %do;Discrete%end;
    %else %if &uarg eq RCLL               %then %do;Discrete%end;
    %else %if &uarg eq BZ1                %then %do;Hats%end;
    %else %if &uarg eq BSO1               %then %do;Hats%end;
    %else %if &uarg eq INTEGRATEDHATS     %then %do;iHats%end;
    %else %if &uarg eq BSPLINEO2          %then %do;BSplineOrder2%end;
    %else %if &uarg eq BZ2                %then %do;BSplineOrder2%end;
    %else %if &uarg eq BSO2               %then %do;BSplineOrder2%end;
    %else %if &uarg eq BSPLINEO3          %then %do;BSplineOrder3%end;
    %else %if &uarg eq BZ3                %then %do;BSplineOrder3%end;
    %else %if &uarg eq BSO3               %then %do;BSplineOrder3%end;
    %else %if &uarg eq CAT                %then %do;Categorical%end;
    %else %if &uarg eq STRING             %then %do;Categorical%end;
    %else %if &uarg eq CATNUM             %then %do;CategoricalNumeric%end;
    %else %if &uarg eq NCAT               %then %do;CategoricalNumeric%end;
    %else %if &uarg eq NCATEGORICAL       %then %do;CategoricalNumeric%end;

    %else %if &uarg eq NONE               %then %do;None%end;
    %else %if &uarg eq CONSTANT           %then %do;Constant%end;
    %else %if &uarg eq CODEDMISSINGS      %then %do;CodedMissings%end;
    %else %if &uarg eq DISCRETELC         %then %do;DiscreteLC%end;
    %else %if &uarg eq DISCRETE           %then %do;Discrete%end;
    %else %if &uarg eq HATS               %then %do;Hats%end;
    %else %if &uarg eq IHATS              %then %do;iHats%end;
    %else %if &uarg eq BSPLINEORDER2      %then %do;BSplineOrder2%end;
    %else %if &uarg eq BSPLINEORDER3      %then %do;BSplineOrder3%end;
    %else %if &uarg eq CATEGORICAL        %then %do;Categorical%end;
    %else %if &uarg eq CATEGORICALNUMERIC %then %do;CategoricalNumeric%end;
    %else %do;&arg%end;
%mend;


%macro ArtificialTreatment(SourceVariable=SourceVariable
        , Treatment=Hats
        , CriticalValues=
        , CleanLimits=
        , AlternateBaseName=
        , JoinChar=_
        , DropList=
        , MarginalSetName=MarginalSetName_Global
        , MarginalTrimmedSetName=MarginalTrimmedSetName_Global
        , RunningMarginalSetName=RunningMarginalSetName_Global
        , RunningMarginalTrimmedSetName=RunningMarginalTrimmedSetName_Global
        , eps=0.00000001
        );

        if _N_ eq 1 then
        put "starting code generation associated with ArtificialTreatment(&SourceVariable,&Treatment,&AlternateBaseName)";

        drop ATTmp_i ATTmp_iM1 ATTmp_iM2 ATTmp_ia ATTmp_iaM1 ATTmp_iaM2 ATTmp_iaM3
            ATTmp_xMci ATTmp_xMciM1 ATTmp_xMciM2
            ATTmp_fo0 ATTmp_fo1 ATTmp_fo2 ATTmp_fo3
            ATTmp_double 
            ;


        %global &MarginalSetName &MarginalTrimmedSetName;
        %global &RunningMarginalSetName &RunningMarginalTrimmedSetName;

        %local ArtIndexList ArtTake ArtI ArtII ArtIIa ArtIIaP1 ArtCVN ArtN ArtBaseName ArtTempName ArtComp;

        %let Treatment=%CleanTreatment(&Treatment);

        %if &AlternateBaseName eq %then %let ArtBaseName=&SourceVariable.&JoinChar;
        %else %let ArtBaseName=&AlternateBaseName.&JoinChar;

        %if &Treatment eq None %then %do;
            %if %str(&DropList) eq 1 %then %do;
                %let &MarginalSetName=;
                %let &MarginalTrimmedSetName=;
                %return;
            %end;
            &ArtBaseName.1=&SourceVariable;
            label &ArtBaseName.1="Art 1 for &SourceVariable, Treatment=&Treatment";
            %let &MarginalSetName=&ArtBaseName.1;
            %let &MarginalTrimmedSetName=&ArtBaseName.1;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %return;
        %end;

        %if &Treatment eq Constant %then %do;
            %if (%str(&DropList) eq 1) or (%str(&CriticalValues) eq ) %then %do;
                %let &MarginalSetName=;
                %let &MarginalTrimmedSetName=;
                %return;
            %end;
            &ArtBaseName.1=%qscan(%str(&CriticalValues),1,%str( ));
            label &ArtBaseName.1="Art 1 for &SourceVariable, Treatment=&Treatment";
            %let &MarginalSetName=&ArtBaseName.1;
            %let &MarginalTrimmedSetName=&ArtBaseName.1;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %return;
        %end;

        %if &Treatment eq CodedMissings %then %do;
            %if %str(&DropList) eq %then %do;
                %let ArtTake=1;
                %let &MarginalSetName=&ArtBaseName.0 &ArtBaseName.1;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end; %else %if %str(&DropList) eq 0 %then %do;
                %let ArtTake=1;
                %let &MarginalSetName=&ArtBaseName.0 &ArtBaseName.1;
                %let &MarginalTrimmedSetName=&ArtBaseName.1;
            %end; %else %if %str(&DropList) eq 1 %then %do;
                %let ArtTake=1;
                %let &MarginalSetName=&ArtBaseName.0 &ArtBaseName.1;
                %let &MarginalTrimmedSetName=&ArtBaseName.0;
            %end; %else %do; 
                %let ArtTake=0;
            %end;
            %if &ArtTake %then %do;
                &ArtBaseName.0=0.0;
                &ArtBaseName.1=0.0;
                if &SourceVariable eq . then do;
                    &ArtBaseName.0=1.0;
                %if %str(&CleanLimits) ne %then %do;
                end; else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then do;
                    &ArtBaseName.0=1.0;
                %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                end; else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then do;
                    &ArtBaseName.0=1.0;
                %end;
                %end;
                end; else do;
                    &ArtBaseName.1=&SourceVariable;
                end;
                label &ArtBaseName.0="Art 0 for &SourceVariable, MissingCode, Treatment=&Treatment";
                label &ArtBaseName.1="Art 1 for &SourceVariable, Treatment=&Treatment";
                %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
                %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %end;
            %return;
        %end;

        %if (&Treatment eq Discrete) or (&Treatment eq DiscreteLC) %then %do;
            %if &Treatment eq DiscreteLC %then 
                %let ArtComp= le (&eps)+ ; 
            %else %let ArtComp= lt (-&eps)+ ;
            %let ArtCVN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN+1));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                &ArtBaseName&ArtIterator_Word=0.0;
                %if &ArtIterator_Index eq 1 %then %do;
                    label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, MissingCode, Treatment=&Treatment";
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    %if &Treatment eq DiscreteLC %then %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, (-Infty, %qscan(&CriticalValues,1,%str( ))], Treatment=&Treatment";
                    %end; %else %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, (-Infty, %qscan(&CriticalValues,1,%str( ))), Treatment=&Treatment";
                    %end;
                %end; %else %if &ArtIterator_Index eq &ArtIterator_Count %then %do;
                    %if &Treatment eq DiscreteLC %then %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),Infty), Treatment=&Treatment";
                    %end; %else %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, [%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),Infty), Treatment=&Treatment";
                    %end;
                %end; %else %do;
                    %if &Treatment eq DiscreteLC %then %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),%qscan(&CriticalValues,&ArtIterator_Word,%str( ))], Treatment=&Treatment";
                    %end; %else %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, [%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),%qscan(&CriticalValues,&ArtIterator_Word,%str( ))), Treatment=&Treatment";
                    %end;
                %end;
            %end;
            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Index eq 1 %then %do;
                    if &SourceVariable eq . then &ArtBaseName&ArtIterator_Word=1.0;
                    %if "%str(&CleanLimits)" ne "" %then %do;
                    else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                    %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                    %end;
                    %end;
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    else if &SourceVariable &ArtComp %qscan(&CriticalValues,&ArtIterator_Index_Lag1,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                %end; %else %if &ArtIterator_Index eq &ArtIterator_Count %then %do;
                    else &ArtBaseName&ArtIterator_Word=1.0;
                %end; %else %do;
                    else if &SourceVariable &ArtComp %qscan(&CriticalValues,&ArtIterator_Index_Lag1,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                %end;
            %end;
            %let &MarginalSetName=%CrossProductWords(&ArtBaseName,&ArtIndexList);
            %if "%str(&DropList)" ne "" %then %do;
                %let &MarginalTrimmedSetName=%CrossProductWords(&ArtBaseName,%StripWords(&ArtIndexList,&DropList));
            %end; %else %do;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end;
            %put MarginalSetName=&MarginalSetName, &&&MarginalSetName;
            %put MarginalTrimmedSetName=&MarginalTrimmedSetName, &&&MarginalTrimmedSetName;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %put RunningMarginalSetName=&RunningMarginalSetName, &&&RunningMarginalSetName;
            %put RunningMarginalTrimmedSetName=&RunningMarginalTrimmedSetName, &&&RunningMarginalTrimmedSetName;
            %return;
        %end;

        %if &Treatment eq Hats %then %do;
            %let ArtCVN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %do %while(%IteratingOver(ArtIterator));
                &ArtBaseName&ArtIterator_Word=0.0;
                %if &ArtIterator_Index eq 1 %then %do;
                    label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, MissingCode, Treatment=&Treatment";
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    %let ArtTempName=Art &ArtIterator_Word for &SourceVariable, -\_ (%qscan(&CriticalValues,1,%str( )),%qscan(&CriticalValues,2,%str( ))), Treatment=&Treatment;
                    label &ArtBaseName.&ArtIterator_Word="&ArtTempName";
                %end; %else %if &ArtIterator_Index eq &ArtIterator_Count %then %do;
                    %let ArtTempName=Art &ArtIterator_Word for &SourceVariable, _/- (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),%qscan(&CriticalValues,&ArtIterator_Word,%str( ))), Treatment=&Treatment;
                    label &ArtBaseName.&ArtIterator_Word="&ArtTempName";
                %end; %else %do;
                    %let ArtTempName=Art &ArtIterator_Word for &SourceVariable, _/\_ (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),%qscan(&CriticalValues,&ArtIterator_Word,%str( )),%qscan(&CriticalValues,&ArtIterator_Word_Lead1,%str( )));
                    %let ArtTempName=&ArtTempName, Treatment=&Treatment;
                    label &ArtBaseName.&ArtIterator_Word="&ArtTempName";
                %end;
            %end;

            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Index eq 1 %then %do;
                    if &SourceVariable eq . then &ArtBaseName&ArtIterator_Word=1.0;
                    %if "%str(&CleanLimits)" ne "" %then %do;
                    else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                    %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                    %end;
                    %end;
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    else if &SourceVariable le %qscan(&CriticalValues,1,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                %end; %else %do;
                    else if &SourceVariable le %qscan(&CriticalValues,&ArtIterator_Word,%str( )) then do;
                        &ArtBaseName&ArtIterator_Word=(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )))) 
                                / ((%qscan(&CriticalValues,&ArtIterator_Word,%str( )))-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))));
                        &ArtBaseName&ArtIterator_Word_Lag1=1.0-&ArtBaseName&ArtIterator_Word;
                        end;
                %end;
            %end;
                    else &ArtBaseName&ArtIterator_Word_Last=1.0;

            %let &MarginalSetName=%CrossProductWords(&ArtBaseName,&ArtIndexList);
            %if "%str(&DropList)" ne "" %then %do;
                %let &MarginalTrimmedSetName=%CrossProductWords(&ArtBaseName,%StripWords(&ArtIndexList,&DropList));
            %end; %else %do;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end;
            %put MarginalSetName=&MarginalSetName, &&&MarginalSetName;
            %put MarginalTrimmedSetName=&MarginalTrimmedSetName, &&&MarginalTrimmedSetName;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %put RunningMarginalSetName=&RunningMarginalSetName, &&&RunningMarginalSetName;
            %put RunningMarginalTrimmedSetName=&RunningMarginalTrimmedSetName, &&&RunningMarginalTrimmedSetName;
            %return;
        %end;

        %if &Treatment eq iHats %then %do;
            ATTmp_double=0.0;
            drop ATTmp_double;
            %let ArtN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtN));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                &ArtBaseName&ArtIterator_Word=0.0;
                %if &ArtIterator_Index eq 1 %then %do;
                    label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, MissingCode, Treatment=&Treatment";
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    %let ArtTempName=Art &ArtIterator_Word for &SourceVariable, /c- (%qscan(&CriticalValues,1,%str( )),%qscan(&CriticalValues,2,%str( ))), Treatment=&Treatment;
                    label &ArtBaseName.&ArtIterator_Word="&ArtTempName";
                %end; %else %if &ArtIterator_Index eq &ArtIterator_Count %then %do;
                    %let ArtTempName=Art &ArtIterator_Word for &SourceVariable, _u/ (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),%qscan(&CriticalValues,&ArtIterator_Word,%str( ))), Treatment=&Treatment;
                    label &ArtBaseName.&ArtIterator_Word="&ArtTempName";
                %end; %else %do;
                    %let ArtTempName=Art &ArtIterator_Word for &SourceVariable, _s- (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )),%qscan(&CriticalValues,&ArtIterator_Word,%str( )),%qscan(&CriticalValues,&ArtIterator_Word_Lead1,%str( )));
                    %let ArtTempName=&ArtTempName, Treatment=&Treatment;
                    label &ArtBaseName.&ArtIterator_Word="&ArtTempName";
                %end;
            %end;

            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Index eq 1 %then %do;
                    if &SourceVariable eq . then &ArtBaseName&ArtIterator_Word=1.0;
                    %if "%str(&CleanLimits)" ne "" %then %do;
                    else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                    %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then &ArtBaseName&ArtIterator_Word=1.0;
                    %end;
                    %end;
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    else do;

                    if &SourceVariable le %qscan(&CriticalValues,1,%str( )) then 
                        &ArtBaseName&ArtIterator_Word=(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word,%str( ))));

                %end; %else %do;
                    else if &SourceVariable le %qscan(&CriticalValues,&ArtIterator_Word,%str( )) then do;
                        ATTmp_double=((&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))))**(2.0)) 
                                / ((%qscan(&CriticalValues,&ArtIterator_Word,%str( )))-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))))
                                / 2.0;
                        &ArtBaseName&ArtIterator_Word=&ArtBaseName&ArtIterator_Word+ATTmp_double;
                        &ArtBaseName&ArtIterator_Word_Lag1=&ArtBaseName&ArtIterator_Word_Lag1
                                +(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )))-ATTmp_double);
                        %do ArtII=%eval(&ArtIterator_Word_Lag1-1) %to 1 %by -1;
                            %let ArtIIa=%eval(&ArtII);
                            %let ArtIIaP1=%eval(&ArtIIa+1);
                            ATTmp_double=((%qscan(&CriticalValues,&ArtIIaP1,%str( )))-(%qscan(&CriticalValues,&ArtIIa,%str( ))))/2.0;
                            &ArtBaseName&ArtIIaP1=&ArtBaseName&ArtIIaP1+ATTmp_double;
                            &ArtBaseName&ArtIIa=&ArtBaseName&ArtIIa+ATTmp_double;
                        %end;
                    end;
                %end;

            %end;
                    else do;
                        ATTmp_double=(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Last,%str( ))));
                        &ArtBaseName&ArtIterator_Word_Last=&ArtBaseName&ArtIterator_Word_Last+ATTmp_double;
                        %do ArtII=%eval(&ArtIterator_Word_Last-1) %to 1 %by -1;
                            %let ArtIIa=%eval(&ArtII);
                            %let ArtIIaP1=%eval(&ArtIIa+1);
                            ATTmp_double=((%qscan(&CriticalValues,&ArtIIaP1,%str( )))-(%qscan(&CriticalValues,&ArtIIa,%str( ))))/2.0;
                            &ArtBaseName&ArtIIaP1=&ArtBaseName&ArtIIaP1+ATTmp_double;
                            &ArtBaseName&ArtIIa=&ArtBaseName&ArtIIa+ATTmp_double;
                        %end;
                    end;
                    end;

            %let &MarginalSetName=%CrossProductWords(&ArtBaseName,&ArtIndexList);
            %if "%str(&DropList)" ne "" %then %do;
                %let &MarginalTrimmedSetName=%CrossProductWords(&ArtBaseName,%StripWords(&ArtIndexList,&DropList));
            %end; %else %do;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end;
            %put MarginalSetName=&MarginalSetName, &&&MarginalSetName;
            %put MarginalTrimmedSetName=&MarginalTrimmedSetName, &&&MarginalTrimmedSetName;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %put RunningMarginalSetName=&RunningMarginalSetName, &&&RunningMarginalSetName;
            %put RunningMarginalTrimmedSetName=&RunningMarginalTrimmedSetName, &&&RunningMarginalTrimmedSetName;
            %return;
        %end;

        %if (&Treatment eq BSplineOrder2) or (&Treatment eq BSplineOrder3) %then %do;

            ATTmp_double=0.0;

            %let ArtCVN=%WordCount(&CriticalValues);
            %if &Treatment eq BSplineOrder2 %then
                %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN-1));
            %else
                %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN-2));

            array &ArtBaseName.A %CrossProductWords(&ArtBaseName,&ArtIndexList);

            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                &ArtBaseName&ArtIterator_Word=0.0;
                %if &ArtIterator_Index eq 1 %then %do;
                    label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, MissingCode, Treatment=&Treatment";
                %end; %else %do;
                    %if &ArtIterator_Index eq &ArtIterator_Count %then %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, Last, Treatment=&Treatment";
                    %end; %else %do;
                        label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, Treatment=&Treatment";
                    %end;
                %end; 
            %end;

            ATTmp_i=-1;

            if &SourceVariable eq . then &ArtBaseName.0=1.0;
            %if "%str(&CleanLimits)" ne "" %then %do;
                else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then &ArtBaseName.0=1.0;
                %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then &ArtBaseName.0=1.0;
                %end;
            %end;
            else if &SourceVariable le %qscan(&CriticalValues,1,%str( )) then 
                &ArtBaseName.1=1.0;
            else if &SourceVariable ge %qscan(&CriticalValues,&ArtCVN,%str( )) then 
                &ArtBaseName&ArtIterator_Word_Last=1.0;
            %do ArtI=%eval(&ArtCVN-1) %to 1 %by -1;
            else if &SourceVariable ge %qscan(&CriticalValues,&ArtI,%str( )) then 
                ATTmp_i=&ArtI;
            %end;

            /* See the corresponding code in WDS-VBA or WDS-Lua, the code was adapted to SAS below. */
            if ATTmp_i gt 0 then do;

                    array &ArtBaseName._CVs &ArtBaseName._Tmp_CV1-&ArtBaseName._Tmp_CV&ArtCVN;
                    drop &ArtBaseName._Tmp_CV1-&ArtBaseName._Tmp_CV&ArtCVN;
                    array &ArtBaseName._dCVs &ArtBaseName._Tmp_dCV1-&ArtBaseName._Tmp_dCV&ArtCVN;
                    drop &ArtBaseName._Tmp_dCV1-&ArtBaseName._Tmp_dCV&ArtCVN;
                    array &ArtBaseName._d2CVs &ArtBaseName._Tmp_d2CV1-&ArtBaseName._Tmp_d2CV&ArtCVN;
                    drop &ArtBaseName._Tmp_d2CV1-&ArtBaseName._Tmp_d2CV&ArtCVN;
                    array &ArtBaseName._d3CVs &ArtBaseName._Tmp_d3CV1-&ArtBaseName._Tmp_d3CV&ArtCVN;
                    drop &ArtBaseName._Tmp_d3CV1-&ArtBaseName._Tmp_d3CV&ArtCVN;
                    %do ArtI=1 %to &ArtCVN;
                        &ArtBaseName._Tmp_CV&ArtI=(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;
                    %do ArtI=1 %to %eval(&ArtCVN-1);
                        &ArtBaseName._Tmp_dCV&ArtI=(%qscan(&CriticalValues,%eval(&ArtI+1),%str( )))-(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;
                    %do ArtI=1 %to %eval(&ArtCVN-2);
                        &ArtBaseName._Tmp_d2CV&ArtI=(%qscan(&CriticalValues,%eval(&ArtI+2),%str( )))-(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;
                    %do ArtI=1 %to %eval(&ArtCVN-3);
                        &ArtBaseName._Tmp_d3CV&ArtI=(%qscan(&CriticalValues,%eval(&ArtI+3),%str( )))-(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;

                    ATTmp_iM1 = ATTmp_i - 1;
                    ATTmp_iM2 = ATTmp_i - 2;
                    ATTmp_ia = ATTmp_i + 2;
                    ATTmp_iaM1 = ATTmp_ia - 1;
                    ATTmp_iaM2 = ATTmp_ia - 2;
                    ATTmp_iaM3 = ATTmp_ia - 3;
                    
                    ATTmp_xMci = (&SourceVariable - &ArtBaseName._CVs{ATTmp_i});
                    ATTmp_xMciM1 = 0;
                    ATTmp_xMciM2 = 0;
                
                    If ATTmp_i gt 1 Then
                        ATTmp_xMciM1 = (&SourceVariable - &ArtBaseName._CVs{ATTmp_iM1});
                    If ATTmp_i gt 2 Then
                        ATTmp_xMciM2 = (&SourceVariable - &ArtBaseName._CVs{ATTmp_iM2});
                    
                    ATTmp_fo0 = 0.0;
                    ATTmp_fo1 = 0.0;
                    ATTmp_fo2 = 0.0;
                    ATTmp_fo3 = 0.0;
                    
                    %if &Treatment eq BSplineOrder2 %then %do;

                         If ATTmp_i lt &ArtCVN - 1 Then
                             ATTmp_fo0 = ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i} * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i};
                         If ATTmp_i eq 1 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo0;
                         Else If ATTmp_i lt &ArtCVN - 1 Then
                             ATTmp_fo1 = ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1} * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}) + (1.0 - ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i}) * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i};
                         If ATTmp_i eq 2 Then
                             ATTmp_fo2 = 1.0 - ATTmp_fo0 - ATTmp_fo1;
                         Else If ATTmp_i gt 2 Then
                             ATTmp_fo2 = (1.0 - ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1}) * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i});
                         If ATTmp_i eq &ArtCVN - 1 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo2;
                         

                         If ATTmp_ia lt &ArtIterator_Count Then
                             &ArtBaseName.A{ATTmp_ia}=ATTmp_fo0;
                         Else
                             &ArtBaseName.A{&ArtIterator_Count}=ATTmp_fo0;
                         
                         If ATTmp_iaM1 gt 1 Then do;
                             If ATTmp_iaM1 lt &ArtIterator_Count Then
                                 &ArtBaseName.A{ATTmp_iaM1}=ATTmp_fo1;
                             Else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo1;
                         end;
                         
                         If ATTmp_iaM2 gt 1 Then
                             &ArtBaseName.A{ATTmp_iaM2}=&ArtBaseName.A{ATTmp_iaM2}+ATTmp_fo2;

                    %end; %else %do;


                         If ATTmp_i lt &ArtCVN - 2 Then
                             ATTmp_fo0 = ATTmp_xMci / &ArtBaseName._d3CVs{ATTmp_i} * 
                                         ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i} * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i};
                         If ATTmp_i eq 1 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo0;
                         Else If ATTmp_i lt &ArtCVN - 2 Then
                             ATTmp_fo1 = ATTmp_xMciM1 / &ArtBaseName._d3CVs{ATTmp_iM1} * 
                                          ( ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1} * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}) 
                                            + (1.0 - ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i}) * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i} )
                                         + (1.0 - ATTmp_xMci / &ArtBaseName._d3CVs{ATTmp_i}) * (ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i} * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i})
                                       ;
                         If ATTmp_i eq 2 Then
                             ATTmp_fo2 = 1.0 - ATTmp_fo0 - ATTmp_fo1;
                         Else If (ATTmp_i gt 2) and (ATTmp_i lt &ArtCVN-1) Then
                             ATTmp_fo2 = (ATTmp_xMciM2 / &ArtBaseName._d3CVs{ATTmp_iM2}) *((1.0 - ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1}) * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}))
                                        + (1.0 - ATTmp_xMciM1 / &ArtBaseName._d3CVs{ATTmp_iM1}) * (ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1} * (1 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}) 
                                                         + (1 - ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i}) * (ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}))
                                       ;
                         If ATTmp_i eq 3 Then
                             ATTmp_fo3 = 1.0 - ATTmp_fo0 - ATTmp_fo1 - ATTmp_fo2;
                         Else If (ATTmp_i gt 3)  Then
                             ATTmp_fo3 = (1.0 - ATTmp_xMciM2 / &ArtBaseName._d3CVs{ATTmp_iM2}) * (1.0 - ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1}) * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i});

                         If ATTmp_i eq &ArtCVN - 2 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo2 - ATTmp_fo3;
                         If ATTmp_i eq &ArtCVN - 1 Then
                             ATTmp_fo2 = 1.0 - ATTmp_fo3;
                         

                         If ATTmp_ia lt &ArtIterator_Count Then
                             &ArtBaseName.A{ATTmp_ia}=ATTmp_fo0;
                         Else
                             &ArtBaseName.A{&ArtIterator_Count}=ATTmp_fo0;
                         
                         If ATTmp_iaM1 gt 1 Then do;
                             If ATTmp_iaM1 lt &ArtIterator_Count Then
                                 &ArtBaseName.A{ATTmp_iaM1}=ATTmp_fo1;
                             Else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo1;
                         end;
                         
                         If ATTmp_iaM2 gt 1 Then do;
                             If ATTmp_iaM2 lt &ArtIterator_Count then
                                 &ArtBaseName.A{ATTmp_iaM2}=ATTmp_fo2;
                             else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo2;
                         end;

                         If ATTmp_iaM3 gt 1 Then do;
                             If ATTmp_iaM3 lt &ArtIterator_Count then
                                 &ArtBaseName.A{ATTmp_iaM3}=ATTmp_fo3;
                             else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo3;
                         end;

                    %end;
                end;
                    

            %let &MarginalSetName=%CrossProductWords(&ArtBaseName,&ArtIndexList);
            %if "%str(&DropList)" ne "" %then %do;
                %let &MarginalTrimmedSetName=%CrossProductWords(&ArtBaseName,%StripWords(&ArtIndexList,&DropList));
            %end; %else %do;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end;
            %put MarginalSetName=&MarginalSetName, &&&MarginalSetName;
            %put MarginalTrimmedSetName=&MarginalTrimmedSetName, &&&MarginalTrimmedSetName;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %put RunningMarginalSetName=&RunningMarginalSetName, &&&RunningMarginalSetName;
            %put RunningMarginalTrimmedSetName=&RunningMarginalTrimmedSetName, &&&RunningMarginalTrimmedSetName;
            %return;
        %end;

        %if (&Treatment eq Categorical) or (&Treatment eq CategoricalNumeric) %then %do;
            %let ArtCVN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN+1));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                &ArtBaseName&ArtIterator_Word=0.0;
                %if &ArtIterator_Index eq 1 %then %do;
                    label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, Missing or Other, Treatment=&Treatment";
                %end; %else %do;
                    label &ArtBaseName.&ArtIterator_Word="Art &ArtIterator_Word for &SourceVariable, (%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))), Treatment=&Treatment";
                %end;
            %end;
            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Word eq 0 %then %do;
                    %if &Treatment eq Categorical %then %do;
                        if trim(left(&SourceVariable)) eq "" then &ArtBaseName.0=1.0;
                    %end; %else %do;
                        if &SourceVariable eq . then &ArtBaseName.0=1.0;
                    %end;
                %end; %else %do;
                    %IteratorInit(ArtSubIterator,%qscan(&CriticalValues,&ArtIterator_Word,%str( )),dlm=|)
                    %do %while(%IteratingOver(ArtSubIterator));
                        %if &Treatment eq Categorical %then %do;
                            else if &SourceVariable eq "&ArtSubIterator_Word" then &ArtBaseName&ArtIterator_Word=1.0;
                        %end; %else %do;
                            else if abs(&SourceVariable - (&ArtSubIterator_Word)) lt &eps then &ArtBaseName&ArtIterator_Word=1.0;
                        %end;
                    %end;
                %end;
            %end;
            else &ArtBaseName.0=1.0;

            %let &MarginalSetName=%CrossProductWords(&ArtBaseName,&ArtIndexList);
            %if "%str(&DropList)" ne "" %then %do;
                %let &MarginalTrimmedSetName=%CrossProductWords(&ArtBaseName,%StripWords(&ArtIndexList,&DropList));
            %end; %else %do;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end;
            %put MarginalSetName=&MarginalSetName, &&&MarginalSetName;
            %put MarginalTrimmedSetName=&MarginalTrimmedSetName, &&&MarginalTrimmedSetName;
            %let &RunningMarginalSetName=&&&RunningMarginalSetName &&&MarginalSetName;
            %let &RunningMarginalTrimmedSetName=&&&RunningMarginalTrimmedSetName &&&MarginalTrimmedSetName;
            %put RunningMarginalSetName=&RunningMarginalSetName, &&&RunningMarginalSetName;
            %put RunningMarginalTrimmedSetName=&RunningMarginalTrimmedSetName, &&&RunningMarginalTrimmedSetName;
            %return;
        %end;

        %mend;


%macro ArtificialTreatmentScored(SourceVariable=SourceVariable
        , TargetBase=
        , Treatment=Hats
        , CriticalValues=
        , CleanLimits=
        , ScoreCount=1
        , Coefficients=
        , eps=0.00000001
        );

        if _N_ eq 1 then
        put "starting code generation associated with ArtificialTreatment(&SourceVariable,&Treatment,&TargetBase)";

        drop ATTmp_i ATTmp_iM1 ATTmp_iM2 ATTmp_ia ATTmp_iaM1 ATTmp_iaM2 ATTmp_iaM3
            ATTmp_xMci ATTmp_xMciM1 ATTmp_xMciM2
            ATTmp_fo0 ATTmp_fo1 ATTmp_fo2 ATTmp_fo3
            ATTmp_double 
            ;

        %local ArtIndexList ArtTake ArtI ArtII ArtIIa ArtIIaP1 ArtCVN ArtN ArtBaseName ArtTempName ArtComp;

        %let Treatment=%CleanTreatment(&Treatment);

        %do ArtI=1 %to &ScoreCount;
            &TargetBase.&ArtI=0.0;
            label &TargetBase.&ArtI="Score &ArtI for SourceVariable=&SourceVariable, Treatment=&Treatment";
        %end;

        %if &Treatment eq None %then %do;

            %do ArtI=1 %to &ScoreCount;
                &TargetBase.&ArtI=(&SourceVariable)*(%qscan(&Coefficients,&ArtI,%str( )));
            %end;

            %return;

        %end;

        %if &Treatment eq Constant %then %do;
            %do ArtI=1 %to &ScoreCount;
                &TargetBase.&ArtI=(%qscan(&CriticalValues,1,%str( )))*(%qscan(&Coefficients,&ArtI,%str( )));
            %end;

            %return;

        %end;

        %if &Treatment eq CodedMissings %then %do;

            %if %str(&DropList) eq %then %do;
                %let ArtTake=1;
                %let &MarginalSetName=&ArtBaseName.0 &ArtBaseName.1;
                %let &MarginalTrimmedSetName=&&&MarginalSetName;
            %end; %else %if %str(&DropList) eq 0 %then %do;
                %let ArtTake=1;
                %let &MarginalSetName=&ArtBaseName.0 &ArtBaseName.1;
                %let &MarginalTrimmedSetName=&ArtBaseName.1;
            %end; %else %if %str(&DropList) eq 1 %then %do;
                %let ArtTake=1;
                %let &MarginalSetName=&ArtBaseName.0 &ArtBaseName.1;
                %let &MarginalTrimmedSetName=&ArtBaseName.0;
            %end; %else %do; 
                %let ArtTake=0;
            %end;
            %if &ArtTake %then %do;
                if &SourceVariable eq . then do;
                    %do ArtI=1 %to &ScoreCount;
                        &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(2*(&ArtI-1)+1),%str( )));
                    %end;
                %if %str(&CleanLimits) ne %then %do;
                end; else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then do;
                    %do ArtI=1 %to &ScoreCount;
                        &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(2*(&ArtI-1)+1),%str( )));
                    %end;
                %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                end; else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then do;
                    %do ArtI=1 %to &ScoreCount;
                        &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(2*(&ArtI-1)+1),%str( )));
                    %end;
                %end;
                %end;
                end; else do;
                    %do ArtI=1 %to &ScoreCount;
                        &TargetBase.&ArtI=(&SourceVariable)*(%qscan(&Coefficients,%eval(2*(&ArtI-1)+1),%str( )));
                    %end;
                end;
            %end;
            %return;

        %end;

        %if (&Treatment eq Discrete) or (&Treatment eq DiscreteLC) %then %do;
            %if &Treatment eq DiscreteLC %then 
                %let ArtComp= le (&eps)+ ; 
            %else %let ArtComp= lt (-&eps)+ ;
            %let ArtCVN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN+1));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Index eq 1 %then %do;
                    if &SourceVariable eq . then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                        %end;
                    end;
                    %if "%str(&CleanLimits)" ne "" %then %do;
                    else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                        %end;
                    end;
                    %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                        %end;
                    end;
                    %end;
                    %end;
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    else if &SourceVariable &ArtComp %qscan(&CriticalValues,&ArtIterator_Index_Lag1,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )));
                        %end;
                    end;
                %end; %else %if &ArtIterator_Index eq &ArtIterator_Count %then %do;
                    else do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )));
                        %end;
                    end;
                %end; %else %do;
                    else if &SourceVariable &ArtComp %qscan(&CriticalValues,&ArtIterator_Index_Lag1,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )));
                        %end;
                    end;
                %end;
            %end;
            %return;
        %end;

        %if &Treatment eq Hats %then %do;
            %let ArtCVN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Index eq 1 %then %do;
                    if &SourceVariable eq . then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                        %end;
                    end;
                    %if "%str(&CleanLimits)" ne "" %then %do;
                    else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                        %end;
                    end;
                    %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                        %end;
                    end;
                    %end;
                    %end;
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    else if &SourceVariable le %qscan(&CriticalValues,1,%str( )) then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+2),%str( )));
                        %end;
                    end;
                %end; %else %do;
                    else if &SourceVariable le %qscan(&CriticalValues,&ArtIterator_Word,%str( )) then do;
                        &TargetBase._ScoreTemp&ArtIterator_Word=(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )))) 
                                / ((%qscan(&CriticalValues,&ArtIterator_Word,%str( )))-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))));
                        drop &TargetBase._ScoreTemp&ArtIterator_Word;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )))*&TargetBase._ScoreTemp&ArtIterator_Word
                                        +(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index-1),%str( )))*(1.0-&TargetBase._ScoreTemp&ArtIterator_Word);
                        %end;
                    end;
                %end;
            %end;
                    else do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Count),%str( )));
                        %end;
                    end;
            %return;
        %end;

        %if &Treatment eq iHats %then %do;
            ATTmp_double=0.0;
            drop ATTmp_double;
            %let ArtCVN=%WordCount(&CriticalValues);
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;

            array &ArtBaseName.A %CrossProductWords(&ArtBaseName._ScoreTemp,&ArtIndexList);
            drop %CrossProductWords(&ArtBaseName._ScoreTemp,&ArtIndexList);

            %do %while(%IteratingOver(ArtIterator));
                &ArtBaseName._ScoreTemp&ArtIterator_Word=0.0;
            %end;

            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Index eq 1 %then %do;
                    if &SourceVariable eq . then &ArtBaseName.A{&ArtIterator_Index}=1.0;
                    %if "%str(&CleanLimits)" ne "" %then %do;
                    else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then &ArtBaseName.A{&ArtIterator_Index}=1.0;
                    %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then &ArtBaseName.A{&ArtIterator_Index}=1.0;
                    %end;
                    %end;
                %end; %else %if &ArtIterator_Index eq 2 %then %do;
                    else do;

                    if &SourceVariable le %qscan(&CriticalValues,1,%str( )) then 
                        &ArtBaseName.A{&ArtIterator_Index}=(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word,%str( ))));

                %end; %else %do;
                    else if &SourceVariable le %qscan(&CriticalValues,&ArtIterator_Word,%str( )) then do;
                        ATTmp_double=((&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))))**(2.0)) 
                                / ((%qscan(&CriticalValues,&ArtIterator_Word,%str( )))-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( ))))
                                / 2.0;
                        &ArtBaseName.A{&ArtIterator_Index}=&ArtBaseName.A{&ArtIterator_Index}+ATTmp_double;
                        &ArtBaseName.A{&ArtIterator_Index-1}=&ArtBaseName.A{&ArtIterator_Index-1}
                                +(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Lag1,%str( )))-ATTmp_double);
                        %do ArtII=%eval(&ArtIterator_Word_Lag1-1) %to 1 %by -1;
                            %let ArtIIa=%eval(&ArtII);
                            %let ArtIIaP1=%eval(&ArtIIa+1);
                            ATTmp_double=((%qscan(&CriticalValues,&ArtIIaP1,%str( )))-(%qscan(&CriticalValues,&ArtIIa,%str( ))))/2.0;
                            &ArtBaseName.A{&ArtIIaP1+1}=&ArtBaseName.A{&ArtIIaP1+1}+ATTmp_double;
                            &ArtBaseName.A{&ArtIIa+1}=&ArtBaseName.A{&ArtIIa+1}+ATTmp_double;
                        %end;
                    end;
                %end;

            %end;
                    else do;
                        ATTmp_double=(&SourceVariable-(%qscan(&CriticalValues,&ArtIterator_Word_Last,%str( ))));
                        &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_double;
                        %do ArtII=%eval(&ArtIterator_Word_Last-1) %to 1 %by -1;
                            %let ArtIIa=%eval(&ArtII);
                            %let ArtIIaP1=%eval(&ArtIIa+1);
                            ATTmp_double=((%qscan(&CriticalValues,&ArtIIaP1,%str( )))-(%qscan(&CriticalValues,&ArtIIa,%str( ))))/2.0;
                            &ArtBaseName.A{&ArtIIaP1+1}=&ArtBaseName.A{&ArtIIaP1+1}+ATTmp_double;
                            &ArtBaseName.A{&ArtIIa+1}=&ArtBaseName.A{&ArtIIa+1}+ATTmp_double;
                        %end;
                    end;
                    end;

                %do ArtII=1 %to &ArtIterator_Count;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=&TargetBase.&ArtI+&ArtBaseName.A{&ArtII}*(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtII),%str( )));
                        %end;
                %end;
                    
            %return;
        %end;

        %if (&Treatment eq BSplineOrder2) or (&Treatment eq BSplineOrder3) %then %do;

            ATTmp_double=0.0;

            %let ArtCVN=%WordCount(&CriticalValues);
            %if &Treatment eq BSplineOrder2 %then
                %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN-1));
            %else
                %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN-2));

            %local ArtBaseName;
            %let ArtBaseName=&TargetBase;
            array &ArtBaseName.A %CrossProductWords(&ArtBaseName._ScoreTemp,&ArtIndexList);
            drop %CrossProductWords(&ArtBaseName._ScoreTemp,&ArtIndexList);

            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do ArtI=1 %to &ArtN;
                &ArtBaseName.A{&ArtI}=0.0;
            %end;

            ATTmp_i=-1;

            if &SourceVariable eq . then &ArtBaseName.A{1}=1.0;
            %if "%str(&CleanLimits)" ne "" %then %do;
                else if &SourceVariable lt %scan(&CleanLimits,1,%str( )) then &ArtBaseName.A{1}=1.0;
                %if %qscan(&CleanLimits,2,%str( )) ne %then %do;
                    else if &SourceVariable gt %scan(&CleanLimits,2,%str( )) then &ArtBaseName.A{1}=1.0;
                %end;
            %end;
            else if &SourceVariable le %qscan(&CriticalValues,1,%str( )) then 
                &ArtBaseName.A{2}=1.0;
            else if &SourceVariable ge %qscan(&CriticalValues,&ArtCVN,%str( )) then 
                &ArtBaseName.A{&ArtN}=1.0;
            %do ArtI=%eval(&ArtCVN-1) %to 1 %by -1;
            else if &SourceVariable ge %qscan(&CriticalValues,&ArtI,%str( )) then 
                ATTmp_i=&ArtI;
            %end;

            /* See the corresponding code in WDS-VBA or WDS-Lua, the code was adapted to SAS below. */
            if ATTmp_i gt 0 then do;

                    array &ArtBaseName._CVs &ArtBaseName._Tmp_CV1-&ArtBaseName._Tmp_CV&ArtCVN;
                    drop &ArtBaseName._Tmp_CV1-&ArtBaseName._Tmp_CV&ArtCVN;
                    array &ArtBaseName._dCVs &ArtBaseName._Tmp_dCV1-&ArtBaseName._Tmp_dCV&ArtCVN;
                    drop &ArtBaseName._Tmp_dCV1-&ArtBaseName._Tmp_dCV&ArtCVN;
                    array &ArtBaseName._d2CVs &ArtBaseName._Tmp_d2CV1-&ArtBaseName._Tmp_d2CV&ArtCVN;
                    drop &ArtBaseName._Tmp_d2CV1-&ArtBaseName._Tmp_d2CV&ArtCVN;
                    array &ArtBaseName._d3CVs &ArtBaseName._Tmp_d3CV1-&ArtBaseName._Tmp_d3CV&ArtCVN;
                    drop &ArtBaseName._Tmp_d3CV1-&ArtBaseName._Tmp_d3CV&ArtCVN;
                    %do ArtI=1 %to &ArtCVN;
                        &ArtBaseName._Tmp_CV&ArtI=(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;
                    %do ArtI=1 %to %eval(&ArtCVN-1);
                        &ArtBaseName._Tmp_dCV&ArtI=(%qscan(&CriticalValues,%eval(&ArtI+1),%str( )))-(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;
                    %do ArtI=1 %to %eval(&ArtCVN-2);
                        &ArtBaseName._Tmp_d2CV&ArtI=(%qscan(&CriticalValues,%eval(&ArtI+2),%str( )))-(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;
                    %do ArtI=1 %to %eval(&ArtCVN-3);
                        &ArtBaseName._Tmp_d3CV&ArtI=(%qscan(&CriticalValues,%eval(&ArtI+3),%str( )))-(%qscan(&CriticalValues,&ArtI,%str( )));
                    %end;

                    ATTmp_iM1 = ATTmp_i - 1;
                    ATTmp_iM2 = ATTmp_i - 2;
                    ATTmp_ia = ATTmp_i + 2;
                    ATTmp_iaM1 = ATTmp_ia - 1;
                    ATTmp_iaM2 = ATTmp_ia - 2;
                    ATTmp_iaM3 = ATTmp_ia - 3;
                    
                    ATTmp_xMci = (&SourceVariable - &ArtBaseName._CVs{ATTmp_i});
                    ATTmp_xMciM1 = 0;
                    ATTmp_xMciM2 = 0;
                
                    If ATTmp_i gt 1 Then
                        ATTmp_xMciM1 = (&SourceVariable - &ArtBaseName._CVs{ATTmp_iM1});
                    If ATTmp_i gt 2 Then
                        ATTmp_xMciM2 = (&SourceVariable - &ArtBaseName._CVs{ATTmp_iM2});
                    
                    ATTmp_fo0 = 0.0;
                    ATTmp_fo1 = 0.0;
                    ATTmp_fo2 = 0.0;
                    ATTmp_fo3 = 0.0;
                    
                    %if &Treatment eq BSplineOrder2 %then %do;

                         If ATTmp_i lt &ArtCVN - 1 Then
                             ATTmp_fo0 = ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i} * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i};
                         If ATTmp_i eq 1 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo0;
                         Else If ATTmp_i lt &ArtCVN - 1 Then
                             ATTmp_fo1 = ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1} * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}) + (1.0 - ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i}) * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i};
                         If ATTmp_i eq 2 Then
                             ATTmp_fo2 = 1.0 - ATTmp_fo0 - ATTmp_fo1;
                         Else If ATTmp_i gt 2 Then
                             ATTmp_fo2 = (1.0 - ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1}) * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i});
                         If ATTmp_i eq &ArtCVN - 1 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo2;
                         

                         If ATTmp_ia lt &ArtIterator_Count Then
                             &ArtBaseName.A{ATTmp_ia}=ATTmp_fo0;
                         Else
                             &ArtBaseName.A{&ArtIterator_Count}=ATTmp_fo0;
                         
                         If ATTmp_iaM1 gt 1 Then do;
                             If ATTmp_iaM1 lt &ArtIterator_Count Then
                                 &ArtBaseName.A{ATTmp_iaM1}=ATTmp_fo1;
                             Else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo1;
                         end;
                         
                         If ATTmp_iaM2 gt 1 Then
                             &ArtBaseName.A{ATTmp_iaM2}=&ArtBaseName.A{ATTmp_iaM2}+ATTmp_fo2;

                    %end; %else %do;


                         If ATTmp_i lt &ArtCVN - 2 Then
                             ATTmp_fo0 = ATTmp_xMci / &ArtBaseName._d3CVs{ATTmp_i} * 
                                         ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i} * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i};
                         If ATTmp_i eq 1 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo0;
                         Else If ATTmp_i lt &ArtCVN - 2 Then
                             ATTmp_fo1 = ATTmp_xMciM1 / &ArtBaseName._d3CVs{ATTmp_iM1} * 
                                          ( ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1} * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}) 
                                            + (1.0 - ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i}) * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i} )
                                         + (1.0 - ATTmp_xMci / &ArtBaseName._d3CVs{ATTmp_i}) * (ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i} * ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i})
                                       ;
                         If ATTmp_i eq 2 Then
                             ATTmp_fo2 = 1.0 - ATTmp_fo0 - ATTmp_fo1;
                         Else If (ATTmp_i gt 2) and (ATTmp_i lt &ArtCVN-1) Then
                             ATTmp_fo2 = (ATTmp_xMciM2 / &ArtBaseName._d3CVs{ATTmp_iM2}) *((1.0 - ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1}) * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}))
                                        + (1.0 - ATTmp_xMciM1 / &ArtBaseName._d3CVs{ATTmp_iM1}) * (ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1} * (1 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}) 
                                                         + (1 - ATTmp_xMci / &ArtBaseName._d2CVs{ATTmp_i}) * (ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i}))
                                       ;
                         If ATTmp_i eq 3 Then
                             ATTmp_fo3 = 1.0 - ATTmp_fo0 - ATTmp_fo1 - ATTmp_fo2;
                         Else If (ATTmp_i gt 3)  Then
                             ATTmp_fo3 = (1.0 - ATTmp_xMciM2 / &ArtBaseName._d3CVs{ATTmp_iM2}) * (1.0 - ATTmp_xMciM1 / &ArtBaseName._d2CVs{ATTmp_iM1}) * (1.0 - ATTmp_xMci / &ArtBaseName._dCVs{ATTmp_i});

                         If ATTmp_i eq &ArtCVN - 2 Then
                             ATTmp_fo1 = 1.0 - ATTmp_fo2 - ATTmp_fo3;
                         If ATTmp_i eq &ArtCVN - 1 Then
                             ATTmp_fo2 = 1.0 - ATTmp_fo3;
                         

                         If ATTmp_ia lt &ArtIterator_Count Then
                             &ArtBaseName.A{ATTmp_ia}=ATTmp_fo0;
                         Else
                             &ArtBaseName.A{&ArtIterator_Count}=ATTmp_fo0;
                         
                         If ATTmp_iaM1 gt 1 Then do;
                             If ATTmp_iaM1 lt &ArtIterator_Count Then
                                 &ArtBaseName.A{ATTmp_iaM1}=ATTmp_fo1;
                             Else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo1;
                         end;
                         
                         If ATTmp_iaM2 gt 1 Then do;
                             If ATTmp_iaM2 lt &ArtIterator_Count then
                                 &ArtBaseName.A{ATTmp_iaM2}=ATTmp_fo2;
                             else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo2;
                         end;

                         If ATTmp_iaM3 gt 1 Then do;
                             If ATTmp_iaM3 lt &ArtIterator_Count then
                                 &ArtBaseName.A{ATTmp_iaM3}=ATTmp_fo3;
                             else
                                 &ArtBaseName.A{&ArtIterator_Count}=&ArtBaseName.A{&ArtIterator_Count}+ATTmp_fo3;
                         end;

                    %end;
                end;

                
                %do ArtII=1 %to &ArtIterator_Count;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=&TargetBase.&ArtI+&ArtBaseName.A{&ArtII}*(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtII),%str( )));
                        %end;
                %end;
                    
            %return;
        %end;

        %if (&Treatment eq Categorical) or (&Treatment eq CategoricalNumeric) %then %do;
            %let ArtCVN=%WordCount(&CriticalValues,dlm=%str( ));
            %let ArtIndexList=%range(start=0,stop=%eval(&ArtCVN));
            %IteratorInit(ArtIterator,&ArtIndexList)
            %let ArtN=&ArtIterator_Count;
            %do %while(%IteratingOver(ArtIterator));
                %if &ArtIterator_Word eq 0 %then %do;
                    %if &Treatment eq Categorical %then %do;
                        if trim(left(&SourceVariable)) eq "" then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )));
                        %end;
                        end;
                    %end; %else %do;
                        if &SourceVariable eq . then do;
                        %do ArtI=1 %to &ScoreCount;
                            &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )));
                        %end;
                        end;
                    %end;
                %end; %else %do;
                    %IteratorInit(ArtSubIterator,%qscan(&CriticalValues,&ArtIterator_Word,%str( )),dlm=|)
                    %do %while(%IteratingOver(ArtSubIterator));
                        %if &Treatment eq Categorical %then %do;
                            else if &SourceVariable eq "&ArtSubIterator_Word" then do;
                        %end; %else %do;
                            else if abs(&SourceVariable - (&ArtSubIterator_Word)) lt &eps then do;
                        %end;
                            %do ArtI=1 %to &ScoreCount;
                                &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+&ArtIterator_Index),%str( )));
                            %end;
                            end;
                    %end;
                %end;
            %end;
            else do;
                            %do ArtI=1 %to &ScoreCount;
                                &TargetBase.&ArtI=(%qscan(&Coefficients,%eval(&ArtN*(&ArtI-1)+1),%str( )));
                            %end;
                            end;

            %return;
        %end;

        %mend;

%put "for testing code of ArtificialTreatments.sas, see zzzExamples/Tests.sas";

