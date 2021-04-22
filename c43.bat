@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
CLS && ECHO #######################################################################
ECHO ###   C A M 4   A N O N Y M O U S   P Y T H O N   3   S C R I P T   ###
ECHO #######################################################################
ECHO.
SET /P MODE=EXIT(5)  C4YTR3(4)  C4SLR3(3)  C4FFR3(2)  C4RR3(1)  C43(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO C43
IF "%MODE%"=="0" GOTO C43
IF "%MODE%"=="1" GOTO C4RR3
IF "%MODE%"=="2" GOTO C4FFR3
IF "%MODE%"=="3" GOTO C4SLR3
IF "%MODE%"=="4" GOTO C4YTR3
IF "%MODE%"=="5" GOTO EXIT
:C43
ECHO.
CLS && ECHO #################################################
ECHO ### C4 #####  P Y T H O N   R E C / P L A Y  ####
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c43.py
ECHO.
PAUSE
GOTO START
:C4RR3
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4RR3_
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,34%
ECHO.
CLS && ECHO ##################################################
ECHO ### C4RR3 ###### P Y T H O N   R E C #### 24/7 ###
ECHO ### RTMP ###### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python c4rr3.py %MODEL%
TIMEOUT 30
GOTO C4RR3_
:C4FFR3
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4FFR3_
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,34%
ECHO.
CLS && ECHO ##################################################
ECHO ### C4FFR3 ##### P Y T H O N   R E C #### 24/7 ###
ECHO ### FFMPEG #### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ffr3.py %MODEL%
TIMEOUT 30
GOTO C4FFR3_
:C4SLR3
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4SLR3_
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,34%
ECHO.
CLS && ECHO ##################################################
ECHO ### C4SLR3 ##### P Y T H O N   R E C #### 24/7 ###
ECHO ### SL ######## %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python c4slr3.py %MODEL%
TIMEOUT 30
GOTO C4SLR3_
:C4YTR3
ECHO.
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M% %MODEL%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Model.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
:C4YTR3_
ECHO.
SET MODELNAME=%MODEL% ############ %M% ############################
SET _MODEL_=%MODELNAME:~0,34%
ECHO.
CLS && ECHO ##################################################
ECHO ### C4YTR3 ##### P Y T H O N   R E C #### 24/7 ###
ECHO ### YTDL ###### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ytr3.py %MODEL%
TIMEOUT 30
GOTO C4YTR3_
:EXIT
GOTO :EOF
ENDLOCAL
