@Echo OFF

REM     I actually do all my development for this in my personal live command line environment,
REM     so for me, these files actually "live" in "c:\bat\" and just need to be refreshed to my 
REM     local GIT repo beore doing anything significant.  Or really, before doing anything ever.


rem VALIDATION & SETUP:
        set SOURCE_DIR=%BAT%
        set COPY=*copy /E /R /Z /Ns
        call validate-environment-variables MANIFEST_FILES BAT SOURCE_DIR COPY
        call validate-in-path important_less success errorlevel

rem TELL USER:
        echo.
        call important_less "Updating files from runtime locations..."
        echo.
        color bright black on black

rem DO COPIES:
        for %myFileFull in (%MANIFEST_FILES%) (
            set myFile=%@UNQUOTE[%myFileFull]
            if not exist %SOURCE_DIR%\%myFile% (call error "Uh oh! Project source file %myFile% doesn't seem to exist in %SOURCE_DIR%")
            attrib -r                       %myFile% >nul
            *del   /z /q                    %myFile%
            echos   y | %COPY% %SOURCE_DIR%\%myFile% .
            call errorlevel
            attrib +r                       %myFile% >nul
        )

rem SHARE REQUIRED BAT FILES THAT WE USE, FOR FURTHER GIGGLES:
        if not defined SECONDARY_BAT_FILES goto :no_secondary_bat_files
            set SOURCE_DIR=c:\bat\
            if not isdir BAT mkdir BAT
            call validate-environment-variable SOURCE_DIR
            for %bat_file_to_copy in (%SECONDARY_BAT_FILES%) (
                call randfg
                echos .
                set COMMENT=call debug "considering %bat_file_to_copy%"
                set myBatFileToCopy=%@UNQUOTE[%bat_file_to_copy]
                set myBatFileToCopyWithPath=%SOURCE_DIR%\%myBatFileToCopy%
                call validate-environment-variable myBatFileToCopyWithPath "Uh oh! Project source bat file %myBatFileToCopy% doesn't seem to exist in %SOURCE_DIR%"
                set COMMENT=if not exist  (call error "Uh oh! Project source bat file %myBatFileToCopy% doesn't seem to exist in %SOURCE_DIR%")
                set myBatFileTargetWithPath=BAT\%myBatFileToCopy%
                color bright black on black
                if exist %myBatFileTargetWithPath% attrib -r %myBatFileTargetWithPath%>nul
                echo y | %COPY% /md /u %myBatFileToCopyWithPath% %myBatFileTargetWithPath%
                call validate-environment-variable myBatFileTargetWithPath "Why isn't %myBatFileTargetWithPath% there?"
                attrib +r %myBatFileTargetWithPath%>nul
            )
        :no_secondary_bat_files

rem CELEBRATE:
        echo.
        call success "Successfully updated from runtime locations into this repo :)"





