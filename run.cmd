@echo off
set PYTHON_DIR=%USERPROFILE%\Downloads\python-3.10.8-amd64-portable
set PATH=%PYTHON_DIR%;%PYTHON_DIR%\Scripts

set FFMPEG_BINARY=%USERPROFILE%\Downloads\ffmpeg-6.0-full_build-shared\ffmpeg-6.0-full_build-shared\bin\ffmpeg.exe
set IMAGEMAGICK_BINARY=%USERPROFILE%\Downloads\ImageMagick-7.1.1-28-portable-Q16-HDRI-x64\magick.exe
python main.py

pause
