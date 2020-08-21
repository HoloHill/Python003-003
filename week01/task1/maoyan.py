import requests
from bs4 import BeautifulSoup as bs
import controller as c
import pandas as pd



urls = c.moviesurl(f'https://maoyan.com/films')
movie_info_list = c.moviesinfo(urls)
movie_data = pd.DataFrame(data=movie_info_list)
movie_data.to_csv('./task1/movies10.csv', encoding='utf8', index=False, header=False)