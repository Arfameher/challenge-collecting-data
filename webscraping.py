import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
from threading import Thread
from bs4 import BeautifulSoup
import requests
from time import perf_counter
import concurrent.futures

start = perf_counter()

num = int(input("Enter the number of pages to scrape links from (between 2 and 330): "))

browser = input("Enter the browser name you are using (Firefox/Chrome) : ")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0)  chrome/94.0.4606.81 Gecko/20100101 Firefox/93.0'}
url1 = "https://www.immoweb.be/en/search/house/for-sale/brussels/district?countries=BE&page=1&orderBy=relevance"
r = requests.get(url1, headers=headers)
print(r.status_code)

class Links(Thread):
    def __init__(self,url):
        Thread.__init__(self)
        self.url = url

    def run(self):

        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.find_all('div', {'class' : 'search-results-container'})
        
        for item in items:
            for elem in soup.find_all('a', attrs={"class": "card__title-link"}):
                file = open("./challenge-collecting-data/links1.txt",'a')
                file.write(elem.get("href"))
                file.write("\n")
        
if browser.lower() == "firefox":
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


elif browser.lower() == "chrome":
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path="/home/mokegg/.local/chromedriver", options=options)

with concurrent.futures.ThreadPoolExecutor() as executor:
    for page in range(1,num+1):
        url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={}&orderBy=relevance".format(page)
        thread = Links(url)
        executor.map(thread.start(),url)


end = perf_counter()

print("Time taken to scrape = ", end-start)
    

    