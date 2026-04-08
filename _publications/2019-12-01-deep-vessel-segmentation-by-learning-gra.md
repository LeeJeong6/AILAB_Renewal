---
title: "Deep vessel segmentation by learning graphical connectivity."
collection: publications
date: 2019-12-01
venue: 'Medical Image Analysis'
excerpt: 'Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Kyoung Mu Lee'
codeurl: 'https://github.com/syshin1014/VGN'
pdfurl: 'https://drive.google.com/file/d/1pJdOIJHaheQIqgVZp_BbkewtPsmCFMxh/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S1361841519300982'
bibtex: |
    @article{Shin_2019, title={Deep vessel segmentation by learning graphical connectivity}, volume={58}, ISSN={1361-8415}, url={http://dx.doi.org/10.1016/j.media.2019.101556}, DOI={10.1016/j.media.2019.101556}, journal={Medical Image Analysis}, publisher={Elsevier BV}, author={Shin, Seung Yeon and Lee, Soochahn and Yun, Il Dong and Lee, Kyoung Mu}, year={2019}, month=dec, pages={101556} }
citation_mla: |
    Shin, Seung Yeon, et al. “Deep Vessel Segmentation by Learning Graphical Connectivity.” Medical Image Analysis, vol. 58, Dec. 2019, p. 101556. Crossref, https://doi.org/10.1016/j.media.2019.101556.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Kyoung Mu Lee

> **TL;DR:** A deep learning method for vessel segmentation that learns graphical connectivity between vessel segments, preserving the topological structure of vascular networks.

---

## What this paper is about

Standard pixel-wise segmentation methods often produce fragmented vessel maps with broken connections, which is a serious problem when the downstream task requires understanding the vascular network topology. Vessels form connected tree- or graph-like structures, and preserving that connectivity is essential for meaningful clinical analysis.

## Key idea

Rather than just classifying individual pixels, this method explicitly learns the graphical connectivity between vessel segments. By incorporating connectivity prediction into the deep network, the model produces segmentation results that maintain the structural integrity of the vascular graph, reducing fragmentation and topological errors.

## Why it matters

Published in Medical Image Analysis, this work addresses a fundamental limitation of pixel-wise segmentation for tubular structures. Maintaining vascular connectivity is critical for applications like blood flow simulation, surgical planning, and disease progression tracking.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2019-12-01-deep-vessel-segmentation-by-learning-gra-fig1.png) -->
