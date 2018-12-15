from dotenv import load_dotenv
load_dotenv()
import os
BNCAPIK = os.getenv("BINANCE_API")
BNCSECK = os.getenv("BINANCE_SEC")
BOTTOKEN =os.getenv('BOT_TOKEN')
MONGOPORT = os.getenv('MONGO_PORT')