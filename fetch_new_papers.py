import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json

papers = [
    "See, Hear, and Understand: Benchmarking Audiovisual Human Speech Understanding in Multimodal Large Language Models",
    "Contamination Detection for VLMs using Multi-Modal Semantic Perturbation",
    "Particle Diffusion Matching: Random Walk Correspondence Search for the Alignment of Standard and Ultra-Widefield Fundus Images"
]

results = []

for title in papers:
    print(f"Searching for: {title}")
    query = urllib.parse.urlencode({'search_query': f'ti:"{title}"'})
    url = f"http://export.arxiv.org/api/query?{query}"
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            entry = root.find('{http://www.w3.org/2005/Atom}entry')
            if entry is not None:
                arxiv_id = ""
                id_tag = entry.find('{http://www.w3.org/2005/Atom}id')
                if id_tag is not None and id_tag.text:
                    arxiv_id = id_tag.text.split('/abs/')[-1].split('v')[0]
                
                published = ""
                pub_tag = entry.find('{http://www.w3.org/2005/Atom}published')
                if pub_tag is not None and pub_tag.text:
                    published = pub_tag.text.split('T')[0]
                    
                authors = [a.find('{http://www.w3.org/2005/Atom}name').text for a in entry.findall('{http://www.w3.org/2005/Atom}author')]
                pdf_link = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                
                print(f"  Found: {arxiv_id} | {published} | {', '.join(authors)}")
                results.append({
                    "title": title,
                    "arxiv_id": arxiv_id,
                    "published": published,
                    "authors": authors,
                    "pdfurl": pdf_link,
                    "htmlurl": f"https://arxiv.org/abs/{arxiv_id}"
                })
            else:
                print("  Not found on arXiv.")
    except Exception as e:
        print(f"  Error: {e}")

with open("new_papers_data.json", "w") as f:
    json.dump(results, f, indent=2)
print("Saved to new_papers_data.json")
