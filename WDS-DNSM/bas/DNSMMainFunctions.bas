Attribute VB_Name = "SMV3_MainFunctions"
Option Base 1

Function PSMFIDOddsFillerWithBase( _
    NMFID As String, _
    PFIDInputs As Range, _
    Optional SS = "SMStateSpaceSpec", _
    Optional SF = "SMStocksAndFlowsSpec", _
    Optional onlyrow = 0, _
    Optional nFlows = 0, _
    Optional PFIDInputsIndex = 1, _
    Optional lastarg = "") As Variant

Dim SMSS, SMSF, SMFID As Worksheet
Set SMFID = Sheets(NMFID)
Set SMSS = Sheets(SS)
Set SMSF = Sheets(SF)

Dim i, j, k, l, s, n, list1, list2, nStates, nStages, nStocks
s = NMFID

nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
nStages = SMSS.XmlDataQuery("/SMStateSpace/Stages/Number").Value

nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
snstocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value
'nflows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
mnflows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value

Set Topology = Range(s & "Topology")
Dim TopologySums
ReDim TopologySums(nStates) As Double
For i = 1 To nStates
    TopologySums(i) = 0
    For j = 1 To nStates
        If Range(s & "Topology").Cells(i, j).Value > 0 Then
            TopologySums(i) = TopologySums(i) + 1
        End If
    Next
Next

Set BaseOdds = Range(s & "BaseOdds")
Set OddsBias = Range(s & "BaseBalanceBias")


Dim rc As Variant
Dim vrc As Variant

nb = SMFID.XmlDataQuery("/SMFID/Betas/Number").Value

