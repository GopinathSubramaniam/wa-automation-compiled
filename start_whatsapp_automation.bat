@echo off

cd /d "D:\Workspace\python\wa-automation-compiled" 

echo Updating software
git pull && call myvenv\Scripts\activate

echo Server will start shortly. Once started please open http://localhost in your browser to access "WhatsApp Bulk Software"

python manage.pyc runserver 80