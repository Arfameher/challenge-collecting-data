# Challenge Collecting Data
Data collection from real estate websites to make price predictions on real estate sales in Belgium.
<p align="center">
  <img src="<p align="center">
  <img src="https://user-images.githubusercontent.com/11362429/137072895-f14036b1-8b88-4898-b8ea-aa1c82556fc8.png" width="600" height="315" />                       </p>

***
### Description
This project is about creating a large dataset on real estate for price prediction purposes. Here we have chosen to collect data from immoweb website. This is a data collection tool that can collect real estate data from websites. The data is to be used to make price predictions on real estate sales in Belgium. The code could collect the following information from every listing on ImmoWeb.be website and the data is stored in a csv file.
- Locality
- Type of property
- Subtype of property
- Price
- Type of sale
- Number of rooms
- Area
- Fully equipped kitchen
- Furnished
- Open fire
- Terrace
- Garden
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool
- State of the building

***
### Installation
For the codes to work, the following packages are required:
  * Selenium
  * BeautifulSoup
  * Pandas

***
### Usage
The tool consists of two codes, named *'scraping_links.py'*and *'scrapeData.py'*.
  * *scraping_links.py* is used to access the search results form the website and it collects the links to each property in the search results and saves them into a '.txt' file. It has been demonstrated that it can collect 10,000 links from the ImmoWeb website.
  * *scrapeData.py* is used to access each link and scrape the required data listed in the description section and saves the datato a '.csv' file.

For successful scraping, *scraping_links.py* needs to rum before *scrapeData.py*. 

***
### Visuals
Running the 1stcode:
![User inputs](../../../Pictures/Screenshot from 2021-10-13 15-32-44.png)
sample data sheet from pandas.

![pandasVisualisation](pandasVisualisation.png)

***
### Contributors
This project is workedout by the following team:

- [Arfameher](https://github.com/Arfameher)                                                                                    
- [Mekonnen](https://github.com/mokegg)                                                                                           
- [Sebastian](https://github.com/sebastianchavezz)                                                                                                                                           
***
### What could be improved 
Threading has been implemented on the first code, and the time needed to extract the links was shortened dramatically. The speed of data collection could be improved by implementing threadig on the second code as well.

### Timeline
October 2021

Time limit: 3 days --> 11/10/2021 - 13/10/2021
This project was given to us to scrape data from a real estate website and gather all the information in a csv file for about 10000 listings.                                                                                                                                            
***
### Personal Situation
This is a group project given to us at [BeCode](https://becode.org/)
Here is how you can contact us :
    
##### LinkedIn :                                                         
- [Arfameher](https://www.linkedin.com/in/arfa-meher/)                    
- [Mekonnen](https://www.linkedin.com/in/mekonnen1/?originalSubdomain=be)
- [Sebastian](https://www.linkedin.com/in/sebastian-chavez-2-9a0790186/)  
                                                                                                                                           
##### Email :                                                                                                                                          
- arfaameher@outlook.com                                                                                                                                          
- mekonnen.gebrehiwot1@gmail.com
- sebastianchavez940@gmail.com                                                                                                                                     
