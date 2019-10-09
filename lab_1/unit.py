import unittest
import json
import htmlCrawler
import requests

class Test_html(unittest.TestCase):

    def test_structure_url_2(self):
        f = open("articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        dict_keys = list(json_dict.keys())
        keys=['url','creationDate','articles']
        self.assertEqual(dict_keys,keys)
        self.assertIsNone(json_dict.get('title'))

    def test_get_titles(self):
        page=htmlCrawler.get_html_page('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru')
        articles = htmlCrawler.find_articles(page)#возвращается список articles
        htmlCrawler.publish_report('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru')
        f = open("articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        for title in json_dict["articles"]:
         self.assertEqual(json_dict["articles"], articles)
    


    def test_get_html_page(self):
        f = open("articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        url_request = requests.get(json_dict['url'])
        self.assertEqual(url_request.status_code, 200)


if __name__== '__main__':
    unittest.main()
