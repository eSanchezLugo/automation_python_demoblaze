echo. 
cd C:\Users\Eduardo_Sanchez\Documents\proyectosTrabajo\automation_testing\src
rmdir /s /q .\allure-results
python -m pytest .\tests\Kikoya\CPA_10_Iniciar_Sesion.py  --alluredir .\allure-results


pause


