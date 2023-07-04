@Echo OFF

REM     I actually do all my development for this in my personal live command line environment,
REM     so for me, these files actually "live" in "c:\bat\" and just need to be refreshed to my 
REM     local GIT repo beore doing anything significant.  Or really, before doing anything ever.


rem CONFIGURATION:
        SET MANIFEST_FILES=fix_wrong_image_extensions.py
        SET SECONDARY_BAT_FILES=update-from-BAT-via-manifest.bat  validate-in-path.bat validate-environment-variables.bat validate-environment-variable.bat white-noise.bat car.bat nocar.bat important_less.bat error.bat fatalerror.bat errorlevel.bat advice.bat print-message.bat randcolor.bat success.bat debug.bat randfg.bat randbg.bat 
                            REM ^^^^^^^^^^^ Note to self: this is just the basic set, nothing related to exe building



REM        ************ Remember to git-add any new files brought in! ************


call update-from-BAT-via-manifest.bat



