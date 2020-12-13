import requests
from bs4 import BeautifulSoup
from APIs import TextAPI


def getDataFromTwitter(text):
    if '" property="og:description" data-rh="true">' in text:
        data = text.split('" property="og:description" data-rh="true">')[0].split('<meta content="')
        result = data[len(data) - 1]
        if '&#39;' in result:
            return result.replace('&#39;', "'")
        return result
    return "ERROR404:Data not found"


def getProfileName(url):
    return url.split("twitter.com/")[1].split("/")[0]


def checkVerifiedAccount(user):
    url = "https://mobile.twitter.com/" + user
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.find("img alt=\"Verified Account\"") != -1:
            return True
    return False


def getFollowers(user):
    url = "https://mobile.twitter.com/" + user
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    separator = '<a href="/' + user + '/followers">'
    return str(soup).split(separator)[1].split('</a>')[0].split('<div class="statnum">')[1].split('</div>')[0]


def getTweets(user):
    url = "https://mobile.twitter.com/" + user
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    separator = '<td class="stat">'
    return str(soup).split(separator)[1].split('</td>')[0].split('<div class="statnum">')[1].split('</div>')[0]


def getRetweets(text):
    if '</span></span></div> <span class="css-901oao css-16my406 r-111h2gw r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Retweets</span>' in text:
        number = \
            text.split(
                '</span></span></div> <span class="css-901oao css-16my406 r-111h2gw r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Retweets</span>')[
                0].split('">')
        return TextAPI.calculateNumber(number[len(number) - 1])
    return 0


def getQuoteTweets(text):
    if '</span></span></div> <span class="css-901oao css-16my406 r-111h2gw r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Quote Tweets</span>' in text:
        number = \
            text.split(
                '</span></span></div> <span class="css-901oao css-16my406 r-111h2gw r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Quote Tweets</span>')[
                0].split('">')
        return TextAPI.calculateNumber(number[len(number) - 1])
    return 0


def getLikes(text):
    if '</span></span></div> <span class="css-901oao css-16my406 r-111h2gw r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Likes</span>' in text:
        number = \
            text.split(
                '</span></span></div> <span class="css-901oao css-16my406 r-111h2gw r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">Likes</span>')[
                0].split('">')
        return TextAPI.calculateNumber(number[len(number) - 1])
    return 0
