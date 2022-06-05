from time import sleep
from pyrogram import Client
import logging


# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)





# Hesap
API_ID = "13201687"
API_HASH = "25db8958ff8c53f4313e21c6a70469ad"
TOKEN = "Here is the token for bot GÖNÜL KELİME BOTU @Gonul_kelimebulmaca_bot:

5533333884:AAFU_TAkAJOyaRfsYJZN-5MbOxe9QR0KSIM" 
USERNAME = "5195937727"




# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


# Oyun Verileri
oyun = {}


# rating
rating = {}





# !!!!!!!!!!!!!! DEĞİŞTİR KESİNLİKLE !!!!!!!!!!!!!!!!
#      SAHİBİN USER ID'Sİ
OWNER_ID = 5195937727

