# General ReadMe

The WDS-ModelUtil-XLL is a collection of common Excel based utilities used by Wypasek Data Science, Inc.
for a compiled non-COM XLL implementation on Windows.

A few brief notes:
<ul>
<li>A compiled stand-alone version is in WDS-Cpp/lib.</li>
<li>Visual Studio C++ prop files are in WDS-Cpp/include/VC/props.</li>
    <ul>
        <li>See WDS-Cpp/include/VC/README.md for environment variables included withn the prop files.</li>
    </ul>
<li>Major external packages:</li>
    <ul>
        <li>xll12 - for simplifying the interface and Excel function registration.</li>
        <li>The Excel 2013 XLL SDK (which works through Excel 2016).</li>
    </ul>
<li>CW Usage note: If one readily goes back and forth between something like Ubuntu via WSL and VS (and you
    might have created directories in Ubuntu), you might encounter occassional trouble with VS finding files.
    The following powershell snippet, possibly needing to be run as admin or with permissions, run in the 
    top location may fix the problem:</li>
    <ul> 
    <li>foreach ( $d in Get-ChildItem -Directory -Recurse ) { fsutil.exe file setCaseSensitiveInfo $d.FullName disable } </li>
    </ul>
</ul>

