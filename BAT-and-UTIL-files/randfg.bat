@Echo OFF

:: Unfortunately, these internal variables don't actually work right:
    set OLDFG=%_FG
    set OLDBG=%_BG  





:ReBG
    ::8,15 = bright colors only // 0,15 = all colors
    SET FG=%@RANDOM[8,15]                           
    set NEXT_COLOR=%FG% on black

if "%NEXT_COLOR%" eq "%LAST_COLOR%" goto :ReBG






set LAST_COLOR_RANDFG_FULLCMD=color %NEXT_COLOR%
   %LAST_COLOR_RANDFG_FULLCMD%

