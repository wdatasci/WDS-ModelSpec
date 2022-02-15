Attribute VB_Name = "RAControlPanelClient"
Sub aba_ControlPanelSync()
    
    
Dim s As String

s = Replace(ActiveWorkbook.Name, ".xls", "")

If InStr(s, "Waterfall") Then
    s = Replace(s, ".Waterfall", "")
ElseIf InStr(s, "CollateralModel") Then
    s = Replace(s, ".CollateralModel", "")
ElseIf InStr(s, "SMCM.10") Then
    s = Replace(s, ".SMCM.10", "")
ElseIf InStr(s, "SMCM.9") Then
    s = Replace(s, ".SMCM.9", "")
ElseIf InStr(s, "SMCM.8") Then
    s = Replace(s, ".SMCM.8", "")
ElseIf InStr(s, "SMCM.7") Then
    s = Replace(s, ".SMCM.7", "")
ElseIf InStr(s, "SMCM.6") Then
    s = Replace(s, ".SMCM.6", "")
ElseIf InStr(s, "SMCM.5") Then
    s = Replace(s, ".SMCM.5", "")
ElseIf InStr(s, "SMCM.4") Then
    s = Replace(s, ".SMCM.4", "")
ElseIf InStr(s, "SMCM.3") Then
    s = Replace(s, ".SMCM.3", "")
ElseIf InStr(s, "SMCM.2") Then
    s = Replace(s, ".SMCM.2", "")
ElseIf InStr(s, "SMCM.1") Then
    s = Replace(s, ".SMCM.1", "")
ElseIf InStr(s, "SMCM") Then
    s = Replace(s, ".SMCM", "")
End If
        
    ActiveWorkbook.UpdateLink Name:=ActiveWorkbook.Path & "\" & s & ".ControlPanel.xls", Type:=xlExcelLinks
          
End Sub
Sub caa_ControlPanelNames()
    
Dim priorcalc
priorcalc = Application.Calculation
Application.Calculation = xlCalculationManual

gaa_ActivateOrAddSheet ("ControlPanelNames")


Dim s, sn, sa, sr As String
Dim i, j, k

s = Replace(ActiveWorkbook.Name, ".xls", "")

If InStr(s, "Waterfall") Then
    s = Replace(s, ".Waterfall", "")
ElseIf InStr(s, "CollateralModel") Then
    s = Replace(s, ".CollateralModel", "")
ElseIf InStr(s, "SMCM.10") Then
    s = Replace(s, ".SMCM.10", "")
ElseIf InStr(s, "SMCM.9") Then
    s = Replace(s, ".SMCM.9", "")
ElseIf InStr(s, "SMCM.8") Then
    s = Replace(s, ".SMCM.8", "")
ElseIf InStr(s, "SMCM.7") Then
    s = Replace(s, ".SMCM.7", "")
ElseIf InStr(s, "SMCM.6") Then
    s = Replace(s, ".SMCM.6", "")
ElseIf InStr(s, "SMCM.5") Then
    s = Replace(s, ".SMCM.5", "")
ElseIf InStr(s, "SMCM.4") Then
    s = Replace(s, ".SMCM.4", "")
ElseIf InStr(s, "SMCM.3") Then
    s = Replace(s, ".SMCM.3", "")
ElseIf InStr(s, "SMCM.2") Then
    s = Replace(s, ".SMCM.2", "")
ElseIf InStr(s, "SMCM.1") Then
    s = Replace(s, ".SMCM.1", "")
ElseIf InStr(s, "SMCM") Then
    s = Replace(s, ".SMCM", "")
End If
        
        
        
    i = 1
    
    While Range("A" & (i + 1)).Text <> ""
    
        i = i + 1
        sn = Range("A" & i).Text
        sa = Range("B" & i).Text
        
        
'        ActiveWorkbook.Names.Add Name:=sn, RefersTo:="='" & ActiveWorkbook.Path & "\[" & s & ".ControlPanel.xls]" & Replace(sa, "!", "'!")
        sr = "=[" & s & ".ControlPanel.xls]" & Mid(Left(sa, InStr(sa, "!") - 1), 2, 100) & "!" & sn
        
        Range("C" & i).Formula = sr
        Range("D" & i).Clear
        Range("E" & i).FormulaR1C1 = "=if(isblank(rc[-1]),rc[-2],rc[-1])"
                
        ActiveWorkbook.Names.Add Name:=sn, RefersToR1C1:="=ControlPanelNames!R" & i & "C5"
        
        
    Wend
    
Application.Calculation = priorcalc
          
End Sub
Sub cba_NamedRangeSetter()
    
Dim x As Range
For Each x In Selection
    If Not IsEmpty(x.Offset(0, -1)) Then
        ActiveWorkbook.Names.Add Name:=x.Offset(0, -1).Text, _
            RefersToR1C1:="='" & ActiveSheet.Name & "'!" & x.Address(1, 1, xlR1C1)
    End If
Next

End Sub
Sub cba_NamedRangeReferencer()
    
Dim x As Range
For Each x In Selection
    If Not IsEmpty(x.Offset(0, -1)) Then
        x.Formula = "=" & x.Offset(0, -1).Text
    End If
Next

End Sub

