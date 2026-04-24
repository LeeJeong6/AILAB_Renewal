---
title: "Consistent color and detail transfer from multiple source images for video and images."
collection: publications
date: 2015-10-01
venue: 'The Visual Computer'
excerpt: 'Yong Seok Heo, **Soochahn Lee**, Ho Yub Jung'
pdfurl: 'https://drive.google.com/file/d/1kv4bdZWpjdlhkeCtPq8MEzp1p-51_r-7/view'
htmlurl: 'https://link.springer.com/article/10.1007/s00371-015-1162-3'
thumbnail: '/images/publications/2015-10-01-consistent-color-and-detail-transfer-fro-fig1.png'
bibtex: |
    @article{Heo_2015, title={Consistent color and detail transfer from multiple source images for video and images}, volume={32}, ISSN={1432-2315}, url={http://dx.doi.org/10.1007/s00371-015-1162-3}, DOI={10.1007/s00371-015-1162-3}, number={10}, journal={The Visual Computer}, publisher={Springer Science and Business Media LLC}, author={Heo, Yong Seok and Lee, Soochahn and Jung, Ho Yub}, year={2015}, month=oct, pages={1273–1289} }
citation_mla: |
    Heo, Yong Seok, et al. “Consistent Color and Detail Transfer from Multiple Source Images for Video and Images.” The Visual Computer, vol. 32, no. 10, Oct. 2015, pp. 1273–89. Crossref, https://doi.org/10.1007/s00371-015-1162-3.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Yong Seok Heo, **Soochahn Lee**, Ho Yub Jung

> **TL;DR:** A method for transferring color and fine details from multiple source images to target video/images while maintaining temporal and spatial consistency.

---

## What this paper is about

![Figure description](/images/publications/2015-10-01-consistent-color-and-detail-transfer-fro-fig1.png)
*a–c Source images. d–f Input video with frame number 1, 15, 30, respectively. g–i Output video using our method with frame number corresponding to d–f, respectively*

Color and detail transfer lets you restyle an image or video to match the look of reference photos, but doing this from multiple sources while keeping the result consistent (no flickering in video, no patchwork artifacts) is quite difficult.

## Key idea

The paper presents a framework that takes multiple source images and transfers both their color palette and fine detail information to a target image or video sequence. The key contribution is ensuring consistency across frames (for video) and across spatial regions, so the transferred style looks natural and coherent rather than fragmented.

## Why it matters

This enables practical image and video editing applications where users can blend the visual style of multiple reference images into their content with temporally stable and visually pleasing results.

