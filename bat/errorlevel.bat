@Echo OFF


REM             #######  ### ###  #######          ### ### #####   #######  #####  ##   ##    ##    #######  #######
REM             #  #  #   #   #    #    #           #   #    #     #  #  #    #     #   #      #    #  #  #   #    #
REM                #      #   #    #                #   #    #        #       #     ## ##      #       #      #
REM                #      #   #    #  #             #   #    #        #       #     ## ##     # #      #      #  #
REM                #      #####    ####             #   #    #        #       #     # # #     # #      #      ####
REM                #      #   #    #  #             #   #    #        #       #     # # #    #   #     #      #  #
REM                #      #   #    #                #   #    #        #       #     #   #    #####     #      #
REM                #      #   #    #    #           #   #    #   #    #       #     #   #    #   #     #      #    #
REM               ###    ### ###  #######            ###   #######   ###    #####  ### ###  ### ###   ###    #######
REM        
REM        
REM         #######  ######   ######     ###    ######               ####     ##    #######   ####   ### ###  #######  ######
REM          #    #   #    #   #    #   #   #    #    #             #    #     #    #  #  #  #    #   #   #    #    #   #    #
REM          #        #    #   #    #  #     #   #    #            #           #       #    #         #   #    #        #    #
REM          #  #     #    #   #    #  #     #   #    #            #          # #      #    #         #   #    #  #     #    #
REM          ####     #####    #####   #     #   #####             #          # #      #    #         #####    ####     #####
REM          #  #     #  #     #  #    #     #   #  #              #         #   #     #    #         #   #    #  #     #  #
REM          #        #  #     #  #    #     #   #  #              #         #####     #    #         #   #    #        #  #
REM          #    #   #   #    #   #    #   #    #   #              #    #   #   #     #     #    #   #   #    #    #   #   #
REM         #######  ###  ##  ###  ##    ###    ###  ##              ####   ### ###   ###     ####   ### ###  #######  ###  ##


rem      WHEN TO USE?:   * Use after any important command in any workflow, ever.
rem                      * Not only will it halt things on error, but it will set a flag 
rem                        that you can use to repeat your situations until errors cease                   



rem      INSTALLATION:   Requires an alias to be set up to capture values when something is called:
rem                      call=`set _callingerrorlevel=%_? %+ set _callingerrorlevel2=%? %+ set _callingfile=%@full[%%0] %+ *call %$`



rem      USAGE:          call errorlevel.bat                          <---- do this! after everything! everythiiiinnng! any program! any command! at the end of bat-files!
rem                      call errorlevel.bat "fail msg"               <---- if you need a more informative  error message when things go wrong
rem                      call errorlevel.bat "fail msg" "success msg" <---- if you need a more reassuring success message when things go right


rem      SIDE EFFECTS:   
rem                      1) sets %REDO_BECAUSE_OF_ERRORLEVEL% to 1 so you can use that result to re-run your situation infinitely until the error goes away
rem                      2) outputs a .BAT pattern that can be incorporated into calling scripts




@Echo OFF


REM Set debug parameters
    set DEBUG_CALLER_ERRORLEVEL=0


REM Get parameters: error messages
    set OUR_ERRORLEVEL=%_?
    if %DEBUG_CALLER_ERRORLEVEL gt 0 echo OUR_ERRORLEVEL is clearly "%OUR_ERRORLEVEL%", _callingerrorlevel="%_callingerrorlevel%", _callingerrorlevel2="%_callingerrorlevel2%", _callingfile="%_callingfile"

    if not %OUR_ERRORLEVEL% gt 0 .and. %_callingerrorlevel gt 0 set OUR_ERRORLEVEL=%_callingerrorlevel
    if %_callingerrorlevel2 gt          %callingerrorlevel      set OUR_ERRORLEVEL=%_callingerrorlevel2
    
    if %DEBUG_CALLER_ERRORLEVEL gt 0 echo OUR_ERRORLEVEL is **NOW** "%OUR_ERRORLEVEL%", _callingerrorlevel="%_callingerrorlevel%", _callingerrorlevel2="%_callingerrorlevel2%", _callingfile="%_callingfile"

    set OUR_CALLING_FILE=%_callingfile


    REM If there is a %3 then we didn't listen to the invocation instructions and screwed up -- just treat the entire set of parameters as one big error message
    if "%3" ne "" (
        set OUR_FAILURE_MESSAGE=%@UNQUOTE[%*]
        set OUR_SUCCESS_MESSAGE=
    ) else (
        set OUR_FAILURE_MESSAGE=%@UNQUOTE[%1]
        set OUR_SUCCESS_MESSAGE=%@UNQUOTE[%2]
    )


REM Make sure sed is in our path, but the sed part can be removed and this will still work
    call validate-in-path sed


if %OUR_ERRORLEVEL% le 0 (   
    if defined OUR_SUCCESS_MESSAGE (
        @Echo OFF
        %COLOR_SUCCESS%
        echo %OUR_SUCCESS_MESSAGE
        %COLOR_NORMAL%
    )
    set REDO_BECAUSE_OF_ERRORLEVEL=0
)

if %OUR_ERRORLEVEL% gt 0 (   
    set REDO_BECAUSE_OF_ERRORLEVEL=1

    if "%OUR_FAILURE_MESSAGE%" eq "" (
        set OUR_FAILURE_MESSAGE=An ERRORLEVEL of %OUR_ERRORLEVEL% (bad) was returned, which is greater than 0 (good)!
    ) else (
        set OUR_FAILURE_MESSAGE=%OUR_FAILURE_MESSAGE%   [errorlevel=%OUR_ERRORLEVEL%]
    )
    REM call print-if-debug * ARGV is: %*

    set OUR_COMMAND=that_thing_you_did[.exe/.bat/etc]
    if "%OUR_CALLING_FILE%" ne "" (set OUR_COMMAND=%OUR_CALLING_FILE%)

    set   optional_success_msg_in_quotes=[optional_success_msg_in_quotes]
    set   optional_failure_msg_in_quotes=[optional_failure_msg_in_quotes]
    if "%OUR_SUCCESS_MESSAGE%" ne "" (set optional_success_msg_in_quotes=%@QUOTE[%OUR_SUCCESS_MESSAGE])
    if "%OUR_FAILURE_MESSAGE%" ne "" (set optional_failure_msg_in_quotes=%@QUOTE[%OUR_FAILURE_MESSAGE]
                                      set optional_failure_msg_in_quotes=%@EXECSTR[echo %optional_failure_msg_in_quotes|sed -r 's/ *\[errorlevel\=[0-9]+\]//'])

    echo.
    color bright white on blue
    echos %OUR_FAILURE_MESSAGE%
    %COLOR_NORMAL% 
    echo.
    echo.
    echo.
    call advice - You can put code like this in your file:
    call advice "     :Redo_1"
    call advice "             %OUR_COMMAND%" 
    REM call advice "             call %0 %optional_success_msg_in_quotes% %optional_failure_msg_in_quotes%"
    %COLOR_ADVICE%
    echos              ``
    echo call %0 %optional_success_msg_in_quotes% %optional_failure_msg_in_quotes%
    REM having to use 64 or 128 percent signs to sextuple-escape the character is lifetime-level madness
    call advice "     if %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%REDO_BECAUSE_OF_ERRORLEVEL eq 1 (goto :Redo_1)"
    echo.
    beep
    setlocal
        set NOPAUSE=0
        pause
        pause
        pause
        pause
        pause
    endlocal
)
