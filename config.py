from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/c2677756d1cfc2408da84.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://GIRLSSAFEZONE ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tamil_yelrasaniyan  ")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5065752827").split()))
