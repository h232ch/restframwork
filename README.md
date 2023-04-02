# restframwork

## Install
1. pip3 install django==4.1.7
2. pip install djangorestframework==23.0.1
3. pip install django-cors-headers==3.14.0
4. pip install cryptography==40.0.1
5. pip install pymysql
6. Install mysql on the test system
 - DB NAME : mytestdb
 - DB CONNETION INFO : root/123qwe

## Run
1. python manage.py runserver 8000

## Setting
1. python manage.py startapp EmployeeApp
2. python manage.py makemigrations EmployeeApp
3. python manage.py migrate EmployeeApp

## Code
It's related to angularCLI frontend server <br>
`https://github.com/h232ch/angularCli2` <br><br>

You can make employees and department on this application <br>
And manage these with `create`, `read`, `update`, `delete`
