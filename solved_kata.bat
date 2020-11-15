@echo off
REM Will take add the name of solved kata to the list in solved_katas.txt
REM Will ammend the commit with solution

REM read the name of the file
set kataname=%1

REM add the filename to list
ECHO %kataname%>>solved_katas.txt

REM ammend the commit with new message
git commit --amend -m "solution for %kataname%"