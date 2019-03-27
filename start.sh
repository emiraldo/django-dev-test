!#/bin/bash
cd usr/src/app
./manage.py makemigrations
./manage.py migrate
gunicorn -w 4 vehiculos_app.wsgi:application -b :8000 -t 3600 --reload