import time
import telepot
from telepot.loop import MessageLoop
import setting
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        try:
            if msg['text'] == '/start' : raise Exception('Hi ' + msg['chat']['first_name'])
            message = msg['text'].split()
            if len(message) != 4: raise Exception('more or less parameters')
            if message[0] != '/notif': raise Exception('follow command. you start your condition with /notif')
            if not str(message[1]).isalpha(): raise Exception('incorrect symbol')
            if str(message[2]).isalpha(): raise Exception('your low value must be float number')
            if str(message[3]).isalpha(): raise Exception('your high value must be float number')
            low = float(message[2])
            high = float(message[3])

            from binance.client import Client
            api_key = setting.BNCAPIK
            api_secret = setting.BNCSECK
            client = Client(api_key, api_secret)
            info = client.get_symbol_info(str(message[1]).upper())

            if not info: raise Exception('your symbol pair is not exist on binance market unfortunately')
            import userCriteria
            userCriteria.storeUser(chat_id,str(message[1]),low,high)
            bot.sendMessage(chat_id, 'we will notify you in future. wait please. bye bye now')
        except Exception as e:
            bot.sendMessage(chat_id, str(e))
            bot.sendMessage(chat_id, 'follow command please /notif \n\b for example if you want get warning when BTCUSDT lower than 3253.51 or higher than 3255.15 you should send : /notif BTCUSDT 3253.51 3255.15')
    if content_type != 'text':
        bot.sendMessage(chat_id, 'follow command please /notif')

TOKEN = setting.BOTTOKEN

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)