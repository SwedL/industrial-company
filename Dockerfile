# pull the official base image
FROM python:3.11.4-alpine

# set work directory
WORKDIR /usr/src/industrial-company

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/industrial-company
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/industrial-company

#CMD python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')"

#CMD python manage.py migrate \
#    && python manage.py runserver 0.0.0.0:8000
#    && python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')"
#    && python manage.py loaddata structure/fixtures/positions.json \
#    && python manage.py init_employees
