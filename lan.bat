@echo off

for /f "tokens=1-2 delims=:" %%a in ('ipconfig^|find "IPv4"') do set ip=%%b
set ip=%ip:~1%
echo %ip%

python3 manage.py runserver %ip%:8000

py -3 manage.py runserver %ip%:8000