import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib
import re
import datetime 
import json
import sys
 
    
gambling_words = ['bonus','play',
                 'casino', 'gambling',
                 'spin','spins', 'gamble',
                 'gambles','card', 'cards', 'win',
                 'money', 'slot machines',
                 'slot machine',  'luck', 'spinning', 'bet', 'betting']


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}    
        
#inserting the links manually 
# links = ['https://www.freecodecamp.org/news/http-error-403-forbidden-what-it-means-and-how-to-fix-it/',
#           'https://www.bet365.com/#/HO/']

#inserting the links as an external arg
links = [sys.argv[1]]

dic = {}
def distinguish_websites ():
    for link in range(len(links)):   
        try:
            req = Request(url=links[link], headers=headers) 
            html = str(urlopen(req).read())
        except:
            print('not a valid page at link:', link)
        finally:
            soup = BeautifulSoup(html)
            data = soup.findAll(text=True)
        
        website_words = [] 
        for l in range(len(data)):
            website_words.append(data[l].strip().split())
    
        for i in range(len(website_words)):
            for j in range(len(website_words[i])):
                if ((website_words[i][j]).lower() in gambling_words):
                    dic.update({links[link]: 'Gambling site'})
                    return True
                else:
                    dic.update({links[link]: 'non-Gambling site'})
                    
distinguish_websites()
print(dic)
                      