
import json
import htmlCrawler
import requests

test_page_file = open("SavedHtml.html", "r", encoding="UTF-8")
test_page_content = test_page_file.read()
test_page_file.close()
articles = htmlCrawler.find_articles(test_page_content)
print(articles)