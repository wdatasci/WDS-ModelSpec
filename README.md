# UNDER CONSTRUCTION
Supporting libraries are added periodically.

# Notes through 2022-02:
The documentation for the model specification and style files have been added in WDS-XLM.


# Notes on updates through 2021-08:
In addition to general updates:
<ul>
    <li>Added utilities for calling Couchbase from Lua for SEC data project.</li>
    <li>Added Vertica C++ UDTF utilities.  In particular, added prototype functions and XSLT transformations for quick XML based specification.</li>
    <li>Added C# Excel XLL example for calling MS ClearScript and V8/Node.js.</li>
</ul>

# Notes on updates through 2020-01:
Continuing standardization of WDS-Lua including additional documentation, a json class, and Couchbase functionality. WPS compatible SAS language macros have been added in WDS-SAS.

# Notes on updates through early 2019-11:
WDS-Cpp was added and includes a basic framework for which additional computational tools will be added.  In particular, a starting Matrix
class, which is usually like the classic Stroustrup, but here extends armadillo.  A basic XLL wrapper starts with simple row-normalizer but
will be extended with parameterized matrix model methods Wypasek Data Science uses.  WDS-Lua was added and WDS-Python was updated.


# WDS-ModelSpec
Documentation, Schemas, Data Wrangling, and Estimation/Implementation Utilities for the ModelSpec of WDataSci

Wypasek Data Science, Inc. (WDataSci or WDS) uses an efficient meta-data and meta-modeling approach that is both project and production 
oriented for data engineering/architecture and model specification.  The methodology is generalizable and has evolved from over 
twenty years of experience in building large data bases, models, implementations, and integrating results into
larger systems for the cash flow forecasting of consumer based assets.

Core to the methodology is an XML specification that can be used both model specification and implementation.  PMML 
is similar in many implementation concepts, especially in more recent versions (4.0+).  However, early versions were 
significantly insufficient for the purposes of the architects of WDS-ModelSpec and it developed independently of PMML.  

XML is used, as implied, as a manner to markup meta-model and model details.  If the mark-up style is sufficient, it can easily be translated
into other styles, such as json, yaml, or other XML such as PMML.
Therefore, this incarnation of the WDS-ModelSpec (please see the extended documentation
for historical development) does contain elements so that PMML can be faithfully generated and be in common PMML implementations.
Please see the sister project, WDS-JniPMML-XLL, for an Excel AddIn that can call the standard PMML evaluator.

The meta-model and model details are not just for implementation (as in PMML).  Some of the most efficient running code for a 
particular model is compilable pedantically enumerated operations on data field values (in almost any language) as opposed to 
operator working on something like a row-object based on information cached in an XML tree.  One can do either, or even better, 
do which ever is better for the process at hand.   Pedantic enumeration can often be the easiest way to generate model estimation 
code, which after incorporation of model estimation products back into the specification, becomes the basis for implementation, 
in almost any language or PMML.

# Specific subdirectory notes (under construction, current directions/targets)
<ul>
    <li>WDS-Doc: the WDSModelSpec documentation including:</li>
                <ul>
                    <li>A concise doc covering:</li>
                        <ul>
                            <li>Naming Conventions</li>
                            <li>Key terms and organization</li>
                            <li>Meta-Modeling objectives</li>
                            <li>Implementation objectives</li>
                        </ul>
                    <li>An extended documentation with discussion of historical development directions and commentary</li>
                </ul>
    <li>WDS-General:</li>
    <ul>
        <li>Prototypes: for use or for teaching purposes, a collection of process meta-models</li>
        <li>util: a collection of helper scripts</li>
    </ul>
    <li>WDS-XSD: the WDS-ModelSpec schema and transformations:</li>
                <ul>
                    <li>XSD-Source-Mapping-Example.xlsm, an example using Excel as a gui to export proper XML formats.</li>
                    <li>XSD</li>
                        <ul>
                            <li>A precise XML Schema (upcoming)</li>
                            <li>States and Stages Schema</li>
                            <li>Stocks and Flows Schema</li>
                            <li>Generic Parameterizable Matrix Schema</li>
                        </ul>
                    <li>XSL (upcoming)</li>
                    <li>WDS-PMML: transformation utilities between WDS-ModelSpec and PMML (upcoming)</li>
                </ul>
    <li>WDS-DNSM: an archive of old dynamic systems model work</li>
</ul>


# Language specific libraries
A goal of the overall methodology is to be language agnostic, therefore, by design, common concepts will be named and coded similarly 
across languages.  Each language specific library and source location, WDS-[AAA], will have as common a structure as possible.
<ul>
    <li>WDS-[AAA]: the root associated with language [AAA], generally on the language specific search path, containing:</li>
        <ul>
            <li>Project/solution configuration and/or build parameter files</li>
            <li>WDS or src: the module root or main src location with sub-libraries</li>
                <ul>
                    <li>Comp: computational routines, such as matrix and artificial libraries</li>
                    <li>ModelSpec: directly related to WDS-ModelSpec</li>
                    <li>Util: general independent utilities</li>
                    <li>Wranglers: data wrangling and data layer utilities</li>
                    <li>zzzExamples: Small non-critical examples which serve as local language reference/test</li>
                </ul>
            <li>scripts: scripts or batch files associated with using or building the [AAA] library</li>
            <li>test: any test data or examples as necessary</li>
        </ul>
</ul>





