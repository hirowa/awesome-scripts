@echo off
REM Extract CAUTH key from cauth.txt
for /f "usebackq tokens=2 delims==" %%a in ("cauth.txt") do set CAUTH_KEY=%%a

REM Trim whitespace from CAUTH_KEY
for /f "tokens=* delims= " %%b in ("%CAUTH_KEY%") do set CAUTH_KEY=%%b

REM Extract first 5 and last 5 characters
set FIRST_PART=%CAUTH_KEY:~0,5%
set LAST_PART=%CAUTH_KEY:~-5%
set OBFUSCATED_KEY=%FIRST_PART%*****%LAST_PART%

REM Display the obfuscated CAUTH key
echo Extracted CAUTH Key: %OBFUSCATED_KEY%

REM Prompt user to enter course name
set /p COURSE_NAME=Enter the course name: 

REM Activate the virtual environment
call coursera_venv\Scripts\activate.bat

REM Run coursera-dl with the CAUTH key and course name
coursera-dl -ca %CAUTH_KEY% %COURSE_NAME% --subtitle-language en

pause
