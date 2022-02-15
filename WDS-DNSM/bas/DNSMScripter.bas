Attribute VB_Name = "SMV3_Scripter"
Option Base 1
Function fxCollateralSheetName(ByVal twn As String)
    twn = Left(twn, InStr(twn, ".SMCM") - 1)
    fxCollateralSheetName = twn & ".Collateral.xls"
End Function
Function fxReturnValueSheetName(ByVal twn As String, Optional arg1 = 1)
'    twn = Left(twn, InStr(twn, ".SMCM") - 1)
If arg1 = 1 Then
    fxReturnValueSheetName = "rv.csv"
ElseIf arg1 = 2 Then
    fxReturnValueSheetName = "rvSq.csv"
ElseIf arg1 = 3 Then
    fxReturnValueSheetName = "rvSampler.csv"
Else
    fxReturnValueSheetName = "rvSamplerSq.csv"
End If
    ' "twn & ".Collateral.xls"
End Function
Function fxReturnValueSheetPath(ByVal twn As String)
    twn = Left(twn, InStr(twn, ".SMCM") - 1)
    fxReturnValueSheetPath = twn & ".SMCM.xmlcomdir/"
End Function
Sub cxx_VintageCollateralStartUp()

    Dim twb, cwb As Workbook
    Dim twn, cwn As String
    
    Set twb = ActiveWorkbook
    twn = twb.Name
    cwn = fxCollateralSheetName(twn)
    
    Set cwb = Workbooks.Add
    Dim tws As Worksheet
    cwb.ActiveSheet.Name = "<<Vin"
    Set tws = cwb.Sheets.Add
    tws.Name = "Vin>>"
    Set tws = cwb.Sheets.Add
    tws.Name = "V1"
    Set tws = cwb.Sheets.Add
    tws.Name = "VinAgg"
    
    cwb.SaveAs Filename:=cwn, FileFormat:=xlNormal
    
    twb.Activate
    Sheets("Sampler").Activate
    Calculate
    Cells.Copy
    cwb.Activate
    Sheets("VinAgg").Activate
    Range("A1").Activate
    Selection.PasteSpecial Paste:=xlPasteAll
    'Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    'Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    Dim x As Range
    For Each x In Range("A75:IA148", "A5:IA17")
        If InStr(x.Formula, "SumIt") Then
            x.FormulaR1C1 = "=sum('Vin>>:<<Vin'!RC)"
        ElseIf InStr(x.Formula, "INDIRECT") Then
            x.Copy
            x.PasteSpecial Paste:=xlPasteValues
        ElseIf (InStr(x.Formula, twn) > 0) And Not x.HasArray Then
            hmm = x.HasArray
            x.Copy
            x.PasteSpecial Paste:=xlPasteValues
        ElseIf (InStr(x.Formula, twn) > 0) And x.HasArray Then
            x.CurrentArray.Copy
            x.CurrentArray.PasteSpecial Paste:=xlPasteValues
        End If
    Next
    For Each x In Range("A201:IA248")
        If InStr(x.Formula, "SumIt") Then
            x.FormulaR1C1 = "=sum('Vin>>:<<Vin'!RC)"
        ElseIf InStr(x.Formula, "INDIRECT") Then
            x.Copy
            x.PasteSpecial Paste:=xlPasteValues
        ElseIf (InStr(x.Formula, twn) > 0) And Not x.HasArray Then
            hmm = x.HasArray
            x.Copy
            x.PasteSpecial Paste:=xlPasteValues
        ElseIf (InStr(x.Formula, twn) > 0) And x.HasArray Then
            x.CurrentArray.Copy
            x.CurrentArray.PasteSpecial Paste:=xlPasteValues
        End If
    Next
    ActiveSheet.Outline.ShowLevels RowLevels:=1

    Range("A77").Value = "Vintage Aggregate"
    
    'This quick fix changes the age-dependent column of new production count
    Range("H80").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Range("G80").Select
    ActiveSheet.Paste


