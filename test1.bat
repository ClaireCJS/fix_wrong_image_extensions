@Echo off

set TESTING_SCRIPT=test_1_function_remove_duplicate_extension.py

echo TESTING_SCRIPT iS %TESTING_SCRIPT%

call validate-in-path update-from-bat %TESTING_SCRIPT%
call update-from-bat

cls

python %TESTING_SCRIPT%

