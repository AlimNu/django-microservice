import pika, json

params = pika.URLParameters('amqps://xywqkakv:n09rwGm9XBtXaBYNjYmFQwGIqGt_H_MV@snake.rmq2.cloudamqp.com/xywqkakv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)