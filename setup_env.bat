@echo off
REM Creates a virtual environment in .venv and installs requirements.txt
if exist .venv (
  echo Virtual environment ".venv" already exists.
) else (
  python -m venv .venv
  if errorlevel 1 (
    echo Failed to create virtual environment. Ensure Python is installed and on PATH.
    exit /b 1
  )
)

REM Activate the venv for this script session and install
call .venv\Scripts\activate
if errorlevel 1 (
  echo Failed to activate virtual environment.
  exit /b 1
)

REM Check for requirements file before installing
if not exist "%~dp0requirements.txt" (
  echo requirements.txt not found in script directory "%~dp0"
  echo Create a requirements.txt containing:
  echo    streamlit
  echo    tensorflow
  echo    pillow
  echo    numpy
  echo Then re-run this script.
) else (
  pip install --upgrade pip
  pip install -r "%~dp0requirements.txt"
)

echo.
echo Setup complete. To activate the environment in a new shell:
echo    call "%~dp0.venv\Scripts\activate"
echo Then run:
echo    streamlit run "%~dp0app.py"
pause
