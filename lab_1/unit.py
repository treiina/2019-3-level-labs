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

    #def get_titles(self):
     #   htmlCrawler.find_articles('Google Новости - Бизнес - Последние.html')#возвращается список articles


    def get_html_page(self):
        f = open("articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        url_request = requests.get(json_dict['url'])
        self.assertEqual(url_request.status_code, 200)

if __name__== '__main__':
    unittest.main()
