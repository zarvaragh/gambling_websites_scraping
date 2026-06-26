# Gambling Websites Scraping

A set of web scraping exercises that extract and analyse data from gambling and casino websites — domains, TLDs, hostnames, link graphs, and gambling keyword detection.

## Requirements

```bash
pip install requests beautifulsoup4 tldextract pandas lxml
```

## Exercises

### Exercise 1 — URL Analysis (`exercise1/q1.py`)

Parses a URL and extracts structural information, then scrapes all links from the page and categorises them by domain relationship.

```bash
python exercise1/q1.py https://example-casino.com
```

**Output:**
```json
{
  "TLD": "com",
  "DOMAIN": "example-casino.com",
  "HOSTNAME": "example-casino.com",
  "PATH": "/",
  "same host": [...],
  "same domain": [...],
  "others": [...]
}
```

---

### Exercise 2 — JSON Data Processing (`exercise2/q2-part1.py`)

Reads a JSON file of user records, groups them by last name, and produces a structured summary with age, address, and occupation distributions.

```bash
python exercise2/q2-part1.py exercise2/data.json
```

---

### Exercise 3 — Gambling Site Classifier

**Step 1 — Collect casino links** (`q3.py`):
```bash
python exercise3/q3.py        # scrapes casino_list.txt
```

**Step 2 — Keyword extraction from each site** (`q3p2.py`):
```bash
python exercise3/q3p2.py exercise3/casino_list.txt   # produces link.json
```

**Step 3 — Binary classification** (`q3p3.py`):
```bash
python exercise3/q3p3.py https://example.com
```
Returns `"Gambling site"` or `"Non-gambling site"` based on presence of gambling-related keywords.

## Tech Stack

| Library | Purpose |
|---------|---------|
| `requests` | HTTP requests with session and proper headers |
| `beautifulsoup4` | HTML parsing (`html.parser`) |
| `tldextract` | Accurate TLD/domain/subdomain extraction |
| `pandas` | JSON → CSV transformation |