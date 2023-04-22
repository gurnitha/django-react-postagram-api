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


#### 2.1 Organizing a project - Part 3: remove most files from the core app

        Activitas:

        1. Keep apps.py file and remove the rest
        2. Modified the apps.py file

        modified:   README.md
        deleted:    core/admin.py
        modified:   core/apps.py
        deleted:    core/migrations/__init__.py
        deleted:    core/models.py
        deleted:    core/tests.py
        deleted:    core/views.py

        NEXT:

        2.2 Creating Creating a user model


#### 2.2 Creating a user model - Part 1: create 'user' app

        Activitas:

        1. Creating 'user' app

        (venv3940) λ django-admin startapp user 

        new file:   user/__init__.py
        new file:   user/admin.py
        new file:   user/apps.py
        new file:   user/migrations/__init__.py
        new file:   user/models.py
        new file:   user/tests.py
        new file:   user/views.py

        NEXT:

        2.2 Creating a user model - Part 2: register 'user' app to the project


#### 2.2 Creating a user model - Part 2: register 'user' app to the project

        Activitas:

        1. Register user app to the project

        INSTALLED_APPS = [
	        ..

	        # new locals
	        'core.apps.CoreConfig',
	        'user.apps.UserConfig',
        ]

        NEXT:

        2.2 Creating a user model - Part 3: move the user app to inside the core app


#### 2.2 Creating a user model - Part 3: move the user app to inside the core app

        Activitas:

        1. Moving the user app to the inside of the core app
        2. Modified INSTALLED_APPS in setting.py file

        INSTALLED_APPS = [
                ..

                # new locals
                'core.apps.CoreConfig',
                'core.user.apps.UserConfig',
        ]

        3. Modified apps.py file

        # name = 'user'
        name = "core.user"
        label = "core_user"

        4. Run server for testing :)

        modified:   CoreRoot/settings.py
        renamed:    user/__init__.py -> core/user/__init__.py
        renamed:    user/admin.py -> core/user/admin.py
        renamed:    user/apps.py -> core/user/apps.py
        renamed:    user/migrations/__init__.py -> core/user/migrations/__init__.py
        renamed:    user/models.py -> core/user/models.py
        renamed:    user/tests.py -> core/user/tests.py
        renamed:    user/views.py -> core/user/views.py

        NEXT:

        2.2 Creating a user model - Part 4: create User model


#### 2.2 Creating a user model - Part 4: create User model 

        Activitas:

        1. Create UserManager and User models
        modified:   core/user/models.py

        2. Tell Django to use this User model for the authentication user model. 
        In the  settings.py file, add the following line:

        AUTH_USER_MODEL = 'core_user.User'

        3. Due to issues made by the previous migrations, delete the db and re-create the same db

        4. Testing:

        (venv3940) λ python manage.py makemigrations
        No changes detected

        (venv3940) λ python manage.py migrate

        new file:   core/user/migrations/0001_initial.py

        5. Run server

        (venv3940) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        April 22, 2023 - 11:05:03
        Django version 4.0, using settings 'CoreRoot.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        NEXT:

        2.2 Creating a user model - Part 5: use python shell to create user 


#### 2.2 Creating a user model - Part 5: use python shell to create user 

        Activitas:

        1. (venv3940) λ :: Use python shell to create user

        (venv3940) λ python manage.py shell
        Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        (InteractiveConsole)
        >>>

        >>> from core.user.models import User
        >>> data_user = {
        ... "email":"testuser@yopmail.com",
        ... "username":"john-doe",
        ... "password":"12345",
        ... "first_name":"John",
        ... "last_name":"Doe"
        ... }
        >>>

        2. The user is created in the database. Let's access some 
        properties of the user object.

        >>> user = User.objects.create_user(**data_user)
        >>>
        >>> user.name
        'John Doe'
        >>> user.email
        'testuser@yopmail.com'
        >>> user.password
        'pbkdf2_sha256$320000$CB3AJtPo7izKHcFf0DEQUV$rI1hNIgYKhCKEPVECQW7VhtbqmptERuj4fRLIpgLejY='
        >>>

        3. Select user from terminal

        postgres=# \c django_react_postagram_api

        django_react_postagram_api=# select first_name, username, email from core_user_user;  
        first_name | username |        email
        ------------+----------+----------------------
        John       | john-doe | testuser@yopmail.com
        (1 row)

        modified:   README.md

        NEXT:

        3. Writing UserSerializer


#### 3. Serializer - Install djangorestframework and django-filter

        Activitas:

        1. About serializer

        A serializer allows us to convert complex Django complex data structures such as QuerySet or model instances into Python native objects that can be easily converted to JSON or XML format. However, a  serializer also serializes JSON or XML to native Python. 

        Django Rest Framework (DRF) provides a serializers package you can use to write serializers and also validations when API calls are made to an endpoint using this serializer. 

        Let’s install the DRF package and make some configurations first:

        2. Install djangorestframework django-filter
        (venv3940) λ pip install djangorestframework django-filter

        3. Register rest_framework to the project

        INSTALLED_APPS = [
                ..

                # third party
                'rest_framework',

                # new locals
                'core.apps.CoreConfig',
                'core.user.apps.UserConfig',
        ]

        4. Testing: run rever :)

        5. Modified requirements.txt file

        modified:   CoreRoot/settings.py
        modified:   README.md
        modified:   requirements.txt

        NEXT:

        4. Create UserSerializer


#### 4. Serializer - Create UserSerializer

        Activitas:

        1. Create serializers.py in core/user
        2. Create UserSerializer class or model
        3. Testing: run server :)

        new file:   core/user/serializers.py
        
        NEXT:

        5. Writing UserViewset
