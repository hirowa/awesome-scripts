@echo start
for /r "E:\Documents\PARA\1. Projects\Echoes of Magic - Ethereal Spaces\Assets\Exteriors" %%a in (*.bat) do (
   cd "%%~pa"
   call "%%~a"
)
pause