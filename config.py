# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "21257327"))
API_HASH = getenv("API_HASH", "1235c1fe45ebc4968d9e23bc93440549")
BOT_TOKEN = getenv("BOT_TOKEN", "7351104744:AAGLI3uyB9JNRb9L-8DvlbG3SYosb7O6RbI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6318243977").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mahakalgaming391:Cluster0@cluster0.j2l3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002267025113")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002650577614"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "1000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
