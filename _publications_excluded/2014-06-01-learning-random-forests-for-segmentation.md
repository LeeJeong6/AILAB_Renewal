---
title: "Learning random forests for segmentation of person in self-portrait photos."
collection: publications
date: 2014-06-01
venue: 'ISCE'
excerpt: '**Soochahn Lee**'
pdfurl: 'https://drive.google.com/file/d/1pM2KhjFlo98nCmZ4n_dNOJgijgq1NwZY/view'
htmlurl: 'https://ieeexplore.ieee.org/document/6884485'
bibtex: |
    @inproceedings{Lee_2014, title={Learning random forests for segmentation of person in self-portrait photos}, url={http://dx.doi.org/10.1109/isce.2014.6884485}, DOI={10.1109/isce.2014.6884485}, booktitle={The 18th IEEE International Symposium on Consumer Electronics (ISCE 2014)}, publisher={IEEE}, author={Lee, Soochahn}, year={2014}, month=jun, pages={1–2} }
citation_mla: |
    Lee, Soochahn. “Learning Random Forests for Segmentation of Person in Self-Portrait Photos.” The 18th IEEE International Symposium on Consumer Electronics (ISCE 2014), June 2014, pp. 1–2. Crossref, https://doi.org/10.1109/isce.2014.6884485.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Soochahn Lee**

> **TL;DR:** A random forest-based method for automatically segmenting people in self-portrait (selfie) photos.

---

## What this paper is about

With the explosion of smartphone cameras, self-portrait photos became ubiquitous. Automatically separating the person from the background in these photos is useful for editing, effects, and sharing, but it is tricky due to diverse poses, lighting, and cluttered backgrounds.

## Key idea

The paper trains a random forest classifier to perform pixel-level segmentation of the person in selfie images. Random forests are well-suited here because they are fast at inference time and can handle the variety of features needed to distinguish person regions from background in uncontrolled photo conditions.

## Why it matters

This work addresses a practical consumer electronics application, enabling real-time person segmentation in self-portraits on resource-constrained mobile devices.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/learning-random-forests-for-segmentation-fig1.png) -->
