Attribute VB_Name = "RAGVBAGeneralFunctions"
Option Base 1
Sub nnn_RAGVBAGeneralFunctions()
    notes = "Risk Analytics Group Miscellaneous VBA Functions" & Chr(10) & Chr(10) & _
        "Odds and ends that are commonly used"
    MsgBox (notes)
End Sub

Function fSheetName(ByRef arg1 As Range, Optional forceit = 0)
fSheetName = arg1.Parent.Name
End Function

Function fWBName(ByRef arg1 As Range, Optional forceit = 0)
fWBName = arg1.Worksheet.Parent.Name

End Function

Function fWBPath(ByRef arg1 As Range, Optional forceit = 0)
fWBPath = arg1.Worksheet.Parent.Path

End Function

Function IsASheetName(ByVal s As String) As Boolean
Dim x As Worksheet

IsASheetName = False
For Each x In ActiveWorkbook.Sheets
    If x.Name = s Then IsASheetName = True
    If IsASheetName Then GoTo ExitFunction
Next

ExitFunction:

End Function

Function fQuote(arg, Optional forceit = 0) As String
fQuote = """" & arg & """"
End Function


Function fColumnFromCode(arg As Integer) As String
Dim x As Integer
Dim y As Integer
x = Int((arg - 1) / 26)
y = arg - x * 26
If x > 0 Then
    fColumnFromCode = Chr(x + 64) & Chr(y + 64)
Else
    fColumnFromCode = Chr(y + 64)
End If

End Function

Function mnmx(arg1, arg2, arg3)
mnmx = ldMin(arg1, ldMax(arg2, arg3))
End Function

Function fCleanLimits(arg1, arg2, arg3, Optional arg4 = 0)
If arg1 < arg2 Then
    fCleanLimits = arg4
ElseIf arg1 > arg3 Then
    fCleanLimits = arg4
Else
    fCleanLimits = arg1
End If
End Function

Function Date2MonthID(arg As Date) As Integer

    y = Year(arg)
    m = Month(arg)
    Date2MonthID = (y - 2000) * 12 + m
    
End Function

Function MonthID2Date(arg As Integer) As Date

    y = Int((arg - 1) / 12)
    m = arg - 12 * y
    y = y + 2000
    MonthID2Date = DateSerial(y, m, 1)

End Function

Function MonthID2MonthN(arg As Integer) As Long

    y = Int((arg - 1) / 12)
    m = arg - 12 * y
    y = y + 2000
    MonthID2MonthN = y * 100 + m

End Function

Function ifnull(ByVal arg As Variant, ByVal arg2 As Double)
On Error Resume Next
    If Application.WorksheetFunction.IsError(arg) Then
        ifnull = arg2
    ElseIf Not IsNumeric(arg) Then
        ifnull = arg2
    Else
        ifnull = arg
    End If
End Function
Function ifnullorzero(ByVal arg As Variant, ByVal arg2 As Double)
    
    ifnullorzero = ifnull(arg, arg2)
    If ifnullorzero = 0 Then ifnullorzero = arg2
    
End Function
Function ldMax(ByVal a As Double, ByVal b As Double)
'VBA Max function
    If a < b Then
        ldMax = b
    Else
        ldMax = a
    End If
End Function
Function ldMin(ByVal a As Double, ByVal b As Double)
'VBA Min function
    If a < b Then
        ldMin = a
    Else
        ldMin = b
    End If
End Function




Function lAtan(ByVal a As Double, ByVal b As Double)
Pi = 3.1428

If a = 0 Then
    If b > 0 Then
        lAtan = Pi / 2
    Else
        lAtan = -Pi / 2
    End If
ElseIf b = 0 Then
    If a < 0 Then
        lAtan = Pi
    Else
        lAtan = 0
    End If
Else
    If a < 0 Then
    If b > 0 Then
        lAtan = Application.WorksheetFunction.Atan2(a, b)
    Else
        lAtan = Application.WorksheetFunction.Atan2(a, b)
    End If
    Else
    If b > 0 Then
        lAtan = Application.WorksheetFunction.Atan2(a, b)
    Else
        lAtan = Application.WorksheetFunction.Atan2(a, b)
    End If
    End If
End If


End Function

Function FlipSumProduct(ByRef r As Range, ByRef s As Range) As Double

Dim sm, lcls As Double

sm = 0

Dim i, j, k, l As Integer

l = r.Rows.Count
If l > s.Rows.Count Then l = s.Rows.Count

k = l + 1
For i = 1 To l
    k = k - 1
    lcls = ifnull(r.Cells(k, 1), 0) * ifnull(s.Cells(i, 1), 0)
    sm = sm + lcls
Next

FlipSumProduct = sm

End Function


Function SumProductAcrossSheets(ByRef r As Range, ByRef s As Range, x As Integer, y As Integer) As Double

