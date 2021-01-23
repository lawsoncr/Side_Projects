# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:24:36 2021

@author: claws
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

html = 'https://www.newegg.com/p/pl?d=amd+cpu'

#opens connection grabs page
client = uReq(html)
page_html = client.read()
client.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll('div', {"class":"item-container"})


filename = "gpu3.csv"
f = open(filename, "w")

headers = "Info\n"

f.write(headers)

for contain in containers:
   #brand = contain.div.div.a.img["title"]
   
   title = contain.findAll("a", {"class":"item-title"})
   product_info = title[0].text
   
   #stock = contain.findAll("li",{"class":"item-stock"}) 
   #stock[0].text 
   
   #print("Brand: " + brand)
   print("Info: " + product_info)
   #print("Stock: " + stock)
   
   f.write(product_info.replace(",", "|") + "\n")
   
f.close()