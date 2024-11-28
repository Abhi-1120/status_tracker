import pika
import json
import pymongo
from fastapi import FastAPI
from datetime import datetime

client = pymongo.MongoClient('localhost', 27017)
db = client['upswingDB']
collection = db['status']

QUEUE_NAME = "status_queue"
EXCHANGE = "status_exchange"
ROUTING_KEY = "status_key"

app = FastAPI()

def initialize_rabbitmq():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel_connection = connection.channel()

    channel_connection.exchange_declare(exchange=EXCHANGE, exchange_type='direct', durable=True)
    channel_connection.queue_declare(queue=QUEUE_NAME, durable=True)
    channel_connection.queue_bind(exchange=EXCHANGE, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

    return channel_connection

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(message)
    status = message['status']
    timestamp = datetime.strptime(message["timestamp"], "%Y-%m-%d %H:%M:%S.%f")
    collection.insert_one({"status": status, "timestamp": timestamp})
    print(f"Received and stored message: {message}")


def start_message_listener():
    channel = initialize_rabbitmq()
    channel.basic_consume(queue='status_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()


if __name__ == "__main__":
    start_message_listener()
