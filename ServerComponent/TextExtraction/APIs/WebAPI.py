import requests
from bs4 import BeautifulSoup
import html2text
import re

def getTitle(url):
    response = requests.get(url)
    found = False
    if response.status_code == 200:
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

def getText(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.findAll('body')
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.ignore_tables = True
        return h.handle(str(data))