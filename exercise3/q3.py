import requests
from bs4 import BeautifulSoup


response = requests.get('https://allgamblinglist.com/')
soup = BeautifulSoup(response.text, 'html.parser')
# casino_links = soup.findAll("li", {"rel":"nofollow"})
# links = soup.select(".attachment-post-thumbnail")
# links[0].attrs
# links[10].get('href', 0)
casino_links = []
for a in soup.find_all('a', { 'rel': 'nofollow'}):
    casino_links.append(a.get('href'))

with open('casino_list.txt', 'w') as f:
    for link in casino_links:
        f.write("%s\n" % link)
    # f.write(casino_links)


