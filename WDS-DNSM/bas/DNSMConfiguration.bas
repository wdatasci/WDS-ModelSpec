Attribute VB_Name = "SMV3_Configuration"
Option Base 1
Sub cca_SMStageXMLDelete()

Dim xm As XmlMap
For Each xm In ActiveWorkbook.XmlMaps
    If _
        Left(xm.Name, 12) = "SMMatrix_Map" _
        Or xm.Name = "SMFID_Map" _
        Or Left(xm.Name, 2) = "Sg" _
        Or xm.Name = "Example" _
        Then
        xm.Delete
    End If
Next


End Sub
Sub caa_SMStageSetUp()
    
Call gaa_ActivateOrAddSheet("<<LGM")
Call gaa_ActivateOrAddSheet("LGM>>", "<<LGM")

Dim SMSS As Worksheet
Dim SMSF As Worksheet
Set SMSS = Sheets("SMStateSpaceSpec")
Set SMSF = Sheets("SMStocksAndFlowsSpec")
Dim SMSSMap, SMSFMap As XmlMap
Set SMSSMap = ActiveWorkbook.XmlMaps("SMStateSpace")
Set SMSFMap = ActiveWorkbook.XmlMaps("SMStocksAndFlows")
NBD = SMSS.XmlDataQuery("/SMStateSpace/States/NumberOfBaseDimensions").Value
nap = SMSS.XmlDataQuery("/SMStateSpace/States/NumberOfAgePages").Value

cca_SMStageXMLDelete


Dim i, j, k
Dim x, y, z, yy, zz As Range
Dim s, sname As String
Dim ns As Integer
ns = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value

For i = 1 To SMSS.XmlDataQuery("/SMStateSpace/Stages/Number").Value


Set x = SMSS.XmlDataQuery("/SMStateSpace/Stages/Stage/Concept").Cells(i, 1)

If i > 0 Then
If x.Text <> "Exit" Then
    
    sname = x.Offset(0, -2).Value
    
    Call sxx_SMLGMConfigSub(sname, "CreatedVia_aabSMStageSetUp", ns)
    
    s = "='" & ActiveSheet.Name & "'!" & _
        Range(ActiveSheet.Name & "DefStateNames").Cells(1, 1).Address & ":" & Range(ActiveSheet.Name & "DefStateNames").Cells(1, 1).Offset(0, ns - 1).Address
    ActiveWorkbook.Names.Add Name:=ActiveSheet.Name & "DefStateNames", RefersTo:=s
    
    Range(sname & "DefStateNames").FormulaArray = _
        "=TRANSPOSE('" & SMSS.Name & "'!" & SMSS.XmlDataQuery("/SMStateSpace/States/State/Mneumonic").Address & ")"
    
    Range("B30").Select
    
    Call sxx_SMFIDProtoTypeSub(sname, ns, ActiveSheet.Name & "DefStateNames")
    
'    Call csa_SMLGMExampleConfigSub(sname, ns)

    Call sxx_SMStageFlowFactorsConfigSub(i, SMSS, SMSF)
    
    ' setting the core BaseOdds/BaseCounts
    
    Set y = Range(sname & "BaseOdds").Cells(1, 2)
    Set z = Range(sname & "BaseCounts").Cells(1, 2)
    
    z.Formula = "=PVTDataRefData!E22"
    z.Copy
    Range(z, z.Offset(ns - 1, ns - 2)).PasteSpecial

    If nap > 0 Then
        Range(z.Offset(ns, 0), z.Offset((nap + 1) * ns - 1, ns - 2)).PasteSpecial
        z.Offset(ns, 0).Formula = "=PVTDataRefDataWithAgePaged!F22"
        z.Offset(ns, 0).Copy
        Range(z.Offset(ns, 0), z.Offset((nap + 1) * ns - 1, ns - 2)).PasteSpecial
        
        Range(y.Offset(ns - 1, -5 - NBD), y.Offset((nap + 1) * ns - 1, -5 - NBD)).FillDown
        ActiveSheet.Calculate
        Range(y.Offset(0, -5 - NBD), y.Offset(ns - 1, -4 - NBD)).Copy
        
        For k = 1 To nap
            y.Offset(k * ns, -5 - NBD).PasteSpecial (xlPasteValues)
        Next
    
        z.Offset(0, -3).FormulaR1C1 = "=int((RC[-1]-1)/R" & (z.Row - 4) & "C[-4])"
        Range(z.Offset(0, -3), z.Offset((nap + 1) * ns - 1, -3)).FillDown
        
        y.Offset(0, -3).FormulaR1C1 = "=int((RC[-1]-1)/R" & (y.Row - 4) & "C[-4])"
        Range(y.Offset(0, -3), y.Offset((nap + 1) * ns - 1, -3)).FillDown
    
    
    End If
    
    
    y.FormulaR1C1 = "=IF(RC" & y.Offset(0, -4 - NBD).Column & "=R" & _
            y.Offset(-2, 0).Row & "C,0,RC[" & z.Column - y.Column & "]/MAX(1," & _
            "OFFSET(RC" & z.Offset(0, -2).Column & ",0,RC" & y.Offset(0, -5 - NBD).Column & ")))"
    y.Copy
    
    Range(y, y.Offset(ns - 1, ns - 2)).PasteSpecial
    If nap > 0 Then
        Range(y.Offset(ns, 0), y.Offset((nap + 1) * ns - 1, ns - 2)).PasteSpecial
    End If
    
    ' setting the core BaseBalanceBias/BaseBalance
    
    Set yy = Range(sname & "BaseBalanceBias").Cells(1, 2)
    Set zz = Range(sname & "BaseBalance").Cells(1, 2)
    
    zz.Formula = "=PVTDataRefData!E" & (22 + ns)
    zz.Copy
    Range(zz, zz.Offset(ns - 1, ns - 2)).PasteSpecial
    
    If nap > 0 Then
        Range(zz.Offset(ns, 0), zz.Offset((nap + 1) * ns - 1, ns - 2)).PasteSpecial
        zz.Offset(ns, 0).Formula = "=PVTDataRefDataWithAgePaged!F" & (22 + ns * nap)
        zz.Offset(ns, 0).Copy
        Range(zz.Offset(ns, 0), zz.Offset((nap + 1) * ns - 1, ns - 2)).PasteSpecial
        
        Range(yy.Offset(ns - 1, -5 - NBD), yy.Offset((nap + 1) * ns - 1, -5 - NBD)).FillDown
        ActiveSheet.Calculate
        Range(yy.Offset(0, -5 - NBD), yy.Offset(ns - 1, -4 - NBD)).Copy
        
        For k = 1 To nap
            yy.Offset(k * ns, -5 - NBD).PasteSpecial (xlPasteValues)
        Next
    
    End If
    
    yy.FormulaR1C1 = "=IF(RC" & yy.Offset(0, -4 - NBD).Column & "=R" & _
            yy.Offset(-2, 0).Row & "C,0," & _
            "if('" & sname & "'!RC[" & z.Column - y.Column & "]=0,0," & _
            "if(RC[" & z.Column - y.Column & "]<=0,0," & _
            "ln(RC[" & z.Column - y.Column & "]/MAX(1," & _
            "OFFSET(RC" & zz.Offset(0, -2).Column & ",0,RC" & yy.Offset(0, -5 - NBD).Column & _
            "))/'" & sname & "'!RC[" & z.Column - y.Column & "]))))"
    yy.Copy
    
    Range(yy, yy.Offset(ns - 1, ns - 2)).PasteSpecial

    If nap > 0 Then
        Range(yy.Offset(ns, 0), yy.Offset((nap + 1) * ns - 1, ns - 2)).PasteSpecial
        
        zz.Offset(0, -3).FormulaR1C1 = "=int((RC[-1]-1)/R" & (zz.Row - 4) & "C[-4])"
        Range(zz.Offset(0, -3), zz.Offset((nap + 1) * ns - 1, -3)).FillDown
        
        yy.Offset(0, -3).FormulaR1C1 = "=int((RC[-1]-1)/R" & (yy.Row - 4) & "C[-4])"
        Range(yy.Offset(0, -3), yy.Offset((nap + 1) * ns - 1, -3)).FillDown
    
    End If

End If
End If
Next


End Sub

Sub cax_SMStageSetUpPatch()
    
Call gaa_ActivateOrAddSheet("<<LGM")
Call gaa_ActivateOrAddSheet("LGM>>", "<<LGM")

