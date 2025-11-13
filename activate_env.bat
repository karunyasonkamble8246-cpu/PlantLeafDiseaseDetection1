@echo off
REM Activate the project virtual environment
if exist .venv\Scripts\activate (
  call .venv\Scripts\activate
) else (
  echo Virtual environment not found. Run setup_env.bat first.
)
