FROM python:3.11-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt
COPY . . 
EXPOSE 8000
RUN mkdir ./static/
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 

