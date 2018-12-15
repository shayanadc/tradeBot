from binance.client import Client

import setting
api_key = setting.BNCAPIK
api_secret = setting.BNCSECK

client = Client(api_key, api_secret)

import rabbitMQ
producer = rabbitMQ.RabbitMQ('topic_logs','topic')


def process_message(msg):

    for item in msg:
        producer.produce(str(item['s'] + '.info'), str(item))


from binance.websockets import BinanceSocketManager

bm = BinanceSocketManager(client)

conn_key = bm.start_ticker_socket(process_message)

bm.start()