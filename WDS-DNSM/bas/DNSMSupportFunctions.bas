Attribute VB_Name = "SMV3_SupportFunctions"
Option Base 1
Function fDefStateNames(arg1 As String, arg2 As Integer) As Variant
Dim rc
ReDim rc(1, ldMax(20, arg2)) As Variant
For i = 1 To arg2
    rc(1, i) = arg1 & i
Next
For i = arg2 + 1 To 20
    rc(1, i) = ""
Next
fDefStateNames = rc
End Function
Function BridgeFromBits(ByRef NameSet As Range, _
ByRef FromPart As Range, _
ByRef ToPart As Range) As String

Dim rc As String
rc = ""
Dim x As Range
Dim i As Integer

i = 0
For Each x In NameSet
    i = i + 1
    If FromPart(i).Value = "Bridge" & ToPart.Value Then
        rc = rc & "1"
    ElseIf NameSet(i) = ToPart Then
        If FromPart(i).Value = "Transient" Then
            rc = rc & "1"
        ElseIf FromPart(i).Value = "Null" Then
            rc = rc & "1"
        ElseIf FromPart(i).Value = "Pickup" Then
            rc = rc & "1"
        ElseIf FromPart(i).Value = "PickupBridge" Then
            rc = rc & "1"
        Else
            rc = rc & "0"
        End If
    Else
        rc = rc & "0"
    End If
Next

BridgeFromBits = rc


End Function


Sub aza_ClearStocksAndFlowsResults()

Dim y As Range
Dim nStates As Integer
nStates = Sheets("SMStateSpaceSpec").XmlDataQuery("/SMStateSpace/States/Number").Value
'Range("AllUnits!" & fColumnFromCode(nStates + 2) & 101 & ":HZ300").Clear
Range("AllUnits!B101:HZ300").Clear

Dim i, j As Integer
i = 0
j = Sheets("SMStocksAndFlowsSpec").XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value
For Each y In Sheets("SMStocksAndFlowsSpec").XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Mneumonic")
    i = i + 1
    If i <= j Then
    Range(y.Text & "!B101:HZ300").Clear
'       Range(y.Text & "!" & fColumnFromCode(nStates + 2) & 101 & ":HZ300").Clear
    End If
Next
For Each y In Sheets("SMStocksAndFlowsSpec").XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic")
    Range(y.Text & "!B101:HZ300").Clear
'    Range(y.Text & "!" & fColumnFromCode(nStates + 2) & 101 & ":HZ300").Clear
Next
End Sub
Sub RunStage1()
SS = "StageAndStateSpec"
SF = "StockAndFlowSpec"
Call RunStage(1, SS, SF)
End Sub
Sub RunStage1NoPickup()
SS = "StageAndStateSpec"
SF = "StockAndFlowSpec"
Call RunStage(1, SS, SF, True)
Application.CalculateFull
End Sub
Sub RunStage(ByVal arg1 As Integer, ByVal SS As String, ByVal SF As String, Optional PrevOnly = False)

'Dim Stages, States As String
'Stages = Range(SS & "StagesHandle").Value
'States = Range(SS & "StatesHandle").Value
'
'Dim Stocks, Flows As String
'Stocks = Range(SF & "StocksHandle").Value
'Flows = Range(SF & "FlowsHandle").Value
'

'Call PMultByFIDSub(SS, SF, Range("AllUnits!A101:A148"), PrevOnly)
'Call PMultByFIDSubV2(SS, SF, Range("AllUnits!A101:A148"), PrevOnly)
Call PMultByFIDSubV3("SMStateSpaceSpec", "SMStocksAndFlowsSpec", Range("Sg1Inputs!A101:A148"), PrevOnly)



End Sub





Sub aba_SMLGMSetModelSpecToZeros()
Dim i, j, tsn, calcprior

tsn = ActiveSheet.Name
calcprior = Application.Calculation
Application.Calculation = xlCalculationManual

For i = 1 To Range(tsn & "ModelSpec").Rows.Count
For j = 1 To Range(tsn & "ModelSpec").Columns.Count
    If (Range(tsn & "ModelSpec").Cells(i, j).Value > 0) And (i <> j) Then
        Range(tsn & "ModelSpec").Cells(i, j).Value = 0
    End If
Next
Next

Application.Calculation = calcprior

End Sub

Function OddsFiller(ByRef BetasIndex As Range, ByRef BetasAddress As Range, ByRef Betas As Range, ByRef Topology As Range) As Variant

