import requests
from bs4 import BeautifulSoup


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