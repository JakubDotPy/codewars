@echo off
REM Will take name of new kata as argument and prepare the file by copying template

REM read the name of the file
set kataname=%1

REM copy and delete pytestmark line
findstr /v /c:"pytestmark" template.py >katas\%kataname%.py

REM add to git
git add katas\%kataname%.py
git commit -m "added file for %kataname%"