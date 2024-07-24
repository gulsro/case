#!/bin/bash

python manage.py makemigrations
python manage.py migrate

# Import data through HTTP
python manage.py import_data


# Start the Django server
python manage.py runserver 0.0.0.0:8000
