FROM python:3.7

ENV WORKDIR=/opt/proj/
WORKDIR $WORKDIR
COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD python manage.py runserver
