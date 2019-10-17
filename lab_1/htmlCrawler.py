# Задача №1. HTML Crawler
import requests
import datetime
from bs4 import BeautifulSoup
import json


def get_request(url):
    url_request = requests.get(url)
    if url_request==200:
     return url_request
    else:
        return null


def get_html_page(url):
    url_request = requests.get(url)
    html_page = url_request.text
    return html_page


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, "html.parser")
    raw_articles = parsed_page.find_all("h3", {"class": "ipQwMb ekueJc RD0gLb"})

    articles = []
    for i in range(len(raw_articles)):
        articles.append({"title": raw_articles[i].text, "url": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru"})
    return articles


def publish_report(url):
    creation_date = datetime.datetime.today().strftime("%Y-%m-%d")
    articles = find_articles(get_html_page(url))
    raw_json_dict = {"url": url, "creationDate": creation_date, "articles": articles}
    formed_json_doc = json.dumps(raw_json_dict, indent=4, ensure_ascii=False)

    with open("C:/Users/Катя/PycharmProjects/2019-3-level-labs/articles.json", "w", encoding="utf-8") as file:
        file.write(formed_json_doc)
