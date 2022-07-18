# WDS-Python
Supporting Python module(s).

## WDS.ModelSpec
Utilities surrounding the WDS Model Specification Schema and implementations. Some
examples and topics include:
<ul>
<li>FieldMD</li>  Field meta data utility.
</ul>

## WDS utilities
General utilities.  Formerly in WDS.util. Some examples and topics include:
<ul>
<li>MonthID</li>  A simple month based identifier, 12(y-2000)+m, and some general utilities.
<li>namespaceop</li>  A decorator to create a function that works on another namespace, saves from having to put "self." on every variable.
<li>history</li>  Lists an interactive session command history and provides an "hbang" function to do something like "!#".
</ul>

## WDS.Wranglers
General data wrangling utilities.  Some examples and topics include:
<ul>
<li>Excel2CSV</li> A simple xlrd based extractor.
<li>dir_walk</li> An extended directory walker.
</ul>

## scripts
Supporting linux based scripts that facilitate odds and ends:
<ul>
<li>p_m</li> Converts "p_m dir/file.py args" into a call of "python -m dir.file args"
</ul>

## zzzExamples
Basic canonical examples of concepts, often mirrored across languages for the WDS ModelSpec.
These are local basic references of a few core concepts.

The examples use paths for some default arguments which are relative to the parent of 
zzzExamples and were tested using the p_m script from that location.

The zzzExamples/data files (not versioned) contains some basic files for testing.  These are not 
on the WDS github site but are readily available from the usual sources.  Recent values:
<ul>
<li>IrisMultinomReg.xml</li> - from the standard dmg.org test set
<li>eis_ABS_AutoLoanAssetData.xsd</li> - EDGAR auto loan schema
<li>Book1.xlsm</li> - a test Excel xlsm file (with a VBA module)
<li>housing.csv</li> - a test csv file
<li>pmml-4-0.xsd</li> - the standard dmg.org source
<li>pmml-4-3.xsd</li> - the standard dmg.org source
</ul>

# UNDER CONSTRUCTION
Supporting libraries are added periodically.

