#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22308775
API_HASH = "6080010c1b489fc613ffb1c5b19e7b3e"
BOT_TOKEN = "6072153523:AAGT4ndgwNM4KdOVSvCWVzQ-cNoKA0MYjko"
SESSION = "BQC0sAeRiPZmoE6vqCAJ1YuWeU593lCBUcZDM3d5mGiXS2OgY3vhlj4jK1NuroIklwCSsXI38NdBS9Omn-xKH4iZ2lWLOVGPDWtYrqYEf60G2xtlFSZuwVTJ8yjiojlg3Ocu8D1UVcXHng-KGao0odUloQ3B5JhzyvOmfny6aMYd241V5WDTu48ujGQLcox7xnJcYaQHHcUJviWFhKdQaD-zCUT4GHbgTnNSqIkbQ5bfL90Lk0MAkUZC9jTCABUBDMCQehLdKXa2fbUIE1GEWejzWUNrr2ANP6xR-m5h-OpyL1CDTBuz_p_kmqalClaFMSHCwq5GZUFLPWAWyHE1nH1WAAAAATNxElIA"
FORCESUB = "hiiiiiiiiiiiiiiiiiip"
AUTH = 5158015570

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
