# UNDER CONSTRUCTION
Supporting libraries are added periodically.

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
    <li>WDS-XSD: the WDS-ModelSpec schema and documentation including:</li>
                <ul>
                    <li>A precise XML Schema (XSD)</li>
                    <li>A concise doc covering:</li>
                        <ul>
                            <li>Naming Conventions</li>
                            <li>Key terms and organization</li>
                            <li>Meta-Modeling objectives</li>
                            <li>Implementation objectives</li>
                        </ul>
                    <li>An extended documentation with discussion of historical development directions and commentary</li>
                    <li>Core examples</li>
                </ul>
    <li>WDS-PMML: transformation utilities between WDS-ModelSpec and PMML</li>
    <li>Prototypes: for use or for teaching purposes, a collection of process meta-models</li>
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





