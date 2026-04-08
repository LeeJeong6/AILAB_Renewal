import os
import requests
import json
import glob
import shutil

base_path = "/Users/sclee/Documents/001_RESEARCH/001_AILab_Kookmin/www/kookmin-ee-ailab.github.io"
img_dir = os.path.join(base_path, "images", "gallery")
md_dir = os.path.join(base_path, "_gallery")

MAPPINGS = [
    {"title": "2025 봄", "url": "https://static.wixstatic.com/media/96c9f6_50d877eec85646f7b4c83e1c610fc179~mv2.jpeg"},
    {"title": "2025 초여름", "url": "https://static.wixstatic.com/media/96c9f6_d4d1012842804ef3a812d6b8b330a651~mv2.jpg"},
    {"title": "2024 CVPR", "url": "https://static.wixstatic.com/media/96c9f6_da849477a06b40dfbfe3b65a23570d6e~mv2.jpg"},
    {"title": "kccv2024", "url": "https://static.wixstatic.com/media/b03ab1_c583466d1269457db6d36adb193843f1~mv2.jpg"},
    {"title": "2024 여름 MT", "url": "https://static.wixstatic.com/media/b03ab1_13b007a151f04e09a68e2e3362bdad5a~mv2.jpg"},
    {"title": "2024 봄", "url": "https://static.wixstatic.com/media/b03ab1_54c80e4968e1472b83140fb14af6cd23~mv2.jpeg"},
    {"title": "2023 겨울 MT", "url": "https://static.wixstatic.com/media/b03ab1_830985a23c1d4ab9a15619c5db8823da~mv2.jpeg"},
    {"title": "2023 겨울 MT", "url": "https://static.wixstatic.com/media/b03ab1_b34cc821ed294ef09703c67a938dad1d~mv2.jpeg"},
    {"title": "2023 봄", "url": "https://static.wixstatic.com/media/b03ab1_28b8df30360247b5be7ff6812e59146c~mv2.png"},
    {"title": "2023 겨울 MT", "url": "https://static.wixstatic.com/media/b03ab1_54f19bc9e7e54a4699585ba9df6d7e96~mv2.jpeg"},
    {"title": "2023 CVPR", "url": "https://static.wixstatic.com/media/b03ab1_91cab8996e0c4b76a1316627ebd08662~mv2.jpeg"},
    {"title": "2022 봄", "url": "https://static.wixstatic.com/media/b03ab1_9254639eb9e44d7fb399d5b77e8c048a~mv2.jpg"},
    {"title": "2022 CVPR", "url": "https://static.wixstatic.com/media/b03ab1_80ce00b3e28d478b8bb147c1fedc1475~mv2.jpeg"}
]

# Wipe old artifacts completely
for f in glob.glob(os.path.join(md_dir, "*.md")): os.remove(f)
for f in glob.glob(os.path.join(img_dir, "*.*")): os.remove(f)

for idx, metadata in enumerate(MAPPINGS):
    url = metadata["url"]
    title = metadata["title"]
    
    sanitized_title = title.replace(" ", "-").lower()
    ext = url.split(".")[-1]
    order_val = idx + 1
    
    img_filename = f"{order_val:02d}-{sanitized_title}.{ext}"
    img_path = os.path.join(img_dir, img_filename)
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(f"Error downlaoding {url}: {e}")

    md_filename = f"{order_val:02d}-{sanitized_title}.md"
    md_path = os.path.join(md_dir, md_filename)
    
    relative_img_path = f"/images/gallery/{img_filename}"
    permalink = f"/gallery/{sanitized_title}-{order_val}/"
    
    content = f"""---
title: "{title}"
order: {order_val}
permalink: {permalink}
categories:
  - gallery
---

<img src="{{{{ base_path }}}}{relative_img_path}" style="border-radius: 8px; margin-top: 15px; width: 100%;">
"""
    with open(md_path, 'w') as f:
        f.write(content)
        
print("Wix replication migration successfully finished!")
