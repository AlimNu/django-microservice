import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorialdjango.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://xywqkakv:n09rwGm9XBtXaBYNjYmFQwGIqGt_H_MV@snake.rmq2.cloudamqp.com/xywqkakv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('recieve in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id)
    product.like = product.like + 1
    product.save()
    print('product likes update')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Start Consuming')

channel.start_consuming()

channel.close()
