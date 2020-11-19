#!/bin/bash

docker-compose up -d
docker exec django-task_tracker python manage.py board
docker exec django-task_tracker python manage.py migrate --noinput
docker-compose stop
