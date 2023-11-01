from shortzy import Shortzy
from info import *

API = "ca40e845c03e9ecc973b777166e7b26aba198bc5"
WEB = "onepagelink.in"

API2 = "810c244584d751ac6c0a7c3c0c6293d06f9b035c"
WEB2 = "moneykamalo.com"

async def get_shortlink(link):
    shortzy = Shortzy(URL_SHORTNER_WEBSITE_API, URL_SHORTENR_WEBSITE)
    return await shortzy.convert(link)

async def get_shortlink2(link):
    shortzy = Shortzy(API, WEB)
    return await shortzy.convert(link)

async def get_shortlink3(link):
    shortzy = Shortzy(API2, WEB2)
    return await shortzy.convert(link)
