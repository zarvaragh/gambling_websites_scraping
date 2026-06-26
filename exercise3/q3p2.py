import sys
import json
import datetime
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

with open(sys.argv[1]) as f:
    links = [line.strip() for line in f if line.strip()]

GAMBLING_WORDS = {
    "bonus", "play", "casino", "gambling", "spin", "spins", "gamble",
    "gambles", "card", "cards", "win", "money", "slot", "luck", "spinning",
}
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

dic = {}
print(f"Started: {datetime.datetime.now()}")

for link in links:
    try:
        req = Request(url=link, headers=HEADERS)
        html = urlopen(req, timeout=10).read()
        soup = BeautifulSoup(html, "html.parser")
        words = {w.lower() for token in soup.get_text().split() for w in [token.strip()]}
        found = words & GAMBLING_WORDS
        if found:
            dic[link] = list(found)
    except Exception as e:
        print(f"Skipped {link}: {e}")

print(f"Finished: {datetime.datetime.now()}")

with open("link.json", "w") as fp:
    json.dump(dic, fp, indent=2)