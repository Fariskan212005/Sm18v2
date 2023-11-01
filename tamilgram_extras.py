## ©® tamilgram ##
import re
from os import environ
from dotenv import load_dotenv
load_dotenv()

## For /start cmd ##

SB_TEXT1 = " 📫 MAIN CHANNEL 📫"
SB_URL1 = "https://telegram.me/Srilinks4k_in"

SB_TEXT2 = "🪩 MOVIES CHANNEL 🪩"
SB_URL2 = "https://telegram.me/+mlWXQ79MwOYzNDVl"


## Auto Delete For Auto Filters ##

AF_DELETE_TIME = int(environ.get('AF_DELETE_TIME', 300))
AF_DELETE = environ.get('AF_DELETE', True)
if AF_DELETE == "True":
    AF_DELETE = True

## Auto Delete For Spell Check ##

SC_DELETE = environ.get('SC_DELETE', True)
if SC_DELETE == "True":
    SC_DELETE = True
SC_DELETE_TIME = int(environ.get('SC_DELETE_TIME', 5))


## How To Download Button In Auto Filter Button ##

DOWNLOAD_VIDEO_LINK = environ.get('DOWNLOAD_VIDEO_LINK', "https://telegram.me/howtodownload4k/3")
DOWNLOAD_BUTTON_TEXT = environ.get('DOWNLOAD_BUTTON_TEXT', "📩 𝗛𝗢𝗪 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 📩")

