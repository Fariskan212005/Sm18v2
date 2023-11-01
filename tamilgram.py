## ©® srilinks4k ##
from shortzy import Shortzy
from os import environ

URL_SHORTNER = environ.get("URL_SHORTNER", "paisakamalo.in")
URL_SHORTNER_API = environ.get("URL_SHORTNER_API", "7d3a376d6c3da787bf1c717b8937352d3b4210ed")



## All Adlinkfly & Shareus Shortner Working ##

async def tamilgramshort(link):
   shortzy = Shortzy(URL_SHORTNER_API, URL_SHORTNER)
   return await shortzy.convert(link)
