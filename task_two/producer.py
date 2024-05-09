import json
from datetime import datetime
from faker import Faker
fake = Faker()
import pika

from models import Task

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='My exchange', exchange_type='direct')
channel.queue_declare(queue='my_queue', durable=True)
channel.queue_bind(exchange='My exchange', queue='my_queue')


def create_tasks(nums: int):
    for i in range(nums):
        message = {
            'id': i,
            'payload': f"Date: {datetime.now().isoformat()}"
        }

        task = Task(message=fake.sentence(nb_words=10, variable_nb_words=False))
        task.save()


        channel.basic_publish(exchange='My exchange', routing_key='my_queue', body=str(task.id).encode())

    connection.close()


if __name__ == '__main__':
    create_tasks(10)