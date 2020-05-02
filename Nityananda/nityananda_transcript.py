# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:29:57 2020

@author: Akshay
"""

import requests
import zipfile
from io import BytesIO 
import csv
import re
import json
from bs4 import BeautifulSoup

url = 'http://nithyananda.com/video/all?page=25&order=field_date_value&sort=asc&tid_op=not&tid_satsang_topic[1348]=1348&field_date_value_op=%3D&title_op=contains&title_video_title=&field_description_english_value_op=contains&field_description_english_value=&field_transcription_value_op=contains&field_transcription_value=#gsc.tab=0'
url = 'http://nithyananda.com/video/all?page=1#gsc.tab=0'

url = 'http://nithyananda.com/video/all?page=1#gsc.tab=0'
url = 'http://nithyananda.com/video/all?page=1#gsc.tab=0'
url = 'http://nithyananda.com/video/all?page=3#gsc.tab=0'
r = requests.get(url)
type(r)
data = r.text

links = []

def getLinks(url):
    html_page = requests.get(url)
    html_text =  html_page.text
    soup = BeautifulSoup(html_text)
    #links = []

    table = soup.find('table', {'class':"views-table cols-2"})
    table_contents = table.findAll('td')
    for table_contet in table_contents:
        try:
            links.append('http://nithyananda.com'+table_contet.find('a')['href'])
        except:
            pass
    
    return links

link_list = []
for i in range(1,34):
    url = 'http://nithyananda.com/video/all?page='+str(i)+'#gsc.tab=0'
    try:
        link_list.append(getLinks(url))
    except:
        pass
    

#file = zipfile.ZipFile(BytesIO(r.content))
len(link_list)
len(link_list[1][2])

corpus = str()

    
    
for lst in link_list:
    for transcript_url in lst:
        corpus = str()
        try:
            html_page = requests.get(transcript_url)
            html_text =  html_page.text
            text = BeautifulSoup(html_text,"lxml").get_text(strip=True)
            start = text.find('Full transcript')
            end = text.find('Full transcript',text.find('Full transcript')+1)
            corpus =  corpus +'\n-----~---------\n'+ text[start:end]
            with open("Output.txt", "a+", encoding="utf-8") as text_file:
                text_file.write(corpus)
        except:
            pass


        
    

transcript_url = 'http://nithyananda.com/video/we-are-nation-integrity'
html_page = requests.get(transcript_url)
html_text =  html_page.text
text = BeautifulSoup(html_text,"lxml").get_text(strip=True)
start = text.find('Full transcript')
end = text.find('Full transcript',text.find('Full transcript')+1)
corpus =  corpus +'\n-----~---------\n'+ text[start:end]


nltk.clean_html(soup.getText())


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

wpage = requests.get(url)
data = wpage.text
soup = BeautifulSoup(data, 'lxml')
table = soup.find('table', attrs={'class':regex})

tr_comps = table.findAll('tr')





from __future__ import print_function
from keras.callbacks import LambdaCallback
from keras.models import Model, load_model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking
from keras.layers import LSTM
from keras.utils.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
from shakespeare_utils import *
import sys
import io


print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

model.fit(x, y, batch_size=128, epochs=1, callbacks=[print_callback])

generate_output()

https://github.com/keras-team/keras/blob/master/examples/lstm_text_generation.py