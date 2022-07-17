import bs4
import requests
url = 'https://habr.com'
base_url = 'https://habr.com/ru/all/'

FILTERS = ['Java','CSS3','Linux']

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1841 Yowser/2.5 Safari/537.36'
}
response = requests.get(base_url, headers = HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features = 'html.parser')

#получили список всех статей
articles = soup.find_all('article')
# print(articles)


for article in articles:

    prev = article.find(class_='tm-article-body tm-article-snippet__lead')
    RESULT = prev.text

    for filter in FILTERS:
        if filter in RESULT:
            title = article.find('h2').find('span').text
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            date = article.find(class_ = 'tm-article-snippet__datetime-published').find('time').attrs['title']
            print(f'Статья: <{title}> по фильтру <{filter}>/ссылка: {url + href}/дата: {date}')


