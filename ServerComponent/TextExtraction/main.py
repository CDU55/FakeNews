import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from APIs import WebAPI, TwitterAPI

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

entry = twitter

print("Data about user profile")
print()

user = TwitterAPI.getProfileName(entry)
print("Username:", user)
print("Verified:", TwitterAPI.checkVerifiedAccount(user))
print("Number of followers:", TwitterAPI.getFollowers(user))
print("Number of tweets:", TwitterAPI.getTweets(user))

print()
print("Data about post")
print()

# DELETE THIS // ONLY FOR TEST
text = '''
PLEASE COPY PASTE FROM EXAMPLE.TXT
'''

print("Likes:", TwitterAPI.getLikes(text))
print("Retweets:", TwitterAPI.getRetweets(text))
print("Quote Tweets", TwitterAPI.getQuoteTweets(text))

print("Text:", TwitterAPI.getDataFromTwitter(entry))