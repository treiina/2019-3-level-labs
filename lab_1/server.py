# Сервер
import htmlCrawler
from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def open_html_page(url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru"):
    htmlCrawler.publish_report(url)
    f = open("C:/Users/Катя/PycharmProjects/2019-3-level-labs/articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    json_dict = json.loads(json_str)
    return render_template("index.html", data=json_dict)


if __name__ == "__main__":
    app.run()
