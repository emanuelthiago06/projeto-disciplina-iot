#!/usr/bin/python3
import pika
import json
from datetime import datetime
import requests

RMQ_HOST = "195.35.17.231"
POST_URL = "http://192.168.0.23:8000/api/add-point/"


# container:  rmq 
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue='iot')

    def callback(ch, method, properties, body):
        data = json.loads(body.decode())
        response = requests.post(url=POST_URL, data=data)
        print(f"{response}")

    channel.basic_consume(queue='iot', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages')
    channel.start_consuming()

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('Quiting!')
            break
        except Exception as err:
            print(err)
            continue
