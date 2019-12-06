%LoadMacros(wds.range wds.Iterator wds.CrossProductWords wds.StripWords);

options mprint;

%let x=%range(start=0,stop=20);

%IteratorInit(IterX,&x);

data temp;
	%do %while (%IteratingOver(IterX));
		i=&IterX_Index;
		x=&IterX_Word;
		output;
	%end;
run;

proc print data=temp; run;

%let x=a b c hey what the heck;
%let y=b the huh;
%let z=%StripWords(&x, &y);

%put x=&x;
%put y=&y;
%put z=&z;

%let w=%CrossProductWords(&x, &y);
%put w=&w;

%let w=%CrossProductWords(&x, &y, a b , joinchar=-);
%put w=&w;

%let w=%CrossProductWords(X,%StripWords(%range(start=0,stop=10), 3 9));
%put w=&w;


%IteratorRangeInit(IterY,start=-100,stop=100,step=1);
data temp;
	%do %while (%IteratingOver(IterY));
		i=&IterY_Index;
		y=(&IterY_Word)/10.0;
		length W $4.;
		if ranuni(-1)< .01 then W="Hey";
		else if ranuni(-1)< .3 then W="What";
		else if ranuni(-1)< .1 then W="The";
		else if ranuni(-1)< .1 then W="Heck";
		else W="Huh";
		output;
	%end;
run;

proc print data=temp; run;

%include "&wds.%str(\)StripWords.sas";
%include "&wds.%str(\)CrossProductWords.sas";
%include "&wds.%str(\)Iterator.sas";
%include "&wds.%str(\)..%str(\)ModelSpec%str(\)ArtificialTreatments.sas";

%let RunningTotalList=;
%let RunningKeepList=;

