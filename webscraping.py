import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0'}


url = 'https://www.immoweb.be/en/search/house/for-sale/brussels/district?countries=BE&page=1&orderBy=relevance'
driver = webdriver.Firefox()

r = requests.get(url, headers=headers)
print(r.status_code)
driver.get(url)
soup = BeautifulSoup(driver.page_source, features='lxml')
print(soup.title)

items = soup.find_all('div', {'class' : 'search-results-container'})

for item in items:
    for elem in soup.find_all('a', attrs={"class": "card__title-link"}):
        print(elem.get("href"))
        print("\n")