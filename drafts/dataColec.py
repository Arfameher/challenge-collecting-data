import requests
from bs4 import BeautifulSoup
from csv 

with open('csv.csv', 'w', encoding='utf-8', newline='') as f:
    the_writer = writer(f)
    description = ['Local','Type of property','Subtype of property', 'Price', 'Type of sale', 'Number of rooms','Area','Fully equipped kitchen','Furnished','Open fire','Terrace','Garden','Surface of the land'
				,'Surface of plot of land', 'Numbers of facades','Swimming pool','State of building']
    the_writer.writerow(description)




with open('links.txt', 'r') as links:
    for url in links:
    	
        my_url = url
        #     my_url = "https://www.immoweb.be/en/classified/house/for-sale/laeken/1020/9560029?searchId=616448237ea81"

        res = requests.get(my_url).text
        soup = BeautifulSoup(res, "lxml")


        items = soup.find_all('main',{'class':'main'})


			#optain the desription and the data 
		for item in items:
			#description; e.g.: price, kitchen, etc
			headers = []
			
			#data from descrition
			data = []

			#dictionary that contains the whole page
			real_estate_description ={}

			title = soup.find('h1',{'class':'classified__title'})
		
			

			"""
			naming the property
			"""


			if title is not None:
				title = title.text.replace('\n','')
				title = ' '.join(title.split()).split()[0]
				real_estate_description['type of property']= title



			'''
			is going to only get the description and the data that belongs to it
			'''

			for elem in soup.find_all('th',attrs={"class":"classified-table__header"}):
				headers.append(elem.text.strip())
				
			"""
			data from descrition
			MUST DO: implement the title, fix the price, fix spaces between words..
			"""
			for elem in soup.find_all('td',attrs={"class":"classified-table__data"}):
				element = elem.text.replace(" ","")
				data.append(element.replace("\n",""))
				

			'''
			everthing is in a dictionary, the description is the key and the data that belongs to the description is the value
			'''
			count = 0
			for dic in headers:
				real_estate_description[dic]= data[count]
				count+=1


			"""
			override the price, it is much easier this way
			"""
			price = soup.find('p',{'class':'classified__price'})
		
			if price is not None:
					price = price.text.replace('\n','').split()[0]
					real_estate_description['Price'] = price

			'''
			append everything in the csv file we made
			I used error handler, because of the fact that some of the keys dont have a value or dont exist.
			this way if it doesnt exist we can assign the variable a NONE value
			this only works if the site is consisted in its way of naming this
			'''
			with open('csv.csv', 'a', encoding='utf-8',newline='') as f:

				the_writer= csv.writer(f)
				try:
					local = real_estate_description.get('local')
					
				except:
					pass
						
				try:
					type_of_property = real_estate_description.get('type_of_property')

				except:
					pass

				try:
					price = real_estate_description.get('Price')
				
				except:
					pass
				
				try:
					type_of_sales = real_estate_description.get('type of sale')

				except:
					pass

				try:
					rooms = real_estate_description.get('Bedrooms')
				except:
					pass
					
				try:
					area = real_estate_description.get("Living area")
				except:
					pass
					
				try:
					if real_estate_description.get('Kitchen type') is not None:
							kitchen = 'Yes'
				except:
					pass
						
				try:
					furnished = real_estate_description.get('Furnished')
				except:
					pass
				
				try:
					openFire = real_estate_description.get('open fire')
				except:
					pass
				
				try:
					terrace = real_estate_description.get('Terrace')
				except:
					pass
				
				try:
					garden = real_estate_description.get('Garden')
				except:
					pass
				
				try:
					surface	= real_estate_description.get('Living area')
				except:
					pass
				
				try:
					plot = real_estate_description.get('Surface of the plot')
				except:
					pass

				try:
					facades = real_estate_description.get('Number of frontages')
				except:
					pass

				try:
					pool= real_estate_description.get('Swimming pool')
				except:
					pass

				try:
					state_building = real_estate_description.get('Building condition')
				except:
					pass

				#this is the final data
				info = [local,type_of_property,price,type_of_sales,rooms,area,kitchen,furnished,openFire,terrace,garden,surface,plot,facades,pool,state_building]


				#to the data that has no value, assing NONE
				for i in range(len(info)):
					if info[i] == None:
						info[i] = 'None'

				#append the rows
				the_writer.writerow(info)

