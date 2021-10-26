import requests
from bs4 import BeautifulSoup
import json

def headlineScrapper(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    ReqJson = []
    for title in soup.find_all('title'):
        if len(title.get_text()):
            ReqJson.append(title.get_text())

    ReqJson = {i+1:ReqJson[i] for i in range(len(ReqJson))}
    ReqJson = json.dumps(ReqJson)
    return ReqJson