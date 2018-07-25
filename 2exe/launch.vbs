Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c pdf.bat"
oShell.Run strArgs, 0, false