Attribute VB_Name = "RACodeToolBar_CommandBars"
Sub abaRACTB_ListCommandBars()
'Base code from the Frye, Freeze, Buckingham book
'page 369

Dim c As CommandBar
Dim i, j As Long

Call abaRACTB_ActivateOrAddSheet("CommandBarsProperties")

i = 2
j = 3
Cells(i, j + 1) = "Name"
Cells(i, j + 2) = "Left"
Cells(i, j + 3) = "Position"
Cells(i, j + 4) = "RowIndex"
Cells(i, j + 5) = "Top"
Cells(i, j + 6) = "Type"
Cells(i, j + 7) = "Visible"
Cells(i, j + 8) = "Width"

i = 3
For Each c In Application.CommandBars
    i = i + 1
    Cells(i, j + 1) = c.Name
    Cells(i, j + 2) = c.Left
    Cells(i, j + 3) = c.Position
    Cells(i, j + 4) = c.RowIndex
    Cells(i, j + 5) = c.Top
    Cells(i, j + 6) = c.Type
    Cells(i, j + 7) = c.Visible
    Cells(i, j + 8) = c.Width
Next c

Dim s As String

i = 2
Cells(i, 1) = "Simple Code To Paste Into CommandBarSettings"
j = 0
s = "if 0=1 then"
j = j + 1
Cells(i + j, 1) = s
For Each c In Application.CommandBars
    i = i + 1
    If c.Visible = True Then
        s = "Elseif c.Name=""" & c.Name & """ then "
        j = j + 1
        Cells(2 + j, 1) = s
        s = "    c.Visible=True"
        j = j + 1
        Cells(2 + j, 1) = s
        s = "    c.Position=" & c.Position
        j = j + 1
        Cells(2 + j, 1) = s
        s = "    c.RowIndex=" & c.RowIndex
        j = j + 1
        Cells(2 + j, 1) = s
        s = "    c.Top=" & c.Top
        j = j + 1
        Cells(2 + j, 1) = s
        s = "''    c.Width=" & c.Width
        j = j + 1
        Cells(2 + j, 1) = s
    End If
Next c
s = "Else"
j = j + 1
Cells(2 + j, 1) = s
s = "''    c.Visible=False"
j = j + 1
Cells(2 + j, 1) = s
s = "EndIf"
j = j + 1
Cells(2 + j, 1) = s


End Sub
Sub abaRACTB_SetCommandBarProperties()
Dim c As CommandBar

For Each c In Application.CommandBars
'Paste Simple Code here

If 0 = 1 Then
ElseIf c.Name = "Worksheet Menu Bar" Then
    c.Visible = True
    c.Position = 1
    c.RowIndex = 1
    c.Top = 0
'    c.Width=1281
ElseIf c.Name = "Standard" Then
    c.Visible = True
    c.Position = 1
    c.RowIndex = 3
    c.Top = 25
'    c.Width=605
ElseIf c.Name = "Formatting" Then
    c.Visible = True
    c.Position = 1
    c.RowIndex = 20
    c.Top = 51
'    c.Width=750
ElseIf c.Name = "Formula Auditing" Then
    c.Visible = True
    c.Position = 1
    c.RowIndex = 3
    c.Top = 25
'    c.Width=231
ElseIf c.Name = "Visual Basic" Then
    c.Visible = True
    c.Position = 1
    c.RowIndex = 20
    c.Top = 51
'    c.Width=278
ElseIf c.Name = "Drawing" Then
    c.Visible = True
    c.Position = 3
    c.RowIndex = 1
    c.Top = 0
'    c.Width=789
ElseIf c.Name = "aapRACodeToolBar" Then
    c.Visible = True
    c.Position = 1
    c.RowIndex = 20
    c.Top = 51
'    c.Width=253
Else
'    c.Visible=False
End If



Next c


End Sub

