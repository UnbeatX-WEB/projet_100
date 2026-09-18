@echo off
title HORLOGE
:loop
cls
echo ===============
echo     HORLOGE
echo ===============
echo.
echo Heure : 
time /t
echo.
timeout /t 1 >nul
goto loop
