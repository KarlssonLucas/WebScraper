import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#function to create csv file
def create_file(titles, imdb_ratings):
    global f
    f = open('Ratings.csv', 'w')
    header = 'Name, IMDb rating\n'
    f.write(header)
    for i in range(len(titles)):
        f.write(titles.__getitem__(i)+","+imdb_ratings.__getitem__(i)+'\n')

headers = {"Accept-Language": "en_US, en:q=0.5"}
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")
# print(soup.prettify()) Gathers information for the whole header

titles = []
imdb_ratings = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:
    title = container.h3.a.text
    titles.append(title)
    rating = container.strong.text
    imdb_ratings.append(rating)

create_file(titles, imdb_ratings)