If 1 Then

    m1 = Topology.Rows.Count
    n1 = Topology.Columns.Count
    ns = m1
    If onlyrow > 0 Then m1 = 1
    
    ReDim rc(m1, n1) As Double
    For i = 1 To m1
    For j = 1 To n1
    rc(i, j) = 0
    Next
    Next
    
    If nFlows > 0 Then
            ReDim vrc(nFlows + 2) As Variant
            For i = 1 To nFlows + 2
                    vrc(i) = rc
            Next
    Else
            nFlows = 0
            ReDim vrc(1) As Variant
            vrc(1) = rc
    End If
    
    
    
    If 1 Then
    
        Dim ii, jj, iia, iib, jja, jjb, u, v As Integer
        Dim fi
        Dim tempdouble As Double
        
        For i = 1 To nb
            u = SMFID.XmlDataQuery("/SMFID/Betas/Beta/I")(i)
            If u = 0 Then
                iia = 1
                iib = ns
            Else
                iia = u
                iib = u
            End If
            If onlyrow = 0 Or u = onlyrow Then
                If onlyrow > 0 Then
                    u = 1
                    iia = 1
                    iib = 1
                End If
                v = SMFID.XmlDataQuery("/SMFID/Betas/Beta/J")(i)
                fi = SMFID.XmlDataQuery("/SMFID/Betas/Beta/FlowRef")(i) + 1
                tempdouble = SMFID.XmlDataQuery("/SMFID/Betas/Beta/Value")(i)
                If v = 0 Then
                    For ii = iia To iib
                    For jj = 1 To ns
                    If ii <> jj Then
                        vrc(fi)(ii, jj) = vrc(fi)(ii, jj) + tempdouble
                    End If
                    Next
                    Next
                Else
                    For ii = iia To iib
                        vrc(fi)(ii, v) = vrc(fi)(ii, v) + tempdouble
                    Next
                End If
            End If
        Next
        
        Dim BaseOffsets
        ReDim BaseOffsets(nFlows + 2) As Integer
        For i = 1 To nFlows + 1
            BaseOffsets(i) = 0
        Next
        
        i = 0
        Dim x As Double
        Dim rx As Range
        
        For i = 1 To SMFID.XmlDataQuery("/SMFID/FunctionalInputs/Number").Value
        If i <= PFIDInputs.Columns.Count Then
        
            Set rx = PFIDInputs(PFIDInputsIndex, i)
            
            If (Not IsEmpty(rx)) And (IsNumeric(rx.Value)) Then
                x = rx.Value
                If SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/BaseSetInd")(i) = 1 Then
                    If SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/FlowRef")(i) = -1 Then
                        BaseOffsets(nFlows + 2) = x
                    ElseIf SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/FlowRef")(i) <= nFlows Then
                        BaseOffsets(SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/FlowRef")(i) + 1) = x
                    End If
                ElseIf SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/BaseSetInd")(i) = -1 Then
                    NullIN = PFIDInputs(i, 1)
                Else
                    u = SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/I")(i).Value
                    If u = 0 Then
                        iia = 1
                        iib = ns
                    Else
                        iia = u
                        iib = u
                    End If
                    If onlyrow = 0 Or u = onlyrow Then
                        If onlyrow > 0 Then
                            u = 1
                            iia = 1
                            iib = 1
                        End If
                        v = SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/J")(i).Value
                        fi = SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/FlowRef")(i).Value + 1
                        If fi <= nFlows + 1 Then
                            If fi = 0 Then fi = nFlows + 2
                            si = SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/OpZeroOrOne")(i).Value
                            If v = 0 Then
                                If si = 0 Then
                                    For ii = iia To iib
                                    For jj = 1 To ns
                                        vrc(fi)(ii, jj) = vrc(fi)(ii, jj) + x
                                    Next
                                    Next
                                Else
                                    For ii = iia To iib
                                    For jj = 1 To ns
                                        vrc(fi)(ii, jj) = vrc(fi)(ii, jj) * x
                                    Next
                                    Next
                                End If
                            Else
                                If si = 0 Then
                                    For ii = iia To iib
                                        vrc(fi)(ii, v) = vrc(fi)(ii, v) + x
                                    Next
                                Else
                                    For ii = iia To iib
                                        vrc(fi)(ii, v) = vrc(fi)(ii, v) * x
                                    Next
                                End If
                            End If
                        End If
                        End If
                End If
            End If
        End If
        Next
        
        For i = 1 To SMFID.XmlDataQuery("/SMFID/RedundantFunctionalInputs/Number").Value
            u = SMFID.XmlDataQuery("/SMFID/RedundantFunctionalInputs/FunctionInput/I")(i).Value
            If u <= nStates Then 'PFIDInputs.Columns.Count Then
                    If u = 0 Then
                        iia = 1
                        iib = ns
                    Else
                        iia = u
                        iib = u
                    End If
                    If onlyrow = 0 Or u = onlyrow Then
                        If onlyrow > 0 Then
                            u = 1
                            iia = 1
                            iib = 1
                        End If
                        v = SMFID.XmlDataQuery("/SMFID/RedundantFunctionalInputs/FunctionInput/J")(i).Value
                        fi = SMFID.XmlDataQuery("/SMFID/RedundantFunctionalInputs/FunctionInput/FlowRef")(i).Value + 1
                    If fi <= nFlows + 1 Then
                    
                        If fi = 0 Then fi = nFlows + 2
                    
                        x = PFIDInputs(PFIDInputsIndex, SMFID.XmlDataQuery("/SMFID/RedundantFunctionalInputs/FunctionInput/InputReference")(i).Value).Value
                        si = SMFID.XmlDataQuery("/SMFID/RedundantFunctionalInputs/FunctionInput/OpZeroOrOne")(i).Value
                        If v = 0 Then
                        If si = 0 Then
                            For ii = iia To iib
                            For jj = 1 To ns
                                vrc(fi)(ii, jj) = vrc(fi)(ii, jj) + x
                            Next
                            Next
                        Else
                            For ii = iia To iib
                            For jj = 1 To ns
                                vrc(fi)(ii, jj) = vrc(fi)(ii, jj) * x
                            Next
                            Next
                        End If
                        Else
                        If si = 0 Then
                            For ii = iia To iib
                                vrc(fi)(ii, v) = vrc(fi)(ii, v) + x
                            Next
                        Else
                            For ii = iia To iib
                                vrc(fi)(ii, v) = vrc(fi)(ii, v) * x
                            Next
                        End If
                        End If
                    End If
                
                End If
            
            End If
        Next
        
        
    End If
    
    nflowstemp = 2
    If nFlows > 0 Then
        nflowstemp = nFlows + 2
    Else
        nflowstemp = 1
    End If
        
    
    For i = 1 To m1
        u = i
        If onlyrow = 0 Or u = onlyrow Then
            If onlyrow > 0 Then u = 1
            If TopologySums(i) > 0 Then
                For j = 1 To n1
                    If Topology.Cells(i, j).Value > 0 Then
                        For k = 1 To nflowstemp
                            If k = 1 Then  ' only for the unit case
                                vrc(1)(u, j) = Exp(mnmx(10, -10, vrc(1)(u, j)))
                                If BaseOffsets(1) = 0 Then
                                    If (Not (IsEmpty(BaseOdds.Cells(i, j)))) And (BaseOdds.Cells(i, j).Value > 0) Then
                                        vrc(1)(u, j) = vrc(1)(u, j) * BaseOdds.Cells(i, j)
                                    Else
                                        If u <> j Then vrc(1)(u, j) = 1E-20
                                    End If
                                Else
                                    If (Not (IsEmpty(BaseOdds.Cells(i, j).Offset(BaseOffsets(1) * ns, 0)))) And (BaseOdds.Cells(i, j).Offset(BaseOffsets(1) * ns, 0).Value > 0) Then
                                        vrc(1)(u, j) = vrc(1)(u, j) * BaseOdds.Cells(i, j).Offset(BaseOffsets(1) * ns, 0)
                                    Else
                                        If u <> j Then vrc(1)(u, j) = 1E-20
                                    End If
                                End If
                            ElseIf k = nFlows + 2 Then
                            
                                    
                                vrc(k)(u, j) = vrc(1)(u, j) * Exp(mnmx(10, -10, vrc(k)(u, j)))
                                If BaseOffsets(nFlows + 2) = 0 Then
                                    If OddsBias.Cells(i, j).Value <> 0 And i <> j Then
                                        vrc(k)(u, j) = vrc(k)(u, j) * Exp(mnmx(10, -10, OddsBias.Cells(i, j)))
                                    Else
                                        If u <> j Then vrc(k)(u, j) = 0.0000001
                                    End If
                                Else
                                    If OddsBias.Cells(i, j).Offset(BaseOffsets(nFlows + 2) * ns, 0).Value <> 0 And i <> j Then
                                        vrc(k)(u, j) = vrc(k)(u, j) * Exp(mnmx(10, -10, OddsBias.Cells(i, j).Offset(BaseOffsets(nFlows + 2) * ns, 0)))
                                    Else
                                        If u <> j Then vrc(k)(u, j) = 0.0000001
                                    End If
                                End If
                            
                            Else
                            
                                If BaseOffsets(k) = 0 Then
                                    If vrc(k)(u, j) <> 0 Then
                                        vrc(k)(u, j) = Exp(vrc(k)(u, j)) * Range(s & "BaseFlow" & k - 1).Cells(i, j).Value
                                    Else
                                        vrc(k)(u, j) = Range(s & "BaseFlow" & k - 1).Cells(i, j).Value
                                    End If
                                Else
                                    If vrc(k)(u, j) <> 0 Then
                                        vrc(k)(u, j) = Exp(vrc(k)(u, j)) * Range(s & "BaseFlow" & k - 1).Cells(i, j).Offset(BaseOffsets(k) * ns, 0).Value
                                    Else
                                        vrc(k)(u, j) = Range(s & "BaseFlow" & k - 1).Cells(i, j).Offset(BaseOffsets(k) * ns, 0).Value
                                    End If
                                End If
                            End If
                        Next
                    Else
                        For k = 1 To nflowstemp
                            vrc(k)(u, j) = 0
                        Next
                    End If
                Next
            End If
        End If
    Next
    
End If

x = vrc(1)(1, 2)

PSMFIDOddsFillerWithBase = vrc

End Function
Function PMultBySMFID(ByRef arg1 As Range, ByRef PFIDInputs As Range, ByVal NMFID As String, _
    Optional SS = "SMStateSpaceSpec", _
    Optional SF = "SMStocksAndFlowsSpec", _
    Optional lastarg = "") As Variant

Dim SMSS, SMSF, SMFID As Worksheet
Set SMFID = Sheets(NMFID)
Set SMSS = Sheets(SS)
Set SMSF = Sheets(SF)

Dim i, j, k, l, s, n, list1, list2, nStates, nStages, nStocks, nFlows
s = NMFID

nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
nStages = SMSS.XmlDataQuery("/SMStateSpace/Stages/Number").Value

nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
snstocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value
nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
mnflows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value

Set Topology = Range(s & "Topology")
Dim TopologyColumnSums, TopologyRowSums
ReDim TopologySums(nStates) As Double
ReDim TopologyColumnSums(nStates) As Double
ReDim TopologyRowSums(nStates) As Double
For i = 1 To nStates
    TopologyColumnSums(i) = 0
    TopologyRowSums(i) = 0
    For j = 1 To nStates

    If Range(s & "Topology").Cells(i, j) > 0 Then
        TopologyColumnSums(i) = TopologyColumnSums(i) + 1
    End If
    If Range(s & "Topology").Cells(i, j) > 0 Then
        TopologyRowSums(i) = TopologyRowSums(i) + 1
    End If

        'TopologyColumnSums(i) = TopologyColumnSums(i) + Range(s & "Topology").Cells(i, j).Value
        'TopologyRowSums(i) = TopologyRowSums(i) + Range(s & "Topology").Cells(j, i).Value
        'TopologyColumnSums(i) = TopologyColumnSums(i) + 1 * (Range(s & "Topology").Cells(i, j).Value > 0)
        'TopologyRowSums(i) = TopologyRowSums(i) + 1 * (Range(s & "Topology").Cells(j, i).Value > 0)
    Next
Next

    Dim rc As Variant
    
If 1 Then

    Dim om As Variant
    
    m1 = PFIDInputs.Rows.Count
    n1 = arg1.Columns.Count
    m2 = nStates
    n2 = m2
    
    ReDim rc(m1, n2) As Double
    
    
    If n1 = m2 Then
    
    
        For i = 1 To m1
        
        If SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/BaseSetInd")(1) = -1 Then
            NullIN = PFIDInputs(i, 1)
        Else
            NullIN = 0
        End If
        
        om = PSMFIDOddsFillerWithBase(NMFID, PFIDInputs, SS, SF, 0, 0, i)(1)
        om = RowNormIt(om, m2, m2)
        For j = 1 To n2
        If TopologyRowSums(j) > 0 Then
        For k = 1 To n1
            If k = 1 And NullIN <> 0 Then
If i = 1 Then
                rc(i, j) = rc(i, j) + (arg1(i, k) + NullIN) * om(k, j)
Else
                rc(i, j) = rc(i, j) + (rc(i - 1, k) + NullIN) * om(k, j)
End If

            Else
If i = 1 Then
                rc(i, j) = rc(i, j) + arg1(i, k) * om(k, j)
Else
                rc(i, j) = rc(i, j) + rc(i - 1, k) * om(k, j)
End If
            End If
        Next
        End If
        Next
        Next
        PMultBySMFID = rc
    
    End If

End If


End Function
Function PMultByFIDWithCF(ByRef arg1 As Range, ByRef PFIDInputs As Range, ByRef PFID As Range, _
    Optional SS = "StageAndStateSpec", Optional SF = "StockAndFlowSpec", Optional PickUpOnlyPrevStage = False) As Variant

Dim asu
asu = Application.ScreenUpdating
Application.ScreenUpdating = False

'Dim s As String
'
's = PFID.Cells(1, 2).Value
'
'Dim TopologyWSums As Range
'Set TopologyWSums = Range(s & "TopologyWSums")

    Dim rc As Variant
    
Call PMultByFIDWithCFSubV3(rc, SS, SF, arg1, PFIDInputs, True, PickUpOnlyPrevStage)
'Call PMultByFIDWithCFSub(rc, SS, SF, arg1, PFIDInputs, PickUpOnlyPrevStage)

'PMultByFIDWithCF = rc
'rc = 3
PMultByFIDWithCF = rc
x = rc(1, 3)
x = 1

Application.ScreenUpdating = asu

End Function
Sub PMultByFIDSubV3( _
        ByVal SS As String, _
        ByVal SF As String, _
        ByRef IndexSet As Range, _
        Optional PickUpOnlyPrevStage = False)

    ', ByRef PFIDInputs As Range, ByRef PFID As Range)



If 1 Then
        Application.CalculateFull
End If
        calcprior = Application.Calculation
        Application.Calculation = xlCalculationManual


        Dim rc As Variant
        Dim rInputDistribution As Range

        Call PMultByFIDWithCFSubV3(rc, SS, SF, _
                rInputDistribution, _
                IndexSet, _
                False, _
                PickUpOnlyPrevStage, _
                False)
 
        Application.Calculation = calcprior

End Sub

Sub PMultByFIDWithCFSubV3( _
        ByRef rc As Variant, _
        ByVal SS As String, _
        ByVal SF As String, _
        ByRef rInputDistribution As Range, _
        ByRef rInputVector As Range, _
        Optional CalledByFunction = True, _
        Optional PickUpOnlyPrevStage = False, _
        Optional OnlyStage1 = True)



Dim asu
asu = Application.ScreenUpdating
Application.ScreenUpdating = False


On Error GoTo CatchIt

Dim i, j, k, l, n, nStates, nStages, nStocks, nFlows As Integer
Dim s As String
Dim list2



Dim SMSS, SMSF, SMFID As Worksheet
Set SMSS = Sheets(SS)
Set SMSF = Sheets(SF)

Dim SMSSMap, SMSFMap As XmlMap
Set SMSSMap = ActiveWorkbook.XmlMaps("SMStateSpace")
Set SMSFMap = ActiveWorkbook.XmlMaps("SMStocksAndFlows")




nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
nStages = SMSS.XmlDataQuery("/SMStateSpace/Stages/Number").Value
If OnlyStage1 Then
        nStages = 1
End If


nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
snstocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value
nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
mnflows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value

Dim StageMneumonic As Range
Set StageMneumonic = SMSS.XmlDataQuery("/SMStateSpace/Stages/Stage/Mneumonic")
    
Dim Topology
ReDim Topology(nStages) As Range
Dim TopologyColumnSums, TopologyRowSums
ReDim TopologyColumnSums(nStages, nStates) As Integer
ReDim TopologyRowSums(nStages, nStates) As Integer

Dim TopologySparseInd
ReDim TopologySparseInd(nStages) As Integer
Dim TopologySparseIndexTags
ReDim TopologySparseIndexTags(nStages) As Range


For k = 1 To nStages
    s = StageMneumonic(k)
    If k = 1 Then
        Set SMFID = Sheets(s)
    End If
    Set Topology(k) = Range(s & "Topology")
    If SMFID.XmlDataQuery("/SMMatrix/ProvidesNonZeroCoords", "", _
            ActiveWorkbook.XmlMaps(s & "Topology")).Value = 1 Then
        TopologySparseInd(k) = SMFID.XmlDataQuery("/SMMatrix/NonZeroElements/Number", "", _
            ActiveWorkbook.XmlMaps(s & "Topology")).Value
        Set TopologySparseIndexTags(k) = SMFID.XmlDataQuery("/SMMatrix/NonZeroElements/NonZeroCoordinates/NonZeroCoordinate/@Position", "", _
            ActiveWorkbook.XmlMaps(s & "Topology"))(1)
        Set TopologySparseIndexTags(k) = Range(s & "!" & _
            TopologySparseIndexTags(k).Offset(0, 1).Address & _
            ":" & _
            TopologySparseIndexTags(k).Offset(TopologySparseInd(k), 2).Address)
        
        TSITagsAddress = TopologySparseIndexTags(k).Address
    Else
        TopologySparseInd(k) = 0
        For i = 1 To nStates
            TopologyColumnSums(k, i) = 0
            TopologyRowSums(k, i) = 0
            For j = 1 To nStates
            If Topology(k).Cells(j, i).Value > 0 Then
                TopologyColumnSums(k, i) = TopologyColumnSums(k, i) + 1
                TopologyRowSums(k, i) = TopologyRowSums(k, i) + 1
            End If
            Next
        Next
    End If

Next

ReDim rc(rInputVector.Rows.Count, (mnstocks + nFlows + 1) * nStates) As Double

Dim tempstring As String
'Dim PUFCT As Range
'tempstring = Range(SS & "PickUpFilterCornerTag").Text
'Set PUFCT = Range(tempstring)
'Dim SADSI As Range
'tempstring = Range(Stocks & "AggDiffSourcesIndex").Text
'Set SADSI = Range(tempstring)
'Dim SADST As Range
'tempstring = Range(Stocks & "AggDiffSourcesType").Text
'Set SADST = Range(tempstring)
'Dim SADSS As Range
'tempstring = Range(Stocks & "AggDiffSourcesScale").Text
'Set SADSS = Range(tempstring)

Dim PUFCT
ReDim PUFCT(nStages, nStages, nStates) As Boolean

For i = 1 To nStages
For j = 1 To nStages
For k = 1 To nStates
    If i = j Then
        PUFCT(i, j, k) = True
    Else
        PUFCT(i, j, k) = False
    End If
Next
Next
Next

For i = 1 To SMSS.XmlDataQuery("/SMStateSpace/Bridges/Number").Value
    If SMSS.XmlDataQuery("/SMStateSpace/Bridges/Bridge/Type")(i) = "PickUp" Then
       PUFCT( _
            SMSS.XmlDataQuery("/SMStateSpace/Bridges/Bridge/From")(i).Value, _
            SMSS.XmlDataQuery("/SMStateSpace/Bridges/Bridge/To")(i).Value, _
            SMSS.XmlDataQuery("/SMStateSpace/Bridges/Bridge/StatePosition")(i).Value _
        ) = True
    End If
Next


Dim m, indexii


Dim arg1, uarg1, uarg
ReDim arg1(nStates) As Double
ReDim uarg1(nStages) As Variant
ReDim uarg(2) As Variant

For i = 1 To nStates
    arg1(i) = 0
Next
zarg = arg1

For k = 1 To nStates
If CalledByFunction Then
        If rInputDistribution(1, k).Value > 0 Then
                arg1(k) = rInputDistribution(1, k).Value
        Else
                arg1(k) = 0
        End If
Else
        arg1(k) = Range("AllUnits!B100:" & _
                fColumnFromCode(1 + nStates) & 100).Cells(1, k).Value
End If
Next

For k = 1 To nStages
    uarg1(k) = zarg
Next
uarg(2) = uarg1
uarg1(1) = arg1
uarg(1) = uarg1


Dim sarg1, sarg
ReDim sarg1(nStages, nStocks) As Variant
ReDim sarg(2) As Variant
For i = 1 To nStages
For j = 1 To nStocks
    sarg1(i, j) = zarg
Next
Next
zsarg = sarg1
sarg(2) = sarg1

i = 1
If CalledByFunction Then
        For j = 1 To mnstocks
                For k = 1 To nStates
                sarg1(i, j)(k) = rInputDistribution(1, k + nStates * j).Value
                Next
        Next
Else
        For j = 1 To snstocks
                temps = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Mneumonic")(j)
                For k = 1 To nStates
                        sarg1(i, j)(k) = _
                                Range(temps & "!" & _
                                fColumnFromCode(1 + nStates * (i - 1) + k) & _
                                100).Value
                Next
        Next
End If
sarg(1) = sarg1

Dim farg1, farg
ReDim farg1(nStages, nFlows) As Variant
ReDim farg(2) As Variant
For i = 1 To nStages
For j = 1 To nFlows
    farg1(i, j) = zarg
Next
Next
zfarg = farg1
farg(1) = farg1
farg(2) = farg1


Dim indexi As Range

Dim PFID As Range

Dim TopologyWSums As Range

wfpayments = zarg
wfpaymentsreduced = 0
wfrtb = zarg
wfrtbreduced = 0

one = 2
two = 1

If Not CalledByFunction Then
        Range("AllUnits!B" & rInputVector(1, 1).Row & ":B" & rInputVector(1).Row + 120).Clear
End If




Dim lsheet As Worksheet

Dim SMneumonic, SType, SLaterUse, STreatment, SFOutput, SMOutput As Range
Dim SNumberOfBases, SBase1, SBase2, SBase3, SBase4, SBase5, SBase6 As Range
Set SMneumonic = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Mneumonic")
Set SType = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Type")
Set SLaterUse = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/LaterUse")
Set STreatment = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Treatment")
Set SFOutput = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/SOutput")
Set SMOutput = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/MOutput")
Set SNumberOfBases = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/NumberOfBases")
Set SBase1 = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Base1Type")
Set SBase2 = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Base2Type")
Set SBase3 = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Base3Type")
Set SBase4 = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Base4Type")
Set SBase5 = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Base5Type")
Set SBase6 = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Base6Type")

Dim FMneumonic, FPrePost, FAorS, FRollWeighting As Range
Dim FNumberOfBases, FBase1, FBase2, FBase3, FBase4, FBase5, FBase6 As Range
Set FMneumonic = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic")
Set FPrePost = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/PrePost")
Set FAorS = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/AorS")
Set FRollWeighting = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/RollWeighting")
Set FNumberOfBases = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/NumberOfBases")
Set FBase1 = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Base1Type")
Set FBase2 = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Base2Type")
Set FBase3 = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Base3Type")
Set FBase4 = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Base4Type")
Set FBase5 = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Base5Type")
Set FBase6 = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Base6Type")


Dim Orders As Range
Set Orders = SMSF.XmlDataQuery("/SMStocksAndFlows/Orders/Order/@Position")

Dim firstrun, runtake As Integer
firstrun = 1
runtake = 1

For indexii = 1 To rInputVector.Rows.Count

    
    
    If two = 1 Then
        one = 1
        two = 2
    Else
        one = 2
        two = 1
    End If
    

For indexs = 1 To nStages
    
    wfpayments = zarg
    wfrtb = zarg
    
    s = StageMneumonic(indexs)
      
    Set lsheet = Sheets(s)
    
    ninputs = Sheets(s).XmlDataQuery("/SMFID/FunctionalInputs/Number").Value
    tmpoutarg = zarg
    tmpinarg = zarg
    
    
    Dim om As Variant

    m2 = nStates
    n2 = m2
    
    
    Dim InputsLag1(40) As Double
    
    runtake = 0
    If firstrun = 1 Or nStages > 1 Then runtake = 1
    
    If runtake = 0 Then
    
        If CalledByFunction Then
            For i = 1 To rInputVector.Columns.Count
                If rInputVector(indexii, i) <> InputsLag1(i) Then
                    runtake = 1
                    Exit For
                End If
            Next
        Else
            For i = 1 To ninputs
                If Range(s & "Inputs!E" & rInputVector(indexii, 1).Row).Offset(0, i).Value <> InputsLag1(i) Then
                    runtake = 1
                    Exit For
                End If
            Next
        End If
    
    End If
    
 '   runtake = 1
    
    If runtake = 1 Then
    
        firstrun = 0
        If CalledByFunction Then
            For i = 1 To rInputVector.Columns.Count
                InputsLag1(i) = rInputVector(indexii, i)
            Next
        Else
            For i = 1 To ninputs
                InputsLag1(i) = Range(s & "Inputs!E" & rInputVector(indexii, 1)).Offset(0, i).Value
            Next
        End If
    
        ' added one column to the inputs page for the default age
        If CalledByFunction Then
            om = PSMFIDOddsFillerWithBase(s, _
                    rInputVector, SS, SF, 0, mnflows, indexii)
        Else
            om = PSMFIDOddsFillerWithBase(s, _
                    Range(s & "Inputs!F" & rInputVector(indexii, 1).Row & _
                    ":" & fColumnFromCode(ninputs + 5) & rInputVector(indexii, 1).Row), _
                    SS, SF, 0, mnflows, 1)
        End If
        
        omu = RowNormIt(om(1), m2, m2)
        omub = RowNormIt(om(mnflows + 2), m2, m2)
    
    End If

    tmpinarg = zarg
        
    For i = 1 To nStates
        For j = 1 To nStages
            If PUFCT(j, indexs, i) Then
                tmpinarg(i) = tmpinarg(i) + uarg(one)(j)(i)
            End If
        Next
    Next
    
    If indexs = 1 Then
    If SMFID.XmlDataQuery("/SMFID/FunctionalInputs/FunctionInput/BaseSetInd")(1) = -1 Then
        If CalledByFunction Then
            tmpinarg(1) = tmpinarg(1) + rInputVector(indexii, 1).Value
        Else
            tmpinarg(1) = tmpinarg(1) + _
                    Range(s & "Inputs!F" & rInputVector(indexii, 1).Row).Value
        End If
    End If
    End If
    
    uarg(two)(indexs) = zarg
    If TopologySparseInd(indexs) = 0 Then
        i = 1
        For j = 1 To n2
            If TopologyRowSums(indexs, j) > 0 Then
                For k = 1 To n2
                If Topology(indexs)(k, j) > 0 Then
                    uarg(two)(indexs)(j) = uarg(two)(indexs)(j) + tmpinarg(k) * omu(k, j)
                End If
                Next
            End If
        Next
    Else
    
        For i = 1 To TopologySparseInd(indexs)
            k = TopologySparseIndexTags(indexs).Cells(i, 1)
            j = TopologySparseIndexTags(indexs).Cells(i, 2)
            uarg(two)(indexs)(j) = uarg(two)(indexs)(j) + tmpinarg(k) * omu(k, j)
        Next
    
    End If
    
    

    'uarg(two)(2)(2) = 2
    
    sarg2 = zsarg
    farg2 = zsarg


    For l = 2 To nStocks + nFlows + 1
        tmparg = zarg
        tmpinsarg = zarg
        
        m = Orders(l, 1).Offset(0, 2).Value
        n = Orders(l, 1).Offset(0, 3).Value
        
        If m = 2 Then ' a flow
        
            
            Select Case FRollWeighting(n, 1)
            
                Case "BalanceBasisUnitRoll", "BalanceBasisUnitRollBounded", _
                    "BalanceBasisBalanceBiasedRoll", "BalanceBasisBalanceBiasedRollBounded", _
                    "SumOfBases"
                
                    If FPrePost(n, 1) = "Pre" Then
                        For i = 1 To nStates
                            For j = 1 To nStages
                                If PUFCT(j, indexs, i) Then
                                
                                   If FBase1(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, FBase1(n, 1).Offset(0, 2))(i) * FBase1(n, 1).Offset(0, 3)
                                   If FBase2(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, FBase2(n, 1).Offset(0, 2))(i) * FBase2(n, 1).Offset(0, 3)
                                   If FBase3(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, FBase3(n, 1).Offset(0, 2))(i) * FBase3(n, 1).Offset(0, 3)
                                   If FBase4(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, FBase4(n, 1).Offset(0, 2))(i) * FBase4(n, 1).Offset(0, 3)
                                   If FBase5(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, FBase5(n, 1).Offset(0, 2))(i) * FBase5(n, 1).Offset(0, 3)
                                   If FBase6(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, FBase6(n, 1).Offset(0, 2))(i) * FBase6(n, 1).Offset(0, 3)
                                            
                                End If
                            Next
                        Next
                    ElseIf FPrePost(n, 1) = "Post" Then
                        For i = 1 To nStates
                            For j = 1 To nStages
                                If PUFCT(j, indexs, i) Then
                                
                                   If FBase1(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase1(n, 1).Offset(0, 2))(i) * FBase1(n, 1).Offset(0, 3)
                                   If FBase1(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase1(n, 1).Offset(0, 2))(i) * FBase1(n, 1).Offset(0, 3)
                                   If FBase2(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase2(n, 1).Offset(0, 2))(i) * FBase2(n, 1).Offset(0, 3)
                                   If FBase2(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase2(n, 1).Offset(0, 2))(i) * FBase2(n, 1).Offset(0, 3)
                                   If FBase3(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase3(n, 1).Offset(0, 2))(i) * FBase3(n, 1).Offset(0, 3)
                                   If FBase3(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase3(n, 1).Offset(0, 2))(i) * FBase3(n, 1).Offset(0, 3)
                                   If FBase4(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase4(n, 1).Offset(0, 2))(i) * FBase4(n, 1).Offset(0, 3)
                                   If FBase4(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase4(n, 1).Offset(0, 2))(i) * FBase4(n, 1).Offset(0, 3)
                                   If FBase5(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase5(n, 1).Offset(0, 2))(i) * FBase5(n, 1).Offset(0, 3)
                                   If FBase5(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase5(n, 1).Offset(0, 2))(i) * FBase5(n, 1).Offset(0, 3)
                                   If FBase6(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase6(n, 1).Offset(0, 2))(i) * FBase6(n, 1).Offset(0, 3)
                                   If FBase6(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase6(n, 1).Offset(0, 2))(i) * FBase6(n, 1).Offset(0, 3)
                                            
                                End If
                            Next
                        Next
                    End If
                    
                Case "WaterFallPaydown"
                
                    If FPrePost(n, 1) = "Post" Then
                        For i = 1 To nStates
                            For j = 1 To nStages
                                If PUFCT(j, indexs, i) Then
                                
                                   If FBase1(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase1(n, 1).Offset(0, 2))(i) * FBase1(n, 1).Offset(0, 3)
                                   If FBase1(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase1(n, 1).Offset(0, 2))(i) * FBase1(n, 1).Offset(0, 3)
                                   If FBase2(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase2(n, 1).Offset(0, 2))(i) * FBase2(n, 1).Offset(0, 3)
                                   If FBase2(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase2(n, 1).Offset(0, 2))(i) * FBase2(n, 1).Offset(0, 3)
                                   If FBase3(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase3(n, 1).Offset(0, 2))(i) * FBase3(n, 1).Offset(0, 3)
                                   If FBase3(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase3(n, 1).Offset(0, 2))(i) * FBase3(n, 1).Offset(0, 3)
                                   If FBase4(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase4(n, 1).Offset(0, 2))(i) * FBase4(n, 1).Offset(0, 3)
                                   If FBase4(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase4(n, 1).Offset(0, 2))(i) * FBase4(n, 1).Offset(0, 3)
                                   If FBase5(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase5(n, 1).Offset(0, 2))(i) * FBase5(n, 1).Offset(0, 3)
                                   If FBase5(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase5(n, 1).Offset(0, 2))(i) * FBase5(n, 1).Offset(0, 3)
                                   If FBase6(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, FBase6(n, 1).Offset(0, 2))(i) * FBase6(n, 1).Offset(0, 3)
                                   If FBase6(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, FBase6(n, 1).Offset(0, 2))(i) * FBase6(n, 1).Offset(0, 3)
                                            
                                End If
                            Next
                        Next
                    End If
                
                Case Else
                
                    tmpinsarg = zarg
            
            End Select
            
            
            
            
            Select Case FRollWeighting(n, 1)
            
                Case "UnitBasisUnitRoll"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omu(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
    
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omu(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                Case "UnitBasisUnitRollBounded"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omu(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omu(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                    For k = 1 To n2
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                        If tmparg(k) > wfrtb(k) Then tmparg(k) = wfrtb(k)
                        wfrtb(k) = wfrtb(k) - tmparg(k)
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                    Next
                
                Case "UnitBasisBalanceBiasedRoll"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omub(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omub(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                Case "UnitBasisBalanceBiasedRollBounded"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omub(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinarg(k) * omub(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                    For k = 1 To n2
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                        If tmparg(k) > wfrtb(k) Then tmparg(k) = wfrtb(k)
                        wfrtb(k) = wfrtb(k) - tmparg(k)
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                    Next
                
                Case "BalanceBasisUnitRoll"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omu(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omu(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                Case "BalanceBasisUnitRollBounded"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omu(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omu(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                    For k = 1 To n2
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                        If tmparg(k) > wfrtb(k) Then tmparg(k) = wfrtb(k)
                        wfrtb(k) = wfrtb(k) - tmparg(k)
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                    Next
                
                Case "BalanceBasisBalanceBiasedRoll"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omub(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omub(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                Case "BalanceBasisBalanceBiasedRollBounded"
                
                    If TopologySparseInd(indexs) = 0 Then
                        For j = 1 To n2
                            For k = 1 To n2
                            If Topology(indexs)(k, j) > 0 Then
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omub(k, j) * om(n + 1)(k, j)
                            End If
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * omub(k, j) * om(n + 1)(k, j)
                        Next
                    
                    End If
                
                    For k = 1 To n2
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                        If tmparg(k) > wfrtb(k) Then tmparg(k) = wfrtb(k)
                        wfrtb(k) = wfrtb(k) - tmparg(k)
                        If wfrtb(k) < 0 Then wfrtb(k) = 0
                    Next
                
                Case "SumOfBases"
                
                    tmparg = tmpinsarg
                    
                Case "WaterFallPaydown"
                
                    tmparg = tmpinsarg
                    
                    For k = 1 To n2
                    
                        If tmparg(k) < 0 Then tmparg(k) = 0
                        If wfpayments(k) > 0 Then
                            If tmparg(k) > wfpayments(k) Then
                                tmparg(k) = wfpayments(k)
                                wfpayments(k) = 0
                            Else
                                wfpayments(k) = wfpayments(k) - tmparg(k)
                            End If
                        Else
                            tmparg(k) = 0
                        End If
                    Next
            
                Case Else
            
            End Select
            
            
            If FAorS(n, 1) = "S" Then
                For k = 1 To n2
                    wfpayments(k) = wfpayments(k) + tmparg(k)
                Next
            End If

            farg(two)(indexs, n) = tmparg

        Else
            
            Dim lomub
            
            Select Case STreatment(n, 1)
                Case "UR"
                    lomub = omu
                Case "BUR"
                    lomub = omub
                Case Else
                    lomub = omub
            End Select
            
            Select Case SType(n, 1)
            
                Case "Agg", "SumOfBases"
                
                    For i = 1 To nStates
                        For j = 1 To nStages
'                            If PUFCT(j, indexs, i) Then
                            
                               If SBase1(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, SBase1(n, 1).Offset(0, 2))(i) * SBase1(n, 1).Offset(0, 3)
                               If SBase1(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, SBase1(n, 1).Offset(0, 2))(i) * SBase1(n, 1).Offset(0, 3)
                               If SBase2(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, SBase2(n, 1).Offset(0, 2))(i) * SBase2(n, 1).Offset(0, 3)
                               If SBase2(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, SBase2(n, 1).Offset(0, 2))(i) * SBase2(n, 1).Offset(0, 3)
                               If SBase3(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, SBase3(n, 1).Offset(0, 2))(i) * SBase3(n, 1).Offset(0, 3)
                               If SBase3(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, SBase3(n, 1).Offset(0, 2))(i) * SBase3(n, 1).Offset(0, 3)
                               If SBase4(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, SBase4(n, 1).Offset(0, 2))(i) * SBase4(n, 1).Offset(0, 3)
                               If SBase4(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, SBase4(n, 1).Offset(0, 2))(i) * SBase4(n, 1).Offset(0, 3)
                               If SBase5(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, SBase5(n, 1).Offset(0, 2))(i) * SBase5(n, 1).Offset(0, 3)
                               If SBase5(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, SBase5(n, 1).Offset(0, 2))(i) * SBase5(n, 1).Offset(0, 3)
                               If SBase6(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(two)(j, SBase6(n, 1).Offset(0, 2))(i) * SBase6(n, 1).Offset(0, 3)
                               If SBase6(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(two)(j, SBase6(n, 1).Offset(0, 2))(i) * SBase6(n, 1).Offset(0, 3)
                                        
'                            End If
                        Next
                    Next
                    
                Case "SLR", "Resid"
                
                    For i = 1 To nStates
                        For j = 1 To nStages
                            If PUFCT(j, indexs, i) Then
                            
                               If SBase1(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, SBase1(n, 1).Offset(0, 2))(i) * SBase1(n, 1).Offset(0, 3)
                               'If SBase1(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(one)(j, SBase1(n, 1).Offset(0, 2))(i) * SBase1(n, 1).Offset(0, 3)
                               If SBase2(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, SBase2(n, 1).Offset(0, 2))(i) * SBase2(n, 1).Offset(0, 3)
                               'If SBase2(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(one)(j, SBase2(n, 1).Offset(0, 2))(i) * SBase2(n, 1).Offset(0, 3)
                               If SBase3(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, SBase3(n, 1).Offset(0, 2))(i) * SBase3(n, 1).Offset(0, 3)
                               'If SBase3(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(one)(j, SBase3(n, 1).Offset(0, 2))(i) * SBase3(n, 1).Offset(0, 3)
                               If SBase4(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, SBase4(n, 1).Offset(0, 2))(i) * SBase4(n, 1).Offset(0, 3)
                               'If SBase4(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(one)(j, SBase4(n, 1).Offset(0, 2))(i) * SBase4(n, 1).Offset(0, 3)
                               If SBase5(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, SBase5(n, 1).Offset(0, 2))(i) * SBase5(n, 1).Offset(0, 3)
                               'If SBase5(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(one)(j, SBase5(n, 1).Offset(0, 2))(i) * SBase5(n, 1).Offset(0, 3)
                               If SBase6(n, 1) = 1 Then tmpinsarg(i) = tmpinsarg(i) + sarg(one)(j, SBase6(n, 1).Offset(0, 2))(i) * SBase6(n, 1).Offset(0, 3)
                               'If SBase6(n, 1) = 2 Then tmpinsarg(i) = tmpinsarg(i) + farg(one)(j, SBase6(n, 1).Offset(0, 2))(i) * SBase6(n, 1).Offset(0, 3)
                                        
                            End If
                        Next
                    Next
                
                Case Else
                
            End Select
            
            Select Case SType(n, 1)
            
                Case "Agg"
                    
                    tmparg = tmpinsarg
                
                Case "SumOfBases", "ScaledSum"
                
                    tmparg = tmpinsarg
                    
                Case "SLR"
                            
                    If TopologySparseInd(indexs) = 0 Then
                        For k = 1 To n2
                            For j = 1 To n2
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * lomub(k, j)
                            Next
                        Next
                    Else
                        
                        For i = 1 To TopologySparseInd(indexs)
                            k = TopologySparseIndexTags(indexs).Cells(i, 1)
                            j = TopologySparseIndexTags(indexs).Cells(i, 2)
                                tmparg(j) = tmparg(j) + tmpinsarg(k) * lomub(k, j)
                        Next
                    
                    End If
                    
                    For i = 1 To nStates
                            
                        If SBase1(n, 1) = 2 Then tmparg(i) = tmparg(i) + farg(two)(indexs, SBase1(n, 1).Offset(0, 2))(i) * SBase1(n, 1).Offset(0, 3)
                        If SBase2(n, 1) = 2 Then tmparg(i) = tmparg(i) + farg(two)(indexs, SBase2(n, 1).Offset(0, 2))(i) * SBase2(n, 1).Offset(0, 3)
                        If SBase3(n, 1) = 2 Then tmparg(i) = tmparg(i) + farg(two)(indexs, SBase3(n, 1).Offset(0, 2))(i) * SBase3(n, 1).Offset(0, 3)
                        If SBase4(n, 1) = 2 Then tmparg(i) = tmparg(i) + farg(two)(indexs, SBase4(n, 1).Offset(0, 2))(i) * SBase4(n, 1).Offset(0, 3)
                        If SBase5(n, 1) = 2 Then tmparg(i) = tmparg(i) + farg(two)(indexs, SBase5(n, 1).Offset(0, 2))(i) * SBase5(n, 1).Offset(0, 3)
                        If SBase6(n, 1) = 2 Then tmparg(i) = tmparg(i) + farg(two)(indexs, SBase6(n, 1).Offset(0, 2))(i) * SBase6(n, 1).Offset(0, 3)
                                        
                    Next
                    
                Case "Resid"
                
                    tmparg = zarg
                    tmparg = wfpayments
                
                Case Else
            
            End Select
            
            
            If SLaterUse(n, 1) = "Bounder" Then
                wfrtb = tmparg
            End If

            sarg(two)(indexs, n) = tmparg

            stuff = 1
            
        End If

    Next
    
    Next
    
    
    If CalledByFunction Then
        
        For indexs = 1 To nStages
            For j = 1 To nStates
                
                rc(indexii, j) = uarg(two)(indexs)(j)
                        
                For k = 1 To mnstocks
                    rc(indexii, k * nStates + j) = sarg(two)(indexs, k)(j)
                Next
                For k = 1 To nFlows '- mnflows
                    rc(indexii, (k + mnstocks) * nStates + j) = _
                        farg(two)(indexs, k)(j)  '+mnflows)(j)
                Next
            
            Next
        Next
    
    Else


        For i = 1 To nStages
        
        If nStages = 1 Then
        
            Range("AllUnits!" & _
                fColumnFromCode(1 + 1) & rInputVector(indexii, 1).Row & ":" & _
                fColumnFromCode(1 + nStates * (i)) & rInputVector(indexii, 1).Row _
                ) = uarg(two)(i)
            For j = 1 To snstocks
                Range(SMneumonic(j, 1) & "!" & _
                    fColumnFromCode(1 + 1) & rInputVector(indexii, 1).Row & ":" & _
                    fColumnFromCode(1 + nStates * (i)) & rInputVector(indexii, 1).Row _
                    ) = sarg(two)(i, j)
            Next
            For j = 1 To nFlows
                Range(FMneumonic(j, 1) & "!" & _
                    fColumnFromCode(1 + 1) & rInputVector(indexii, 1).Row & ":" & _
                    fColumnFromCode(1 + nStates * (i)) & rInputVector(indexii, 1).Row _
                    ) = farg(two)(i, j)
            Next
        
        End If
        
            Range("AllUnits!" & _
                fColumnFromCode(1 + nStates * i + 1) & rInputVector(indexii, 1).Row & ":" & _
                fColumnFromCode(1 + nStates * (i + 1)) & rInputVector(indexii, 1).Row _
                ) = uarg(two)(i)
            For j = 1 To snstocks
                Range(SMneumonic(j, 1) & "!" & _
                    fColumnFromCode(1 + nStates * i + 1) & rInputVector(indexii, 1).Row & ":" & _
                    fColumnFromCode(1 + nStates * (i + 1)) & rInputVector(indexii, 1).Row _
                    ) = sarg(two)(i, j)
            Next
            For j = 1 To nFlows
                Range(FMneumonic(j, 1) & "!" & _
                    fColumnFromCode(1 + nStates * i + 1) & rInputVector(indexii, 1).Row & ":" & _
                    fColumnFromCode(1 + nStates * (i + 1)) & rInputVector(indexii, 1).Row _
                    ) = farg(two)(i, j)
            Next
        Next
    
    End If
    

Next

CatchIt:
'rc = 0

Application.ScreenUpdating = asu

End Sub




