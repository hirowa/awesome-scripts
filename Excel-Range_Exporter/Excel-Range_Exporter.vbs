Sub ExportRangetoFile()
    Dim wb As Workbook
    Dim saveFile As Variant
    Dim WorkRng As Range
    Dim xTitleId As String
    
    xTitleId = "HiroWa - Selection Exporter"
    
    If Application.Selection.Count = 1 Then
        Set WorkRng = Application.InputBox("Range", xTitleId, Type:=8)
    Else
        Set WorkRng = Application.Selection
    End If
    
    If WorkRng Is Nothing Then
        MsgBox "No range selected"
        Exit Sub
    End If
    
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    
    Set wb = Application.Workbooks.Add
    wb.Worksheets(1).Range("A1").Resize(WorkRng.Rows.Count, WorkRng.Columns.Count).Value = WorkRng.Value

    saveFile = Application.GetSaveAsFilename(fileFilter:="Text Files (*.txt), *.txt")
    
    If saveFile <> False Then
        wb.SaveAs Filename:=saveFile, FileFormat:=xlText, CreateBackup:=False
        wb.Close
    End If
    
    Application.CutCopyMode = False
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
End Sub

'Copyright HiroWa 2023