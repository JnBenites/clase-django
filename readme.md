pip install django 
python -m django startproject clase
python manage.py runserver
python manage.py runserver 0.0.0.0:8000
python manage.py startapp libros
python manage.py migrate
python manage.py createsuperuser
user: admin
password: admin

python manage.py makemigrations libros
python manage.py migrate