data temp;
	set temp;
	%ArtificialTreatment(SourceVariable=Y
		, AlternateBaseName=YNone
		, Treatment=None
		, MarginalSetName=YNoneMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
		, AlternateBaseName=YConst
		, Treatment=Constant
		, CriticalValues=7.2
		, MarginalSetName=YConstMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
	    , AlternateBaseName=YDisc
		, Treatment=Discrete
		, CriticalValues=-4.73 3 8
		, CleanLimits=-100 9.4
		, DropList=1 2
		, MarginalSetName=YDiscMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
		, Treatment=Hats
		, AlternateBaseName=YHats
		, CriticalValues=-4.73 3 8
		, CleanLimits=-100 9.4
		, DropList=1 2
		, MarginalSetName=YHatsMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
		, Treatment=iHats
		, AlternateBaseName=YiHats
		, CriticalValues=-4.73 3 8
		, CleanLimits=-100 9.4
		, DropList=1 2
		, MarginalSetName=YiHatsMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
		, Treatment=BZ2
		, AlternateBaseName=YBZ2
		, CriticalValues=-4.73 1 3 4 5 6
		, CleanLimits=-100 9.4
		, DropList=1 2
		, MarginalSetName=YBZ2Marginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
		, Treatment=BZ3
		, AlternateBaseName=YBZ3
		, CriticalValues=-4.73 1 3 4 5 6 
		, CleanLimits=-100 9.4
		, DropList=1 2
		, MarginalSetName=YBZ3Marginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=Y
		, Treatment=CategoricalNumeric
		, AlternateBaseName=YCN
		, CriticalValues=1|2|3 7|8|8.1|9  
		, CleanLimits=-100 9.4
		, MarginalSetName=YCNMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
	%ArtificialTreatment(SourceVariable=W
		, AlternateBaseName=WC
		, Treatment=Categorical
		, CriticalValues=Hey|The Huh  
		, MarginalSetName=WMarginals
		, RunningMarginalSetName=RunningTotalList
		, RunningMarginalTrimmedSetName=RunningKeepList
		);
run;

/* To test the "Scored" macro, each score is also scored "Long-Hand" with an enumerated calculation
using the artificials generated above. */

data temp;
	set temp;
	%ArtificialTreatmentScored(SourceVariable=Y
		, TargetBase=YNoneScore
		, Treatment=None
		, ScoreCount=2
		, Coefficients=1.2 4
		);
	YNoneScoreLH1=1.2*Y;
	YNoneScoreLH2=4*Y;
	YNoneScoreLH1_Delta=YNoneScoreLH1-YNoneScore1;
	YNoneScoreLH2_Delta=YNoneScoreLH2-YNoneScore2;
	
	%ArtificialTreatmentScored(SourceVariable=Y
		, TargetBase=YConstScore
		, Treatment=Constant
		, CriticalValues=7.2
		, ScoreCount=2
		, Coefficients=1.2 4
		);
	YConstScoreLH1=1.2*7.2;
	YConstScoreLH2=4*7.2;
	YConstScoreLH1_Delta=YConstScoreLH1-YConstScore1;
	YConstScoreLH2_Delta=YConstScoreLH2-YConstScore2;

	%ArtificialTreatmentScored(SourceVariable=Y
	    , TargetBase=YDiscScore
		, Treatment=Discrete
		, CriticalValues=-4.73 3 8
		, CleanLimits=-100 9.4
		, ScoreCount=2
		, Coefficients=-1 1 4 -2 3
						-2 2 1 3 -1
		);
	YDiscScoreLH1=(-1)*YDisc_0+1*YDisc_1+4*YDisc_2+(-2)*YDisc_3+3*YDisc_4;
	YDiscScoreLH2=(-2)*YDisc_0+2*YDisc_1+1*YDisc_2+3*YDisc_3+(-1)*YDisc_4;
	YDiscScoreLH1_Delta=YDiscScoreLH1-YDiscScore1;
	YDiscScoreLH2_Delta=YDiscScoreLH2-YDiscScore2;

	%ArtificialTreatmentScored(SourceVariable=Y
		, Treatment=Hats
		, TargetBase=YHatsScore
		, CriticalValues=-4.73 3 8
		, CleanLimits=-100 9.4
		, ScoreCount=2
		, Coefficients=-1 1 2 -1
						-2 4 -1 3
		);
	YHatsScoreLH1=(-1)*YHats_0+1*YHats_1+2*YHats_2+(-1)*YHats_3;
	YHatsScoreLH2=(-2)*YHats_0+4*YHats_1+(-1)*YHats_2+3*YHats_3;
	YHatsScoreLH1_Delta=YHatsScoreLH1-YHatsScore1;
	YHatsScoreLH2_Delta=YHatsScoreLH2-YHatsScore2;

	%ArtificialTreatmentScored(SourceVariable=Y
		, Treatment=iHats
		, TargetBase=YiHatsScore
		, CriticalValues=-4.73 3 8
		, CleanLimits=-100 9.4
		, ScoreCount=2
		, Coefficients=-1 1 4 3
						-2 3 1 2
		);
	YiHatsScoreLH1=(-1)*YiHats_0+1*YiHats_1+4*YiHats_2+3*YiHats_3;
	YiHatsScoreLH2=(-2)*YiHats_0+3*YiHats_1+1*YiHats_2+2*YiHats_3;
	YiHatsScoreLH1_Delta=YiHatsScoreLH1-YiHatsScore1;
	YiHatsScoreLH2_Delta=YiHatsScoreLH2-YiHatsScore2;

	%ArtificialTreatmentScored(SourceVariable=Y
		, Treatment=BZ2
		, TargetBase=YBZ2Score
		, CriticalValues=-4.73 1 3 4 5 6
		, CleanLimits=-100 9.4
		, ScoreCount=2
		, Coefficients=-1 4 -1 3 2 1
						-2 1 2 3 2 4
		);
	YBZ2ScoreLH1=(-1)*YBZ2_0+4*YBZ2_1+(-1)*YBZ2_2+3*YBZ2_3+2*YBZ2_4+1*YBZ2_5;
	YBZ2ScoreLH2=(-2)*YBZ2_0+1*YBZ2_1+2*YBZ2_2+3*YBZ2_3+2*YBZ2_4+4*YBZ2_5;
	YBZ2ScoreLH1_Delta=YBZ2ScoreLH1-YBZ2Score1;
	YBZ2ScoreLH2_Delta=YBZ2ScoreLH2-YBZ2Score2;

	%ArtificialTreatmentScored(SourceVariable=Y
		, Treatment=BZ3
		, TargetBase=YBZ3Score
		, CriticalValues=-4.73 1 3 4 5 6 
		, CleanLimits=-100 9.4
		, ScoreCount=2
		, Coefficients=-1 4 -1 3 2
						-2 1 2 3 2
		);
	YBZ3ScoreLH1=(-1)*YBZ3_0+4*YBZ3_1+(-1)*YBZ3_2+3*YBZ3_3+2*YBZ3_4;
	YBZ3ScoreLH2=(-2)*YBZ3_0+1*YBZ3_1+2*YBZ3_2+3*YBZ3_3+2*YBZ3_4;
	YBZ3ScoreLH1_Delta=YBZ3ScoreLH1-YBZ3Score1;
	YBZ3ScoreLH2_Delta=YBZ3ScoreLH2-YBZ3Score2;

	%ArtificialTreatmentScored(SourceVariable=Y
		, Treatment=CategoricalNumeric
		, TargetBase=YCNScore
		, CriticalValues=1|2|3 7|8|8.1|9
		, ScoreCount=2
		, Coefficients=-1 1 2
						-2 10 20
		);
	YCNScoreLH1=(-1)*YCN_0+1*YCN_1+2*YCN_2;
	YCNScoreLH2=(-2)*YCN_0+10*YCN_1+20*YCN_2;
	YCNScoreLH1_Delta=YCNScoreLH1-YCNScore1;
	YCNScoreLH2_Delta=YCNScoreLH2-YCNScore2;

	%ArtificialTreatmentScored(SourceVariable=W
		, Treatment=Categorical
		, TargetBase=WCScore
		, CriticalValues=Hey|The Huh  
		, ScoreCount=2
		, Coefficients=-1 1 2
						-2 10 20
		);
	WCScoreLH1=(-1)*WC_0+1*WC_1+2*WC_2;
	WCScoreLH2=(-2)*WC_0+10*WC_1+20*WC_2;
	WCScoreLH1_Delta=WCScoreLH1-WCScore1;
	WCScoreLH2_Delta=WCScoreLH2-WCScore2;


run;

proc contents data=temp;run;
proc print data=temp; run;

proc univariate data=temp;  
	var 
	YNoneScoreLH1_Delta
	YNoneScoreLH2_Delta
	YConstScoreLH1_Delta
	YConstScoreLH2_Delta
	YDiscScoreLH1_Delta
	YDiscScoreLH2_Delta
	YHatsScoreLH1_Delta
	YHatsScoreLH2_Delta
	YiHatsScoreLH1_Delta
	YiHatsScoreLH2_Delta
	YBZ2ScoreLH1_Delta
	YBZ2ScoreLH2_Delta
	YBZ3ScoreLH1_Delta
	YBZ3ScoreLH2_Delta
	YCNScoreLH1_Delta
	YCNScoreLH2_Delta
	WCScoreLH1_Delta
	WCScoreLH2_Delta
	;
run;

%macro temp;
%IteratorInit(Vars,&YDiscMarginals);
proc sgplot data=temp; 
	%do %while ( %IteratingOver(Vars) );
		series y=&Vars_Word x=Y; 
	%end;
run;
proc sgplot data=temp; 
	series y=YDiscScore1 x=Y;
	series y=YDiscScore2 x=Y;
run;
%IteratorInit(Vars,&YHatsMarginals);
proc sgplot data=temp; 
	%do %while ( %IteratingOver(Vars) );
		series y=&Vars_Word x=Y; 
	%end;
run;
proc sgplot data=temp; 
	series y=YHatsScore1 x=Y;
	series y=YHatsScore2 x=Y;
run;
%IteratorInit(Vars,&YiHatsMarginals);
proc sgplot data=temp; 
	%do %while ( %IteratingOver(Vars) );
		series y=&Vars_Word x=Y; 
	%end;
run;
proc sgplot data=temp; 
	series y=YiHatsScore1 x=Y;
	series y=YiHatsScore2 x=Y;
run;
%IteratorInit(Vars,&YBZ2Marginals);
proc sgplot data=temp; 
	%do %while ( %IteratingOver(Vars) );
		series y=&Vars_Word x=Y; 
	%end;
run;
proc sgplot data=temp; 
	series y=YBZ2Score1 x=Y;
	series y=YBZ2Score2 x=Y;
run;
%IteratorInit(Vars,&YBZ3Marginals);
proc sgplot data=temp; 
	%do %while ( %IteratingOver(Vars) );
		series y=&Vars_Word x=Y; 
	%end;
run;
proc sgplot data=temp; 
	series y=YBZ3Score1 x=Y;
	series y=YBZ3Score2 x=Y;
run;
%mend;
%temp;


%put RunningKeepList=&RunningKeepList;

proc print data=temp(keep=i y &RunningKeepList); run;