Dim SMSS As Worksheet
Dim SMSF As Worksheet
Set SMSS = Sheets("SMStateSpaceSpec")
Set SMSF = Sheets("SMStocksAndFlowsSpec")
Dim SMSSMap, SMSFMap As XmlMap
Set SMSSMap = ActiveWorkbook.XmlMaps("SMStateSpace")
Set SMSFMap = ActiveWorkbook.XmlMaps("SMStocksAndFlows")
NBD = SMSS.XmlDataQuery("/SMStateSpace/States/NumberOfBaseDimensions").Value


i = 1


Set x = SMSS.XmlDataQuery("/SMStateSpace/Stages/Stage/Concept").Cells(i, 1)

Sheets("Sg1").Activate
Call sxx_SMStageFlowFactorsConfigSub(i, SMSS, SMSF, 1)
    
End Sub

Sub caa_SMStageInputsSetUp()


calcprior = Application.Calculation
Application.Calculation = xlCalculationManual

Dim ni ' allowance columns for input calculations

ni = 10

Dim SMSS, SMSF As Worksheet

Dim SS, Stages, States As String
SS = "SMStateSpaceSpec"
Set SMSS = Sheets(SS)

Dim SF, Stocks, Flows As String
SF = "SMStocksAndFlowsSpec"
Set SMSF = Sheets(SF)


Call gaa_ActivateOrAddSheet("LGM>>")
Call gaa_ActivateOrAddSheet("<<StageInputs", "LGM>>")
Call gaa_ActivateOrAddSheet("StageInputs>>", "<<StageInputs")
Call gaa_ActivateOrAddSheet("<<Flows", "StageInputs>>")
Call gaa_ActivateOrAddSheet("Flows>>", "<<Flows")
Call gaa_ActivateOrAddSheet("<<Stocks", "Flows>>")
Call gaa_ActivateOrAddSheet("Stocks>>", "<<Stocks")
Call gaa_ActivateOrAddSheet("<<Units", "Stocks>>")
Call gaa_ActivateOrAddSheet("Units>>", "<<Units")

Dim i, j, k, l, s, n, list1, list2, nStates, nStages, nStocks, nFlows

nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
nStages = SMSS.XmlDataQuery("/SMStateSpace/Stages/Number").Value

nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
snstocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value
nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
mnflows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value


For i = 1 To nStages
    
    s = SMSS.XmlDataQuery("/SMStateSpace/Stages/Stage/Mneumonic")(i).Value
    
    Call gaa_ActivateOrAddSheet(s & "Inputs", "<<StageInputs")
    Range("A1:A90").Select
    Selection.Rows.Group
    
    Range("A95").FormulaR1C1 = s
    Range("A95").Font.Size = 24
    Range("A95").Font.Bold = True
    Range("A95").Font.Italic = True
    
    Range("A99").FormulaR1C1 = "Index"
    'Range("A100").FormulaR1C1 = "=ROW()-100"
    Range("A100").FormulaR1C1 = "=mod(ROW()-100,49)"
    Range("A100:A148").FillDown
    Range("B98").FormulaR1C1 = s & "FID Input Calculations"
        
    Range("B99").Value = "PrimaryVinVar"
    Range("B100").Formula = "=INT((ROW()-100-MOD(ROW()-100,49))/49)+1"
    Range("C99").Value = "SecondaryVinVar"
    Range("C100").Formula = "=0"
    
    
    Range("D99").Value = "Age"
