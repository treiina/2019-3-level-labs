# Задача №1. HTML Crawler

import requests
import datetime
from bs4 import BeautifulSoup
import json


def get_html_page(url):
    url_request = requests.get(url)
    html_page = url_request.text

    if url_request.status_code == 200:
        print("Yay! We performed a successful request!")
        return html_page
    else:
        print("Oops.. Something went wrong")
        return []


def find_articles(html_page):
    parsed_page = BeautifulSoup(html_page, "html.parser")
    raw_articles = parsed_page.find_all("h3", {"class": "ipQwMb ekueJc RD0gLb"})

    articles = []
    for i in range(len(raw_articles)):
        articles.append({"title": raw_articles[i].text})
    return articles


def publish_report(path, url, day, articles):
    raw_json_dict = {"url:": url, "creationDate:": day, "articles": articles}
    formed_json_doc = json.dumps(raw_json_dict, indent=4, ensure_ascii=False)

    with open(path, "w", encoding="utf-8") as file:
        file.write(formed_json_doc)


'''''''-------------------------------------------------------------------------'''

# Google Новости - Бизнес - Последние
page_url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru"
today = datetime.datetime.today().strftime("%Y-%m-%d")

google_business_content = get_html_page(page_url)  # Получили валидный HTML
json_articles = find_articles(google_business_content)  # Получили массив заголовков в формате json
publish_report("data.json", page_url, today, json_articles)  # Записали заголовки в json-файл: data.json
