echo. behave --junit --tags=-skip --no-skipped

cd C:\Users\Eduardo_Sanchez\Documents\automation_python_demoblaze\src

echo. del /f /q .\allure-results

behave -f allure_behave.formatter:AllureFormatter --tags=test --tags=-skip --no-skipped -o .\allure-results ./features -f pretty 

echo. behave -f allure_behave.formatter:AllureFormatter -o .\allure-results -f pretty

pause