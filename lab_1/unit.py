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
        test_page_file = open("SavedHtml.html", "r", encoding="UTF-8")
        test_page_content = test_page_file.read()
        test_page_file.close()
        articles = htmlCrawler.find_articles(test_page_content)
        self.assertListEqual(articles, [{'title': '«АвтоВАЗ» выпустит новую модель'}, {'title': 'Lada Vesta будет оснащаться вариатором и двигателем 1,6 литра HR-16'}, {'title': 'Изображение нового Skoda Rapid в Новосибирске 9 октября 2019'}, {'title': 'Майкл Най, Titan Ventures: «Bitcoin ниже $8000 — я покупаю'}, {'title': 'Создатели родстера «Крым» рассказали о его недостатках'}, {'title': 'Найден склад, где Nissan Skyline продают дешевле нового айфона'}, {'title': 'Новый Mercedes-Maybach GLS: первые фотографии без камуфляжа'}, {'title': 'АвтоВАЗ опроверг выход Lada Van, но выпустит другие новинки'}, {'title': 'BMW представила новый седан M8 Gran Coupe'}, {'title': 'Новый минимум Bitcoin и рост альткоинов. Обзор рынка криптовалют'}, {'title': '«Лента» запускает AR-игру для покупателей'}, {'title': 'Poloniex удалит из листинга Steem, Pascal, GameCredits, Navcoin, LBRY Credits и Clams'}, {'title': 'Составлен рейтинг самых популярных дизельных авто в Москве'}, {'title': 'Китайцы обновили семиместный внедорожник, который привезут в Россию'}, {'title': 'Binance запустила сервис P2P-торговли. Монета биржи выросла на 9%'}, {'title': '10 технологий, которых не было на машинах еще 10 лет назад'}, {'title': 'Volvo и Geely займутся совместной разработкой двигателей нового поколения'}, {'title': 'FoodPlex из экосистемы «Сбербанка» предложила небольшим кафе и ресторанам систему управления процессами по подписке'}, {'title': 'Обновленная Skoda Superb в России: пока только один двигатель'}, {'title': 'Глава Forbes: криптовалюты — это крик о помощи современного общества'}, {'title': 'Дайджест дня: будущий Sandero, Honda с икс-фейсом и другие события индустрии'}, {'title': 'Новый Kia Sorento засняли на дороге в Корее'}, {'title': 'Посмотрите на Acura, у которой очень много лошадей'}, {'title': 'Telegram сможет блокировать криптовалюту пользователей'}, {'title': 'УАЗ «Патриот» поступил на дежурство по охране природных ресурсов'}, {'title': 'Toyota RAV4: Можно ли заказать машину без «допов»? - блогер'}, {'title': 'Появились первые изображения Mitsubishi Outlander нового поколения'}, {'title': 'Lamborghini представит миру первую четырёхдверную модель с электродвигателем'}, {'title': 'Сезон альткоинов на подходе. Графики XRP и ETH говорят в пользу роста'}, {'title': 'Прибыль Samsung упала на 56%'}, {'title': 'Дайджест дня: новый глава компании Nissan, Ford Puma на конвейере и другие события индустрии'}, {'title': 'Немецкий программист взломал сервер вымогателя биткоинов в ответ на атаку'}, {'title': 'В Америке начали открывать поликлиники прямо в магазинах'}, {'title': 'Hyundai Creta второго поколения с большим тачскрином и многоярусной оптикой уже у дилеров - КОЛЕСА.ру – автомобильный журнал'}, {'title': '«Вот что значит китайцы – даже ограничители сделали по-немецки правильно»: Блогер похвалил Chery Tiggo 4'}, {'title': 'Alfa Romeo показала реальные фотографии новой модели Tonale'}, {'title': 'В шаге от полного доминирования: Чего не хватает Haval F7 для абсолютного успеха?'}, {'title': 'Bitwise: мы как никогда близки к одобрению биткоин-ETF'}, {'title': '«Bitcoin снова поднимется выше $9000». Как изменится цена криптовалюты'}, {'title': 'МАЗ открыл завод во Вьетнаме'}, {'title': 'Для огородных дел и путешествий: Почему не стоит бояться Skoda Kodiaq с «мокрой» DSG'}, {'title': 'Посмотрите, как BMW M8 разгоняется до 100 км/ч за 2,88 секунды'}, {'title': 'В России создано ПО против мошенников, которые представляются «сотрудниками банка»'}, {'title': 'Краш-тест: кроссовер Renault Arkana разбился на "отлично"'}, {'title': 'Кроссовер Mazda CX-4 обновлен в стиле старших моделей'}, {'title': 'Ущерб SoftBank от вложений в Uber и WeWork может превысить $5 млрд'}, {'title': 'Chevrolet доработал экстремальную версию пикапа Colorado'}, {'title': 'Цена биткоина и других криптовалют резко выросла'}, {'title': 'Доллар проигнорировал сентябрьские «минутки» ФРС'}, {'title': 'Continental разработала "обидчивую" шину: она умеет надуваться сама'}, {'title': 'На Украине нашли замену выпущенному при Хрущеве грузовику'}, {'title': 'Стала известна полная информация о новой Skoda Octavia'}, {'title': 'Toyota GranAce: новый бизнесвэн для Японии'}, {'title': 'Toyota показала беспилотники для Олимпиады в Токио'}, {'title': 'Инвестирование и трейдинг. Что выбрать при нестабильном курсе Bitcoin'}, {'title': 'Составлен топ самых популярных марок на вторичном авторынке РФ'}, {'title': 'BMW представит электрокар на базе модели 1 Series в 2021 году'}, {'title': 'Разочарованные инвесторы. Почему биржевые индексы ускорили падение'}, {'title': 'Обнародованы фотографии новой версии Kia Optima'}, {'title': 'Курс биткоина поднялся выше $8200'}, {'title': '09.10.2019 Пострадавший от вируса-вымогателя программист взломал разработчиков вируса'}, {'title': 'Кто поцарапал? Tesla научились полезному трюку'}, {'title': 'Белка превратила моторный отсек Kia Sorento в склад с орехами'}, {'title': 'Администратор штрафов в «Платоне» переходит с софта Microsoft на российское и открытое ПО'}, {'title': 'Протокол заседания ФРС: печатный станок готов к запуску?'}, {'title': '«Детёныш Гелика»: Самодельный болотоход на базе LADA 4x4 удивил сеть'}, {'title': 'Зажали со всех сторон: Азия активно «выживает» отечественный автопром из России?'}, {'title': 'Ford Mustang GT превратили в 710-сильный шоукар'}, {'title': 'Как создать самоуправляемый автомобиль после взлома iPhone'}, {'title': 'Что купить вместо LADA Vesta? Бывший «веставод» высказался о Volkswagen Polo'}]
)
        '''
        page=htmlCrawler.get_html_page('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru')
        articles = htmlCrawler.find_articles(page)#возвращается список articles
        htmlCrawler.publish_report('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru')
        f = open("articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        for title in json_dict["articles"]:
         self.assertEqual(json_dict["articles"], articles)
    '''


    def test_get_html_page(self):
        f = open("articles.json", encoding='UTF-8')
        json_str = f.read()
        f.close()
        json_dict = json.loads(json_str)
        url_request = requests.get(json_dict['url'])
        self.assertEqual(url_request.status_code, 200)


if __name__== '__main__':
    unittest.main()
