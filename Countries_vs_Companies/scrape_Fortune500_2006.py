# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:26:31 2019

@author: Akshay
"""

import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import re

years = []
pages = ['','101_200.html','201_300.html','301_400.html','401_500.html']
revenue = []
c_name = []
profit = []
rnk = []

regex = re.compile('.*maglisttable.*|.*with220inset.*')

for year in range(2006,2013):
    
    for page in pages:
        #page = pages[0]
        base_url = 'https://money.cnn.com/magazines/fortune/fortune500/'+str(year)+'/full_list/'+page

        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        
        try:
            wpage = requests.get(base_url)
            data = wpage.text
            soup = BeautifulSoup(data, 'lxml')
            table = soup.find('table', attrs={'class':regex})
            
            tr_comps = table.findAll('tr')
            #company_names = table.findAll('td',attrs={'class':'company'})
            #Revenue_profit = table.findAll('td',attrs={'class':'datacell'})
            
            for tr_comp in tr_comps:
                chk= tr_comp.find('td')
                if chk is None:
                    pass
                else:
                    rnk.append(tr_comp.findAll('td')[0].text.replace('\n','').replace(',',''))
                    c_name.append(tr_comp.findAll('td')[1].text.replace('\n','').replace(',',''))
                    years.append(year)
                    revenue.append(float(tr_comp.findAll('td')[2].text.replace('\n','').replace(',','')))
                    profit.append(float(tr_comp.findAll('td')[3].text.replace('\n','').replace(',','')))
            
        except:
            pass
        
zippedList =  list(zip(years, rnk, c_name, revenue, profit))
data = pd.DataFrame(zippedList ,columns = ['year' , 'Rank', 'company', 'revenue', 'profit'])  

data.to_csv("f500_history_2.csv")  