Dim rc As Variant
nb = BetasIndex.Rows.Count
If nb = BetasAddress.Rows.Count And nb = Betas.Rows.Count Then

m1 = Topology.Rows.Count
n1 = Topology.Columns.Count

ReDim rc(m1, n1) As Double
For i = 1 To m1
For j = 1 To n1
rc(i, j) = 0
Next
Next

For i = 1 To nb
    u = BetasAddress(i, 1)
    v = BetasAddress(i, 2)
    rc(u, v) = rc(u, v) + Betas(i).Value
Next

For i = 1 To m1
For j = 1 To n1
    If Topology.Cells(i, j).Value > 0 Then
        rc(i, j) = Exp(rc(i, j))
    End If
Next
Next

End If
OddsFiller = rc

End Function
Function OddsFillerWithBase(ByRef BetasIndex As Range, ByRef BetasAddress As Range, ByRef Betas As Range, ByRef Topology As Range, ByRef BaseOdds As Range) As Variant

Dim rc As Variant
nb = BetasIndex.Rows.Count
If nb = BetasAddress.Rows.Count And nb = Betas.Rows.Count Then

m1 = Topology.Rows.Count
n1 = Topology.Columns.Count

ReDim rc(m1, n1) As Double
For i = 1 To m1
For j = 1 To n1
rc(i, j) = 0
Next
Next

For i = 1 To nb
    u = BetasAddress(i, 1)
    v = BetasAddress(i, 2)
    If Not (IsEmpty(Betas(i))) Then
        rc(u, v) = rc(u, v) + Betas(i).Value
    End If
Next

For i = 1 To m1
For j = 1 To n1
    If Topology.Cells(i, j).Value > 0 Then
        If rc(i, j) < -8 Then
            rc(i, j) = -8
        End If
        If rc(i, j) > 8 Then
            rc(i, j) = 8
        End If
        rc(i, j) = Exp(rc(i, j))
        If (Not (IsEmpty(BaseOdds.Cells(i, j)))) And (BaseOdds.Cells(i, j).Value > 0) Then
            rc(i, j) = rc(i, j) * BaseOdds.Cells(i, j)
        End If
    End If
Next
Next

End If
OddsFillerWithBase = rc

End Function
Function OddsWithDiagRef(ByRef m As Range) As Variant

Dim rc As Variant

m1 = m.Rows.Count
n1 = m.Columns.Count
m2 = m1
n2 = n1
If n1 < m1 Then m2 = n1

ReDim rc(m1, n1) As Double
For i = 1 To m1
For j = 1 To n1
rc(i, j) = 0
Next
Next


For i = 1 To m2
If m(i, i) > 0 Then
    For j = 1 To n2
        If i <> j Then
            If m(i, j) > 0 Then
                rc(i, j) = m(i, j) / m(i, i)
            End If
        End If
    Next
End If
Next

OddsWithDiagRef = rc

End Function
Function OddsWithDiagRefAndTopology(ByRef m As Range, ByRef topol As Range) As Variant

Dim rc As Variant

m1 = m.Rows.Count
n1 = m.Columns.Count
m2 = m1
n2 = n1
If n1 < m1 Then m2 = n1

ReDim rc(m1, n1) As Double
For i = 1 To m1
For j = 1 To n1
rc(i, j) = 0
Next
Next


For i = 1 To m2
'If m(i, i) > 0 Then
    For j = 1 To n2
        If i <> j Then
            If m(i, j) > 0 Then
            If m(i, i) > 0 Then
                rc(i, j) = m(i, j) / m(i, i)
            Else
                rc(i, j) = m(i, j) / 0.00001
            End If
            ElseIf topol(i, j) > 0 Then
                rc(i, j) = 0.0001
            End If
        End If
    Next
'End If
Next

OddsWithDiagRefAndTopology = rc

End Function

Sub caa_LGMFIDProtoType()

Dim tsn, tadd As String

tsn = ActiveSheet.Name
tadd = Selection.Cells(1, 1).Address
targetFID = InputBox("Which LGM is this FID being setup for?")
Call xxx_LGMFIDProtoTypeSub(tsn, tadd, targetFID)

End Sub
Sub xxx_LGMFIDProtoTypeSub(ByVal tsn As String, ByVal tadd As String, ByVal targetFID As String)

calcprior = Application.Calculation

Application.Calculation = xlCalculationManual

Dim xr As Range
Set xr = Range(tsn & "!" & tadd)
xr.Value = "FID"
xr.Offset(0, 1).Value = targetFID
xr.Offset(1, 0).Value = "NumStates"
xr.Offset(1, 1).Formula = "=" & targetFID & "!C3"
Dim ci
ci = 1