'   Range("D100").Formula = "=if($B100<>$B99,offset(SMDriverInfoSpec!F$21,Sg1Inputs!$B100,0),D99+1)"
    Range("D100").Formula = "=if(AND(OR(NOT(ISBLANK(SMDriverInfoSpec!B12)),NOT(ISBLANK(SMDriverInfoSpec!B14))),$B100<>$B99),SMDriverInfoSpec!B16,IF($B100<>$B99,offset(SMDriverInfoSpec!F$21,Sg1Inputs!$B100,0),D99+1))"
    Range("E99").Value = "MonthID"
    Range("e100").Formula = "=if(AND(OR(NOT(ISBLANK(SMDriverInfoSpec!B12)),NOT(ISBLANK(SMDriverInfoSpec!B14))),$B100<>$B99),SMDriverInfoSpec!B17,IF($B100<>$B99,offset(SMDriverInfoSpec!G$21,Sg1Inputs!$B100,0),E99+1))"
    Range("A100:C" & 99 + 49 * Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVarNumber").Value).FillDown
    Range("D100:E" & 99 + 49 * Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVarNumber").Value).FillDown
    'Range("B101:B148").FillDown
    'Range("B101:C148").FillRight
    
    ActiveSheet.Outline.ShowLevels RowLevels:=1, ColumnLevels:=1
    Range("A92").Activate
Next

Application.Calculation = calcprior
End Sub
Sub caa_SMStocksAndFlowsSetUp()


calcprior = Application.Calculation
Application.Calculation = xlCalculationManual

Dim ni ' allowance columns for input calculations

ni = 10

Dim SMSS, SMSF As Worksheet

Dim SS, Stages, States As String
SS = "SMStateSpaceSpec"
Set SMSS = Sheets(SS)

Dim SF, Stocks, Flows As String
SF = "SMStocksAndFlowsSpec"
Set SMSF = Sheets(SF)

Dim hasPVTDataSheet, hasPVTDataTotalsSheet, hasDriverInfoSheet As Boolean
hasPVTDataSheet = IsASheetName("PVTData")
hasPVTDataTotalsSheet = IsASheetName("PVTDataTotals")
hasDriverInfoSheet = IsASheetName("SMDriverInfoSpec")


Call gaa_ActivateOrAddSheet("LGM>>")
Call gaa_ActivateOrAddSheet("<<StageInputs", "LGM>>")
Call gaa_ActivateOrAddSheet("StageInputs>>", "<<StageInputs")
Call gaa_ActivateOrAddSheet("<<Flows", "StageInputs>>")
Call gaa_ActivateOrAddSheet("Flows>>", "<<Flows")
Call gaa_ActivateOrAddSheet("<<Stocks", "Flows>>")
Call gaa_ActivateOrAddSheet("Stocks>>", "<<Stocks")
Call gaa_ActivateOrAddSheet("<<Units", "Stocks>>")
Call gaa_ActivateOrAddSheet("Units>>", "<<Units")

Dim i, j, k, l, s, n, list1, list2, nStates, nStages, nStocks, nFlows

nStates = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
nStages = SMSS.XmlDataQuery("/SMStateSpace/Stages/Number").Value

nStocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Number").Value
snstocks = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/MacroReturnNumber").Value
nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Number").Value
mnflows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value

list0 = Array("Units", "Stocks", "Flows")
list1 = Array(0, Stocks, Flows)
list2 = Array(1, snstocks, nFlows)



For i = 1 To 3
For j = 1 To list2(i)
    
    If list0(i) = "Units" Then
        s = "AllUnits"
        actualsvar = "n"
        Call gaa_ActivateOrAddSheet(s, "<<Units")
    ElseIf list0(i) = "Stocks" Then
        s = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Mneumonic")(j).Value
        actualsvar = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/ActualsVariable")(j).Value
        Call gaa_ActivateOrAddSheet(s, "<<Stocks")
    Else
        s = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic")(j).Value
        actualsvar = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/ActualsVariable")(j).Value
        Call gaa_ActivateOrAddSheet(s, "<<Flows")
    End If
    
    
    Range("A1:A90").Select
    Selection.Rows.Group
    
    Range("A95").FormulaR1C1 = s
    Range("A95").Font.Size = 24
    Range("A95").Font.Bold = True
    Range("A95").Font.Italic = True
    
    Range("A99").FormulaR1C1 = "Index"
    Range("A100").FormulaR1C1 = "=ROW()-100"
    Range("A100:A112").FillDown
    Range("B96").FormulaR1C1 = "State Delinquency"
    If list0(i) = "Units" Then
        For k = 1 To nStates
            Range(fColumnFromCode(1 + k) & 97).Value = SMSS.XmlDataQuery("/SMStateSpace/States/State/NotionalDelq")(k)
        Next
    Else
        For k = 1 To nStates
            Range(fColumnFromCode(1 + k) & 97).Value = Range("AllUnits!" & fColumnFromCode(1 + k) & 97).Value
        Next
    End If
    Range("B98").FormulaR1C1 = "Stage Aggregate"
    Range("B99:" & fColumnFromCode(1 + nStates) & 99).FormulaArray = "=Sg1DefStateNames"
    tempstr = "=0"
    For k = 1 To nStages
        Range(fColumnFromCode(1 + nStates * k + 1) & 98).Value = SMSS.XmlDataQuery("/SMStateSpace/Stages/Stage/Mneumonic")(k)
        tempstr = tempstr & "+RC[" & (nStates * k) & "]"
    Next
    Range(fColumnFromCode(1 + nStates + 1) & 99).FormulaR1C1 = "=RC[" & (-nStates) & "]"
    Range(fColumnFromCode(1 + nStates + 1) & 99 & ":" & fColumnFromCode(1 + nStates * (nStages + 1)) & 99).FillRight
    Range(fColumnFromCode(2) & 100).FormulaR1C1 = tempstr
    Range(fColumnFromCode(1 + 1) & 100 & ":" & fColumnFromCode(1 + nStates) & 100).FillRight
    Range(fColumnFromCode(1 + 1) & 100 & ":" & fColumnFromCode(1 + nStates) & 100 + 48).FillDown
    
'    Columns("C:Y").Select
'    Selection.Columns.Group
    
'    Columns(fColumnFromCode(26 - ni) & ":X").Select
'    Selection.Columns.Group
    
    
    Range("A9").Value = "Field"
    Range("B9").Value = "NA"
    If actualsvar <> "NA" Then
    If Left(actualsvar, 2) = "f:" Then
    Else
        Range("B9").Value = actualsvar
    End If
    End If
    
    If hasDriverInfoSheet Then
        Range("C9").Formula = "=SMDriverInfoSpec!B17"
    End If
    Range("D9").Value = 40
    Range("E9").Value = "InitCase"
    If hasDriverInfoSheet Then
        Range("F9").Formula = "=IF(SMDriverInfoSpec!B15=1,1,0)"
    End If
    Range("A10").Value = "Index"
    Range("A11").Formula = "=row()-($D$9-$C$9)"
    Range("A11:A60").FillDown
    
    ''''''''''''''''''''''''''''
    Range("B10").Formula = "=B99"
    
    ' ScripterInitx is the column letter where the new production
    ' initial value is take from the Segments list in SMDriverInfo
    
    ScripterInitx = ""
    
    If ActiveSheet.Name = "AllUnits" Then
        Range("B11").Formula = "=if($F$9=1,if(A11=$C$9,1,0),0)"
        Range("B9").Value = "n"
        ScripterInitx = "J"
    ElseIf ActiveSheet.Name = "BCL" Then
        Range("B11").Clear
        ScripterInitx = "K"
    ElseIf ActiveSheet.Name = "BAR" Then
        Range("B11").Clear
        ScripterInitx = "L"
    ElseIf ActiveSheet.Name = "BPB" Then
        Range("B11").Clear
        ScripterInitx = "M"
    ElseIf ActiveSheet.Name = "FFees" Then
        Range("B11").Clear
        ScripterInitx = "N"
    ElseIf ActiveSheet.Name = "FPurch" Then
        Range("B11").Clear
        ScripterInitx = "O"
    ElseIf ActiveSheet.Name = "FPmt" Then
        Range("B11").Clear
        ScripterInitx = "P"
    Else
        Range("B11").Clear
        ScripterInitx = "Q"
    End If
    Range("B11:B60").FillDown
    
    ''''''''''''''''''''''''''''
    Range("C10").Formula = "=C99"

    Dim lr As Range
    
    Set lr = SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/@Name")
    Dim ii, jj
    ii = 0
    While ii < lr.Count And lr(ii + 1) <> "StateVariable"
        ii = ii + 1
    Wend
    ii = ii + 1
    

    jj = 0
    While jj < lr.Count And lr(jj + 1) <> "StateVariable"
        jj = jj + 1
    Wend
    jj = jj + 1


    If ii <= lr.Count And hasPVTDataSheet Then
    If hasPVTDataTotalsSheet Then
        If Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVar").Value <> "NA" Then
            Range("C11").Formula = "=if(or($B$9=""NA"",$F$9=1,isblank($B$9)),0," & _
                "GETPIVOTDATA(""Sum of ""&$B$9,PVTData!$C$20,""" & _
                Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar").Value & _
                """,SMDriverInfoSpec!$B$18,""" & _
                Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVar").Value & _
                """,offset(SMDriverInfoSpec!$E$14,0,ScripterInit!$A$7),""akMonthID"",$A11,""" & _
                SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & """,C$10)" & _
                ")"
        ElseIf Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar").Value <> "NA" Then
            Range("C11").Formula = "=if(or($B$9=""NA"",$F$9=1,isblank($B$9)),0," & _
                "if(isblank(SMDriverInfoSpec!$B$14)" & _
                ",GETPIVOTDATA(""Sum of ""&$B$9,PVTDataTotals!$C$20," & _
                """akMonthID"",$A11,""" & _
                SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & _
                """,C$10)" & _
                ",GETPIVOTDATA(""Sum of ""&$B$9,PVTData!$C$20,""" & _
                Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar").Value & _
                """,SMDriverInfoSpec!$B$18,""akMonthID"",$A11,""" & _
                SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & _
                """,C$10)" & _
                ")" & _
                ")"
        Else
            Range("C11").Formula = "=if(or($B$9=""NA"",$F$9=1,isblank($B$9)),0,GETPIVOTDATA(""Sum of ""&$B$9,PVTData!$C$20,""akMonthID"",$A11,""" & SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & """,C$10))"
        End If
    Else
        If Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVar").Value <> "NA" Then
            Range("C11").Formula = "=if(or($B$9=""NA"",$F$9=1,isblank($B$9)),0,GETPIVOTDATA(""Sum of ""&$B$9,PVTData!$C$20,""" & _
                Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar").Value & _
                """,SMDriverInfoSpec!$B$18,""" & _
                Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/SecondaryVinVar").Value & _
                """,offset(SMDriverInfoSpec!$E$14,0,ScripterInit!$A$7),""akMonthID"",$A11,""" & _
                SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & """,C$10))"
        ElseIf Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar").Value <> "NA" Then
            Range("C11").Formula = "=if(or($B$9=""NA"",$F$9=1,isblank($B$9)),0,GETPIVOTDATA(""Sum of ""&$B$9,PVTData!$C$20,""" & _
                Sheets("SMDriverInfoSpec").XmlDataQuery("/SMDriverInfo/Segments/PrimaryVinVar").Value & _
                """,SMDriverInfoSpec!$B$18,""akMonthID"",$A11,""" & _
                SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & _
                """,C$10))"
        Else
            Range("C11").Formula = "=if(or($B$9=""NA"",$F$9=1,isblank($B$9)),0,GETPIVOTDATA(""Sum of ""&$B$9,PVTData!$C$20,""akMonthID"",$A11,""" & SMSS.XmlDataQuery("/SMStateSpace/States/ParameterList/Parameter/Value")(ii) & """,C$10))"
        End If
    End If
    End If
    
    
    If actualsvar <> "NA" Then
    If Left(actualsvar, 2) = "f:" Then
'        Range("C11").Formula = Replace(Replace(Mid(actualsvar, 3, 50), "xx", "C11"), "XX", "C11")
    End If
    End If
    
    
    
    Range("C11:C60").FillDown
    Range("C10:" & fColumnFromCode(1 + nStates) & 60).FillRight
    Range(fColumnFromCode(1 + nStates + 1) & 10).FormulaR1C1 = "=if(isnumber(RC[-" & nStates & "]),RC[-" & nStates & "],0)"
    Range(fColumnFromCode(1 + nStates + 1) & 10 & ":" & fColumnFromCode(1 + nStates + 1) & 60).FillDown
    Range(fColumnFromCode(1 + nStates + 1) & 10 & ":" & fColumnFromCode(1 + 2 * nStates) & 60).FillRight
    
    '''''''''''''''''''''''''
    'Range("B100").Formula = "=INDIRECT(fColumnFromCode(COLUMN())&$D$9)"
    
    If ScripterInitx <> "" And hasDriverInfoSheet Then
        Range("B100").Formula = "=if(B$97>SMDriverInfoSpec!$H$14,0,IF(SMDriverInfoSpec!$B$15=1,IF(B$99=OFFSET(SMDriverInfoSpec!$I$21,SMDriverInfoSpec!$B$14,0),OFFSET(SMDriverInfoSpec!$" & ScripterInitx & "$21,SMDriverInfoSpec!$B$14,0),0),INDIRECT(fColumnFromCode(COLUMN())&$D$9)))"
    Else
        Range("B100").Formula = "=if(B$97>SMDriverInfoSpec!$H$14,0,INDIRECT(fColumnFromCode(COLUMN())&$D$9))"
    End If
    
    Range("B100:" & fColumnFromCode(1 + nStates) & 100).FillRight
    
    
    ''''Stage1 is always a copy of the aggregate for pickup reasons
    Range(fColumnFromCode(1 + nStates + 1) & 100).FormulaR1C1 = "=RC[-" & nStates & "]"
    
    Range(fColumnFromCode(1 + nStates + 1) & 100 & ":" & fColumnFromCode(1 + 2 * nStates) & 100).FillRight
    
    
'    ActiveSheet.Outline.ShowLevels RowLevels:=1, ColumnLevels:=1
    Range("A92").Activate
    
Next
Next


' The "f:" actualsvars were held and must be processed now
For i = 1 To 3
For j = 1 To list2(i)
    If list0(i) = "Units" Then
        s = "AllUnits"
        actualsvar = "n"
    ElseIf list0(i) = "Stocks" Then
        s = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/Mneumonic")(j).Value
        actualsvar = SMSF.XmlDataQuery("/SMStocksAndFlows/Stocks/Stock/ActualsVariable")(j).Value
    Else
        s = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic")(j).Value
        actualsvar = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/ActualsVariable")(j).Value
    End If
    If actualsvar <> "NA" Then
    If Left(actualsvar, 2) = "f:" Then
        Call gaa_ActivateOrAddSheet(s)
        Range("C11").Formula = Replace(Replace(Mid(actualsvar, 3, 50), "xx", "C11"), "XX", "C11")
        Range("C11:C60").FillDown
        Range("C10:" & fColumnFromCode(1 + nStates) & 60).FillRight
    End If
    End If
Next
Next

Cells.Replace What:="PVTData!$C$20", Replacement:="PVTData!$e$20", LookAt _
    :=xlPart, SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
    ReplaceFormat:=False

Application.Calculation = calcprior


End Sub
Sub sxx_SMLGMConfigSub(ByVal csn As String, ByVal tsn As String, ByVal ns As Integer)

    Dim i, foundeol As Integer
    Dim x
    
    
    If (ns = 0) Or (ns > 50) Then
        foundns = 0
        ns = 20
    End If
    
    Call gaa_ActivateOrAddSheet(csn, "<<LGM")
    ActiveSheet.Cells.Clear
    
    Dim gb As GroupBox
    Set gb = ActiveSheet.GroupBoxes.Add(Range("A2").Left + Range("A2").Width / 2, Range("A2").Top + Range("A2").Height / 2, _
        Range("A23").Offset(0, ns + 3).Left, Range("A23").Offset(0, ns + 3).Top)
    gb.Placement = xlMoveAndSize
    gb.Select
    Selection.Characters.Text = csn
    Range("B23").Value = "OrigDataSheet"
    Range("C23").Value = tsn
    ActiveWorkbook.Names.Add Name:=csn & "OrigDataSheet", RefersToR1C1:="=" & csn & "!R23C3"
    Range("D23").Value = "ConditionalInd"
    ActiveWorkbook.Names.Add Name:=csn & "ConditionalInd", RefersToR1C1:="=" & csn & "!R23C5"
    Range("E23").Value = foundcond
    
    
    ActiveWorkbook.Names.Add Name:=csn & "NumStates", RefersToR1C1:="=" & csn & "!R3C3"
    Range(csn & "NumStates").Offset(0, -1).Value = "Number Of States"
    Range(csn & "NumStates").Value = ns
    
    ActiveWorkbook.Names.Add Name:=csn & "NumObservableStates", RefersToR1C1:="=" & csn & "!R5C3"
    Range(csn & "NumObservableStates").Offset(0, -1).Value = "Number of Observable"
    Range(csn & "NumObservableStates").FormulaR1C1 = "=" & csn & "NumStates"
    
    ActiveWorkbook.Names.Add Name:=csn & "DefStateNamePrefix", RefersToR1C1:="=" & csn & "!R7C3"
    Range(csn & "DefStateNamePrefix").Offset(0, -1).Value = "DefStateNamePrefix"
    Range(csn & "DefStateNamePrefix").Value = "Pi"
    
    ActiveWorkbook.Names.Add Name:=csn & "DefStateNames", RefersToR1C1:="=" & csn & "!R9C3:R9C" & (2 + ns)
    Range(csn & "DefStateNames").Cells(1, 1).Offset(0, -1).Value = "DefStateNames"
    If foundns Then
        Range(csn & "DefStateNames").FormulaArray = "=" & tsn & "!R1C" & foundns + 1 & ":R1C" & foundns + ns
    Else
        Range(csn & "DefStateNames").FormulaArray = "=fDefStateNames(" & csn & "DefStateNamePrefix," & csn & "NumStates)"
    End If
    
    ActiveWorkbook.Names.Add Name:=csn & "DefObservableStateNamePrefix", RefersToR1C1:="=" & csn & "!R11C3"
    Range(csn & "DefObservableStateNamePrefix").Offset(0, -1).Value = "DefObservableStateNamePrefix"
    Range(csn & "DefObservableStateNamePrefix").Value = "PiH"
    
    ActiveWorkbook.Names.Add Name:=csn & "DefObservableStateNames", RefersToR1C1:="=" & csn & "!R13C3:R13C" & (2 + ns)
    Range(csn & "DefObservableStateNames").Cells(1, 1).Offset(0, -1).Value = "DefObservableStateNames"
    Range(csn & "DefObservableStateNames").FormulaArray = "=fDefStateNames(" & csn & "DefObservableStateNamePrefix," & csn & "NumObservableStates)"
    
    ActiveWindow.View = xlNormalView
    Cells.Select
    Cells.EntireColumn.AutoFit
    
    
End Sub
Sub sxx_SMStageFlowFactorsConfigSub( _
    ByVal StageNumber, _
    ByRef SMSS As Worksheet, _
    ByRef SMSF As Worksheet, _
    Optional justlast = 0)
    'ByVal nflows As Integer, Optional FlowSpec = "FlowSpec")

    Dim tsn As String
    tsn = ActiveSheet.Name
    
    
    
    
    
    ns = SMSS.XmlDataQuery("/SMStateSpace/States/Number").Value
    nFlows = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/MacroReturnNumber").Value
    NBD = SMSS.XmlDataQuery("/SMStateSpace/States/NumberOfBaseDimensions").Value
    baseci = 30 '+ ns
    ci = baseci
    cj = 40
    
    nos = ns 'Range(tsn & "NumObservableStates").Value
    
    cistep = (Int(ns / 5) + 2) * 5 - ns
    cistep = Int(1.5 * ns)
    
    Dim calcprior
    calcprior = Application.Calculation
    Application.Calculation = xlCalculationManual
    
If justlast = 0 Then
    
    Cells(ci, cj).Select
    
    Call sxx_MapSMMatrixToLocationSub(tsn & "ModelSpec", ns, tsn & "DefStateNames", NBD)
    
    Sheets("<<LGM").Activate
    Sheets(tsn).Activate
    
    Cells(ci, cj + (ns + 10)).Select
    
    Call sxx_MapSMMatrixToLocationSub(tsn & "BaseOdds", ns, tsn & "DefStateNames", NBD)
    
    Sheets("<<LGM").Activate
    Sheets(tsn).Activate
    
    Cells(ci, cj + 2 * (ns + 10)).Select
    
    Call sxx_MapSMMatrixToLocationSub(tsn & "BaseCounts", ns, tsn & "DefStateNames", NBD)
    
    If cj + 4 * (ns + 10) > 128 Then
            
        Call gaa_ActivateOrAddSheet(tsn & "Continued", tsn, 2)
        stageshifter = 3
    
    Else
        
        stageshifter = 0
    
    End If
    
    Cells(ci, cj + (3 - stageshifter) * (ns + 10)).Select
    
    Call sxx_MapSMMatrixToLocationSub(tsn & "BaseBalanceBias", ns, tsn & "DefStateNames", NBD)
    
    Cells(ci, cj + (4 - stageshifter) * (ns + 10)).Select
    
    Call sxx_MapSMMatrixToLocationSub(tsn & "BaseBalance", ns, tsn & "DefStateNames", NBD)
    
    Cells(1, 1).Activate
    
    Call gaa_ActivateOrAddSheet(tsn)
    
    cie = ci
    
    ci = ci + ns + cistep
    
    Cells(ci, cj).Select
    
    Call sxx_MapSMMatrixToLocationSub(tsn & "Topology", ns, tsn & "DefStateNames", NBD, 1)
    
    ' reset the "ProvidesNonZeroCoords" flag unless the user wants it
    Cells(ci + 2, cj + 1).Value = 0
    
    Cells(1, 1).Activate
    
    Dim lr As Range
    Set lr = Range(tsn & "ModelSpec").Cells(1, 1)
    
    lr.Offset(-6, 1).Value = "Max"
    lr.Offset(-6, 2).Value = 0
    
    Range(tsn & "ModelSpec").FormulaR1C1 = "=MIN(" & _
          lr.Offset(-6, 2).Address(ReferenceStyle:=xlR1C1) & _
          ",IF(R" & lr.Offset(-1, 0).Row & "C =""Col"" & R[0]C" & _
          lr.Offset(0, -4 - NBD).Column & ",0,IF(Index(" & tsn & "BaseCounts,RC" & lr.Offset(0, -4 - NBD).Column & _
          ",column()-column(" & lr.Address(1, 1, xlR1C1) & ")+1)<=0,-1," & _
          "Max(" & lr.Offset(-1, 0).Address(1, 1, xlR1C1) & ":R[-1]C" & lr.Offset(0, ns - 1).Column & _
          ",R[0]C" & lr.Column & ":R[0]C[-1])+1)))"
    
    Set lr = Range(tsn & "Topology").Cells(1, 1).Offset(-1, -1)
    
    Range(tsn & "Topology").FormulaR1C1 = "=IF(ElementIsNonNeg(Sg1ModelSpec,RC" & _
            lr.Offset(0, -0 - NBD).Column & ",COLUMN()-COLUMN(RC" & lr.Column & "))=1,IF(R" & lr.Row & "C=""Col1""," & _
            "MAX(R" & lr.Row & "C" & lr.Offset(0, 1).Column & ":R[-1]C" & lr.Column + ns & ")," & _
            "MAX(R" & lr.Row & "C" & lr.Offset(0, 1).Column & ":R[-1]C" & lr.Column + ns & ",RC[-1]:RC" & lr.Offset(0, 1).Column & "))+1,0)"
    
    '=IF(ElementIsNonNeg(Sg1ModelSpec,RC43,COLUMN()-COLUMN(RC44))=1,IF(R147C="Col1",MAX(R147C45:R[-1]C89),MAX(R147C45:R[-1]C89,RC[-1]:RC45))+1,0)

'
'    Range(tsn & "Odds").FormulaArray = "=OddsFillerWithBase(" & tsn & "BetasIndex," & tsn & "BetasAddress," & tsn & "Betas," & tsn & "Topology," & tsn & "BaseOdds)"
'
'    Range(tsn & "Transistion").FormulaArray = "=RowNormalization(" & tsn & "Odds)"
'

'    Call baa_LGMConfigEye(tsn, tsn & "Observability", ci, cj, ns)
'

'    Call baa_LGMConfigEye(tsn, tsn & "BaseOdds", ci, cj, ns, "")
'
'    Range(tsn & "BaseOdds").FormulaArray = "=OddsWithDiagRef(" & tsn & "ExampleMatrix)"
'

End If

    Dim nflowsbreak1, nflowsbreak2 As Integer
    
    Call gaa_ActivateOrAddSheet(tsn & "Flows1", tsn)
    nflowsbreak1 = 0
    nflowsbreak2 = 1
    
    nnap = 0
    
    Dim naptag As Range
    
    For nfi = 1 To nFlows
        If 4 + (ns + 12) * (nfi - nflowsbreak1 + 1) < 256 Then
            Cells(1, 4 + (ns + 12) * (nfi - nflowsbreak1 - 1) + 2).Activate
        If justlast = 0 Or nfi = nFlows Then
            Selection.Value = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic")(nfi).Value
        End If
            Cells(1, 4 + (ns + 12) * (nfi - nflowsbreak1 - 1)).Activate
        Else
            Cells(1, 1).Activate
            nflowsbreak2 = nflowsbreak2 + 1
            Call gaa_ActivateOrAddSheet(tsn & "Flows" & nflowsbreak2, tsn & "Flows" & nflowsbreak2 - 1, 2)
            nflowsbreak1 = nfi - 1
            Cells(1, 4 + (ns + 12) * (nfi - nflowsbreak1 - 1) + 2).Activate
        If justlast = 0 Or nfi = nFlows Then
            Selection.Value = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/Mneumonic")(nfi).Value
        End If
            Cells(1, 4 + (ns + 12) * (nfi - nflowsbreak1 - 1)).Activate
        End If
        
        If justlast = 0 Or nfi = nFlows Then
            
            Set naptag = Cells(1, 4 + (ns + 12) * (nfi - nflowsbreak1 - 1))
            
            Call sxx_MapSMMatrixToLocationSub(tsn & "BaseFlow" & nfi, ns, tsn & "DefStateNames", NBD)
        
            nap = SMSF.XmlDataQuery("/SMStocksAndFlows/Flows/Flow/NumberOfFlowMatrices")(nfi).Value
            
            naptag.Offset(0, 3).Value = "Min"
            naptag.Offset(0, 4).Value = -9999999
            naptag.Offset(0, 5).Value = "max"
            naptag.Offset(0, 6).Value = 999999
           
            If nap > 0 Then
            
                nnap = nnap + 1
                
                naptag.Offset(6, 4).FormulaR1C1 = "=int((RC[-1]-1)/R3C[-4])"
                
                Range(naptag.Offset(6, 4), naptag.Offset(5 + (nap + 1) * ns, 4)).FillDown
                
                GNAP = SMSS.XmlDataQuery("/SMStateSpace/States/NumberOfAgePages").Value
                
                naptag.Offset(6, 4 + NBD + 1).Formula = "=max(" & naptag.Offset(0, 4).Address(1, 1) & ",min(" & _
                            naptag.Offset(0, 6).Address(1, 1) & ",PVTDataRefData!E" & (22 + (nnap + 1) * ns) & "))"
                naptag.Offset(6, 4 + NBD + 1).Copy
                Range(naptag.Offset(6, 4 + NBD + 1), naptag.Offset(5 + ns, 4 + NBD + ns - 1)).PasteSpecial
                
                If nap > 1 Then
                    naptag.Offset(6 + ns, 4 + NBD + 1).Formula = "=max(" & naptag.Offset(0, 4).Address(1, 1) & ",min(" & _
                            naptag.Offset(0, 6).Address(1, 1) & ",PVTDataRefDataWithAgePaged!F" & (22 + (nnap + 1) * ns * GNAP) & "))"
                    naptag.Offset(6 + ns, 4 + NBD + 1).Copy
                    Range(naptag.Offset(6 + ns, 4 + NBD + 1), naptag.Offset(5 + ns * (GNAP + 1), 4 + NBD + ns - 1)).PasteSpecial
                
                End If
                
            End If
        
        End If
    Next

    Cells(1, 1).Activate
            
    Call gaa_ActivateOrAddSheet(tsn)

    ci = 25 'baseci
    cj = 1 'cj + ns + cistep

'    ActiveWorkbook.Names.Add Name:=tsn & "NumberBetas", RefersToR1C1:="=" & tsn & "!R" & ci & "C" & cj + 1
'    Range(tsn & "NumberBetas").Cells(1, 1).Offset(0, -1).Value = "NumberBetas"
'    Range(tsn & "NumberBetas").Cells(1, 1).Value = "=max(" & tsn & "ModelSpec)"
    
    Application.Calculation = calcprior
    
    
End Sub
Sub cba_LGMConfig()

    Dim tsn As String
    tsn = ActiveSheet.Name
    
    Dim calcprior
    calcprior = Application.Calculation
    Application.Calculation = xlCalculationManual
    Application.CalculateFull
    
For Each Nm In ActiveSheet.Names
    If Nm = tsn & "BetasAddress" Then
    Range(tsn & "BetasAddress").Clear
    End If
    If Nm = tsn & "BetasWLabels" Then
    Range(tsn & "BetasIndex").Clear
    End If
    If Nm = tsn & "BetasIndex" Then
    Range(tsn & "BetasIndex").Clear
    End If
Next
    
    ci = Range(tsn & "NumberBetas").Cells(1, 1).Row
    cj = Range(tsn & "NumberBetas").Cells(1, 1).Column - 1
    
    nb = Range(tsn & "NumberBetas").Value
    If nb = 0 Then nb = nb + 1
    
    ci = ci + 2
        
On Error GoTo moveon
    
    Range(tsn & "Betas").Clear
moveon:
    On Error GoTo 0

For Each Nm In ActiveSheet.Names
    If Nm = tsn & "BetasAddress" Then
    Range(tsn & "BetasAddress").Clear
    End If
    If Nm = tsn & "BetasWLabels" Then
    Range(tsn & "BetasIndex").Clear
    End If
    If Nm = tsn & "BetasIndex" Then
    Range(tsn & "BetasIndex").Clear
    End If
Next
    
    ActiveWorkbook.Names.Add Name:=tsn & "BetasWLabels", RefersToR1C1:="=" & tsn & "!R" & ci & "C" & cj & ":R" & (ci + nb) & "C" & (cj + 3)
    ActiveWorkbook.Names.Add Name:=tsn & "BetasAddress", RefersToR1C1:="=" & tsn & "!R" & (ci + 1) & "C" & (cj + 1) & ":R" & (ci + nb) & "C" & (cj + 2)
    ActiveWorkbook.Names.Add Name:=tsn & "BetasIndex", RefersToR1C1:="=" & tsn & "!R" & (ci + 1) & "C" & cj & ":R" & (ci + nb) & "C" & cj
    ActiveWorkbook.Names.Add Name:=tsn & "Betas", RefersToR1C1:="=" & tsn & "!R" & (ci + 1) & "C" & (cj + 3) & ":R" & (ci + nb) & "C" & (cj + 3)
    Range(tsn & "BetasWLabels").Cells(1, 1).Offset(-1, 0).Value = "Betas"
    Range(tsn & "BetasWLabels").Cells(1, 1).Value = "No."
    Range(tsn & "BetasWLabels").Cells(1, 2).Value = "I"
    Range(tsn & "BetasWLabels").Cells(1, 3).Value = "J"
    Range(tsn & "BetasWLabels").Cells(1, 3).Offset(-2, 0).Value = "SolverTarget"
    Range(tsn & "BetasWLabels").Cells(1, 4).Value = "Value"
    Range(tsn & "BetasWLabels").Cells(1, 4).Offset(-2, 0).FormulaR1C1 = "=" & tsn & "ConditionalInd"
    
    For i = 1 To nb
        Range(tsn & "BetasIndex").Cells(i, 1).Value = i
    Next
    
    Range(tsn & "BetasAddress").FormulaArray = "=StampFind(" & tsn & "BetasIndex," & tsn & "ModelSpec)"
'    Range(tsn & "Odds").FormulaArray = "=OddsFillerWithBase(BetasIndex,BetasAddress,Betas,Topology,BaseOdds)"
'    Range(tsn & "Transistion").FormulaArray = "=RowNormalization(Odds)"
    
    Application.Calculation = calcprior
    
End Sub
Sub sxx_SMFIDProtoTypeSub( _
    Optional Nm = "Example", _
    Optional ns = 21, _
    Optional StateNames = "", _
    Optional PathToSMProtoTypeXSDs = "C:\LocalWork\SMV1\SMProtoType\xsd\", _
    Optional lastarg = "")
    'ByVal tsn As String, _
    'ByVal tadd As String, _
    'ByVal targetFID As String, _

    Dim priorcalc
    priorcalc = Application.Calculation
    Application.Calculation = xlCalculationManual

    Dim tag As Range
    Dim llo As ListObject
    Dim tsn As String
    tsn = ActiveSheet.Name
    
    Set tag = ActiveCell
    
    Dim nstatenames As Integer
    Dim i As Integer
    
    nstatenames = 0
    Dim nstatenamesrange As Range
    If StateNames <> "" Then
        Set nstatenamesrange = Range(StateNames)
        nstatenames = nstatenamesrange.Cells.Count
    End If

    If IsAnXMLMapName(Nm) Then
        ActiveWorkbook.XmlMaps(Nm).Delete
    End If
    
    ActiveWorkbook.XmlMaps.Add(PathToSMProtoTypeXSDs & "SMFID.xsd", "SMFID").Name = Nm


    tag.FormulaR1C1 = "Name"
    tag.Offset(0, 1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/@Name"
    tag.Offset(0, 1).Value = Nm
    tag.Offset(1, 0).FormulaR1C1 = "Number Of States"
    tag.Offset(2, 0).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/NumberOfStates"
    tag.Offset(2, 0).Value = ns
    tag.Offset(4, 0).FormulaR1C1 = "State Labels"
    Range(tag.Offset(5, 0), tag.Offset(4 + ns, 1)).Select
    Set llo = ActiveSheet.ListObjects.Add
    llo.ListColumns(1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/StateLabels/StateLabel/@Position"
    tag.Offset(5, 0).Value = "Position"
    Range(tag.Offset(6, 0), tag.Offset(5 + ns, 0)).FormulaR1C1 = "=N(R[-1]C)+1"
    llo.ListColumns(2).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/StateLabels/StateLabel"
    tag.Offset(5, 1).Value = "State Label"
    If nstatenames = ns Then
        For i = 1 To ns
            tag.Offset(5 + i, 1).Value = nstatenamesrange(i)
        Next
    End If
    
' Betas has 7 elements/attributes
' FunctionalInputs and RedundantFunctionalInputs each has the
' same 10 elements/attributes, but only 9 are mapped for used for each
    'BaseSetInd
    'Script
    'InputReference
    
    
    Dim no As Integer
    no = 2 - 7
    Dim slevel1, slevel2 As String
    Dim slevel1set, slevel2set, slevel_attr_cnts
    slevel1set = Array("Betas", "FunctionalInputs", "RedundantFunctionalInputs")
    slevel2set = Array("Beta", "FunctionInput", "FunctionInput")
    slevel_attr_cnts = Array(7, 9, 9)
    
    For i = 1 To 3
        slevel1 = slevel1set(i)
        slevel2 = slevel2set(i)
        no = no + slevel_attr_cnts(i) + 2
        
    
        tag.Offset(1, no + 1).FormulaR1C1 = "Number Of " & slevel1
        tag.Offset(2, no + 1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/Number"
        ' note ->>>>> formula for the count has to be held until xsd is mapped
        
        Application.Names.Add Name:=Nm & "Num" & slevel1, RefersTo:="=" & tsn & "!" & tag.Offset(2, no + 1).Address
        
        tag.Offset(4, no + 1).FormulaR1C1 = slevel1
        
        Range(tag.Offset(5, no + 1), tag.Offset(6, no + slevel_attr_cnts(i))).Select
        Set llo = ActiveSheet.ListObjects.Add
        llo.ListColumns(1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/@Position"
        tag.Offset(5, no + 1).Value = "Position"
        Range(tag.Offset(6, no + 1), tag.Offset(6, no + 1)).FormulaR1C1 = "=N(R[-1]C)+1"
        
        llo.ListColumns(2).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/Label"
        tag.Offset(5, no + 2).Value = "Label"
        'Range(tag.Offset(6, no + 2), tag.Offset(5 + ns, 4)).FormulaR1C1 = "=0"
        tag.Offset(6, no).FormulaR1C1 = "=if(RC[4]=0,if(RC[4]=0,""OddsBaseOffset"",""Across Column "" & INDEX(" & Nm & "DefStateNames,RC[4])),if(RC[4]=0,""Across Row "" & INDEX(" & Nm & "DefStateNames,RC[3]),INDEX(" & Nm & "DefStateNames,RC[3]) & "" to "" & INDEX(" & Nm & "DefStateNames,RC[3])))"
        
        llo.ListColumns(3).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/I"
        tag.Offset(5, no + 3).Value = "I"
        'Range(tag.Offset(6, no+3), tag.Offset(5 + ns, no+3)).FormulaR1C1 = "=0"
        
        llo.ListColumns(4).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/J"
        tag.Offset(5, no + 4).Value = "J"
        'Range(tag.Offsvet(6, no+4), tag.Offset(5 + ns, no+4)).FormulaR1C1 = "=0"
        
        llo.ListColumns(5).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/Value"
        tag.Offset(5, no + 5).Value = "Value"
        'Range(tag.Offset(6, no+5), tag.Offset(5 + ns, no+5)).FormulaR1C1 = "=0"
        
        llo.ListColumns(6).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/FlowRef"
        tag.Offset(5, no + 6).Value = "FlowRef"
        'Range(tag.Offset(6, no+6), tag.Offset(5 + ns, no+6)).FormulaR1C1 = "=0"
        
        llo.ListColumns(7).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/OpZeroOrOne"
        tag.Offset(5, no + 7).Value = "OpZeroOrOne"
        'Range(tag.Offset(6, no+7), tag.Offset(5 + ns, no+7)).FormulaR1C1 = "=0"
            
        If slevel1 = "FunctionalInputs" Or slevel1 = "RedundantFunctionalInputs" Then
        
            llo.ListColumns(8).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/BaseSetInd"
            tag.Offset(5, no + 8).Value = "BaseSetInd"
            'Range(tag.Offset(6, no+8), tag.Offset(5 + ns, no+8)).FormulaR1C1 = "=0"
        
        End If
            
        If slevel1 = "FunctionalInputs" Then
            
            llo.ListColumns(9).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/Script"
            tag.Offset(5, no + 9).Value = "Script"
            'Range(tag.Offset(6, no+9), tag.Offset(5 + ns, no+9)).FormulaR1C1 = "=0"
            
        End If
        
        If slevel1 = "RedundantFunctionalInputs" Then
            
            llo.ListColumns(9).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMFID/" & slevel1 & "/" & slevel2 & "/InputReference"
            tag.Offset(5, no + 9).Value = "InputReference"
            'Range(tag.Offset(6, no+9), tag.Offset(5 + ns, no+9)).FormulaR1C1 = "=0"
                
        End If
        
        tag.Offset(2, no + 1).Formula = "=COUNTA(SMFIDSubRange(""" & Nm & """,""/SMFID/" & slevel1 & "/" & slevel2 & "/I""))-1"
    
    Next
    
    
    


Application.Names.Add Name:=Nm & "FID", RefersTo:="=" & tsn & "!" & tag.Address

Application.Calculation = priorcalc

End Sub

Sub caa_SMInputsExportMap()

    Dim ns As Integer
    ns = Sheets("SMStateSpaceSpec").XmlDataQuery("/SMStateSpace/States/Number").Value
    nStages = Sheets("SMStateSpaceSpec").XmlDataQuery("/SMStateSpace/Stages/Number").Value
    ninputs = Sheets("Sg1").XmlDataQuery("/SMFID/FunctionalInputs/Number").Value

For ii = 1 To nStages

    Call gaa_ActivateOrAddSheet("Sg" & ii & "InputsExportMap", "Sg" & ii & "Inputs", 1)
    
    Cells.Clear
    Range("A1").Activate

    Call sxx_MapSMMatrixToLocationSub("Sg" & ii & "InputsExportMap", ninputs + 2, "", 4)
 
    Range("E7").Select
    ActiveCell.Formula = "=Sg" & ii & "Inputs!A100"
    Range("E7", "G7").FillRight
    
    
    Range("I7").Formula = "=Sg" & ii & "Inputs!D100"
    
    Range("I7", fColumnFromCode(ninputs + 2 + 8) & 7).FillRight
        
    'Range("E3").Select
    'ActiveCell.FormulaR1C1 = "=MAX(R[4]C:R[65533]C)-MIN(R[4]C:R[65533]C)+1"
    'Range("E3", "H3").FillRight
'    Range("G3").Value = 1
    
    Range("D1").Select
    ActiveCell.Formula = "=counta(Sg" & ii & "Inputs!a100:a10000)"
    ActiveSheet.Calculate
    
    Range("E7", fColumnFromCode(ninputs + 2 + 8) & 6 + Range("D1").Value).FillDown
    
    
Next ii

End Sub

Sub caa_SMPVTDataExportMap()

    Dim ns As Integer
    ns = Sheets("SMStateSpaceSpec").XmlDataQuery("/SMStateSpace/States/Number").Value
    
    Call gaa_ActivateOrAddSheet("PVTDataExportMap", "PVTData", 1)
    
    Cells.Clear
    Range("A1").Activate

    Call sxx_MapSMMatrixToLocationSub("PVTDataExportMap", ns, "Sg1DefStateNames", 4)
 
    Range("E7").Select
    ActiveCell.FormulaR1C1 = "=PVTData!R[15]C"
    Range("F7").Select
    ActiveCell.FormulaR1C1 = "=IF(NOT(ISBLANK(PVTData!R[15]C[-2])),if(PVTData!R[15]C[-2]=PVTData!R22C4,1,N(R[-1]C)+1),R[-1]C)"
    Range("G7").Select
    ActiveCell.FormulaR1C1 = "=IF(NOT(ISBLANK(PVTData!R[15]C[-4])),if(PVTData!R[15]C[-4]=PVTData!R22C3,1,N(R[-1]C)+1),R[-1]C)"
    Range("D1").Select
    ActiveCell.FormulaR1C1 = "=COUNTA(PVTData!C[1])"
    Range("J7").Select
    ActiveCell.FormulaR1C1 = "=PVTData!R[15]C[-4]"
    Range("J7").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.FillDown
    Range(Selection, Selection.End(xlToRight)).Select
    Selection.FillRight
    ActiveSheet.Calculate
    Range("E3").Select
    ActiveCell.FormulaR1C1 = "=MAX(R[4]C:R[65533]C)-MIN(R[4]C:R[65533]C)+1"
    Range("E3").Select
    Selection.Copy
    Range("F3").Select
    ActiveSheet.Paste
    Range("G3").Select
    ActiveSheet.Paste
    Range("F3:G3").Select
    Range("G3").Activate
    Application.CutCopyMode = False
    ActiveSheet.Calculate
    Range("D3").Select
    ActiveCell.FormulaR1C1 = "3"
    Range("A1").Select

    Range("D7:" & fColumnFromCode(ns + 3 + 5) & 5 + Range("D1").Value).FillDown
    
 
End Sub
Function SMFIDSubRange(Nm As String, xp As String)
Dim x As Worksheet
Set x = Sheets(Nm)
SMFIDSubRange = x.XmlMapQuery(xp)
End Function
Sub csa_SMLGMExampleConfigSub(ByVal xtext As String, ByVal ns As Integer)


Dim xr As Range
Dim i, j, k, x


    
    Call aca_LGMFIDProtoTypeSub(xtext, fColumnFromCode(10 + ns) & 26, xtext)
    
    Set xr = Range(fColumnFromCode(10 + ns) & 60)
    xr.FormulaR1C1 = "Test"
    xr.Offset(1, ns + 1).Value = "Inputs"
    Range(xr.Offset(2, 0).Address & ":" & xr.Offset(2, ns - 1).Address).FormulaArray = "=" & xtext & "DefStateNames"
    Range(xr.Offset(3, 0).Address & ":" & xr.Offset(3, ns - 1).Address).Value = 0
    xr.Offset(3, 0).Value = 1
    Range(xr.Offset(4, 0).Address & ":" & xr.Offset(4, ns - 1).Address).FormulaArray = _
        "=PMultByFID(R[-1]C:R[-1]C[" & ns - 1 & "],RC[" & ns + 2 & "]," & xtext & "FID)"



End Sub

Sub ssm_MapSMMatrixToLocation()
Call sxx_MapSMMatrixToLocationSub
End Sub

Sub sxx_MapSMMatrixToLocationSub( _
    Optional Nm = "Example", _
    Optional ns = 21, _
    Optional StateNames = "", _
    Optional NumberOfBaseDimensions = 4, _
    Optional ProvidesNonZeroCoords = 0, _
    Optional PathToSMProtoTypeXSDs = "C:\LocalWork\SMV1\SMProtoType\xsd\", _
    Optional lastarg = "")

    Dim tag As Range
    Dim llo As ListObject
    
    Set tag = ActiveCell
    Dim ts As Worksheet
    Set ts = ActiveSheet
    
    Dim priorcalc
    priorcalc = Application.Calculation
    Application.Calculation = xlCalculationManual

    Dim nstatenames As Integer
    Dim i As Integer
    
    nstatenames = 0
    Dim nstatenamesrange As Range
    If StateNames <> "" Then
        Set nstatenamesrange = Range(StateNames)
        nstatenames = nstatenamesrange.Cells.Count
    End If

    If IsAnXMLMapName(Nm) Then
        ActiveWorkbook.XmlMaps(Nm).Delete
    End If
    
    ActiveWorkbook.XmlMaps.Add(PathToSMProtoTypeXSDs & "SMMatrix.xsd", "SMMatrix").Name = Nm

    tag.FormulaR1C1 = "Name"
    tag.Offset(0, 1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/@Name"
    tag.Offset(0, 1).Value = Nm
    tag.Offset(1, 0).FormulaR1C1 = "Number Of States"
    tag.Offset(2, 0).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/NumberOfStates"
    tag.Offset(2, 0).Value = ns
    tag.Offset(1, 1).FormulaR1C1 = "Provides Non-Zero Coords"
    tag.Offset(2, 1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/ProvidesNonZeroCoords"
    tag.Offset(2, 1).Value = ProvidesNonZeroCoords
    
    'tag.Offset(2, 0).FormulaR1C1 = "Additional Axes"
    tag.Offset(1, 3).FormulaR1C1 = "Number Of Axes"
    tag.Offset(2, 3).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/NumberOfAdditionalAxes"
    tag.Offset(2, 3).Value = NumberOfBaseDimensions
If NumberOfBaseDimensions > 0 Then
    tag.Offset(1, 4).FormulaR1C1 = "Axis 1 Limits (N/Min)"
    tag.Offset(2, 4).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesUpperLimits/Axis1"
    tag.Offset(3, 4).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesLowerLimits/Axis1"
End If
If NumberOfBaseDimensions > 1 Then
    tag.Offset(1, 5).FormulaR1C1 = "Axis 2 Limits (N/Min)"
    tag.Offset(2, 5).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesUpperLimits/Axis2"
    tag.Offset(3, 5).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesLowerLimits/Axis2"
End If
If NumberOfBaseDimensions > 2 Then
    tag.Offset(1, 6).FormulaR1C1 = "Axis 3 Limits (N/Min)"
    tag.Offset(2, 6).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesUpperLimits/Axis3"
    tag.Offset(3, 6).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesLowerLimits/Axis3"
End If
If NumberOfBaseDimensions > 3 Then
    tag.Offset(1, 7).FormulaR1C1 = "Axis 4 Limits (N/Min)"
    tag.Offset(2, 7).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesUpperLimits/Axis4"
    tag.Offset(3, 7).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/AdditionalAxesLowerLimits/Axis4"
End If
    
    
If ProvidesNonZeroCoords = 1 Then

    If tag.Column() - 5 >= 1 Then
    
        Dim ztag As Range
        Set ztag = tag.Offset(5, -4)
        Set ztag = tag.Offset(8 + ns, 3)
        
        ztag.Activate
        
        Set llo = ActiveSheet.ListObjects.Add
        llo.ListColumns(1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/NonZeroElements/NonZeroCoordinates/NonZeroCoordinate/@Position"
        ztag.Value = "Position"
        Range(ztag.Offset(1, 0), ztag.Offset(ns, 0)).FormulaR1C1 = "=N(R[-1]C)+1"
        llo.ListColumns.Add
        llo.ListColumns.Add
        llo.ListColumns(2).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/NonZeroElements/NonZeroCoordinates/NonZeroCoordinate/I"
        ztag.Offset(0, 1).Value = "I"
        llo.ListColumns(3).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/NonZeroElements/NonZeroCoordinates/NonZeroCoordinate/J"
        ztag.Offset(0, 2).Value = "J"
            
        ztag.Offset(1, 0).Value = "Number Of Non-Zero Elements"
        ztag.Offset(1, 1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/NonZeroElements/Number"
        ztag.Offset(1, 1).FormulaR1C1 = "=max(R[1]C[-1]:R[1000]C[-1])"
    
    End If

End If
    
    
    
    
    
    
    
    
    tag.Offset(4, 0).FormulaR1C1 = "State Labels"
    Range(tag.Offset(5, 0), tag.Offset(4 + ns, 1)).Select
    Set llo = ActiveSheet.ListObjects.Add
    llo.ListColumns(1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/StateLabels/StateLabel/@Position"
    tag.Offset(5, 0).Value = "Position"
    Range(tag.Offset(6, 0), tag.Offset(5 + ns, 0)).FormulaR1C1 = "=N(R[-1]C)+1"
    llo.ListColumns(2).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/StateLabels/StateLabel"
    tag.Offset(5, 1).Value = "State Label"
    If nstatenames = ns Then
        For i = 1 To ns
            tag.Offset(5 + i, 1).Value = nstatenamesrange(i)
        Next
    End If
    
If 1 Then ' first set, watch for limits on the column maps (excel bug)

    tag.Offset(4, 3).FormulaR1C1 = "MData"
    Range(tag.Offset(5, 3), tag.Offset(4 + ns, 3 + NumberOfBaseDimensions + ns)).Select
    Set llo = ActiveSheet.ListObjects.Add
    llo.ListColumns(1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Row"
    tag.Offset(5, 3).Value = "Row"
    Range(tag.Offset(6, 3), tag.Offset(5 + ns, 3)).FormulaR1C1 = "=N(R[-1]C)+1"
If NumberOfBaseDimensions > 0 Then
    coffset = 2
    llo.ListColumns(2).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis1"
    tag.Offset(5, 4).Value = "Axis1"
    Range(tag.Offset(6, 4), tag.Offset(5 + ns, 4)).FormulaR1C1 = "=0"
End If
If NumberOfBaseDimensions > 1 Then
    coffset = 3
    llo.ListColumns(3).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis2"
    tag.Offset(5, 5).Value = "Axis2"
    Range(tag.Offset(6, 5), tag.Offset(5 + ns, 5)).FormulaR1C1 = "=0"
End If
If NumberOfBaseDimensions > 2 Then
    coffset = 4
    llo.ListColumns(4).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis3"
    tag.Offset(5, 6).Value = "Axis3"
    Range(tag.Offset(6, 6), tag.Offset(5 + ns, 6)).FormulaR1C1 = "=0"
End If
If NumberOfBaseDimensions > 3 Then
    coffset = 5
    llo.ListColumns(5).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis4"
    tag.Offset(5, 7).Value = "Axis4"
    Range(tag.Offset(6, 7), tag.Offset(5 + ns, 7)).FormulaR1C1 = "=0"
End If
    Dim llolc As ListColumn
    For i = 1 To ns
'        Set llolc = llo.ListColumns.Add
        llo.ListColumns(i + coffset).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/Col" & i
'        llolc.XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/Col" & i
        tag.Offset(5, 2 + coffset + i).Value = "Col" & i
        tag.Offset(4, 2 + coffset + i).Formula = "=offset(" & tag.Offset(5, 1).Address & "," & i & ",0)"
    Next


Else

'    tag.Offset(4, 3).FormulaR1C1 = "MData"
    tag.Offset(5, 3).Select
    Set llo = ActiveSheet.ListObjects.Add
    llo.ListColumns(1).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Row"
    tag.Offset(5, 3).Value = "Row"
    Range(tag.Offset(6, 3), tag.Offset(5 + ns, 3)).FormulaR1C1 = "=N(R[-1]C)+1"

If NumberOfBaseDimensions > 0 Then
    coffset = 2
    llo.ListColumns.Add
    llo.ListColumns(2).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis1"
    tag.Offset(5, 4).Value = "Axis1"
    Range(tag.Offset(6, 4), tag.Offset(5 + ns, 4)).FormulaR1C1 = "=0"
End If
If NumberOfBaseDimensions > 1 Then
    coffset = 3
    llo.ListColumns.Add
    llo.ListColumns(3).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis2"
    tag.Offset(5, 5).Value = "Axis2"
    Range(tag.Offset(6, 5), tag.Offset(5 + ns, 5)).FormulaR1C1 = "=0"
End If
If NumberOfBaseDimensions > 2 Then
    coffset = 4
    llo.ListColumns.Add
    llo.ListColumns(4).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis3"
    tag.Offset(5, 6).Value = "Axis3"
    Range(tag.Offset(6, 6), tag.Offset(5 + ns, 6)).FormulaR1C1 = "=0"
End If
If NumberOfBaseDimensions > 3 Then
    coffset = 5
    llo.ListColumns.Add
    llo.ListColumns(5).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/@Axis4"
    tag.Offset(5, 7).Value = "Axis4"
    Range(tag.Offset(6, 7), tag.Offset(5 + ns, 7)).FormulaR1C1 = "=0"
End If
    
    For i = 1 To ldMin(100, ns)
        llo.ListColumns.Add
        llo.ListColumns(i + coffset).XPath.SetValue ActiveWorkbook.XmlMaps(Nm), "/SMMatrix/MData/Col" & i
        tag.Offset(5, 2 + coffset + i).Value = "Col" & i
        tag.Offset(4, 2 + coffset + i).Formula = "=offset(" & tag.Offset(5, 1).Address & "," & i & ",0)"
    Next
    
End If
        
If NumberOfBaseDimensions > 0 Then
    tag.Offset(2, 4).FormulaR1C1 = "=max(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis1"",""" & Nm & """))-R[1]C[0]+1"
    tag.Offset(3, 4).FormulaR1C1 = "=min(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis1"",""" & Nm & """))"
End If
If NumberOfBaseDimensions > 1 Then
    tag.Offset(2, 5).FormulaR1C1 = "=max(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis2"",""" & Nm & """))-R[1]C[0]+1"
    tag.Offset(3, 5).FormulaR1C1 = "=min(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis2"",""" & Nm & """))"
End If
If NumberOfBaseDimensions > 2 Then
    tag.Offset(2, 6).FormulaR1C1 = "=max(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis3"",""" & Nm & """))-R[1]C[0]+1"
    tag.Offset(3, 6).FormulaR1C1 = "=min(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis3"",""" & Nm & """))"
End If
If NumberOfBaseDimensions > 3 Then
    tag.Offset(2, 7).FormulaR1C1 = "=max(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis4"",""" & Nm & """))-R[1]C[0]+1"
    tag.Offset(3, 7).FormulaR1C1 = "=min(rXMLDataQuery(""" & ts.Name & """,""/SMMatrix/MData/@Axis4"",""" & Nm & """))"
End If
    
    
    ActiveWorkbook.Names.Add Name:=Nm, RefersTo:="='" & ActiveSheet.Name & "'!" & _
        llo.ListColumns(coffset + 1).Range.Cells(2, 1).Address & ":" & _
        llo.ListColumns(coffset + ns).Range.Cells(1 + ns, 1).Address
    
    
    
    Application.Calculation = priorcalc
    
End Sub


