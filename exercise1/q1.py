import sys
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import tldextract


def extract_info_url(url):
    _, domain, tld = tldextract.extract(url)
    parsed = urlparse(url)
    return {
        "TLD": tld,
        "DOMAIN": f"{domain}.{tld}",
        "HOSTNAME": parsed.hostname or "",
        "PATH": parsed.path,
        "LINKS": "empty",
    }


def categorize_links(links, host_name, domain):
    same_hostname, same_domain, other_domains = [], [], []
    for link in links:
        if not isinstance(link, str):
            continue
        _, d, _ = tldextract.extract(link)
        h = urlparse(link).hostname or ""
        if h and h == host_name:
            same_hostname.append(link)
        elif d and d == domain:
            same_domain.append(link)
        else:
            other_domains.append(link)
    return {"same host": same_hostname, "same domain": same_domain, "others": other_domains}


url_input = sys.argv[1]
info = extract_info_url(url_input)
print(info)
print("*" * 100)

_, domain, _ = tldextract.extract(url_input)
host_name = urlparse(url_input).hostname or ""

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; research-bot/1.0)"})
response = session.get(url_input, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

links = [a.get("href") for a in soup.find_all("a")]
print(categorize_links(links, host_name, domain))