ci = ci + 1
xr.Offset(ci, 0).Value = "Betas"
xr.Offset(ci, 1).Formula = "=" & targetFID & "NumberBetas"
Application.Names.Add Name:=targetFID & "FIDNumBetas", RefersTo:="=" & tsn & "!" & xr.Offset(ci, 1).Address
ci = ci + 1
xr.Offset(ci, 0).Value = "Label"
xr.Offset(ci, 1).FormulaR1C1 = "=if(R[2]C=0,if(R[3]C=0,""OddsBaseOffset"",""Across Column "" & INDEX(" & targetFID & "DefStateNames,R[3]C)),if(R[3]C=0,""Across Row "" & INDEX(" & targetFID & "DefStateNames,R[2]C),INDEX(" & targetFID & "DefStateNames,R[2]C) & "" to "" & INDEX(" & targetFID & "DefStateNames,R[3]C)))"
ci = ci + 1
xr.Offset(ci, 0).Value = "No."
xr.Offset(ci, 1).FormulaR1C1 = "=N(RC[-1])+1"
If xr.Offset(ci - 2, 1).Value > 0 Then
    Range(tsn & "!" & xr.Offset(ci - 1, 1).Address & ":" & xr.Offset(ci, xr.Offset(ci - 2, 1).Value).Address).FillRight
End If
ci = ci + 1
xr.Offset(ci, 0).Value = "I"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "J"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "Value"
ci = ci + 1
xr.Offset(ci, 0).Value = "Point To Flow"
xr.Offset(ci, 1).Value = 0


ci = ci + 1
xr.Offset(ci, 0).Value = "Single Inputs"
xr.Offset(ci, 1).FormulaR1C1 = "=counta(r[3]c:r[3]c[20])"
Application.Names.Add Name:=targetFID & "FIDNumInputs", RefersTo:="=" & tsn & "!" & xr.Offset(ci, 1).Address
ci = ci + 1
xr.Offset(ci, 0).Value = "Label"
xr.Offset(ci, 1).FormulaR1C1 = "=if(R[2]C=0,if(R[3]C=0,""OddsBaseOffset"",""Across Column "" & INDEX(" & targetFID & "DefStateNames,R[3]C)),if(R[3]C=0,""Across Row "" & INDEX(" & targetFID & "DefStateNames,R[2]C),INDEX(" & targetFID & "DefStateNames,R[2]C) & "" to "" & INDEX(" & targetFID & "DefStateNames,R[3]C)))"
ci = ci + 1
xr.Offset(ci, 0).Value = "No."
xr.Offset(ci, 1).FormulaR1C1 = "=N(RC[-1])+1"
If xr.Offset(ci - 2, 1).Value > 0 Then
    Range(tsn & "!" & xr.Offset(ci - 1, 1).Address & ":" & xr.Offset(ci, xr.Offset(ci - 2, 1).Value).Address).FillRight
End If
ci = ci + 1
xr.Offset(ci, 0).Value = "I"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "J"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "Default Value"
ci = ci + 1
xr.Offset(ci, 0).Value = "Op 0-Add 1-Mult"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "Point To Flow"
xr.Offset(ci, 1).Value = 0
ci = ci + 1
xr.Offset(ci, 0).Value = "Base Set Index (starts at 0)"
xr.Offset(ci, 1).Value = 0


ci = ci + 1
xr.Offset(ci, 0).Value = "Redundant Inputs"
xr.Offset(ci, 1).FormulaR1C1 = "=counta(r[3]c:r[3]c[20])"
Application.Names.Add Name:=targetFID & "FIDNumRedundantInputs", RefersTo:="=" & tsn & "!" & xr.Offset(ci, 1).Address
ci = ci + 1
xr.Offset(ci, 0).Value = "Label"
xr.Offset(ci, 1).FormulaR1C1 = "=if(R[2]C=0,if(R[3]C=0,""OddsBaseOffset"",""Across Column "" & INDEX(" & targetFID & "DefStateNames,R[3]C)),if(R[3]C=0,""Across Row "" & INDEX(" & targetFID & "DefStateNames,R[2]C),INDEX(" & targetFID & "DefStateNames,R[2]C) & "" to "" & INDEX(" & targetFID & "DefStateNames,R[3]C)))"
ci = ci + 1
xr.Offset(ci, 0).Value = "No."
xr.Offset(ci, 1).FormulaR1C1 = "=N(RC[-1])+1"
If xr.Offset(ci - 2, 1).Value > 0 Then
    Range(tsn & "!" & xr.Offset(ci - 1, 1).Address & ":" & xr.Offset(ci, xr.Offset(ci - 2, 1).Value).Address).FillRight
