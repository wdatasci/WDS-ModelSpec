Attribute VB_Name = "SMV3_XMLTools"

Function valuein(arg1, arg2)
valuein = False
Dim x
For Each x In arg2
    If x = arg1 Then
        valuein = True
        Exit For
    End If
Next
End Function

Sub xxxDumpXMLMapsSub(Optional DumpAll = True, _
    Optional DumpDriver = False, _
    Optional DumpInputs = False, _
    Optional DumpSpecs = False, _
    Optional lastarg = 1)


Dim twn, twncomdir As String
twn = ActiveWorkbook.Name
twncomdir = Replace(twn, ".xls", ".xmlcomdir")

Dim fs As Object
Set fs = CreateObject("Scripting.FileSystemObject")

'Set a = fs.CreateTextFile("c:\testfile.txt", True)
'a.WriteLine ("This is a test.")
'a.Close

If Not fs.FolderExists(twncomdir) Then
    MkDir (twncomdir)
End If

Dim x As Worksheet
Dim ts As Worksheet

Set ts = ActiveSheet

Dim y As XmlMap

    For Each y In ActiveWorkbook.XmlMaps
    If y.IsExportable Then
    If DumpAll = True Then
        y.Export URL:=twncomdir & "\" & y.Name, Overwrite:=True
    ElseIf DumpDriver = True And y.Name = "SMDriverInfo" Then
        y.Export URL:=twncomdir & "\" & y.Name, Overwrite:=True
    ElseIf DumpInputs = True And y.Name = "Sg1InputsExportMap" Then
        y.Export URL:=twncomdir & "\" & y.Name, Overwrite:=True
    ElseIf DumpSpecs = True And valuein(y.Name, Array("SMStocksAndFlows", "SMStateSpace", "SMStateSpaceSampler")) Then
        y.Export URL:=twncomdir & "\" & y.Name, Overwrite:=True
    End If
    End If
    Next

End Sub
Sub xaaDumpXMLMaps()
Call xxxDumpXMLMapsSub
End Sub
Sub xaaDumpXMLInputsAndDriver()
Call xxxDumpXMLMapsSub(DumpAll:=False, DumpInputs:=True, DumpDriver:=True)
End Sub
Sub xaaDumpXMLDriver()
Call xxxDumpXMLMapsSub(DumpAll:=False, DumpInputs:=False, DumpDriver:=True)
End Sub
Sub xaaDumpXMLSpecs()
Call xxxDumpXMLMapsSub(DumpAll:=False, DumpInputs:=False, DumpDriver:=False, DumpSpecs:=True)
End Sub
Sub cbaPullInUsualXMLMaps()

    Dim PathToSMProtoTypeXSDs
    PathToSMProtoTypeXSDs = "C:\LocalWork\SMV1\SMProtoType\xsd\"

    'ActiveWorkbook.XmlMaps.Add(PathToSMProtoTypeXSDs & "SMStateSpaceSpec.xsd", "SMStateSpace").Name = "SMStateSpace"
    'ActiveWorkbook.XmlMaps.Add(PathToSMProtoTypeXSDs & "SMStateSpaceSamplerSpec.xsd", "SMStateSpaceSampler").Name = "SMStateSpaceSampler"
    'ActiveWorkbook.XmlMaps.Add(PathToSMProtoTypeXSDs & "SMStocksAndFlowsSpec.xsd", "SMStocksAndFlows").Name = "SMStocksAndFlows"
    ActiveWorkbook.XmlMaps.Add(PathToSMProtoTypeXSDs & "SMDriverInfo.xsd", "SMDriverInfo").Name = "SMDriverInfo"


End Sub

Sub xaaClearUsualMaps()


Dim y As XmlMap

    For Each y In ActiveWorkbook.XmlMaps
    If y.Name <> "SMStateSpaceSpec_Map" And _
        y.Name <> "SMStateSpaceSpec" And _
        y.Name <> "SMStateSpace_Map" And _
        y.Name <> "SMStateSpace" And _
        y.Name <> "SMStateSpaceSamplerSpec" And _
        y.Name <> "SMStocksAndFlowsSpec_Map" And _
        y.Name <> "SMStocksAndFlowsSpec" And _
        y.Name <> "SMStocksAndFlows_Map" And _
        y.Name <> "SMStocksAndFlows" And _
        y.Name <> "SMDriverInfo" _
    Then
        ActiveWorkbook.XmlMaps(y.Name).Delete
    End If
    Next



End Sub

