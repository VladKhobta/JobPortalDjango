# JobPortalDjango


## How to use this project?

1. Fork/Clone

1. Run terminal commands in project`s repo:
```
python -m venv venv
.\venv\Scripts\activate
pip install django-cors-headers  
pip install djangorestframework 
pip install django-extensions 
pip install django-ckeditor 
pip install psycopg2-binary 
pip install python-dotenv
```

3. Open SQL Shell(psql) and after authentication run this code:
```
create database your_db_name
```

4. Add .env file in JobPortalDjango\ with this code:
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

5. After all in project`s repo again:
```
.\venv\Scripts\activate
python manage.py makemigrations
python manage.py migrate
python maange.py runserver
```
