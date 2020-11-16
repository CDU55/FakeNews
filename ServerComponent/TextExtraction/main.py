import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

from twitter_scraper import Profile

url = 'http://web.mta.info/developers/turnstile.html'
protv = 'https://incont.stirileprotv.ro/joburi-romania/cum-se-va-desfasura-telemunca-si-munca-la-domiciliu-si-cum-se-schimba-programul-de-lucru-noi-reglementari.html?_ga=2.18512444.441552134.1604862638-837112706.1604862638'
fblink = 'https://www.facebook.com/PresedinteleTraianBasescu/posts/3918068968206625'
twitter = "https://mobile.twitter.com/pinkfloyd/status/1325772237341945858"
badea = "https://mobile.twitter.com/lupulalbastru1/status/1284161708194504705"


# FOR NORMAL WEBSITE
def getTitleForWebsite(url):
    response = requests.get(url)
    found = False
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.findAll('title')
        try:
            found = True
            title = re.search("<title>(.*?)</title>", str(data[0])).group(1)
        except:
            return found, "HTML Tag for title not found"
        return found, title
    else:
        return found, "Failed to receive the text"

# TESTING FOR NORMAL WEBSITE
# answer, text = getTitleForWebsite(url2)
# print(answer, text)

# FOR TWITTER
def getDataFromTwitter(url):
    new_url = "https://mobile.twitter.com" + url.split('twitter.com')[1]
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        data = str(soup).split('<td class=\"tweet-content\" colspan=\"3\">')[1].split('</td>')[0].split('<div class=\"dir-ltr\" dir=\"ltr\">')[1].split('</div>')[0]
    except:
        data = "Data not found"
    return data

# TESTING FOR TWITTER GetData
# print(getDataFromTwitter(badea))

def getTwitterProfile():
    pass
    #work in progress


