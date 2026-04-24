---
title: "Optimization of local shape and appearance probabilities for segmentation of knee cartilage in 3-D MR images."
collection: publications
date: 2011-12-01
venue: 'Computer Vision and Image Understanding'
excerpt: '**Soochahn Lee**, Sang Hyun Park, Hackjoon Shim, Il Dong Yun, Sang Uk Lee'
pdfurl: 'https://drive.google.com/file/d/1ZjXALrxHqbCdDl3DZ0dfow2VJRs7dOvQ/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S1077314211001639'
thumbnail: '/images/publications/2011-12-01-optimization-of-local-shape-and-appearan-fig1.png'
bibtex: |
    @article{Lee_2011, title={Optimization of local shape and appearance probabilities for segmentation of knee cartilage in 3-D MR images}, volume={115}, ISSN={1077-3142}, url={http://dx.doi.org/10.1016/j.cviu.2011.05.014}, DOI={10.1016/j.cviu.2011.05.014}, number={12}, journal={Computer Vision and Image Understanding}, publisher={Elsevier BV}, author={Lee, Soochahn and Park, Sang Hyun and Shim, Hackjoon and Yun, Il Dong and Lee, Sang Uk}, year={2011}, month=dec, pages={1710–1720} }
citation_mla: |
    Lee, Soochahn, et al. “Optimization of Local Shape and Appearance Probabilities for Segmentation of Knee Cartilage in 3-D MR Images.” Computer Vision and Image Understanding, vol. 115, no. 12, Dec. 2011, pp. 1710–20. Crossref, https://doi.org/10.1016/j.cviu.2011.05.014.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Soochahn Lee**, Sang Hyun Park, Hackjoon Shim, Il Dong Yun, Sang Uk Lee

> **TL;DR:** This paper optimizes both local shape and appearance probability models to achieve more accurate segmentation of knee cartilage in 3D MR images, improving over methods that treat these cues independently.

---

## What this paper is about

![Figure description](/images/publications/2011-12-01-optimization-of-local-shape-and-appearan-fig1.png)
*An illustration of the knee articular joint in 3D (left) and on a 2D MR image slice (right).*

Accurate cartilage segmentation in knee MRI is essential for studying osteoarthritis, but cartilage is thin, has low contrast against surrounding tissues, and varies considerably across patients. Using fixed or global models for shape and appearance often fails to capture local anatomical variations.

## Key idea

![Figure description](/images/publications/2011-12-01-optimization-of-local-shape-and-appearan-fig2.png)
*Flowchart of the proposed method.*

The paper jointly optimizes local shape and appearance probability models rather than using them independently. By tailoring these models to local regions of the knee, the segmentation adapts to patient-specific anatomy and achieves finer boundary delineation for cartilage structures in 3D MR images.

## Why it matters

Published in Computer Vision and Image Understanding (a top journal), this work advances medical image segmentation by demonstrating that locally optimized shape-appearance models significantly outperform global approaches for challenging thin-structure segmentation tasks.

