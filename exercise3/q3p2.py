import pandas as pd
# import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
# import urllib
# import re
import datetime 
import sys

#inserting the file manually
# with open('casino_list.txt', 'r') as reader:
#     # Read and print the entire file line by line
#     links = []
#     for line in reader:
#         links.append(line.strip('\n'))
 
#inserting the file as an external arg       
with open(sys.argv[1], 'r') as reader:
    # Read and print the entire file line by line
    links = []
    for line in reader:
        links.append(line.strip('\n'))
        
gambling_words = ['bonus','play',
                 'casino', 'gambling',
                 'spin','spins', 'gamble',
                 'gambles','card', 'cards', 'win',
                 'money', 'slot machines',
                 'slot machine',  'luck', 'spinning']


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}    
        
datetime.datetime.now()        
dic = {}     
for link in range(len(links)):   
    try:
        req = Request(url=links[link], headers=headers) 
        html = str(urlopen(req).read())
    except:
        print('not a valid page at link:', link)
    finally:
        soup = BeautifulSoup(html)
        data = list(soup.findAll(text=True))
    
    website_words = [] 
    for l in range(len(data)):
        website_words.append(data[l].strip().split())
     
    gambling_related_words = [] 
    for i in range(len(website_words)):
        for j in range(len(website_words[i])):
            if (website_words[i][j]).lower() in gambling_words:
                gambling_related_words.append(website_words[i][j].lower())
                dic.update({links[link]: set(gambling_related_words)})
                
datetime.datetime.now()


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

import json
result = json.dumps(dic, default=set_default)  

with open('link.json', 'w') as fp:
    json.dump(result, fp)




