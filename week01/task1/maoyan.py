import requests
from bs4 import BeautifulSoup as bs
import lxml.etree

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"

header = {"user-agent":user_agent}

myurl = "https://maoyan.com/films/3606"

response = requests.get(myurl, headers=header)

""" bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        print(atag.text) """

#xml化处理
selector = lxml.etree.HTML(response.text)

#上映日期
release_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
print(f'上映日期{release_date}')
