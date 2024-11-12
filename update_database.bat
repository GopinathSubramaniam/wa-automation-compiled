@echo off

cd /d "D:\Workspace\python\wa-automation-compiled" 

echo Updating software
git pull && call myvenv\Scripts\activate

echo updating database
python manage.pyc makemigrations app_api && python manage.pyc migrate app_api