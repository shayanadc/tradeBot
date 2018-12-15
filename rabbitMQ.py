import pika
import sys


class RabbitMQ:
    def __init__(self, exc_name, exc_type):
        self.exc_name = exc_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exc_name, exchange_type=exc_type)

    def close(self):
        self.connection.close()


    def produce(self, routing_key, message):
        self.channel.basic_publish(exchange=self.exc_name, routing_key=routing_key, body=message)


    def consume(self, routing_key):

        result = self.channel.queue_declare(exclusive=True)
        self.queue_name = result.method.queue

        self.channel.queue_bind(exchange=self.exc_name,
                                queue=self.queue_name,
                                routing_key=routing_key)

        self.channel.basic_consume(self.callback,
                                   queue=self.queue_name,
                                   no_ack=True)
        self.channel.start_consuming()

    def callback(self,ch, method, properties, body):

        symbol = method.routing_key.split('.')
        symbol = symbol[0]
        body = body.decode('utf8').replace("'", '"')
        import json
        body = json.loads(body)
        import userCriteria
        for user in userCriteria.getAll(symbol):
            if float(body['c']) > user['high'] or float(body['c']) < user['low']:
                import datetime
                now = datetime.datetime.now()
                message = 'Hii  Friend ' + '\n\b' + str(body['s']) + ' price is '+ body['c'] + ' at : ' + str(now)
                import telepot
                TOKEN = '639857757:AAGvOiTLkizq8mxYVI92wGMgeR_T79kF5dM'
                bot = telepot.Bot(TOKEN)
                bot.sendMessage(user['name'], message)
                userCriteria.deleteKey(symbol,user['name'])

