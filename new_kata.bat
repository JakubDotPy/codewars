@echo off
REM Will take name of new kata as argument and prepare the file by copying template

REM read the name of the file
set filename=%1

REM copy and delete pytestmark line
findstr /v /c:"pytestmark" template.py >katas\%filename%.py
