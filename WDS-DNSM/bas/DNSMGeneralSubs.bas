Attribute VB_Name = "RAGVBAGeneralSubs"
Option Base 1
Sub nnn_RAGVBAGeneralSubs()
    notes = "Risk Analytics Group Miscellaneous VBA Subs (sub-routines)" & Chr(10) & Chr(10) & _
        "Odds and ends that are commonly used"
    MsgBox (notes)
End Sub
Sub gba_RACM_MoveSheetToFront()
    ActiveSheet.Move Before:=Sheets(1)
End Sub
Sub gaa_ActivateOrAddSheet(ByVal arg1 As String, Optional indx = 1, Optional BeforeOrAfter = 1)

TryIt:

On Error GoTo CatchIt

    Sheets(arg1).Activate

GoTo ElseIt
CatchIt:

    Dim NewSheet As Worksheet
    Set NewSheet = Sheets.Add
    NewSheet.Name = arg1
    If BeforeOrAfter = 1 Then
        NewSheet.Move Before:=Sheets(indx)
    Else
        NewSheet.Move After:=Sheets(indx)
    End If
    
ElseIt:

End Sub

Sub gba_RACM_TwiddleValues()

Dim arg As Range

Dim temp As Variant

Set arg = Selection

If arg.Cells.Count > 1 Then

    temp = arg.Cells(1, 1)
    arg.Cells(1, 1) = arg.Cells(arg.Rows.Count, arg.Columns.Count)
    arg.Cells(arg.Rows.Count, arg.Columns.Count) = temp
    
End If


End Sub
Sub gba_RACM_AddWrapperTabs()
    
    Dim s As String
    
    s = InputBox("Tab title")
    
    Dim lts As Worksheet
    Dim d
    
For Each d In Array("<<", ">>")

    Set lts = Sheets.Add
    lts.Select
    lts.Name = s & d
    lts.Cells(2, 2) = s & d
    lts.Cells(2, 2).Font.Size = 36
    lts.Cells(2, 2).Font.Bold = True
    lts.Cells(2, 2).Font.Italic = True
    lts.Tab.ColorIndex = 44
    ActiveWindow.DisplayGridlines = False
Next

End Sub
Sub setAppPath2ThisWBPath()
'Hit if opening a workbook in the finder or explorer and then going to open a local file

Application.Path = ActiveWorkbook.Path

End Sub

Function aAddButtonOverCell(lButtonName, lSheetName, lCellAddress, lButtonText, lMacroName)
'Creates a button over a cell with location exactly defined by the cell
'Sheets(lSheetName).Select
Range(lCellAddress).Select
l = Selection.Left + 1
t = Selection.Top
w = Selection.Width
h = Selection.Height
ActiveSheet.Buttons.Add(l, t, w, h).Select
Selection.Name = lButtonName
Selection.OnAction = lMacroName
Selection.Characters.Text = lButtonText

aAddButtonOverCell = 0

End Function

Function aAddSpinnerOverCell(lButtonName, lSheetName, lCellAddress, lMin, lInitialValue, lMax, lTargetCellAddress)
'Creates a spinner over a cell with location exactly defined by the cell
'Sheets(lSheetName).Select
Range(lCellAddress).Select
l = Selection.Left + 1
t = Selection.Top
w = Selection.Width
h = Selection.Height
ActiveSheet.Spinners.Add(l, t, w, h).Select
Selection.Name = lButtonName
Selection.Value = lInitialValue
Selection.Min = lMin
Selection.Max = lMax
Selection.LinkedCell = lTargetCellAddress

aAddSpinnerOverCell = 0

End Function



Public Sub cbpRACTB_ClearExternalNamedRanges()

 '   cbpRACTB_SheetOverview

    i = 0
    While Range("A" & (i + 1)).Value <> "Names"
        i = i + 1
    Wend
    
    Dim xr As Range
    For Each xr In Range("B" & i & ":B" & (i + 500)).Cells
        If InStr(xr.Text, "\") Then
            ActiveWorkbook.Names(xr.Offset(0, -1).Text).Delete
        End If
    Next
    
 '   cbpRACTB_SheetOverview
    


End Sub



Sub FillWithSumAcrossSheets()

Dim x As Range
Set x = Selection
s = x.Cells(1, 1).Value
x.Cells(1, 1).FormulaR1C1 = "=sum('" & s & "'!R[0]C[0])"
x.Columns(1).FillDown
x.FillRight

End Sub

