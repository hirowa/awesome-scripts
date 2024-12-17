@echo off
REM GridCreator.bat - Batch script to create a grid of images using ImageMagick.

REM Step 1: Set variables for output file names
set OUTPUT_FILE=Grid.png
set RESIZED_OUTPUT_FILE=ResizedGrid.png

REM Step 2: Create the image grid
echo Creating image grid...
magick montage -density 300 -geometry +0+0 -tile 3x0 *.png %OUTPUT_FILE%

REM Check if the grid was created successfully
if exist %OUTPUT_FILE% (
    echo Grid created successfully: %OUTPUT_FILE%
) else (
    echo Error: Grid could not be created.
    exit /b 1
)

REM Step 3: Resize the grid (optional)
set /p RESIZE_CHOICE="Do you want to resize the grid? (Y/N): "
if /i "%RESIZE_CHOICE%"=="Y" (
    set /p RESIZE_DIMENSIONS="Enter the desired dimensions (e.g., 100x100): "
    echo Resizing grid to %RESIZE_DIMENSIONS%...
    magick convert %OUTPUT_FILE% -resize %RESIZE_DIMENSIONS% %RESIZED_OUTPUT_FILE%
    
    REM Check if the resized grid was created successfully
    if exist %RESIZED_OUTPUT_FILE% (
        echo Resized grid created successfully: %RESIZED_OUTPUT_FILE%
    ) else (
        echo Error: Resized grid could not be created.
    )
) else (
    echo Skipping resizing step.
)

echo Done.
pause
