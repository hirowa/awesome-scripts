@echo off

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python first.
    pause
    exit /b
)

REM Create and activate virtual environment
if not exist venv (
    python -m venv venv
)

REM Activate virtual environment (Windows)
call venv\Scripts\activate.bat

REM Upgrade pip and install dependencies (tkinter is bundled with Python)
pip install --upgrade pip
pip install opencv-python numpy pillow svgwrite cairosvg

REM Run the script
python Win-Image_Stipple_Effect.py

REM Optional: Deactivate virtual environment
call venv\Scripts\deactivate.bat

REM Keep the window open
pause
