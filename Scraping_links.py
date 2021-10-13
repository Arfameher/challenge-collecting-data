import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager # GeckoDriver is a link between selenium tests and the Firefox browser.

from datetime import date
from threading import Thread
import concurrent.futures
from bs4 import BeautifulSoup
import requests
from time import perf_counter
import time

start = perf_counter() # The timer is starting to calculate amount of time required to scrape.
today = date.today()

# User asked to input number of pages to scrape.
num = int(input("Enter the number of pages to scrape links from (between 2 and 330): "))
# User asked to input which broswer to use.
browser = input("Enter the browser name you are using (Firefox/Chrome) : ")

# The below lines of code is used to check the HTTP status of the webpage. if 200 OK then its a successful request.
"""
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0)  chrome/94.0.4606.81 Gecko/20100101 Firefox/93.0'}
url1 = "https://www.immoweb.be/en/search/house/for-sale/brussels/district?countries=BE&page=1&orderBy=relevance"
r = requests.get(url1, headers=headers)
print(r.status_code)
"""

class Links(Thread):

    """
    A Thread class to call in each url and run parallel programming.
    Each url extracts about 30 links of listings. Threading in python is used to run multiple threads (tasks)
    at the same time. 
    """
    def __init__(self,url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        """
        The run() method of thread class is called whenever it is started using thread.start()
        This method runs parallel to all the threads called. It can be called multiple times.
        """
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        items = soup.find_all('div', {'class' : 'search-results-container'})
        
        for item in items:
            for elem in soup.find_all('a', attrs={"class": "card__title-link"}):
                file = open(f"./links_{today}.txt",'a')
                file.write(elem.get("href"))
                file.write("\n")

"""
    A headless browser is a web browser without a graphical user interface.
    Here we are setting up headless browser for chrome and firefox users.
    """        
# Headless browsing for firefox is defined here.
if browser.lower() == "firefox":
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

# Headless browsing for chrome is defined here.
elif browser.lower() == "chrome":
    executablepath = input("Enter the executable path where chrome is stored : ")
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=executablepath, options=options)

"""
Using Concurrent.futures to speed up the process for each thread. It is an abstract class that provides methods to 
execute calls asynchronously. It provides a high level interface for asynchronously executing callables. This can be 
performed with threads, using ThreadPoolExecutor.
"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    for page in range(1,num+1): 
        url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={}&orderBy=relevance".format(page)
        thread = Links(url)
        executor.map(thread.start(),url)   # Here the run method in class Links is called and url is passed as each thread is called.


end = perf_counter()
print("Time taken to scrape = ", end-start) # Prints out the time taken to run the program.