'    Sheets("Sheet1").name = "V1"
    
    Sheets("VinAgg").Select
    Sheets("VinAgg").Copy Before:=Sheets("Vin>>")
    Sheets("VinAgg (2)").Select
    Sheets("VinAgg (2)").Name = "VinNewProd"
    Range("G80").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.ClearContents
    Range("G77").Select
    ActiveCell.FormulaR1C1 = "ProtoType Vin"
    Range("H77").Select
    ActiveCell.FormulaR1C1 = "Vin1"
    Range("H80").Select
    ActiveCell.FormulaR1C1 = "=IF(RC2<=0,0,SumProductAcrossSheetsWithUpDraft2(RC7:R101C7,R77C8,ROW(),COLUMN(),RC2))"
    ActiveCell.Copy
    For Each x In Cells
        If Not IsEmpty(x) Then
            s = x.Formula
            If Len(s) > 11 Then
                If Left(s, 11) = "=SUM('Vin>>" Then
                    x.PasteSpecial (xlPasteFormulas)
                End If
            End If
        End If
    Next
    Range("A77").Value = "Vintage New Production"
    Sheets("VinNewProd").Move After:=Sheets("Vin>>")
    
    twb.Activate



End Sub
Sub cxx_VintageCopySamplerToCollateral()

    cxx_VintageCopySamplerToCollateralSub

End Sub
Sub cxx_VintageCopySamplerToCollateralSub(Optional Nm = "VinXXX")

    Dim twb, cwb As Workbook
    Dim twn, cwn As String
    
    Set twb = ActiveWorkbook
    cwn = fxCollateralSheetName(twb.Name)
    Dim PlaceSamplerCopyBefore As String
    PlaceSamplerCopyBefore = Range("SMDriverInfoSpec!H19").Text
    
    Set cwb = Workbooks(cwn)
    cwb.Activate
    Dim nws As Worksheet
    Set nws = Sheets.Add
    'nws.Move after:=Sheets("Vin>>")
    'nws.Move after:=Sheets("VinNewProd")
    If IsASheetName(PlaceSamplerCopyBefore) Then
        nws.Move Before:=Sheets(PlaceSamplerCopyBefore)
    Else
        nws.Move After:=Sheets("Vin>>")
    End If

    Range("A1").Activate
    
    twb.Activate
    Sheets("Sampler").Activate
    ActiveSheet.Calculate
    Cells.Copy
    cwb.Activate
	
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    ActiveSheet.Outline.ShowLevels RowLevels:=1

    nws.Name = Nm
    
    twb.Activate

End Sub
Sub aaa_VintageScripter()

    Call xxx_VintageScripterSub("RunSingle")

End Sub
Sub aaa_VintageScripterUsingRV()

    Call xxx_VintageScripterSub("NoRunSingle")

End Sub
 
Sub xxx_VintageScripterSub(Optional CaseArg = "RunSingle")
Attribute xxx_VintageScripterSub.VB_Description = "Macro recorded 9/4/2006 by cwypasek"
Attribute xxx_VintageScripterSub.VB_ProcData.VB_Invoke_Func = " \n14"
    
    twbn = ActiveWorkbook.Name
    twbnr = Left(twbn, InStr(twbn, "SMCM") - 2)
    
    Dim SMDriver As Worksheet
    Set SMDriver = Sheets("SMDriverInfoSpec")
    
    nsets = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVarNumber").Value
    If nsets = "NA" Then nsets = 1
        
    vv = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar")
    SecondVVInd = 0
    Dim SecondVVValues As Range
    NSecondVV = 0
    If SMDriver.XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVar") <> "NA" Then
        vv2 = SMDriver.XmlDataQuery("/SMDriverInfo/Segements/SecondaryVinVar").Value
        SecondVVInd = 1
        vv2start = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVarStartIndex").Value
        vv2stop = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVarStopIndex").Value
        iii = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinvarSingleIndex").Value
        If iii <> "NA" Or iii > 0 Then
            vv2start = iii
            vv2stop = iii
        End If
        NSecondVV = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/SecondarVinVarNumber").Value
        Set SecondVVValues = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVarStart")
    End If
    
    twb = ActiveWorkbook.Name
    
    vv1start = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVarStartIndex").Value
    vv1stop = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVarStopIndex").Value
    ii = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVarSingleIndex").Value
    If (Not IsEmpty(ii)) And (ii <> "NA") And (ii > 0) Then
        vv1start = ii
        vv1stop = ii
    End If
    
    
    If NSecondVV = 0 Then NSecondVV = 1
    For ii = vv1start To vv1stop
    For iii = 1 To NSecondVV
    
        Range("SMDriverInfoSpec!B14").Value = ii
        Application.CalculateFull
        
        
