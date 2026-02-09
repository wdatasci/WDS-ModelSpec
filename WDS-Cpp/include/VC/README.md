# General ReadMe
For Visual Studio (on Windows) and to anonymize the github projects, the following environment variables are used:
<ul>
<li>WDataSci_ROOT - the local Windows path to the local copy of the WDataSci github root</li>
<li>IntelSWTools_ROOT - the local Windows path to the Intel compile tools</li>
<li>CppLocalExternalPackages - a common root for xll/master, Excel2013XLLSDK, XLW, and/or other non-standard
    C++ Windows libraries that may need to be included or linked
    <ul>
    <li>As noted elsewhere, xll is the one of the excellent projects by Keith A. Lewis, the latest used here is
    [xll24](https://github.com/xlladdins/xll24).</li>
    <li>xll_ROOT and Excel2013XLLSDK_ROOT can be changed in props/WDS.xll.props.</li>
    </ul>
</li>
</ul>
