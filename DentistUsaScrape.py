# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 12:54:53 2018

@author: Kiran
"""

import bs4 as bs
import urllib.request
import xlwt


wb = xlwt.Workbook()
ws = wb.add_sheet("Houston_Dentist")


title = []
address = []
road = []
phnum = []

for i in range(1,100):
    link = 'http://www.dentists.com/Houston-dentists-directory/TX/'+ str(i)
    link1 = urllib.request.urlopen(link)
    soup = bs.BeautifulSoup(link1, 'lxml')


    for dentist in soup.find_all('a', class_='office_title'):
        sheetdata = dentist.text
        title.append(sheetdata)


    for dentist in soup.find_all('address', class_='address'):
        sheetdata = dentist.text
        address.append(sheetdata)
        
    for dentist in soup.find_all('span', class_='city_state_zip'):
        sheetdata = dentist.text
        road.append(sheetdata)    


    for dentist in soup.find_all('p', class_='phone'):
        sheetdata = dentist.text
        phnum.append(sheetdata)



for i in range(len(title)):
    ws.write(i, 0, title[i])    
    ws.write(i, 1, address[i]) 
    ws.write(i,2, road[i])
    ws.write(i, 3, phnum[i]) 

wb.save("Houston_Dentist Data.xls")    
       