'        Sheets("PVTData").Select
'        ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv).CurrentPage = "(All)"
'        If SecondVVInd Then
'            ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv2).CurrentPage = "(All)"
'        End If
'
'        If vv <> "NA" Or SMDriver.XmlDataQuery("/SMDriverInfo/Segments/Segment/NewProductionInd")(ii).Value = 0 Then
'            ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv).CurrentPage = SMDriver.XmlDataQuery("/SMDriverInfo/Segments/Segment/PrimaryVinVarValue")(ii).Value
'        End If
        
        If SecondVVInd Then
                ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv2).CurrentPage = SecondVVValues.Value + (iii - 1)
                vintagesuffix = "S" & (SecondVVValues.Value + iii - 1)
                Range("SMDriverInfo!E14").Value = SecondVVValues.Value + iii - 1
        Else
                vintagesuffix = ""
        End If
    
        
        Sheets("Sampler").Activate
    
        If CaseArg = "RunSingle" Then
            aza_ClearStocksAndFlowsResults
        End If
        
        Application.CalculateFull
        
        If CaseArg = "RunSingle" Then
            Call RunStage1NoPickup
        End If
        
        Call cxx_VintageCopySamplerToCollateralSub(Range("SMDriverInfoSpec!B19").Text & vintagesuffix)
    
        Workbooks(twb).Activate
        
    
    Next
    Next
    
End Sub



Sub aaa_VintageFitter()
    
    twbn = ActiveWorkbook.Name
    twbnr = Left(twbn, InStr(twbn, "SMCM") - 2)
    
    nsets = Range("ScripterInit!B16").Value
    
    vv = Range("ScripterInit!B14").Text
    SecondVVInd = 0
    Dim SecondVVValues As Range
    NSecondVV = 0
    If Not IsEmpty(Range("ScripterInit!D14")) Then
        vv2 = Range("ScripterInit!D14").Text
        SecondVVInd = 1
        NSecondVV = Range("ScripterInit!f14").Value
        Set SecondVVValues = Range("ScripterInit!G14:z14")
    End If
    
    twb = ActiveWorkbook.Name
    
    For ii = Range("ScripterInit!B11").Value To Range("ScripterInit!B12").Value
    For iii = 1 To NSecondVV + (NSecondVV = 1)
    
        i = ii - 20
        Range("ScripterInit!B18").Value = i
        Application.CalculateFull
        Sheets("PVTData").Select
        ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv).CurrentPage = "(All)"
        If SecondVVInd Then
            ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv2).CurrentPage = "(All)"
        End If
    
        If Not IsNumeric(Range("ScripterInit!A19")) Or Range("ScripterInit!A19").Value > 30 Then
            ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv).CurrentPage = Range("ScripterInit!A19").Value
        End If
        
        If SecondVVInd Then
                ActiveSheet.PivotTables("PVTDataTable1").PivotFields(vv2).CurrentPage = SecondVVValues(1, iii).Value
                vintagesuffix = "S" & SecondVVValues(1, iii).Value
                Range("ScripterInit!A7").Value = iii - 1
        Else
                vintagesuffix = ""
        End If
    
        
        
        Application.CalculateFull
    
        Sheets("Sg1").Activate
        
        For Each lx In Range("AA54:AD54")
            If lx.Value > 1 Then
                lx.Value = 1
            ElseIf lx.Value < -1 Then
                lx.Value = -1
            End If
            lx.Value = -0.1
        Next
        
        
        
        SolverOk SetCell:="$Z$55", MaxMinVal:=2, ValueOf:="0", ByChange:="$AA$54:$AD$54"

        SolverSolve UserFinish:=True
        SolverFinish KeepFinal:=1
            
        Range("AA54:AD54").Copy
        
        Sheets("ScripterInit").Activate
        
        If iii = 1 Then
            Range("Q" & ii).Activate
            ActiveSheet.Paste
        ElseIf iii = 2 Then
            Range("U" & ii).Activate
            ActiveSheet.Paste
        Else
            Range("Y" & ii).Activate
            ActiveSheet.Paste
        End If
    
    
    Next
    Next
    
End Sub
Sub aaa_RVUser()
Call xxx_RVUserSub
End Sub
Sub aaa_RVUserSims()
Call xxx_RVUserSub(2)
Call xxx_RVUserSub(3)
Call xxx_RVUserSub(4)
End Sub

