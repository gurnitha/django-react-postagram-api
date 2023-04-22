## Membuat Aplikasi Sosial Media 'Postagram' Menggunakan Django v4 dan React 18

[Github repo](https://github.com/gurnitha/django-react-postagram-api)
[Proyek](F:\_ingafter65\DJANGO-REACT-SOSMED-POSTAGRAM\django-react-postagram-api)


## Part 1: Technical Background

        Activitas:

        modified:   .gitignore
        modified:   README.md


### 1. Creating a Django Project

        Activitas:

        modified:   .gitignore


#### 1.1 Setting up the work environment

        Activitas:

        1. Instal node, python 3, pip, dan virtualenv
        2. Memastikan versi yang terinstal


#### 1.2 Creating a virtual environment and install django v4.0

        Activitas:

        F:\_ingafter65\DJANGO-REACT-SOSMED-POSTAGRAM\django-react-postagram-api

        1. Create venv
        λ python -m venv venv3940

        2. Activate venv
        λ venv3940\Scripts\activate.bat

        3. Create requirements.txt
        (venv3940) λ touch requirements.txt

        4. Add Django==4.0 to requirements.txt

        5. Instal django
        (venv3940) λ pip install -r requirements.txt

        6. Upgrade pip
        (venv3940) λ python.exe -m pip install --upgrade pip

        modified:   README.md
        new file:   requirements.txt
        new file:   venv3940/Scripts/Activate.ps1
        new file:   venv3940/Scripts/activate
        new file:   venv3940/Scripts/activate.bat
        new file:   venv3940/Scripts/deactivate.bat
        new file:   venv3940/Scripts/django-admin.exe
        new file:   venv3940/Scripts/pip.exe
        new file:   venv3940/Scripts/pip3.10.exe
        new file:   venv3940/Scripts/pip3.9.exe
        new file:   venv3940/Scripts/pip3.exe
        new file:   venv3940/Scripts/python.exe
        new file:   venv3940/Scripts/pythonw.exe
        new file:   venv3940/Scripts/sqlformat.exe
        new file:   venv3940/pyvenv.cfg


#### 1.3 Creating a sample project

        Activitas:

        1. Membuat proyek
        (venv3940) λ django-admin startproject CoreRoot .

        2. Jalankan migrasi
        (venv3940) λ python manage.py migrate

        3. Jalankan server
        (venv3940) λ python manage.py runserver

        4. Lihat hasilnya di browser
        http://127.0.0.1:8000/

        NOTE: berhasil

        new file:   CoreRoot/__init__.py
        new file:   CoreRoot/asgi.py
        new file:   CoreRoot/settings.py
        new file:   CoreRoot/urls.py
        new file:   CoreRoot/wsgi.py
        modified:   README.md
        new file:   manage.py

        NEXT: Postgres configuration (Create database)


#### 1.4 Postgres configuration (Create database)

        Activitas:

        1. Login

        λ psql -U postgres
        Password for user postgres:
        psql (13.0, server 15.1)
        ...
        postgres=#

        2. Create database

        postgres=# CREATE DATABASE coredb;
        CREATE DATABASE

        3. Create user with password

        postgres=# CREATE USER core WITH PASSWORD 'wCh29&HE&T83';
        CREATE ROLE

        4. Grant privileges on database (coredb) to user (core)
        postgres=# GRANT ALL PRIVILEGES ON DATABASE coredb TO core;
        GRANT

        5. Make sure this user can create a database

        postgres=#  ALTER USER core CREATEDB;
        ALTER ROLE
        postgres=#

        modified:   README.md
        modified:   requirements.txt

        NEXT:

        Connecting the database


#### 1.5 Connecting the database - Part 1: Configure connection 

        Activitas:

        1. Configuring db connection in settings.py

        modified:   CoreRoot/settings.py
        modified:   README.md

        2. Run migration

        NEXT: 

        Create environment variable


#### 1.5 Connecting the database - Part 2: Create environment variable

        Activitas:

        1. Install django-environ

        (venv3940) λ pip install django-decouple
        ...
        Successfully installed django-decouple-2.1

        2. Create .env and .env-example files

        (venv3940) λ touch .env .env-example

        3. Configure the .env file

        4. Setup environ on settings.py

        5. Configure TIME_ZONE = 'Asia/Jakarta'

        Testing: :)

        new file:   .env-example
        modified:   .gitignore
        modified:   CoreRoot/settings.py
        modified:   README.md

        NEXT:

        2: Authentication and  Authorization using JWTs


#### 2. Authentication and Authorization Using JWTs

        Activitas:

        1. modified:   README.md

        NEXT:

        2.1 Organizing a project by creating 'core' app


#### 2.1 Organizing a project - Part 1: creating 'core' app

        Activitas:

        1. Creating a new app 'core'

        (venv3940) λ django-admin startapp core

        modified:   README.md
        new file:   core/__init__.py
        new file:   core/admin.py
        new file:   core/apps.py
        new file:   core/migrations/__init__.py
        new file:   core/models.py
        new file:   core/tests.py
        new file:   core/views.py

        NEXT:

        2.1 Organizing a project - Part 2: register the core app to the project


#### 2.1 Organizing a project - Part 2: register the core app to the project

        Activitas:

        1. Register core app

        INSTALLED_APPS = [
	        ..

	        # new locals
	        'core.apps.CoreConfig',
        ]

        2. Run server

        Testing: :)

        NEXT:

        2.1 Organizing a project - Part 3: remove most files from the core app