@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
SET /P MODE=EXIT(4) - C4RW(3) - C4R(2) - C4W(1) - C4(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO C4
IF "%MODE%"=="0" GOTO C4
IF "%MODE%"=="1" GOTO C4W
IF "%MODE%"=="2" GOTO C4R
IF "%MODE%"=="3" GOTO C4RW
IF "%MODE%"=="4" GOTO EXIT
:C4
ECHO.
CLS && ECHO #################################################
ECHO ### C4 ######## R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4.py
ECHO.
PAUSE
GOTO START
:C4W
ECHO.
CLS && ECHO #################################################
ECHO ### C4W ####### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4w.py
ECHO.
PAUSE
GOTO START
:C4R
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 MODEL Name (%M%:%MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4R_
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### C4R ####### R E C O R D I N G ##### 24/7 ####
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4r.py %MODEL%
TIMEOUT 30
GOTO C4R_
:C4RW
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 MODEL Name (%M%:%MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4RW_
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### C4RW ###### R E C O R D I N G ##### 24/7 ####
ECHO ############### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4rw.py %MODEL%
TIMEOUT 30
GOTO C4RW_
ENDLOCAL