Sub xxx_RVUserSub(Optional arg1 = 1)
    
    Dim calcprior
    calcprior = Application.Calculation
    Application.Calculation = xlCalculationManual
    
    Dim SMSS, SMSSampler, SMSMSF As Worksheet
    Set SMSS = Sheets("SMStateSpaceSpec")
    Set SMSSampler = Sheets("SMStateSpaceSamplerSpec")
    Set SMSF = Sheets("SMStocksAndFlowsSpec")
    
    Dim i, j, k, l, s, n, list1, list2, nStates, nStages, nStocks, nFlows
    Dim nStocksMRN, nFlowsMRN, nSSamplerAggregates

    nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
    nSSamplerAggregates = SMSSampler.XmlDataQuery("/SMStateSpaceSampler/NumberOfAggregates").Value
    
    nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
    nFlowsMRN = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value
    
    nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
    nStocksMRN = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value

    Call gaa_ActivateOrAddSheet("AllUnits")
    Range("A101:A148").FillDown
    
    Range("A96").Value = "NSimComp"
    Range("A97").Formula = _
        "=if(rXMLDataQuery(""SMDriverInfoSpec"",""/SMDriverInfo/Segments/SimAggType"")=1," & _
        "rXMLDataQuery(""SMDriverInfoSpec"",""/SMDriverInfo/Segments/NumberOfSimulations""),1)"
    Range("A98").Formula = "=1/R[-1]C"
        

    Range("B101", fColumnFromCode(1 + nStates) & "148").FormulaArray = _
        "=(OFFSET(RV!C1,MATCH(SMDriverInfoSpec!$B$14-1,RV!C:C,0),4)" & _
        ":OFFSET(RV!C1,MATCH(SMDriverInfoSpec!$B$14-1,RV!C:C,0)+47," & 3 + nStates & "))" & _
        "*$A$98"

    If arg1 = 2 Then
    Range("B201", fColumnFromCode(1 + nStates) & "248").FormulaArray = _
        "=RVVar(B101:" & fColumnFromCode(1 + nStates) & "148," & _
        "OFFSET(RVSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSq!C:C,0),4)" & _
        ":OFFSET(RVSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSq!C:C,0)+47," & 3 + nStates & ")" & _
        ",1/$A$98)"
    End If
    
    If arg1 = 3 Then
    Range("B301", fColumnFromCode(1 + nSSamplerAggregates) & "348").FormulaArray = _
        "=(OFFSET(RVSampler!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSampler!C:C,0),4)" & _
        ":OFFSET(RVSampler!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSampler!C:C,0)+47," & 3 + nSSamplerAggregates & "))" & _
        "*$A$98"
    End If
    
    If arg1 = 4 Then
    Range("B401", fColumnFromCode(1 + nSSamplerAggregates) & "448").FormulaArray = _
        "=RVVar(B301:" & fColumnFromCode(1 + nSSamplerAggregates) & "348," & _
        "OFFSET(RVSamplerSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSamplerSq!C:C,0),4)" & _
        ":OFFSET(RVSamplerSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSamplerSq!C:C,0)+47," & 3 + nSSamplerAggregates & ")" & _
        ",1/$A$98)"
    End If

    For i = 1 To nStocksMRN
        Sheets(SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Mneumonic").Cells(i, 1).Value).Activate
        Range("A101:A148").FillDown
        Range("A96").Value = "NSimComp"
        Range("A97").Formula = _
            "=if(rXMLDataQuery(""SMDriverInfoSpec"",""/SMDriverInfo/Segments/SimAggType"")=1," & _
            "rXMLDataQuery(""SMDriverInfoSpec"",""/SMDriverInfo/Segments/NumberOfSimulations""),1)"
        Range("A98").Formula = "=1/R[-1]C"
        Range("B101", fColumnFromCode(1 + nStates) & "148").FormulaArray = _
        "=(OFFSET(RV!C1,MATCH(SMDriverInfoSpec!$B$14-1,RV!C:C,0)+" & i * 49 & ",4)" & _
        ":OFFSET(RV!C1,MATCH(SMDriverInfoSpec!$B$14-1,RV!C:C,0)+47+" & i * 49 & "," & 3 + nStates & "))" & _
        "*$A$98"

    If arg1 = 2 Then
        Range("B201", fColumnFromCode(1 + nStates) & "248").FormulaArray = _
        "=RVVar(B101:" & fColumnFromCode(1 + nStates) & "148," & _
        "OFFSET(RVSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSq!C:C,0)+" & i * 49 & ",4)" & _
        ":OFFSET(RVSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSq!C:C,0)+47+" & i * 49 & "," & 3 + nStates & ")" & _
        ",1/$A$98)"
    End If
    
    If arg1 = 3 Then
        Range("B301", fColumnFromCode(1 + nSSamplerAggregates) & "348").FormulaArray = _
        "=(OFFSET(RVSampler!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSampler!C:C,0)+" & i * 49 & ",4)" & _
        ":OFFSET(RVSampler!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSampler!C:C,0)+47+" & i * 49 & "," & 3 + nSSamplerAggregates & "))" & _
        "*$A$98"
    End If
    
    If arg1 = 4 Then
        Range("B401", fColumnFromCode(1 + nSSamplerAggregates) & "448").FormulaArray = _
        "=RVVar(B301:" & fColumnFromCode(1 + nSSamplerAggregates) & "348," & _
        "OFFSET(RVSamplerSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSamplerSq!C:C,0)+" & i * 49 & ",4)" & _
        ":OFFSET(RVSamplerSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSamplerSq!C:C,0)+47+" & i * 49 & "," & 3 + nSSamplerAggregates & ")" & _
        ",1/$A$98)"
    End If
    
    Next

    For i = 1 To nFlows
        Sheets(SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic").Cells(i, 1).Value).Activate
        Range("A101:A148").FillDown
        Range("A96").Value = "NSimComp"
        Range("A97").Formula = _
            "=if(rXMLDataQuery(""SMDriverInfoSpec"",""/SMDriverInfo/Segments/SimAggType"")=1," & _
            "rXMLDataQuery(""SMDriverInfoSpec"",""/SMDriverInfo/Segments/NumberOfSimulations""),1)"
        Range("A98").Formula = "=1/R[-1]C"
        Range("B101", fColumnFromCode(1 + nStates) & "148").FormulaArray = _
        "=(OFFSET(RV!C1,MATCH(SMDriverInfoSpec!$B$14-1,RV!C:C,0)+" & (i + nStocks) * 49 & ",4)" & _
        ":OFFSET(RV!C1,MATCH(SMDriverInfoSpec!$B$14-1,RV!C:C,0)+47+" & (i + nStocks) * 49 & "," & 3 + nStates & "))" & _
        "*$A$98"

    If arg1 = 2 Then
        Range("B201", fColumnFromCode(1 + nStates) & "248").FormulaArray = _
        "=RVVar(B101:" & fColumnFromCode(1 + nStates) & "148," & _
        "OFFSET(RVSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSq!C:C,0)+" & (i + nStocks) * 49 & ",4)" & _
        ":OFFSET(RVSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSq!C:C,0)+47+" & (i + nStocks) * 49 & "," & 3 + nStates & ")" & _
        ",1/$A$98)"
    End If
    
    If arg1 = 3 Then
        Range("B301", fColumnFromCode(1 + nSSamplerAggregates) & "348").FormulaArray = _
        "=(OFFSET(RVSampler!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSampler!C:C,0)+" & (i + nStocks) * 49 & ",4)" & _
        ":OFFSET(RVSampler!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSampler!C:C,0)+47+" & (i + nStocks) * 49 & "," & 3 + nSSamplerAggregates & "))" & _
        "*$A$98"
    End If
    
    If arg1 = 4 Then
        Range("B401", fColumnFromCode(1 + nSSamplerAggregates) & "448").FormulaArray = _
        "=RVVar(B301:" & fColumnFromCode(1 + nSSamplerAggregates) & "348," & _
        "OFFSET(RVSamplerSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSamplerSq!C:C,0)+" & (i + nStocks) * 49 & ",4)" & _
        ":OFFSET(RVSamplerSq!C1,MATCH(SMDriverInfoSpec!$B$14-1,RVSamplerSq!C:C,0)+47+" & (i + nStocks) * 49 & "," & 3 + nSSamplerAggregates & ")" & _
        ",1/$A$98)"
    End If

    Next
    
    Application.Calculation = calcprior

End Sub
Function RVVar(ByRef arg1 As Range, ByRef arg2 As Range, Optional nn = 1) As Variant
Dim rv
Dim n, m, i, j
n = arg1.Rows.Count
m = arg1.Columns.Count
If arg2.Rows.Count <> n Or arg2.Columns.Count <> m Then
Else
    ReDim rv(n, m) As Double
    If nn = 1 Then
    
        For i = 1 To n
        For j = 1 To m
            rv(i, j) = arg2(i, j) - arg1(i, j) ^ 2
        Next
        Next
    
    Else
    
    
        ' arg1 has already been normalized
        For i = 1 To n
        For j = 1 To m
            rv(i, j) = (arg2(i, j) - nn * (arg1(i, j) ^ 2)) / (nn - 1)
        Next
        Next
    
    End If
    
    RVVar = rv
End If
End Function
Sub aaa_RVLoader()
Call xxx_RVLoaderSub
End Sub
Sub aaa_RVLoaderSims()
Call xxx_RVLoaderSub(1)
Call xxx_RVLoaderSub(2)
Call xxx_RVLoaderSub(3)
Call xxx_RVLoaderSub(4)
End Sub
Sub xxx_RVLoaderSub(Optional arg1 = 1)
    
    Dim s As String
    If arg1 = 1 Then
        s = ""
    ElseIf arg1 = 2 Then
        s = "Sq"
    ElseIf arg1 = 3 Then
        s = "Sampler"
    Else
        s = "SamplerSq"
    End If
    
    Dim calcprior
    calcprior = Application.Calculation
    Application.Calculation = xlCalculationManual
    
    Dim SMSS, SMSSampler, SMSMSF As Worksheet
    Set SMSS = Sheets("SMStateSpaceSpec")
    Set SMSSampler = Sheets("SMStateSpaceSamplerSpec")
    Set SMSF = Sheets("SMStocksAndFlowsSpec")
    
    Dim i, j, k, l, n, list1, list2, nStates, nStages, nStocks, nFlows
    Dim nStocksMRN, nFlowsMRN, nSSamplerAggregates

    nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
    nSSamplerAggregates = SMSSampler.XmlDataQuery("/SMStateSpaceSampler/NumberOfAggregates").Value
    
    nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
    nFlowsMRN = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value
    
    nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
    nStocksMRN = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value

    Dim twn As String
    twn = ActiveWorkbook.Name
    
    Call gaa_ActivateOrAddSheet("RV" & s)
    Sheets("RV" & s).Cells.Clear
    'Sheets("RV").Move Before:="Sampler"

    rvn = fxReturnValueSheetName(twn, arg1)
    rvp = fxReturnValueSheetPath(twn)
    
    Range("C20").Select
    With ActiveWorkbook.PivotCaches.Add(SourceType:=xlExternal)
        .Connection = _
            "ODBC;DBQ=" & rvp & ";DefaultDir=" & rvp & _
            ";Driver={Microsoft Text Driver (*.txt; *.csv)};" & _
            "DriverId=27;Extensions=None,asc,csv,tab,txt;" & _
            "FIL=text;MaxBufferSize=2048;MaxScanRows=8;" & _
            "PageTimeout=5;SafeTransactions=0;Threads=3;UserCommitSync=Yes;"
        .CommandType = xlCmdSql
        .CommandText = "SELECT * from  " & rvn
        .CreatePivotTable TableDestination:="RV" & s & "!R20C3", _
        TableName:="RV" & s & "PVTDataTable1", _
        DefaultVersion:=xlPivotTableVersion10
    End With
    If arg1 <= 2 Then
        For i = 0 To nStates - 1
            ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").AddDataField ActiveSheet.PivotTables( _
                "RV" & s & "PVTDataTable1").PivotFields("Col" & i), "Sum of Col" & i, xlSum
        Next
    Else
        For i = 0 To nSSamplerAggregates - 1
            ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").AddDataField ActiveSheet.PivotTables( _
                "RV" & s & "PVTDataTable1").PivotFields("Col" & i), "Sum of Col" & i, xlSum
        Next
    End If
    
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").DataPivotField
        .Orientation = xlColumnField
        .Position = 1
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("Row")
        .Orientation = xlRowField
        .Position = 1
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("Vintage")
        .Orientation = xlRowField
        .Position = 1
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("StockOrFlow")
        .Orientation = xlRowField
        .Position = 2
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("StockOrFlowIndex")
        .Orientation = xlRowField
        .Position = 3
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("Vintage")
        .Subtotals = Array(False, False, False, False, False, False, False, False, False, False, False, False)
    '    .ShowAllItems = True
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("StockOrFlow")
        .Subtotals = Array(False, False, False, False, False, False, False, False, False, False, False, False)
    '    .ShowAllItems = True
    End With
    With ActiveSheet.PivotTables("RV" & s & "PVTDataTable1").PivotFields("StockOrFlowIndex")
        .Subtotals = Array(False, False, False, False, False, False, False, False, False, False, False, False)
    '    .ShowAllItems = True
    End With
    
'    Call aaa_RVUser
    
    Application.Calculation = calcprior
End Sub


