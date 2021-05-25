Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "admin-privilege.bat" & Chr(34), 0, False
'WshShell.Run(command, [intWindowStyle]==0=Invisible, [bWaitOnReturn])'
Set WshShell = Nothing