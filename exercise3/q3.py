import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; research-bot/1.0)"}

response = requests.get("https://allgamblinglist.com/", headers=HEADERS, timeout=15)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

casino_links = [a.get("href") for a in soup.find_all("a", {"rel": "nofollow"}) if a.get("href")]

with open("casino_list.txt", "w") as f:
    f.writelines(f"{link}\n" for link in casino_links)

print(f"Saved {len(casino_links)} links to casino_list.txt")