# Сервер
import htmlCrawler
from flask import Flask, render_template, redirect, url_for
import json


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def open_html_page(url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru"):
    htmlCrawler.publish_report(url)
    f = open("../articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    json_dict = json.loads(json_str)
    return render_template("index.html", data=json_dict)


@app.route('/refresh', methods=['POST'])
def refresh():
    return redirect(url_for('open_html_page'))


@app.route("/other", methods=['POST'])
def open_other_page(url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru"):
    htmlCrawler.publish_report(url)
    f = open("../articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    json_dict = json.loads(json_str)
    arr = []
    for i in range(int(json_dict['creationSec'])+1):
        arr.append(i)
    return render_template("otherPage.html", data=arr)


#Вторая кнопка, чтобы по нажатию происходил переход на другую страницу и на этой странице будет другой шаблон
#Любая страница, массив чисел (сгенерированный)
#Цифры от текущего количества секунд

if __name__ == "__main__":
    app.run()
