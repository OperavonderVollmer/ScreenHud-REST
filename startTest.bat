@echo off
setlocal

cd /d "%~dp0"

title ScreenHud-REST


call ".\.venv\Scripts\activate.bat"

uvicorn main:app --reload
