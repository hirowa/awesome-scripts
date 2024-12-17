@echo start
for /r "C:\Path\To\Root\Directory" %%a in (*.bat) do (
   cd "%%~pa"
   call "%%~a"
)
pause
