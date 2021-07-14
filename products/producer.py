## amqps://xywqkakv:n09rwGm9XBtXaBYNjYmFQwGIqGt_H_MV@snake.rmq2.cloudamqp.com/xywqkakv

import pika


params = pika.URLParameters('amqps://xywqkakv:n09rwGm9XBtXaBYNjYmFQwGIqGt_H_MV@snake.rmq2.cloudamqp.com/xywqkakv')


connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='',routing_key='admin', body='hello')