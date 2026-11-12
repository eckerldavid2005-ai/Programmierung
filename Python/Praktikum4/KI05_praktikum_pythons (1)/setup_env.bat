@echo off
rem setup_env.bat - Startet setup_env.py unter Windows (Doppelklick reicht).
rem Versucht zuerst den Python Launcher "py", danach "python" vom PATH.
rem Fuer den CIP-Pool mit separatem venv-Laufwerk:
rem   setup_env.bat --venv-dir U:\KI.venv

cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 setup_env.py %*
) else (
    python setup_env.py %*
)

if errorlevel 1 (
    echo.
    echo FEHLER: Setup wurde nicht erfolgreich abgeschlossen.
)
echo.
pause
