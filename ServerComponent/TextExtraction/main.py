import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from TextExtraction.APIs import WebAPI, TwitterAPI

protv = 'https://incont.stirileprotv.ro/joburi-romania/cum-se-va-desfasura-telemunca-si-munca-la-domiciliu-si-cum-se-schimba-programul-de-lucru-noi-reglementari.html?_ga=2.18512444.441552134.1604862638-837112706.1604862638'
fblink = 'https://www.facebook.com/PresedinteleTraianBasescu/posts/3918068968206625'
twitter = "https://mobile.twitter.com/pinkfloyd/status/1325772237341945858"
badea = "https://mobile.twitter.com/lupulalbastru1/status/1284161708194504705"
test = "https://mobile.twitter.com/RockstarGames/status/1327306496217128967"


### FOR NORMAL WEBSITE
# GET TITLE
#answer, text = WebAPI.getTitle(protv)
#print(answer, text)

# GET TEXT
#print(WebAPI.getText(protv))

# MessageTwitter


# TESTING FOR TWITTER GetData
#print(TwitterAPI.getDataFromTwitter(test))
#print(TwitterAPI.getProfileName(test))
print(TwitterAPI.checkVerifiedAccount(TwitterAPI.getProfileName(test)))

#TwitterAPI.checkVerifiedAccount(TwitterAPI.getProfileName(test))
