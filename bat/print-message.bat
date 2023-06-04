@Echo Off

REM usage call %0 MESSAGE_TYPE "message" [0|1]               - arg1=message/colorType, arg2=message, arg3=pause (1) or not (0)
REM usage call %0 message without quotes                     - no 3rd arg of 0|1 will cause the whole line to be treated as the message
REM                               NOTE: arg1 must match a color type i.e. "ERROR" "WARNING" "DEBUG" "SUCCESS" "IMPORTANT" "INPUT" "LESS_IMPORTANT", etc

REM DEBUG:
    set DEBUG_PRINTMESSAGE=0

REM Initialize variables
    set TYPE=
    set MESSAGE=Null
    set DO_PAUSE=-666
    set OUR_COLORTOUSE=

REM Process parameters
    if %3 GE 0 .and. %3 LE 1 (
        if "%3" eq "1"     (set DO_PAUSE=1)
        if "%2" eq "yes"   (set DO_PAUSE=1)                         %+ REM capture a few potential call mistakes
        if "%2" eq "pause" (set DO_PAUSE=1)                         %+ REM capture a few potential call mistakes
        set MESSAGE=%@UNQUOTE[`%2`]
        if %DEBUG_PRINTMESSAGE% eq 1 echo debug branch 1 because %%3 is %3 - btw %%2=%2 - message is now %MESSAGE
        set TYPE=%1                                                 %+ REM both the color and message type
    ) else (
        set MESSAGE=%@UNQUOTE[`%*`]
        if %DEBUG_PRINTMESSAGE% eq 1 echo debug branch 2: message is now %MESSAGE
        REM set TYPE=NORMAL                                         making this assumption hurts flexibility for misshappen calls to this script. We like to alzheimer's-proof things around here.
        REM set OUR_COLORTOUSE=%COLOR_NORMAL%                       making this assumption hurts flexibility for misshappen calls to this script. We like to alzheimer's-proof things around here.
        REM changed my mind: set DO_PAUSE=1                         we pause by default becuase calling this way means the user doesn't know what they are doing quite as well
    )
    if %DEBUG_PRINTMESSAGE% eq 1 (echo DEBUG: TYPE=%TYPE%,DO_PAUSE=%DO_PAUSE%,MESSAGE=%MESSAGE%)
    if defined COLOR_%TYPE% (set OUR_COLORTOUSE=%[COLOR_%TYPE%])
    if not defined OUR_COLORTOUSE  (
        if %DEBUG_PRINTMESSAGE% eq 1 (echo - Oops! Let's try setting OUR_COLORTOUSE to %%COLOR_%@UPPER[%1])
        set TYPE=%1
        set OUR_COLORKEY=COLOR_%TYPE%
        if %DEBUG_PRINTMESSAGE% eq 1 (
            echo colorkey is %OUR_COLORKEY%
            echo     next is %[%OUR_COLORKEY%]
        )
        set OUR_COLORTOUSE=%[%OUR_COLORKEY%]
        set MESSAGE=%@UNQUOTE[`%2$`]
    )
    if %DEBUG_PRINTMESSAGE% eq 1 (echo TYPE=%TYPE% OUR_COLORTOUSE=%OUR_COLORTOUSE% DO_PAUSE=%DO_PAUSE% MESSAGE is: %MESSAGE% )

REM Validate parameters
    call validate-environment-variable  TYPE 
    call validate-environment-variable  COLOR_%TYPE% "This variable should be an existing COLOR_* variable in our environment"
    call validate-environment-variables OUR_COLORTOUSE DO_PAUSE 
    call validate-environment-variable  MESSAGE skip_validation_existence
    set MESSAGE=%@UNQUOTE[%MESSAGE%]

REM Behavior overides and message decoarators depending on the type of message?
    if %DO_PAUSE% ne 1 .and. "%TYPE%" eq "ERROR" (set DO_PAUSE=1 %+ echo.)                                                         %+ REM pause always when error
    if  "%TYPE%"  eq "DEBUG"          set MESSAGE=- DEBUG: %MESSAGE%
    if  "%TYPE%"  eq "IMPORTANT_LESS" set MESSAGE=* %MESSAGE%
    if  "%TYPE%"  eq "IMPORTANT"      set MESSAGE=* %MESSAGE%
    if  "%TYPE%"  eq "WARNING"        set MESSAGE=! %MESSAGE% !
    if  "%TYPE%"  eq "CELEBRATION"    set MESSAGE=*** %MESSAGE%! ***
    if  "%TYPE%"  eq "ERROR"          set MESSAGE=***** %MESSAGE% ******

REM Actually output the message!
    if %DO_PAUSE% eq 1 (echo.)                                                                                                     %+ REM pausable messages need a litle visual cushion
    %OUR_COLORTOUSE% %+ echos %MESSAGE% %+ %COLOR_NORMAL% %+ echo.

REM Sounds Effects depending on type of message?
    :DEBUG: echo type=%TYPE%
    if "%TYPE%" eq "ERROR"   (beep 145 1 ^ beep 120 1 ^ beep 100 1 ^ beep 80 1 ^ beep 65 1 ^ beep 50 1 ^ beep 40 1)                %+ REM sound effect: errors
    if "%TYPE%" eq "WARNING" (
        beep  60 1  
        beep  69 1                                                                                                   
        delay 2                                                                                                                    %+ REM delay for warnings
    )                                                                                                                              

    

REM Pause if we've decided to pause...
    if %DO_PAUSE% eq 1 (
        echo.
        call randcolor %+ *pause %+ %COLOR_NORMAL%
        call randcolor %+ *pause %+ %COLOR_NORMAL%
        call randcolor %+ *pause %+ %COLOR_NORMAL%
        call randcolor %+ *pause %+ %COLOR_NORMAL%
        call randcolor %+ *pause %+ %COLOR_NORMAL%
    )
