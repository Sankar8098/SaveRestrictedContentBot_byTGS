#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29409646
API_HASH = "a69d0340a520cg1913c517bea1h3a3de7"
BOT_TOKEN = "5682083705:AAHgHEc78t-XJUKPMba4Rc4C1by-GH9lxE"
SESSION = "-Q859e1-YfDzmc5VGGbEk9RqSqEV143wP4NsnsXe3bsVxupot5AXH050oxpH76R3b2Y6-D-RcLZaDMwpiDM6htEHAlI1xDit9ew3nnsFbGdeKwwTnYVA1P_GdIP3yEvvlR1hkEvFkvKyVSAoUkoElBHHLyw_vHA4dtGgCAt9IZbdWdG5qUQ2PHWttBcs3otU5DTw6Pk_tuE80oDjxAj8yOaBYPETX0Ts6nTJSmLV2szo7uNVK-g5a0Rhvuez_hGxQdQ1MSpZQ_JRKT722Qw7WIojAAAAAFerw5dAA"
FORCESUB = "SK_MoviesOffl"
AUTH = 5883498077

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
