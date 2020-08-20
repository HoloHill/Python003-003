import requests
from bs4 import BeautifulSoup as bs

def moviesurl(myurl):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"

    header = {'user-agent':user_agent}

    response = requests.get(myurl, headers=header)

    bs_info = bs(response.text, 'html.parser')

    #获取信息
    urls = []
    for tags in bs_info.find_all('div', attrs={'class':'channel-detail movie-item-title'},limit=10):
        for atag in tags.find_all('a',):
            urls.append(f'https://maoyan.com' + atag.get('href'))
    return urls

def moviesinfo(urls):
    for url in urls:
        pass




