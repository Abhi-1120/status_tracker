import pika
import json
import time
import random
from datetime import datetime

QUEUE_NAME = "status_queue"
EXCHANGE = "status_exchange"
ROUTING_KEY = "status_key"

def initialize_rabbitmq():

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel_connection = connection.channel()

    channel_connection.exchange_declare(exchange=EXCHANGE, exchange_type='direct', durable=True)
    channel_connection.queue_declare(queue=QUEUE_NAME, durable=True)
    channel_connection.queue_bind(exchange=EXCHANGE, queue=QUEUE_NAME, routing_key=ROUTING_KEY)

    return channel_connection


def emit_message():

    channel = initialize_rabbitmq()

    while True:
        message = {
            "status": random.randint(0, 6),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        }
        print(message)
        channel.basic_publish(exchange=EXCHANGE, routing_key=ROUTING_KEY, body=json.dumps(message))
        print(f"Sent message successfully: {message}")
        time.sleep(1)


if __name__ == "__main__":
    emit_message()
