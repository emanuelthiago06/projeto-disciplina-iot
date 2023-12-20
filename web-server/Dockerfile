FROM python:3.11-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . . 
EXPOSE 8000
EXPOSE 80
RUN mkdir ./static/
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:$WEB_PORT 

