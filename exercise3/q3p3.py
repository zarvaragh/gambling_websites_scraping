import sys
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

GAMBLING_WORDS = {
    "bonus", "play", "casino", "gambling", "spin", "spins", "gamble",
    "gambles", "card", "cards", "win", "money", "slot", "luck", "spinning",
    "bet", "betting",
}
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

links = sys.argv[1:]

dic = {}
for link in links:
    try:
        req = Request(url=link, headers=HEADERS)
        html = urlopen(req, timeout=10).read()
        soup = BeautifulSoup(html, "html.parser")
        words = {w.lower() for w in soup.get_text().split()}
        is_gambling = bool(words & GAMBLING_WORDS)
        dic[link] = "Gambling site" if is_gambling else "Non-gambling site"
    except Exception as e:
        dic[link] = f"Error: {e}"

print(json.dumps(dic, indent=2))