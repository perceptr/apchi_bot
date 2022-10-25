import random
from YandexImagesParser.ImageParser import YandexImage


def get_picture_links():
    parser = YandexImage()
    urls = []
    for item in parser.search("маникюр без лица"):
        urls.append(item.preview.url)

    return urls


urls = get_picture_links()


def get_picture_link():
    return random.choice(urls)


print(get_picture_link())