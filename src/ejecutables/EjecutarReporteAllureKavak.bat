echo. 
cd C:\Users\Eduardo_Sanchez\Documents\proyectosTrabajo\automation_testing\src
rmdir /s /q .\allure-results
python -m pytest .\features\Kavak\CPA_20_Pre_Approval.feature  --alluredir .\allure-results


pause


