import json
import requests


def test_structure_url(f):
    f = open("articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    json_dict = json.loads(json_str)
    if json_dict["url"]:
        return True
    else:
        return False


def test_structure_head(f):
    f = open("articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    json_dict = json.loads(json_str)
    if json_dict["articles"]:
        if json_dict["articles"][0]["title"]:
            return True
        else:
            return False
    else:
        return False

def test_heads_notEmpty(f):
    f = open("articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    count=0
    json_dict = json.loads(json_str)
    for i in range(len(json_dict["articles"])):
        if json_dict["articles"][i]["title"]:
            count=count+1

    return count==len(json_dict["articles"])



def test_html_page(f):
    f = open("articles.json", encoding='UTF-8')
    json_str = f.read()
    f.close()
    json_dict = json.loads(json_str)
    url_request = requests.get(json_dict["url"])

    if url_request.status_code == 200:

        return True
    else:

        return False


print(test_html_page("articles.json"))



