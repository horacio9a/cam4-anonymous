@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
SET /P MODE=EXIT(7) START(6) C4SLR(5) C4FFR(4) C4YTR(3) C4RR(2) C4AW(1) C4A(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO C4A
IF "%MODE%"=="0" GOTO C4A
IF "%MODE%"=="1" GOTO C4AW
IF "%MODE%"=="2" GOTO C4RR
IF "%MODE%"=="3" GOTO C4YTR
IF "%MODE%"=="4" GOTO C4FFR
IF "%MODE%"=="5" GOTO C4SLR
IF "%MODE%"=="6" GOTO START
IF "%MODE%"=="7" GOTO EXIT
:C4A
ECHO.
CLS && ECHO #################################################
ECHO ### C4A ####### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4a.py
ECHO.
PAUSE
GOTO START
:C4AW
ECHO.
CLS && ECHO #################################################
ECHO ### C4AW ###### R E C O R D I N G ###############
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4aw.py
ECHO.
PAUSE
GOTO START
:C4RR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 MODEL Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4RR_
ECHO.
SET MODELNAME=%MODEL% #######################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### C4RR ###### R E C O R D I N G ###### 24/7 ###
ECHO ### RTMP ###### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4rr.py %MODEL%
TIMEOUT 30
GOTO C4RR_
:C4YTR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 MODEL Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4YTR_
ECHO.
SET MODELNAME=%MODEL% #######################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### C4YTR ##### R E C O R D I N G ###### 24/7 ###
ECHO ### YTDL ###### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ytr.py %MODEL%
TIMEOUT 30
GOTO C4YTR_
:C4FFR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 MODEL Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4FFR_
ECHO.
SET MODELNAME=%MODEL% #######################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### C4FFR ##### R E C O R D I N G ###### 24/7 ###
ECHO ### FFMPEG #### %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ffr.py %MODEL%
TIMEOUT 30
GOTO C4FFR_
:C4SLR
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 MODEL Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/Windows/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4SLR_
ECHO.
SET MODELNAME=%MODEL% #######################################
SET _MODEL_=%MODELNAME:~0,33%
ECHO.
CLS && ECHO #################################################
ECHO ### C4SLR ##### R E C O R D I N G ###### 24/7 ###
ECHO ### SL ######## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4slr.py %MODEL%
TIMEOUT 30
GOTO C4SLR_
:EXIT
GOTO :EOF
ENDLOCAL
