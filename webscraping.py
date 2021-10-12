import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0)  chrome/94.0.4606.81 Gecko/20100101 Firefox/93.0'}

for page in range(1,4):
    url = "https://www.immoweb.be/en/search/house/for-sale/brussels/district?countries=BE&page={}&orderBy=relevance".format(page)
    driver = webdriver.Chrome(executable_path=r"/home/mokegg/.local/chromedriver")
    r = requests.get(url, headers=headers)
    print(r.status_code)

    driver = webdriver.Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.title)

    items = soup.find_all('div', {'class' : 'search-results-container'})
    driver.close()
    for item in items:
    for elem in soup.find_all('a', attrs={"class": "card__title-link"}):
        file = open("./challenge-collecting-data/links.txt",'a')
        file.write(elem.get("href"))
        file.write("\n")
        print(elem.get("href"))
        print("\n")
