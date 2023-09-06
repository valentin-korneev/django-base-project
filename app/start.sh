#!/bin/sh

python manage.py db_health_check
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
python manage.py create_superuser --no-input

if [ ${DEBUG} = 1 ]
then
  python manage.py runserver 0.0.0.0:${PROJECT_PORT}
else
  gunicorn project.wsgi:application --bind 0.0.0.0:${PROJECT_PORT}
fi