import requests
from bs4 import BeautifulSoup
from csv import writer

with open('immo_data.csv', 'w', encoding='utf8', newline='') as f:
    the_writer = writer(f)
    header = ['Property Type', 'Price', 'Bedrooms', 'Livable area']  # , 'Total land area', 'Date available']
    the_writer.writerow(header)

with open('links.txt', 'r') as links:
    for url in links:
        my_url = url
        #     my_url = "https://www.immoweb.be/en/classified/house/for-sale/laeken/1020/9560029?searchId=616448237ea81"

        res = requests.get(my_url).text
        soup = BeautifulSoup(res, "lxml")

        # ------------------------------------------------------
        title = soup.find('h1', {'class': 'classified__title'})
        if title is not None:
            title = title.text.replace('\n', '')
            title = ' '.join(title.split()).split()[0]

        room_area = soup.find('div', {'class': 'classified__header-secondary-info'})
        if room_area is not None:
            room_area = room_area.text.replace('\n', '').split()
            rooms = room_area[0]
            area = room_area[3]

        # ------------------------------------------------------
        price = soup.find('p', {'class': 'classified__price'})
        if price is not None:
            price = price.text.replace('\n', '').split()[0]
        info = [title, price, rooms, area]

        with open('immo_data.csv', 'a', encoding='utf8', newline='') as f:
            the_writer = writer(f)
            the_writer.writerow(info)
        # print(title, price, rooms, area)
