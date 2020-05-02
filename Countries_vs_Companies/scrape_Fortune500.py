# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:22:59 2019

@author: Akshay
"""

import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

years = []
pages = ['1','101','201','301','401']
revenue = []
c_name = []
profit = []

for year in range(1955,2006):
    
    for page in pages:
        base_url = 'http://archive.fortune.com/magazines/fortune/fortune500_archive/full/'+str(year)+'/'+page+'.html'
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        
        try:
            page = requests.get(base_url)
            data = page.text
            soup = BeautifulSoup(data, 'lxml')
            table = soup.find('table', attrs={'class':'maglisttable'})
            
            tr_comps = table.findAll('tr')
            #company_names = table.findAll('td',attrs={'class':'company'})
            #Revenue_profit = table.findAll('td',attrs={'class':'datacell'})
            
            for tr_comp in tr_comps:
                
                company_name = tr_comp.find('td',attrs={'class':'company'})
                if company_name is None:
                    pass
                else:
                    c_name.append(company_name.text.replace('\n',''))
                    years.append(year)
                    revenue.append(float(tr_comp.findAll('td',attrs={'class':'datacell'})[0].text.replace('\n','').replace(',','')))
                    profit.append(float(tr_comp.findAll('td',attrs={'class':'datacell'})[1].text.replace('\n','').replace(',','')))
                
        except:
            pass
        
zippedList =  list(zip(years, revenue, c_name, profit))
data = pd.DataFrame(zippedList ,columns = ['year' , 'revenue', 'company', "profit"])  

data.to_csv("f500_history_1.csv")  

