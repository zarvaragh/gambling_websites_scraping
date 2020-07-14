from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import sys
import tldextract


def extract_info_url(url):
    _, domain, tld= tldextract.extract(url)
    _, host_name, path, _, _, _ =urlparse(url)
    x = dict(TLD=tld, DOMAIN=domain+'.'+tld, HOSTNAME=host_name, PATH=path, LINKS='empty' )
    return x
    
#print manually    
# print(extract_info_url('http://test.testdomain.org/xyz'))

#print by passing external Argument 
url_input = (sys.argv[1])
print(extract_info_url(url_input))
print('*'*100)



#print manually
# _, domain, tld= tldextract.extract('http://news.google.com.my/')
# _, host_name, path, _, _, _ =urlparse('http://news.google.com.my/')
# url = "http://news.google.com.my/"

#print by passing external Argument
_, domain, tld= tldextract.extract(url_input)
_, host_name, path, _, _, _ =urlparse(url_input)
url = url_input


page = requests.get(url)    
data = page.text
soup = BeautifulSoup(data)

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
    print(link.get('href'))

same_hostname=[]
same_domain = []
other_domains = []

type(links[0])==str
for i in range(len(links)):
    if (type(links[i])==str):
        _, domain2, _= tldextract.extract(links[i])
        _, host_name2, _, _, _, _ =urlparse(links[i])
        # print (host_name2)
        if host_name2 == host_name and host_name2 != '':
            same_hostname.append(links[i])
        if domain2 == domain and domain2 != '':
            same_domain.append(links[i])
        else:
            other_domains.append(links[i])
    else:
        pass

#just add them dictionary wise 
    
    
thisdict =	{
  "same host": same_hostname,
  "same domain": same_domain,
  "others": other_domains
}

print(thisdict)
    
