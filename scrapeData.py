
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time 
import re
import csv


#this works only in my pc 
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



'''
Opens file with links as readable
'''
with open('links.txt', 'r') as links:

	"""
	loop through the file and gets every URL
	"""
    for url in links:
    	driver.get(url)
    	content = driver.page_source
    	soup = BeautifulSoup(content,'html.parser')
    	
    	

    	items = soup.find_all('main',{'class':'main'})

    	for item in items:
    		#decription row
    		header = []

    		#data that belongs to the description
    		data = []

    		#dictionary that holds the description and its data
    		real_estate_description = {}


    		#find the title , assing in the dictionary
    		title = soup.find('h1',{'class','classified__title'})

    		if title is not None:
    			title = title.text.replace('\n','')
    			title = ' '.join(title.split()).split()[0]
    			real_estate_description ['type of property'] = title

    		'''
			is going to only get the description and the data that belongs to it
			'''
    		for elem in soup.find_all('th',attrs={'class':'classified-table__header'}):
    			header.append(elem.text.strip())

    		#data from description
    		for elem in soup.find_all('td',attrs={'class':'classified-table__data'}):
    			element = elem.text.replace(' ','')
    			data.append(element.replace('\n',''))

    		'''
			everthing is in a dictionary, the description is the key and the data that belongs to the description is the value
			'''
    		count = 0
    		for dic in header:
    			real_estate_description[dic]= data[count]
    			count +=1


    		"""
			override the price, it is much easier this way
			"""
    		price = soup.find('p',{'class':'classified__price'})

    		if price is not None:
    			price = price.text.replace('\n','').split()[0]
    			real_estate_description['Price'] = price
			
    		'''
    		this normally gets the local (place of living) from the page, it doesnt seem to work in this program like it should do
    		'''
    		try:
		
	    		divs = soup.find_all('span',{'class':'classified__informatio--address-row'})

	    		for div in divs:
	    			for span in div:
	    				span = span.text.split()
	    				
	    		for s in dude:
	    			real_estate_description['local'] = s


	    	except:
	    		real_estate_description['local'] = 'None'


			'''
			append everything in the csv file we made
		
			'''

	    	with open('cvs2.csv','a',encoding='utf-8',newline='') as f:
	    		the_writer = csv.writer(f)

	    		if real_estate_description.get('local') is not None:
	    			local = real_estate_description.get('local')
	    		

	    		if real_estate_description.get('type of property') is not None:
	    			type_of_property = real_estate_description.get('type of property')

	    		else: 
	    			type_of_property ='None'

	    		if real_estate_description.get('subtype of property') is not None: 
	    			subtypeProperty = real_estate_description.get('subtype of property')
	    		else:
	    			subtypeProperty ='None'

	    		if real_estate_description.get('Price') is not None: 
	    			price = real_estate_description.get('Price')
	    		else:
	    			price ='None'

	    		if real_estate_description.get('typer of sale') is not None: 
	    			type_of_sale = real_estate_description.get('type of sale')
	    		else:
	    			type_of_sale ='None'

	    		if real_estate_description.get('Bedrooms') is not None: 
	    			rooms = real_estate_description.get('Bedrooms')

	    		else:
	    			rooms ='None'

	    		if real_estate_description.get('Living area') is not None: 
	    			area = real_estate_description.get('Living area')	    			
	    		else:
	    			area ='None'

	    		if real_estate_description.get('Kitchen type') is not None: 
	    			kitchen = 'Yes'
	    		else:
	    			kitchen ='No'

	    		if real_estate_description.get('Terrace') is not None:
	    			terrace = 'Yes'
	    		else:
	    			terrace = 'No'

	    		if real_estate_description.get('Garden') is not None:
	    			garden = 'Yes'
	    		else:
	    			garden ='No'

	    		if real_estate_description.get('Furnished') is not None:
	    			furnished = 'Yes'
	    		else: 
	    			furnished = 'No'
	    		
	    		if real_estate_description.get('open fire') is not None:
	    			openfire = 'Yes'
	    		else:
	    			openfire = 'No'

	    		if real_estate_description.get('Surface of the plot'):
	    			plot = real_estate_description.get('Surface of the plot')
	    		else: 
	    			plot ='None'

	    		if real_estate_description.get('Building condition'):
	    			state_building = real_estate_description.get('Building condition')
	    		else:
	    			state_building ='None'

	    		if real_estate_description.get('Swimming pool') is not None:
	    			pool = 'Yes'
	    		else:
	    			pool = 'No'

	    		if real_estate_description.get('Number of frontages') is not None:
	    			facades = real_estate_description.get('Number of frontages')
	    		else: 
	    			facades ='None'

	    		if real_estate_description.get('Living area') is not None:
	    			surface = real_estate_description.get('Living area')
	    		else:
	    			surface ='None'

	    		info = [local,type_of_property,subtypeProperty,price,type_of_sale,rooms,area,kitchen,furnished,openfire,terrace,garden,surface,plot,facades,pool,state_building]


	    		the_writer.writerow(info)



driver.close()
       