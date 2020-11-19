#!/bin/bash

EXCLUDE='*/migrations/*.py,*/__init__.py,manage.py,*/settings/*.py'

rm -rf htmlcov/
docker exec -it django-task_tracker coverage run --omit=$EXCLUDE --source='.' manage.py test board.tests

docker exec -it django-task_tracker coverage html
docker cp django-task_tracker:/opt/proj/htmlcov ./htmlcov
docker exec -it django-task_tracker coverage erase
