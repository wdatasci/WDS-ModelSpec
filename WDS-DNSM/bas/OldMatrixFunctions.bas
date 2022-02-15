Attribute VB_Name = "RAGVBAMatrixFunctions"
Option Base 1
Sub nnn_RAGVBAMatrixFunctions()
    notes = "Risk Analytics Group Miscellaneous Matrix Functions" & Chr(10) & Chr(10) & _
        "Odds and ends that are commonly used"
    MsgBox (notes)
End Sub

Function MatMult(ByRef arg1 As Range, ByRef arg2 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = arg2.Rows.Count
    n2 = arg2.Columns.Count
    
    If n1 = m2 Then
    
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
        For j = 1 To n2
        For k = 1 To n1
            rc(i, j) = rc(i, j) + arg1(i, k) * arg2(k, j)
        Next
        Next
        Next
        MatMult = rc
    
    End If

End Function

Function MatMultByCorners(ByRef arg1 As Range, ByRef arg2 As Range, ByRef arg3 As Range, ByRef arg4 As Range) As Variant

    Dim rc As Variant
    m1 = arg2.Row - arg1.Row + 1
    n1 = arg2.Column - arg1.Column + 1
    m2 = arg4.Row - arg3.Row + 1
    n2 = arg4.Column - arg3.Column + 1
        
    If n1 = m2 Then
    
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
        For j = 1 To n2
        For k = 1 To n1
            rc(i, j) = rc(i, j) + arg1.Offset(i - 1, k - 1) * arg3.Offset(k - 1, j - 1)
        Next
        Next
        Next
        MatMultByCorners = rc
    
    End If

End Function
Function TransistionFromAltPage(ByRef arg1 As Range, ByVal arg2 As String, ByVal arg3 As String, ByVal arg4 As Integer) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = n1
    n2 = n1
    
        
    If (n1 = m2) And (m2 = n2) Then
    
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
        For k = 1 To n1
        s = 0
        For j = 1 To n2
            x = ifnull(Range(arg2 & "!" & arg3 & arg4).Offset(k - 1, j - 1), 0)
            If x < 0 Then x = 0
            If x > 1 Then x = 1
            s = s + x
            rc(i, j) = rc(i, j) + arg1.Cells(i, k) * x
        Next
        If s < 1 Then
            rc(i, k) = rc(i, k) + arg1.Cells(i, k) * (1 - s)
        End If
        Next
        Next
    
    x = 1
    End If
        
    TransistionFromAltPage = rc

End Function

Function UnNormedTransistion(ByRef arg1 As Range, ByVal arg2 As String, ByVal arg3 As String, ByVal arg4 As Integer, arg5, Optional defdiag = 1) As Variant

' arg5 is meaningless for dependency re-calculations
    
    Dim rc
    Dim t
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = n1
    n2 = n1
    
    Dim x As Double
        
    If (n1 = m2) And (m2 = n2) Then
    
        ReDim t(n2, n2) As Double
        For i = 1 To n2
            s = 0
            For j = 1 To n2
                x = ifnull(Range(arg2 & "!" & arg3 & arg4).Offset(i - 1, j - 1).Value, 0)
                If x < 0 Then x = 0
                s = s + x
                t(i, j) = x
            Next
            If s = 0 Then
                t(i, i) = defdiag
            Else
                For j = 1 To n2
                    t(i, j) = t(i, j) / s
                Next
            End If
        Next
        
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
        For j = 1 To n2
        For k = 1 To n2
            rc(i, j) = rc(i, j) + arg1.Cells(i, k) * t(k, j)
        Next
        Next
        Next
    
    End If
        
    UnNormedTransistion = rc

End Function
Function ReDist(ByRef Feeder As Range _
    , _
    ByRef Distributer As Range _
    , _
    ByRef PeriodReward As Range _
    , _
    Optional CarryingCost = 0 _
    , _
    Optional InputIsCDF = 0 _
    , _
    Optional FeederHasDollars = 0 _
    ) As Variant

Dim rc
Dim x As Double
Dim xs As Double

Dim x2 As Double
Dim xs2 As Double

Dim xsrc As Double
Dim xsrc2 As Double

Dim xr As Double
Dim xr2 As Double


m1 = Feeder.Rows.Count
m2 = Distributer.Rows.Count
n2 = Distributer.Columns.Count
m3 = PeriodReward.Rows.Count

ng = Feeder.Columns.Count
If FeederHasDollars Then ng = ng / 2


Dim FeederTally
ReDim FeederTally(Feeder.Rows.Count, 2 * ng) As Double
Dim FeederTally2
ReDim FeederTally2(Feeder.Rows.Count, 2 * ng) As Double

For i = 1 To Feeder.Rows.Count
For j = 1 To 2 * ng
    FeederTally(i, j) = 0
    FeederTally2(i, j) = 0
Next
For j = 1 To Feeder.Columns.Count
    FeederTally(i, j) = Feeder(i, j)
Next
Next

If InputIsCDF Then
For i = 2 To Feeder.Rows.Count
For j = 1 To Feeder.Columns.Count
    FeederTally(i, j) = Feeder(i, j) - Feeder(i - 1, j)
Next
Next
End If

For i = 1 To Feeder.Rows.Count
For j = 1 To ng
    FeederTally2(i, j) = Feeder(i, j)
Next
Next


If ng > 1 Then n2 = Int(n2 / ng)

x2 = 0
ReDim rc(m1, n2 * 3) As Double

For i = 1 To m1
For kk = 1 To ng
    
    xsrc = FeederTally(i, kk)
    xs = xsrc
    xsrc2 = FeederTally(i, kk + ng)
    xs2 = xsrc2
    
    For j = 2 To m2
        jj = i + j - 1
        If jj <= m1 Then
        For k = 1 To n2
        k2 = n2 + k
        k3 = 2 * n2 + k
                             
        If k < n2 Then
                    x = xsrc * Distributer(j, (kk - 1) * n2 + k)
                    xrat = x / (xs + 0.00001)
                    
                    rc(jj, k) = rc(jj, k) + x
                    xs = xs - x
                    
                    xr = x * (ifnull(PeriodReward(ldMin(j, m3), (kk - 1) * n2 + k), 0) + CarryingCost)
                    rc(jj, k2) = rc(jj, k2) + xr
                    
                    rc(jj, k3) = rc(jj, k3) + xs2 * xrat + xr
                    xs2 = xs2 * (1 - xrat)
        Else
                    rc(jj, k) = rc(jj, k) + xs
                    xr = xs * (ifnull(PeriodReward(ldMin(j, m3), (kk - 1) * n2 + k), 0) + CarryingCost)
                    rc(jj, k2) = rc(jj, k2) + xr
                    xs2 = xs2 + xr
                    rc(jj, k3) = rc(jj, k3) + xs2
                    
        End If
        Next
        End If
    
    Next
Next
Next
   
'
'For i = 1 To m1
'    For j = 1 To m2
'        jj = i + j - 1
'        If jj <= m1 Then
'            For k = 1 To n2
'                k2 = n2 + k
'                k3 = 2 * n2 + k
'
'                For kk = 1 To ng
'
'                    xsrc = FeederTally(i, kk)
'
'                    x = xsrc * Distributer(j, (kk - 1) * n2 + k)
'                    xs = FeederTally2(i, kk)
'                    FeederTally2(i, kk) = FeederTally2(i, kk) - x
'
'                    rc(jj, k) = rc(jj, k) + x
'
'
'
'                    xr = (ifnull(PeriodReward(ldMin(j, m3), (kk - 1) * n2 + k), 0) + CarryingCost)
'                    xrs = (xs - x) * xr
'                    xr = xr * x
'
'                    rc(jj, k2) = rc(jj, k2) + xr
'
'If 1 = 0 Then
'                    xsrc2 = FeederTally(i, ng + kk)
'                    x2 = xsrc2 * Distributer(j, (kk - 1) * n2 + k)
'Else
'
'                    x2 = FeederTally2(i, ng + kk) * x / (xs + 0.00001)
'                    FeederTally2(i, ng + kk) = FeederTally2(i, ng + kk) + x2 + xrs
'                    x2 = x2 + FeederTally(i, ng + kk) * Distributer(j, (kk - 1) * n2 + k)
'End If
'
'                    rc(jj, k3) = rc(jj, k3) + x2
'
'
''
''
''                    xs2 = FeederTally2(i, ng + kk)
''
''                    FeederTally2(i, ng + kk) = FeederTally2(i, kk) + xr
''                    FeederTally2(i, ng + kk) = FeederTally2(i, ng + kk) - xs
''
''                    rc(jj, k) = rc(jj, k) + FeederTally(i, kk) * Distributer(j, (kk - 1) * n2 + k)
''                    rc(jj, k2) = rc(jj, k2) + xr
'                    '+ FeederTally2(i, ng + kk) * Distributer(j, (kk - 1) * n2 + k)
'
''                    FeederTally2(i, ng + kk) = FeederTally2(i, ng + kk) * (1 - Distributer(j, (kk - 1) * n2 + k))
'
'                Next
'            Next
'        End If
'    Next
'Next

ReDist = rc

End Function


Function NonNormedTransistion(ByRef arg1 As Range, ByVal arg2 As String, ByVal arg3 As String, ByVal arg4 As Integer, arg5, Optional defdiag = 1, Optional nrm = 1, Optional altewf = 0) As Variant

' arg5 is meaningless for dependency re-calculations


    Dim rc
    Dim t
    Dim t2
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = n1
    n2 = n1
    Dim normitwith As Double
    normitwith = nrm
    
    Dim x As Double
        
    If (n1 = m2) And (m2 = n2) Then
    
        ReDim t(n2, n2) As Double
        For i = 1 To n2
            s = 0
            For j = 1 To n2
                x = ifnull(Range(arg2 & "!" & arg3 & arg4).Offset(i - 1, j - 1).Value, 0) / normitwith
'                If x < 0 Then x = 0
                s = s + x
                t(i, j) = x
            Next
            If s = 0 Then
                t(i, i) = defdiag
            Else
'                For j = 1 To n2
'                    t(i, j) = t(i, j) / s
'                Next
            End If
        Next
        
        If altewf <> 0 Then
        
            ReDim t2(n2, n2) As Double
            For i = 1 To n2
                s = 0
                For j = 1 To n2
                    x = ifnull(Range(arg2 & "!" & arg3 & altewf).Offset(i - 1, j - 1).Value, 0) '/ normitwith
                    If x < 0 Then x = 0
                    s = s + x
                    t2(i, j) = x
                Next
                If s = 0 Then
'                    t2(i, i) = defdiag
                    t2(i, i) = 1
                Else
                    For j = 1 To n2
                        t2(i, j) = t2(i, j) / s
                    Next
                End If
            Next
                
            For i = 1 To n2
            For j = 1 To n2
                t(i, j) = t(i, j) * t2(i, j)
            Next
            Next
        
        
        End If
        
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
        For j = 1 To n2
        For k = 1 To n2
            rc(i, j) = rc(i, j) + arg1.Cells(i, k) * t(k, j)
        Next
        Next
        Next
    
    End If
        
    NonNormedTransistion = rc

End Function
Function NNT(ByRef arg1 As Range, ByVal arg2 As String, ByVal arg3 As String, ByVal arg4 As Integer, arg5, Optional defdiag = 1, Optional nrm = 1, Optional altewf = 0) As Variant
NNT = NonNormedTransistion(arg1, arg2, arg3, arg4, arg5, defdiag, nrm, altewf)

End Function
Function CNNT(ByRef arg1 As Range, ByVal arg2 As String, ByVal arg3 As String, ByVal arg4 As Integer, arg5, Optional defdiag = 1, Optional nrm = 1, Optional altewf = 0) As Variant

' arg5 is meaningless for dependency re-calculations


    Dim rc
    Dim t
    Dim t2
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = n1
    n2 = n1
    Dim normitwith As Double
    normitwith = 1
    capitwith = nrm
    
    
    Dim x As Double
        
    If (n1 = m2) And (m2 = n2) Then
    
        ReDim t(n2, n2) As Double
        For i = 1 To n2
            s = 0
            For j = 1 To n2
                x = ifnull(Range(arg2 & "!" & arg3 & arg4).Offset(i - 1, j - 1).Value, 0) / normitwith
'                If x < 0 Then x = 0
                s = s + x
                t(i, j) = x
            Next
            s = 1
            
            If s = 0 Then
                t(i, i) = defdiag
            Else
                For j = 1 To n2
                    t(i, j) = t(i, j) * s
                Next
            End If
        Next
        
        If altewf <> 0 Then
        
            ReDim t2(n2, n2) As Double
            For i = 1 To n2
                s = 0
                For j = 1 To n2
                    x = ifnull(Range(arg2 & "!" & arg3 & altewf).Offset(i - 1, j - 1).Value, 0) '/ normitwith
                    If x < 0 Then x = 0
                    s = s + x
                    t2(i, j) = x
                Next
                If s = 0 Then
'                    t2(i, i) = defdiag
                    t2(i, i) = 1
                Else
                    For j = 1 To n2
                        t2(i, j) = t2(i, j) / s
                    Next
                End If
            Next
                
            For i = 1 To n2
            For j = 1 To n2
                t(i, j) = t(i, j) * t2(i, j)
            Next
            Next
        
        
        End If
        
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
        For j = 1 To n2
        For k = 1 To n2
            rc(i, j) = rc(i, j) + arg1.Cells(i, k) * t(k, j)
        Next
        Next
        Next
            
        For i = 1 To m1
        s = 0
        For j = 1 To n1
        s = rc(i, j) + s
        Next
            If (capitwith > 0) And (s > capitwith) Then
                s = capitwith / s
            ElseIf capitwith < 0 Then
                s = 0
            Else
                s = 1
            End If
        For j = 1 To n1
            rc(i, j) = rc(i, j) * s
        Next
        Next
    
    End If
        
    CNNT = rc

End Function

Function TransistionFromAltPageWNorm(ByRef arg1 As Range, ByVal arg2 As String, ByVal arg3 As String, ByVal arg4 As Integer, ByVal arg5 As Double) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = n1
    n2 = n1
    
    y = ifnull(arg5, 1)
        
    If (n1 = m2) And (m2 = n2) Then
    
        ReDim rc(m1, n2) As Variant
        For i = 1 To m1
        For k = 1 To n1
        s = 0
        For j = 1 To n2
            x = ifnull(Range(arg2 & "!" & arg3 & arg4).Offset(k - 1, j - 1), 0) ' / y
'            x = ifnull(Range(arg2 & "!" & arg3 & arg4).Offset(k - 1, j - 1), 0)
'            x = Range(arg2 & "!" & arg3 & arg4).Offset(k - 1, j - 1)

            If x < 0 Then x = 0
            If x > 1 Then x = 1
            s = s + x
            rc(i, j) = rc(i, j) + arg1.Cells(i, k) * x
 '           rc(i, j) = Range(arg2 & "!" & arg3 & arg4).Offset(k - 1, j - 1)
 '           rc(i, j) = x
        Next
'        If s < 1 Then
'            rc(i, k) = rc(i, k) + arg1.Cells(i, k) * (1 - s)
'        End If
        Next
        Next
    
    x = 1
    End If
        
    TransistionFromAltPageWNorm = rc

End Function

Function ElementWiseNotIsBlank(ByRef arg1 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    
    
    ReDim rc(m1, n1) As Double
    For i = 1 To m1
        For j = 1 To n1
            rc(i, j) = 1 + (IsEmpty(arg1.Cells(i, j)))
        Next
    Next
    ElementWiseNotIsBlank = rc


End Function
Function ElementWiseIsNonNeg(ByRef arg1 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    
    
    ReDim rc(m1, n1) As Double
    For i = 1 To m1
        For j = 1 To n1
            If Not IsEmpty(arg1.Cells(i, j)) Then
            If arg1.Cells(i, j).Value >= 0 Then
                rc(i, j) = 1
            End If
            End If
        Next
    Next
    ElementWiseIsNonNeg = rc


End Function
Function ElementIsNonNeg(ByRef x As Range, ByVal i As Integer, ByVal j As Integer)

TryIt:
    On Error GoTo CatchIt:
    
    If IsEmpty(x.Cells(i, j)) Then
        ElementIsNonNeg = 0
    ElseIf x.Cells(i, j) >= 0 Then
        ElementIsNonNeg = 1
    End If
    GoTo ElseIt:
CatchIt:
    ElementIsNonNeg = 0
ElseIt:

End Function
Function ElementWiseMult(ByRef arg1 As Range, ByRef arg2 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = arg2.Rows.Count
    n2 = arg2.Columns.Count
    
    If n1 = n2 And m1 = m2 Then
    
        ReDim rc(m1, n2) As Double
        For i = 1 To m1
            For j = 1 To n2
                rc(i, j) = arg1(i, k) * arg2(i, j)
            Next
        Next
        ElementWiseMult = rc
    
    End If
    
End Function
Function ElementWiseDiv(ByRef arg1 As Range, ByRef arg2 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = arg2.Rows.Count
    n2 = arg2.Columns.Count
    
    If (n1 = 1 And m1 = 1) Or (n2 = 1 And m2 = 1) Or (n1 = n2 And m1 = m2) Then
    
        ReDim rc(ldMax(m1, m2), ldMax(n1, n2)) As Double
        For i = 1 To ldMax(m1, m2)
            For j = 1 To ldMax(n1, n2)
                rc(i, j) = arg1(ldMin(i, m1), ldMin(j, n1)) / arg2(ldMin(i, m2), ldMin(j, n2))
            Next
        Next
        ElementWiseDiv = rc
    
    End If
    
End Function
Function ElementWiseNonZeroDiv(ByRef arg1 As Range, ByRef arg2 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    m2 = arg2.Rows.Count
    n2 = arg2.Columns.Count
    
    If (n1 = 1 And m1 = 1) Or (n2 = 1 And m2 = 1) Or (n1 = n2 And m1 = m2) Then
    
        ReDim rc(ldMax(m1, m2), ldMax(n1, n2)) As Double
        For i = 1 To ldMax(m1, m2)
            For j = 1 To ldMax(n1, n2)
                If arg2(ldMin(i, m2), ldMin(j, n2)) <> 0 Then
                    rc(i, j) = arg1(ldMin(i, m1), ldMin(j, n1)) / arg2(ldMin(i, m2), ldMin(j, n2))
                End If
            Next
        Next
        ElementWiseNonZeroDiv = rc
        
    End If
    
End Function
Function RowNormIt(ByRef arg1 As Variant, m1, n1) As Variant

    Dim rc As Variant
'    m1 = arg1.Rows.Count
'    n1 = arg1.Columns.Count
    
    
    ReDim rc(m1, n1) As Double
    For i = 1 To m1
        s = 0
        For j = 1 To n1
        If arg1(i, j) > 0 Then
            s = s + arg1(i, j)
        End If
        Next
        If s > 0 Then
            For j = 1 To n1
            If arg1(i, j) > 0 Then
                rc(i, j) = arg1(i, j) / s
            Else
                rc(i, j) = 0
            End If
            Next
        Else
            For j = 1 To n1
                rc(i, j) = 0
            Next
        End If
    Next
    RowNormIt = rc

End Function
Function RowNormalization(ByRef arg1 As Range) As Variant

    Dim rc ' As Variant
    m1 = arg1.Rows.Count
    n1 = arg1.Columns.Count
    
    
    ReDim rc(m1, n1) As Double
    Dim s As Double
    
    For i = 1 To m1
        s = 0
        For j = 1 To n1
            s = s + ifnull(arg1(i, j), 0)
        Next
        If s <> 0 Then
            For j = 1 To n1
                rc(i, j) = arg1(i, j) / s
            Next
        Else
            For j = 1 To n1
                rc(i, j) = 0
            Next
        End If
    Next
    RowNormalization = rc

End Function
Function StampFind(ByRef arg1 As Range, ByRef arg2 As Range) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    m2 = arg2.Rows.Count
    n2 = arg2.Columns.Count
    
    Dim i, k As Integer
    
    ReDim rc(m1, 2) As Integer
    For i = 1 To m2
    For k = 1 To n2
        If arg2(i, k) > 0 And arg2(i, k) <= m1 Then
            rc(arg2(i, k), 1) = i
            rc(arg2(i, k), 2) = k
        End If
    Next
    Next

If 0 Then
    For i = 1 To m1
        found = 0
        u = 1
        v = 0
        For k = 1 To m2 * n2
            If found = 0 Then
                If v = n2 Then
                    u = u + 1
                    v = 1
                Else
                    v = v + 1
                End If
                If arg1(i) = arg2(u, v) Then
                    rc(i, 1) = u
                    rc(i, 2) = v
                    found = 1
                End If
            End If
        Next
    Next
End If
    
    StampFind = rc


End Function

Function ColoredStampFind(ByRef arg1 As Range, ByRef arg2 As Range, _
    ByRef arg3 As Range _
    ) As Variant

    Dim rc As Variant
    m1 = arg1.Rows.Count
    m2 = arg2.Rows.Count
    n2 = arg2.Columns.Count
    m3 = arg3.Cells.Count
    
    Dim i, k As Integer
    
    ReDim rc(m1, 3) As Integer
    jj = RGB(255, 255, 255)
    
    ii = 0
    For i = 1 To m2
    For j = 1 To n2
    
        If arg2(i, j).Interior.Color <> jj Then
            ii = ii + 1
            If ii <= m1 Then
                For k = 1 To m3
                    If arg3(k).Interior.Color = arg2(i, j).Interior.Color Then
                        rc(ii, 1) = i
                        rc(ii, 2) = j
                        rc(ii, 3) = arg3(k).Value
                        Exit For
                    End If
                Next
            Else
                Exit For
            End If
        End If
    Next
    Next
                        
                        
       
    ColoredStampFind = rc


End Function


