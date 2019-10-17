import unittest
import json
import htmlCrawler
import requests

class Test_html(unittest.TestCase):

    def setup(self):
        htmlCrawler.publish_report("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru")
        f = open("C:/Users/Катя/PycharmProjects/2019-3-level-labs/articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        return json_dict


    def test_structure_url_2(self):
        '''
        htmlCrawler.publish_report("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru")
        f = open("C:/Users/Катя/PycharmProjects/2019-3-level-labs/articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)'''
        json_dict = self.setup()
        dict_keys = list(json_dict.keys())
        keys=['url','creationDate','articles']
        self.assertEqual(dict_keys,keys)
        for i in range (len(json_dict['articles'])):
         self.assertIsNotNone(json_dict['articles'][i]['title'])

    def test_get_titles(self):
        page= open("SavedHtml.html", "r", encoding="UTF-8")
        page_content = page.read()
        page.close()
        articles = htmlCrawler.find_articles(page_content)
        self.assertListEqual(articles, [ {
            "title": "Майкл Най, Titan Ventures: «Bitcoin ниже $8000 — я покупаю"
        },
        {
            "title": "Названа дата начала продаж высокого «каблука» Lada"
        },
        {
            "title": "Нужна ли LADA Vesta с японской КПП и французским двигателем?"
        },
        {
            "title": "Так будет выглядеть новый Volkswagen Golf: первые эскизы - Авто Mail.ru"
        },
        {
            "title": "Новый Skoda Rapid для РФ получит внешность в силе еврохэтча Scala. Премьера – в конце года"
        },
        {
            "title": "По 350 тысяч: реальные отзывы хозяев Solaris, Rio, Polo и Logan - Авто Mail.ru"
        },
        {
            "title": "Придуман новый способ подогрева сидений в автомобиле - Авто Mail.ru"
        },
        {
            "title": "SEC отклонила заявку на биткоин-ETF от Bitwise"
        },
        {
            "title": "Обнаружен склад, где Nissan Skyline продают за «гроши»"
        },
        {
            "title": "Как теолог стал гендиректором Nissan"
        },
        {
            "title": "BMW представила новый седан M8 Gran Coupe"
        },
        {
            "title": "Будущий конкурент Bentley Bentayga от Mercedes явился без камуфляжа"
        },
        {
            "title": "Кроссовер Aston Martin DBX: подробности и заказы в России"
        },
        {
            "title": "Глава Forbes: Bitcoin играет очень важную роль в современном мире"
        },
        {
            "title": "Кроссовер Geely Vision X6 опять обновлен"
        },
        {
            "title": "Создатели родстера «Крым» рассказали о его недостатках"
        },
        {
            "title": "Китайский «ГАК» vs «Крузак»: Россияне предпочтут покупать новый GAC GS8 вместо Land Cruiser"
        },
        {
            "title": "PayPal «обеднел» на 228 млн долларов"
        },
        {
            "title": "Binance запустила сервис P2P-торговли. Монета биржи выросла на 9%"
        },
        {
            "title": "UAZ Patriot с автоматом"
        },
        {
            "title": "Чем новый Toyota RAV4 лучше своего главного конкурента в лице Volkswagen Tiguan?"
        },
        {
            "title": "10 технологий, которых не было на машинах еще 10 лет назад"
        },
        {
            "title": "Bitmain представила улучшенные ASIC-майнеры S17+ и T17+"
        },
        {
            "title": "Белка устроила склад орехов под капотом автомобиля (фото) - Авто Mail.ru"
        },
        {
            "title": "И скупился, и поиграл: Лента придумала AR-игру для покупателей"
        },
        {
            "title": "В Южной Корее 13,5 тыс. магазинов начнут принимать к оплате криптовалюту"
        },
        {
            "title": "Немецкий программист взломал сервер вымогателя биткоинов в ответ на атаку"
        },
        {
            "title": "Первый легально перепроданный Ford GT ушел с молотка за тройную цену"
        },
        {
            "title": "Дайджест дня: будущий Sandero, Honda с икс-фейсом и другие события индустрии"
        },
        {
            "title": "Обновленная Skoda Superb в России: пока только один двигатель"
        },
        {
            "title": "Пластиковое «рено» от производителя: Механик рассказал об ужасном качестве «допов» для Renault Kaptur"
        },
        {
            "title": "Volvo и Geely займутся совместной разработкой двигателей нового поколения"
        },
        {
            "title": "Poloniex удалит со своей биржи шесть криптовалют"
        },
        {
            "title": "Появились изображения Mitsubishi Outlander нового поколения"
        },
        {
            "title": "Осажденный со всех сторон «Техносерв» создал новые юрлица и получил 700-миллионный господряд"
        },
        {
            "title": "FoodPlex из экосистемы «Сбербанка» предложила небольшим кафе и ресторанам систему управления процессами по подписке"
        },
        {
            "title": "Найден новый мопед «Карпаты-2», забытый в гараже на 30 лет"
        },
        {
            "title": "На Украине нашли замену выпущенному при Хрущеве грузовику"
        },
        {
            "title": "Лошадей много не бывает: странный тюнинг из США (видео) - Авто Mail.ru"
        },
        {
            "title": "«Ростелеком» за 1,7 миллиарда купил поставщика московской видеослежки"
        },
        {
            "title": "Сезон альткоинов на подходе. Графики XRP и ETH говорят в пользу роста"
        },
        {
            "title": "Новый минимум Bitcoin и рост альткоинов. Обзор рынка криптовалют"
        },
        {
            "title": "Прибыль Samsung упала на 56%"
        },
        {
            "title": "Ford выпустит спецсерию «Мустангов» с рекордной мощностью"
        },
        {
            "title": "Посмотрите, как BMW M8 разгоняется до 100 км/ч за 2,88 секунды"
        },
        {
            "title": "Новый Suzuki Jimny пользуется ажиотажным спросом"
        },
        {
            "title": "В России создано ПО против мошенников, которые представляются «сотрудниками банка»"
        },
        {
            "title": "«Bitcoin снова поднимется выше $9000». Как изменится цена криптовалюты"
        },
        {
            "title": "Налоговая США впервые за пять лет обновила правила для криптоинвесторов"
        },
        {
            "title": "Lamborghini представит миру первую четырёхдверную модель с электродвигателем"
        },
        {
            "title": "Раскрыта внешность серийного кроссовера Alfa Romeo Tonale"
        },
        {
            "title": "Глава Bitwise: «Мы как никогда близки к одобрению Bitcoin-ETF"
        },
        {
            "title": "Дайджест дня: новый глава компании Nissan, Ford Puma на конвейере и другие события индустрии"
        },
        {
            "title": "В шаге от полного доминирования: Чего не хватает Haval F7 для абсолютного успеха?"
        },
        {
            "title": "«Вот что значит китайцы – даже ограничители сделали по-немецки правильно»: Блогер похвалил Chery Tiggo 4"
        },
        {
            "title": "УАЗ «Патриот» поступил на дежурство по охране природных ресурсов"
        },
        {
            "title": "Mazda обновила CX-4: фирменная решётка радиатора и новая мультимедийная система"
        },
        {
            "title": "Hyundai Creta второго поколения с большим тачскрином и многоярусной оптикой уже у дилеров"
        },
        {
            "title": "Continental разработала \"обидчивую\" шину: она умеет надуваться сама"
        },
        {
            "title": "Цена биткоина и других криптовалют резко выросла"
        },
        {
            "title": "Для огородных дел и путешествий: Почему не стоит бояться Skoda Kodiaq с «мокрой» DSG"
        },
        {
            "title": "Пострадавший от вируса-вымогателя программист взломал разработчиков вируса"
        },
        {
            "title": "Криптосообщество создаст неподконтрольную корпорациям версию Libra"
        },
        {
            "title": "Кто поцарапал? Tesla научились полезному трюку"
        },
        {
            "title": "Новое поколение Kia Sorento: первые фото - Авто Mail.ru"
        },
        {
            "title": "Разочарованные инвесторы. Почему биржевые индексы ускорили падение"
        },
        {
            "title": "BMW представит электрокар на базе модели 1 Series в 2021 году"
        },
        {
            "title": "Доллар проигнорировал сентябрьские «минутки» ФРС"
        },
        {
            "title": "У Solaris в России появится совершенно новая версия - Авто Mail.ru"
        },
        {
            "title": "Администратор штрафов в «Платоне» переходит с софта Microsoft на российское и открытое ПО"
        }
    ])
      

    def test_get_html_page(self):
        '''
        f = open("C:/Users/Катя/PycharmProjects/2019-3-level-labs/articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        '''
        json_dict = self.setup()
        url_request=htmlCrawler.get_request(json_dict['url'])
        self.assertEqual(url_request.status_code, 200)
        url_request = htmlCrawler.get_request('123')
        self.assertEqual(url_request.status_code,404)


if __name__== '__main__':
    unittest.main()
