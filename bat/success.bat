@Echo OFF

set MSG=%*
if "%1" eq "" set MSG=*** Success!!! ***

call print-message success %MSG%
goto :END

            :LEGACY
                    call AlarmCharge
                    %COLOR_SUCCESS% %+ echos *** Success!!! ***
                    %COLOR_NORMAL%  %+ echo.

:END
