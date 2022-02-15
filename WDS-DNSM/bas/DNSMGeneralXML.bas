Attribute VB_Name = "RAGVBAGeneralXML"
Option Base 1
Sub nnn_RAGVBAGeneralXML()
    notes = "Risk Analytics Group Miscellaneous VBA XML functions and subs" & Chr(10) & Chr(10) & _
        "Odds and ends that are commonly used"
    MsgBox (notes)
End Sub
Function IsAnXMLMapName(ByVal s As String) As Boolean
Dim x As XmlMap

IsAnXMLMapName = False
For Each x In ActiveWorkbook.XmlMaps
    If x.Name = s Then IsAnXMLMapName = True
    If IsAnXMLMapName Then GoTo ExitFunction
Next

ExitFunction:

End Function
Function rXMLDataQuery(ByVal sheetname As String, ByVal xp As String, Optional map = "") As Range
Dim x As Worksheet
Set x = Sheets(sheetname)

If map = "" Then

    Set rXMLDataQuery = x.XmlDataQuery(xp)

Else

    Dim xmp As XmlMap
    Set xmp = ActiveWorkbook.XmlMaps(map)
    
    Set rXMLDataQuery = x.XmlDataQuery(xp, "", xmp)

End If


End Function
