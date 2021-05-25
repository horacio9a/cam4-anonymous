@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
CLS && ECHO #############################################################################
ECHO ###    C A M 4    A N O N Y M O U S    P Y T H O N    2    S C R I P T    ###
ECHO #############################################################################
ECHO.
SET /P MODE=EXIT(7) - C4YTR(6) - C4SLR(5) - C4SLR(4) - C4FFR(3) - C4(2) -  GETOW(1) - GETOA(0)(ENTER)(%MODE%): 
IF "%MODE%"=="" GOTO GETOA
IF "%MODE%"=="0" GOTO GETOA
IF "%MODE%"=="1" GOTO GETOW
IF "%MODE%"=="2" GOTO C4
IF "%MODE%"=="3" GOTO C4FFR
IF "%MODE%"=="4" GOTO C4SLR
IF "%MODE%"=="5" GOTO C4LSR
IF "%MODE%"=="6" GOTO C4YTR
IF "%MODE%"=="7" GOTO EXIT
:GETOA
ECHO.
CLS && ECHO ##################################################
ECHO ### GETOA ###  O N L I N E   A L L   L I S T  ####
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python C4_getOnlineAllModels.py > C4_Online_All.txt
ECHO.
PAUSE
GOTO START
:GETOW
ECHO.
CLS && ECHO ########################################################
ECHO ### GETOW ###  O N L I N E   W A N T E D   L I S T  ####
ECHO ########################################################
cd C:/
COLOR 0F
cd -c4-py
python C4_getOnlineWantedModels.py > C4_Online_Wanted.txt
ECHO.
PAUSE
GOTO START
:C4
ECHO.
CLS && ECHO ###############################################
ECHO ### C4 ###### R E C O R D I N G ###############
ECHO ###############################################
cd C:/
COLOR 0F
cd -c4-py
python c4.py
ECHO.
PAUSE
GOTO START
:C4FFR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:C4FFR_
ECHO.
CLS && ECHO #################################################
ECHO ### C4FFR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ffr.py %MODEL%
TIMEOUT 30
GOTO C4FFR_
:C4SLR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:C4SLR_
ECHO.
CLS && ECHO #################################################
ECHO ### C4SLR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4slr.py %MODEL%
TIMEOUT 30
GOTO C4SLR_
:C4LSR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:C4LSR_
ECHO.
CLS && ECHO #################################################
ECHO ### C4LSR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4lsr.py %MODEL%
TIMEOUT 30
GOTO C4LSR_
:C4YTR
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
SET _fav!n!=%%A
ECHO !n! %%A
)
ECHO.
SET /P MODEL=Choose C4 Model Name (%M%): 
FOR /L %%f IN (1,1,!n!) DO (
IF /I '%MODEL%'=='%%f' SET M=%%f
)
SET n=0
FOR /F "tokens=*" %%A IN (C:/-c4-py/C4_Wanted.txt) DO (
SET /A n=n+1
IF !n!==%M% SET MODEL=%%A
)
ECHO.
SET MODELNAME=%MODEL% #####################################
SET _MODEL_=%MODELNAME:~0,34%
:C4YTR_
ECHO.
CLS && ECHO #################################################
ECHO ### C4YTR #### R E C O R D I N G ################
ECHO ############## %_MODEL_%
ECHO #################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ytr.py %MODEL%
TIMEOUT 30
GOTO C4YTR_
:EXIT
GOTO :EOF
ENDLOCAL
