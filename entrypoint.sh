#!/bin/bash

if [[ "$DJANGO_SKIP_MIGRATIONS" == "false" ]]; then
  python manage.py migrate
fi

if [[ "$DJANGO_DEBUG" == "true" ]]; then
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn DRFTestTask.wsgi:application -b 0.0.0.0:8000
fi