Dim sm, lcls As Double

sm = 0

Dim i, j, k, l As Integer

l = r.Cells.Count
If l > s.Cells.Count Then l = s.Cells.Count

For i = 1 To l
    lcls = ifnull(r(i).Value, 0) * ifnull(Range(s(i).Value & "!" & fColumnFromCode(y) & x).Value, 0)
    sm = sm + lcls
Next

SumProductAcrossSheets = sm

End Function



Function SumProductAcrossSheetsWithUpDraft(ByRef r As Range, ByRef s As Range, x As Integer, y As Integer, z As Integer) As Double

Dim sm, lcls As Double

sm = 0

If z > 0 Then
Dim i, j, k, l, m As Integer

l = r.Cells.Count
If l > s.Cells.Count Then l = s.Cells.Count

Dim xx As Double

For i = 1 To l
    xx = ifnull(r(i).Value, 0)
    
For m = 0 To z - 1
    lcls = xx * ifnull(Range(s(i).Value & "!" & fColumnFromCode(y) & (x - m)).Value, 0)
    sm = sm + lcls
Next
Next

End If

SumProductAcrossSheetsWithUpDraft = sm

End Function

Function SumProductAcrossSheetsWithUpDraft2( _
    ByRef r As Range, _
    ByRef s As Range, _
    x As Integer, _
    y As Integer, _
    z As Integer _
    ) As Double

' r is the production factor
' s is the list of sheets to add over
' x is the row to take (current row)
' y is the column to take
' z is not necessary

Dim sm, lcls As Double

sm = 0

If z > 0 Then
Dim i, j, k, l, m As Integer

l = r.Cells.Count
If l > s.Cells.Count Then l = s.Cells.Count

Dim xx As Double

Dim nz
nz = r.Rows.Count
For i = 1 To l
    For m = 0 To nz - 1
'        xx = ifnull(r(l - m, i).Value, 0)
        xx = ifnull(r(m + 1, i).Value, 0)
        lcls = xx * ifnull(Range(s(i).Value & "!" & fColumnFromCode(y) & (x - m)).Value, 0)
        sm = sm + lcls
    Next
Next

End If

SumProductAcrossSheetsWithUpDraft2 = sm

End Function

Function sumbystride(ByRef r As Range, ByVal stp As Integer)

Dim rc, i As Integer
rc = r.Cells.Count
sumbystride = 0
For i = 1 To Int((rc - 1) / stp + 1)
    sumbystride = sumbystride + r.Cells((i - 1) * stp + 1, 1)
Next


End Function

Function SumOffsetRange(ByRef r As Range, ByVal c As Integer, ByVal stp As Integer, ByVal n As Integer) As Variant

Dim rc

ReDim rc(1, c) As Double

For j = 1 To c
rc(1, j) = 0
For i = 1 To n
rc(1, j) = rc(1, j) + r.Offset(i * stp, j)
Next
Next
SumOffset = rc

End Function
Function SumOffsetSingle(ByRef r As Range, ByVal c As Integer, ByVal stp As Integer, ByVal n As Integer) As Variant

Dim rc

ReDim rc(1, 1) As Double

For j = c To c
rc(1, 1) = 0
For i = 1 To n
rc(1, 1) = rc(1, 1) + ifnull(r.Offset(i * stp, j), 0)

Next
Next
SumOffsetSingle = rc

End Function



Function ContingencyTableChi2(ByRef arg1 As Range, ByRef arg2 As Range, Optional denompower = 1)

m1 = arg1.Rows.Count
n1 = arg1.Columns.Count
m2 = arg2.Rows.Count
n2 = arg2.Columns.Count
rc = 0
If n1 = n2 And m1 = m2 Then
Dim x, y As Double
For i = 1 To m1
For j = 1 To n2
x = arg2(i, j).Value
y = arg1(i, j).Value

If x <> 0 Then
    rc = rc + (x - y) ^ 2 / x ^ denompower
    
End If
Next
Next

End If
ContingencyTableChi2 = rc

End Function
Function ContingencyTableChi22(ByRef arg1 As Range, ByRef arg2 As Range, Optional denompower = 1)

m1 = arg1.Rows.Count
n1 = arg1.Columns.Count
m2 = arg2.Rows.Count
n2 = arg2.Columns.Count
rc = 0
If n1 = n2 And m1 = m2 Then
Dim x, y As Double
For i = 1 To m1
s = 0
r = 0
For k = 1 To n2
    r = r + arg1(i, k).Value
    s = s + arg2(i, k).Value
Next
If s > 0 And r > 0 Then
For j = 1 To n2
x = arg2(i, j).Value
y = arg1(i, j).Value
If x <> 0 Then
    rc = rc + (y - x * r / s) ^ 2 / (x * r / s) ^ denompower
End If
Next
End If
Next

End If
ContingencyTableChi22 = rc

End Function





