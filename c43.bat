@ECHO OFF
SETLOCAL EnableDelayedExpansion
:START
CLS
ECHO.
CLS && ECHO #############################################################################
ECHO ###    C A M 4    A N O N Y M O U S    P Y T H O N    3    S C R I P T    ###
ECHO #############################################################################
ECHO.
SET /P MODE=EXIT(6) C4YTR3(5) C4SLR3(4) C4FFR3(3) C43(2) GETOW3(1) GETOA3(0) (ENTER) (%MODE%): 
IF "%MODE%"=="" GOTO GETOA3
IF "%MODE%"=="0" GOTO GETOA3
IF "%MODE%"=="1" GOTO GETOW3
IF "%MODE%"=="2" GOTO C43
IF "%MODE%"=="3" GOTO C4FFR3
IF "%MODE%"=="4" GOTO C4SLR3
IF "%MODE%"=="5" GOTO C4YTR3
IF "%MODE%"=="6" GOTO EXIT
:GETOA3
ECHO.
CLS && ECHO #############################################################
ECHO ### GETOA3 ###  C A M 4   O N L I N E   A L L   L I S T  ####
ECHO #############################################################
cd C:/
COLOR 0F
cd -c4-py
python C4_getOnlineAllModels3.py > C4_Online_All.txt
ECHO.
PAUSE
GOTO START
:GETOW3
ECHO.
CLS && ECHO ###################################################################
ECHO ### GETOW3 ###  C A M 4   O N L I N E   W A N T E D   L I S T  ####
ECHO ###################################################################
cd C:/
COLOR 0F
cd -c4-py
python C4_getOnlineWantedModels3.py > C4_Online_Wanted.txt
ECHO.
PAUSE
GOTO START
:C43
ECHO.
CLS && ECHO ##########################################################
ECHO ### C43 ######  C A M 4  R E C O R D I N G ###############
ECHO ##########################################################
cd C:/
COLOR 0F
cd -c4-py
python c43.py
ECHO.
PAUSE
GOTO START
:C4FFR3
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
:C4FFR3_
ECHO.
CLS && ECHO ##################################################
ECHO ### C4FFR3 #### R E C O R D I N G ################
ECHO ############### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python c4ffr3.py %MODEL%
TIMEOUT 30
GOTO C4FFR3_
:C4SLR3
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
:C4SLR3_
ECHO.
CLS && ECHO ##################################################
ECHO ### C4SLR3 #### R E C O R D I N G ################
ECHO ############### %_MODEL_%
ECHO ##################################################
cd C:/
COLOR 0F
cd -c4-py
python c4slr3.py %MODEL%
TIMEOUT 30
GOTO C4SLR3_
:C4YTR3
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
:C4YTR3_
ECHO.
CLS && ECHO ##################################################
ECHO ### C4YTR3 #### R E C O R D I N G ################
ECHO ############### %_MODEL_%
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
