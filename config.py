# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20071888"))
API_HASH = getenv("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")
BOT_TOKEN = getenv("BOT_TOKEN", "7716433955:AAFhH0_Y8ltddApzJGLSYbxvNqttwvz-6-8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1c4cb9d94b23282abd9ae2a87a521b53").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Dam:aloksingh@cluster0.6z0hq.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002267894978")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002381050327"))
