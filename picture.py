import requests
from bs4 import BeautifulSoup as bs
import random


def get_picture_link():
    r = requests.get("https://www.google.ru/search?tbm=isch&q=ноготочки")
    text = r.text
    soup = bs(text, "html.parser")
    the_result = {}
    i = 0
    for qwerty in soup.find_all('img'):
        the_result[i] = qwerty.get('src')
        print(the_result[i])
        i = i + 1
        print(i)
    i = random.randint(1, 19)
    return the_result[i]
