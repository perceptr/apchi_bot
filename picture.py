import random
from YandexImagesParser.ImageParser import YandexImage


def get_picture_links(query):
    parser = YandexImage()
    urls = []
    for item in parser.search(query):
        urls.append(item.preview.url)

    return urls


manicure_urls = get_picture_links("маникюр без лица")
pedicure_urls = get_picture_links("педикюр без лица")


def get_manicure_link():
    return random.choice(manicure_urls)


def get_pedicure_link():
    return random.choice(pedicure_urls)
