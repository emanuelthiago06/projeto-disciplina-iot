FROM python:3.11-slim
WORKDIR /usr/src/app
RUN pip install --no-cache-dir pika requests
COPY . .
EXPOSE 8000
EXPOSE 80 
EXPOSE 5672
EXPOSE 5671
CMD python main.py $WEB_HOST $WEB_PORT $RMQ_HOST
