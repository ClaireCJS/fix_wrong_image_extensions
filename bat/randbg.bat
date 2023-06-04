@Echo OFF
set BGOLD=%_BG
:ReBG
    set FG=%_FG
    SET BG=%@RANDOM[0,15]  
if "%BG%" eq "%FG%"    goto :ReBG
if "%BG%" eq "%BGOLD%" goto :ReBG

set LAST_COLOR_RANDBG=color %FG% on %BG%
   %LAST_COLOR_RANDBG%

