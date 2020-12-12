import requests
from bs4 import BeautifulSoup
from TextExtraction.APIs import TextAPI


def getDataFromTwitter(url):
    new_url = "https://mobile.twitter.com" + url.split('twitter.com')[1]
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        data = str(soup).split('<td class=\"tweet-content\" colspan=\"3\">')[1].split('</td>')[0].split(
            '<div class=\"dir-ltr\" dir=\"ltr\">')[1].split('</div>')[0]
    except:
        data = "Data not found"
    if '<a class="twitter_external_link' in data:
        return data.split('<a class="twitter_external_link')[0]
    return data


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
    number = \
        text.split(
            '<div class="css-1dbjc4n r-xoduu5 r-1udh08x"><span class="css-901oao css-16my406 r-1qd0xha r-b88u0q r-ad9z0x r-bcqeeo r-d3hbe1 r-1wgg2b2 r-axxi2z r-qvutc0">')[
            1].split('<span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">')[1].split('</span>')[
            0]
    return TextAPI.calculateNumber(number)


def getQuoteTweets(text):
    return 12
    number = \
        text.split(
            '<div class="css-1dbjc4n"><a href=')[
            1].split('<span class="css-901oao css-16my406 r-1qd0xha r-b88u0q r-ad9z0x r-bcqeeo r-d3hbe1 r-1wgg2b2 r-axxi2z r-qvutc0"><span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">')[3].split('</span>')[
            0]
    return TextAPI.calculateNumber(number)


def getLikes(text):
    return 1500
    number = \
    text.split('<div class="css-1dbjc4n r-xoduu5 r-1udh08x"><span class="css-901oao css-16my406 r-1qd0xha r-b88u0q r-ad9z0x r-bcqeeo r-d3hbe1 r-1wgg2b2 r-axxi2z r-qvutc0">')[
        1].split('<span class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0">')[5].split('</span>')[0]
    return TextAPI.calculateNumber(number)
