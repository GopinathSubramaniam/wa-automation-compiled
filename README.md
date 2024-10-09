# wa-automation-compiled


#### Pandas

pip install django==5.0.7
pip install djangorestframework
pip install django-cors-headers
pip install django-import-export
pip install pandas
pip install django-crispy-forms
pip install mysqlclient
pip install selenium
pip install webdriver-manager
pip install openpyxl
pip install psutil
pip install django-background-tasks

##### Instructions

1. Create virtual environment
2. Install dependencies
3. Place chromedriver in "C" drive (C:\chromedriver.exe)
4. update tbl_app_setting
   key: base_session_path, value: D:\Workspace\python\sessions\
   key: template_path, value: D:\Workspace\python\WhatsappAutomation\app_api\static\templates\
   key: downloads_folder_path, value: C:\Users\Mahi\Downloads\
5. Add user credentials in tbl_user (For user login)
6. Add machine name in subscription table

https://google-chrome.en.uptodown.com/windows/versions

##### For Linux

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config

##### Optional

pip install markupsafe

Add chromedriver.exe in the project folder root directory

#### Error

##### Error message:
Pandas requires version '3.1.0' or newer of 'openpyxl' (version '3.0.10' currently installed).

##### Solution:
pip uninstall openpyxl
pip install openpyxl

##### For Apache Configuration

pip install mod_wsgi

python manage.py makemigrations <app_name>
python manage.py migrate <app_name>

Recommended python 3.10
https://www.python.org/downloads/release/python-3100/

##### Add .bat file in startup program

shell:startup

##### Encrypted Password
admin - pbkdf2_sha256$320000$CaPVihub3lLYZWNcRUXmPQ$smYe6qS3AkDFICPArFFwgMGVSmG7dkptjyEg7GScu6g=

##### Start Server

python .\manage.py runserver 80