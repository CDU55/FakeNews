import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

facebook = "https://mobile.facebook.com/361235817223309/posts/3925919104088278/"

def getDataFromFacebook(url):
    new = "https://mobile.facebook.com/361235817223309/posts/3925919104088278/"+url.split("facebook.com")[1]
    response = requests.get(new)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        data = str(soup).split("<span class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55"
                               " a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em "
                               "fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh "
                               "oo9gr5id hzawbc8m' dir='auto' >").split("</span>")
        #data = str(soup)
    except:
        data = "Data not found"
    return data

#print(getDataFromFacebook())

def getTitleFromFB(url):
    new = "https://mobile.facebook.com/361235817223309/posts/3925919104088278/" \
          + url.split("facebook.com")[1]
    response = requests.get(new)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        data = soup.find("title")
        # data = str(soup)
    except:
        data = "Data not found"
    return data

def getProfile(url):
    pass
    #va urma