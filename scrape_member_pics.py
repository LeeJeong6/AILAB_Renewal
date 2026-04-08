import requests
from bs4 import BeautifulSoup
import json

url = "https://ailab.kookmin.ac.kr/members"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Wix sites often store image info in specific components. Let's find all images.
    images = soup.find_all('img')
    print(f"Found {len(images)} total images.")
    for i, img in enumerate(images[:20]):
        print(f"[{i}] alt: {img.get('alt', '')}, src: {img.get('src', '')}")
        
    # Let's also search for typical Wix text containers to see proximity to images
    # We'll just dump a small portion of the text to see how it's structured
    text_blocks = soup.find_all(['h2', 'h3', 'p', 'span'])
    # Filtering for those containing names
    print("\nSample name blocks and their parents:")
    for block in text_blocks:
        t = block.get_text(strip=True)
        if 'Soochahn Lee' in t or 'Subin An' in t or 'Juwan Maeng' in t:
            print(f"\n--- Found '{t}' ---")
            print(f"Tag: {block.name}, Class: {block.get('class')}")
            # Look at parent hierarchy to see if images are nearby
            parent = block.parent
            for _ in range(3):
                if parent:
                    imgs = parent.find_all('img')
                    if imgs:
                        print(f"  -> Found {len(imgs)} imgs within {parent.name} (class={parent.get('class')})")
                        for im in imgs:
                            print(f"     src={im.get('src')}")
                        break
                    parent = parent.parent

except Exception as e:
    print(f"Error: {e}")
