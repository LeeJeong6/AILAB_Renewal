import requests
from bs4 import BeautifulSoup
import re

url = "https://ailab.kookmin.ac.kr/"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a', href=True)
    found = []
    for a in links:
        text = a.get_text(strip=True).lower()
        if 'member' in text or 'people' in text:
            found.append((text, a['href']))
            
    print("Found Member Links:")
    for text, href in found:
        print(f"Text: '{text}', URL: {href}")
        
    # Also print all distinct links to easily scan if 'member' isn't explicitly in the text
    print("\nAll distinct links:")
    distinct_links = set([a['href'] for a in links if a['href'].startswith('http') or a['href'].startswith('/')])
    for l in sorted(distinct_links):
        print(l)
except Exception as e:
    print(f"Error: {e}")
