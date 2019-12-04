%LoadMacros(wds.range wds.Iterator wds.CrossProductWords wds.StripWords);

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
