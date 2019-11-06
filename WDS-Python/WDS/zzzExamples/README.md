DocNote: Christian Wypasek

The zzzExamples directory is not an integral part of the WDS library but represents a collection
of simple canonical examples for a local reference and for test/trial.  Here written in python, 
but the corresponding concepts will be duplicated in other languages.

Why the "zzz" prefix?  So that it naturally alphabetically sorts to the end.....

Since these examples are meant to be basic and a simple reference, these should not use any other 
than basic python3 or external importable packages that can be installed via apt-get or pip3, such 
as numpy, scipy, matplotlib, xlsxwriter, pandas, etc. 

Goal List, target code:

Hello World               - HelloWorld.py
argparse                  - HelloWorld.py

general python
    classes               - MonkeyPatch.py
    monkey patching       - MonkeyPatch.py
    functions, lambdas    - Functions.py
    iterators, generators - Iterators.py
    decorators            - Iterators.py
    filter                - generateDS_example_usage.py
    map                   - DataViaODBC.py

multi-proc (or possibly with an example of GIL multi-threading problems and how to solve with pool processing)
                     - Pools.py

basic XML            - BasicXML.py
basic XSL            - BasicXML.py
basic XSD validation - BasicXML.py


PMML                            - BasicXML.py, generateDS_example_usage.py
code binding with generateDS.py - generateDS_example_usage.py
Excel reading                   - ExcelRead.py
Excel writing                   - ExcelWrite.py
directory transversing          - Iterators.py
accessing data                  - DataViaODBC.py
flat file reading and writing   - Files.py


generateDS - an external package for code-binding based on XSD
    Use the linux shell script generateDS_example to create a data-bound module
        based on an XSD
    Use generateDS_example_usage to parse an XML based on the created module





TODOs:

Half-baked:
records/DataFrame               - DataFrame_Stuff.py 

XAML? -------later

additional basic common platform trials:
    numpy
    scipy
    matplotlib
    pandas
    Numba?






