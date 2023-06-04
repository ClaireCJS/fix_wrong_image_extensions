@Echo off

set TESTING_SCRIPT=test_2_main.py

echo TESTING_SCRIPT iS %TESTING_SCRIPT%

call validate-in-path update-from-bat %TESTING_SCRIPT%
call update-from-bat

cls

python %TESTING_SCRIPT%

