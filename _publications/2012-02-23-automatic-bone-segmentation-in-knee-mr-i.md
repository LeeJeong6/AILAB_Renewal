---
title: "Automatic bone segmentation in knee MR images using a coarse-to-fine strategy."
collection: publications
date: 2012-02-23
venue: 'SPIE Medical Imaging'
excerpt: 'Sang Hyun Park, **Soochahn Lee**, Il Dong Yun, Sang Uk Lee'
pdfurl: 'https://drive.google.com/file/d/1eX6b1fuOlrH3SbVHbFOJx6kd4ggF9r79/view'
htmlurl: 'https://www.spiedigitallibrary.org/conference-proceedings-of-spie/8314/831405/Automatic-bone-segmentation-in-knee-MR-images-using-a-coarse/10.1117/12.910868.short?SSO=1'
thumbnail: '/images/publications/2012-02-23-automatic-bone-segmentation-in-knee-mr-i-fig1.png'
bibtex: |
    @inproceedings{Park_2012, title={Automatic bone segmentation in knee MR images using a coarse-to-fine strategy}, volume={8314}, ISSN={0277-786X}, url={http://dx.doi.org/10.1117/12.910868}, DOI={10.1117/12.910868}, booktitle={Medical Imaging 2012: Image Processing}, publisher={SPIE}, author={Park, Sang Hyun and Lee, Soochan and Yun, Il Dong and Lee, Sang Uk}, editor={Haynor, David R. and Ourselin, Sébastien}, year={2012}, month=feb, pages={831405} }
citation_mla: |
    Park, Sang Hyun, et al. “Automatic Bone Segmentation in Knee MR Images Using a Coarse-to-Fine Strategy.” Medical Imaging 2012: Image Processing, edited by David R. Haynor and Sébastien Ourselin, vol. 8314, Feb. 2012, p. 831405. Crossref, https://doi.org/10.1117/12.910868.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Sang Hyun Park, **Soochahn Lee**, Il Dong Yun, Sang Uk Lee

> **TL;DR:** An automatic bone segmentation method for knee MR images that uses a coarse-to-fine strategy, starting with a rough localization and progressively refining the boundary.

---

## What this paper is about

Accurate bone segmentation in knee MRI is a prerequisite for many orthopedic applications, from measuring joint space width to planning knee replacement surgery. The difficulty lies in the complex 3D geometry of knee bones and the sometimes ambiguous tissue boundaries in MR images.

## Key idea

![Figure description](/images/publications/2012-02-23-automatic-bone-segmentation-in-knee-mr-i-fig1.png)
*Flow chart of the proposed method. Constrained branch and mincut11 is used to obtain initial segmentation in low resolution level. Then, the optimal aligned atlas is searched from the training set. Finally, segmentation is again conducted as adaptively integrating the shape prior and the appearance prior in the fine segmentation step. We note that the weight $w_g$ is high on the red rectangle including clear boundary, while the $w_g$ is low on the yellow rectangle. The last two steps are repeated until the result of the original resolution is obtained. As iteratively conducting the segmentation and the registration on multiple resolution levels, the performance is enhanced.*

The paper employs a coarse-to-fine strategy: first obtaining an approximate bone region through a coarse segmentation step, then iteratively refining the boundary with more detailed local analysis. This hierarchical approach avoids getting stuck in local optima while keeping computation tractable.

## Why it matters

Building on the group's earlier work on knee bone segmentation (ICIP 2009), this method further improves accuracy and robustness, contributing to the pipeline needed for fully automated analysis of large-scale knee MRI datasets like the Osteoarthritis Initiative.
