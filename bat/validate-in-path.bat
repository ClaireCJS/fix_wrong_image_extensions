@echo off
for %arg in (%*) do (
    set search=%@SEARCH[%arg]

    REM echo * search = %search%
    if "%search%" eq "" (
        %COLOR_ERROR%
            call fatalerror "FATAL ERROR! %arg is not in your path, and needs to be."
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
            pause
    )
)
