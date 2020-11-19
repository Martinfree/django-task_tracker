#!/bin/bash

EXCLUDE='*/migrations/*.py,*/__init__.py,*/adapter.py,*/apps.py,*/cron.py,*/permissions.py,*/validators.py,*/tests/*.py,*/admin.py,*/parsing.py,wsgi.py,manage.py,*/utils/*.py,*/settings/*.py'

rm -rf htmlcov/
docker exec -it django-task_tracker coverage run --omit=$EXCLUDE --source='.' manage.py test "" --nocapture

docker exec -it django-task_tracker coverage html
docker cp django-task_tracker:/opt/proj/htmlcov ./htmlcov
docker exec -it django-task_tracker coverage erase
