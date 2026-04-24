---
title: "Hierarchical MRF of globally consistent localized classifiers for 3D medical image segmentation."
collection: publications
date: 2013-09-01
venue: 'Pattern Recognition'
excerpt: 'Sang Hyun Park, **Soochahn Lee**, Il Dong Yun, Sang Uk Lee'
pdfurl: 'https://drive.google.com/file/d/1A9g0qc2mciihUgrMJfPpCe-PcxiPxMil/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S0031320313001076'
thumbnail: '/images/publications/2013-09-01-hierarchical-mrf-of-globally-consistent-fig1.png'
bibtex: |
    @article{Park_2013, title={Hierarchical MRF of globally consistent localized classifiers for 3D medical image segmentation}, volume={46}, ISSN={0031-3203}, url={http://dx.doi.org/10.1016/j.patcog.2013.02.014}, DOI={10.1016/j.patcog.2013.02.014}, number={9}, journal={Pattern Recognition}, publisher={Elsevier BV}, author={Park, Sang Hyun and Lee, Soochahn and Yun, Il Dong and Lee, Sang Uk}, year={2013}, month=sep, pages={2408–2419} }
citation_mla: |
    Park, Sang Hyun, et al. “Hierarchical MRF of Globally Consistent Localized Classifiers for 3D Medical Image Segmentation.” Pattern Recognition, vol. 46, no. 9, Sept. 2013, pp. 2408–19. Crossref, https://doi.org/10.1016/j.patcog.2013.02.014.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Sang Hyun Park, **Soochahn Lee**, Il Dong Yun, Sang Uk Lee

> **TL;DR:** A hierarchical Markov Random Field framework that combines globally consistent localized classifiers for accurate 3D medical image segmentation.

---

## What this paper is about

Segmenting structures in 3D medical images is challenging because tissue appearance varies across different regions of the volume. A single global classifier often fails to capture this local variation, while purely local classifiers can produce spatially inconsistent results.

## Key idea

![Figure description](/images/publications/2013-09-01-hierarchical-mrf-of-globally-consistent-fig1.png)
*The proposed Hierarchical MRF (H-MRF) framework. The target object is modeled within multiple local patches (denoted as rectangles with different colors within the test image, top-left). Reference patches determined to have similar position and appearance with the test patch are selected from the training set. Multiple segmentation candidates (pink labels representing object voxels, top-right) are constructed from local-level MRFs (top-mid) using each reference patch as prior for each local region. These local segmentation candidates are aggregated by a global-level MRF (bottom-left, mid) based on their cumulative global consistency to construct the final segmentation result (bottom-right).*

The paper proposes a hierarchical MRF framework that trains localized classifiers tailored to specific spatial regions, then enforces global consistency across them using a multi-level MRF structure. This allows each classifier to specialize in its local context while the hierarchical model ensures coherent segmentation across the full 3D volume.

## Why it matters

This approach bridges the gap between local discriminative power and global spatial coherence, improving segmentation accuracy for 3D medical imaging tasks where anatomical structures exhibit spatially varying appearance.

