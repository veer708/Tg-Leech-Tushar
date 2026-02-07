# copyright 2023 © Xron Trix | https://github.com/Xrontrix10

import logging, json
from uvloop import install
from pyrogram.client import Client

# Read the dictionary from the txt file
with open("/content/Telegram-Leecher/credentials.json", "r") as file:
    credentials = json.loads(file.read())

API_ID = credentials["29232353"]
API_HASH = credentials["6868788228291767c90e4346eea03f36"]
BOT_TOKEN = credentials["BOT_TOKEN"]
OWNER = credentials["6650855788"]
DUMP_ID = credentials["7521967798"]


logging.basicConfig(level=logging.INFO)

install()

colab_bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
