import urllib.request
import urllib.parse
import json
import glob
import re
import time

files = glob.glob('_publications/*.md')
success = 0
failed = []

print("Booting up Crossref API BibTeX aggregator...", flush=True)

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'bibtex:' in content:
        continue
        
    title_match = re.search(r'title:\s*"(.*?)"', content)
    if not title_match:
        continue
        
    title = title_match.group(1).replace('\\"', '"')
    print(f"-> Querying Crossref for: {title[:50]}...", flush=True)
    
    try:
        query = urllib.parse.quote(title)
        url = f"https://api.crossref.org/works?query.title={query}&rows=1&select=DOI,title"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
        items = data.get('message', {}).get('items', [])
        if not items:
            print("   [ERR] No results found on Crossref.", flush=True)
            failed.append(title)
            continue
            
        item = items[0]
        doi = item.get('DOI')
        if not doi:
            print("   [ERR] No DOI found.", flush=True)
            failed.append(title)
            continue
            
        res_title_words = set(item.get('title', [''])[0].lower().split())
        query_title_words = set(title.lower().split())
        
        if len(query_title_words.intersection(res_title_words)) >= 2 or len(query_title_words) <= 2:
            bib_url = f"https://doi.org/{doi}"
            bib_req = urllib.request.Request(bib_url, headers={'Accept': 'application/x-bibtex'})
            try:
                with urllib.request.urlopen(bib_req, timeout=10) as bib_res:
                    bibtex_str = bib_res.read().decode('utf-8').strip()
            except BaseException as e:
                print(f"   [ERR] DOI resolution failed: {e}", flush=True)
                failed.append(title)
                continue
                
            if bibtex_str:
                bib_formatted = "\n".join(["    " + line for line in bibtex_str.split("\n")])
                inject = f"\nbibtex: |\n{bib_formatted}\n---"
                new_content = re.sub(r'\n---(?!.*\n---)', inject, content, count=1, flags=re.DOTALL)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"   [OK] Injected BibTex for {title[:30]}", flush=True)
                success += 1
            else:
                print("   [ERR] Empty BibTeX", flush=True)
                failed.append(title)
        else:
            print(f"   [SKIP] Title mismatch. Found: {item.get('title', [''])[0]}", flush=True)
            failed.append(title)
            
        time.sleep(1)
        
    except Exception as e:
        print(f"   [ERR] Exception: {e}", flush=True)
        failed.append(title)

print(f"\nFinished! Successfully fetched {success} BibTeX items.", flush=True)
if failed:
    print(f"Failed to fetch {len(failed)} items.", flush=True)
