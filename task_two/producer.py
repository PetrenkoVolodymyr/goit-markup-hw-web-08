import pika
import random

from models import Task
from faker import Faker

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='My exchange', exchange_type='direct')
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_declare(queue='sms_queue', durable=True)
channel.queue_bind(exchange='My exchange', queue='email_queue')
channel.queue_bind(exchange='My exchange', queue='sms_queue')


def create_tasks(nums: int):
    for i in range(nums):
        task = Task(message=fake.sentence(nb_words=10, variable_nb_words=False),
                    name = fake.name(),
                    email=fake.email(),
                    phone=fake.phone_number(),
                    comm_chan=random.choice(["sms", "email"]))
        task.save()

        if task.comm_chan == "email":
            channel.basic_publish(exchange='My exchange', routing_key='email_queue', body=str(task.id).encode())
        else:
            channel.basic_publish(exchange='My exchange', routing_key='sms_queue', body=str(task.id).encode())

    connection.close()


if __name__ == '__main__':
    create_tasks(20)