End If
ci = ci + 1
xr.Offset(ci, 0).Value = "I"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "J"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "Default Value"
ci = ci + 1
xr.Offset(ci, 0).Value = "Op 0-Add 1-Mult"
xr.Offset(ci, 1).Value = 1
ci = ci + 1
xr.Offset(ci, 0).Value = "Point To Flow"
xr.Offset(ci, 1).Value = 0
ci = ci + 1
xr.Offset(ci, 0).Value = "Point To Single"
xr.Offset(ci, 1).Value = 1


Application.Names.Add Name:=targetFID & "FID", RefersTo:="=" & tsn & "!" & xr.Address & ":" & xr.Offset(ci, 20).Address

Application.Calculation = calcprior

End Sub

Function SumIt( _
    ByRef s As Range, _
    ByVal r As Integer, _
    ByVal o As Integer, _
    ByVal nStages As Integer, _
    ByRef stageind As Range, _
    ByVal nStates As Integer, _
    ByRef stateind As Range, _
    Optional depends = 0)

Dim i, j, k, l, rc
Dim lr As Range

SumIt = -99

On Error GoTo JustLeave
    
    rc = 0
    For l = 1 To s.Count
        If Not IsEmpty(s(l)) Then
            For i = 1 To nStages + 1
                If Not IsEmpty(stageind(i)) Then
                    For j = 1 To nStates
                        If Not IsEmpty(stateind(j)) Then
                            Set lr = Sheets(s(l).Text).Cells(r, o + (i - 1) * nStates + j)
                            If IsNumeric(lr.Value) Then
                                rc = rc + lr.Value
                            End If
                        End If
                    Next
                End If
            Next
        End If
    Next

JustLeave:

SumIt = rc
End Function
Function SumItR( _
    ByRef s As Range, _
    ByRef r As Range, _
    ByVal o As Integer, _
    ByVal nStages As Integer, _
    ByRef stageind As Range, _
    ByVal nStates As Integer, _
    ByRef stateind As Range, _
    Optional depends = 0) As Variant

x = 1

Dim i, j, k, l, ii, jj, kk, ll, nr, nc
Dim lr As Range

nr = r.Rows.Count
nc = stateind.Columns.Count

'SumIt = -99
Dim rc As Variant

ReDim rc(nr, nc) As Double

On Error GoTo JustLeave2
    
For kk = 1 To nc
For k = 1 To nr
    rc(k, kk) = 0
    For l = 1 To s.Rows.Count
        If (Not IsEmpty(s(l, kk))) And (s(l, kk) <> 0) Then
            For i = 1 To nStages + 1
                If (Not IsEmpty(stageind(i, kk))) And (stageind(i, kk) <> 0) Then
                    For j = 1 To nStates
                        If (Not IsEmpty(stateind(j, kk))) And (stateind(j, kk) <> 0) Then
                            Set lr = Sheets(s(l, kk).Text).Cells(r(k, 1).Row + r(k, 1).Value, o + (i - 1) * nStates + j)
                            If IsNumeric(lr.Value) Then
                                rc(k, kk) = rc(k, kk) + lr.Value
                            End If
                        End If
                    Next
                End If
            Next
        End If
    Next
Next
Next

JustLeave2:

SumItR = rc
End Function




Sub FixAFew()
Attribute FixAFew.VB_Description = "Macro recorded 4/19/2007 by cwypasek"
Attribute FixAFew.VB_ProcData.VB_Invoke_Func = " \n14"
    
    
    
    
x = Array("Sg1BaseCounts", _
    "Sg1BaseOdds", _
    "Sg1BaseBalance", _
    "Sg1BaseBalanceBias", _
    "Sg1BaseFlow1", _
    "Sg1BaseFlow2", _
    "Sg1BaseFlow3", _
    "Sg1BaseFlow4", _
    "Sg1BaseFlow5")
    
Dim z As Range
For Each y In x

    Set z = Range(y)
    
    s = z.Name.RefersTo
    s = Mid(s, 2, InStr(s, "!") - 2)
    Sheets(s).Activate
    
    z.Activate
    z.Cells(3, 3).Select
    
    Range(Selection, Selection.End(xlDown)).Select
    Range(Selection, Selection.End(xlToRight)).Select
    Selection.Copy
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False

    Cells(1, 1).Activate
    
Next


End Sub
