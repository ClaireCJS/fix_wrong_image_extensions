@Echo OFF

for %ee in (%*) do (
    call %BAT%\validate-environment-variable %ee
)
